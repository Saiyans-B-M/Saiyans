# Generated by Django 3.1 on 2020-10-18 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20201018_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='username',
            field=models.CharField(help_text='This will be your username, you cannot change it later', max_length=55),
        ),
    ]
