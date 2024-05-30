from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        verbose_name: str = "Категорию"
        verbose_name_plural: str = 'Категории'

    def __str__(self):
        return self.name




class Partners(models.Model):
    title = models.CharField('Название', max_length=90)
    photo = models.ImageField(blank=True, upload_to="media/main/image/", verbose_name='Фото', null=True)
    full_text = models.TextField('Описание')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name: str = "Компания"
        verbose_name_plural: str = 'Компании'
        ordering = ['-category']



