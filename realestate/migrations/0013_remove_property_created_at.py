# Generated by Django 5.1.5 on 2025-02-18 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0012_alter_property_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='created_at',
        ),
    ]
