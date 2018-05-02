# Generated by Django 2.0.5 on 2018-05-02 14:31

from django.db import migrations, models
import django.db.models.deletion

from django.db.migrations.operations.base import Operation
from django_admin_ownership.cross_app_migrations import WithAppLabelOperation

class Migration(migrations.Migration):

    dependencies = [
        ('cloudberry_app', '0001_initial'),
        ('django_admin_ownership', '__first__'),
        ('django_x509', '0005_organizational_unit_name'),
    ]

    operations = [
        WithAppLabelOperation(
            'django_x509',
            migrations.AddField(
                model_name='ca',
                name='group',
                field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.ConfigurationGroup'),
                preserve_default=False,
            )
        ),
    ]
