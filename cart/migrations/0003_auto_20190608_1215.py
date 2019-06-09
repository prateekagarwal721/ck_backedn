# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20190608_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 8, 12, 15, 26, 7010, tzinfo=utc), editable=False, blank=True),
        ),
    ]
