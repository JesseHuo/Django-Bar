# Generated by Django 4.2.1 on 2023-05-18 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_fav_base_spirits_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favorite_base_spirits',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
