from django.db import models
from django.urls import reverse
from django.utils import timezone

def upload_event_images_folder(instance, filename):
    filename = instance.id + '.' + filename.split('.')[-1]
    return "{}/{}".format(instance.id, filename)

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Заголовок',max_length=120)
    day = models.DateField('День события')
    start_time = models.TimeField('Начало', blank=True)
    end_time = models.TimeField('Конец', blank=True)
    place = models.CharField('Место', blank=True, max_length=300)
    image = models.ImageField('Фотография', blank=True, upload_to=upload_event_images_folder)
    notes = models.TextField('Заметки', blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')
    
    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
    
    def __str__(self):
        return "{0}: создано {1}".format(self.title, self.created)

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'id': self.id})