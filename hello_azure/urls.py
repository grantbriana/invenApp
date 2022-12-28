from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello, name='hello'),
    path('login/', views.login, name='login'),
    path('inventory/', views.inventory, name='inventory'),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),
    re_path('items/(?P<pk>\d+)$', views.ItemListView.as_view(), name='items'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),
    path('item/create/', views.ItemCreate.as_view(), name='item-create'),
    path('item/<int:pk>/update/', views.ItemUpdate.as_view(), name='item-update'),
    path('item/<int:pk>/delete/', views.ItemDelete.as_view(), name='item-delete'),    
    path('inventory/item/create/', views.ItemCreate.as_view(), name='item-create'),
    path('inventory/item/<int:pk>/update/', views.ItemUpdate.as_view(), name='item-update'),
    path('inventory/item/<int:pk>/delete/', views.ItemDelete.as_view(), name='item-delete'),    
]