# Generated by Django 4.1.1 on 2023-04-05 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0024_dumbster_booking_numberofday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dumbster_booking',
            name='numberofdumbster',
            field=models.IntegerField(default='1'),
        ),
    ]
