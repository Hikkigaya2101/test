from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index,post_position,edit,delete,post_worker

urlpatterns = [
path('post_position/', post_position,name = 'post_position'),
path('post_worker/', post_worker,name = 'post_worker'),
path("edit/<int:id>/", edit,name = 'edit'),
path('delete/<int:id>/', delete,name = 'delete'),
  path('', index),
]+ static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)

