# Generated by Django 4.1.1 on 2023-04-16 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0017_alter_job_assigned_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_assigned',
            name='arrived_near',
            field=models.BooleanField(default='0'),
        ),
        migrations.AddField(
            model_name='job_assigned',
            name='completed',
            field=models.BooleanField(default='0'),
        ),
        migrations.AddField(
            model_name='job_assigned',
            name='out_of_service',
            field=models.BooleanField(default='0'),
        ),
    ]
