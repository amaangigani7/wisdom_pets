# Generated by Django 3.0.3 on 2021-05-17 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='vaccine',
            new_name='vaccinations',
        ),
    ]
