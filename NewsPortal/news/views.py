from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime
from .templatetags import custom_filters, custom_tags


class NewsList(ListView):
    model = Post
    ordering = 'title'  # Отсортируем по дате публикации, чтобы новые новости были первыми
    template_name = 'posts.html'  # Используем шаблон default.html
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'post.html'  # Используем шаблон default.html
    context_object_name = 'post'
