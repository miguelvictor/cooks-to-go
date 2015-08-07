# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150807_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipecomponent',
            name='extra',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recipecomponent',
            name='quantity',
            field=models.FloatField(),
        ),
    ]
