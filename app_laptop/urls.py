from django.urls import path
from .views import LaptopListView, LaptopDetailView, search_view

urlpatterns = [
    path('', search_view, name='search'),
    path('all_laptops/', LaptopListView.as_view(), name='all_laptops'),
    path('news/<int:pk>/', LaptopDetailView.as_view(), name='detail_laptop'),
]
