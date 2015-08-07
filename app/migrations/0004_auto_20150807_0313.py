# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_recipecomponent_extra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipecomponent',
            name='quantity',
            field=models.DecimalField(max_digits=4, decimal_places=4),
        ),
    ]
