from django import forms
from .models import Property
from .models import Message


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'location', 'price', 'description', 'image', 'status', 'bedrooms', 'bathrooms', 'area_sqft']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'subject', 'body']




