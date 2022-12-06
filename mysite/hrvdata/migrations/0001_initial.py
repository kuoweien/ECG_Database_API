# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('DataID', models.CharField(max_length=124, default='A123456789_20220629131831')),
                ('UserID', models.TextField(default='A123456789')),
                ('UserName', models.TextField(default='郭怡彤')),
                ('Gender', models.BooleanField(default=True)),
                ('BirthdayDate', models.DateField(default=datetime.date.today)),
            ],
            options={
                'db_table': 'UserData',
            },
        ),
        migrations.CreateModel(
            name='EcgData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('DataID', models.CharField(max_length=124, default='A123456789_20220629131831')),
                ('EcgBinaryData_col1', models.BinaryField()),
                ('EcgBinaryData_col2', models.TextField(default=' ')),
                ('EcgBinaryData_col3', models.TextField(default=' ')),
                ('EcgBinaryData_col4', models.TextField(default=' ')),
                ('EcgBinaryData_col5', models.TextField(default=' ')),
            ],
            options={
                'db_table': 'EcgData',
            },
        ),
        migrations.CreateModel(
            name='PdfReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('DataID', models.CharField(max_length=124, default='A123456789_20220629131831')),
                ('PdfBinaryData', models.BinaryField()),
            ],
            options={
                'db_table': 'PdfReport',
            },
        ),
        migrations.CreateModel(
            name='RecordHrvData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('DataID', models.CharField(max_length=124, default='A123456789_20220629131831')),
                ('MeasureDevice', models.TextField(default='00:30:04:1A:53:BC')),
                ('MeasureTime', models.TextField(default='20220629131831')),
                ('MeasureDuration', models.IntegerField(default=0)),
                ('HandleStatus', models.BooleanField(default=True)),
                ('HR', models.FloatField(default=0.0)),
                ('MeanNN', models.FloatField(default=0.0)),
                ('N', models.FloatField(default=0.0)),
                ('RRIV', models.FloatField(default=0.0)),
                ('Blance', models.FloatField(default=0.0)),
                ('SDNN', models.FloatField(default=0.0)),
                ('ANS', models.FloatField(default=0.0)),
                ('SYM', models.FloatField(default=0.0)),
                ('VAG', models.FloatField(default=0.0)),
                ('TP', models.FloatField(default=0.0)),
                ('SDNNZ', models.FloatField(default=0.0)),
                ('ANSZ', models.FloatField(default=0.0)),
                ('SYMZ', models.FloatField(default=0.0)),
                ('VAGZ', models.FloatField(default=0.0)),
                ('TPZ', models.FloatField(default=0.0)),
                ('SYMModulation', models.FloatField(default=0.0)),
                ('RWaveValidity', models.FloatField(default=0.0)),
                ('History', models.TextField(default=' ')),
                ('Remark', models.TextField(default=' ')),
                ('Suggest', models.TextField(default=' ')),
                ('SpO2', models.IntegerField(default=0)),
                ('RMSSD', models.IntegerField(default=0)),
                ('AF', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'RecordData',
            },
        ),
    ]
