# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ckuser', '0014_auto_20190608_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ckuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 8, 10, 49, 45, 572214, tzinfo=utc), verbose_name='date joined'),
        ),
    ]
