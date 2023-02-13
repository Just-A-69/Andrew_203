from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('preview.urls')),
    path('comments/', include('comments.urls')),
    path('me/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts')
]
