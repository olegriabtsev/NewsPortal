from django.urls import path
# Импортируем созданное нами представление
from .views import NewsList, NewsDetail


urlpatterns = [
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('', NewsList.as_view()),

   # Добавьте новый URL-путь для деталей новости
   path('<int:pk>', NewsDetail.as_view()),
]
