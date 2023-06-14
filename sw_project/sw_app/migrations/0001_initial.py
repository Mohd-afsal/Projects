# Generated by Django 4.1.7 on 2023-03-11 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('images', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]
