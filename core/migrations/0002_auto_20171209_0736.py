# Generated by Django 2.0 on 2017-12-09 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mission',
            old_name='mission_desecription',
            new_name='mission_description',
        ),
    ]