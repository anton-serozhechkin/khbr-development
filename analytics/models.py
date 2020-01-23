from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from tinymce import HTMLField
from django.contrib.auth import get_user_model

User = get_user_model()

"""class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    article = models.ForeignKey('Article', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Коментарии к посту'
        verbose_name_plural = 'Коментарии к постам'
"""

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Просмотры поста'
        verbose_name_plural = 'Просмотры постов'


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

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
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created = models.DateTimeField('Дата создания', default=timezone.now)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, null=True, blank=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
            
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={
            'slug': self.slug
        })
    #@property
    #def get_comments(self):
    #    return self.comments.all().order_by('-created')
    
    @property
    def view_count(self):
        return PostView.objects.filter(article=self).count()

    #@property
    #def comment_count(self):
    #    return Comment.objects.filter(article=self).count()
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'