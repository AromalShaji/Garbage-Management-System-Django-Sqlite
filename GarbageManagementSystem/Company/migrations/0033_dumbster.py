# Generated by Django 4.1.1 on 2023-04-03 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0018_service_booking_phone'),
        ('Company', '0032_employee_offer_end_time_employee_offer_start_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='dumbster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberofdumbster', models.CharField(default='', max_length=100)),
                ('size', models.CharField(default='', max_length=100)),
                ('dimension', models.CharField(default='', max_length=100)),
                ('rate', models.CharField(default='', max_length=100)),
                ('status', models.CharField(default='1', max_length=100)),
                ('companyid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Home.company')),
            ],
        ),
    ]
