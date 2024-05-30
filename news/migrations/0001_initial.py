# Generated by Django 4.2.6 on 2024-05-12 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/main/image/', verbose_name='Фото')),
                ('full_text', models.TextField(verbose_name='Статья')),
                ('date', models.DateField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]