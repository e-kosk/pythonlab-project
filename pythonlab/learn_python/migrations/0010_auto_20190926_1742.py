# Generated by Django 2.2.5 on 2019-09-26 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_python', '0009_auto_20190926_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='data'),
        ),
    ]
