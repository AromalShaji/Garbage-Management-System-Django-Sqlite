# Generated by Django 4.1.1 on 2023-03-18 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_alter_rate_companyid_alter_rate_userid'),
        ('Company', '0018_alter_vehicle_vehicle_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver_offer',
            name='companyid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='Home.company'),
        ),
        migrations.AlterField(
            model_name='employee_offer',
            name='companyid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='Home.company'),
        ),
    ]
