# Generated by Django 3.2.12 on 2022-03-05 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_film'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='runtime',
            field=models.IntegerField(blank=True),
        ),
    ]
