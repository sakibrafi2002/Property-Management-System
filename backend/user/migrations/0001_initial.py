# Generated by Django 5.1.4 on 2024-12-17 07:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('nid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('members', models.IntegerField(help_text='Total number of members in the household.', validators=[django.core.validators.MinValueValidator(1)])),
                ('adults', models.IntegerField(blank=True, help_text='Number of adults in the household.', null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('women', models.IntegerField(blank=True, help_text='Number of women in the household.', null=True, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]