# Generated by Django 4.0.3 on 2022-05-20 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='available_products',
            new_name='stock',
        ),
    ]
