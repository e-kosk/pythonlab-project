# Generated by Django 2.2.5 on 2019-09-26 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn_python', '0010_auto_20190926_1742'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='message',
            unique_together=set(),
        ),
    ]