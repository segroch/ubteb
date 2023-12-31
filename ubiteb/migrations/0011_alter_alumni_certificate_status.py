# Generated by Django 4.2 on 2023-06-06 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ubiteb", "0010_alter_alumni_certificate_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alumni",
            name="certificate_status",
            field=models.CharField(
                choices=[("received", "Received"), ("not received", "Not Received")],
                default="received",
                max_length=30,
            ),
        ),
    ]
