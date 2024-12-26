from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from .serializers import SignupSerializer
from django.contrib.auth import get_user_model


User = get_user_model()

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