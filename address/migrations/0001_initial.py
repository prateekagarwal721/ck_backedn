# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_1', models.CharField(max_length=128, null=True, verbose_name='address', blank=True)),
                ('address_2', models.CharField(max_length=128, null=True, verbose_name="address cont'd", blank=True)),
                ('city', models.CharField(max_length=64, null=True, verbose_name='city', blank=True)),
                ('state', models.CharField(max_length=64, null=True, verbose_name='state', blank=True)),
                ('zip_code', models.CharField(max_length=6, verbose_name='zip code')),
                ('description', models.TextField(null=True, blank=True)),
                ('customer', models.ForeignKey(to='customer.Customer')),
            ],
        ),
    ]
