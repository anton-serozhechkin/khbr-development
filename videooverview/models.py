from django.db import models
from django.urls import reverse
from django.utils import timezone
from embed_video.fields import EmbedVideoField

class VideoDownloading(models.Model):
    title = models.CharField('Заголовок',max_length=120, blank=True)
    url = models.CharField('Ссылка', max_length=200, help_text='URL-страницы')
    notes = models.TextField('Заметки', help_text='Заметки', blank=True, null=True)
    video = EmbedVideoField('Загрузить видео', blank=True, help_text='Заходим на страницу видео-Поделиться-Встроить-Копируем link, содержащий строку embeded')
    created = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')

    def __str__(self):
        return "{} создано {}".format(self.title, self.created.strftime('%Y-%m-%d %H:%M'))
                    
    class Meta:
        verbose_name = 'Видеообзор'
        verbose_name_plural = 'Видеообзоры'

    