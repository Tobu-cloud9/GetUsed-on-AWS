# Generated by Django 3.2 on 2021-12-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GetUsed', '0002_search_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='sold_out',
        ),
        migrations.AddField(
            model_name='search',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='status'),
        ),
    ]
