# Generated by Django 3.2.12 on 2022-03-31 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_auto_20220331_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='rating',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
