# Generated by Django 5.1.2 on 2024-10-22 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='savedplace',
            old_name='name',
            new_name='label',
        ),
    ]
