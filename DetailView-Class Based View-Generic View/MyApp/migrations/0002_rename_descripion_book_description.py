# Generated by Django 5.0.7 on 2024-08-09 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='descripion',
            new_name='description',
        ),
    ]
