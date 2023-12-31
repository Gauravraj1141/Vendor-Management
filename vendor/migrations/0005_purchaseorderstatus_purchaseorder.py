# Generated by Django 4.2.7 on 2023-11-23 15:54

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0004_alter_vendor_email_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrderStatus',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('po_number', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(default=datetime.datetime.now)),
                ('delivery_date', models.DateTimeField(default=datetime.datetime.now)),
                ('items', models.JSONField()),
                ('quantity', models.IntegerField()),
                ('quality_rating', models.FloatField(blank=True, null=True)),
                ('issue_date', models.DateTimeField()),
                ('acknowledgment_date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('order_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_order_status', to='vendor.purchaseorderstatus')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_vendor', to='vendor.vendor')),
            ],
        ),
    ]
