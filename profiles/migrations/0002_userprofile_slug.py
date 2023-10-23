# Generated by Django 3.2.21 on 2023-10-23 11:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
    ]
