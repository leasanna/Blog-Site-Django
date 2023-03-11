from .models import Post, Category

from django.db.models import F
from django.views.generic import ListView, DetailView


class HomePage(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'news'

    def get_queryset(self):
        return Post.objects.filter(is_published=True)[:12]

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['selected'] = Post.objects.filter(
            is_published=True, is_selected=True)[:3]

        return contex


class NewsDetail(DetailView):
    model = Post
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)

        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()

        return contex


class CatigoriesInfo(ListView):
    model = Post
    template_name = 'blog/category.html'
    context_object_name = 'news'
    paginate_by = 12
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(is_published=True, categories__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['category'] = Category.objects.get(slug=self.kwargs['slug'])

        return contex


class TagsInfo(ListView):
    model = Post
