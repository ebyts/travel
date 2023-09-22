# Generated by Django 4.2.4 on 2023-08-07 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('image', models.ImageField(upload_to='pics')),
                ('description', models.TextField()),
            ],
        ),
    ]

          