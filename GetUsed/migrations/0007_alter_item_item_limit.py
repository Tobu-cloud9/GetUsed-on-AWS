# Generated by Django 3.2 on 2021-12-23 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GetUsed', '0006_search_quality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_limit',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='time_limit'),
        ),
    ]
