# Generated by Django 3.2.4 on 2021-06-11 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='balance',
            field=models.IntegerField(null=True),
        ),
    ]
