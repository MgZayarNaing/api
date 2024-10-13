from django.urls import path
from .views import categories_views

urlpatterns = [
    path('categories/', categories_views.categories_list, name='categories-list'),
    path('categories/create/', categories_views.categories_create, name='categories_create'),

]