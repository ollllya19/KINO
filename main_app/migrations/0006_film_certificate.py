# Generated by Django 3.2.12 on 2022-03-06 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_film_runtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='certificate',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
