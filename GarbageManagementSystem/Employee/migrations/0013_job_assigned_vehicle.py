# Generated by Django 4.1.1 on 2023-04-11 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0012_alter_job_assigned_employeeid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_assigned',
            name='vehicle',
            field=models.CharField(default='', max_length=50),
        ),
    ]
