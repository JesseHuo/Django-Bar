# Generated by Django 4.2.1 on 2023-05-18 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='fav_base_spirits',
        ),
        migrations.AddField(
            model_name='profile',
            name='favorite_base_spirits',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
