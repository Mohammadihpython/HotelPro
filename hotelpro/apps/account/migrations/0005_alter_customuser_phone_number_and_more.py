# Generated by Django 4.2.4 on 2023-09-19 20:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_userotp_code_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+989xxxxxxxxx'. Up to 14 digits allowed.", regex='^09\\d{9}$')], verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='userotp',
            name='phone_number',
            field=models.CharField(blank=True, max_length=14, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+989xxxxxxxxx'. Up to 14 digits allowed.", regex='^09\\d{9}$')], verbose_name='Phone number'),
        ),
    ]
