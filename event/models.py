from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from tinymce import HTMLField
from django.contrib.auth import get_user_model
from analytics.models import Author

User = get_user_model()

class EventView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Event(models.Model):
    title = models.CharField('Заголовок',max_length=120)
    slug = models.SlugField('Ссылка')
    overview = models.TextField('Краткий обзор события')
    place = models.CharField('Место', blank=True, max_length=300)
    day = models.DateField('День события')
    start_time = models.TimeField('Начало', blank=True)
    end_time = models.TimeField('Конец', blank=True)
    thubmnail = models.ImageField('Заставка', blank=True)
    content = HTMLField("Контент", blank=True)
    author = models.ForeignKey(Author, verbose_name='Автор события', on_delete=models.CASCADE)
    created = models.DateTimeField('Дата создания', default=timezone.now)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')
    previous_event = models.ForeignKey('self', related_name='event_previous', verbose_name='Предыдущее событие', on_delete=models.SET_NULL, null=True, blank=True)
    next_event = models.ForeignKey('self', related_name='event_next', verbose_name='Следующее событие', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('event_detail', kwargs={
            'slug': self.slug
            })
    
    @property
    def view_count(self):
        return EventView.objects.filter(event=self).count()
