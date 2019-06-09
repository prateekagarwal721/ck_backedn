# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('cart', '0003_auto_20190608_1215'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(default=b'', blank=True)),
                ('customer', models.ForeignKey(to='customer.Customer')),
                ('order', models.ForeignKey(null=True, to='cart.Order', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField(default=0, help_text=b'In case of custom items, say a T shirt for 500')),
                ('pro_rata_factor', models.FloatField(default=1)),
                ('description', models.CharField(default=b'', max_length=200, blank=True)),
                ('amount_type', models.CharField(default=b'item_price', max_length=100, null=True)),
                ('is_eligible', models.BooleanField(default=True)),
                ('object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('cart_item', models.ForeignKey(to='cart.Item', null=True)),
                ('content_type', models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True)),
                ('invoice', models.ForeignKey(related_name='items', to='payment.Invoice')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='invoiceitem',
            unique_together=set([('invoice', 'cart_item', 'amount_type')]),
        ),
    ]
