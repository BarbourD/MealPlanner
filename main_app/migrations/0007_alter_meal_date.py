# Generated by Django 4.0.6 on 2022-07-12 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_rename_week_meal_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]
