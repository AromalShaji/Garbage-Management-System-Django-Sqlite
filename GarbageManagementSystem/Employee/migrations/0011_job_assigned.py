# Generated by Django 4.1.1 on 2023-04-10 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0028_service_booking_rate'),
        ('Employee', '0010_employee_ephone'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_assigned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dumbster_scheduled', models.CharField(default='', max_length=50)),
                ('service_scheduled', models.CharField(default='', max_length=50)),
                ('assistant', models.CharField(default='', max_length=50)),
                ('status', models.BooleanField(default='0', max_length=100)),
                ('companyid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Home.company')),
                ('employeeid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Employee.employee')),
            ],
        ),
    ]
