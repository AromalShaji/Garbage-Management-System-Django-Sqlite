# Generated by Django 4.1.1 on 2023-03-30 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0028_alter_driver_offer_companyid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver_offer',
            name='status',
            field=models.BooleanField(default='1', max_length=100),
        ),
        migrations.AlterField(
            model_name='employee_offer',
            name='status',
            field=models.BooleanField(default='1', max_length=100),
        ),
    ]
