# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150910_0238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='step',
            options={'ordering': ['sequence']},
        ),
    ]
