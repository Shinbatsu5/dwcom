from django.db import models
class Articles(models.Model):
    title = models.CharField('Название', max_length=90)
    photo = models.ImageField(blank=True, upload_to="media/main/image/", verbose_name='Фото', null=True)
    full_text = models.TextField('Статья')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date']