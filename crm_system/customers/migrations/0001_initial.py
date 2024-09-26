# Generated by Django 5.1.1 on 2024-09-26 12:36

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ads', '0001_initial'),
        ('contracts', '0006_contract_document_contract_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('surname', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='RU')),
                ('ad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ads.ads')),
                ('contract', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='contracts.contract')),
            ],
        ),
    ]
