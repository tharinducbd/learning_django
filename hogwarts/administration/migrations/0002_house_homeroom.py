# Generated by Django 5.0.4 on 2024-05-07 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='homeroom',
            field=models.CharField(default='specify...', max_length=32),
            preserve_default=False,
        ),
    ]