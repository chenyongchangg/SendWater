# Generated by Django 2.2 on 2019-04-24 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SendWaterBG', '0002_auto_20190423_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='boss',
            field=models.CharField(default='none', max_length=130),
            preserve_default=False,
        ),
    ]
