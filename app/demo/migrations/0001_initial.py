# Generated by Django 3.2.4 on 2021-06-11 10:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('arrf_1d', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=3), null=True, size=None)),
                ('arrf_2d', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), null=True, size=2)),
                ('jfield', models.JSONField(null=True)),
            ],
        ),
    ]
