# Generated by Django 3.2.12 on 2022-03-30 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_alter_user_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='login',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]