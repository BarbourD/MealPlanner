# Generated by Django 4.0.6 on 2022-07-12 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_meal_options_rename_week_meal_day_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='day',
            new_name='week',
        ),
    ]