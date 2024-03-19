from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.StorageListView.as_view()),
    path('index/', views.IndexListView.as_view()),
    path('<int:pk>/', views.ProductDetailView.as_view())
]
