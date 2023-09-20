# Generated by Django 4.2.4 on 2023-09-18 14:32

import django.core.validators
from django.db import migrations, models
import hotelpro.apps.account.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_userotp_email_customuser_verify_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userotp',
            name='expire_time_end',
            field=models.DateTimeField(blank=True, default=hotelpro.apps.account.models.default_expire_time, null=True, verbose_name='end of expire time'),
        ),
        migrations.AlterField(
            model_name='userotp',
            name='phone_number',
            field=models.CharField(blank=True, max_length=14, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+989xxxxxxxxx'. Up to 14 digits allowed.", regex='^\\+{1}989\\d{9}$')], verbose_name='Phone number'),
        ),
    ]