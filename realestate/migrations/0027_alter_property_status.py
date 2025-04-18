# Generated by Django 5.1.5 on 2025-03-20 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0026_alter_property_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('sold', 'Sold'), ('rented', 'Rented'), ('pending', 'Pending')], default='Available', max_length=20),
        ),
    ]
