# Generated by Django 4.2 on 2023-06-09 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ubiteb", "0019_alter_alumni_program_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alumni",
            name="center",
            field=models.CharField(
                choices=[("mbi", "MBI"), ("mubs", "MUBS")], default=None, max_length=50
            ),
        ),
        migrations.AlterField(
            model_name="alumni",
            name="certificate_status",
            field=models.CharField(
                choices=[("received", "Received"), ("not received", "Not Received")],
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="alumni",
            name="employment_entity",
            field=models.CharField(
                choices=[
                    ("government", "Government"),
                    ("private", "Private"),
                    ("ngo", "NGO"),
                    ("missionary", "Missionary"),
                    ("none", "None"),
                ],
                max_length=40,
            ),
        ),
        migrations.AlterField(
            model_name="alumni",
            name="employment_status",
            field=models.CharField(
                choices=[("employed", "Employed"), ("unemployed", "Unemployed")],
                max_length=40,
            ),
        ),
        migrations.AlterField(
            model_name="alumni",
            name="program",
            field=models.CharField(
                choices=[
                    (
                        "national diploma in mechanic engineering",
                        "National Diploma in Mechanical Engineering",
                    ),
                    (
                        "national diploma in civil engineering",
                        "National Diploma in Civil Engineering",
                    ),
                    (
                        "national diploma in water engineering",
                        "National Diploma in Water Engineering",
                    ),
                    (
                        "national diploma in electrical engineering",
                        "National Diploma in Electrical Engineering",
                    ),
                ],
                default=None,
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="alumni",
            name="program_level",
            field=models.CharField(
                choices=[
                    ("higher diploma", "Higher Diploma"),
                    ("diploma", "Diploma"),
                    ("national certificate", "National Certificate"),
                    ("ucpc", "Uganda Community of Polytechnic Certificate"),
                ],
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="alumni",
            name="transcript_status",
            field=models.CharField(
                choices=[("received", "Received"), ("not received", "Not Received")],
                max_length=30,
            ),
        ),
    ]
