# Generated by Django 4.0.2 on 2022-10-22 08:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_post_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='likes_field', to=settings.AUTH_USER_MODEL),
        ),
    ]
