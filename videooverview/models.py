from django.db import models
from django.urls import reverse
from django.utils import timezone
from embed_video.fields import EmbedVideoField

class VideoDownloading(models.Model):
    title = models.CharField('Заголовок',max_length=120, default='')
    url = models.CharField('Ссылка', max_length=200, help_text='Вводить только URL-страницы', default='')
    notes = models.TextField('Заметки', help_text='Заметки', blank=True, null=True)
    video = EmbedVideoField('Загрузить видео', blank=True, help_text='Заходим на страницу видео-Поделиться-Встроить-Копируем link, содержащий строку embeded')
    created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видеообзор'
        verbose_name_plural = 'Видеообзоры'

    