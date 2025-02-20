# Generated by Django 5.1.2 on 2024-10-31 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=3)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.PositiveIntegerField()),
                ('barcode', models.CharField(max_length=50, unique=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.price')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.producttype')),
            ],
        ),
    ]
