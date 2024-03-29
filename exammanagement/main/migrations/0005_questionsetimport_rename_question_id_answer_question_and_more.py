# Generated by Django 4.2.5 on 2023-09-12 09:41

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_alter_answer_is_correct_alter_chapter_num_questions_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="QuestionSetImport",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=512)),
                ("filename", models.FileField(max_length=512, upload_to="uploads/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name="enroll",
            name="status",
            field=models.IntegerField(
                blank=True, choices=[(1, "Completed"), (0, "Incomplete")], default=0
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="id",
            field=models.CharField(
                default=uuid.uuid4,
                editable=False,
                max_length=100,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="test",
            name="status",
            field=models.IntegerField(
                blank=True, choices=[(1, "Completed"), (0, "Incomplete")], default=0
            ),
        ),
    ]
