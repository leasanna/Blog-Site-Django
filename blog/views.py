from .models import Post, Category
from .forms import CommentForm

from django.db.models import F
from django.shortcuts import redirect
from django.views.generic import View
from django.views.generic import ListView, DetailView


class HomePage(ListView):
    """Домашняя страница"""
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.filter(is_published=True)[:12]

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['selected'] = Post.objects.filter(
            is_published=True, is_selected=True)[:3]

        return contex


class NewsDetail(DetailView):
    """Пост"""
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)

        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()

        return contex


class CatigoriesInfo(ListView):
    """Категории"""
    model = Post
    template_name = 'blog/category.html'
    context_object_name = 'post'
    paginate_by = 12
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(is_published=True, categories__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['category'] = Category.objects.get(slug=self.kwargs['slug'])

        return contex


class TagsInfo(ListView):
    """Теги"""
    model = Post


class Search(ListView):
    """Посик"""
    template_name = 'blog/search.html'
    context_object_name = 'post'
    paginate_by = 12

    def get_queryset(self):
        return Post.objects.filter(is_published=True, title__icontains=self.request.GET.get('s'))

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['s'] = self.request.GET.get('s')

        return contex


class AddCommnet(View):
    """Коментарии"""
    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = Post.objects.get(id=pk)

        if form.is_valid():
            form = form.save(commit=False)

            if res := request.POST.get('parent'):
                form.parent_id = int(res)

            form.post = post
            form.save()

        return redirect(post.get_absolute_url())
