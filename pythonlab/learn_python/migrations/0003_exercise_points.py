# Generated by Django 2.2.5 on 2019-09-24 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_python', '0002_auto_20190923_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='points',
            field=models.PositiveSmallIntegerField(default=10, verbose_name='punkty za zadanie'),
            preserve_default=False,
        ),
    ]
