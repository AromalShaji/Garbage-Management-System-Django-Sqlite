# Generated by Django 4.1.1 on 2023-03-15 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0011_driver_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='area',
        ),
    ]
