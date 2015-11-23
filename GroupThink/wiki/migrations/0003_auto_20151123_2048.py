# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_auto_20151123_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revision',
            name='text',
            field=models.ForeignKey(to='wiki.Text'),
        ),
    ]
