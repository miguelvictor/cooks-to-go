# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('banner', models.URLField()),
                ('description', models.CharField(max_length=255)),
                ('icon', models.URLField()),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('picture', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(default=0)),
                ('who', models.CharField(max_length=b'20')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('banner', models.URLField()),
                ('icon', models.URLField()),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RecipeComponent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.FloatField()),
                ('extra', models.CharField(max_length=255, null=True, blank=True)),
                ('ingredient', models.OneToOneField(to='app.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('picture', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sequence', models.IntegerField(default=1)),
                ('instruction', models.TextField()),
                ('recipe', models.ForeignKey(related_name='steps', to='app.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='UnitOfMeasure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='recipecomponent',
            name='unit_of_measure',
            field=models.ForeignKey(to='app.UnitOfMeasure'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_components',
            field=models.ManyToManyField(to='app.RecipeComponent'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='type',
            field=models.ForeignKey(related_name='recipes', to='app.RecipeType'),
        ),
        migrations.AddField(
            model_name='rating',
            name='recipe',
            field=models.ForeignKey(related_name='ratings', to='app.Recipe'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='type',
            field=models.ForeignKey(related_name='ingredients', to='app.IngredientType'),
        ),
    ]
