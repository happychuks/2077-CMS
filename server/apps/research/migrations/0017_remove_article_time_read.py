# Generated by Django 5.0.8 on 2024-08-29 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0016_article_time_read'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='time_read',
        ),
    ]
