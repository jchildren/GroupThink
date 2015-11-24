# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0004_auto_20151123_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='revision',
            name='log',
            field=models.CharField(default='asdasd', max_length=100),
            preserve_default=False,
        ),
    ]
