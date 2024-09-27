from django.urls import path
from . import views

urlpatterns = [
    # Item URLs
    path('', views.home, name='home'),  # Root URL
    path('items/', views.item_list, name='item_list'),
    path('items/create/', views.create_item, name='create_item'),
    path('items/<int:item_id>/', views.item_detail, name='item_detail'),
    path('items/<int:item_id>/edit/', views.update_item, name='update_item'),
    path('items/<int:item_id>/delete/', views.delete_item, name='delete_item'),

    # Category URLs
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('categories/<int:category_id>/edit/', views.update_category, name='update_category'),
    path('categories/<int:category_id>/delete/', views.delete_category, name='delete_category'),
]
