# Generated by Django 3.0.4 on 2020-03-25 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corona_app', '0004_auto_20200325_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateDeathData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('death', models.IntegerField(default=0)),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name': 'Date Death',
                'ordering': ['-date'],
            },
        ),
        migrations.AlterModelOptions(
            name='datecasedata',
            options={'ordering': ['-date'], 'verbose_name': 'Date Case'},
        ),
    ]
