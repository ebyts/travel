# Generated by Django 4.2.4 on 2023-08-08 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0005_alter_place_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=250)),
                ('image1', models.ImageField(upload_to='pics')),
                ('description1', models.TextField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.TextField(max_length=100),
        ),
    ]