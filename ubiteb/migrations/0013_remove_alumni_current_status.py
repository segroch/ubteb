# Generated by Django 4.2 on 2023-06-08 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ubiteb", "0012_alter_alumni_employment_entity_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="alumni", name="current_status",),
    ]