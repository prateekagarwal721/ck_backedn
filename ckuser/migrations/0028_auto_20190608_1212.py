# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ckuser', '0027_auto_20190608_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ckuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 8, 12, 12, 5, 152012, tzinfo=utc), verbose_name='date joined'),
        ),
    ]
