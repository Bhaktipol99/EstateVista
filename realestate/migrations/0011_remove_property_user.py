# Generated by Django 5.1.5 on 2025-02-18 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0010_remove_property_key_features_property_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='user',
        ),
    ]
