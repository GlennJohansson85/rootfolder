# Generated by Django 5.0.1 on 2024-02-08 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='content',
        ),
    ]