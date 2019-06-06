# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import customer.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('profile_pic', models.ImageField(upload_to=customer.models.get_upload_to, blank=True)),
                ('customer_business_type', models.PositiveIntegerField(blank=True, null=True, choices=[(0, b'Default'), (1, b'Retailer'), (2, b'Wholesaler'), (3, b'Manufacturer'), (4, b'Other')])),
                ('primary_zip_code', models.CharField(max_length=6, null=True, verbose_name='zip code', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
