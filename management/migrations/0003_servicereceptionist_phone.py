# Generated by Django 3.2.9 on 2022-01-29 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20220128_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicereceptionist',
            name='phone',
            field=models.BigIntegerField(default=655433221),
            preserve_default=False,
        ),
    ]
