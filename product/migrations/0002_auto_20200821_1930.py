# Generated by Django 3.0.8 on 2020-08-21 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='passwd',
            new_name='password',
        ),
    ]
