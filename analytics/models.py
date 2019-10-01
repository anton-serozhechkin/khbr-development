from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings


class Category(models.Model):
    name = models.CharField('Название',max_length=100)  
    slug = models.SlugField('Ссылка')
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category,verbose_name="Категория",on_delete=models.CASCADE)
    title = models.CharField('Заголовок',max_length=120)
    slug = models.SlugField("Ссылка")
    image = models.ImageField("Фотография")#,upload_to=generate_filename)
    content = models.TextField("Контент")
    author = models.TextField("Автор", default='')
    like = models.PositiveIntegerField("Лайки", default=0)
    users_reaction = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='Кто отреагировал на пост', blank=True)
    created = models.DateTimeField(default=timezone.now)
     
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'category': self.category.slug, 'id': self.id})
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'