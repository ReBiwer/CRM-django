# Generated by Django 5.1.1 on 2024-09-24 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0004_alter_contract_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
