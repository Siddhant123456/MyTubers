# Generated by Django 3.2 on 2021-04-27 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0002_auto_20210424_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtuber',
            name='email',
            field=models.CharField(default='Siddhant.17504@sscbs.du.ac.in', max_length=255),
        ),
    ]