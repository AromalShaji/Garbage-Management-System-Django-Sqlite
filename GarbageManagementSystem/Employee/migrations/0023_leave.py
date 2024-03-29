# Generated by Django 4.1.1 on 2023-04-18 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0035_alter_dumbster_booking_status'),
        ('Employee', '0022_rename_id_job_assigned_job_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default='0', max_length=100)),
                ('status', models.BooleanField(default='0', max_length=100)),
                ('companyid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Home.company')),
                ('userid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Employee.employee')),
            ],
        ),
    ]
