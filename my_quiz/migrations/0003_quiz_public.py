# Generated by Django 4.0.4 on 2022-06-18 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_quiz", "0002_alter_quiz_options_quiz_hit"),
    ]

    operations = [
        migrations.AddField(
            model_name="quiz",
            name="public",
            field=models.BooleanField(blank=True, default=True),
        ),
    ]