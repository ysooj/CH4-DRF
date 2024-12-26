# articles/urls.py
from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    # path('<int:productId>/', views.ProductDetail.as_view(), name='product_detail'),
]