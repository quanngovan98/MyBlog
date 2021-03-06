# Generated by Django 2.0.5 on 2018-05-26 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_auto_20180525_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cagetory',
            name='name',
            field=models.CharField(default='none', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='cagetory',
            field=models.ForeignKey(default='0000000', on_delete=django.db.models.deletion.CASCADE, to='Blog.Cagetory', to_field='name'),
        ),
    ]
