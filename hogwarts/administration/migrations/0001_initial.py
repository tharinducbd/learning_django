# Generated by Django 5.0.4 on 2024-05-07 12:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('founder', models.CharField(max_length=64)),
                ('emblem', models.CharField(max_length=64)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students_of_house', to='administration.house')),
                ('subjects', models.ManyToManyField(to='administration.subject')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('age', models.IntegerField()),
                ('subjects', models.ManyToManyField(to='administration.subject')),
            ],
            options={
                'ordering': ['name', '-age'],
            },
        ),
        migrations.AddField(
            model_name='house',
            name='head',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='administration.teacher'),
        ),
    ]
