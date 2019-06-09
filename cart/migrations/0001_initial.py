# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField(default=0)),
                ('extra_details', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2019, 6, 8, 12, 13, 59, 334583, tzinfo=utc), editable=False, blank=True)),
                ('status', models.PositiveIntegerField(default=1, choices=[(1, b'cart'), (2, b'payment_initiated'), (3, b'paid'), (4, b'shipped'), (5, b'completed'), (6, b'cancelled')])),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(to='customer.Customer')),
                ('customer_address', models.ForeignKey(blank=True, to='address.CustomerAddress', null=True)),
            ],
        ),
    ]
