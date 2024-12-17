# Generated by Django 5.1.4 on 2024-12-17 07:13

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('location', models.CharField(max_length=255)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('size', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)])),
                ('property_history', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyOwner',
            fields=[
                ('nid', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('contact_info', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('nid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('members', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('adults', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('women', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('flat_no', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('room', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('bath', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('attached_bath', models.IntegerField(blank=True, default=False, null=True)),
                ('drawing', models.BooleanField(blank=True, default=False, null=True)),
                ('dining', models.BooleanField(blank=True, default=False, null=True)),
                ('size', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('rent_amount', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('floor', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='flats', to='user.user')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flats', to='properties.property')),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_description', models.TextField()),
                ('request_date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_requests', to='properties.flat')),
                ('tenant', models.ForeignKey(limit_choices_to={'user_type': 4}, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='properties.propertyowner'),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('plan', models.CharField(blank=True, max_length=50, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='properties.propertyowner')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='properties.property')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField(help_text='Month for which the rent is being paid (1-12).', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2000)])),
                ('flat', models.ForeignKey(help_text='The flat for which rent is being paid.', on_delete=django.db.models.deletion.CASCADE, to='properties.flat')),
                ('tenant', models.ForeignKey(help_text='The tenant paying the rent.', on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('flat', 'tenant', 'month'), name='unique_rent_per_tenant_per_month')],
            },
        ),
    ]