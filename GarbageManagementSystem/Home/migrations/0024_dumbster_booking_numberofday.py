# Generated by Django 4.1.1 on 2023-04-05 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0023_payment_is_for'),
    ]

    operations = [
        migrations.AddField(
            model_name='dumbster_booking',
            name='numberofday',
            field=models.CharField(default='', max_length=20),
        ),
    ]
