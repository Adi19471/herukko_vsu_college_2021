# Generated by Django 3.0 on 2021-08-28 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210828_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.URLField(default=None, null=True),
        ),
    ]
