# Generated by Django 2.2 on 2019-12-22 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='Central',
            field=models.IntegerField(default=0),
        ),
    ]