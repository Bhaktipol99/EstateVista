# Generated by Django 5.1.5 on 2025-02-16 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0004_property'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='user',
        ),
    ]
