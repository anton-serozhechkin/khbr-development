from django.db import models
from django.urls import reverse
from django.utils import timezone
from analytics.models import Author
from tinymce.models import HTMLField
from django.core.mail import send_mail
from khbr.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string
from pathlib import Path
from analytics.models import Subscribe

class Raiting(models.Model):
    title = models.CharField('Заголовок',max_length=200)
    slug = models.SlugField('Ссылка')
    short_description = HTMLField('Короткое описание на 200 символов', max_length=200)
    content = HTMLField("Контент")
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, verbose_name="Автор")
    image = models.ImageField('Фотография', upload_to='raitings/%Y/%m/%h/')
    created = models.DateTimeField('Дата создания', default=timezone.now)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')
    views = models.PositiveIntegerField('Просмотров публикации', default=0)
    send_email = models.BooleanField(default=True, verbose_name='Отправить на рассылку')

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('raiting_detail', kwargs={'slug': self.slug})

    def save(self):
        if self.created:
            subscribers = Subscribe.objects.values_list('email', flat=True)
            if subscribers and self.send_email == True:
                image = Path(self.image.url).name
                html_message = render_to_string('../templates/mails/ratings.html', {'title': self.title,
                                                                                    'short_description': self.short_description, 
                                                                                    'image': image,
                                                                                    'slug': self.slug
                                                                                    })
                send_mail(
                        'Рассылка от KHBR - Рейтинги',
                        '',
                        EMAIL_HOST_USER,
                        subscribers,
                        fail_silently=False,
                        html_message=html_message
                        )

            super(Raiting, self).save()

class RaitingImage(models.Model):
    raiting = models.ForeignKey(Raiting, on_delete=models.CASCADE, verbose_name='Рейтинг')
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
        verbose_name = 'Фотография рейтинга'
        verbose_name_plural = 'Фотографии рейтингов'