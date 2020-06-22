from django.db import models
from django.urls import reverse
from django.utils import timezone
from analytics.models import Author
from tinymce.models import HTMLField

class Event(models.Model):
    title = models.CharField('Заголовок',max_length=120)
    slug = models.SlugField('Ссылка')
    short_description = HTMLField('Короткое описание на 200 символов', max_length=200)
    day = models.DateField('День события')
    start_time = models.TimeField('Начало', null=True, blank=True)
    end_time = models.TimeField('Конец', null=True, blank=True)
    place = models.CharField('Место', blank=True, max_length=300)
    image = models.ImageField('Фотография', upload_to='event/%Y/%m/%h/')
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, verbose_name="Автор")
    content = HTMLField("Контент")
    created = models.DateTimeField('Дата создания', default=timezone.now)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')
    views = models.PositiveIntegerField('Просмотров публикации', default=0)
    
    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'slug': self.slug})


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Выберите событие')
    title = models.CharField('Название картинки', blank=True, null=True, max_length=50)
    image = models.ImageField(upload_to='article_inside/%Y/%m/%h/', verbose_name='Загрузить картинку')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    created = models.DateTimeField('Дата создания', default=timezone.now)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.author.user.username
            
    class Meta:
        verbose_name = 'Фотография события'
        verbose_name_plural = 'Фотографии событий'