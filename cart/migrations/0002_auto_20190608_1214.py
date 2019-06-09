# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField(default=0)),
                ('item_price', models.FloatField(default=0)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('extra_details', models.TextField(null=True, blank=True)),
                ('content_type', models.ForeignKey(default=12, to='contenttypes.ContentType')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 8, 12, 14, 24, 529539, tzinfo=utc), editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='order',
            field=models.ForeignKey(to='cart.Order'),
        ),
    ]
