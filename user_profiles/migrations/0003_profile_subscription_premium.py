# Generated by Django 3.0.8 on 2020-11-14 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0002_auto_20201113_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='subscription_premium',
            field=models.BooleanField(default=False),
        ),
    ]
