# Generated by Django 5.0 on 2023-12-05 16:36

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_alter_complaint_id_alter_flat_has_balcony_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region=None, verbose_name='Нормализированный номер владельца'),
        ),
    ]
