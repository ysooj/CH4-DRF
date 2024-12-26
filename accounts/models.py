from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError

# 사용자명으로 로그인하기 위해 정의
class CustomUserManager(BaseUserManager):
    # 일반 회원 생성 메서드
    def create_user(self, username, password=None, email=None, name=None, nickname=None, birthdate=None, **extra_fields):
        # 필수 필드 검증
        if not username:
            raise ValueError('사용자 이름은 필수입니다')
        if not email:
            raise ValueError('이메일은 필수입니다')
        if not name:
            raise ValueError('이름은 필수입니다')
        if not nickname:
            raise ValueError('닉네임은 필수입니다')
        if not birthdate:
            raise ValueError('생일은 필수입니다')
        
        # 사용자명 및 이메일 중복 검사
        if self.model.objects.filter(username=username).exists():
            raise ValidationError('이미 존재하는 사용자 이름입니다.')
        if self.model.objects.filter(email=email).exists():
            raise ValidationError('이미 존재하는 이메일입니다.')

        user = self.model(username=username, email=self.normalize_email(email), name=name, nickname=nickname, birthdate=birthdate, **extra_fields)

        # 비밀번호가 있을 때만 설정
        if password:
            user.set_password(password)
        
        user.save()
        return user
        

class User(AbstractUser):
    email = models.EmailField('이메일', unique=True)
    username = models.CharField('사용자명', max_length=150, unique=True)
    name = models.CharField(max_length=15)
    nickname = models.CharField(max_length=20)
    birthdate = models.DateField()

    profile_image = models.ImageField('프로필 이미지', upload_to='profile_images/', blank=True, null=True)

    USERNAME_FIELD = 'username'  # 로그인 시 사용자명을 사용
    REQUIRED_FIELDS = ['email', 'name', 'nickname', 'birthdate']  # 이메일 및 추가 필드 필수

    objects = CustomUserManager()

    def __str__(self):
        return self.username