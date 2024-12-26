from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import SignupSerializer
from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse


User = get_user_model()

# 회원 가입
@api_view(['POST'])
# settings.py에서 전역으로 설정해서, 모든 작업에 대해 인증이 필요하지만, 회원가입은 누구나 해야 하기때문에 이렇게 비워놓으면 인증이 필요없다는 뜻이 된다.
@authentication_classes([])
@permission_classes([])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "회원가입이 성공적으로 완료되었습니다."
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 로그인
@api_view(['POST'])
@authentication_classes([])      # 전역 인증 설정 무시
@permission_classes([AllowAny])  # 전역 IsAuthenticated 설정 무시
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 사용자 인증
    user = authenticate(request, username=username, password=password)
    if user is not None:
        # JWT 토큰 생성
        refresh = RefreshToken.for_user(user)
        return JsonResponse({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'message': '로그인 성공'
        }, status=200)
    else:
        return JsonResponse({'error': '이메일 또는 비밀번호가 올바르지 않습니다.'}, status=400)