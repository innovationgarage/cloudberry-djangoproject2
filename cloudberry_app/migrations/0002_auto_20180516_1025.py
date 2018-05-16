# Generated by Django 2.0.5 on 2018-05-16 10:25

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cloudberry_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backend',
            name='schema',
            field=jsonfield.fields.JSONField(blank=True, default=dict, help_text='<a target="_blank" href="http://json-schema.org/">JSONSchema</a> for the configuration', verbose_name='schema'),
        ),
        migrations.AlterField(
            model_name='backend',
            name='transform',
            field=jsonfield.fields.JSONField(blank=True, default=dict, help_text='<a target="_blank" href="https://innovationgarage.github.io/cloudberry-djangoproject/docs/backends.html">Transform</a> of the configuration', verbose_name='transform'),
        ),
    ]
