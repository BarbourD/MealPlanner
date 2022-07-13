# Generated by Django 4.0.6 on 2022-07-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_meal_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meal',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='chowtime',
        ),
        migrations.AddField(
            model_name='meal',
            name='chowtime',
            field=models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner'), ('S', 'Snack')], default='B', max_length=1),
        ),
        migrations.AlterField(
            model_name='meal',
            name='date',
            field=models.DateField(verbose_name='meal date'),
        ),
    ]