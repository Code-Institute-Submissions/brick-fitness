# Generated by Django 3.0.8 on 2020-11-30 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0011_auto_20201130_0742'),
        ('user_profiles', '0004_auto_20201114_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='active_meal_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plans.MealPlan'),
        ),
    ]
