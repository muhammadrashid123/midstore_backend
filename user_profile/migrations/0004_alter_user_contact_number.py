# Generated by Django 4.0.3 on 2022-05-17 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_user_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact_number',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
