from django.db import models
from django.urls import reverse
from django.utils import timezone

def upload_raiting_images_folder(instance, filename):
    filename = instance.id + '.' + filename.split('.')[-1]
    return "{}/{}".format(instance.id, filename)

class Raiting(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Заголовок',max_length=200)
    content = models.TextField('Контент')
    author = models.TextField('Автор')
    image = models.ImageField('Фотография',upload_to=upload_raiting_images_folder)
    created = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
    
    def __str__(self):
        return "{}: создано {}".format(self.title, self.created)
    
    def get_absolute_url(self):
        return reverse('raiting_detail', kwargs={'id': self.id})