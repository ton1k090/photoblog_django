from django.db import models
from django.urls import reverse
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


class Biography(models.Model):
    """Модель автора"""
    first_name = models.CharField('Имя', max_length=120)
    last_name = models.CharField('Фамилия', max_length=120)
    image = models.ImageField('Фото', upload_to='users/')
    biography = models.TextField('О себе')
    achievements = models.TextField('Достижения')
    experience = models.PositiveSmallIntegerField('Стаж', default=0)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Биография'
        verbose_name_plural = 'Биографии'


class Testimonial(models.Model):
    name = models.ForeignKey(Biography, on_delete=models.CASCADE)
    text = models.TextField('Текст Свидетельства')
    image = models.ImageField('Фото', upload_to='testimonial/', default=None)

    class Meta:
        verbose_name = 'Свидетельство'
        verbose_name_plural = 'Свидетельство'


class Post(models.Model):
    """Модель постов"""
    author = models.ForeignKey(Biography, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=200)
    image = models.ImageField('Изображение', upload_to='articles/')
    text = models.TextField('Текст')
    created_at = models.DateTimeField('Дата', auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True)


    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def get_comments(self):
        return self.comment.all()


class Comment(models.Model):
    '''Класс модели комментариев'''
    name = models.CharField('Имя', max_length=50)
    email = models.CharField('Почта', max_length=100)
    website = models.CharField('Сайт', max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    message = models.TextField('Сообщение', max_length=500)
    post = models.ForeignKey(
        Post,
        related_name='comment',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Photo(models.Model):
    """Класс модели галереи"""
    name = models.CharField('Название', max_length=250)
    image = models.ImageField('Изображение', upload_to='gallery')
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['image']

    def get_thumbnail(self):
        return self.image.url