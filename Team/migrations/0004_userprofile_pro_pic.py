# Generated by Django 3.1 on 2020-10-18 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Team', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='pro_pic',
            field=models.ImageField(default='default.png', upload_to='pro_pics/'),
        ),
    ]
