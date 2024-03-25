# Generated by Django 5.0.3 on 2024-03-25 00:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('social', '0002_alter_userprofile_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='sites.site'),
        ),
    ]
