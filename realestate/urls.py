from django.urls import path
from . import views
from .views import other_users_properties, buy_property, buy_now, checkout_page, payment_page, payment_success

urlpatterns = [
    # Home and Authentication Routes
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register_view'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),

    # Property Routes
    path('add_property/', views.add_property, name='add_property'),
    path('properties/<int:pk>/edit/', views.edit_property, name='edit_property'),
    path('delete_property/<int:property_id>/', views.delete_property, name='delete_property'),
    path('property/<int:id>/', views.property_detail, name='property_detail'),
    path('properties/', views.property_list, name='property_list'),
    path('properties/others/', other_users_properties, name='other_users_properties'),

    # Property Actions: Buy, Save, Unsave
    path('buy/<int:property_id>/', buy_property, name='buy_property'),  # View Property to Buy
    path('buy-now/<int:property_id>/', buy_now, name='buy_now'),  # Proceed with Buying Property
    path('checkout/<int:property_id>/', checkout_page, name='checkout_page'),  # Checkout Page

    # Save/Unsave Property
    path('saved_properties/', views.saved_properties, name='saved_properties'),  # ✅ View saved properties
    path('save_property/<int:property_id>/', views.save_property, name='save_property'),  # ✅ Save property
    path('save_unsave/<int:property_id>/', views.save_unsave_property, name='save_unsave_property'),  # ✅ Save/Unsave property

    # Search and Messaging Routes
    path('search/', views.search_properties, name='search_properties'),
    path('inbox/', views.inbox, name='inbox'),
    path('sent/', views.sent_messages, name='sent_message'),
    path('send/', views.send_message, name='send_message'),
    path('notifications/', views.notifications, name='notifications'),
    path('mark-notification-read/<int:notification_id>/', views.mark_notification_read, name='mark_notification_read'),

    # Profile Management Routes
    path('profile/', views.profile_view, name='profile'),
    path('edit-profile/', views.edit_profile_view, name='edit_profile'),
    path('change-password/', views.change_password_view, name='change_password'),

    # Payment Routes
    path('properties/', views.available_properties, name='available_properties'),
    path('payment/<int:property_id>/', views.payment_page, name='payment_page'),
    path('payment_success/<int:property_id>/', views.payment_success, name='payment_success'),
       
  
]
