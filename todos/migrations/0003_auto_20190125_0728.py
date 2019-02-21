# Generated by Django 2.1.5 on 2019-01-25 07:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_todo_upd_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 7, 28, 0, 776516, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='upd_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 7, 28, 0, 776550, tzinfo=utc)),
        ),
    ]
