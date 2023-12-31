# Generated by Django 4.2 on 2023-06-08 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ubiteb", "0013_remove_alumni_current_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="AlumniBulkUpload",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("csv_file", models.FileField(upload_to="students/bulkupload/")),
            ],
        ),
        migrations.AlterModelOptions(
            name="alumni", options={"ordering": ["surname", "othernames", "regNo"]},
        ),
    ]
