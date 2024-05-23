# Generated by Django 4.1.13 on 2024-05-23 14:06

import apps.categories.enums
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('Uncategorized', 'UNCATEROGIZED'), ('Sports', 'SPORTS'), ('Technology', 'TECHNOLOGY'), ('Entertainment', 'ENTERTAINMENT'), ('Politics', 'POLITICS'), ('Health', 'HEALTH'), ('Education', 'EDUCATION')], default=apps.categories.enums.Category['UNCATEROGIZED'], max_length=20),
        ),
    ]
