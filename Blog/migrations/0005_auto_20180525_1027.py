# Generated by Django 2.0.5 on 2018-05-25 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_auto_20180525_1027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cagetory',
            old_name='title',
            new_name='name',
        ),
    ]