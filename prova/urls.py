from django.contrib import admin
from django.urls import path, include
from .pessoas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('prova.pessoas.urls')),
    path('create/', include('prova.pessoas.urls'), name='create'),
]
