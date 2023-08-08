# Generated by Django 4.2.4 on 2023-08-08 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Trainee",
            fields=[
                (
                    "trainee_id",
                    models.CharField(max_length=5, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=100)),
                ("age", models.PositiveIntegerField()),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("male", "Male"),
                            ("female", "Female"),
                            ("other", "Other"),
                        ],
                        max_length=10,
                    ),
                ),
                ("date_of_birth", models.DateField()),
                ("phone_num", models.CharField(max_length=15)),
                ("address", models.TextField()),
            ],
        ),
    ]