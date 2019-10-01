from django.db import models
from django.urls import reverse
from django.utils import timezone

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Заголовок',max_length=120)
    day = models.DateField('День события', help_text='День события')
    start_time = models.TimeField('Начало', help_text='Начало')
    end_time = models.TimeField('Конец', help_text='Окончание')
    place = models.CharField('Место',max_length=120, default='')
    image = models.ImageField('Фотография')#,upload_to=generate_filename, default='')
    notes = models.TextField('Заметки', help_text='Заметки', blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'id': self.id})