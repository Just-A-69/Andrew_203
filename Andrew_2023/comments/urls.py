from django.urls import path
from . import views


urlpatterns = [
    path('', views.comments_index, name='comments_index'),
    path('<int:pk>/', views.comments_detail, name='comments_detail'),
    path('category/<name>/', views.comments_cat, name='comments_category')
]
