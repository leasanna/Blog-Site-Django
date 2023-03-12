from django.urls import path
from .views import HomePage, NewsDetail, TagsInfo, CatigoriesInfo, Search

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    path('news/<slug:slug>', NewsDetail.as_view(), name='post_detail'),
    path('tags/<slug:slug>', TagsInfo.as_view(), name='tag_detail'),
    path('catigories/<slug:slug>', CatigoriesInfo.as_view(), name='category_detail'),
    path('search/', Search.as_view(), name='search'),
]
