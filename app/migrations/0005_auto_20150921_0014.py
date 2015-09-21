# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150912_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='who',
            field=models.CharField(max_length=20),
        ),
    ]
