from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import uuid

# User Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    image = models.ImageField(
        upload_to='profile_pics/', 
        default='default.jpg', 
        validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )

    def __str__(self):
        return self.user.username


# Property Model
class Property(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='property_images/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
    ('available', 'Available'),   # Open for sale or rent
    ('sold', 'Sold'),            # Property has been sold
    ('rented', 'Rented'),        # Property is rented
    ('pending', 'Pending'),      # Offer is being processed
], default='Available')
    bedrooms = models.PositiveIntegerField(default=1)
    bathrooms = models.PositiveIntegerField(default=1)
    area_sqft = models.PositiveIntegerField(help_text="Total area in square feet", null=True, blank=True)
    property_type = models.CharField(max_length=50, choices=[
        ('apartment', 'Apartment'),
        ('villa', 'Villa'),
        ('office', 'Office'),
    ], default='apartment')

    # ✅ Add this field to track when the property was created
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """ Automatically assigns the owner if not set. """
        if not self.owner:
            self.owner = User.objects.first()  # Assign the first user as the owner (or modify as needed)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

# Saved Property Model
class SavedProperty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'property')  # Ensures a user can save a property only once

    def __str__(self):
        return f"{self.user.username} saved {self.property.name}"
    

# Message Model
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    subject = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"From {self.sender} to {self.receiver} - {self.subject}"

# Notification Model
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    message = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True, null=True)  # Optional: Add links for action
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user} - {self.message}"
    
# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     property = models.ForeignKey(Property, on_delete=models.CASCADE)
#     status = models.CharField(max_length=50, default='pending')  # 'pending', 'successful'
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"Order by {self.user.username} for {self.property.name}"

# class Payment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     property = models.ForeignKey(Property, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     payment_method = models.CharField(max_length=50)  # Store payment method
#     status = models.CharField(max_length=50, default='pending')  # 'successful' or 'failed'

#     def __str__(self):
#         return f"Payment of {self.amount} by {self.user.username} for {self.property.name}"

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=[('successful', 'Successful'), ('failed', 'Failed')])
   

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('completed', 'Completed'), ('pending', 'Pending')])
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
  


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"