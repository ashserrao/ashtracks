# Generated by Django 3.0.6 on 2020-05-30 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ash_tracks', '0002_auto_20200530_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Email_id',
            new_name='email',
        ),
    ]
