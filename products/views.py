# articles/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer
from django.core.cache import cache

# 상품 목록 조회 및 등록
class ProductListCreate(APIView):
    # 로그인하지 않아도 읽기는 가능하지만, 상품을 등록하려면 로그인해야 한다.
    permission_classes = [IsAuthenticatedOrReadOnly]

    # 상품 목록 조회
    def get(self, request):
        articles = Product.objects.all()
        serializer = ProductListSerializer(articles, many=True)  # 목록용 Serializer 사용
        return Response(serializer.data)

    # 상품 등록
    def post(self, request):
        serializer = ProductDetailSerializer(data=request.data)  # 상세 Serializer 사용
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 상품 상세 조회, 수정, 삭제
class ProductDetail(APIView):
    def get_object(self, productId):
        return get_object_or_404(Product, pk=productId)

    # 상품 상세 조회
    def get(self, request, productId):
        product = self.get_object(productId)
        serializer = ProductDetailSerializer(product)  # 상세 Serializer 사용
        return Response(serializer.data)
    
    # 상품 상세 수정
    def put(self, request, productId):
        product = self.get_object(productId)
        serializer = ProductDetailSerializer(product, data=request.data, partial=True)  # 상세 Serializer 사용
        # title만 수정하거나, content만 수정하고 싶을 때를 위해서 partial=True 옵션 설정.
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)
    
    # 상품 삭제
    def delete(self, request, productId):
        product = self.get_object(productId)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)