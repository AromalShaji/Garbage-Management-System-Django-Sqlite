# Generated by Django 4.1.1 on 2023-04-18 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0025_leave_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leave',
            old_name='date',
            new_name='end_date',
        ),
        migrations.AddField(
            model_name='leave',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
