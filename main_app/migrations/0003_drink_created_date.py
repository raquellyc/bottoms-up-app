# Generated by Django 4.0.2 on 2022-02-16 09:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_ingredient_drink_drink_ingredients_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created'),
        ),
    ]
