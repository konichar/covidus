# Generated by Django 3.0.5 on 2020-04-26 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidus_main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='temperature',
        ),
        migrations.AddField(
            model_name='profile',
            name='temperature_pills',
            field=models.CharField(choices=[('34.0', 'Normal'), ('37.5 - 38.0°C', 'Low Fever'), ('38.1-39.0°C', 'High Fever'), ('>39.0°C', 'Very High Fever')], default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='current_postalcode',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='postal_code',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.IntegerField(),
        ),
    ]
