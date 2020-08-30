### 1. Django
***
* django : `파이썬으로 만들어진 무료 오픈소스 웹 애플리케이션 프레임워크`

1. django의 파일 구조
    - __최상위 디렉토리__ : `타 프로젝트와 구별하기 위해 보통 프로젝트 이름으로 설정`
    - __root app__ : `django-admin.py startproject [패키지명]` 명령어로 생성된 루트 앱. inbound http request를 가장 처음 받아 처리하는 앱으로서 엔드포인트를 통해서 urls.urlpatterns에 기술된 적절한 앱으로 request를 라우팅한다.
        일반적으로 프로젝트 이름을 사용하지만 실제로는 프로젝트의 설정 파일이 들어가므로 `conf` 이름으로 사용한다.
        
        1. setting.py : `django core에서 사용할 수 있는 전역 설정 목록과 기본값이 정의된 파일`
        2. urls.py : `urlpatterns 리스트의 항목(엔드포인트, 대상)에 따라 request를 라우팅 한다`
     
    - __user defined app__ : `python manage.py startapp [패키지명]` 명령어로 생성된 앱이다. root app에서 라우팅된 request를 views의 객체로 라우팅하여 로직을 수행한다
        
        1. admin.py : `adminpage에서 GUI를 통해 관리할 모델을 선언하는 페이지. python manage.py createsuperuser 명령어를 통해 만든 관리자 ID, 비밀번호로 접근한다`
        2. models.py : `앱에서 사용하기 위한 데이터 베이스 테이블을 ORM문법에 의거하여 작성하는 파일. 클래스는 DB에서 테이블과, 각 멤버 객체들은 column에 대응한다`
        3. urls.py : `root app에서 라우팅된 request의 엔드포인트에 따라 라우팅될 view가 정의된 파일`
        4. view.py : `request가 최종적으로 라우팅되어 동작시킬 로직이 정의된 파일`
        
