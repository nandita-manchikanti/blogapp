# Generated by Django 3.1.2 on 2021-06-22 11:04

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210621_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]