# Generated by Django 4.2.7 on 2023-11-23 16:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_purchaseorderstatus_purchaseorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='issue_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
