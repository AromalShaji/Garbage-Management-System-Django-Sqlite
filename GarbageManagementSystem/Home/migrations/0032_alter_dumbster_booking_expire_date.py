# Generated by Django 4.1.1 on 2023-04-12 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0031_dumbster_booking_expire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dumbster_booking',
            name='expire_date',
            field=models.CharField(default='', max_length=20),
        ),
    ]
