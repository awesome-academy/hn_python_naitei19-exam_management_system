# Generated by Django 3.2.20 on 2023-09-11 09:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0005_alter_enroll_progress"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="enroll",
            unique_together={("user", "subject")},
        ),
    ]
