# Generated by Django 4.1.1 on 2023-03-30 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_alter_company_status_alter_customer_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='cemail',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
    ]