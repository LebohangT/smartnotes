# Generated by Django 5.0.6 on 2024-05-22 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0004_alter_notes_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notes",
            name="text",
            field=models.TextField(),
        ),
    ]
