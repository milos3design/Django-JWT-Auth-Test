# Generated by Django 4.2.1 on 2023-12-07 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mimkviz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='date_of_birth',
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
    ]
