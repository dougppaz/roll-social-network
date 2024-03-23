# Generated by Django 5.0.3 on 2024-03-23 18:43

import django.core.files.storage
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0004_alter_post_options_alter_post_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='timeline.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(max_length=256, storage=django.core.files.storage.FileSystemStorage(), upload_to='photos'),
        ),
    ]