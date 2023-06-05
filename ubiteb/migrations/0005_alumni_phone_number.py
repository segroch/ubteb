# Generated by Django 4.2 on 2023-06-05 00:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubiteb', '0004_remove_alumni_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='phone_number',
            field=models.IntegerField(default='0000000000', verbose_name=django.core.validators.RegexValidator(message="Entered mobile number isn't in a right format!", regex='^[0-9]{10,15}$')),
            preserve_default=False,
        ),
    ]
