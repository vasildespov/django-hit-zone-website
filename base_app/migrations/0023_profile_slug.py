# Generated by Django 3.1.3 on 2020-12-22 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0022_auto_20201222_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]