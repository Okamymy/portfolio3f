# Generated by Django 4.2.6 on 2023-10-27 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(default='Generic Category Name', max_length=32)),
                ('description', models.CharField(default='Generic Category Description', max_length=256)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('update_category', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=16)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='Generic Category Name', max_length=32)),
                ('description', models.CharField(default='Generic Category Description', max_length=256)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('update_category', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=16)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(default='Generic Category Name', max_length=32)),
                ('description', models.CharField(default='Generic Category Description', max_length=256)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('update_category', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=16)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='Generic Category Name', max_length=32)),
                ('description', models.CharField(default='Generic Category Description', max_length=256)),
                ('stock', models.IntegerField(default=0)),
                ('price_cost', models.FloatField(default=0.0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products_images')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('update_category', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=16)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.brand')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subcategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
