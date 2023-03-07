from django.db import models
from django.urls import reverse

"""
Post: 
    Title 
    
    Image - blunk=True
    
    Content
    
    Date
    
    Categories:
        Title
        Slug

    Tags:
        Title
        Slug

    Author: blunk=True
        Name

        Description

        Social Network:
            title
            link

    Сomment:
        SOON
    
    Is published - default=True
    
    Selected default=False
    
    Slug
"""


class News(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    image = models.ImageField(
        'Изображение', upload_to='image/%Y/%m/%d', blank=True)
    content = models.TextField('Контент')
    create_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', verbose_name='Категории')
    tags = models.ManyToManyField('Tag', verbose_name='Теги')
    author = models.ForeignKey(
        'Author', on_delete=models.PROTECT, blank=True, verbose_name='Автор')
    # comment =
    is_selected = models.BooleanField('Избранный', default=False)
    is_published = models.BooleanField('Публикация', default=True)
    slug = models.SlugField('URL', max_length=255, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-create_at']


class Category(models.Model):
    title = models.CharField('Название', max_length=100)
    slug = models.SlugField('URL', max_length=100, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField('Название', max_length=100)
    slug = models.SlugField('URL', max_length=100, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']


class Author(models.Model):
    name = models.CharField('Имя', max_length=100)
    slug = models.SlugField('URL', max_length=255, unique=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
        # return reverse("author_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['name']
