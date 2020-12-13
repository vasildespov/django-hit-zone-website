# Generated by Django 3.1.3 on 2020-12-13 04:12

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0013_remove_article_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(default='Write content here...', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
