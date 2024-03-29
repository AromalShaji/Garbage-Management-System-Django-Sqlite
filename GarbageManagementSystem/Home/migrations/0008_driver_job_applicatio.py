# Generated by Django 4.1.1 on 2023-03-27 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0026_remove_driver_offer_license'),
        ('Home', '0007_company_crate'),
    ]

    operations = [
        migrations.CreateModel(
            name='driver_job_applicatio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp', models.CharField(default='1', max_length=100)),
                ('limg', models.ImageField(default='', upload_to='images')),
                ('companyid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='Home.company')),
                ('jobid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='Company.driver_offer')),
                ('userid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='Home.customer')),
            ],
        ),
    ]
