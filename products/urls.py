# articles/urls.py
from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductListCreate.as_view(), name='product_list_create'),
    path('<int:productId>/', views.ProductDetail.as_view(), name='product_detail'),
]

# accounts 앱은 함수 기반으로 뷰를 작성했다.
# products 앱은 클래스 기반으로 뷰를 작성할 것이라서 as_view()가 필요하다.