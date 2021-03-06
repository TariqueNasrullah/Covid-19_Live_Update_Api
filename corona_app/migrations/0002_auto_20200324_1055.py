# Generated by Django 3.0.4 on 2020-03-24 10:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('corona_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coronadata',
            name='active',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coronadata',
            name='closed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coronadata',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coronadata',
            name='death',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coronadata',
            name='death_percentage',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='coronadata',
            name='mild',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coronadata',
            name='mild_percentage',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='coronadata',
            name='recovered',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coronadata',
            name='recovered_or_discharged',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coronadata',
            name='recovered_or_discharged_percentage',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='coronadata',
            name='serious',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coronadata',
            name='serious_percentage',
            field=models.FloatField(default=0.0),
        ),
    ]
