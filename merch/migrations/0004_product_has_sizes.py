# Generated by Django 3.0.8 on 2020-11-23 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merch', '0003_auto_20200807_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_sizes',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]