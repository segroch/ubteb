# Generated by Django 4.2 on 2023-06-10 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ubiteb", "0023_alter_alumni_exam_center"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alumni",
            name="district",
            field=models.CharField(choices=[], max_length=50),
        ),
    ]
