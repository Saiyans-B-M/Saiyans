# Generated by Django 3.1 on 2020-10-18 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Team', '0007_auto_20201018_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='position',
            field=models.CharField(choices=[('MEMBER', 'MEMBER'), ('TEAM LEADER', 'TEAM LEADER'), ('SAIYANS LEADER', 'SAIYANS LEADER')], default='mem', max_length=20),
        ),
    ]