# Generated by Django 5.0.1 on 2024-02-04 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(max_length=256, upload_to='posts'),
        ),
    ]