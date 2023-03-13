from django.db import models
from django.urls import reverse


class Post(models.Model):
    """Пост"""
    title = models.CharField('Заголовок', max_length=255)
    image = models.ImageField(
        'Изображение', upload_to='image/%Y/%m/%d')
    content = models.TextField('Контент')
    create_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField('Количество просмотров', default=0)
    categories = models.ManyToManyField('Category', verbose_name='Категории')
    tags = models.ManyToManyField('Tag', verbose_name='Теги')
    author = models.ForeignKey(
        'Author', on_delete=models.PROTECT, blank=True, verbose_name='Автор')
    is_selected = models.BooleanField('Избранный', default=False)
    is_published = models.BooleanField('Публикация', default=True)
    slug = models.SlugField('URL', max_length=255, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def get_comment(self):
        return self.comment_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-create_at']


class Category(models.Model):
    """Категория"""
    title = models.CharField('Название', max_length=100)
    slug = models.SlugField('URL', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})


class Tag(models.Model):
    """Тег"""
    title = models.CharField('Название', max_length=100)
    slug = models.SlugField('URL', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"slug": self.slug})


class Author(models.Model):
    """Автор"""
    name = models.CharField('Имя', max_length=100)
    image = models.ImageField(
        'Изображение', upload_to='image/author/', blank=True)
    content = models.TextField('Контент', default='')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['name']

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Почта')
    content = models.TextField('Контент', default='')
    create_at = models.DateTimeField('Время написания', auto_now_add=True)
    parent = models.ForeignKey(
        'self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True)
    post = models.ForeignKey(Post, verbose_name='Пост',
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ['-create_at']

    def __str__(self):
        return f"{self.name} - {self.post}"
