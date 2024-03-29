# Generated by Django 4.2.5 on 2023-10-05 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0022_notification_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="updated_chapter",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="main.chapter",
            ),
        ),
    ]
