# Generated by Django 5.1.1 on 2024-09-27 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_name_profile_second_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='products',
        ),
    ]
