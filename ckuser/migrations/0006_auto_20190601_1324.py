# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ckuser', '0005_auto_20190529_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ckuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 1, 13, 24, 34, 705727, tzinfo=utc), verbose_name='date joined'),
        ),
    ]
