# 🤖 RAG를 활용한 Sparta 복습용 챗봇 만들기

## 📖 목차
1. [How To Use](#-how-to-use)
2. [Directory Structure](#-directory-structure)
3. [팀 소개 및 협업 도구](#-팀-소개-및-협업-도구)
4. [프로젝트 소개](#-프로젝트-소개)
5. [프로젝트 계기](#-프로젝트-계기)
6. [프로젝트 핵심 목표](#-프로젝트-핵심-목표)
7. [Key Summary](#️-key-summary)
8. [인프라 아키텍처 & 적용 기술](#-인프라-아키텍처-적용-기술)
9. [주요기능](#-주요기능)
10. [서비스 구조](#-서비스-구조)
11. [기술적 고도화](#-기술적-고도화)
12. [Timeline](#-timeline)

---
## 📣 How To Use
1. 원격 저장소에 올라와 있는 코드 clone 받기
```python
git clone https://github.com/ysooj/CH4-DRF.git
```

2. 가상환경 생성 및 활성화
    - 가상환경 생성
    ```python
    python -m venv 가상환경이름
    ```
    - 가상환경 활성화
    ```python
    # MacOS
    source 가상환경이름/bin/activate
    # Windows
    source 가상환경이름/Scripts/activate
    ```

3. requirements.txt 설치
```python
pip freeze > requirements.txt
```

4. 서버 실행 
```python
python manage.py runserver
```

5. Postman 실행
서버가 동작하는지 확인하기 위해서 Postman과 같은 소프트웨어를 이용할 수 있다.


---
## 🔍 Directory Structure

```
clone한 폴더/
├── accounts/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── products/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── spartamarket_DRF/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── ERD.drawio
└── manage.py
```

---
## 📋 프로젝트 소개
- 프로젝트명 : spartamarket_DRF
- 개발 기간 : 2024.12.19 - 2024.12.27

---
## ❕ 프로젝트 핵심 목표
프로젝트의 핵심 목표는 Django REST Framework(DRF)를 활용하여 백엔드 기능을 구현하는 것입니다. DRF는 Django를 기반으로 RESTful API를 보다 효율적이고 직관적으로 구축할 수 있도록 돕는 강력한 도구입니다. 이를 통해 API 설계와 개발 과정에서 발생할 수 있는 복잡성을 줄이고, 더 나아가 유지보수와 확장이 용이한 시스템을 구축하는 것을 목표로 하고 있습니다. DRF의 다양한 기능을 잘 활용하여 빠르고 안정적인 API 서버를 구현하는 데 중점을 두고 있습니다.

---
## 🗝️ Key Summary
- accounts 앱에서 회원가입, 로그인, 프로필 조회 기능을 구현했습니다.
- products 앱에서 상품 등록, 상품 목록 조회, 상품 상세 조회, 상품 상세 수정, 상품 상세 삭제 기능을 구현했습니다.
      
- 주요 트러블 슈팅 사례
   <details>
  <summary>오타 문제</summary>
    변수나 함수명, html 등의 오타로 인해 다양한 오류가 발생해서, 오타를 찾아서 수정하는 작업이 많았습니다.
  </details>

  </details>

  <details>
  <summary>회원가입 시리얼라이저 모델 정의 시 500번대 에러 발생</summary>
   원인 : Meta 클래스에도 필수 필드들을 추가해야 하는데, 필수 필드들을 추가하지 않았기 때문이었습니다.
   
   문제 코드
   ```
    class Meta:
        model = User
        fields = ('email', 'password', 'password2', 'username', 'profile_image')
   ```
   
   해결 코드
   ```
    class Meta:
        model = User
        fields = ('email', 'password', 'password2', 'username', 'profile_image', 'name', 'nickname', 'birthdate')
   ```
  </details>

     
       <details>
  <summary>OperationalError 발생</summary>
   원인 : 데이터베이스에서 author_id라는 컬럼을 찾을 수 없다는 에러 메세지를 확인할 수 있었습니다. 이는 models.py를 수정한 후 마이그레이션을 하지 않았기 때문이었습니다.
   
   문제 코드
   ```
    class Product(models.Model):
        author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
        title = models.CharField(max_length=120)
        content = models.TextField()
        profile_image = models.ImageField('상품 이미지', upload_to='product_images/', blank=True, null=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.title  # title 필드를 반환
   ```
   
   해결 코드
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
  </details>

---
## 📝 API 문서
## acoounts 앱
---
### API Info
---
```
http://127.0.0.1:8000/api/accounts/
```
회원가입 API 입니다.
권한 : User
#### Request
---
- Header
    - None  
- Body
    - None 
#### Response
---
201 Created
``` json
{
    "message": "회원가입이 성공적으로 완료되었습니다."
}
 ```
400 Bad Request
``` json
{
    "email": [
        "user with this 이메일 already exists."
    ],
    "username": [
        "user with this 사용자명 already exists."
    ]
}
 ```
400 Bad Request
``` json
{
    "email": [
        "user with this 이메일 already exists."
    ],
    "name": [
        "This field is required."
    ],
    "nickname": [
        "This field is required."
    ],
    "birthdate": [
        "This field is required."
    ]
}
 ```
---
### API Info
---
```
http://127.0.0.1:8000/api/accounts/login/
```
로그인 API 입니다.
권한 : User
#### Request
---
- Header
    
    - None
        
- Body
    
    - None
        

#### Response

---

200 OK

``` json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM1MjAyODU0LCJpYXQiOjE3MzUyMDEwNTQsImp0aSI6Ijc3YWRkNjkyYmVhNTQ3ZDc4YzY2NGVjZDA3NTFlMzIzIiwidXNlcl9pZCI6MX0.06MjpHLr8sLwSCAbBIrFokdRuEEVJ-TGAe7qLfYQ79c",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczNTI4NzQ1NCwiaWF0IjoxNzM1MjAxMDU0LCJqdGkiOiJlZGZmMWRjNjZlZWE0ODE0YTEyMjVmNWNjY2QyNzJmNSIsInVzZXJfaWQiOjF9.Ful5XETPDtKD5CgJlga2npf-FwcrknelIE6N1ZN1WTQ",
    "message": "로그인 성공"
}

 ```

400 Bad Request

``` json
{
    "error": "이메일 또는 비밀번호가 올바르지 않습니다."
}

 ```
---
### API Info

---
```
http://127.0.0.1:8000/api/accounts/test/
```

프로필 조회 API 입니다.

권한 : User

#### Request

---

- Header
    
    - Authorization : access_token
        
- Body
    
    - None
        

#### Response

---

200 OK

``` json
{
    "email": "test@gmail.com",
    "username": "test",
    "profile_image": null,
    "name": "테스트",
    "nickname": "테스트닉네임",
    "birthdate": "2024-12-25"
}

 ```

404 Not Found

``` json
{
    "error": "User not found"
}

 ```
---
### API Info

---
```
http://127.0.0.1:8000/api/accounts/newtest/
```
프로필 수정 API 입니다.

권한 : User

#### Request

---

- Header
    
    - Authorization : access_token
        
- Body
    
    - None
        

#### Response

---

200 OK

``` json
{
    "message": "회원정보가 성공적으로 수정되었습니다.",
    "user": {
        "email": "newemail@naver.com",
        "username": "newtest",
        "profile_image": null,
        "name": "테스트",
        "nickname": "테스트닉네임",
        "birthdate": "2024-12-26"
    }
}

 ```

400 Bad Request

``` json
{
    "email": [
        "Enter a valid email address."
    ]
}

 ```

401 Unauthorized

``` json
{
    "detail": "Authentication credentials were not provided."
}

 ```

404 Not Found

``` json
{
    "error": "User not found"
}

 ```
---
## products 앱
---
### API Info

---
```
http://127.0.0.1:8000/api/products/
```
상품 목록 조회 API 입니다.

권한 : User

#### Request

---

- Header
    
    - None
        
- Body
    
    - None
        

#### Response

---

200 OK

``` json
[]

 ```
---
### API Info

---
```
http://127.0.0.1:8000/api/products/22/
```
상품 상세 조회 API 입니다.

권한 : User

#### Request

---

- Header
    
    - Authorization : access_token
        
- Body
    
    - None
        

#### Response

---

200 OK

``` json
{
    "id": 1,
    "author": "jgarcia",
    "title": "Writer not wish happen senior media.",
    "content": "Study wall their identify bill gun traditional oil. Movie entire three rather sit behind. Simple late have.",
    "created_at": "1981-08-01T18:09:18.966302Z",
    "updated_at": "2009-02-11T10:14:57.362068Z"
}

 ```

401 Unauthorized

``` json
{
    "detail": "Authentication credentials were not provided."
}

 ```

404 Not Found

``` json
{
    "detail": "No Product matches the given query."
}

 ```
---
## API Info

---
```
http://127.0.0.1:8000/api/products/
```
상품 등록 API 입니다.

권한 : User

### Request

---

- Header
    
    - Authorization : access_token
        
- Body
    
    - None
        

### Response

---

200 OK

``` json
{
    "id": 21,
    "author": "test",
    "title": "sofa",
    "content": "nice sofa",
    "created_at": "2024-12-26T09:18:41.874824Z",
    "updated_at": "2024-12-26T09:18:41.874861Z"
}

 ```

400 Bad Request

``` json
{
    "title": [
        "This field is required."
    ],
    "content": [
        "This field is required."
    ]
}

 ```

401 Unauthorized

``` json
{
    "detail": "Authentication credentials were not provided."
}

 ```
---
## API Info

---
```
http://127.0.0.1:8000/api/products/21/
```
상품 상세 수정 API 입니다.

권한 : User

### Request

---

- Header
    
    - Authorization : access_token
        
- Body
    
    - None
        

### Response

---

200 OK

``` json
{
    "id": 1,
    "author": "jgarcia",
    "title": "새로운 가구로 수정",
    "content": "새로운 가구에 대한 설명",
    "created_at": "1981-08-01T18:09:18.966302Z",
    "updated_at": "2024-12-26T09:39:01.743980Z"
}

 ```

401 Unauthorized

``` json
{
    "detail": "Authentication credentials were not provided."
}

 ```

404 Not Found

``` json
{
    "detail": "No Product matches the given query."
}

 ```
---
## API Info

---
```
http://127.0.0.1:8000/api/products/21/
```
상품 삭제 API 입니다.

권한 : User

### Request

---

- Header
    
    - Authorization : access_token
        
- Body
    
    - None
        

### Response

---

204 No Content

401 Unauthorized

``` json
{
    "detail": "Authentication credentials were not provided."
}

 ```

404 Not Found

``` json
{
    "detail": "No Product matches the given query."
}

 ```

---
## 🗝️ Postman으로 기능 점검
- accounts 앱
    - 회원가입
    <p align="center">
        <img width="1582" alt="회원가입" src="https://github.com/user-attachments/assets/6aa052bf-a6fe-40f0-9df2-d7bb4d733cd3" />
    </p>
    - 로그인
    <p align="center">
        <img width="1582" alt="로그인" src="https://github.com/user-attachments/assets/1c77d8d2-6771-41d0-9af0-1279b0656558" />
    </p>
    - 프로필 조회
    <p align="center">
        <img width="1582" alt="프로필 조회" src="https://github.com/user-attachments/assets/bbc9ba90-abfb-497b-be2c-4cfe8798dcdc" />
    </p>
    - 프로필 수정
    <p align="center">
        <img width="1582" alt="프로필 수정" src="https://github.com/user-attachments/assets/7a3c4c41-723f-445b-8242-f98d0b3fd320" />
    </p>
- products 앱
    - 상품 목록 조회
    <p align="center">
        <img width="1582" alt="상품 목록 조회" src="https://github.com/user-attachments/assets/6ba7fa1b-55b1-4f39-9ba3-c8cb1403197f" />
    </p>
    - 상품 상세 조회
    <p align="center">
        <img width="1582" alt="상품 상세 조회" src="https://github.com/user-attachments/assets/0102a8cb-e0f2-4e47-b50d-27de12395faa" />
    </p>
    - 상품 등록
    <p align="center">
        <img width="1582" alt="상품 등록" src="https://github.com/user-attachments/assets/80460a20-d0ef-40b6-9b0e-0ad6143323d1" />
    </p>
    - 상품 상세 수정
    <p align="center">
        <img width="1582" alt="상품 상세 수정" src="https://github.com/user-attachments/assets/33e45ba5-75a1-4320-9301-99c66e549224" />
    </p>
    - 상품 삭제
    <p align="center">
        <img width="1582" alt="상품 삭제" src="https://github.com/user-attachments/assets/a983e34e-ed12-4ca8-b9f8-26aad3c206a8" />
    </p>