# Generated by Django 3.2.4 on 2021-06-10 03:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=100)),
                ('work_time', models.CharField(blank=True, max_length=100)),
                ('tel', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('item1', models.CharField(blank=True, max_length=200)),
                ('item1_price', models.CharField(blank=True, max_length=200)),
                ('item2', models.CharField(blank=True, max_length=200)),
                ('item2_price', models.CharField(blank=True, max_length=200)),
                ('item3', models.CharField(blank=True, max_length=200)),
                ('item3_price', models.CharField(blank=True, max_length=200)),
                ('item4', models.CharField(blank=True, max_length=200)),
                ('item4_price', models.CharField(blank=True, max_length=200)),
                ('photo_main', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
