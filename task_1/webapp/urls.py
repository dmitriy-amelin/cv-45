from django.urls import path
from webapp.views import index_view, article_view, article_create_view

urlpatterns = [
    path('', index_view),
    path('article/add/', article_create_view),
    path('article/', article_view),
]