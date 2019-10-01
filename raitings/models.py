from django.db import models
from django.urls import reverse
from django.utils import timezone

class Raiting(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Заголовок',max_length=200)
    content = models.TextField('Контент')
    author = models.TextField('Автор',default='')
    like = models.PositiveIntegerField('Лайки',default=0)
    image = models.ImageField('Фотография')#,upload_to=generate_filename, default='')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
    
    def get_absolute_url(self):
        return reverse('raiting_detail', kwargs={'id': self.id})