# Generated by Django 3.2.12 on 2022-03-22 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_remove_film_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='film',
            name='rating',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]