# Generated by Django 4.0.6 on 2022-07-11 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='directions',
        ),
        migrations.RemoveField(
            model_name='meal',
            name='ingnumber',
        ),
        migrations.RemoveField(
            model_name='meal',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='meal',
            name='ingtype',
        ),
        migrations.AlterField(
            model_name='meal',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]