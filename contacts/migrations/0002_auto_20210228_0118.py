# Generated by Django 3.1.5 on 2021-02-27 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contacts',
            new_name='contact',
        ),
    ]
