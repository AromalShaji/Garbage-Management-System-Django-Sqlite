# Generated by Django 4.1.1 on 2023-03-31 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0005_alter_employee_role_alter_employee_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='vehicleid',
        ),
    ]
