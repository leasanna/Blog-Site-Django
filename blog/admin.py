from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import News, Category, Tag, Author



class NewsAdminForm(forms.ModelForm):
    """Добавление ckeditor"""
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


@admin.register(News)
class PostAdmin(admin.ModelAdmin):
    form = NewsAdminForm

    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tag)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Author)
class PostAdmin(admin.ModelAdmin):
    pass
