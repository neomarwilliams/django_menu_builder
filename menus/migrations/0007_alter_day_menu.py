# Generated by Django 3.2.12 on 2022-03-20 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0006_alter_menu_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='menu',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='menus.menu'),
            preserve_default=False,
        ),
    ]
