# Generated by Django 3.1 on 2020-09-20 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200919_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='phone',
        ),
    ]
