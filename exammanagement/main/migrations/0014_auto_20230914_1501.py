# Generated by Django 3.2.20 on 2023-09-14 08:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0013_chapter_is_passed"),
    ]

    operations = [
        migrations.AddField(
            model_name="chapter",
            name="best_score",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="chapter",
            name="do_times",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
