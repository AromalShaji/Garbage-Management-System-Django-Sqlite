# Generated by Django 4.1.1 on 2023-03-19 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0023_alter_driver_offer_vehicle_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver_offer',
            name='vehicle_details',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='Company.vehicle'),
        ),
    ]
