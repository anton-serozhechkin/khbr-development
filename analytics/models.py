from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.core.mail import send_mail
from khbr.settings import EMAIL_HOST_USER

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    slug = models.SlugField('Ссылка')
    bio = HTMLField('Немного о себе')
    avatar = models.ImageField(verbose_name='Аватар', upload_to='avatars/', blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('authors_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Category(models.Model):
    name = models.CharField('Название', max_length=100)  
    slug = models.SlugField('Ссылка', unique=True)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article_by_categ', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Article(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=120)
    slug = models.SlugField('Ссылка')
    short_description = HTMLField('Короткое описание на 200 символов', max_length=200)
    image = models.ImageField("Фотография", upload_to='article/%Y/%m/%h/')
    content = HTMLField("Контент")
    integer_of_day = models.BooleanField('Цифра дня', default=False)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, verbose_name="Автор")
    created = models.DateTimeField('Дата создания', default=timezone.now)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')
    views = models.PositiveIntegerField('Просмотров публикации', default=0)
    send_email = models.BooleanField(default=True, verbose_name='Отправить на рассылку')

    def __str__(self):
        return self.title
            
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'category_slug': self.category.slug, 'slug': self.slug})
    
    def save(self):
        if self.created:
            subscribers = Subscribe.objects.values_list('email', flat=True)
            if subscribers and self.send_email == True:
                with open('templates/mails/analytic.txt', 'r+', encoding='UTF-8') as f:
                    old_file_content = f.readline() # read everything in the file
                    new_email_content = old_file_content.format(self.title)
                    send_mail(
                            str(self.title),
                            str(new_email_content),
                            'khbr.info@gmail.com',
                            subscribers,
                            fail_silently=False
                            )

            super(Article, self).save()


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Links(models.Model):
    name = models.CharField('Название соц.сети', max_length=50)
    link = models.CharField('Ссылка', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Соц.сеть'
        verbose_name_plural = 'Соц.сети'

class Subscribe(models.Model):
    email = models.EmailField(verbose_name='Электронная почта', unique=True)
    created = models.DateTimeField('Дата создания', default=timezone.now)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Подписчик на рассылку'
        verbose_name_plural = 'Подписчики на рассылку'

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Пост')
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
        verbose_name = 'Фотография поста'
        verbose_name_plural = 'Фотографии постов'