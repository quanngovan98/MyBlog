# Generated by Django 2.0.5 on 2018-05-29 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_post_slugifytitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='demo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slugifytitle',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
