# Generated by Django 4.1.6 on 2023-03-02 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_region_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
