# Generated by Django 3.2.2 on 2021-05-10 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_auto_20210510_1414'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
