from django.db import models
from django.urls import reverse
from django.utils import timezone
from embed_video.fields import EmbedVideoField
from tinymce import HTMLField
from django.contrib.auth import get_user_model
from analytics.models import Author

User = get_user_model()

class VideoView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey('Video', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Video(models.Model):
    title = models.CharField('Заголовок',max_length=120)
    slug = models.SlugField('Ссылка внутри сайта')
    overview = models.TextField('Краткий обзор видео')
    url = models.CharField('Ссылка на видео из источника', max_length=200, help_text='URL-страницы')
    content = HTMLField("Контент")
    author = models.ForeignKey(Author, verbose_name='Автор видео', on_delete=models.CASCADE)
    video = EmbedVideoField('Загрузить видео', help_text='Заходим на страницу видео-Поделиться-Встроить-Копируем link, содержащий строку embeded')
    created = models.DateTimeField('Дата создания', default=timezone.now)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')
    previous_video = models.ForeignKey('self', verbose_name='Предыдущее видео', related_name='video_previous', on_delete=models.SET_NULL, null=True, blank=True)
    next_video = models.ForeignKey('self', verbose_name='Следующее видео', related_name='video_next', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Видеообзор'
        verbose_name_plural = 'Видеообзоры'
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('videooverview_detail', kwargs={
            'slug': self.slug
        })

    @property
    def view_count(self):
        return VideoView.objects.filter(video=self).count()
