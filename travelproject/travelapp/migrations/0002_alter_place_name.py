# Generated by Django 4.2.4 on 2023-08-08 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
