from rest_framework import serializers
from .models import Product

# 상품 목록 조회 시리얼라이저 모델 정의
class ProductListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username') # author 필드에 작성자의 username만 출력
    
    class Meta:
        model = Product
        fields = ('id', 'author', 'title', 'created_at')
        read_only_fields = ('author', )

# 상품 상세 조회 및 상품 등록 시리얼라이저 모델 정의
class ProductDetailSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username') # author 필드에 작성자의 이메일만 출력
    
    class Meta:
        model = Product
        fields = ('id', 'author', 'title', 'content', 'created_at', 'updated_at')