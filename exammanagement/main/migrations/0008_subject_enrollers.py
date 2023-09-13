# Generated by Django 3.2.20 on 2023-09-12 11:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_merge_20230912_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='enrollers',
            field=models.ManyToManyField(through='main.Enroll', to=settings.AUTH_USER_MODEL),
        ),
    ]