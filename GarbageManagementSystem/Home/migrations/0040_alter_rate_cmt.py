# Generated by Django 4.1.1 on 2023-05-16 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0039_rate_cmt_alter_rate_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='cmt',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
