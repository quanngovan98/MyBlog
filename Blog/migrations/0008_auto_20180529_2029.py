# Generated by Django 2.0.5 on 2018-05-29 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_remove_post_demo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slugifytitle',
            field=models.CharField(default='no need to fill', max_length=100, unique=True),
        ),
    ]
