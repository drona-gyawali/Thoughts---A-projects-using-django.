# Generated by Django 5.1.3 on 2024-12-05 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_content_user_alter_like_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
