# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('short_name', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('specification', models.TextField(null=True, blank=True)),
                ('price', models.FloatField(default=0)),
                ('product_code', models.SlugField(max_length=6, unique=True, null=True, blank=True)),
                ('picture', models.ImageField(upload_to=b'product', blank=True)),
                ('picture_extra_1', models.ImageField(upload_to=b'product', blank=True)),
                ('picture_extra_2', models.ImageField(upload_to=b'product', blank=True)),
                ('picture_extra_3', models.ImageField(upload_to=b'product', blank=True)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('picture', models.ImageField(upload_to=b'product', blank=True)),
                ('picture_extra_1', models.ImageField(upload_to=b'product', blank=True)),
                ('picture_extra_2', models.ImageField(upload_to=b'product', blank=True)),
                ('picture_extra_3', models.ImageField(upload_to=b'product', blank=True)),
                ('specification', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(blank=True, to='product.Category', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(blank=True, to='product.SubCategory', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('sub_category', 'product_code')]),
        ),
    ]
