# Generated by Django 5.1.3 on 2024-12-01 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_remove_cart_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(to='homepage.booksupload'),
        ),
    ]
