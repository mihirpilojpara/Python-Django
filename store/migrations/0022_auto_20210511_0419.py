# Generated by Django 3.2.2 on 2021-05-10 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_auto_20210510_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=2005, verbose_name='date joined'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='last_login',
            field=models.DateTimeField(auto_now=True, verbose_name='last login'),
        ),
    ]
