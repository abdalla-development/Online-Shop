# Generated by Django 3.2.7 on 2021-09-19 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0005_alter_cart_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user_id',
            field=models.IntegerField(default=1),
        ),
    ]
