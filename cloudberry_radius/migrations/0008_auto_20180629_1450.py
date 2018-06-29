# Generated by Django 2.0.6 on 2018-06-29 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cloudberry_radius', '0007_auto_20180629_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricing',
            name='latest_price_for',
        ),
        migrations.AddField(
            model_name='pricing',
            name='latest_price',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pricing',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='radius_pricing', to='auth.ConfigurationGroup'),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, db_column='timestamp', verbose_name='Time'),
        ),
    ]