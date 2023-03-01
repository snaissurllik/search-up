# Generated by Django 4.1.6 on 2023-02-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_profile_city_profile_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='time_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='country',
        ),
        migrations.AlterField(
            model_name='profile',
            name='tags',
            field=models.ManyToManyField(related_name='profiles', to='account.tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.ManyToManyField(related_name='profiles', to='account.city'),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.ManyToManyField(related_name='profiles', to='account.country'),
        ),
    ]
