# Generated by Django 5.0.1 on 2024-02-16 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Study_app', '0002_crescentlib_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crescentlib',
            name='manager',
        ),
    ]
