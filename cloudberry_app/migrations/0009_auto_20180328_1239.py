# Generated by Django 2.0.3 on 2018-03-28 12:39

import cloudberry_app.models
import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('cloudberry_app', '0008_auto_20180328_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backend',
            name='backend',
            field=cloudberry_app.models.DynamicTextListField(blank=True, help_text='Select <a href="http://netjsonconfig.openwisp.org/en/stable/" target="_blank">netjsonconfig</a> backend', max_length=128, verbose_name='backend'),
        ),
        migrations.AlterField(
            model_name='config',
            name='backend',
            field=cloudberry_app.models.DynamicTextListField(blank=True, help_text='Select <a href="http://netjsonconfig.openwisp.org/en/stable/" target="_blank">netjsonconfig</a> backend', max_length=128, verbose_name='backend'),
        ),
        migrations.AlterField(
            model_name='device',
            name='mac_address',
            field=models.CharField(blank=True, db_index=True, help_text='primary mac address', max_length=17, null=True, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'), code='invalid', message='Must be a valid mac address.')]),
        ),
    ]
