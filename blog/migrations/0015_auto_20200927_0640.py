# Generated by Django 3.1 on 2020-09-27 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0014_auto_20200925_0834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(help_text='please enter along with your country code. e.g "+91"', max_length=128, region=None)),
                ('status', models.CharField(choices=[('scholar', 'SCHOLAR'), ('fresher', 'FRESHER')], default='scholar', max_length=10)),
                ('About', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
