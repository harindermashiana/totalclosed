# Generated by Django 2.0.2 on 2018-05-05 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recognition', '0003_auto_20180421_2100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='document',
            new_name='file_field',
        ),
    ]
