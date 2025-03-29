# Generated by Django 5.1.5 on 2025-03-11 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0018_property_area_sqft_property_bathrooms_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[('apartment', 'Apartment'), ('villa', 'Villa'), ('office', 'Office')], default='apartment', max_length=50),
        ),
    ]
