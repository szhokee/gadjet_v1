# Generated by Django 4.1.7 on 2023-02-17 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Название продукта')),
                ('model', models.CharField(max_length=50, null=True, verbose_name='Модель')),
                ('price', models.DecimalField(decimal_places=10, max_digits=1000, verbose_name='сом')),
                ('color', models.CharField(max_length=50, null=True)),
                ('nalich', models.BooleanField(verbose_name='В наличии')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание продукта')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product')),
            ],
        ),
    ]