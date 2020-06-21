from django.db import models
from django.urls import reverse
from django.utils import timezone
from tinymce.models import HTMLField
from analytics.models import Author
from django.contrib.auth.models import User

class Poll(models.Model):
    title = models.CharField('Заголовок', max_length=120)
    slug = models.SlugField('Ссылка')
    content = HTMLField("Контент")
    question = HTMLField("Вопрос")
    image = models.ImageField("Фотография", upload_to='poll/%Y/%m/%h/', blank=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, verbose_name="Автор")
    created = models.DateTimeField('Дата создания', default=timezone.now)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')
    views = models.PositiveIntegerField('Просмотров публикации', default=0)

    def __str__(self):
        return self.title
            
    def get_absolute_url(self):
        return reverse('poll_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

class Answer(models.Model):
    poll = models.ForeignKey(Poll, verbose_name='Опрос', on_delete=models.CASCADE)
    text = models.CharField('Ответ', max_length=50)
    counter = models.IntegerField('Количество проголосовавших', default=0)

    def __str__(self):
        return 'Опрос {}, кол-во проголосовавших - {}'.format(self.poll.title, self.counter)
                
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name='Опрос')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, verbose_name='Ответ пользователя')

    def __str__(self):
        return 'Опрос {}, пользователь - {}'.format(self.poll.title, self.user.username)
                
    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователей'