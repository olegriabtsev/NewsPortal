from django.urls import path
# Импортируем созданное нами представление
from .views import NewsList, NewsDetail


urlpatterns = [
   path('', NewsList.as_view(), name='news-list'),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>/', NewsList.as_view(), name='news_list'),

   # Добавьте новый URL-путь для деталей новости
   path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),
]
