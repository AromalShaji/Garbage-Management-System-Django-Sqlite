# Generated by Django 4.1.1 on 2023-04-16 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0018_job_assigned_arrived_near_job_assigned_completed_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job_assigned',
            old_name='out_of_service',
            new_name='out_for_service',
        ),
    ]
