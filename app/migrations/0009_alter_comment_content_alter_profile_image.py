# Generated by Django 5.1.3 on 2024-12-12 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_content_image_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='app.content'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='profile_images\x824\n\x08\\default.jpg', null=True, upload_to='profile_images/%Y/%m/%d/'),
        ),
    ]
