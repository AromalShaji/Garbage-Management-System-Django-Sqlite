# Generated by Django 4.1.1 on 2023-03-31 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0029_alter_driver_offer_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver_offer',
            name='vehicle_details',
        ),
        migrations.RemoveField(
            model_name='employee_offer',
            name='driverid',
        ),
    ]
