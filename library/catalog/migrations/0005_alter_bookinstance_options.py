# Generated by Django 5.0.6 on 2024-08-19 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['book', 'due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'), ('can_renew', "Renew the book's loaned period"))},
        ),
    ]
