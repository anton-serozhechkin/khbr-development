from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from tinymce import HTMLField
from django.contrib.auth import get_user_model
from analytics.models import Author

User = get_user_model()

class RaitingView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    raiting = models.ForeignKey('Raiting', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Просмотры рейтинга'
        verbose_name_plural = 'Просмотры рейтингов'


class Raiting(models.Model):
    title = models.CharField('Заголовок',max_length=200)
    slug = models.SlugField('Ссылка')
    overview = models.TextField('Краткий обзор рейтинга')
    content = HTMLField('Контент')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thubmnail = models.ImageField('Фотография', blank=True)
    created = models.DateTimeField('Дата создания', default=timezone.now)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')
    previous_raiting = models.ForeignKey('self', related_name='raiting_previous', on_delete=models.SET_NULL, null=True, blank=True)
    next_raiting = models.ForeignKey('self', related_name='raiting_next', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('raiting_detail', kwargs={'slug': self.slug})

    @property
    def view_count(self):
        return RaitingView.objects.filter(raiting=self).count()
