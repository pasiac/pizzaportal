# Generated by Django 2.2.5 on 2019-09-25 16:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20190925_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]