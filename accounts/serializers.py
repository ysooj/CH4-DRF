from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model() # 많이 쓰일 거라서 전역 변수로 선언.

# 회원가입 시리얼라이저 모델 정의
class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2', 'username', 'profile_image', 'name', 'nickname', 'birthdate')
        # profile_image는 models.py에서 blank=True로 해서, 없어도 회원가입 된다.

    # 비밀번호 확인용 password2는 유저 모델에 없는 필드라서 validate 메서드로 따로 정의했다.
    def validate(self, data):
        if data['password'] != data['password2']:
            # 비밀번호와 확인용 비밀번호가 다를 경우 에러 발생 시킴.
            raise serializers.ValidationError({
                "password": "비밀번호가 일치하지 않습니다."
            })
        return data

    def create(self, validated_data):
        validated_data.pop('password2')  # password2 제거 ; 검증을 위한 것이기 때문에 저장할 필요가 없어서.
        return User.objects.create_user(**validated_data)