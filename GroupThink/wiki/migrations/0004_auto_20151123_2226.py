# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0003_auto_20151123_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='revision',
            name='page',
        ),
        migrations.AddField(
            model_name='page',
            name='latest',
            field=models.ForeignKey(default=1, to='wiki.Revision'),
            preserve_default=False,
        ),
    ]
