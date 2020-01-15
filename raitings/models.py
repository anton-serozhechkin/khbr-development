from django.db import models
from django.urls import reverse
from django.utils import timezone

def upload_raiting_images_folder(instance, filename):
    filename = instance.id + '.' + filename.split('.')[-1]
    return "{}/{}".format(instance.id, filename)

class Raiting(models.Model):
    title = models.CharField('Заголовок',max_length=200)
    slug = models.SlugField('Ссылка')
    content = models.TextField('Контент')
    author = models.TextField('Автор', blank=True)
    image = models.ImageField('Фотография', blank=True, upload_to=upload_raiting_images_folder)
    created = models.DateTimeField('Дата создания', default=timezone.now)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('raiting_detail', kwargs={'slug': self.slug})