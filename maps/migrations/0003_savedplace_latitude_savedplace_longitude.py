# Generated by Django 5.1.2 on 2024-10-22 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_rename_name_savedplace_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedplace',
            name='latitude',
            field=models.FloatField(default=45.75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='savedplace',
            name='longitude',
            field=models.FloatField(default=4.85),
            preserve_default=False,
        ),
    ]
