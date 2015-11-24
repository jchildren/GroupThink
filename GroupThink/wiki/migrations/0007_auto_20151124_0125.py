# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0006_auto_20151124_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='revisions',
            field=models.ManyToManyField(related_name='Page', to='wiki.Revision'),
        ),
        migrations.AlterField(
            model_name='page',
            name='latest',
            field=models.ForeignKey(related_name='+', to='wiki.Revision'),
        ),
    ]
