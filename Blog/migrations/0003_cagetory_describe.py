# Generated by Django 2.0.5 on 2018-05-25 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20180525_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='cagetory',
            name='describe',
            field=models.CharField(default='none', max_length=200),
        ),
    ]
