# Generated by Django 4.0.3 on 2022-05-15 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
