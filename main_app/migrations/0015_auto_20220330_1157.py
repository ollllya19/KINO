# Generated by Django 3.2.12 on 2022-03-30 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='login',
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
    ]
