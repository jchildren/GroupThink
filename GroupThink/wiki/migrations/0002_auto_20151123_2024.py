# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='created_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='revision',
            old_name='modified_date',
            new_name='date',
        ),
    ]
