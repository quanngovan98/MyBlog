# Generated by Django 2.0.5 on 2018-05-29 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_auto_20180529_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='demo',
        ),
    ]
