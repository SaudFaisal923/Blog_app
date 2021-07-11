# Generated by Django 3.2.3 on 2021-07-10 17:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210710_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted_date',
            field=models.DateField(verbose_name=datetime.datetime(2021, 7, 10, 17, 6, 45, 344284, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 7, 10, 17, 6, 45, 346284, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_date',
            field=models.DateField(verbose_name=datetime.datetime(2021, 7, 10, 17, 6, 45, 344284, tzinfo=utc)),
        ),
    ]