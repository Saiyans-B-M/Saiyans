# Generated by Django 3.1 on 2020-09-27 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20200927_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='About',
            field=models.TextField(help_text='say something about you, you can leave it empty too'),
        ),
    ]