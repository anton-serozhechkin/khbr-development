from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from tinymce import HTMLField
from django.contrib.auth import get_user_model

User = get_user_model()

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Author(models.Model):
    user = models.OneToOneField(User, verbose_name='Выберите пользователя', on_delete=models.CASCADE)
    profile_picture = models.ImageField(verbose_name='Фотография пользователя')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Category(models.Model):
    name = models.CharField('Название',max_length=100)  
    slug = models.SlugField('Ссылка', unique=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article_by_categ', kwargs={
            'slug': self.slug
        })
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=120)
    slug = models.SlugField('Ссылка')
    overview = models.TextField('Краткий обзор статьи')
    categories = models.ManyToManyField(Category, verbose_name="Категория",)
    content = HTMLField("Контент")
    thubmnail = models.ImageField("Фотография", blank=True)
    author = models.ForeignKey(Author, verbose_name='Автор статьи', on_delete=models.CASCADE)
    created = models.DateTimeField('Дата создания', default=timezone.now)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')
    previous_post = models.ForeignKey('self', verbose_name='Предыдущий пост', related_name='previous', on_delete=models.SET_NULL, null=True, blank=True)
    next_post = models.ForeignKey('self', verbose_name='Следующий пост', related_name='next', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
            
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={
            'slug': self.slug
        })

    @property
    def view_count(self):
        return PostView.objects.filter(article=self).count()

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Signup(models.Model):
    email = models.EmailField('Электронный адрес подписчика')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'