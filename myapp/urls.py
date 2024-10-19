from django.urls import path
from .views import categories_views,products_views

urlpatterns = [

    # Categories
    path('categories/', categories_views.categories_list, name='categories-list'),
    path('categories/create/', categories_views.categories_create, name='categories_create'),
    path('categories/<int:pk>/', categories_views.categories_detail, name='categories-detail'),
    path('categories/<int:pk>/update/', categories_views.categories_update, name='categories-update'),
    path('categories/<int:pk>/delete/', categories_views.categories_delete, name='categories_delete'),

    # Products
    path('products/', products_views.Products_list, name='Products_list'),
    path('products/create/', products_views.Products_create, name='Products_create'),



]