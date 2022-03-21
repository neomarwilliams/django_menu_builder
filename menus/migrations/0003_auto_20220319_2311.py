# Generated by Django 3.2.12 on 2022-03-19 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_auto_20220315_2248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='name',
            new_name='menu_name',
        ),
        migrations.AlterField(
            model_name='menu',
            name='tags',
            field=models.ManyToManyField(related_name='menus', to='menus.Tag'),
        ),
    ]
