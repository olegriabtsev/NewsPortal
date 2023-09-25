from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime
from .templatetags import custom_filters, custom_tags


class NewsList(ListView):
    model = Post
    ordering = 'created_date'  # Отсортируем по дате публикации, чтобы новые новости были первыми
    template_name = 'default.html'  # Используем шаблон default.html
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Распродажа в среду!"
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'default.html'  # Используем шаблон default.html
    context_object_name = 'post'
