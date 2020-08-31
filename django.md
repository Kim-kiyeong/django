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
        
- root app, admin.py X
- models.py, urls.py, view.py 중요 : 흐름(로직) 파악 할 것
- 사용자 url 접속(REST API 이용) > url 요청에 맞는 url을 찾고, 이에 이어진 함수(view(controller)) >  

<br>

### 2. REST API
***

1. REST API (Representational State Transfer API)
    - REST : `HTTP 기반으로 필요한 자원에 접근하는 방식을 정해놓은 아키텍쳐`
    - 자원 : `저장된 데이터, 이미지, 동영상, 문서 등과 같은 파일, 서비스`

2. 구성
    - 자원(Resource) : URI
    - 행위(Verb) : HTTP Method (GET, POST, PUT, DELETE)
    - 표현(Representations) : message

3. 특징

4. 속성
    1. 서버에 있는 모든 자원은 각 자원 당 클라이언트가 바로 접근 할 수 있는 고유 URI가 존재
    2. 모든 요청은 클라이언트가 요청할 때마다 필요한 정보를 주기 때문에 서버에서는 세션 정보를 보관할 필요가 없음 
        - 서비스 자유도 높음, 유연한 아키텍쳐 적응 가능
        
    3. HTTP 메서드를 사용함(GET, POST, PUT, DELETE)
    4. 서비스 내에서 하나의 자원 주변에 연관된 리소스들과 연결되어 표현이 되어야 함

5. 설계
    - `REST API 설계 시 가장 중요한 항목 2가지`
        1. `URI은 정보의 자원을 표현해야 한다.`
        2. `자원에 대한 행위는 HTTP Method로 표현한다.`
    
    1. '/' 쓰임새
        - 슬래시 구분자는 계층 관계를 나타냄. 따라서 URI 마지막 문자로 '/'를 포함하지 않음
        > Bad
        >
        > `http://api.test.com/users/`
   
        > Good
        >
        > `http://api.test.com/users`
    
    2. URI를 이루는 자원들은 동사보단 명사로 구성
         - 자원 간의 관계를 표현하는 방법
            >`리소스명/리소스 ID/관계가 있는 다른 리소스명
            >
            > ex ) GET : /users/{userid}/devices (일반적으로 소유 'has'의 관계를 표현할 때)`     
        
        - But 컨트롤 자원을 의미하는건 예외적으로 동사 허용
            > Bad
            > `http://api.test.com/posts/duplicating`

            > Good
            > `http://api.test.com/posts/duplicate`

    3. URI에서는 '_'(언더바)보다는 '-'(하이픈)을 권장

    4. URI 경로에는 소문자가 적합
    
    5. 파일 확장자는 URI에 포함시키지 않음 `Accept header` 이용
        > ex) Accept : image/jpg

    6. 행위(method)는 포함 X
        > Bad
        > `POST http://api.test.com/users/1/delete-post/1`

        > Good
        > `DELETE http://api.test.com/users/1/posts/1`
                                                        
6. HTTP Method

    METHOD | 역할
    ---|---
    POST | POST를 통해 해당 URI를 요청하면 리소스를 생성합니다. 때에 따라서는 PUT, DELETE의 동작도 수행 가능
    GET | GET를 통해 해당 리소스를 조회합니다. 리소스를 조회하고 해당 도큐먼트에 대한 자세한 정보를 가져온다.
    PUT | PUT를 통해 해당 리소스를 수정합니다.
    DELETE | DELETE를 통해 리소스를 삭제합니다.


7. 자원을 표현하는 Collection과 Document
    - Collection : 문서 또는 객체들의 집합 : __복수로 사용__
    - Document : 문서, 객체
        > ex) 
        >
        > `http://restapi.example.com/sports/soccer`
        >
        > `sports : Collection` `Soccer : Document`
    
8. message
    - 메세지는 HTTP header와 body, 응답상태코드로 구성.
    - header와 body에 포함된 메세지는 메세지를 처리하기 위한 충분한 정보를 포함

9. Body
    - 자원에 대한 정보를 전달

10. Header
    - HTTP body에 어떤 포맷으로 데이터가 담겼는지 정의
    
- 8, 9, 10 항목은 HTTP에서 구체적으로 다룸

<br>

### 3. HTTP
***
1. HTTP(Hyper Text Transfer Protocol)
    - 서버와 클라이언트가 인터넷 상에서 HTML문서를 주고받을 수 있도록 하기 위해 만든 통신 규약
    - HTTP 통신은 클라이언트가 데이터를 request하면 그 요청을 처리하여 서버가 다시 클라이언트에게 response하는 큰 흐름을 따름

2. Https (HTTP + Source)
    - ssl/tls에 의해 암호화된 데이터를 주고받는다
    - 민감한 정보를 통신할 때 사용 권장

3. 특징
    - 무상태(Stateless) & 비연결성(Connectionless) : 모든 요청과 응답은 이전의 것들과는 상관없이 독립적으로 이루어진다.
    - 불특정 다수를 대상으로 하는 서비스에 적합하다.
    
4. HTTP Request Message 의 구조

    > ![image](https://media.vlpt.us/post-images/rosewwross/6cafb380-4b37-11ea-b8a3-d182d6d1a356/image.png)
    > 1. Start line(Request line) : HTTP request의 첫 라인. 세 부분으로 구성
    >   - HTTP Method : action을 정의
    >   - Request target : request가 전송되는 URI(endpoint)
    >   - HTTP Version
    >   - `ex) GET /doc/test.html HTTP/1.1`
    >
    > 2. Headers : request에 대한 meta정보를 담고 있으며, key:value 값으로 되어있음
    >   - Host : 요청이 전송되는 target의 host
    >   - User-Agent : 요청을 보내는 클라이언트의 대한 정보
    >   - Accept : 해당 요청이 받을 수 있는 response 타입
    >   - Connection : 해당 요청이 끝난 후 클라이언트와 서버가 계속해서 네트워크 커넥션을 유지 할것인지 지시하는 부분
    >   - Content-Type : 해당 요청이 보내는 메세지 body의 타입
    >   - Content-Length : 메세지 body 길이
    >
    > 3. Empty line : 요청에 대한 meta 정보가 전송되었음을 알리는 빈 line
    >
    > 4. Body
    >   - 해당 request의 실제 메세지/내용이 들어있음
    >   - XML이나 JSON 데이터가 들어갈 수 있음
    >   - GET은 body가 대부분 없음

5. HTTP Response Message

    > ![image](https://documentation.help/DogeTool-HTTP-Requests-vt/http_responsemessageexample.png)
    > 1. Status line : response의 상태를 간략히 나타냄. 세부분으로 구성
    >   - status code : 응답 상태를 나타내는 코드
    >   - status text : 응답 상태의 설명 (ex : Not Found)
    >
    > 2. Headers : request의 header와 동일
    >   - response에서만 사용되는 header 값이 있음 (ex : User-Agent가 없고, Server가 있음)
    >
    > 3. Empty line
    >
    > 4. Body : 실제 응답하는 데이터를 나타냄
