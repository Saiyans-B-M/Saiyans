# Generated by Django 3.1 on 2020-09-24 04:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200923_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
