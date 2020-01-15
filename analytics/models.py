from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings


class Category(models.Model):
    name = models.CharField('Название',max_length=100)  
    slug = models.SlugField('Ссылка', unique=True)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article_by_categ', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


def upload_article_images_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[-1]
    return "{}/{}".format(instance.slug, filename)


class Article(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=120)
    slug = models.SlugField('Ссылка')
    image = models.ImageField("Фотография", blank=True, upload_to=upload_article_images_folder)
    content = models.TextField("Контент")
    author = models.TextField("Автор", blank=True)
    created = models.DateTimeField('Дата создания', default=timezone.now)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')

    def __str__(self):
        return self.title
            
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'