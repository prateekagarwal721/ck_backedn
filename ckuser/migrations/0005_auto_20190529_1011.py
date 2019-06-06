# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ckuser', '0004_auto_20190529_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ckuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 29, 10, 11, 13, 669001, tzinfo=utc), verbose_name='date joined'),
        ),
    ]
