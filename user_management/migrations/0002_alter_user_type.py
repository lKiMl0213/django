# Generated by Django 5.2 on 2025-04-19 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('HR', 'Human Resources'), ('STORAGE', 'Storage'), ('MARKET', 'Market')], max_length=10),
        ),
    ]
