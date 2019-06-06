# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('product', '0002_auto_20190601_1402'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField(default=0)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('extra_details', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField(default=0)),
                ('extra_details', models.TextField(blank=True)),
                ('status', models.PositiveIntegerField(default=1, choices=[(1, b'cart'), (2, b'payment_initiated'), (3, b'paid'), (4, b'shipped'), (5, b'completed'), (6, b'cancelled')])),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(to='customer.Customer')),
                ('customer_address', models.ForeignKey(blank=True, to='address.CustomerAddress', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='order',
            field=models.ForeignKey(to='cart.Order'),
        ),
        migrations.AddField(
            model_name='item',
            name='products',
            field=models.ManyToManyField(to='product.Product', blank=True),
        ),
    ]
