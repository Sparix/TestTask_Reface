# Generated by Django 4.2.7 on 2024-04-29 08:59

from django.db import migrations, models
import task_manager.models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0005_alter_task_assignees'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasktype',
            name='color',
            field=models.CharField(default=2007, max_length=20, validators=[task_manager.models.validate_hex_color]),
            preserve_default=False,
        ),
    ]