# Generated by Django 5.1.5 on 2025-02-14 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='property',
            old_name='location',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='property',
            name='image',
        ),
        migrations.RemoveField(
            model_name='property',
            name='name',
        ),
    ]
