# Generated by Django 2.1.7 on 2019-03-19 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='capacity',
            field=models.IntegerField(verbose_name='Tour Capacity'),
        ),
    ]
