# Generated by Django 4.1.1 on 2023-04-18 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0028_leave_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='rejected',
            field=models.BooleanField(default='0', max_length=100),
        ),
    ]
