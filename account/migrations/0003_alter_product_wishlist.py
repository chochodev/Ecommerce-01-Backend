# Generated by Django 4.1.1 on 2022-11-29 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_product_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='wishlist',
            field=models.BooleanField(default=False, null=True),
        ),
    ]