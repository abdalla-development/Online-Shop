# Generated by Django 3.2.7 on 2021-09-13 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=500)),
                ('category', models.CharField(max_length=500)),
                ('price', models.CharField(max_length=500)),
                ('quantity', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('amount', models.CharField(max_length=500)),
                ('colors', models.CharField(max_length=500)),
                ('sizes', models.CharField(max_length=500)),
                ('user_id', models.CharField(max_length=500)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]