# Generated by Django 4.1.7 on 2023-03-29 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='0001-01-01'),
            preserve_default=False,
        ),
    ]
