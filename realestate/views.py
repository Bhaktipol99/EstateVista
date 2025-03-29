from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile, Property,SavedProperty
from .forms import PropertyForm
from django.db.models import Q
from .models import Message,Notification
from .forms import MessageForm
from .models import Order, Property, Payment
from django.contrib import messages
from django.db import transaction

# Home view
def home(request):
    return render(request, 'home.html')


# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            messages.success(request, "Login successful! Click OK to continue.")
            return redirect("login")  
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


# Register view
def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        name = request.POST["name"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        gender = request.POST["gender"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("register_view")  # Stay on register page

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect("register_view")  # Stay on register page

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = name
        user.save()

        Profile.objects.create(user=user, mobile=mobile, gender=gender)

        messages.success(request, "Registration successful! Click OK to log in.")
        return redirect("register_view")  

    return render(request, "register.html")



# About view
def about(request):
    return render(request, 'about.html')

# Contact view
def contact(request):
    return render(request, 'contact.html')

# Dashboard view (Requires login)
@login_required
def dashboard(request):
    user_properties = Property.objects.filter(owner=request.user).order_by('-created_at')[:5]
    recent_properties = Property.objects.all().order_by('-created_at')[:5]  # All new listings

    return render(request, 'dashboard.html', {
        'user_properties': user_properties,
        'recent_properties': recent_properties
    })


# Logout view
def logout_view(request):
    logout(request)
    return redirect("home")  # Redirect to home after logout


# Add property
def add_property(request):
    storage = messages.get_messages(request)
    storage.used = True 
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property_instance = form.save(commit=False)
            property_instance.owner = request.user  # Assign logged-in user as the owner
            property_instance.save()
            return redirect('property_list')  # Redirect to property list page
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})


# Edit Property view
@login_required
def edit_property(request, pk):  # Ensure 'pk' is used
    property = get_object_or_404(Property, pk=pk, owner=request.user)  # Get the property by primary key
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'edit_property.html', {'form': form})

# Delete Property view
@login_required
def delete_property(request, property_id):
    property = get_object_or_404(Property, id=property_id, owner=request.user)  # Ensure ownership

    if request.method == 'POST':
        property.delete()
        messages.success(request, 'Property deleted successfully!')
        return redirect('property_list')

    return render(request, 'delete_property.html', {'property': property})

# Property Detail view
def property_detail(request, id):
    property_obj = get_object_or_404(Property, id=id)
    return render(request, 'property_detail.html', {'property': property_obj})


# Property List view
@login_required
def property_list(request):
    properties = Property.objects.filter(owner=request.user)  # Show only logged-in user's properties
    return render(request, 'property_list.html', {'properties': properties})

@login_required
def other_users_properties(request):
    properties = Property.objects.exclude(owner=request.user)  # Show properties not owned by the logged-in user
    return render(request, 'other_users_properties.html', {'properties': properties})

# Save Property view
@login_required
def save_property(request, property_id):
    if request.method == "POST":
        property_obj = get_object_or_404(Property, id=property_id)

        # Check if the property is already saved
        saved, created = SavedProperty.objects.get_or_create(user=request.user, property=property_obj)

        if created:
            print(f" Property  saved successfully!")  
        else:
            print(f" Property  was already saved.")  

        return redirect('saved_properties')

    print("⚠️ Invalid request method (should be POST)") 
    return redirect('saved_properties')


def saved_properties(request):  
    saved_properties = SavedProperty.objects.filter(user=request.user)
    return render(request, 'saved_properties.html', {'saved_properties': saved_properties}) 

def save_unsave_property(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)

    saved_property = SavedProperty.objects.filter(user=request.user, property=property_obj)
    
    if saved_property.exists():
        saved_property.delete()  
        print(f" Property unsaved.")
    else:
        SavedProperty.objects.create(user=request.user, property=property_obj)  
        print(f" Property  saved.")

    return redirect('saved_properties')


def search_properties(request):
    query = request.GET.get('query', '')
    property_type = request.GET.get('property_type', '')
    status = request.GET.get('status', '')
    price_range = request.GET.get('price_range', '')

    # If no search query is given, just show the search form
    if not query and not property_type and not status and not price_range:
        return render(request, 'search.html')  # This will show the search form first

    properties = Property.objects.exclude(owner=request.user)
    # Start filtering properties
    properties = Property.objects.all()

    if query:
        properties = properties.filter(name__icontains=query) | properties.filter(location__icontains=query)  # Search by name

    if property_type:
        properties = properties.filter(property_type=property_type)

    if status:
        properties = properties.filter(status=status)

    if price_range:
        min_price, max_price = price_range.split('-') if '-' in price_range else (price_range[:-1], None)
        if min_price:
            properties = properties.filter(price__gte=min_price)
        if max_price:
            properties = properties.filter(price__lte=max_price)

    return render(request, 'search_results.html', {'properties': properties})



# View to send a message
@login_required
def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            # Create Notification for receiver
            Notification.objects.create(
                user=message.receiver,
                message=f"You have a new message from {message.sender}",
                link="/messages/"
            )

            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'send_message.html', {'form': form})

# View for inbox (received messages)
@login_required
def inbox(request):
    received_messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'inbox.html', {'messages': received_messages})

# View for sent messages
@login_required
def sent_messages(request):
    sent_messages = Message.objects.filter(sender=request.user).order_by('-timestamp')
    return render(request, 'sent_message.html', {'messages': sent_messages})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
        
# View to display notifications
@login_required
def notifications(request):
    user_notifications = Notification.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'notifications.html', {'notifications': user_notifications})

# Mark notification as read
@login_required
def mark_notification_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect(notification.link if notification.link else 'notifications')

@login_required
def other_users_properties(request):
    # Get properties created by users other than the logged-in user
    properties = Property.objects.exclude(owner=request.user)

    return render(request, 'other_users_properties.html', {'properties': properties})

@login_required
def buy_property(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)

    # Ensure 'status' exists and check it correctly
    if hasattr(property_obj, 'status') and property_obj.status.lower().strip() == "available":
        property_obj.status = "sold"
        property_obj.save()

    return redirect('other_users_properties')


# Profile view
def profile_view(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)  # Ensure profile exists

    return render(request, "profile.html", {"user": user, "profile": profile})

# Edit Profile view
def edit_profile_view(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)  

    if request.method == "POST":
        user.username = request.POST.get("username", user.username)
        user.email = request.POST.get("email", user.email)
        profile.mobile = request.POST.get("mobile", profile.mobile)
        profile.gender = request.POST.get("gender", profile.gender)

        if 'profile_image' in request.FILES:
            profile.image = request.FILES['profile_image'] 

        user.save()
        profile.save()
        messages.success(request, "Profile updated successfully!")
        return redirect("profile")  

    return render(request, "edit_profile.html", {"profile": profile})


# Change Password view
def change_password_view(request):
    return render(request, 'change_password.html')


def buy_now(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)

    # Create a pending order (status: "pending", not sold yet)
    order = Order.objects.create(
        user=request.user,
        property=property_obj,
        total_amount=property_obj.price,
        status='pending'  # Do NOT mark as sold yet
    )

    # Redirect to the checkout page with the order ID
    return redirect('checkout_page', order_id=order.id)


def checkout_page(request, property_id):
    property = get_object_or_404(Property, id=property_id)

    # Fix: Ensure total_amount is not null
    order, created = Order.objects.get_or_create(
        property=property, 
        user=request.user, 
        status="Pending",
        defaults={'total_amount': property.price}  # Set the default price
    )

    return render(request, 'checkout.html', {'order': order, 'property': property})


# @login_required
# def payment_page(request, property_id):
#     try:
#         property_obj = get_object_or_404(Property, id=property_id)

#         if property_obj.status == 'sold':
#             messages.warning(request, "This property has already been sold.")
#             return redirect('other_users_properties')

#         if request.method == "POST":
#             selected_payment_method = request.POST.get("payment_method")

#             # Simulate a successful payment
#             payment_successful = True  

#             if payment_successful:
#                 try:
#                     with transaction.atomic():
#                         # Create a payment record
#                         payment = Payment.objects.create(
#                             user=request.user,
#                             property=property_obj,
#                             amount=property_obj.price,
#                             payment_method=selected_payment_method,
#                             status="successful"
#                         )

#                         # Create an order record
#                         order = Order.objects.create(
#                             user=request.user,
#                             property=property_obj,
#                             status="completed",
#                             total_amount=property_obj.price
#                         )

#                         # Now update the property status
#                         property_obj.status = 'sold'
#                         property_obj.save()

#                     messages.success(request, f"Payment successful using {selected_payment_method}!")
#                     return redirect('payment_success', property_id=property_obj.id)

#                 except Exception as db_error:
#                     messages.error(request, f"Database error: {db_error}")
#                     return redirect('other_users_properties')

#             else:
#                 messages.error(request, "Payment failed! Please try again.")
#                 return render(request, 'payment_transaction.html', {'property': property_obj})

#         return render(request, 'payment_transaction.html', {'property': property_obj})

#     except Exception as e:
#         messages.error(request, f"An error occurred: {str(e)}")
#         return redirect('other_users_properties')

@login_required
def payment_page(request, property_id):
    try:
        property_obj = get_object_or_404(Property, id=property_id)

        if property_obj.status == 'sold':
            messages.warning(request, "This property has already been sold.")
            return redirect('other_users_properties')

        if request.method == "POST":
            selected_payment_method = request.POST.get("payment_method")
            print(f"Payment method selected: {selected_payment_method}")

            # Simulate a successful payment
            payment_successful = True  

            if payment_successful:
                try:
                    with transaction.atomic():
                        payment = Payment.objects.create(
                            user=request.user,
                            property=property_obj,
                            amount=property_obj.price,
                            payment_method=selected_payment_method,
                            status="successful"
                        )
                        print(f"Payment created: {payment}")

                        order = Order.objects.create(
                            user=request.user,
                            property=property_obj,
                            status="completed",
                            total_amount=property_obj.price
                        )
                        print(f"Order created: {order}")

                        property_obj.status = 'sold'
                        property_obj.save()
                        print(f"Property status updated: {property_obj.status}")

                    messages.success(request, f"Payment successful using {selected_payment_method}!")
                    return redirect('payment_success', property_id=property_obj.id)

                except Exception as db_error:
                    print(f"Database error: {db_error}")
                    messages.error(request, f"Database error: {db_error}")
                    return redirect('property_list')

            else:
                messages.error(request, "Payment failed! Please try again.")
                return render(request, 'payment_transaction.html', {'property': property_obj})

        return render(request, 'payment_transaction.html', {'property': property_obj})

    except Exception as e:
        print(f"Error: {e}")
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('property_list')

    
@login_required
def payment_success(request, property_id):
    try:
        # Fetch the property using the property_id
        property_obj = get_object_or_404(Property, id=property_id)

        if property_obj.status != 'sold':
            messages.warning(request, "This property has not been marked as sold yet.")
            return redirect('other_users_properties')

        messages.success(request, "Payment successful! The property is now marked as Sold.")
        return render(request, 'payment_success.html', {'property': property_obj})

    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('other_users_properties')
    
def available_properties(request):
    # Get all properties, regardless of whether they are sold or available
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})