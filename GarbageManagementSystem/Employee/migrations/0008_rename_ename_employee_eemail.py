# Generated by Django 4.1.1 on 2023-04-01 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0007_employee_ename_employee_epass'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='ename',
            new_name='eemail',
        ),
    ]
