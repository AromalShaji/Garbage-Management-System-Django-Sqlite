# Generated by Django 4.1.1 on 2023-03-07 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_remove_company_cemail_remove_company_cpassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='cemail',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='company',
            name='cpassword',
            field=models.CharField(default='123', max_length=50),
        ),
    ]
