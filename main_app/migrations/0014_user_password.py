# Generated by Django 3.2.12 on 2022-03-30 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_auto_20220330_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
    ]