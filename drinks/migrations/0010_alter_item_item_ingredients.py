# Generated by Django 4.2.1 on 2023-05-26 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0009_alter_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_ingredients',
            field=models.CharField(default='TBU', max_length=400),
        ),
    ]
