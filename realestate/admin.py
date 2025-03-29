from django.contrib import admin
from .models import Profile
from .models import Property
from .models import SavedProperty
from .models import Message
from .models import Notification
from .models import Order
from .models import Payment

#Registration
admin.site.register(Profile)

#Property
admin.site.register(Property)

#SavedProperty
admin.site.register(SavedProperty)


admin.site.site_header = "Real Estate Management"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome to Property Dashboard"

#Message
admin.site.register(Message)
admin.site.register(Notification)
admin.site.register(Order)
admin.site.register(Payment)
