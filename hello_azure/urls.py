from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello, name='hello'),
    path('login/', views.login, name='login'),
    path('inventory/', views.inventory, name='inventory'),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),

]