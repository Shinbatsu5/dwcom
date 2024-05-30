from django.db import models

class Realise (models.Model):
    title = models.CharField('Название', max_length=120)
    photo = models.ImageField(blank=True, null=True, upload_to="media/main/image/", verbose_name='Фото')
    full_text = models.TextField('Статья')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name = 'Реализованный проект'
        verbose_name_plural = 'Реализованные проекты'
        ordering = ['-date']