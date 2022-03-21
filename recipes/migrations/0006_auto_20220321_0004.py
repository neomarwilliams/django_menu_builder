# Generated by Django 3.2.12 on 2022-03-21 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_mealtype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mealtype',
            name='meals',
        ),
        migrations.AddField(
            model_name='mealtype',
            name='recipes',
            field=models.ManyToManyField(related_name='meals', to='recipes.Recipe'),
        ),
    ]