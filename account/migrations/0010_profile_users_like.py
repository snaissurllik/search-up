# Generated by Django 4.1.6 on 2023-02-21 11:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0009_profile_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='users_like',
            field=models.ManyToManyField(related_name='profiles_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
