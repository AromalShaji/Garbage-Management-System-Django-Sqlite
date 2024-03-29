# Generated by Django 4.1.1 on 2023-03-28 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_employee_job_application'),
        ('Company', '0027_alter_driver_offer_vehicle_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver_offer',
            name='companyid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Home.company'),
        ),
        migrations.AlterField(
            model_name='driver_offer',
            name='vehicle_details',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Company.vehicle'),
        ),
        migrations.AlterField(
            model_name='employee_offer',
            name='companyid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Home.company'),
        ),
        migrations.AlterField(
            model_name='employee_offer',
            name='driverid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Company.driver_offer'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='companyid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Home.company'),
        ),
    ]
