from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.StorageListView.as_view()),
    path('index/', views.IndexListView.as_view()),
    path('<int:pk>/', views.ProductDetailView.as_view()),

    path('product_create/', views.StorageCreateView.as_view()),
    path('product_update/<int:pk>/', views.StorageUpdateView.as_view()),
    path('product_delete/<int:pk>/', views.StorageDeleteView.as_view())
]
