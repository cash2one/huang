# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(verbose_name='\u7c7b\u578b', choices=[(1, '\u5b58\u5165'), (2, '\u652f\u51fa')])),
                ('money', models.FloatField(verbose_name='\u91d1\u989d')),
                ('business_time', models.DateTimeField(verbose_name='\u4e1a\u52a1\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u4e1a\u52a1',
                'verbose_name_plural': '\u4e1a\u52a1',
            },
        ),
        migrations.CreateModel(
            name='BusinessMan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name='\u59d3\u540d')),
                ('achievement', models.FloatField(verbose_name='\u4e1a\u7ee9')),
            ],
            options={
                'verbose_name': '\u4e1a\u52a1\u5458',
                'verbose_name_plural': '\u4e1a\u52a1\u5458',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name='\u59d3\u540d')),
                ('business_man', models.ForeignKey(related_name='customer_manager', verbose_name='\u4e1a\u52a1\u5458', to='query.BusinessMan')),
            ],
            options={
                'verbose_name': '\u5ba2\u6237',
                'verbose_name_plural': '\u5ba2\u6237',
            },
        ),
        migrations.AddField(
            model_name='business',
            name='business_man',
            field=models.ForeignKey(related_name='business_man', verbose_name='\u4e1a\u52a1\u5458', to='query.BusinessMan'),
        ),
        migrations.AddField(
            model_name='business',
            name='customer',
            field=models.ForeignKey(related_name='business_customer', verbose_name='\u5ba2\u6237', to='query.Customer'),
        ),
    ]
