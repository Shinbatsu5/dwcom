# Generated by Django 5.0.6 on 2024-05-15 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partners',
            options={'ordering': ['-category'], 'verbose_name': 'Компания', 'verbose_name_plural': 'Компании'},
        ),
    ]
