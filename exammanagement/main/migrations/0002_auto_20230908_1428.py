# Generated by Django 3.2.20 on 2023-09-08 07:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="chapter",
            old_name="subject_id",
            new_name="subject",
        ),
        migrations.RenameField(
            model_name="choice",
            old_name="answer_id",
            new_name="answer",
        ),
        migrations.RenameField(
            model_name="choice",
            old_name="question_id",
            new_name="question",
        ),
        migrations.RenameField(
            model_name="choice",
            old_name="test_id",
            new_name="test",
        ),
        migrations.RenameField(
            model_name="choice",
            old_name="user_id",
            new_name="user",
        ),
        migrations.RenameField(
            model_name="enroll",
            old_name="subject_id",
            new_name="subject",
        ),
        migrations.RenameField(
            model_name="enroll",
            old_name="user_id",
            new_name="user",
        ),
        migrations.RenameField(
            model_name="test",
            old_name="chapter_id",
            new_name="chapter",
        ),
        migrations.RenameField(
            model_name="test",
            old_name="user_id",
            new_name="user",
        ),
        migrations.RemoveField(
            model_name="question",
            name="corerct_answer",
        ),
        migrations.AddField(
            model_name="answer",
            name="is_correct",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="chapter",
            name="num_questions",
            field=models.PositiveIntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="answer",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="chapter",
            name="time_limit",
            field=models.PositiveIntegerField(help_text="Time limit for the test"),
        ),
        migrations.AlterField(
            model_name="choice",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="enroll",
            name="status",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "Completed"), (0, "Incomplete")],
                default="i",
                max_length=1,
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="test",
            name="status",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "Completed"), (0, "Incomplete")],
                default="i",
                max_length=1,
            ),
        ),
    ]
