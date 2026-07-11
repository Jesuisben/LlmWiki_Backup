FrontEnd_BackEnd 총정리 (2026.03.30(월) ~ 2026.04.03(금))
#### \# 웹페이지를 만들기 위해 필요한 과정
1\. 프로그램 기본 세팅들 (node.js / springboot등 설치 포함)

(스프링)
2\. 스프링에 application.properties에 설정하기
포트이름, 파일 경로, url경로, mysql 경로 등
3\. 사용할 엔티티 생성
(3.5 DB에 저장된 내용을 사용한다면 Repository필요)
4\. 엔티티를 사용할 컨트롤러 생성 (RestController)

(리액트)
5\. config.tsx로 설정파일 만들어서 스프링의 port번호 저장하는 변수 생성
6\. 스프링과 동일한 속성을 가진 ts생성(types폴더에) (대소문자구별)
7\. 보여줄 페이지를 생성 (스프링의 컨트롤러의 매핑방식과 주소가 대응되게)
useState와 useEffect 사용
axios를 사용
```typescript
const fetchResult = async () => { // async와
const response = await axios.get<Fruit>(url, config); // await는 짝꿍
```
8\. AppRoutes.tsx를 생성해서 라우터로 해당 주소와 해당 페이지를 연결해줌
8.5 페이지를 최소 2곳을 이용 (이동)한다면 main.tsx에 \<App \>을
\<BrowserRouter\>로 감싸줘야 함
(스프링)
9\. 리액트와 스프링이 연결되기 위해 CORS 설정을 해줌
스프링에 WebConfig파일을 만들고 @Configuration으로 설정용 파일로 설정 후
허용할 오리진 주소 (리액트 주소)와 매핑 방식을 허용함

10\. 연결 성공!


#### \# 사용한 프로그램
- Spring
백엔드

- Spring Boot
Spring 도우미

- Visual Studio Code
React의 IDE

- NodeJs
1) build해주는 프로그램
build한다 : React로 나온 파일인 vite 파일들을 묶음으로 만들기? 실행하기? (마치 패키지 형태로)

2) 리액트를 사용하려면 npm(Node Packaged Manager)이라는 프로그램을 사용하면 좋습니다.
npm은 node.js에 내장(built in)되어 있으므로, node.js을 설치하기만 하면 됩니다.


- MySQL
데이터 베이스

- React
프론트엔드



#### \# MySQL 설치 및 설정
링크 : https://dev.mysql.com/downloads/
1) 설치
MySQL Installer for Windows - Select Version:8.0.45 / Select Operating System:Microsoft Windows
- Windows (x86, 32-bit), MSI Installer	8.0.45	556.0M Download

2) 설치 세팅
Custom - (MySQL Servers - MySQL Server - MySQL Server 8.0 - MySQL Server 8.0.45 - X64 선택),
(Applications - MySQL Workbench - MySQL Workbench 8.0 - MySQL Workbench 8.0.46 - X64선택)
후에 Next - Execute - Next - Next - Port번호가 3306이라는 것 기억하기 - Use Legacy 체크
- MySQL Root Password (mysql) / Repeat Password (mysql) - Windows Service Name : MYSQL로 바꾸기
- 마지막에 Finish - Start MySQL Workbench after setup 체크해제

3) MySQL Workbench 실행
커넥션 - Password(mysql) + 체크박스 체크


#### \# Node.Js 설치
링크 : https://nodejs.org/ko
1) 설치
Get Node.js® - Windows 설치 프로그램 (.msi) - 설치

2) 설치 확인
cmd 관리자 권한으로 실행 - (npm -version) 입력 - (11.11.0) 확인



#### \# Visual Studio Code 설치
링크 : https://code.visualstudio.com/
Download - Windows Windows 10, 11



#### \# SpringBoot 활용해서 Spring 세팅파일 초기구성
링크 : https://spring.io/
Projects - Spring Initializr
1) 구성하기
- Project : Maven (Maven으로 패키징하기)(빌드툴)
- Language : Java (언어)
- Spring Boot : 3.5.13 (팀별 프로젝트할때 이 버전도 맞춰야함)
- Project Metadata
Group : com.coffee
Artifact : coffee
Package name(패키지 경로 - 보통 3단계) : com.coffee (이건 2단계 - 나중에 직접 만들거라서)
Packaging : Jar (패키징 종류)(꿀단지 - 안쪽에 많은 클래스, 인터페이스, 추상메소드 등이 있다는걸 의미함)
Configuration : Properties (내부의 설정파일을 어떤 형식으로 할 것이냐)
Java : 21 (이제 20 밑으로는 잘 지원 안함)

- Dependencies(의존성)
어떤걸 자동으로? 편하게? 하기 위해 필요한 툴?들 / 순서 상관 X / 나중에 추가도 가능
ex) getter setter를 편하게 쓰기 위해서 툴을 설치

(SpringBoot 교안 PDF (P.12))에서 Oracle Driver빼고 다 추가하기

추가할 항목들 :
Spring Boot DevTools
Lombok
Spring Data JPA
MySQL Driver
Thymeleaf
Spring Web
Spring Web Services
H2 Database

- Generate하면 zip 파일로 다운됨
압축해제하면 안에 들어 있는 파일들이 바로 초기화 파일들임

2) 폴더 생성 (intelliJ에 연결할 경로에 폴더생성)
D드라이브에 FrontEnd_BackEnd(폴더생성) - spring_cafe 폴더 생성
spring_cafe : 스프링 소스

3) 초기화 파일들을 spring_cafe에 넣기

4) 파일들을 intelliJ로 열기
메뉴 - open - spring_cafe있는 경로 들어가서 Select Folder

5) main프로그램 확인하기
scr - main - java 자바 관련 소스 코드들
scr - main - java - com.coffee - CoffeeApplication이 main프로그램임
scr - main - resources - templates안에 HTML 파일들 생김
scr - main - resources - static안에 CSS, JS 파일들 생김
scr - test는 간단한 테스트 작업

\* pom.xml : maven을 위한 설정용 파일
\* application.properties파일은 스프링전반의 설정용 파일

6) intelliJ에서 java의 버전을 똑같이 맞추기
메뉴 - Project Structure - SDK - Download JDK - version : 21 - Download



#### \# IT 관련 용어 PDF (P.37~42)
- Protocol (통신 규약)
컴퓨터나 네트워크 장치끼리 통신하기 위한 약속 또는 규칙을 의미
ex) HTTP / HTTPS 등
\* 통신 규약이 다르면 중간에 번역기가 필요함 \*

- IP Address (IP 주소)
IP (Internet Protocol) : 인터넷 프로토콜
4개의 숫자 덩어리
ex) 192.168.0.1

- Port
똑같은 주소면 다 IP주소가 같은데
여러가지(Spring Boot / MySQL / Web Server (HTTP)) 돌리려면 식별자(Port)가 필요함

- Port number
동일한 IP주소로 들어와서 갈라지기 위한 Port number
ex)
8080 -\> Spring Boot
3306 -\> MySQL
80 -\> Web Server (HTTP)

- localhost
내 컴퓨터 자신을 가리키는 주소
이것을 IP로 바꾸면 (127.0.0.1) 이렇게 됨

- SpringBoot
http://localhost:9000
Port 9000

- React
http://localhost:3000
Port 3000

\* Port number는 내가 임의로 지정가능 \*



#### \# 홈페이지 구성 절차
(intelliJ - spring_cafe)

1) 기본 포트 number 설정
(application.properties (스트링부트의 설정용파일))
```properties
server.port=9000 (복붙하기)
```
-\> 기본 포트값은 80이지만 이 스프링부트의 포트값을 내가 임의로 9000으로 설정함

2) 시작 페이지 HTML 생성
src/main/resources/static/index.html (경로에 파일생성)

(아래 소스코드 복붙)
```html
<!DOCTYPE html>
<html lang="ko">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>홈 페이지</title>
   <style>
      body {
         font-family: Arial, sans-serif;
      }
      .username {
         color: blue;
         font-weight: bold;
      }
   </style>
</head>
<body>
<h3>홈 페이지</h3>
<p><span class="username">홍길동</span>님~~ 안녕하세요.</p>
</body>
</html>
```

3) 스프링 부트 main 실행
src/main/java/com.coffee/CoffeeApplication.java 파일 실행

4) 브라우저에 웹페이지 주소 입력
http://localhost:9000/
-\> 내 컴퓨터 IP주소 타고 와서 9000인 Port로 들어가라
9000이라는 Port number는 내가 아까 (1) 기본 포트 number 설정)에서 설정한 값

\* 만약 내가 application.properties에서 server.port=80으로 변경하면
http://localhost:80/으로 가야 내가 설정한 HTML이 나옴



#### \# Node.js 환경에서 빌드 도구인 Vite를 사용하여 React 프로젝트를 생성하기
\* npm(Node Packaged Manager) \*

1) cmd 실행

2) react파일을 만들 경로로 이동
d: (d드라이브로 전환)
D:\>cd "d:\FrontEnd_BackEnd" (cd : change directory)

3) 디렉토리 안의 파일 목록 확인
d:\FrontEnd_BackEnd>dir

4) vite 생성하기
```bash
npm create vite@latest
```
-\> 현재 디렉토리에서 하위 디렉토리를 생성

5) 재확인
Ok to proceed? (y) y

6) 이름 지정
 Project name:
|  react_cafe

7) 프레임워크 선택하기
키보드 화살표로 조절해서 React에 놓고 엔터키
  Select a framework:
|  React

8) 세부 선택지, 옵션 모델 설정
o  Select a variant:
|  TypeScript + React Compiler
-\> 우리가 앞으로 코딩할 때 타입스크립트라는 언어를 쓰고,
리액트 컴파일러라는 최신 기술을 적용해서 프로젝트 뼈대를 만들겠다"고 선언하는 과정

9) 
Install with npm and start now?
|    Yes / > No (No 선택)

10) 
  Scaffolding project in d:\FrontEnd_BackEnd\react_cafe...
|
—  Done. Now run:

11) 프로젝트 폴더로 이동
```bash
cd react_cafe
```

12) 패키지 설치
```bash
npm install
```

13) 개발 서버 다시 실행하기
```bash
npm run dev
```

14) 리액트 홈페이지 들어가기
VITE v8.0.3  ready in 2153 ms

  ➜  Local:   http://localhost:5173/ - 이부분 복사해서 웹페이지 주소창에 입력
  ➜  Network: use --host to expose
  ➜  press h + enter to show help

15) 리액트 관련 라이브러리 설치
cmd 일괄 작업 취소한 후 (Ctrl + C)
아래 코드 입력

```bash
npm install axios
npm install react-router-dom
npm install bootstrap
npm install react-bootstrap
```

16) cmd 화면 내용 다 지우기
cls 입력

17) 설치된 모듈 목록 확인
```bash
npm list
```


#### \# MySQL Workbench에 샘플로 coffee 테이블 만들어보기
1) 02. 개발 환경 구축.txt에 적힌 SQL 구문들 복붙하기
```sql
-- coffee 데이터 베이스 삭제
drop database coffee ;

-- coffee 데이터 베이스 생성
create database coffee ;

-- 데이터 베이스 목록 확인
show databases;

-- coffee 데이터 베이스를 사용하겠습니다.
use coffee ;

-- 테이블 목록을 보여 주세요.
show tables ;

-- auto_increment : 숫자가 1씩 자동으로 커짐, 오라클의 시퀀스와 유사
create table coffee(
	id int auto_increment primary key,
	name varchar(50) not null,
	type varchar(30),
	price decimal(5, 2) not null
);

insert into coffee (name, type, price) values
('Espresso', 'Espresso', 3.50),
('Latte', 'Milk Coffee', 4.50),
('Cappuccino', 'Milk Coffee', 4.00),
('Americano', 'Black Coffee', 3.00);

commit;

select * from coffee;
```

2) Ctrl + Enter로 실행하기 (or Ctrl + Shift + Enter로 전체 실행)



#### \# Spring 기본 설정하기
(intelliJ - application.properties)
1) 아래 코드 복붙 (추가)
```properties
spring.devtools.restart.enabled=true
spring.devtools.livereload.enabled=true
productImageLocation=C:\\shop\\images\\
uploadPath=file:///C:/shop/images/
spring.datasource.url=jdbc:mysql://localhost:3306/coffee?useSSL=false&serverTimezone=Asia/Seoul&characterEncoding=UTF-8
spring.datasource.username=root
spring.datasource.password=mysql
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.jpa.properties.hibernate.show_sql=true
spring.jpa.properties.hibernate.format_sql=true
logging.level.org.hibernate.type.descriptor.sql=trace
spring.jpa.hibernate.ddl-auto=update
spring.jpa.database-platform=org.hibernate.dialect.MySQL8Dialect
server.servlet.session.timeout=120m
```

2) 코드 설명
- 로컬호스트 port number
```properties
spring.datasource.url=jdbc:mysql://localhost:3306/coffee?
```
- 사용자 이름
```properties
spring.datasource.username=root
```
- 비밀번호
```properties
spring.datasource.password=mysql
```
- 데이터베이스 종류
```properties
spring.jpa.database-platform=org.hibernate.dialect.MySQL8Dialect
```

3) Automatic Restart 기능 활성화
3-1) 의존성 코드 추가
(pom.xml 파일에 아래 코드 추가)
(spring-boot-devtools 항목이 이미 설정되어 있으므로 생략)
```xml
<dependency>
	<groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-devtools</artifactId>
	<scope>runtime</scope>
	<optional>true</optional>
</dependency>
```

3-2) 설정 코드 추가
(application.properties 파일에 아래 코드 추가)
(이미 설정되어 있으므로 생략)
```properties
spring.devtools.restart.enabled=true
spring.devtools.livereload.enabled=true
```

3-3) intelliJ 설정
설정 - Advanced Settings - Compiler 항목 - Allow auto-make to start ... 체크
설정 - Build, Execution, Deployment - Compiler 항목 - Build project automatically 체크

4) 롬복(Lombok) 설정
4-1) 의존성 코드 추가
(pom.xml 파일에 아래 코드 추가)
(spring-boot-devtools 항목이 이미 설정되어 있으므로 생략)
```xml
<dependency>
	<groupId>org.projectlombok</groupId>
	<artifactId>lombok</artifactId>
	<optional>true</optional>
</dependency>
```

4-2) intelliJ 설정
- Lombok 플러그인 설치 (이미 기본으로 설치 되어 있음)
Lombok 플러그인은 IDE가 Lombok이 생성한 메소드/생성자를 인식할 수 있게 해주는 역할
설정 - Plugins - Marketplace - lombok 검색 - install

- annotation processing 설정
자바에서는 @Override, @Deprecated 같은 기본 어노테이션뿐 아니라
개발자가 정의한 어노테이션을 사용가능
특정 어노테이션은 단순 표시뿐만 아니라, 컴파일 시점에 코드를 생성 / 수정하는 기능하는 수행
이를 담당하는 것이 어노테이션 프로세서(annotation processor)
설정 - Build, Execution, Deployment - Compiler - Annotation Processors
- Enable annotation processing
-\> IDE가 컴파일 시 Lombok 같은 어노테이션 프로세서를 실행하도록 허용하는 것



#### \# Lombok 사용해보기
(intelliJ - com.coffee에 entity폴더 생성 후 Fruit클래스 생성)
```java
package com.coffee.entity;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter @Setter @ToString
public class Fruit {
    private String id;
    private String name;
    private int price;

    public Fruit(){}

    public Fruit(String id, String name, int price) {
        this.id = id;
        this.name = name;
        this.price = price;
    }
}
```

-\> 어노테이션(Getter / Setter / ToString)만 적어도 자동으로 import가 됨


#### \# Metadata란? (IT 관련 용어 PDF (P.8))
원본 데이터를 설명하기 위하여 추가적으로 보유하고 있는 다른 데이터를 의미

#### \# 어노테이션(Annotation) (IT 관련 용어 PDF (P.9))
Spring에서 어노테이션(Annotation)은 메타 데이터를 제공하는 데 사용이 됨
즉, 코드에 대한 추가 정보를 제공하고, Spring이 해당 코드를 어떻게 처리해야 하는지 알려줌



#### \# FruitHtmlController.java 생성 후 작성
(com.coffee - controller 폴더 생성 후 - FruitHtmlController 클래스 생성)
과일과 관련된 웹 요청에 대하여 데이터를 표현해 주는 컨트롤러 클래스 (단순 html 형식)
(코드 복붙)
```java
package com.coffee.controller;

import com.coffee.entity.Fruit;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class FruitHtmlController {
    @GetMapping("/fruit01") // http://localhost:9000/fruit01
    public String test(Model model){
        // Model은 데이터 저장소 역할
        Fruit bean = new Fruit(); // bean이 저장될 데이터
        bean.setId("banana");
        bean.setName("바나나");
        bean.setPrice(1000);

        // 저장시 식별할 수 있도록 "fruit"라는 이름으로 저장
        model.addAttribute("fruit", bean);

        // html 문서에서 이를 접근할 수 있음
        return "fruit"; // fruit.html 문서로 이동 (보낼 html파일 이름 적기 - 대소문자 구별함)
    }
}
```

(코드 풀이)
- @Controller (클래스 설정)
이 클래스가 "웹 요청을 처리하는 컨트롤러"임을 Spring에게 알림
이 어노테이션이 붙어야 Spring이 실행될 때 이 클래스를 자동으로 메모리에 올려서 관리함

- @GetMapping("/fruit") (매핑 - Mapping)
브라우저 주소창에 http://localhost:9000/fruit01를 입력했을 때 이 메서드가 실행되도록 연결(매핑)함

- 메서드 파라미터: Model model
```java
public String test(Model model)
```
스프링이 이 메서드를 호출할 때, 데이터를 담을 수 있는 빈 바구니(Model)를 자동으로 넣어줌
개발자는 이 바구니에 담기만 하면 됨
컨트롤러(백엔드)와 HTML(프론트엔드) 사이를 이어주는 데이터 전달용 트럭

- 객체 생성
Fruit bean = new Fruit();

- 객체에 데이터 넣기
bean.setId("banana");
bean.setName("바나나");
bean.setPrice(1000);

- model.addAttribute(Key, Value)
빈 바구니에 데이터 채우기
"fruit": HTML 파일에서 이 데이터를 부를 별명(Key)
bean: 방금 만든 실제 데이터(Value)
이렇게 담아두면, 이제 fruit.html 안에서 ${fruit.name} 같은 방식으로 바나나 정보를 꺼내 쓸 수 있음
-\> 식별자("fruit"): HTML 문서 안에서 ${fruit.name}과 같이 데이터를 꺼낼 때 사용하는 열쇠임

- return "fruit";
Spring MVC의 규칙에 따라 src/main/resources/templates/ 폴더 안에 있는 fruit.html 파일을 찾아 사용자 브라우저에 보여주라는 명령
문자열 "fruit"는 이동할 HTML 파일의 이름을 의미

(전체 흐름)
1\. 사용자: 브라우저 주소창에 http://localhost:9000/fruit01을 입력하여 접속 요청
2\. 컨트롤러: @GetMapping("/fruit01") 어노테이션이 해당 URL 요청을 감지하고 test(Model model) 메서드를 실행
3\. 데이터 생성 (로직 수행): new Fruit()를 통해 객체를 생성 후, banana, 바나나, 1000이라는 구체적인 데이터를 세팅
4\. 데이터 저장 (Model 담기): 생성된 Fruit 객체를 HTML에서 사용할 수 있도록 model.addAttribute("fruit", bean)를 통해 "fruit"라는 별명을 붙여 바구니에 담음.
5\. 뷰 이름 반환: 메서드가 "fruit"라는 문자열을 반환. 이는 이동할 HTML 파일의 이름을 지정하는 것
6\. 응답 (View Rendering): 스프링이 fruit.html 파일을 찾아 Model 바구니에 담긴 데이터와 결합한 뒤, 최종적으로 완성된 화면을 사용자의 브라우저에 띄워줌



#### \# fruit.html 생성 후 작성
(resources - templates 폴더 생성 후 - fruit.html 생성)
(코드 복붙)
```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>과일 1개</title>
</head>
<body>

<h1>과일 정보</h1>

<p>아이디: <span th:text="${fruit.id}"></span></p>
<p>이름: <span th:text="${fruit.name}"></span></p>
<p>가격: <span th:text="${fruit.price}"></span> 원</p>

</body>
</html>
```

(코드풀이)
FruitHtmlController클래스로부터 Model model을 이용해서 만든
model.addAttribute("fruit", bean); 라는 데이터를
return "fruit"으로 넘겨 받은 데이터를 이용하기위한 문법인
${모델명.속성명}을 이용해서
fruit모델이 가진 속성들을 표현하고 있음.

\* ${모델명.속성명}은 Thymeleaf(타임리프)라는 템플릿 엔진이
서버(Java)에서 전달받은 Model 속 데이터를 꺼내 쓰기 위해 정해둔 문법 \*



#### \# 컬렉션에 대해서 공부하기 (Java 교안(이론_20260226) (P.153))
- 표를 머리 속에 각인하기
- 컬렉션은 Java의 인터페이스(데이터 그룹을 다루기 위한 표준화된 설계 구조)여서
객체를 생성하지 못해서 하위 개념인 구현체 클래스를 만들어서 사용함
\* 컬렉션은 추상적인 설계도일뿐 메모리에 실제 공간을 저장할 수 없음

- 유형
1) Set
중복X / 순서따짐X (마치 DB에서 distinct를 쓴 느낌)
ex) 로또, (수학의) 집합

원소넣기 : add()
원소제거 : remove()
원소찾기 : contains()
원소크기 : size()
구현체 클래스 : HashSet/TreeSet/LinkedHashSet

2) List 유형
중복O / 순서따짐O
ex) 기차(량) - 몇번째 객차인가?
게시물 목록들을 나열할때
상품 목록들 나열할때 (신상품을 최신에 나열함)

원소넣기 : add()
원소제거 : remove()
원소찾기 : get(숫자)
원소크기 : size()
구현체 클래스 : ArrayList/Vector/Stack
\* Stack은 LIFO / 나머지는 FIFO

3) Map 유형
중복 - Key : X
		   Value : O
순서따짐X
ex) 키랑 값이 짝지어있을때
회원의 정보를 넣을때
id=hong
name=홍길동
password=1234

원소넣기 : put()
원소제거 : remove()
원소찾기 : containsKey/containsValue/get(key)
원소크기 : size()
구현체 클래스 : HashMap/Hashtable/Properties

- Generic (제너릭)
클래스 내의 데이터 타입을 클래스 밖에서 지정하여 타입을 일반화하는 것
ex) 구현체클래스<참조타입>
ArrayList\<Car\>


#### \# 여러개 HTML로 보내기
(FruitHtmlController)
(실습)
(List) (빈 소쿠리에 3개의 과일을 담음)
```java
@GetMapping("/fruit01/list") // http://localhost:9000/fruit01/list
public String test02(Model model){
        // 상품 여러개를 저장하기 위한 List 컬렉션
        List<Fruit> fruitList = new ArrayList<>();

        fruitList.add(new Fruit("apple", "사과", 1000));
        fruitList.add(new Fruit("pear", "배", 2000));
        fruitList.add(new Fruit("grape", "포도", 3000));

        model.addAttribute("fruitList", fruitList);

        return "fruitList";
    }
```

(풀이)
- @GetMapping("/fruit01/list") // http://localhost:9000/fruit01/list
()안에 있는 주소는 중복되면 안됨 (중요!!)

- List\<Fruit\> fruitList = new ArrayList<>();
fruitList가 빈 소쿠리
List 컬렉션의 ArrayList 구현체 클래스를 이용해서 fruitList라는 객체 생성
제러닉에는 entity폴더에 있는 Fruit를 참조타입으로 사용함

- fruitList.add(new Fruit("apple", "사과", 1000));
(List컬렉션이여서) add로 Fruit클래스에 있는 메소드를 이용해서 데이터 추가하기

- model.addAttribute("fruitList", fruitList);
식별자 이름 : "fruitList"
데이터의 값 : fruitList (add로 3개의 데이터들이 들어간 List컬렉션)

- return "fruitList";
fruitList라는 이름의 HTML에 보내기


#### \# 데이터를 보낼 fruitList라는 HTML만들기
(templates 폴더에 fruitList.html 파일생성)
(실습)
```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">    // 확장for느낌을 할 수 있게 해주기
<head>
    <meta charset="UTF-8">
    <title>Fruit List</title>
</head>
<body>
<h1>과일 목록</h1>

<table border="1">
    <tr>
        <th>ID</th>
        <th>이름</th>
        <th>가격</th>
    </tr>

    <tr th:each="fruit : ${fruitList}">     // 확장for느낌
        <td th:text="${fruit.id}"></td>
        <td th:text="${fruit.name}"></td>
        <td th:text="${fruit.price}"></td>
    </tr>
</table>

</body>
</html>
```

- http://localhost:9000/fruit01/list 주소 검색해서 확인하기



#### \# 현재까지 한 작업들
클라이언트 -\> templates -\> controller -\> templates -\> 클라이언트
순수하게 프로트엔트를 고려하지 않고 백엔드쪽만 코딩한거임



#### \# FruitController.java 생성
(controller 폴더에 - FruitController.java 파일생성)
(실습)
```java
package com.coffee.controller;

import com.coffee.entity.Fruit;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController // Rest API 요청에 대하여 처리를 해주는 컨트롤러입니다.
public class FruitController {
    @GetMapping("/fruit")
    public Fruit test(){
        Fruit bean = new Fruit(); // bean이 저장될 데이터
        bean.setId("banana");
        bean.setName("바나나");
        bean.setPrice(1000);
        return bean;
    }

    @GetMapping("/fruit/list")
    public List<Fruit> test02(){
        List<Fruit> fruitList = new ArrayList<>();

        fruitList.add(new Fruit("apple", "사과", 1000));
        fruitList.add(new Fruit("pear", "배", 2000));
        fruitList.add(new Fruit("grape", "포도", 3000));
        return fruitList;
    }
}
```


(풀이)
- @RestController 입력
```java
@RestController // Rest API 요청에 대하여 처리를 해주는 컨트롤러입니다.
```
웹페이지에 바로 보여주는 것이 아니라 JSON 형식으로 변환해서
웹페이지에 던져줌

(중요!!)
\* "Model 안 쓰고 List로 바로 못 보내나?"라는 질문에 대한 해답
1) @Controller + Model 사용
HTML 화면을 그릴 때 데이터를 전달하는 방식 (Thymeleaf 등을 쓸 때)
+ return할때 어느 html로 보낼지 결정함

2) @RestController 사용
화면 없이 데이터(JSON)만 깔끔하게 보낼 때.
지금 코드처럼 리스트를 return하면 별도의 Model 없이도 데이터가 바로 전달됨
+ return할때 어디로 보낼지가 아니라 나를 요청한 그곳으로 바로 JSON 데이터만 반환함
이렇게 받은 JSON 형식의 데이터를 react가 받아서 사용함


#### \# JSON(제이슨)이란? (IT 관련 용어 PDF (P.24))
Java Script Object Notation - JS를 표현하는 기법
데이터 표현법 중에 하나
XML의 약식 느낌
가장 많이 사용되고 가볍고 JS/React에서 사용하기 편리함
ex)
```json
{
	"id": 1,
	"name": "노트북",
	"price": 1000000
}
```


#### \# REST API 설명 (IT 관련 용어 PDF (P.26~))
- API (Application Programming Interface)
1) Client와 Server가 서로 요청과 응답을 주고 받기 위한 약속된 통로 역할 (중개자)
2) 어떤 요청자 또는 프로그램이 다른 프로그램의 기능(서비스)을
사용할 수 있도록 제공해주는 중간 인터페이스(접점)
3) 소프트웨어 시스템과 통신하기 위해 따라야 하는 규칙을 정의해 놓은 명세표

ex01)
Client  -요청>  API  -전달>  Server
Server  -응답>  API  -전달>  Client

ex02)
- 요청
Get방식 /products

- 응답
JSON 형태로
```json
[
	{ "name": "노트북", "price": 1000000 },
	{ "name": "마우스", "price": 20000 },
	{ "name": "키보드", "price": 50000 },
	{ "name": "모니터", "price": 300000 }
]
```

- Resource
웹 서버에 존재하는 HTML 페이지, 소리 파일, 이미지 파일, pdf 파일 등등을 의미

- State
자원의 실제 데이터 상태 정보(JSON, XML, HTML, CSS, TEXT 등)를 의미

- REpresentation
서버가 클라이언트에게 응답해주는 Resource의 State 표현 방식
(JSON, XML 등)

- REST (Representational State Transfer)
자원에 대한 접근을 시도할 때 이름을 구분자로 구분 지어서
자원의 정보를 주고 받는 동작을 의미

- REST API
REST 기반으로 서비스 API를 구현한 것을 의미
ex)
```java
@GetMapping("/fruit") // http://localhost:9000/fruit
@GetMapping("/fruit/list") // http://localhost:9000/fruit/list
```

/fruit	과일 하나(Fruit)의 정보 반환 (JSON Object)
/fruit/list	과일 여러 개(List\<Fruit\>)의 정보 반환 (JSON Array)

- jsx
Javascript extension
자바스크립트 확장자
텍스트 파일임

- tsx
Typescript extension
타입스크립트 확장자
텍스트 파일임


#### \# 포론트엔드 시작
#### \# Visual Studio Code 실행 (react 사용하는 툴) (03.기본기 다지기 txt - 199번째 줄)
- 초기 세팅
open folder - (D드라이브 - FrontEnd_BackEnd - react_cafe) 폴더 선택

- VSC 추가 설정
1\. 좌측 파일 탐색기 영역 조금 더 편하게 보기
설정창 여는 단축키 : Ctrl + ,
1) 설정 검색창에 workbench.tree.indent 입력
2) Workbench › Tree: Indent
Controls tree indentation in pixels.
이곳에 24 입력

2\. 저장하면 자동 줄맞춤
세팅에 fommat on save 검색
체크박스 체크하기

- 초기 설명
1) node_modules
어제 cmd창에서  npm install로 설치한 것들이 들어 있음
관련된 패키지들이 들어있음
(깃허브에 올릴때 포함 X / 예외사항으로 둠)

2) public
공용 폴더

3) src
이곳에 하위 폴더 만들고 여기에 파일들을 만들 예정

- src/config/config.tsx	 생성
config폴더 생성 후 config.tsx파일 생성

- config.tsx 파일에 작성
\* // : 주석 \*

(작성)
```typescript
// 이 파일은 백앤드의 url과 포트 번호를 저장해 놓은 설정용 파일입니다.
const API_HOST = "localhost" ; // 호스트 컴퓨터의 이름(127.0.0.1)

const API_PORT = "9000" ; // 스프링 부트의 Port 번호

// export 키워드를 적어 주어야 외부에서 이 파일을 접근할 수 있습니다.
export const API_BASE_URL = `http://${API_HOST}:${API_PORT}` ;

// 앞으로 http://localhost:9000를 적지 말고, API_BASE_URL를 사용하면 됩니다.
```

- Auto save 설정 (VisualStudioCode PDF (P.10))
File에 Auto save 체크하기


- main.tsx 초기 세팅
main 유저 인터페이스
main.tsx는 기본 골격형태
그 안에 들어 있는 App.tsx이 실제 UI를 담당하고 있음

이곳에 부트스트랩 파일을 넣으면 해당 파일과 관련된? 파일에
하나하나 다 import하지 않아도 부트스트랩 사용가능

아래의 코드 복붙 (03.기본기 다지기.txt 221번째 줄 src/main.tsx)
```typescript
// 코드 작성
import ReactDOM from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import App from './App';

import 'bootstrap/dist/css/bootstrap.min.css'; // (step01) for 부트 스트랩

ReactDOM.createRoot(document.getElementById('root')!).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
)
```

- App.tsx 초기 세팅
내용 전체 삭제 후 아래 코드 복붙
```typescript
import './App.css';

function App(){
  return (
    <>
      하하하
    </>
  );
}

export default App;
```
\* 리액트에서는 파일 하나하나를 컴포넌트 (component)라고 부름 \*
컴포넌트 중에서 App을 만든 것

\* 웹페이지에 여러 파트를 파일에 각자 만들고나서 나중에 조립함 \* (중요!)
-\> 이유 : 나중에 필요한 다른 웹페이지에 바로바로 각 파트를 재활용할 수 있어서


- App.tsx에 파트 한 부분 가져오기
1) (src폴더에 ui폴더 생성 후 MenuItems.tsx 파일 생성)
MenuItems.tsx 파일 : 리액트에서 사용하는 상단 영역의 메뉴 정보를 저장해 놓은 파일

코드 작성 :
```typescript
function App(){
    return(
        <>
            <h3>메뉴아이템</h3>
        </>
    );
};

export default App;
```

2) App.tsx에 MenuItems.tsx를 가져오기
```typescript
import './App.css';

// 외부 컴포넌트 import하기
// import 컴포넌트이름 from '경로와 파일명';
import MenuItems from './ui/MenuItems';

function App(){
  return (
    <>
      <MenuItems />
    </>
  );
}

export default App;
```

2-1) 경로 문법
```typescript
import 이름설정 from '경로' ;
```
-\> 가져올 컴포넌트의 이름을 따로 설정할 수 있음
-\> 경로만 잘 맞으면 됨 (src안의 경로만 가능)

2-2) 컴포넌트 가져올때
태그를 입력하듯 입력하면 됨
<컴포넌트파일명></컴포넌트파일명>

2-3) 가져올 컴포넌트에 추가할 내용물이 없다면
ex) \<MenuItems\>\</MenuItems\>
위의 코드를 간소화해서
```typescript
<MenuItems />
```
이렇게도 작성 가능


#### \# 절대경로 상대경로 (IT전반에 사용되는 개념)
import를 할때 import MenuItems from './ui/MenuItems'; 에서 경로 표현방법
. 기호는 현위치
.. 기호는 상위 디렉토리
/ 기호는 리눅스에서의 폴더 또는 디렉토리 구분자 (코딩 프로그램)
\ 기호는 윈도우에서의 폴더 또는 디렉토리 구분자 (윈도우 운영체제)
(\ 기호는 특수기호여서 2개를 써줘야 한개로 인식함)(ex - \n처럼 \는 특수기호처리)
ex) productImageLocation=C:\\shop\\images\\

1) 상대경로
- 특정한 누군가를 가지고 경로를 정하는 것
서로 다른 디렉토리를 연결하려면
. . 기호로 상위 디렉토리로 올라가고 /로 구분해놓고
연결하려는 파일의 디렉토리 적고 다시 /로 구분해놓으면 됨
ex)
FruitOne.tsx : src/pages/FruitOne.tsx
AppRoutes : src/routes/AppRoutes

AppRoutes상에서
```typescript
import 파일명 from "../pages/FruitOne"
```
이렇게 하면 FruitOne과 연결/참조됨

2) 절대 경로
- 어떠한 기준점을 가지고 경로를 정하는 것

\* 특수 항목만 가져오려면
```typescript
import { API_BASE_URL } from "../config/config";
```
이런식으로 {}를 사용하면 됨



#### \# 스프링에서 만든 FruitController와 대응되는
FruitOne.tsx와 FruitList.tsx 리액트 내에서 연결하기

1\. (MenuItems.tsx에 아래 코드 복사)
```typescript
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import { useNavigate } from 'react-router-dom';

function BasicExample() {
    const navigate = useNavigate();

  return (
    <Navbar expand="lg" className="bg-body-tertiary">
      <Container>
        <Navbar.Brand href="#home">React-Bootstrap</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#link">Link</Nav.Link>
            <NavDropdown title="기본 연습" id="basic-nav-dropdown">
              <NavDropdown.Item onClick={() => navigate(`/fruit`)}>과일 1개</NavDropdown.Item>
              <NavDropdown.Item onClick={() => navigate(`/fruit/list`)}>과일 목록</NavDropdown.Item>
            </NavDropdown>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default BasicExample;
```


2\. FruitOne.tsx와 FruitList.tsx 생성
(src폴더에 pages폴더 생성 후 FruitOne.tsx / FruitList.tsx 파일생성)

1) FruitOne.tsx 안에 코드 작성
```typescript
function App(){
  return (
    <>
      상품 1개
    </>
  );
}

export default App;
```

2) FruitList.tsx 안에 코드 작성
```typescript
function App(){
  return (
    <>
      상품 목록
    </>
  );
}

export default App;
```


#### \# 스프링에서 만든 FruitController와 대응되는
FruitOne.tsx와 FruitList.tsx 리액트 내에서 연결하기

1\. 라우터(router) 설명
네트워크 통시에서 가이드 역할을 하는 것
동작 : 라우팅(routing)
라우팅 테이블 : 통신을 어디로 보낼지 가이드하는 방법이 있는 장부

1) AppRoutes.tsx 생성
(src 폴더에 routes 폴더 생성 후 AppRoutes.tsx 파일생성)

1-1) 아래 코드 작성
```typescript
import { Route, Routes } from "react-router-dom";

import FruitOne from './../pages/FruitOne';
import FruitList from './../pages/FruitList';

function App(){
  return (
    <Routes>
      <Route path="/fruit" element={<FruitOne />} />
      <Route path="/fruit/list" element={<FruitList />} />
    </Routes>
  );
}

export default App;
```

1-2) 풀이
path에는 MenuItems.tsx에 적힌 navigate(`/fruit`)과 대응되게 같은 주소를 넣고
element에는 import한 파일명과 대응되게 추가할 파일이름(컴포넌트)을 적는다.


2\. 라우트를 App.tsx의 컴포넌트로 등록해주기
1) App.tsx파일에 AppRoutes.tsx를 import하기
```typescript
import AppRoutes from './routes/AppRoutes';
```

2) return안에 AppRoutes 넣기
```typescript
<AppRoutes />
```


3\. react웹페이지 확인하기
기본 연습 탭 - 과일 1개 클릭 - 주소창에 /fruit가 추가 - 화면상에 "상품 1개"가 나옴
기본 연습 탭 - 과일 목록 클릭 - 주소창에 /fruit/list가 추가 - 화면상에 "상품 목록"이 나옴



#### \# App.tsx의 코드 수정하기 (footer추가)
(전체 코드 복붙)
```typescript
import './App.css';

// 외부 컴포넌트 import하기
// import 컴포넌트이름 from '경로와 파일명';
import MenuItems from './ui/MenuItems';
import AppRoutes from './routes/AppRoutes';

function App(){
  const appName = "IT Academy Coffee Shop" ;

  return (
    <>
      <MenuItems />

	  {/* 라우터 추가 */}
      <AppRoutes />

      <footer className="bg-dark text-light text-center py-3 mt-5">
        <p>&copy; 2025 {appName}. All rights reserved.</p>
      </footer>
    </>
  );
}

export default App;
```



#### \# MenuItems.tsx의 코드 교체하기 (03.기본기 다지기.txt 247번째 줄 이용)
```typescript
import { NavDropdown, Navbar, Container, Nav } from "react-bootstrap";

import { useNavigate } from "react-router-dom";

function App() {
   const navigate = useNavigate();

   return (
      <Navbar bg="dark" variant="dark" expand="lg">
         <Container>
            <Nav className="me-auto">
               <NavDropdown title={`기본 연습`}>
                  <NavDropdown.Item onClick={() => navigate(`/fruit`)}>과일 1개</NavDropdown.Item>
                  <NavDropdown.Item onClick={() => navigate(`/fruit/list`)}>과일 목록</NavDropdown.Item>
               </NavDropdown>
            </Nav>
         </Container>
      </Navbar >
   );
}

export default App;
```



#### \# Fruit.ts파일 생성
(src - type 폴더 생성 후 Fruit.ts 파일 생성)
ts는 typescript 파일을 의미함
백엔드 or 프론트엔트 컴포넌트에 보낼 데이터의 타입을 명시하는 것
FruitOne.tsx에서 useState의 타입으로 사용됨
스프링에서 데이터를 가져올때 사용되기에!
스프링에서 가져올 데이터의 속성과 동일하게? 만들어야 함!!
스프링에서 가져올 데이터는 RestController여서 JSON(key: value형식)으로 반환되어서
이것과 같은 형식으로 만들어야함 (순서는 상관 X)

- 코드 작성
```typescript
// 리액트에서 사용할 과일의 유형은 다음과 같습니다.
export interface Fruit {
    id: string
    name: string
    price: number
}
```

- 코드 풀이
-\> Fruit라는 데이터가 3개의 변수를 가지고 있다는 것? 타입?을 명시함
-\> Fruit라는 객체가 어떤 형태(Shape)여야 하는지 "설계도"를 그린 것


#### \# useState 설명
State는 해당 파일 내에서 바뀔 소지가 있어서 관리해야 하는 데이터들
문법 :
```typescript
const [state변수명, setstate변수명] = useState<타입>(초기값);
ex) const [fruit, setFruit] = useState<Fruit | null>(null);
```
\* | 이 기호는 or이라는 뜻
\* 혹시나 하는 상황에 대비해 넣어놓음

오직 setstate변수명만으로 state변수의 값을 바꿀 수 있음


#### \# useEffect
해당 컴포넌트가 화면에 나타날 때 특정 작업을 자동으로 실행하게 만드는 도구
문법 :
useEffect(() => {}); 매번 도구 호출
\* useEffect(() => {}, \[\]); //  ,\[\]로 인해 한번만! 도구 호출(실행)됨 / 우리가 자주 사용할 코드
useEffect(() => {}, \[prop, state\]); // 바뀔 수 있는 state가 있고, 한번 호출하고 state가 바뀔때마다 호출



#### \# 화살표 함수
(매개변수) => {동작}



#### \# 리액트에서 스프링의 데이터를 받아서 State에 넣어서 사용 (중요!!)(탬플릿)
- 탬플릿
```typescript
const [state변수명, setstate변수명] = useState<타입>(초기값);

// 컴포넌트가 화면에 나타날 때 특정 작업을 자동으로 실행하게 만드는 도구
useEffect(() => { // BackEnd 서버에서 데이터 읽어 오기
	const fetchResult = async () => {
		try {
			// 요청할 url 주소(매핑한 주소) // config.tsx에서 변수 가져와야해서 import도 함
			// 백틱 주의
			const url = `${API_BASE_URL}/주소`;

			// 쿠키 관련 내용인데 나중에 설명해줌
			const config = { withCredentials: true };

			// axios의 get방식으로 메핑된 url에 가서 타입과 동일한 형식의 데이터의 값을 가져와서
            // response에 넣기
			const response = await axios.매핑방식<타입>(url, config);

			// 가져온 데이터를 state변수에 넣기
			setstate변수명(response.data);

		} catch (error) {
			console.log(error);
		}
	};

	fetchResult(); // 직접 호출
}, []);
```


- 항상 같이 다니는 문구
async (비동의 통신 방식)
이 함수는 비동기적으로 실행될 것이라고 선언하는 표식
(비동기적 : 앞선 작업이 끝날 때까지 기다리지 않고, 다음 작업을 즉시 실행하는 방식)
(작업에 시간이 걸리니까 기다리지말고 다음 작업을 하다가 완료되면 작업을 실행함)

await
결과가 올 때까지 기다리되, 기다리는 동안 브라우저가 멈추지 않게 조절하는 정지 문구
(async의 함수로인해 async 함수 밖은 다른 일을 하고 있지만 async안에서는 await로인해
async안에서 일이 순차적으로 진행되다가 await해당 함수는 데이터가 올때까지
기다리다가 데이터가 오면 async안의 다른 일들이 또 순차적으로 진행됨)

- return안의 JSX 영역에 JS 자료 사용하기
JSX영역에 {}를 넣으면 자동으로 JS의 데이터가 온다고 인식해서
스프링에서 JS로 받아온 데이터를 JSX에 쓸때는 {}를 사용하면 됨
그냥 적으면 문자열로 인식함


#### \# 백엔드한테 데이터를 요청하고 웹페이지에 보여주기 (간단 설명) (중요!!)
(03.기본기 다지기.txt 389번째 줄 설명)
(FruitOne.tsx 파일 이용)
해당 컴포넌트는 Spring Boot API(/fruit)에서 과일 데이터를 가져와
React 상태(state)에 저장한 뒤 Bootstrap 테이블을 사용해 화면에
예쁘게 출력하는 기능을 합니다.

- 코드 입력
```typescript
import axios from "axios"

import { useEffect, useState } from "react";
import { API_BASE_URL } from "../config/config";
import { Table } from "react-bootstrap";

import type { Fruit } from "../types/Fruit"

// axios 라이브러리를 이용하여 리액트에서 스프링으로 데이터를 요청해야 합니다.
function App() {
    // Fruit 타입으로 상태를 지정하세요.(Fruit.ts에서 지정한 타입)
    // 처음에는 값이 없으므로 null, 데이터가 들어 오면 Fruit 타입
    // const [state변수, state변경함수] = useState<타입>(초기값);
    const [fruit, setFruit] = useState<Fruit | null>(null); // 넘겨 받은 과일 1개

    // 컴포넌트가 화면에 나타날 때 특정 작업을 자동으로 실행하게 만드는 도구
    useEffect(() => { // BackEnd 서버에서 데이터 읽어 오기
        const fetchResult = async () => {
            try { // 백엔드에 요청하는 내용 작성
                // 요청할 url 주소 // config.tsx에서 변수 가져와야해서 import도 함
                const url = `${API_BASE_URL}/fruit`;

                // 쿠키 관련 내용인데 나중에 설명해줌
                const config = { withCredentials: true };

                // 스프링에서 /fruit가 RestController로 되어있어서 JSON파일로 받아짐
                // <Fruit>라는건 Fruit.ts와 똑같은 형식의 데이터를 해당 url에 가서 찾으라는 말
				// 스프링의 @GetMapping("/fruit")된 곳인 FruitController의 경우
                // bean이라는 Fruit클래스의 객체가 이에 해당함

                // axios의 get방식으로 메핑된 url에 가서 Fruit와 동일한 형식의 데이터의 값을 가져와서
                // response에 넣기
                const response = await axios.get<Fruit>(url, config);

                // fruit라는 State변수에 스프링에서 가져온 데이터인 response의 데이터를 넣음
                setFruit(response.data); // 응답 데이터를 fruit인 state변수에 넣음
            } catch (error) { // 예외처리할때 사용하는 구문 (오류처리)
                console.log(error);
            }
        };

        fetchResult(); // 직접 호출
    }, []);

    return (
        <>
            <Table hover style={{ margin: '20px' }}>
                <tbody>
                    <tr>
                        <td>아이디</td>

                        {/* optional chaining은 객체가 null 또는 undefined일 때 오류 없이 접근하도록 하는 자바 스크립트 문법입니다.*/}
                        {/* optional chaining : fruit가 null → 아무것도 안 나옴(undefined 반환), fruit가 존재 → id 출력 */}
                        <td>{fruit?.id}</td>
                    </tr>
                    <tr>
                        <td>상품명</td>
                        <td>{fruit?.name}</td>
                    </tr>
                    <tr>
                        <td>단가</td>
						{/* toLocaleString은 사용자 지역의 숫자 단위에 맞게 ,등이 생김 */}
                        {/* 원래 10000원이라는 문장을 10,000원으로 바꿔줌 */}
                        <td>{fruit?.price.toLocaleString()}원</td>
                    </tr>
                </tbody>
            </Table >
        </>
    );
}

export default App;
```

\* 이후에 리액트 홈 웹페이지를 켜보고 FruitOne.tsx와 연결된 http://localhost:5173/fruit를 실행해봐도
스프링에서 받아서 fruit state변수에 넣은 데이터인 id, name, price등이 표시가 안됨

(spring과 react의 port number가 달라서 SOP(Same-origin policy)때문에 오류가 남)
Access to XMLHttpRequest at 'http://localhost:9000/fruit'
from origin 'http://localhost:5173' has been blocked by CORS policy: No 'Access-Control-Allow-Origin'
header is present on the requested resource.



#### \# axios 응답 스키마 (React 교안 PDF (P.104))
살펴보기



#### \# CORS (교차 출처 리소스 공유) (IT 관련 용어 PDF (P.56~58))
CORS(Cross-Origin Resource Sharing, 교차 출처 리소스 공유) 라고 부르며,
웹 브라우저에서 다른 도메인(출처)의 리소스(데이터, 이미지, API 등)에 접근할 수 있도록 허용/제어하는 보안 메커니즘
웹 브라우저는 보안상 기본적으로 동일 출처 정책(Same-Origin Policy, SOP)을 따름
즉 포트 번호가 동일하지 않으면 접속을 거부

- 사용 예시
	http://localhost:3000 → http://localhost:3000/api/data (같은 출처 → 허용)
	http://localhost:3000 → http://localhost:9000/api/data (포트 다름 → 차단)
	http://myapp.com → http://api.myapp.com (서브 도메인 달라서 차단)



#### \# CORS 설정하기 (port 다른걸 서로 연결하기) (spring - java에서 하기)
- WebConfig 클래스 생성 (CORS 설정용 파일 생성)
(config 폴더 생성 후 WebConfig 클래스 파일생성 )

- 코드 작성
1) WebConfig 클래스를 @Configuration 어노테이션에 의하여 Spring Boot의 설정 클래스로 등록

2) WebMvcConfigurer를 상속받기
```java
public class WebConfig implements WebMvcConfigurer
```

3) addCorsMappings 메소드 오버라이딩하기
React(3000번 포트)에서 스프링으로 들어 오는
모든 요청을 허용하도록 세부 규칙 설정

- 작성한 코드
```java
package com.coffee.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

// 1) WebConfig 클래스를 @Configuration 어노테이션에 의하여 Spring Boot의 설정 클래스로 등록
@Configuration // 이 파일은 스프링에서 설정용 파일로 사용하겠습니다.
// 2) WebMvcConfigurer를 상속받기
public class WebConfig implements WebMvcConfigurer {
    @Override // 3) addCorsMappings 메소드 오버라이딩하기
    public void addCorsMappings(CorsRegistry registry) {
        // 3000번 포트에서 GET부터 PATCH까지의 열거한 요청들을 모두 수락하겠습니다.
        registry.addMapping("/**") /* 모든 경로 허용  */ // 모든 URL 허용
                /* react 포트 */
                .allowedOrigins("http://localhost:5173", "http://localhost:3000")
                /* 허용할 메소드 */
                .allowedMethods("GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH")
                // 쿠키 전송 허용
                .allowCredentials(true) ;
    }
}
```



#### \# FruitList.tsx 파일에 코드 추가 (FruitOne.tsx처럼)
차이점 : 배열이 state변수임

- 코드작성
```typescript
import { useEffect, useState } from "react";
import type { Fruit } from "../types/Fruit";
import axios from "axios";
import { API_BASE_URL } from "../config/config";
import { Table } from "react-bootstrap";


function App() {
  const [fruitList, setFruitList] = useState<Fruit[]>([]); // 과일 여러개
  // FruitOne과 같이 Fruit.ts를 가져오지만 Fruit.ts의 양식으로 된 변수의 갯수가 여러개여서
  // Fruit[]인 배열로 만들어서 가져오기
  // | null을 넣으면 오히려 오류가 날 수 있어서 넣지 않음


  useEffect(() => {
    const fetchData = async () => {
      try {
        // 해당하는 주소 입력하기
        // 백틱 주의
        const url = `${API_BASE_URL}/fruit/list`;

        // 타입은 state와 동일하게 배열을 입력
        const response = await axios.get<Fruit[]>(url);
        setFruitList(response.data);

      } catch (error) {
        console.log(error);
      }
    }
    fetchData();
  }, []);

  return (
    <>
      <Table hover style={{ margin: '20px' }}>
        <thead>
          <tr>
            <th>아이디</th>
            <th>상품명</th>
            <th>단가</th>
          </tr>
        </thead>
        <tbody> {/* fruitList라는 state는 배열이여서 배열 안에 있는 요소를 꺼내기 위해 map함수 사용 */}
          {fruitList.map((fruit) => // map((매개변수명) => ) // map은 key가 필수 여러가지 요소중 특정하기 위해서
            <tr key={fruit.id}> {/* 데이터 베이스의 primary key같은 느낌 */}
              <td>{fruit.id}</td> {/* 그냥 적으면 문자열로 인식하니까 { }중괄호 사용해서 붙여넣기 */}
              <td>{fruit.name}</td>
              <td>{fruit.price.toLocaleString()}</td>
            </tr>
          )}
        </tbody>
      </Table >
    </>
  );
}

export default App;
```


\---------------------------------------------------------------------------------------------------
컨텐츠 내용 8. 번 부터 시작


(이미지 사용하기)
#### \# 홈 페이지 구현 절차 (03.기본기 다지기.txt)
이미지 파일 복사
"public_images_폴더이미지.zip" 압축해체 후 c드라이브 shop\images 폴더 생성 후 폴더 안에 복사

#### \# 이미지 경로 설정 (03.기본기 다지기.txt)
(application.properties에 해당 코드 있는지 확인)

- 이미지 위치 (윈도우) (운영체제)
```properties
productImageLocation=C:\\shop\\images\\
```

- 업로드 위치 (리눅스) (인텔리제이)
```properties
uploadPath=file:///C:/shop/images/
```
-\> 이건 \가 3개인데 표기법이 원래 이러니까 그러려니 하기


#### \# 이미지 가져오기 (addResourceHandlers() 메소드 이용) (중요!!)
(스프링 - WebConfig)
```java
// 이미지 가져오는 법
// @Value는 값을 자바 변수로 가져오는 어노테이션 / 가져오는 경로는 기본적으로 설정파일 (application.properties)
// 설정 파일에서 uploadPath라는 key가 가진 값을 가져와서 아래의 변수에 값으로 넣어라
// ${ }의 의미 : 스프링(Spring) 프레임워크 전반에서는 "어딘가에 저장된 값을 꺼내올 때 쓰는 공통 약속"
@Value("${uploadPath}")
private String uploadPath ; // file:///C:/shop/images/

// 정적 리소스 핸들러(Static Resource Handler)
// 웹 브라우저의 가상 주소와 컴퓨터의 실제 폴더를 연결하는 다리 역할하는 메소드
// Override from WebMvcConfigurer
@Override // addResourceHandlers : 리소스를 어디서 어떻게 가져올지 규칙을 정하는 메서드 이름
public void addResourceHandlers(ResourceHandlerRegistry registry) { // 등록 대장 객체
	registry // 웹 브라우저의 가상 주소
			// 리액트에서 JSX영역에 해당 소스로 이미지를 요청하면 그 요청을 수락하고
			// 요청 받은 그 이미지를 .addResourceLocations(uploadPath);로 인해
			// uploadPath(application.properties파일에 있는 변수)라는 변수를 통해 운영체제에 해당 위치에 있는
			// 이미지 파일을 가져옴
			.addResourceHandler("/images/**") //**은 이 주소안의 모든 것을 의미

			// 컴퓨터의 실제 폴더 위치
			// @Value 어노테이션에 의해 uploadPath라는 변수를 사용할 수 있음
			.addResourceLocations(uploadPath);

	/* 프로그램 진행 순서 (중요!!!)
	1) <img src="/images/latte.jpg">라는 코드를 실행
```
	2) 브라우저: "스프링 서버야, /images/latte.jpg 파일 좀 줘!
	3) 스프링: "잠깐만, 내 등록 대장(registry)을 확인해 볼게.
	어? /images/\*\* 패턴은 uploadPath로 가라고 되어 있네?"
	4) 서버 시스템: "알겠어. 실제 위치인 C:/shop/images/
	폴더에 가서 latte.jpg가 있는지 찾아볼게."
	5) 결과: 파일을 찾아서 브라우저에 이미지를 띄워줍니다.
	\*/
}

\* (중요!!) 추가적으로 정적 리소스인 이미지, CSS, JS 같은 파일들은
일반적인 데이터인 JSON과는 처리 방식이 달라서
Controller파일을 만들어 매핑을 해줘서 리액트와 스프링을 연결해줘야하는 JSON과 달리
정적 리소스 파일들은 WebConfig에서 따로 매핑 필요 없이 리액트와 스프링 연결 가능
(정적 리소스 파일들은 말 그대로 정적! 변하지 않는 파일이기 때문에 이런 방식이 가능함)


#### \# 프롭스 넘겨주기 (리액트)
App.tsx의 변수 하나를 MenuItems.tsx에 넘겨주는 것
일종의 부모 자식 관계라고 생각하면
App.tsx가 부모 / MenuItems.tsx가 자식

- property (properties -\> props 프롭스)
부모가 자식에게 넘겨주는 값
(key=value 방식)

- 부모에서 1개의 props를 자식에게 주면
자식은 2개의 행동을 해야 함
-\> 받은 프롭스의 type 작성 / 매개변수에 해당 프롭스 추가 및 type 지정

(App.tsx)
프롭스 주기
- 코드 수정 (appName={appName} 추가)
```typescript
<MenuItems appName={appName} />
```

(풀이)
App.tsx가 MenuItems.tsx에게 appName라는 변수명으로
App.tsx에 있는 appName이라는 변수의 데이터의 값을 줌

(MenuItems.tsx)
받은 프롭스 사용
- 코드 수정
1) 받은 프롭스의 type 작성 (import 밑에)
type MenuItemsProps = {
    appName: string;
};
(풀이)
MenuItems이 가진(받은) 프롭스는 ~가 있는데
그중에서 appName은 string타입이다.

2) 매개변수에 해당 프롭스 추가 및 type 지정
2-1) App.tsx에게 받은 프롭스를 매개변수로 추가
- {}을 사용하는 이유
프롭스는 원래 주머니 형태(배열?같은?)로 받아와서 그냥 쓰면 안되고
프롭스에 담긴 것중 사용하고 싶은 것을 {}에 담아서 사용해야 함

- 매개변수에 굳이 프롭스를 넣은 이유
이렇게 한번 프롭스에서 해당 데이터를 꺼내놓으면 그 함수 안에서는
일반 변수처럼 {}없이 사용 가능함
function App({appName}) {

2-2) 매개변수인 프롭스의 type 지정
- 굳이 App.tsx에서 이미 ""로 문자열인 데이터를 가져와서 다시 지정하는 이유
타입스크립트는 독립성을 가지고 있어서 다른 컴포넌트에 들어가면 무슨 타입인지 모름
그래서 해당 컴포넌트에서 사용하려면 타입을 또 다시 지정해야 함

1)단계에서 작성한 type을 이용해서 :(콜론)을 이용해서 지정
function App({appName} : MenuItemsProps) {
(풀이)
프롭스 주머니에서 appName이라는 프롭을 써낸다 : {appName}
프롭스 주머니의 타입은 MenuItemsProps여야 한다 : MenuItemsProps
(이 MenuItemsProps안에 appName의 속성도 정의되어 있음)

3) 확인용으로 콘솔에 입력
console.log('appName프롭스 : ' + appName); // 로그에 표시



#### \# 빨간줄이 뜰때 해결법
빨간줄 뜨는 곳 클릭 후 Ctrl + Space
보통 import가 안되는 상태에서 빨간줄 뜨는건 바로 해결됨

#### \# VSC에 pages폴더 안에 template.tsx파일 생성
기본 코드들을 미리 적어놓아서 탬플릿처럼 사용하려고 만드는 파일
- 코드
```typescript
function App() {
    console.log('자바스크립트 코딩 영역');

    return (
        <>
            JSX 영역
        </>
    );
};

export default App;
```



#### \# JSX 특이 사항 (리액트) (return안쪽)
- class 선택자 대신 className을 사용함
ex)
```typescript
<img
	className=""
	src=""
	alt="크로아상"
```
/>

- JS문법을 적으려면 {}를 쓰고 그 안에 써야 함
ex) src={`${API_BASE_URL}`}


- 템플릿 스트링 (백틱 + 플레이스홀더)
1) 백틱 ( ` ` )
+를 사용하지 않고 문자열로 연결함

2) 플레이스 홀더
변수나 계산식을 문자열의 일부로 변환
ex) ${API_BASE_URL}


#### \# 기본 홈페이지 화면 생성 (리액트)
(pages - HomePage.tsx 파일 생성(template.tsx파일 이용))

- React Bootstrap에서 Carousels찾아서 코드 사용
ex)
```typescript
<img
	className="d-block w-100"
	src={`${API_BASE_URL}/images/whitewine01_bigsize.png`}
	alt="크로아상"
```
/>

- 코드 작성 (HomePage.tsx)
```typescript
import { Carousel, Container } from "react-bootstrap";
import { API_BASE_URL } from "../config/config";

function App() {
    return (
        <Container className="mt-4">
            <Carousel>
                <Carousel.Item>
                    <img
                        className="d-block w-100"
                        src={`${API_BASE_URL}/images/croissant_03_bigsize.png`}
                        alt="크로아상"
                    />
                    <Carousel.Caption>
                        <h3>크로아상</h3>
                        <p>바삭하고 결이 살아있는 프랑스식 버터 페이스트리</p>
                    </Carousel.Caption>
                </Carousel.Item>
                <Carousel.Item>
                    <img
                        className="d-block w-100"
                        src={`${API_BASE_URL}/images/brioche_04_bigsize.png`}
                        alt="브리오슈"
                    />
                    <Carousel.Caption>
                        <h3>브리오슈</h3>
                        <p>달콤하고 부드러운 식감의 버터 함유 빵.</p>
                    </Carousel.Caption>
                </Carousel.Item>
                <Carousel.Item>
                    <img
                        className="d-block w-100"
                        src={`${API_BASE_URL}/images/americano01_bigsize.png`}
                        alt="아메리카노"
                    />
                    <Carousel.Caption>
                        <h3>아메리카노</h3>
                        <p>에스프레소에 뜨거운 물을 추가한 커피.</p>
                    </Carousel.Caption>
                </Carousel.Item>
                <Carousel.Item>
                    <img
                        className="d-block w-100"
                        src={`${API_BASE_URL}/images/whitewine01_bigsize.png`}
                        alt="화이트 와인"
                    />
                    <Carousel.Caption>
                        <h3>화이트 와인</h3>
                        <p>청포도로 만든 가볍고 산뜻한 와인.</p>
                    </Carousel.Caption>
                </Carousel.Item>
                <Carousel.Item>
                    <img
                        className="d-block w-100"
                        src={`${API_BASE_URL}/images/french_baguette_01_bigsize.png`}
                        alt="프랑스 바게트"
                    />
                    <Carousel.Caption>
                        <h3>프랑스 바게트</h3>
                        <p>바삭한 겉과 쫄깃한 속의 긴 막대형 빵.</p>
                    </Carousel.Caption>
                </Carousel.Item>
            </Carousel>
        </Container>
    );
}

export default App;
```


- AppRoutes.tsx에 HomePage.tsx 컴포넌트 추가 및 주소 연결

```typescript
import HomePage from './../pages/HomePage';

<Route path="/" element={<HomePage />} />
```



#### \# 데이터 베이스 연동관련 개념
1) ORM (Object Relational Mapping) (IT 관련 용어 PDF (P.24))
(기술 이름))
자바 객체와 데이터베이스의 테이블 및 컬럼과 맵핑하는 것
Mapping : 같은 이름으로 매칭하는 것
Class <-\> Table (클래스 <-\> 테이블)
Fiedls <-\> Columns (변수 <-\> 컬럼)

2) JPA (Java Persistence API) (IT 관련 용어 PDF (P.25))
(ORM이라는 기술(이론)을 바탕으로 만든 공식 메뉴얼 -\> 공식에 맞춰 생성하면 ORM기술이 써짐)
자바 객체 맵핑 -\>  SQL 데이터 베이스에 쿼리 만들어서(테이블만들어서) 자바 객체랑 맵핑해줘서 -\> 관리 쉬워짐
But 맵핑하기 위해 테이블 만들어 놓고 자바 클래스(Entity) 사라지면 삭제는 자동으로 안해서 내가 삭제 해줘야 함
JPA에서는 자바의 클래스를 클래스라고 하지 않고 Entity라고 부름
Entity : JPA가 관리하는 클래스
\* 사용하는 이유 : 원래는 자바에서 아주 긴 SQL문을 직접 써줘야 하는데 이걸 사용하면 JPA가 알아서 SQL문을 만들어서 DB에 쏴줌
따라서 개발자가 SQL 공부보다는 자바 로직에만 집중할 수 있게 됨



#### \# 데이터 베이스와 연동하기 (JPA이용 - @Entity이용) (중요!!!!!)

```java
@Entity 어노테이션된 클래스를 DB에 JPA를 통해서 연결하는 것 (중요!!!)
```
- 테이블/컬럼 생성 (DDL)
애플리케이션이 실행될 때 @Entity 정보를 읽어서 CREATE TABLE을 실행하는 것은
Hibernate라는 JPA 구현체가 수행하는 초기 설정 작업 (설계, 구조)
<-\> Repository로 DB를 조작하는 것은 : 데이터 반영 (DML)
-\> 프로그램 실행 중에 "새로운 회원 A를 저장해라" 혹은 "회원 B의 이름을 수정해라"와 같은 실제 데이터 로직을 수행


- 연동하기 전에 설정하기
1) MySQL 설정확인 (스프링)
데이터 베이스 연결 설정

1-1) 의존성 확인
(pom.xml 파일에서 코드 확인)
MySQL Driver 의존성
```xml
<dependency>
   <groupId>com.mysql</groupId>
   <artifactId>mysql-connector-j</artifactId>
   <scope>runtime</scope>
</dependency>
```

1-2) application.properties 설정 파일
(application.properties 파일에서 코드 확인)
MySQL 주소 / 이름 / 비밀번호 / 드라이버 확인
```properties
spring.datasource.url=jdbc:mysql://localhost:3306/coffee?useSSL=false&serverTimezone=Asia/Seoul&characterEncoding=UTF-8
spring.datasource.username=root
spring.datasource.password=mysql
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
```


2) JPA 설정확인 (스프링)
2-1) 의존성 확인
(pom.xml 파일에서 코드 확인)
- Spring Data JPA 의존성
```xml
<dependency>
   <groupId>org.springframework.boot</groupId>
   <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
```

- Validation 관련 의존성
(pom.xml 파일에 코드 추가)
(사용자가 입력한 값을 DB에 입력하기전에 그 값이 내가 설정한 규칙에 적절한지 확인함)
```xml
<dependency>
   <groupId>org.springframework.boot</groupId>
   <artifactId>spring-boot-starter-validation</artifactId>
</dependency>
```
-\> 우측 maven 열어서 Reload All maven Projects 누르면 적용됨 (빨간줄 없어짐)


2-2) application.properties 설정 파일
(application.properties 파일에서 코드 확인)
```properties
spring.jpa.properties.hibernate.show_sql=true
spring.jpa.properties.hibernate.format_sql=true
logging.level.org.hibernate.type.descriptor.sql=trace
spring.jpa.hibernate.ddl-auto=update
spring.jpa.database-platform=org.hibernate.dialect.MySQL8Dialect

spring.jpa.properties.hibernate.show_sql=true
spring.jpa.properties.hibernate.format_sql=true
logging.level.org.hibernate.type.descriptor.sql=trace
spring.jpa.hibernate.ddl-auto=update
spring.jpa.database-platform=org.hibernate.dialect.MySQL8Dialect
```


- 정규 표현식
\[\] 안에 있는 것 필수 입력?
```java
@Pattern(regexp = ".*[A-Z].*", message = "비밀 번호는 대문자 1개 이상을 포함해야 합니다.")
@Pattern(regexp = ".*[!@#$%].*", message = "비밀 번호는 특수 문자 '!@#$%' 중 하나 이상을 포함해야 합니다.")
```


- 스프링의 Entity 클래스를 이용해서 DB에 자동으로 테이블 및 컬럼 생성하기 (JPA 사용해보기)
0) 명확한 구분이 되는 값이 있는 컬럼은 enum(열거형) 파일로 따로 정의하기
개발자가 그냥 String으로 정의를 해서 테이블에 저장하면
나중에 값을 넣을때 값이름에 오타가 나면 문제가 생기는데
enum 파일로 따로 정의를 해두면 빨간줄이 뜨면서 오류를 미연에 방지할 수 있음
값이 명확히 정해져 있는 것은 enum 파일로 만들어서 미리 정의를 해두면 이런 오류를 미연에 방지할 수 있어서 이렇게 함
(개발자가 컬럼의 값을 매번 한치의 오차 없이 입력할 수 있다면 이렇게 굳이 안해도 됨) (필수가 아닌 선택!!(중요!!))
\* Java의 enum은 이렇게 고정된 역할(Role)이나 상태(Status)를 정의할 때 유용하게 사용됨 \*
+ 관례적으로 값은 대문자로 작성함

1) 고정된 역할인 Role의 enum 파일 생성
(constant 폴더 생성 - Role이름의 enum파일 생성)
```java
package com.coffee.constant;

// 회원과 관련된 열거형 상수
public enum Role {
    USER, ADMIN
}
```

2) Member Entity 생성하기
(entity - Member 클래스 생성)
```java
package com.coffee.entity;

import com.coffee.constant.Role;
import jakarta.persistence.*;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;
import jakarta.validation.constraints.Size;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import java.time.LocalDate;

@Getter
@Setter
@ToString
@Entity // JPA에게 이 클래스는 DB랑 연결해서 관리해야 할 클래스라는 것을 알리는 어노테이션
@Table(name = "members") // 테이블로 설정하고 테이블 이름을 설정함
public class Member {
    @Id // 프라이머리 키로 설정하기
    // 값 생성하는 어노테이션
    // 방법으로 자동 생성하는 값을 넣음
    @GeneratedValue(strategy = GenerationType.AUTO)
    // 컬럼명 따로 설정하기 - 자바의 변수명은 id지만 DB컬럼명은 member_id가 됨
    @Column(name = "member_id")// pk컬럼명 : 테이블단수명_id
    private Long id ;
	// id를 int가 아니라 Long으로 타입을 설정한 이유
	// int는 4바이트 사용 / Long은 8바이트 사용 -> Long이 더 많은 숫자 사용가능
	// Long은 int보다 많은 숫자를 설정할 수 있어서 보험용으로 Long을 사용하는게 관례임

	@NotBlank(message = "이름은 필수 입력 사항입니다.")
    // 빈칸으로 두면 안되게 설정하고 텍스트를 표시함(데이터베이스의 제약조건느낌)
	private String name ;

    // 컬럼에 제약조건을 속성으로 설정할 수 있음
    @Column(unique = true, nullable = false)
	@NotBlank(message = "이메일은 필수 입력 사항입니다.")
	// 빈칸으로 두면 안되게 설정하고 텍스트를 표시함(데이터베이스의 제약조건느낌)
	@Email(message = "올바른 이메일 형식으로 입력해 주셔야 합니다.")
	// 이메일 형식인지 아닌지 검사하는 것 / 틀리면 메시지 출력
    private String email ;

	@NotBlank(message = "비밀 번호는 필수 입력 사항입니다.")
	// 빈칸으로 두면 안되게 설정하고 텍스트를 표시함(데이터베이스의 제약조건느낌)
	@Size(min = 8, max = 255, message = "비밀 번호는 8자리 이상, 255자리 이하로 입력해 주세요.")
	// 비밀번호의 사이즈 입력 조건 / 틀리면 메시지 출력
	@Pattern(regexp = ".*[A-Z].*", message = "비밀 번호는 대문자 1개 이상을 포함해야 합니다.")
	@Pattern(regexp = ".*[!@#$%].*", message = "비밀 번호는 특수 문자 '!@#$%' 중 하나 이상을 포함해야 합니다.")
    private String password ;

	@NotBlank(message = "주소는 필수 입력 사항입니다.")
	// 빈칸으로 두면 안되게 설정하고 텍스트를 표시함(데이터베이스의 제약조건느낌)
    private String address ;

    // Enum의 상수를 문자열 형태로 DB에 저장하겠다는 어노테이션
    @Enumerated(EnumType.STRING)
    private Role role ;

    private LocalDate regdate ; // 등록 일자
}
```


3) CoffeeApplication.java (main 클래스) 실행
JPA에 의해서  복잡한 SQL문장을 쓸 필요없이 자동으로
Member 엔티티(클래스)에 적힌 양식대로 테이블과 컬럼들 생성 및 제약 조건 설정 해줌
```java
@Entity라는 어노테이션을 JPA가 인식해서 그 안에 있는 것들을 DB와 연결해줌
```
but DB의 데이터를 인식하는 것은 아니라서 DB에서 데이터를 직접삭제해도
main클래스를 다시 실행하면 다시 @Entity의 적힌 내용을 생성해줌
-\> application.properties에 설정된 hibernate.ddl-auto 옵션값이 update로 설정되어있어서
update SQL문으로 생성해주고 컬럼들을 넣고 제약 조건을 넣음

4) MySQL Workbench에서 확인
4-1) coffee 데이터 베이스 사용
use coffee ;

4-2) 테이블 목록 보기
show tables ;
-\>
members 테이블
members_seq 테이블
(id 컬럼의 @GeneratedValue(strategy = GenerationType.AUTO) 어노테이션 때문에 생긴 테이블)

4-3) 테이블의 컬럼 보기
desc members ;
-\>
Field 				Type 								Null 		Key 		Dafault 	Extra

member_id		bigint								NO		PRI
address			varchar(255)					NO
email				varchar(255)					NO		UNI
name				varchar(255)					NO
password			varchar(255)					NO
regdate			date	YES
role					enum('ADMIN','USER')	YES




#### \# Spring Security (SpringBoot 교안 PDF(P.135))
Spring Security 소개
스프링 기반 애플리케이션의 '보안(인증, 인가, 공격 방어)'을 도맡아 처리하는 프레임워크

- 인증 (Authentication)
해당 리소스에 대해서 작업을 수행할 수 있는 주체인지 확인하는 절차
신원 검증 (by 비번, 생체 인식, 일회용 Pin)

- 인가 (Authorization)
인증 절차를 거친 다음에 해당 url에 대하여 인가된 회원인지를 검사하는 기능
인증된 사용자가 실제로 사용할 수 있는 기능이나 서비스를 결정하는 것
특정 기능에 권한을 부여해주는 능력을 의미
일종의 허가권
자원(페이지/기능) 접근 권한



#### \# Spring Security 설정하기 (04.회원.txt 파일)
- 기본 설정 및 확인하기 (스프링)
1\. pom.xml 에 코드 추가 (의존성 파일 추가)
```xml
<dependency>
     <groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-starter-security</artifactId>
</dependency>
```
-\> 이제부터 스프링은 모든 URL(문들)을 security로 잠금

2\. main클래스 실행
콘솔창에
Using generated security password:
확인하기


3\. 홈페이지 접속해보기
3-1) 스프링 홈페이지 접속
http://localhost:9000/fruit 들어가면
자동으로 http://localhost:9000/login로 들어가져서
Username과 Password를 입력하라고 뜸

Username에 user 입력하고
Password에 bde1e08f-60c3-424e-83eb-555ffeef461c 입력 후 로그인하면
http://localhost:9000/fruit?continue 로 이동하고 원래의 화면이 보여짐

http://localhost:9000/logout 들어가면 로그아웃 창도 뜸

-\> 우리가 해야 할 것은 이 로그인 창을 기본 테마말고 우리 마음대로 바꾸는 것!

3-2) 리액트 홈페이지 접속
http://localhost:5173/ 들어가면 페이지는 로딩되지만
Spring Security 때문에 이미지가 보이지 않음

이미지가 계속 보인다면, 브라우저 캐시 메모리 때문이라서
Ctrl + Shift + Delete 눌러서 캐시를 삭제해야 함

-\> 이를 해결 하기 위해서는 스프링에서 보안 설정 클래스를 작성해야 함


- 보안 설정 클래스 작성 (04.회원.txt 파일)
(코드 작성 : SecurityConfig01.txt 파일 참조)
(config폴더에 SecurityConfig 클래스 생성)
Spring Security로 인해 잠긴 URL들을 내 입맛대로 열어주고 규칙을 설정하는 클래스
코드 복붙하기

```java
package com.coffee.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.web.SecurityFilterChain;

@Configuration // 설정용 파일 어노테이션
public class SecurityConfig {

    // 스프링 컨테이너가 관리하는 객체로 설정하는 어노테이션 (Java의 객체를 부르는 이름이 Bean임)
    // 이 어노테이션이 붙으면 그 메소드의 결과물인 반환데이터를 객체화 시켜서
    // 스프링 빈(Spring Bean)이라는 이름으로 스프링 컨테이너에 넣고 관리함
    // 원래 일반적으로 객체를 사용할때는 new연산자를 사용해서 매번 새로 만들지만 이렇게 객체화 시켜서 컨테이너에 저장해놓으면
    // 나중에 해당 객체가 필요할때 새로 생성하지 않고 스프링 컨테이네에서 꺼내다 재사용 할 수 있음
    @Bean
    // SecurityFilterChain : 스프링 시큐리티의 보안 필터들이 순서대로 늘어선 체인(사슬)" 그 자체를 의미하는 인터페이스
    // HttpSecurity : SecurityFilterChain의 필터를 조립하는 도구함
    // throws : 예외 전이 선언문 - 호출한 상위 메서드가 알아서 처리하게 하기 <-> try-catch는 내가 직접 예외사항 처리하기
    // Exception은 모든 예외 상황을 포함하는 최상위 클래스라서 throws Exception은 아주 포괄적인 선언문임
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {

        // 인증 없이 요청을 허용할 url 배열 (배열 생성 초기화 기법)
        String[] permitUrls = {
                "/images/**", "/fruit/**", "/css/**", "/js/**", "/member/signup", "/member/login"
        };

        // Spring Security 기본 정책 : POST / PUT / DELETE 요청은 CSRF 토큰 필요함
        http
                // 사이트 간 요청 위조(CSRF) 방지 기능을 일단 비활성화 시켜 두고 -> (.csrf(csrf -> csrf.disable()))
                // 나중에 JWT를 사용해서 CSRF를 끄고 키고 할 수 있음
                .csrf(csrf -> csrf.disable())
                // 요청에 대한 권한 설정 (인가)
                // .authorizeHttpRequests(auth -> auth ...) : 어떤 주소로 들어오는 요청을 허용하거나 막을지 정하는 구역
                .authorizeHttpRequests(auth -> auth
                        // permitUrls 배열에 담긴 주소들은 누구에게나(Permit All) 허용함
                        .requestMatchers(permitUrls).permitAll()
                        // 그 외의 나머지 모든 요청(anyRequest)은 반드시 로그인(authenticated)을 해야만 볼 수 있게 막음
                        .anyRequest().authenticated()
                )
                // .formLogin(form -> form ...) : 사용자에게 보여줄 로그인 폼에 대한 설정
                // 인증 리다이렉션 경로 지정:
                // -> 로그인이 필요한 페이지에 권한 없는 사용자가 접근하면, 어느 주소로 보낼지(Redirect) 정하는 것
                // 해당 주소로 이동시 어떤 HTML주소를 보여줄지 정하는 컨트롤러와는 다른 개념임
                // 따라서 리다이렉션도하고 컨트롤러에서 "/member/login" 에 맞는 HTML도 따로 설정해줘야함
                .formLogin(form -> form
                        // 스프링이 제공하는 기본 로그인창 대신, 직접 만든 /member/login 주소의 화면을 로그인 페이지로 사용
                        .loginPage("/member/login")
                        // 로그인 페이지 자체는 로그인을 안 한 사람도 접근할 수 있어야 하므로 접근을 허용
                        .permitAll()
                );

        // 다른 도메인(예: 리액트 포트 5173)에서 오는 요청을 허용하기 위한 기초 설정을 적용
        // SecurityConfig의 이 설정이 없을때는 다른 오리진에서 들어오는 것을
        // WebConfig의 WebMvcConfigurer가 직접 결정하는데
        // 이 설정이 생기면 이제부터는 오리진 허용 여부도 SecurityConfig가 관리하고
        // WebConfig의 WebMvcConfigurer는 단순히 설정된 값만 SecurityConfig에게 전달하게 됨
        // * 사실상 이 코드는 WebMvcConfigurer의 내용 전체를 가져오는 것과 같음 *
        // 따로 설정도 가능하지만 공백으로 두어서 WebMvcConfigurer 내용을 가져와서 사용하게 함
        http.cors(cors -> {});

        // 지금까지 http 도구함에 담은 모든 설정들을 빌드해서
        // 실제 동작하는 보안 필터 객체(SecurityFilterChain)를 생성하여 반환
        return http.build();
    }
}
```

- 브라우저 접속 테스트 (04.회원.txt 파일)
1\. 홈페이지 접속	http://localhost:5173/
SecurityConfig에서 따로 홈(/)에 대한 설정이 안되어 있어도
리액트 홈은 스프링에게 API로 요청한 내용이 없기에 SecurityConfig가 검문할 방법도 없어서
따로 허용하지 않아도 잘 들어가짐
+ 홈페이지의 이미지들은 permitUrls에 허용이 되어있어야 에러없이 잘 보임

2\. permitUrls로 허용된 홈페이지 접속
과일 1개 보기 페이지 접속	http://localhost:5173/fruit
과일 여러개 보기 페이지 접속	http://localhost:5173/fruit/list




#### \# Repository 생성
(repository폴더 생성 후 MemberRepository 인터페이스 생성)
```java
package com.coffee.repository;

import com.coffee.entity.Member;
import org.springframework.data.jpa.repository.JpaRepository;

// 리파지토리는 설계도이자 부품이여서
// 이 부품을 쓰는 비즈니스 로직인 Service 클래스를 이용해서 사용함

// 리파지토리를 클래스가 아닌 인터페이스로 만드는 이유 :
// 리자피토리 기능을 수행하기 위해서 JpaRepository 인터페이스를 상속받아야 하는데
// 클래스로 이 인터페이스를 상속받으면 이 인터페이스에 있는 모든 메소드를 반드시
// 오버라이드해야하는데 인터페이스들끼리 상속받으면 이 의무가 없기때문에 효율적으로 사용이 가능함

// JpaRepository : Spring에서 제공하는 부모 인터페이스 / 기본적인 CRUD(Create, Read, Update, Delete) 메소드를 이미 다 가지고 있음
// <Member, Long> : 제레닉 : 이 repository가 관리할 대상은 Member 클래스 / 관리 대상의 기본키로 설정된 변수의 데이터 타입
// 관리할 대상과 관리 대상의 기본키로 설정된 변수의 데이터 타입을 적는 이유는
// JPA는 이 2개로 DB에서 사용자가 원하는 정보를 찾기 때문에 그냥 DB를 사용한다면 기본키가 없어도 되지만
// JPA를 사용한다면 기본키가 무조건 있어야 한다.

// repository의 구체적인 역할 : 서비스(Service)로부터 요청을 받아서 실제 DB에 관여하는 역할
// CRUD(Create 생성-insert / Read 조회-select / Update 수정-update / Delete 삭제-delete)를 복잡한 SQL 명령어 대신 자바 언어를 써서
// DB를 조작할 수 있게 해주는 역할
// 이 자바 언어는 요청하는 곳인 서비스(Service)에 작성함
public interface MemberRepository extends JpaRepository<Member, Long> {
}
```



#### \# Spring DI (Dependency Injection) (의존성 주입)
- 의존
어떠한 클래스가 정상적으로 굴러가기 위해서 어떠한 데이터가 필요한 것
ex) CarMain01 클래스가 정상적으로 굴러가기 위해서는 Person 클래스의 객체 정보가 필요함
-\> CarMain01 클래스는 Person 클래스를 의존하고 있음
```java
public class CarMain01 {
	public static void main(String[] args) {
		// 생성자를 이용하여 Constructor Injection을 수행하고 있습니다.
		Person bean = new Person("김철수", 25, "남자");
		System.out.println(bean.toString());
	}
}
```


- 주입
의존해서 해당 클래스가 정상적으로 굴러가기 위해 데이터를 넣어주는 것
ex) CarMain01이 Person에 의존하기 위해서 필요한 Person의 객체의 값을
의존하는 중인 CarMain01이 주입하는 주체가 되어 값을 주입하고 있고
주입하는 통로를 의존시켜주는 Person클래스가 생성자로 만들어둔 상태


```java
public class CarMain01 {
	public static void main(String[] args) {
		// 생성자를 이용하여 Constructor Injection을 수행하고 있습니다.
		Person bean = new Person("김철수", 25, "남자");
		System.out.println(bean.toString());
	}


@ToString
public class Person {
	private String name ;
	private int age ;
	private String gender ;

	public Person(String name, int age, String gender) {
		this.name = name ;
		this.age = age ;
		this.gender = gender ;
	}
}
```

- 의존성 주입의 종류
1) 생성자 주입(Constructor Injection)
클래스의 생성자의 매개 변수로 의존성 정보를 전달시켜 객체를 생성
\* 참고로 위의 예시가 생성자 주입의 예시
2) 세터 주입(Setter Injection)
클래스의 setter() 메소드를 통해 의존성을 주입하는 방식
3) 필드 주입(Field Injection)
```java
@Autowired 어노테이션을 사용하여 멤버 변수에 직접 의존성을 주입하는 방식
```



#### \# Member 엔티티의 Test를 위한 준비
(백엔드 기능이 실제로 잘 작동하는지 테스트해보기 위해서)
- pom.xml에 의존성 추가
```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope> <!—삭제 요망 -->
    </dependency>
```

주의)
src/test/java에서 @SpringBootTest를 \<scope\>test\</scope\>를 사용하려면 지우지 않아도 됨
src/main/java에서 사용하면 컴파일 에러가 발생하므로 지워야함
-\> main에서 사용하려고 하기 때문에 지움

- SecurityConfig.java에 패스워드 암호화를 위한 코드 입력
(config - SecurityConfig)
```java
@Bean // 비밀번호를 암호화하는 메소드 (BCrypt 방식)
// "admin@naver.com"을 DB에 "$2a$10$JvA36EqRtX4EHtsv42wUXeO6ma9OpdvxO7sZ6rhufqMbTgkclmacW"로 저장함
public PasswordEncoder passwordEncoder() {
	return new BCryptPasswordEncoder();
}
```

- MemberTest 클래스 생성
(test 폴더 생성 후 - MemberTest 클래스 생성)
```java
package com.coffee.test;

import com.coffee.constant.Role;
import com.coffee.entity.Member;
import com.coffee.repository.MemberRepository;
import lombok.RequiredArgsConstructor;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.test.context.TestConstructor;

import java.time.LocalDate;

// 백엔드 기능이 실제로 잘 작동하는지 테스트해보기 위해서 만드는 테스트 클래스

// 스프링 부트의 모든 설정(Bean, 리파지토리 등)을 다 불러와서 테스트 환경을 만듭 / 실제 서버를 띄운 것과 거의 같은 환경을 빌려옴
@SpringBootTest
@RequiredArgsConstructor // 필수/재료/생성자
// final(필수)이 붙은 변수는 값이 무조건 있어야하는데 값이 없는 변수가 있으면 (의존하는 변수)
// 그 변수를 찾아서 아래와 같은 코드를 보이지 않게 자동으로 작성해줌 (주입해주기)
// public MemberTest(MemberRepository memberRepository) {
//    this.memberRepository = memberRepository;
//}
// 매개변수 MemberRepository memberRepository는 스프링이 미리 만들어 놓은 객체여서 이 객체의 값을 대입하면 사실상
// 이 MemberTest 클래스이 변수인 memberRepository가 객체가 되는거임
// 따라서 해당 객체의 맴버 변수와 맴버 메소드를 사용 가능함
@TestConstructor(autowireMode = TestConstructor.AutowireMode.ALL) // 테스트용 어노테이션
public class MemberTest {
    private final MemberRepository memberRepository;
    private final PasswordEncoder passwordEncoder;

    @Test // main메소드가 없어도 run할 수 있게 만들어주는 어노테이션 (일종의 가짜 main메소드)
    @DisplayName("회원 몇 명 추가하기") // 테스트 결과 창에 insertMember라는 코드 이름을 ""안의 문자열로 보여줌
    // id는 자동생성되게 @GeneratedValue(strategy = GenerationType.AUTO)를 써서 setter하지 않음
    void insertMember(){
        Member mem01 = new Member();
        mem01.setName("관리자");
        mem01.setEmail("admin@naver.com");
        mem01.setPassword(passwordEncoder.encode("admin@naver.com")); // 비밀번호 암호화
        mem01.setAddress("마포구 공덕공");
        mem01.setRole(Role.ADMIN);
        mem01.setRegdate(LocalDate.now());

        memberRepository.save(mem01); // 리파지토리에 해당 객체의 데이터를 저장하기
        System.out.println("----------------------------------------");

        Member mem02 = new Member();
        mem02.setName("유영석");
        mem02.setEmail("bluesky@naver.com");
        mem02.setPassword(passwordEncoder.encode("Bluesky@456"));
        mem02.setAddress("용산구 이태원동");
        mem02.setRole(Role.USER);
        mem02.setRegdate(LocalDate.now());
```

        memberRepository.save(mem02) ;
        System.out.println("----------------------");

        Member mem03 = new Member();
        mem03.setName("곰돌이");
        mem03.setEmail("gomdori@naver.com");
        mem03.setPassword(passwordEncoder.encode("Gomdori@789"));
        mem03.setAddress("동대문구 휘경동");
        mem03.setRole(Role.USER);
        mem03.setRegdate(LocalDate.now());

        memberRepository.save(mem03) ;
        System.out.println("----------------------");
    }
}

\* memberRepository.save(mem03) ;의 save메소드는 CrudRepository에 있음 (할아버지? 부모를 넘어서)


- MySQL Workbench에서 확인하기
select \* from members ;  실행
데이터가 한 행 들어가 있으면 성공



#### \# JpaRepository로 SQL문법대신 Java문법으로 DB 제어하는 명령어들
save(entity) : INSERT INTO ... (새로운 데이터)
save(entity) : UPDATE ... SET ... (ID가 있는 객체에 넣으면 자동으로 수정)
findById(id) : SELECT \* FROM ... WHERE id = ? (특정 PK(id)값으로 데이터를 조회)
findAll() : SELECT \* FROM ... (데이블의 모든 데이터 조회)
delete(entity) : DELETE FROM ... WHERE id = ? (특정 데이터 삭제)
count() : SELECT COUNT(\*) FROM ... (갯수 조회)



#### \# JSX에서 주석 넣는 법
Ctrl + / : {/\* \*/}



#### \# MySQL Workbench
delete from members ; 를 하기 위해서 안전모드 비활성화하기 (My-Sql 설치&설정 PDF (P.25))
Edit - Preferences... - SQL Editor - Safe Updates (rejects UPDATEs and DELETEs with no restrictions) 체크해제
만약 MemberTest를 이전에 실행하고 다시 실행하면 데이터 중복돼서 에러가 남
기존의 members 데이터를 없애기 위해 해당 쿼리 실행
(그냥 java 실행하면 이미 추가했던 unique데이터 중복돼서 에러남)



#### \# REST API (IT 관련 용어 PDF (P.36))
- 4대 구성 요소
Method + 요청 경로 + Content Type + Parameter = REST API

- Method (동사: 행위) (CRUD와 1대1 대응됨)
사용자의 요청(URL)을 서버의 어떤 기능과 연결(Mapping)할지 경정하는 기준

REST Method (웹 요청)	CRUD (개념)		DB SQL (명령어)		JPA 메서드 (Java)
POST								Create (생성)		INSERT						save()
GET									Read (조회)			SELECT						findById() / findAll()
PUT / PATCH					Update (수정)		UPDATE					save() (ID가 있을 때)
```sql
DELETE							Delete (삭제)		DELETE					delete()
```


- 요청 경로 (명사: 대상) (URL)
누구에게(어디에) 할 것인가?
ex) (1번 회원)처럼 자원(Resource)을 명시
/members, /members/1


- 응답 콘텐츠/Content Type (유형: 포맷)
데이터를 어떤 형태로 주고받을 것인가?


- 파라미터 (상세 내용: 조건)
어떤 조건이나 데이터를 보낼 것인가?
로그인할 때의 아이디/비밀번호 데이터나, 특정 페이지 번호 등


- URL의 자원 vs 파라미터
1) 자원 (Resource) = 어떤 페이지(또는 데이터)인가? (대상)
URL의 경로(Path)에 위치 (주로 명사로 표현)
데이터의 고유한 번호(ID)나 카테고리처럼 그 데이터를 가리키는 절대적인 주소일 때 사용
ex)
/members : 회원 전체 (자원)
/members/1 : 1번 회원 (특정 자원)
/members/1/orders : 1번 회원의 주문 목록 (연관된 자원)

2) 파라미터 (Parameter) = 어떻게 보여줄 것인가? (방법)
파라미터(Query Parameter)는 URL 끝에 ? 뒤에 붙으며, 자원을 필터링, 정렬, 검색할 때 사용
데이터의 본질은 바뀌지 않지만!!!! 보여주는 방식이나 범위만 바뀜
있어도 그만, 없어도 그만인 추가 조건 (중요!!)
ex)
/members?role=ADMIN : 회원들 중 '관리자'만 골라서(필터링)
/members?page=2 : 회원 목록의 2페이지를(페이징)
/members?sort=regdate,desc : 회원 목록을 등록일순으로(정렬)



#### \# 서버의 응답 코드(Status Code) (IT 관련 용어 PDF (P.54))
- 100번대 (정보) : 요청을 받아 처리 중

- 200번대 (성공) (중요함) : 클라이언트의 요청이 성공적으로 처리되었음을 알려줌

- 300번대 (경로 변경) : 	요청을 완전히 처리하기 위해 추가적인 액션 수행
										301 : sendRedirect을 사용하게 되면 header 정보에 들어가는 상수
										302 : 강제 페이지 이동할 때 많이 사용하는 코드

- 400대 (클라이언트 에러) : 	클라이언트의 요청에 오류가 있는 경우에 발생
												파일 발견이 되지 않는 경우에 발생
												사용자의 오타로 인하여 페이지를 찾을 수 없음

- 500대 (서버 에러) :	클라이언트의 요청에 오류가 있는 경우에 발생
									문법적인 오류로 인하여 발생
									사용자의 오타로 인한 경우에 발생







#### \# 회원 가입 페이지 : SignupPage.tsx (react) (src/pages/에 생성) (04.회원.txt)
해당 tsx 파일 참고


#### \# SignupPage.tsx (react)의 라우팅 설정
(AppRouters.tsx) (리액트)
- 코드 추가
```typescript
import SignupPage from './../pages/SignupPage';

<Routes>
	... 생략
	<Route path='/member/signup' element={<SignupPage />} />
</Routes>
```


#### \# SignupPage.tsx (react)의 링크 설정
(MenuItems.tsx) (리액트)
- 코드 추가
```typescript
<Nav className="me-auto">
    <Nav.Link onClick={() => navigate(`/member/signup`)}>회원 가입</Nav.Link>           // 이 문장 추가
    ... 코드 생략
</Nav>
```


#### \# 리파지토리에 쿼리 메소드 추가 (04.회원.txt)
(MemberRepository.java)
- 코드 추가
// 이메일을 사용하여 회원 정보를 조회하는 쿼리 메소드
// 인터페이스여서 만들어 놓기만 하고 Spring Data JPA가 자동으로 구체화 해서 실행해줌
// findBy+컬럼명 = select(SQL) / Get 매핑 / read(CRUD)
// 반환타입이 Member인 findByEmail이 메소드명인 메소드
Member findByEmail (String email);


#### \# 서비스 작성 (스프링) (04.회원.txt)
- 파일 생성 : com.coffee안에 service폴더 생성 후 안에 MemberService 클래스 생성
회원 관리 기능의 핵심 로직을 담당하는 `MemberService` 클래스

- 코드 작성 : MemberService01.txt 파일 참조
```java
package com.coffee.service;

import com.coffee.constant.Role;
import com.coffee.entity.Member;
import com.coffee.repository.MemberRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.time.LocalDate;

@Service
@RequiredArgsConstructor
public class MemberService { // MemberService가 MemberRepository를 의존하고 있음
    // 의존 + 무의미한 데이터여서 주입(injection)해야 함 + final로 변경
    private final MemberRepository memberRepository;

    public Member findByEmail(String email){
        return memberRepository.findByEmail(email);
    }

    @Autowired // 필드 주입 : 맴버 변수에 직접 의존성을 주입하는 방식 (@RequiredArgsConstructor 이용해도 됨)
    private PasswordEncoder passwordEncoder;

    public void insert(Member bean){
        // 회원 가입한 사용자의 역할과 등록 일자는 여기서 설정
        bean.setRole(Role.USER);
        bean.setRegdate(LocalDate.now());

        String encodedPassword = passwordEncoder.encode(bean.getPassword());
        bean.setPassword(encodedPassword);

        memberRepository.save(bean);
    }
}
```



#### \# 컬렉션 개요 (Java 교안(이론_20260226) PDF (P.153))
- MapTest.java 생성
코드 추가해서 Map 컬렉션 생성 테스트

- 코드 작성
```java
package com.coffee.test;

import java.util.HashMap;
import java.util.Map;

public class MapTest {
    public static void main(String[] args) {
        // Map<키, 값>
        Map<String, String> errors = new HashMap<>();

        errors.put("password", "비밀 번호 누락"); // error.put(String key, String value);
        errors.put("email", "이메일 잘못 들어옴");

        System.out.println(errors);
        // 출력 : {password=비밀 번호 누락, email=이메일 잘못 들어옴}
```

        Map\<String, String\> colors // Map.of(key, value, key, value ......);
                = Map.of("red", "빨강", "blue", "파랑", "yellow", "노랑");
        System.out.println(colors);
        // 출력 : {yellow=노랑, blue=파랑, red=빨강}
    }
}



#### \# 컨트롤러 작성 (스프링) (04.회원.txt)
- 파일 생성 : com.coffee안에 controller폴더 안에 MemberController 클래스 생성
리액트에서 SignupAction 함수 구현시 요청 url 주소가 `/member/signup`이었고, 요청 메소드는 post 방식임 (post - Create)

- 코드 작성 : MemberController01.txt 파일 참조
```java
package com.coffee.controller;

import com.coffee.entity.Member;
import com.coffee.service.MemberService;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.BindingResult;
import org.springframework.validation.FieldError;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequiredArgsConstructor
public class MemberController {
    private final MemberService memberService;

    // @Valid : Member 엔티티에 @NotBlank(공백 불가)나 @Size(글자수 제한) 같은 유효성 검사 규칙이 있다면
    // 프론트엔드에서 데이터를 보낼때 해당 규칙에 맞게 보냈는지 검사하는 어노테이션
    // BindingResult : 방금 @Valid로 검사했을때 오류가 있는지 없는지에 대한 결과를 담는 바구니
    // @RequestBody : 리액트가 보낸 JSON 데이터를 Java 형식으로 변환해서 Member 객체(변수명 bean)에 넣음
    // 따라서 리액트가 보내는 파라미터의 이름과 그걸 받는 엔티티(Member)의 맴버 변수의 이름이 동일해야 자동 매핑됨
    // Controller까지는 그대로의 데이터, 그 이후인 Service에서 암호화를 하든 말든 함
    @PostMapping("/member/signup")
    // ResponseEntity<?> : http 상태 코드, 헤더(부가정보), 바디(프론트가 쓸 알맹이)
    // 이 3가지를 한번에 보낼 수 있는 반환타입 (<?> 이 와일드 카드는 여러 타입의 데이터가 동시에 들어가도 상관없다는 뜻)
    // 만약에 에러코드 (ex-400)를 반환하면 리액트에서는 try로 안들어가고 바로 catch (error)로 들어감
    public ResponseEntity<?>signup(@Valid @RequestBody Member bean, BindingResult bindingResult){
        System.out.println("회원 가입 정보");
        System.out.println(bean);

        // hasErrors() : 에러가 존재하면 true를 리턴함 (SpringBoot 교안 PDF (P.146))
        if(bindingResult.hasErrors()){
            Map<String, String> errors = new HashMap<>();
            // 확장 for 사용
            // bindingResult의 getFieldErrors() 바구니에서 에러들을 FieldError 타입으로 꺼내서 Map에 넣음
            for(FieldError xx:bindingResult.getFieldErrors()){// Field:Java에서의 변수(name,password등)
                errors.put(xx.getField(), xx.getDefaultMessage());
            }
            System.out.println(errors);
            // Map 형식을 프론트에 반환함
            return new ResponseEntity<>(errors, HttpStatus.BAD_REQUEST);
        }else{
            System.out.println("ok");
        }

        // 이메일 중복 체크
        Member member = memberService.findByEmail(bean.getEmail());
        if (member != null){ // member가 null이 아니라는 것은 이미 존재하는 id(맴버)라는 것을 의미함
            // 이미 존재하는 이메일 주소
            // Map.of : Map 컬렉션의 축약버전
            // <>안에 원래 타입을 적어줘야하는데 스프링이 알아서 Map<String, String>을 뒤에 Map.of보고 추론함
            // ResponseEntity(T body, HttpStatus status) 생성자 이용
            return new ResponseEntity<>(Map.of("email", "이미 존재하는 이메일 주소입니다."),
                    HttpStatus.BAD_REQUEST);
        }

        // 회원 가입 처리
        memberService.insert(bean); // memberService에서 insert메소드를 넣어서 나머지 정보들도 넣음
        return new ResponseEntity<>("회원 가입 성공", HttpStatus.OK) ; // 회원 가입 성공 (OK라는건 200번대라는 뜻)
    }
}
```



#### \# 로컬 스토리지(localStorage)확인하는 법
크롬 - F12 - Application - Storage - Local storage



#### \# JWT 시작
#### \# axiosInstance.tsx (리액트) (04.회원.txt)
src - api 폴더 생성 - axiosInstance.tsx 생성)

- 코드 작성
```typescript
// 로그인 인증(JWT)을 자동으로 처리해주는 커스텀 axios 설정 파일
// get방식 post방식 등을 계속해서 요청하지 않고 자동으로 하게 만드는 파일

// 즉, API 요청할 때마다 토큰 붙이고
// 인증 실패(401)하면 자동 로그 아웃까지 처리해주는 구조입니다.
// 전체 과정 : 토큰확인 - 토큰이 없거나 올바르지 않은 토큰일 경우 삭제 후 로그인 페이지로 보내서 새로운 토큰 생성 유도

import axios from "axios";
import { API_BASE_URL } from "../config/config";

// withCredentials: true 항목은 세션 방식 설정이므로 jwt를 사용하면 삭제하도록 합니다.
const axiosInstance = axios.create({
    baseURL: API_BASE_URL
});

// 인터셉터(interceptor) : 요청(Request)이나 응답(Response)을 가로 채서 공통 로직을 처리하는 기능입니다.
// 요청(Request) : ~하기 전에 가로채기 (사전)
// 응답(Response) : ~한 후에 가로채기 (사후)
// 요청을 보내기 전에 인터셉터가 자동으로 JWT 붙이기 (사전에 가로채기)
// 토큰을 확인하는 과정
// 스프링 서버로 요청보내기 바로 직전에 가로채서 무조건 실행할 공통 로직
```
axiosInstance.interceptors.request.use(
```typescript
    (config) => { // 가로챈 요청의 모든 설정 정보(주소, 헤더, 데이터 등)를 config에 넣어서 가져옴
        // 로컬스토리지에서 이전 로그인 성공때 저장했던 "accessToken"(JWT 토큰 입장권)이 있는지 token 변수에 담아봄
        // 로컬스토리지에 "accessToken"(JWT 토큰 입장권)이 있다 : 로그인한 회원 + 토큰기한이 지나지 않음
        const token = localStorage.getItem("accessToken");
        console.log("interceptors.request 토큰 확인 : ", token);

        // 토큰 확인 token이 true이면 로그인한 회원이라는 뜻
        if (token) { // token가 undefined일 수 있으므로...
            // config.headers 공간 자체가 없더라도 에러나지 않게  {}라는 빈공간이라도 만들어두기
            config.headers = config.headers || {};
            // Bearer 단어 대소문자 주의 바람 + token 사이에 한칸 공백 주의
            // Spring Security에서 확인할때 Bearer 뒤에 있는 token을 보고 허가를 해줌
            config.headers.Authorization = `Bearer ${token}`;
        }

        // token이 있으면 config.headers.Authorization에 `Bearer ${token}`을 넣은 config를 반환함
        // token이 없으면 빈 봉투로 스프링에 보내게 됨
        // 스프링에서 SecurityConfig에서 permitAll() 된 부분이면 통과되고 아닌 부분이면 거부됨(401에러 반환됨)
        return config;
    },
    // 스프링 서버에 요청하기도 전에 리액트 자체 내부 오류로 인해 전송 에러가 발생하면 에러를 그 다음단계로 거절하며 넘김
    // ()=> 여기에서 {}를 안적으면 return을 생각해서 바로 return 할 값만 적어도 됨
    // error 발생시 스프링에 보내지 않고 리액트 내부에서 에러처리를 함 (try-catch(error)의 catch부분 실행됨)
    (error) => Promise.reject(error)
);

// 응답 처리 : 401 에러 발생 시 자동 로그 아웃 처리 (사후에 가로채기)
// 401에러 : 인증이 필요하거나 실패했다는 의미
// 올바르지 않아서 401에러가 생긴? 토큰 삭제 후 로그인 페이지로 유도하기
// 스프링 서버로부터 응답을 받고 다른 리액트 코드로 들어가기전에 바로 가로채서 무조건 실행할 공통 로직
```
axiosInstance.interceptors.response.use(
```typescript
    // HttpStatus.OK (200번대)같은 응답이 오면 그대로 response로 보내줌
    // () => {} 중괄호를 안써서 return 단어를 생략함
    (response) => response,
    (error) => { // 400, 401, 500 같은 오류 코드로 온다면 가로채서 검사함

        // 현재 에러가 난 이 요청이 "혹시 로그인 하려고 시도했던 요청이었나?"를 판별하는 중
        // 로그인 시도 중 비번을 틀려서 난 401 에러와, 로그인 후 토큰이 만료되어 난 401 에러를 구분 가능
        // url에 "/member/login"가 포함되어 있다면 로그인 시도중 비번 틀린 오류
        const isLoginRequest = error.config?.url?.includes("/member/login");

        // 401오류인데 url 주소에 "/member/login"가 포함되어있지 않다면
        // 토큰 유효기간이 만료되었거나 토큰이 처음부터 존재하지 않았거나해서 인증이 안된상태
        if (error.response?.status === 401 && !isLoginRequest) {
            // 만료된 토큰 삭제처리 (+ 로그아웃 처리)
            localStorage.removeItem("accessToken");

            // window.location.href 사용시 React Router 사용 중이면
            // 페이지 전체 리로드 발생할 수 있으므로 replace() 메소드 사용 바람
            // 인증이 안된 사용자를 강제로 로그인페이지("/member/login")로 이동시킴
            // replace()를 사용하면 뒤로가기 기록도 삭제해서 뒤로가기 버튼을 사용하지 못함
            window.location.replace("/member/login");
        }

        return Promise.reject(error);
    }
);

export default axiosInstance;
```



#### \# User.ts (리액트) (04.회원.txt)
(src - types - User.ts 생성)
리액트 앱 내부에서 사용하는 사용자 모델을 처리해주는 타입 스크립트 인터페이스를 작성
\* 여기서 export는 Java의 public같은 것 - 모든 곳에서 사용해야하니까

- 코드 작성
/\*
TypeScript 타입 정의
User라는 객체는 반드시 다음 형태이어야 함을 알려 주는 타입(설계도)입니다.

이건 문자열 리터럴 유니온 타입 입니다.
role은 오직 "USER" 또는 "ADMIN"만 가능합니다.
```typescript
*/
/* 리액트 앱 내부에서 사용하는 사용자 모델 */
export interface User {
    id: number;
    name: string;
    email: string;
    role: "USER" | "ADMIN";
}

/* 서버가 로그인 시 내려주는 응답 */
// LoginResponse는 User를 포함 (상속함)
export interface LoginResponse extends User {
    accessToken: string;
}
```



#### \# MIME type (IT 관련 용어 PDF (P.50))
(Content type이라고도 함)
파일이나 데이터의 "종류(형식)"를 나타내는 표준 문자열
-\> JSON으로 줄때는 application/json 이런 양식을 적어서 줘야한다는 것을 약속함

- 기본 구조
type/subtype

ex)
text/html (메모장으로 볼 수 있는 html형식이구나) → 브라우저가 웹페이지로 렌더링
application/json → 데이터로 처리 (JS에서 사용)
image/jpeg (그림판으로 볼 수 있는 jpef형식이구나) → 이미지로 표시
application/xml

- http로 MIME type을 이용해서 보낼때
header부분과 body부분이 있음
```typescript
const config = {
	headers: {
		"Content-Type": "application/json"
	}
};
```
header 부분에 어떤 것을 넘길때 이렇게 작성함



#### \# 전개 연산자 (React 교안 (P.41))
나열형 자료(배열, 객체 등)를 개별로 추출하거나 연결하고자 할 때 사용하는 연산자

- 예시
1) 배열 - 순서 중요
```typescript
const numbers = [1, 2, 3, 4, 5, 6];

const [one, two, ...rest] = numbers;
// one에 숫자 1이, two에 숫자 2의 값이 저장됩니다.
// 변수 rest에 나머지 항목 [3, 4, 5, 6]이 저장됩니다.
```

2) 객체 - 순서 X / key에 연결된 값을 가져옴 // 서버의 응답을 전개 연산자로 처리
response.data는 스프링의 RestController 때문에 JSON 형식이라 key와 value로 나뉘어져있음
```typescript
// accessToken는 JWT, userData는 User.ts으로 구성된 객체
const { accessToken, ...userData } = response.data;
```


#### \# LoginPage.tsx (리액트) (04.회원.txt)
(src - pages - LoginPage.tsx 생성)

- 코드 작성
```typescript
import { useState } from "react";
import { Alert, Button, Card, Col, Container, Form, Row } from "react-bootstrap";
import { Link, useNavigate } from "react-router-dom";

import axios from "../api/axiosInstance.tsx";
import type { LoginResponse, User } from "../types/User";

interface Props {
    // App.tsx -> AppRoutes.tsx를 거쳐온 프롭스(정보가 들어오면 App.tsx에 데이터를 보내야함)
    // onLogin 프롭스는 User 형식으로 매개 변수를 받고, 반환 타입이 없습니다.
    onLogin: (user: User) => void;
}

function App({ onLogin }: Props) { // 프롭스를 매개변수에 넣어서 사용할 수 있게 함
    // 이 문서내에서 바뀔 소지가 있는 것들은 state로 만들어 관리 할 수 있음
    // props는 부모에게서! 받은거고 / state는 자신의 문서 내에서! 있는 것들이고
    // 로그인과 관련된 state (로그인에 필요해서 스프링에서 정보 대응시킴)
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    // 에러 관련 메시지
    const [errors, setErrors] = useState('');

    const navigate = useNavigate();

    const handleLogin = async (event: React.SubmitEvent) => {
        event.preventDefault(); // 새로고침 방지
        console.log('로그인 시도중입니다.');

        try {
            const url = '/member/login';
            const params = { email, password }; // 파라미터
            const config = {
                headers: { // 헤더에 MIME type 적어서 요청
                    "Content-Type": "application/json"
                }
            };
            // 요청해서 가져올 데이터를 LoginResponse 형식으로 요청함
            const response = await axios.post<LoginResponse>(url, params, config);

            console.log('응답 데이터 : \n' + response.data);

            // 서버의 응답을 전개 연산자로 처리합니다.
            // accessToken는 JWT, userData는 User.ts으로 구성된 객체
            // accessToken은 변수로 가져오고 ...userData는 객체로 가져옴
            const { accessToken, ...userData } = response.data;

            // localStorage에는 문자열만 들어갈 수 있음
            // 전개 연산자로 변수로 가져온 accessToken은 바로 넣을 수 있음
            localStorage.setItem("accessToken", accessToken);

            console.log('로그인 성공 사용자 : ' + userData);

            // 함수를 조건식에 넣는 것은 존재 유무를 판별하려고
            // (프롭스로 진짜 받아온 함수인가정도를 판단함)
            if (onLogin) {
                onLogin(userData);

                // userData는 자바스크립트 객체여서 문자열로 바꿔줘야 함
                // JSON.stringify 함수는 JavaScript 객체를 JSON 문자열로 변환해 줍니다.
                localStorage.setItem("user", JSON.stringify(userData));
            }

            // 로그인이 되면 메인 홈페이지로 이동시킴
            navigate("/");

        } catch (error: any) {
            if (error.response) { // 서버가 에러 응답을 보냈을때
                // 백엔드에서 작성한 에러 메시지
                setErrors(error.response.data.message || "로그인 실패");
            } else { // 서버가 에러 응답을 안보냈을때 - 네트워크 문제
                setErrors("Server Error");
            }
        }
    };

    console.log('자바스크립트 코딩 영역');

    return (
        <Container fluid className="d-flex justify-content-center align-items-center" style={{ height: "70vh" }}>
            <Row className="w-100 justify-content-center">
                <Col md={6} sm={10}>
                    <Card>
                        <Card.Body>
                            <h2 className="text-center mb-4">로그인</h2>

                            {errors && <Alert variant="danger">{errors}</Alert>}

                            <Form onSubmit={handleLogin}>
                                <Form.Group as={Row} className="mb-3 align-items-center">
                                    <Form.Label column sm={3} className="text-end fw-bold text-primary">
                                        이메일
                                    </Form.Label>
                                    <Col sm={9}>
                                        <Form.Control
                                            type="email"
                                            placeholder="이메일을 입력해 주세요."
                                            value={email}
                                            onChange={(e) => setEmail(e.target.value)}
                                            required
                                        />
                                    </Col>
                                </Form.Group>

                                <Form.Group as={Row} className="mb-3 align-items-center">
                                    <Form.Label column sm={3} className="text-end fw-bold text-primary">
                                        비밀 번호
                                    </Form.Label>
                                    <Col sm={9}>
                                        <Form.Control
                                            type="password"
                                            placeholder="비밀 번호을 입력해 주세요."
                                            value={password}
                                            onChange={(e) => setPassword(e.target.value)}
                                            required
                                        />
                                    </Col>
                                </Form.Group>

                                <Row className="g-2">
                                    <Col xs={8}>
                                        <Button variant="primary" type="submit" className="w-100">
                                            로그인
                                        </Button>
                                    </Col>
                                    <Col xs={4}>
                                        <Link to="/member/signup" className="btn btn-outline-secondary w-100">
                                            회원 가입
                                        </Link>
                                    </Col>
                                </Row>
                            </Form>

                        </Card.Body>
                    </Card>
                </Col>
            </Row>
        </Container>
    );
};

export default App;
```



#### \# AppRoutes.tsx (리액트) (04.회원.txt)
(src - routes - AppRoutes.tsx)

- 코드 추가 (전체 코드)
```typescript
import { Route, Routes } from "react-router-dom";

import FruitOne from './../pages/FruitOne';
import FruitList from './../pages/FruitList';

import HomePage from './../pages/HomePage';

import SignupPage from './../pages/SignupPage';
import LoginPage from './../pages/LoginPage';

import type { User } from "../types/User";
```

interface AppProps { // App.tsx에서 온 프롭스 - LoginPage.tsx에 전달만 함
```typescript
  user: User | null ; // 지금 당장은 user 프롭스가 필요하지 않음
  handleLoginSuccess : (userData: User) => void ;
}

function App({ user, handleLoginSuccess }: AppProps) {
  return (
    <Routes>
      <Route path="/fruit" element={<FruitOne />} />
      <Route path="/fruit/list" element={<FruitList />} />

      <Route path="/" element={<HomePage />} />

      <Route path='/member/signup' element={<SignupPage />} />
      <Route path='/member/login' element={<LoginPage onLogin={handleLoginSuccess} />} />
    </Routes>
  );
}

export default App;
```



#### \# 메뉴 목록 구성 : MenuItems.tsx (리액트) (04.회원.txt)
(src - ui - MenuItems.tsx)

주요 변경 사항
	user, handleLogout 프롭스 추가됨
	renderMenu 함수 추가

- 코드 작성 : MenuItems01.txt 파일 참조
```typescript
// 리액트에서 사용하는 상단 영역의 메뉴 정보를 저장해 놓은 파일
import { NavDropdown, Navbar, Container, Nav } from "react-bootstrap";

import { useNavigate } from "react-router-dom";
import type { User } from "../types/User";

/*
```
- 부모에서 1개의 props를 자식에게 주면
자식은 2개의 행동을 해야 함
-\> 1) 받은 프롭스의 type 작성 / 2) 매개변수에 해당 프롭스 추가 및 type 지정
```typescript
*/

// 1) 받은 프롭스의 type 작성
// App.tsx에서 받은 프롭스를 해당 컴포넌트에서 다시 타입 정의
type MenuItemsProps = {
   appName: string;
   user: User | null; // 이 데이터는 null일 수도 있습니다.
   handleLogout: (event: React.MouseEvent<HTMLElement>) => void; // App.tsx에서 받아옴
};

// 2) 매개변수에 해당 프롭스 추가 및 type 지정
// 원래 프롭스에서 프롭을 꺼낼때는 {}을 사용함
// 매개변수에 넣어서 해당 함수 안에는 원래 변수처럼 {}없이 사용하게 하기
// 해당 매개변수의 타입이 해당 컴포넌트에서 정의한 타입을 이용해서 다시 정의 함
function App({ appName, user, handleLogout }: MenuItemsProps) {
   console.log('appName 프롭스 : ' + appName);
   const navigate = useNavigate();

   // user 프롭스를 사용하여 상단에 보이는 풀다운 메뉴를 적절히 분기 처리합니다.
   // App.tsx에서 받은 프롭스인 user에 들어있는 role을 이용 (LoginPage.tsx에서 얻은 데이터)
   // 원래 switch-case문은 break가 있을때까지 쭉 진행하지만 여기서는 return이 이 역할을 대신함
   const renderMenu = () => {
      switch (user?.role) {
         case 'ADMIN':
            return (
               <>
                  <Nav.Link onClick={() => navigate(`/product/insert`)}>상품 등록</Nav.Link>
                  {/* 관리자는 모든 사람의 주문 내역 확인 */}
                  <Nav.Link onClick={() => navigate(`/order/list`)}>주문 내역</Nav.Link>
                  <Nav.Link onClick={handleLogout}>로그 아웃</Nav.Link>
               </>
            );
         case 'USER':
            return (
               <>
                  <Nav.Link onClick={() => navigate(`/cart/list`)}>장바구니</Nav.Link>
                  <Nav.Link onClick={() => navigate(`/order/list`)}>주문 내역</Nav.Link>
                  <Nav.Link onClick={handleLogout}>로그 아웃</Nav.Link>
               </>
            );
         default:
            return (
               <>
                  <Nav.Link onClick={() => navigate(`/member/login`)}>로그인</Nav.Link>
                  <Nav.Link onClick={() => navigate(`/member/signup`)}>회원 가입</Nav.Link>
               </>
            );
      }
   };

   return (
      <Navbar bg="dark" variant="dark" expand="lg">
         <Container>
            {/* 매개변수로 받은 프롭 사용하기 */}
            <Navbar.Brand href='/'>{appName}</Navbar.Brand>
            <Nav className="me-auto">

               {renderMenu()}

               <NavDropdown title={`기본 연습`}>
                  <NavDropdown.Item onClick={() => navigate(`/fruit`)}>과일 1개</NavDropdown.Item>
                  <NavDropdown.Item onClick={() => navigate(`/fruit/list`)}>과일 목록</NavDropdown.Item>
               </NavDropdown>
            </Nav>
         </Container>
      </Navbar >
   );
}

export default App;
```




#### \# 앱 메인 파일 : src/App.tsx (리액트 종료) (04.회원.txt)
- 코드 작성 : App02.txt 파일 참조
(리액트 부분 완성)
```typescript
import { useEffect, useState } from 'react';
import './App.css';

// 외부 컴포넌트 import하기
// import 컴포넌트이름 from '경로와 파일명';
import { useNavigate } from 'react-router-dom';
import AppRoutes from './routes/AppRoutes';
import type { User } from './types/User';
import MenuItems from './ui/MenuItems';

function App() {
  const appName = "IT Academy Coffee Shop";

  // 로그인 안한 상태 : User는 null
  // 로그인 한 상태 : User는 값이 있음
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => { // 사이트가 처음 켜지거나 새로고침 했을때 setUser 관리
    // 로컬스토리지에 보관된 'user'정보를 가져옴
    const loginUser = localStorage.getItem('user');
    if (typeof loginUser === 'string') {
      // 로컬스토리지에 담긴 문자열인 'user'인 loginUser를 자바스크립트 객체{ } 형태로 형식으로 바꿈
      // key: value 형태
      const parsed = JSON.parse(loginUser);
      setUser(parsed);
    }
  }, []);

  const handleLoginSuccess = (userData: User) => { // LoginPage를 통해 로그인했을때 setUser 관리
    setUser(userData);
    localStorage.setItem('user', JSON.stringify(userData));
    console.log('로그인 성공');
  }

  const navigate = useNavigate();

  // 로그인한 사용자가 '로그 아웃' 버튼을 클릭했습니다.
  const handleLogout = (event: React.MouseEvent<HTMLElement>) => {
    event.preventDefault();
    setUser(null);
    localStorage.removeItem('user');
	localStorage.removeItem('accessToken');
    console.log('로그 아웃 성공');
    // 로그아웃시 이동할 페이지 설정
    navigate(`/member/login`);
  };

  return (
    <>
      {/* App.tsx의 appName변수를 MenuItems에 appName라는 변수명으로 프롭스로 주기 */}
      <MenuItems appName={appName} user={user} handleLogout={handleLogout} />

      {/* 분리된 라우터 정보 */}
      {/* handleLoginSuccess는 로그인 성공 후 사용자 상태를 갱신하는 함수 */}
      <AppRoutes user={user} handleLoginSuccess={handleLoginSuccess} />

      <footer className="bg-dark text-light text-center py-3 mt-5">
        <p>&copy; 2025 {appName}. All rights reserved.</p>
      </footer>
    </>
  );
}

export default App;
```




#### \# 직렬화 문제 해결 (스프링 시작) (04.회원.txt)
네트워크를 통해 데이터를 보낼때 자바 객체 상자인  { }로는 못보내고
한 줄짜리 문자열(JSON)으로 만들어서 보내는데 이게 직렬화임
스프링부트에는 Jackson이라는 라이브러리를 이용해서 처리하는데
LocalDate나 LocalDateTime같은 데이터 타입은 복잡하게 되어있어서
직렬화 규칙을 몰라서 에러가 발생함
-\> 따라서 규칙(패턴)을 알려줘야함

1\. pom.xml (의존성 추가)
jackson 라이브러리한테 규격을 알려줌
```xml
<dependency>
   <groupId>com.fasterxml.jackson.datatype</groupId>
   <artifactId>jackson-datatype-jsr310</artifactId>
</dependency>
```

2\. 엔터티(회원)(entity - Member에 추가)
의존성만 추가해도 에러는 안나지만 더 이쁘게 보이기 위해 규격을 추가함
```java
private LocalDate regdate ; // 등록 일자
```
이 구문 위에
```java
@JsonFormat(pattern = "yyyy-MM-dd")
```
이 구문 추가



#### \# pom.xml / jwt와 관련된 의존성을 3개 추가 (스프링 시작) (04.회원.txt)
- 코드 작성
```xml
<!-- JWT API -->
<dependency>
	<groupId>io.jsonwebtoken</groupId>
	<artifactId>jjwt-api</artifactId>
	<version>0.11.5</version>
</dependency>

<!-- JWT 구현체 -->
<dependency>
	<groupId>io.jsonwebtoken</groupId>
	<artifactId>jjwt-impl</artifactId>
	<version>0.11.5</version>
	<scope>runtime</scope>
</dependency>

<!-- JSON 처리 (Jackson 연동) -->
<dependency>
	<groupId>io.jsonwebtoken</groupId>
	<artifactId>jjwt-jackson</artifactId>
	<version>0.11.5</version>
	<scope>runtime</scope>
</dependency>
```



#### \# Bean 객체
- 같은 의미의 다른 표현
dto (Data Transfer Object) / vo (Value Object)


#### \# LoginDto 클래스 신규 작성  (스프링 시작) (04.회원.txt)
클라이언트에서 온 로그인 데이터를 담는 전용 클래스입니다.
(com.coffee - dto폴더 생성 후 - LoginDto 클래스 생성 후 작성)

(코드 작성)
```java
package com.coffee.dto;

import lombok.Getter;
import lombok.Setter;

// dto(Data Transfer Object)
// 클라이언트에서 넘겨진 로그인 정보를 저장하기 위한 자바 클래스
@Getter @Setter
public class LoginDto {
    private String email ;
    private String password ;
}
```



#### \# Claims 인터페이스 (JWT(이론)(P.15))
JWT 안에 담기는 사용자 정보(누가 주인, 어떤 권한)의 데이터 조각을 의미
JWT 안에 들어 있는 토큰 속 정보 상자(Key-Value 모음)를 Claims(클레임)
이 사용자가 누구냐 이 사용자가 어디까지 할 수 있는지

- Registered Claims (참고정도)
iss 토큰 발급자(Issuer)
sub 토큰 주제(Subject, 보통 사용자 ID)
aud 토큰 대상자(Audience)
exp 만료 시간(Expiration)
iat 발급 시간(Issued At)
nbf 유효 시작 시간(Not Before)



#### \# 토큰 관리 클래스 신규 작성 : JwtTokenProvider(config 패키지)  (스프링) (04.회원.txt)
(config 폴더에 JwtTokenProvider 클래스 생성)
JWT를 생성하고, 해석하고, 검증하는 기능을 합니다.
JWT 생성, 검증 기능 담당자 클래스
- getSigningKey() 메소드 : 위조 방지를 위한 서명
- createToken(Member member) 메소드 : JWT 생성
- getClaims(String token) 메소드 : 토큰을 사용하여 Claims 정보 추출
- getEmail(String token) 메소드 : 토큰에서 email 추출
- public boolean validateToken(String token) : 토큰 유효성 검사

(코드)
```java
package com.coffee.config;

import com.coffee.entity.Member;
import io.jsonwebtoken.*;
import io.jsonwebtoken.security.Keys;
import org.springframework.stereotype.Component;

import java.security.Key;
import java.util.Date;
import java.util.Map;

@Component // bean 객체를 만들어서 관리 - 나중에 컨트롤러에서 편하게 불러다 쓸 수 있음
public class JwtTokenProvider { // JWT 생성, 검증 기능 담당자 클래스
    // 토큰을 위조하지 못하도록 도장을 찍을 때 사용할 백엔드만의 비밀번호(비밀키)
    // 노출시 해커가 마음대로 토큰 위조 가능
    // 실무에서는 application.properties에 숨겨둠 (나중에 @Value로 설정해서 가져오기)
    private final String SECRET_KEY =
            "my-secret-key-my-secret-key-my-secret-key";

    // 우리가 지정한 문자열 SECRET_KEY를 JWT 라이브러리가 서명용 도장으로 인식할 수 있도록
    // 컴퓨터용 암호화 키 객체로 다듬어서 반환해 주는 내부 헬퍼 메서드
    private Key getSigningKey(){ // 위조 방지를 위한 서명
        return Keys.hmacShaKeyFor(SECRET_KEY.getBytes());
    }

    // 토큰 유효 기간 설정 (밀리초(ms) 단위)
    private final long EXPIRATION = 1000 * 60 * 60 ; // 만료 1 시간

    // 1. 토큰(JWT) 생성 : createToken(Member member) 메소드
    // 회원 정보를 가지고 그에 해당하는 토큰 생성
    // MemberController 클래스에서 인증 성공한 사용자를 위하여 로그인 증명서(토큰)를 발급하는 데 사용될 예정입니다.
    public String createToken(Member member){ // 매개 변수 : 토큰 안에 사용자 식별값 저장
        return Jwts.builder()
                .setSubject(member.getEmail()) // 토큰 주인 - sub 토큰 주제(Subject, 보통 사용자 ID)
                .setIssuedAt(new Date()) // 토큰 발급 시간 - iat 발급 시간(Issued At)
                .setExpiration(new Date(System.currentTimeMillis() + EXPIRATION)) // 토큰 만료 시간 - exp 만료 시간(Expiration)
                // 비밀키 도장(getSigningKey())과 HS256이라는 암호화 알고리즘을 사용해서 토큰 맨 뒤에 절대 위조할 수 없는 전자 서명(Sign)을 각인
                .signWith(getSigningKey(), SignatureAlgorithm.HS256)
                // 표준 클레임 말고 우리가 커스텀하게 넣고 싶은 정보(예: "role": "USER")를 Map 형태로 추가 주입
                .setClaims(Map.of("role", member.getRole().name())) // 권한 정보
                // 이 모든 정보를 압축하여 점(.) 두 개로 연결된 그 유명한 JWT 긴 문자열(eyJhbGci...)을 완성
                .compact(); // 최종 문자열 생성하기
    }

    // 2. 토큰 해체 및 정보 추출
    // 외부에서 토큰을 주면, 그 토큰을 해체해서 안에 들어있던 주인공 이메일(Subject)만 쏙 뽑아서 돌려주는 편의 메서드
    public String getEmail(String token){ // JWT 토큰에서 사용자 정보 가져 오기
        return this.getClaims(token).getSubject() ; // .setSubject(member.getEmail())
    }
    // 토큰 해체 분석기
    public Claims getClaims(String token){
        return Jwts.parserBuilder()
                .setSigningKey(getSigningKey())
                .build()
                .parseClaimsJws(token)
                .getBody();
    }

    // 3. 출입증 위조/만료 검사
    // 들어온 토큰을 우리 비밀키로 시험 삼아 파싱(해체)해 보는 검문소
    // 온전하게 해체가 잘 되면 법적으로 유효한 토큰이므로 true를 뱉고 통과
    public boolean validateToken(String token){ // JWT 토큰 유효성 검사
        try {
            Jwts.parserBuilder()
                    .setSigningKey(getSigningKey())
                    .build()
                    .parseClaimsJws(token);
            return true; // 아무 문제 없으면 정상적인 토큰이므로 true 반환!

        } catch (ExpiredJwtException e) { // 발급된 지 1시간이 넘어서 유통기한이 지난 토큰일 때
            System.out.println("토큰 만료됨");

        // 해커가 글자를 임의로 바꿨거나 서명이 일치하지 않는 가짜 위조 토큰일 때
        } catch (io.jsonwebtoken.security.SecurityException | MalformedJwtException e) {
            System.out.println("토큰 서명/형식 오류");

        } catch (Exception e) { // 그외 예외 사항
            System.out.println("기타 토큰 오류");
        }
        return false ;
    }
}
```


#### \# String 클래스 공부 (스프링) (04.회원.txt)
(src - main - java - com.coffee - test폴더에 StringTest 클래스 생성)
- 코드 작성
```java
package com.coffee.test;

/*startsWith(), endsWith(), substring(), length(), toLowerCase()
```
toUpperCase(), lastIndexOf(), replace(), contains()
```java
        String.format("%02d", count);*/

public class StringTest {
    public static void main(String[] args) {
        String sample = "Bearer hello world" ;

        String result ;
        // IT에서 Case는 무조건 대소문자와 연관된 것
        // String인 sample의 데이터 값을 소문자로 만들기
        result = sample.toLowerCase() ;
        System.out.println("소문자 : " + result);

        // String인 sample의 데이터 값을 대문자로 만들기
        result = sample.toUpperCase() ;
        System.out.println("대문자 : " + result);
```

        // String인 sample의 데이터 값에서 특정 문자가 들어가있는지 확인하기
        // 어떠한 문장이 들어가있으면 ~~하시오 같이 나중에 if나 다중if문장에서 활용
        boolean bool = sample.contains("hello");
        System.out.println("hello 존재 여부 : " + bool);

        // String인 sample의 데이터 값이 특정 문자로 시작하는지 확인하기
        // if문장에 조건식에서 활용
        bool = sample.startsWith("hello");
        System.out.println("hello로 시작 여부 : " + bool);

        // String인 sample의 데이터 값이 특정 문자로 끝나는지 확인하기
        // if문장에 조건식에서 활용
        bool = sample.endsWith("world");
        System.out.println("world로 끝이 납니까? : " + bool);

        // String인 데이터 그 자체를 가지고 길이를 측정하기
        int size = "Bearer ".length() ;
        System.out.println("문자열 길이 : " + size);

        // String은 타입이기도 하지만 기본으로 제공되는 클래스이기도 함
        // format() 메소드는 static메소드여서 객체없이 바로 사용 가능
        result = String.format("%03d", size);
        System.out.println("서식 지정 : " + result);

        // String인 sample의 데이터 값에서 특정 인덱스부분부터 추출하기
        // 전체 긴 문자열에서 일부분을 가져올때 (데이터 분석시)
        result = sample.substring(7);
        System.out.println("추출 결과 01 : " + result);

        // String인 sample의 데이터 값에서 특정 인덱스부분부터 추출하기 (변수 이용)
        // 전체 긴 문자열에서 일부분을 가져올때 (데이터 분석시)
        result = sample.substring(size);
        System.out.println("추출 결과 01-1 : " + result);

        // String인 sample의 데이터 값에서 특정 인덱스부분부터 특정 인덱스부분까지 추출하기
        // 전체 긴 문자열에서 일부분을 가져올때 (데이터 분석시)
        // Java에서 숫자가 2개가 나오면 앞에 숫자는 포함되지만 뒤에 숫자는 포함안됨
        // "hello"에서 h의 인덱스가 7인데 앞에꺼는 포함됨 -\> 따라서 7을 써줘야 함
        // "hello"에서 o의 인덱스가 11인데 뒤에꺼 포함안됨 -\> 따라서 12를 써줘야 함
        result = sample.substring(7, 12);
        System.out.println("추출 결과 02 : " + result);

        // String인 result의 데이터 값에서 특정 문자열을 다른 문자열로 대체하기
        result = sample.replace("hello", "bluesky");
        System.out.println("치환 : " + result);
    }
}



#### \# JWT 필터 클래스 신규 작성 : JwtAuthenticationFilter (스프링) (04.회원.txt)
(config - JwtAuthenticationFilter 클래스 생성)
- 코드 작성
```java
package com.coffee.config;

import io.jsonwebtoken.Claims;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;
import java.util.List;

// 컨트롤러마다 매번 로그인 확인할 필요없이 컨트롤러 전에 공통적으로 로그인 확인하는 자동화 시스템
public class JwtAuthenticationFilter extends OncePerRequestFilter {
    // 아직 무의미한 null값임 - 값을 주입해야함
    // 사용할 도구 가져오기 (마치 Repository와 Service의 관계)
    private final JwtTokenProvider jwtTokenProvider ;

    // 값을 주입함 (@RequiredArgsConstructor 이 어노테이션으로 해결해도 됨)
    public JwtAuthenticationFilter(JwtTokenProvider jwtTokenProvider){
        this.jwtTokenProvider = jwtTokenProvider;
    }

    @Override // 모든 요청이 들어올 때 컨트롤러 보다 먼저 (한번만!) 실행이 되는 핵심 로직(메소드)
    protected void doFilterInternal(
            HttpServletRequest request, // 프론트가 들고 온 요청 정보
            HttpServletResponse response, // 프론트에게 돌려줄 응답 정보
            // 검문소 다음 단계로 이어지는 고속도로 통로 (다음 필터들)
            FilterChain filterChain) throws ServletException, IOException {

        // 1단계: 가방 뒤지기 (Authorization 헤더 확인)
        // 프론트가 들고온 요청 헤더에서 Authorization 값을 가져온다
        String bearer = request.getHeader("Authorization");
        // 값이 존재하고 "Bearer "로 시작하는지 확인한다
        if(bearer != null && bearer.startsWith("Bearer ")){
            // Bearer "를 제거하여 JWT 토큰만 추출한다
            String token = bearer.substring("Bearer ".length());

            // 2단계: 출입증 진위 여부 및 신원 파악
            // 토큰의 유효성을 검증한다 (validateToken) (만료여부, 위조여부)
            if(jwtTokenProvider.validateToken(token)){
                // 토큰에서 사용자 이메일을 추출한다 (getEmail)
                String email = jwtTokenProvider.getEmail(token); // 회원의 이메일 정보 가져오기
                Claims claims = jwtTokenProvider.getClaims(token); // 토큰 해체해서 객체에 넣기

                // 토큰의 claims에서 role 값을 추출한다
                String role = claims.get("role", String.class);

                // 3단계: 시큐리티 전용 통행증 발급 및 보고 (★보안의 핵심)
                // 권한 객체 생성 (권한을 담고 있는 객체 모음)
                // 인터페이스라서 객체 생성 불가능 - 구현체를 이용해서 객체를 생성해야 함
                // SimpleGrantedAuthority라는 구현체를 이용함
                // 스프링 시큐리티는 문자열 데이터 그대로를 인식 못해서
                // 이해할 수 있는 양식인 GrantedAuthority로 변환해줌
                List<GrantedAuthority> authorities
                        = List.of(new SimpleGrantedAuthority("ROLE_" + role));
```

                // 인증 객체 생성 (인증 객체 auth 발행)
                UsernamePasswordAuthenticationToken auth
                        // 비밀번호 자리는 토큰으로 대체해서 null로 표시함
                        = new UsernamePasswordAuthenticationToken(email, null,
                        authorities);

                // SecurityContextHolder : 스프링 시큐리티에 인증 객체인 auth를 넣어두면
                // 스프링 시큐리티가 이 요청을 보낸 사람이 로그인이 완벽히 된 사람이라고 인식함
				// Authentication가 SecurityContext안에 있고 이것을 SecurityContextHolder가 유지보수 및 관리를 해줌
                SecurityContextHolder.getContext().setAuthentication(auth);

            }
        }

        // 검문 종료: 고속도로 개통 -\> 컨트롤러로 패스시킴
        // 출입증이 없는 비로그인 유저라도 컨트롤러로 패스시킴
        filterChain.doFilter(request, response);
    }
}



#### \# WebConfig 클래스 (04.회원.txt)
addCorsMappings : 기존 Cors 설정을 위하여 오버라이딩한 메소드 주석 처리하기
(CorsConfig 파일에 따로 설정 할 예정)

- 주석 처리
```java
/*@Override
public void addCorsMappings(CorsRegistry registry) {
	// 3000번 포트에서 GET부터 PATCH까지의 열거한 요청들을 모두 수락하겠습니다.
	registry.addMapping("/**") *//* 모든 경로 허용  *//*
			.allowedOrigins("http://localhost:5173", "http://localhost:3000") *//* react 포트 *//*
			.allowedMethods("GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH")  *//* 허용할 메소드 *//*
			.allowCredentials(true) ; // 쿠키 전송 허용
}*/
```



#### \# config\CorsConfig 클래스 신규 작성 (04.회원.txt)
(config - CorsConfig 클래스 생성)
CORS 정책을 정의하고 있는 클래스 파일
- 코드 작성
```java
package com.coffee.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.CorsConfigurationSource;
import org.springframework.web.cors.UrlBasedCorsConfigurationSource;

import java.util.List;

@Configuration // 설정 파일임을 의미
public class CorsConfig {
    // 객체임을 의미
    @Bean // Spring Security가 이 이름으로 된 Bean을 읽으면 자동으로 CORS 정책으로 사용함
    public CorsConfigurationSource corsConfigurationSource(){
        // configuration 객체는 클라이언트로부터 요청이 들어 왔을 때 CORS 정책을 적용시켜주는 객체
        // 구체적인 CORS 허용 기준(출처, 메서드, 헤더 등)을 조율하고 담아둘 설정 바구니 객체
        CorsConfiguration configuration = new CorsConfiguration();

        // 리액트의 포트 번호를 여기에 작성
        configuration.setAllowedOrigins(List.of(
                "http://localhost:5173",
                "http://127.0.0.1:5173"
        ));

        // 허용 HTTP 메소드
        // 조회(GET), 등록(POST), 수정(PUT, PATCH), 삭제(DELETE), 예비 요청(OPTIONS)
        configuration.setAllowedMethods(List.of(
                "GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"
        ));
```

        // Authorization은 axiosInstance.tsx 파일 참조
        // Content-Type은 LoginPage.tsx 파일 참조
        // 프론트가 요청보낼때 헤더에 담아 보낼 키 값들을 허용
        configuration.setAllowedHeaders(List.of(
                "Authorization", // JWT 토큰을 담아 보낼 헤더
                "Content-Type", // MIME 타입 / JSON 형태로 보낼 때(application/json)
                "Accept" // 백엔드로부터 어떤 응답 데이터 포맷을 받기를 원하는지 명시할 때 쓰임
        ));

        // 쿠키 Authorization 헤더 포함 요청 허용
        // 프론트엔드에서 axios나 fetch를 쓸 때 인증 정보(withCredentials)를 실어 보내도
        // 서버가 거부하지 않고 정상 처리
        configuration.setAllowCredentials(true);

        // CorsConfigurationSource가 인터페이스여서 객체 생성 못함
        // 그래서 구현체를 만들어서 객체 생성함
        UrlBasedCorsConfigurationSource source
                = new UrlBasedCorsConfigurationSource();

```typescript
        // 설정 객체인 configuration을 구현체로 생성한 객체인 source에 할당함
        // 모든 요청에 똑같이 위의 설정값들을 적용함 (**의 의미)
        // 만든 정책 바구니(configuration)를 어떤 URL 주소에 적용할지 연결(등록)하는 과정
        // 백엔드 서버로 들어오는 모든 경로의 모든 요청
        source.registerCorsConfiguration("/**", configuration);

        /* 어떤 요청에는 어떤 설정값을 적용할지 상세히 나눌 수도 있음
        source.registerCorsConfiguration("/member/**", memberConfig);
        source.registerCorsConfiguration("/product/**", productConfig);
        source.registerCorsConfiguration("/cart/**", cartConfig);
        */

        // 구현체를 리턴함 (모든 설정과 URL 매핑이 완료된 source 객체를 반환)
        // 반환된 객체가 스프링 컨테이너에 빈(Bean)으로 등록되어 CORS 설정으로 사용됨
        return source ;
    }
}
```



#### \# MemberDetailsService (스프링) (04.회원.txt)
(service - MemberDetailsService 클래스 생성)
UserDetailsService를 상속 받는 MemberDetailsService 구현체 클래스를 작성
직접 호출하는 코드가 아니라, Spring Security에 의하여 로그인 시 자동 실행이 되는 핵심 인증 로직

즉, MemberController의 login() 메소드의 UsernamePasswordAuthenticationToken에 의하여
내부적으로 loadUserByUsername(email)를 자동 호출

로그인 요청 → Spring Security → MemberDetailsService 실행

- 코드 작성
```java
package com.coffee.service;

import com.coffee.entity.Member;
import com.coffee.repository.MemberRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

@Service // 클래스는 서비스 목적으로 사용된다.
@RequiredArgsConstructor
// 스프링 시큐리티에게 "로그인할 때 DB에서 유저 정보 찾는 로직은 내가 커스텀하게 만든 이 클래스를 사용해 줘!"라고 선언
public class MemberDetailsService implements UserDetailsService {
    private final MemberRepository memberRepository ;

    @Override // 사용자가 로그인할때 스프링 시큐리티가 인증 처리를 시작하면서 이 메소드를 자동으로 호출합니다.
    public UserDetails loadUserByUsername(String email) throws UsernameNotFoundException {
        Member member = memberRepository.findByEmail(email) ;

        if(member == null){
            String message = "이메일이 " + email + "인 회원은 존재하지 않습니다.";

            // 존재하지 않는 회원이니까 예외를 발생시켜야함(일으켜야함)
            // 자바에서 사용자가 예외를 발생시키고자 하는 경우에는 throw 키워드를 사용합니다.
            throw new UsernameNotFoundException(message); // 객체임

        }else{
            // 나중에 디버깅할때 어디서 나왔는지 알려고 메소드명을 적음
            System.out.println("loadUserByUsername() 메소드");
            System.out.println(member);
        }
        // User는 UserDetails(인터페이스-구현체필요)와 상속관계여서 구현체로 사용함
        // DB에서 꺼내온 진짜 알맹이 데이터들(Member)을 시큐리티 표준 박스(User)의 칸막이에 맞춰서 이사시키는 작업
        // DB에 저장된 정보를 가진 User 객체를 시큐리티 엔진에게 보내면 시큐리티가 알아서
        // DB에 있는 암호화된 비밀번호와 사용자가 방금 로그인 창에 입력한 비밀번호와 비교해서
        // 최종 로그인을 통과시키거나 거부하게 됨
        return User.builder()
                .username(member.getEmail())
                .password(member.getPassword())
                .roles(member.getRole().name())
                .build();
    }
}
```



#### \# SecurityConfig.java 파일 수정 (04.회원.txt)
JWT로 변환하기

기존 파일 다 삭제 후
SecurityConfig03.txt 파일 복붙

- 코드 작성
```java
package com.coffee.config;

import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.annotation.authentication.configuration.AuthenticationConfiguration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;
import org.springframework.web.cors.CorsConfigurationSource;

@Configuration // 설정용 파일 어노테이션
@RequiredArgsConstructor
public class SecurityConfig {

    // JwtTokenProvider.java에서 @Component로 생성함
    // 토큰 검독기
    private final JwtTokenProvider jwtTokenProvider;

    // CorsConfig.java에 CorsConfigurationSource의 @Bean으로 객체 생성이 되어 있음
    // 리액트(5173 포트)의 접근을 허락해 줄 교차 출입 허가증 정보
    private final CorsConfigurationSource corsConfigurationSource;

    @Bean // 비밀번호를 암호화하는 메소드 (BCrypt 방식)
    // "admin@naver.com"을 DB에 "$2a$10$JvA36EqRtX4EHtsv42wUXeO6ma9OpdvxO7sZ6rhufqMbTgkclmacW"로 저장함
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    // 스프링 컨테이너가 관리하는 객체로 설정하는 어노테이션 (Java의 객체를 부르는 이름이 Bean임)
    // 이 어노테이션이 붙으면 그 메소드의 결과물인 반환데이터를 객체화 시켜서
    // 스프링 빈(Spring Bean)이라는 이름으로 스프링 컨테이너에 넣고 관리함
    // 원래 일반적으로 객체를 사용할때는 new연산자를 사용해서 매번 새로 만들지만 이렇게 객체화 시켜서 컨테이너에 저장해놓으면
    // 나중에 해당 객체가 필요할때 새로 생성하지 않고 스프링 컨테이네에서 꺼내다 재사용 할 수 있음
    @Bean
    // SecurityFilterChain : 스프링 시큐리티의 보안 필터들이 순서대로 늘어선 체인(사슬)" 그 자체를 의미하는 인터페이스
    // HttpSecurity : SecurityFilterChain의 필터를 조립하는 도구함
    // throws : 예외 전이 선언문 - 호출한 상위 메서드가 알아서 처리하게 하기 <-> try-catch는 내가 직접 예외사항 처리하기
    // Exception은 모든 예외 상황을 포함하는 최상위 클래스라서 throws Exception은 아주 포괄적인 선언문임
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {

        // 인증 없이 요청을 허용할 url 배열 (배열 생성 초기화 기법)
        String[] permitUrls = {
                "/images/**",
                "/fruit/**",
                "/css/**",
                "/js/**",
                "/member/signup",
                "/member/login",
                "/product/list"
        };

        // Spring Security 기본 정책 : POST / PUT / DELETE 요청은 CSRF 토큰 필요함
        http    // CorsConfig에 설정해놓은 반환값인 source를 사용해서 CORS 설정함
                // 주입받은 교차 허가증(corsConfigurationSource)을 시큐리티 시스템에 주입
                .cors(cors -> cors.configurationSource(corsConfigurationSource))
                // 사이트 간 요청 위조(CSRF) 방지 기능을 일단 비활성화 시켜 두고 -> (.csrf(csrf -> csrf.disable()))
                // 나중에 JWT를 사용해서 CSRF를 끄고 키고 할 수 있음
                .csrf(csrf -> csrf.disable())
                // 세션(Session)이라는 메모리 카드를 절대 쓰지 않는 STATELESS(무상태) 방식을 채택
                // -> 세션말고 오직 토큰만 검사 (JWT 보안의 핵심 정책!)
                .sessionManagement(session ->
                        session.sessionCreationPolicy(SessionCreationPolicy.STATELESS)
                )
                // 요청에 대한 권한 설정 (인가)
                // .authorizeHttpRequests(auth -> auth ...) : 어떤 주소로 들어오는 요청을 허용하거나 막을지 정하는 구역
                .authorizeHttpRequests(auth -> auth
                        // permitUrls 배열에 담긴 주소들은 누구에게나(Permit All) 허용함
                        .requestMatchers(permitUrls).permitAll()
                        // 그 외의 나머지 모든 요청(anyRequest)은 반드시 로그인(authenticated)을 해야만 볼 수 있게 막음
                        .anyRequest().authenticated()
                );

        // JWT 필터 등록 (JwtAuthenticationFilter에 생성되어있음)
        // 내가 만든 JWT 필터로 검사하기
        http.addFilterBefore(
                new JwtAuthenticationFilter(jwtTokenProvider),
                UsernamePasswordAuthenticationFilter.class
        );

        // http에 넣은 모든 설정(CORS 허용, CSRF 비활성화, 세션 안 쓰기, 하이패스 주소 지정, JWT 경비원 배치 등)을
        // 하나의 거대한 사슬 객체(SecurityFilterChain)로 완성해 반환함
        return http.build();
    }

    @Bean
    // 로그인 처리를 총괄 지휘하는 대빵 매니저 객체인 AuthenticationManager를 스프링 빈으로 등록
    // 나중에 사용자가 아이디/비번을 치고 들어왔을 때 MemberDetailsService를
    // 호출해서 진짜 로그인을 진행시키는 실무 총책임자 역할
    public AuthenticationManager authenticationManager(
            AuthenticationConfiguration config
    ) throws Exception {
        return config.getAuthenticationManager();
    }
}
// 더 이상 필요없어진 설정 (옛날 방식의 서버가 직접 로그인 창 HTML 화면을 띄워주던 방식) - 이제는 리액트가 함
/*// .formLogin(form -> form ...) : 사용자에게 보여줄 로그인 폼에 대한 설정
// 인증 리다이렉션 경로 지정:
// -> 로그인이 필요한 페이지에 권한 없는 사용자가 접근하면, 어느 주소로 보낼지(Redirect) 정하는 것
// 해당 주소로 이동시 어떤 HTML주소를 보여줄지 정하는 컨트롤러와는 다른 개념임
// 따라서 리다이렉션도하고 컨트롤러에서 "/member/login" 에 맞는 HTML도 따로 설정해줘야함
.formLogin(form -> form
        // 스프링이 제공하는 기본 로그인창 대신, 직접 만든 /member/login 주소의 화면을 로그인 페이지로 사용
        .loginPage("/member/login")
        // 로그인 페이지 자체는 로그인을 안 한 사람도 접근할 수 있어야 하므로 접근을 허용
        .permitAll()
);*/

// 이제는 해당 설정을 CorsConfig 클래스로 설정해놓아서 그걸 가져오면 됨
/*        // 다른 도메인(예: 리액트 포트 5173)에서 오는 요청을 허용하기 위한 기초 설정을 적용
// SecurityConfig의 이 설정이 없을때는 다른 오리진에서 들어오는 것을
// WebConfig의 WebMvcConfigurer가 직접 결정하는데
// 이 설정이 생기면 이제부터는 오리진 허용 여부도 SecurityConfig가 관리하고
// WebConfig의 WebMvcConfigurer는 단순히 설정된 값만 SecurityConfig에게 전달하게 됨
// * 사실상 이 코드는 WebMvcConfigurer의 내용 전체를 가져오는 것과 같음 *
// 따로 설정도 가능하지만 공백으로 두어서 WebMvcConfigurer 내용을 가져와서 사용하게 함
```
http.cors(cors -\> {});\*/

```typescript
// 위에서 build() 함
/*// 지금까지 http 도구함에 담은 모든 설정들을 빌드해서
// 실제 동작하는 보안 필터 객체(SecurityFilterChain)를 생성하여 반환
return http.build();*/
```



#### \# MemberController 수정 (04.회원.txt)
login() 메소드를 구현
- 코드 작성
```java
package com.coffee.controller;

import com.coffee.config.JwtTokenProvider;
import com.coffee.dto.LoginDto;
import com.coffee.entity.Member;
import com.coffee.service.MemberService;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.validation.BindingResult;
import org.springframework.validation.FieldError;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/member")
@RequiredArgsConstructor
public class MemberController {
    private final MemberService memberService;

    private final AuthenticationManager authenticationManager ;
    private final JwtTokenProvider jwtTokenProvider ;

    @PostMapping("/login")
    // LoginDto의 데이터를 객체에 담으려고 @RequestBody 작성
    // Long타입과 String타입을 동시에 만족하는 타입은 최상위 타입인 Object타입이여서 Object타입도 적음
    public ResponseEntity<Map<String, Object>> login(@RequestBody LoginDto dto){
        // 인증 처리
        // username, password, roles 정보를 가진 객체를 이용
        // 스프링 시큐리티가 자동으로 웹페이지에서 받아온 정보과 비교
        // username - 받아온 정보와 내가 가진 정보가 맞는지
        // password - 올바른 비밀번호를 썼는지 (이게 핵심)
        // roles - 비밀번호 확인이 되면 지정해줄 roles
        // authenticationManager.authenticate : UsernamePasswordAuthenticationToken에
        // 임시로 담은 정보를 MemberDetailsService의 User의 정보와 비교해서 비밀번호가 대응되면
        // 인증서 (authentication)를 발급해줌
        Authentication authentication = authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(// 프론트에서 가져온 로그인 정보를 담은 객체를 임시로 담음
                        dto.getEmail(),
                        dto.getPassword()
                )
        );

        // 사용자 정보 조회
        // 비밀번호 대조가 끝났으니 리액트에게 응답할 유저의 진짜 데이터 정보를 담은 회원 객체를 가져옴
        Member member = memberService.findByEmail(dto.getEmail());

        if(member == null){ // 정상적이면 null이 될 수 없지만 혹시 모르니까 검사함
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED)
                    .body(Map.of("error", "사용자 정보를 찾을 수 없습니다."));
        }else{
            // JWT 토큰 생성하기
            String token = jwtTokenProvider.createToken(member);

            // 응답 (사용자 정보 조회로 가져온 회원의 진짜 데이터 정보들을 응답함)
            return ResponseEntity.ok(Map.of("accessToken", token, "id", member.getId(),
                    "name", member.getName(), "email", member.getEmail(),
                    "role", member.getRole().toString())) ;
        }


    }

    // @Valid : Member 엔티티에 @NotBlank(공백 불가)나 @Size(글자수 제한) 같은 유효성 검사 규칙이 있다면
    // 프론트엔드에서 데이터를 보낼때 해당 규칙에 맞게 보냈는지 검사하는 어노테이션
    // BindingResult : 방금 @Valid로 검사했을때 오류가 있는지 없는지에 대한 결과를 담는 바구니
    // @RequestBody : 리액트가 보낸 JSON 데이터를 Java 형식으로 변환해서 Member 객체(변수명 bean)에 넣음
    // 따라서 리액트가 보내는 파라미터의 이름과 그걸 받는 엔티티(Member)의 맴버 변수의 이름이 동일해야 자동 매핑됨
    // Controller까지는 그대로의 데이터, 그 이후인 Service에서 암호화를 하든 말든 함
    @PostMapping("/signup")
    // ResponseEntity<?> : http 상태 코드, 헤더(부가정보), 바디(프론트가 쓸 알맹이)
    // 이 3가지를 한번에 보낼 수 있는 반환타입 (<?> 이 와일드 카드는 여러 타입의 데이터가 동시에 들어가도 상관없다는 뜻)
    // 만약에 에러코드 (ex-400)를 반환하면 리액트에서는 try로 안들어가고 바로 catch (error)로 들어감
    public ResponseEntity<?>signup(@Valid @RequestBody Member bean, BindingResult bindingResult){
        System.out.println("회원 가입 정보");
        System.out.println(bean);

        // hasErrors() : 에러가 존재하면 true를 리턴함 (SpringBoot 교안 PDF (P.146))
        if(bindingResult.hasErrors()){
            Map<String, String> errors = new HashMap<>();
            // 확장 for 사용
            // bindingResult의 getFieldErrors() 바구니에서 에러들을 FieldError 타입으로 꺼내서 Map에 넣음
            for(FieldError xx:bindingResult.getFieldErrors()){// Field:Java에서의 변수(name,password등)
                errors.put(xx.getField(), xx.getDefaultMessage());
            }
            System.out.println(errors);
            // Map 형식을 프론트에 반환함
            return new ResponseEntity<>(errors, HttpStatus.BAD_REQUEST);
        }else{
            System.out.println("ok");
        }

        // 이메일 중복 체크
        Member member = memberService.findByEmail(bean.getEmail());
        if (member != null){ // member가 null이 아니라는 것은 이미 존재하는 id(맴버)라는 것을 의미함
            // 이미 존재하는 이메일 주소
            // Map.of : Map 컬렉션의 축약버전
            // <>안에 원래 타입을 적어줘야하는데 스프링이 알아서 Map<String, String>을 뒤에 Map.of보고 추론함
            // ResponseEntity(T body, HttpStatus status) 생성자 이용
            return new ResponseEntity<>(Map.of("email", "이미 존재하는 이메일 주소입니다."),
                    HttpStatus.BAD_REQUEST);
        }

        // 회원 가입 처리
        memberService.insert(bean); // memberService에서 insert메소드를 넣어서 나머지 정보들도 넣음
        return new ResponseEntity<>("회원 가입 성공", HttpStatus.OK) ; // 회원 가입 성공 (OK라는건 200번대라는 뜻)
    }
}
```



#### \# JwtTokenProvider.java 파일 수정하기 (스프링)
중요 코드 application.properties에 숨기기

- 아래 코드를 삭제함
```java
// 이 값도 사실 노출 방지를 위하여 어딘가에 숨겨야 함
private final String SECRET_KEY =
		"my-secret-key-my-secret-key-my-secret-key";

private Key getSigningKey(){ // 위조 방지를 위한 서명
	return Keys.hmacShaKeyFor(SECRET_KEY.getBytes());
}

private final long EXPIRATION = 1000 * 60 * 60 ; // 만료 1 시간
```

- application.properties 파일에 변수로 넣기
```properties
jwt.secret=my-secret-key-my-secret-key-my-secret-key
jwt.expiration=3600000
```

- 새로운 코드로 대체



#### \# Category.java (스프링) (05.상품.txt)
(constant - Category 이름의 Enun 생성)
상품 카테고리 의미하는 열거형 타입 정의

- 코드 작성
```java
package com.coffee.constant;

// 상품의 카테고리 정보를 위한 열거형 상수
// 한글 이름도 같이 명시함
public enum Category {
    // 각각 독립된 static 객체
    // 괄호 안에 있는 내용을 생성자의 매개변수로 넣음
    // 1) ALL("전체")를 호출하면, (Category category라고 하면 그냥 선언된거임)
    // 2) 아래에 작성하신 Category(String description)라는 생성자가 실행됩니다.
    // 3) 전달된 "전체"라는 값이 this.description에 저장되는 것이죠.
    // 4) getDescription()으로 다른 곳에서도 쓸 수 있게 하기
    ALL("전체"), BREAD("빵"), BEVERAGE("음료수"), CAKE("케이크"), MACARON("마카롱") ;

    // 매개변수가 문자열이니까 String으로 지정
    // 그냥 맴버변수 만든거임
    private String description ;

    Category(String description) { // 생성자
        this.description = description;
    }

    public String getDescription() {
        return description;
    }
}
```



#### \# Product.java (스프링) (05.상품.txt)
(entity - Product 클래스 생성)
- 코드 작성
```java
package com.coffee.entity;

import com.coffee.constant.Category;
import com.fasterxml.jackson.annotation.JsonFormat;
import jakarta.persistence.*;
import jakarta.validation.constraints.*;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import java.time.LocalDate;

@Entity
@Table(name= "products")
@Getter @Setter @ToString
public class Product {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "product_id")
    private Long id; // 정수 int 보다 더 큰 타입은 Long으로 지정함

    @Column(nullable = false)
    @NotBlank(message = "상품 이름은 필수 입력 사항입니다.")
    private String name;

    @Column(nullable = false)
    // 정수형의 크기 제한
    @Min(value = 100, message = "가격은 100원이상이어야 합니다.")
    @Max(value = 10000, message = "가격은 10000원이하이어야 합니다.")
    private int price;

    @Enumerated(EnumType.STRING)
    @NotNull(message = "카테고리는 반드시 선택해야 합니다.")
    private Category category;

    @Column(nullable = false)
    @Min(value = 10, message = "재고 수량은 10개 이상이어야 합니다.")
    @Max(value = 1000, message = "재고 수량은 1000개 이하이어야 합니다.")
    private int stock ;

    @Column(nullable = false)
    @NotBlank(message = "이미지는 필수 입력 사항입니다.")
    private String image;

    @Column(nullable = false)
    @NotBlank(message = "상품 설명은 필수 입력 사항입니다.")
    // 문자열의 크기 제한
    @Size(max = 1000, message = "상품에 대한 설명은 최대 1,000 자리 이하로만 입력해 주세요.")
    private String description;

    @JsonFormat(pattern = "yyyy-MM-dd")
    private LocalDate inputdate;
}
```



#### \# 이미지 파일 복사
    c:\shop\images 폴더에 boot_images.zip 압축 해제 후 복사하도록 합니다.



#### \# FileTest.java (스프링) (05.상품.txt)
(test - FileTest 클래스 생성)
File 클래스를 사용하여 c:\shop\images 폴더의 이미지 정보를 다뤄 봅니다.

- 코드 작성
```java
package com.coffee.test;

import java.io.File;

public class FileTest {
    public static void main(String[] args) {
        // 운영체제의 폴더 구분자는 역슬래쉬 (\)
        // 역슬래쉬는 특수한 문자여서 2개를 적어야 함
        // 원래 역슬래쉬하고 n이나 다른 문자를 써서 특수한 문자를 만들어서
        // 사실상 역슬래쉬 하나는 특수한 문자를 만드는 문법이고 진짜 문자?인 역슬래쉬는 두번째 역슬래쉬

        // 리눅스의 폴더 구분자는 슬래쉬 (/)

        // 지역 변수에는 접근지정자를 붙일 수 없어서 private을 못 넣음
        final String imageFolder = "c:\\shop\\images";

        // 이미지가 들어간 파일이 들어간 폴더를 지칭하는 folder 객체
        // 지정한 경로("c:\\shop\\images")를 바탕으로 하드디스크의 해당 위치를
        // 가리키는 File 객체 상자를 만들어서 folder라는 변수에 주소를 담음
        File folder = new File(imageFolder);

        // folder의 존재 여부 조건식
        // File 클래스로 객체를 만들면 객체는 무조건 생성되는데 실제로 해당 경로에 폴더가 존재하는지는 확인해야함
        if(folder.exists()){ // 실제로 해당 경로에 폴더가 존재하는지 확인
            // is로 시작하는 메소드들의 반환타입은 대부분 boolean 타입임
            if(folder.isDirectory()){ // 해당 경로에 있는 것이 폴더면
                System.out.println("폴더");

                // 해당 경로에 있는 폴더 안에 있는 모든 파일과 하위 폴더들을 모아서 File 배열에 넣음
                File[] imageList = folder.listFiles();

                // 확장 for => for(타입 단수 : 복수){}
                for(File one : imageList){
                    if (one.isFile()){ // 내용물이 파일이면
                        // String 클래스 이용하기 (04.07(화).txt확인)
                        if (one.getName().endsWith(".jpg")){ // 내용물이 파일이고 이름이 .jpg로 끝나면
                            // 이렇게 하면 확장자도 다 출력됨
                            System.out.println(one.getName());

                            // 확장자 제거하고 파일 이름만 출력하기
                            // indexof는 특정 문자가 있는 인덱스의 위치를 알려줌
                            // int end_index = one.getName().indexOf(".") ;
                            // 만약 파일명에 "."이 있을때 마지막 "."을 없애기위해
                            // lastindexof() 사용하면 됨
                            int end_index = one.getName().lastIndexOf(".") ;
                            String filename = one.getName().substring(0, end_index) ;
                            System.out.println(filename);

                            // 확장자만 가져올때
                            String extension = one.getName().substring(end_index + 1) ;
                            System.out.println(extension);
                        }
                    }
                }
            }else{
                System.out.println("파일");
            }
        }else{
            System.out.println("존재하지 않는 항목입니다.");
        }
    }
}
```



#### \# RandomTest.java (스프링) (05.상품.txt)
(test - RandomTest 클래스 생성)
- 코드 작성
```java
package com.coffee.test;

import java.util.Random;

public class RandomTest {
    public static void main(String[] args) {
        Random rand = new Random();

        // rand.nextBoolean()는 50%의 확률로 true나 false 중 하나를 무작위로 뽑아주는 동작
        boolean bool = rand.nextBoolean();
        System.out.println(bool);

        // rand.nextInt()는 숫자의 범위가 0부터 시작함 6넣으면 0~5사이 나옴
        // 그래서 소괄호 바깥에 + 1 하면 됨
        int jusawee = rand.nextInt(6) + 1;
        System.out.println(jusawee);
```

        // 배열의 배열요소를 rand.nextInt()를 이용해서 랜덤으로 추출하기
        String\[\] menu = {"제육볶음", "돈까스", "오므라이스", "떡볶이", "마라탕"};
        String item = menu\[rand.nextInt(menu.length)\];
        String message = "오늘 점심 메뉴 : " + item;
        System.out.println(message);

        // 가격 설정 (범위 설정)
        // 3000원 <= 가격 <= 7000원
        int price = 1000 \* (rand.nextInt(5) + 3) ;
        System.out.println("가격 : " + price);
    }
}



#### \# ProductRepository.java (스프링) (05.상품.txt)
(repository - ProductRepository 인터페이스 생성)

- 코드 작성
```java
package com.coffee.repository;

import com.coffee.entity.Product;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProductRepository extends JpaRepository<Product, Long> {
}
```



#### \# GenerateData.java (스프링) (05.상품.txt)
(common 폴더 생성 - GenerateData 클래스 생성)
GenerateDatac:\shop\images 폴더 내의 모든 이미지 정보를 읽어서 products 테이블에
데이터를 만들어 주는 유틸리티 클래스입니다.

- 코드 작성
```java
package com.coffee.common;

import com.coffee.constant.Category;
import com.coffee.entity.Product;

import java.io.File;
import java.time.LocalDate;
import java.util.*;

public class GenerateData {

    private final String imageFolder = "c:\\shop\\images";

    // 🔥 상품명 중복 카운트용 Map
    private Map<String, Integer> nameCountMap = new HashMap<>();

    // 📌 이미지 파일 목록 가져오기
    public List<String> getImageFileNames() {
        File folder = new File(imageFolder); // 해당 경로의 객체 생성
        List<String> imageFiles = new ArrayList<>(); // 이미지 파일 이름 수집을 위한 빈 공간 생성

        // 해당 경로가 존재하지 않거나 해당 경로가 폴더가 아니고 파일일 경우 아래 메소드들이 필요없어서
        // return으로 getImageFileNames() 메소드 종료시키기
        if (!folder.exists() || !folder.isDirectory()) {
            System.out.println(imageFolder + " 폴더가 존재하지 않습니다");
            return imageFiles;
        }

        String[] imageExtensions = {".jpg", ".jpeg", ".png"}; // 이미지 확장자를 미리 배열에 넣어놓기
        File[] fileList = folder.listFiles(); // folder 경로에 들어있는 모든 파일 및 하위 폴더들을 배열에 넣음

        if (fileList != null) { // fileList 내용물 미리 체크하기
            for (File file : fileList) { // 확장 for
                // fileList 내용물이 파일이고 Arrays.stream() 소괄호 안에 들어있는 것을 확장 for처럼 꺼냄
                // .anyMatch(ext -> )에서 ext에 꺼낸 내용물을을 넣고 하나하나 체크함
                // 결국 fileList에 든 모든 파일들을 하나씩 꺼내서 imageExtensions에 들어있는 String들이 끝에
                // 있는지 검사하고 맞으면 그에 해당하는 파일들의 이름을 imageFiles 리스트에 넣음
                if (file.isFile() && Arrays.stream(imageExtensions)
                        .anyMatch(ext -> file.getName().toLowerCase().endsWith(ext))) {
                    imageFiles.add(file.getName());
                }
            }
        }
        // 조건식에 맞는 파일들의 이름이 담긴 String들을 imageFiles 리스트에 넣고 반환함
        return imageFiles;
    }

    // 📌 상품 생성
    public Product createProduct(int index, String imageName) {
        Product product = new Product();

        // 1️⃣ 확장자 제거
        String fileName = imageName.substring(0, imageName.lastIndexOf(".")).toLowerCase();

        // 2️⃣ _bigsize 제거
        fileName = fileName.replace("_bigsize", "");
```

        // 3️⃣ 숫자 제거 → 기본 이름 추출 // 정규표현식 \[0-9\]을 시용해서 0~9까지의 모든 숫자를 공백으로 치환
        String baseName = fileName.replaceAll("\[0-9\]", "");

        // 4️⃣ "_" 제거
        baseName = baseName.replace("_", "");

        // 5️⃣ 한글 상품명 변환
        String koreanName = convertToKoreanName(baseName);

        // 6️⃣ 동일 상품명에 번호 붙이기
        // getOrDefault(키, 기본값)은 map의 값을 가져옴
        // map의 키값이 koreanName을 가져오는데 없으면 0이라는 기본값을 반환함
        // 있으면 그 값을 가져옴
        int count = nameCountMap.getOrDefault(koreanName, 0) + 1;
        nameCountMap.put(koreanName, count);

        // %02d : 숫자가 한 자리면 앞에 0을 붙여서 무조건 2자리 숫자로 채우라는 자바 문법
        String productName = koreanName + String.format("%02d", count);

        // 7️⃣ 카테고리 자동 분류
        product.setCategory(getCategoryFromName(baseName));

        // 8️⃣ 상품명
        product.setName(productName);

        // 9️⃣ 설명
        product.setDescription(getRandomDescription(productName));

        // 🔟 이미지
        product.setImage(imageName);

```java
        // 11️⃣ 가격 / 재고
        product.setPrice(1000 * getRandomDataRange(1, 10));
        product.setStock(100 * getRandomDataRange(1, 10));

        // 12️⃣ 날짜
        product.setInputdate(LocalDate.now().minusDays(index));

        return product;
    }

    // 📌 맛 표현 랜덤 리스트
    private String getRandomDescription(String productName) {
        String[] descriptions = {
                productName + "는 깊고 진한 풍미가 일품입니다.",
                productName + "는 부드럽고 달콤한 맛을 자랑합니다.",
                productName + "는 고소하고 풍부한 향이 매력적입니다.",
                productName + "는 신선하고 깔끔한 맛이 특징입니다.",
                productName + "는 입안 가득 퍼지는 진한 맛을 느낄 수 있습니다.",
                productName + "는 달콤하면서도 부드러운 식감이 좋습니다.",
                productName + "는 은은한 향과 깊은 맛이 조화롭습니다.",
                productName + "는 누구나 좋아하는 클래식한 맛입니다."
        };

        return descriptions[new Random().nextInt(descriptions.length)];
    }

    // 📌 카테고리 자동 분류
    private Category getCategoryFromName(String name) {
        name = name.toLowerCase();

        if (name.contains("americano") || name.contains("cappuccino") || name.contains("latte") || name.contains("espresso") || name.contains("milk") || name.contains("juice")) {
            return Category.BEVERAGE;
        } else if (name.contains("cake") || name.contains("chocolate") || name.contains("sponge")) {
            return Category.CAKE;
        } else if (name.contains("bread") || name.contains("croissant") || name.contains("ciabatta") || name.contains("brioche") || name.contains("baguette") || name.contains("scone")) {
            return Category.BREAD;
        } else if (name.contains("wine")) {
            return Category.BEVERAGE;
        } else {
            return Category.BREAD; // 기본값
        }
    }

    // 📌 랜덤 범위 값
    private int getRandomDataRange(int start, int end) {
        return new Random().nextInt(end) + start;
    }

    // 📌 영문 → 한글 상품명 변환
    private String convertToKoreanName(String name) {
        name = name.toLowerCase();

        if (name.contains("americano")) return "아메리카노";
        if (name.contains("cappuccino")) return "카푸치노";
        if (name.contains("latte")) return "바닐라라떼";
        if (name.contains("espresso")) return "에스프레소";
        if (name.contains("milk")) return "우유";
        if (name.contains("juice")) return "주스";

        if (name.contains("croissant")) return "크로아상";
        if (name.contains("ciabatta")) return "치아바타";
        if (name.contains("brioche")) return "브리오슈";
        if (name.contains("baguette")) return "바게트";
        if (name.contains("scone")) return "스콘";

        if (name.contains("cake")) return "케이크";
        if (name.contains("chocolate")) return "초코케이크";
        if (name.contains("sponge")) return "스펀지케이크";

        if (name.contains("macaron")) return "마카롱";

        if (name.contains("wine")) return "와인";

        // 매칭 안될 경우
        return name;
    }
}
```



#### \# ProductTest.java (스프링) (05.상품.txt)
(test - ProductTest 클래스 생성)

- 코드 작성
```java
package com.coffee.test;

import com.coffee.common.GenerateData;
import com.coffee.entity.Product;
import com.coffee.repository.ProductRepository;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.List;

@SpringBootTest
public class ProductTest {
    @Autowired
    private ProductRepository productRepository ;

    @Test
    @DisplayName("이미지를 이용한 데이터 추가")
    public void createProductMany(){
        // 특정한 폴더 내에 들어 있는 상품 이미지들을 이용하여 상품 테이블에 추가합니다.
        GenerateData gendata = new GenerateData();

        List<String> imageNameList = gendata.getImageFileNames();
        System.out.println("총 이미지 갯수 : " + imageNameList.size());

        for (int i = 0; i < imageNameList.size(); i++) {
            // bean 객체에 imageNameList의 요소들을 가져와서 넣음
            // 이미 완성된 객체 자체인 product를 GenerateData에서 가져와서 이 클래스에서는
            // 객체를 따로 생성하지 않아도 됨
            Product bean = gendata.createProduct(i, imageNameList.get(i));
            // System.out.println(bean);
            // 굳이 this를 적지 않아도 됨
            this.productRepository.save(bean);
        }
    }
}
```



#### \# MenuItems.tsx 수정 (리액트) (05.상품.txt)
- 코드 추가 (\<Nav\> 태크 안에 넣기)
```typescript
{/* 하이퍼링크 : Nav.Link는 다른 페이지로 이동할 때 사용됩니다.  */}
<Nav.Link onClick={() => navigate(`/product/list`)}>상품 보기</Nav.Link>
```


#### \# AppRoutes.tsx 수정 (리액트) (05.상품.txt)
- 코드 추가
```typescript
import ProductList from './../pages/ProductList';

<Route path='/product/list' element={<ProductList />} />
```




#### \# Product.ts (리액트) (05.상품.txt)
(types - Product.ts 생성)
원래는 스프링의 Entity보고 작성해야하는 코드

- 코드 작성
```typescript
export interface Product {
    id: number;
    name: string;
    price: number;
    category: string;      // Enum은 JSON으로 오면 문자열
    stock: number;
    image: string;
    description: string;
    inputdate: string;     // LocalDate → 문자열로 넘어옴 (예: "2026-02-20")
}
```



#### \# axios, rechart, chart.js - Promise (React 교안 PDF (P.102))
- then()
Promise가 이행되었을 때 실행할 콜백 함수를 등록합니다.
콜백 함수는 Promise가 이행된 결과를 전달받습니다.
정상적으로 되었을 때

- catch()
Promise가 거부되었을 때 실행할 콜백 함수를 등록합니다.
콜백 함수는 Promise가 거부된 이유를 전달받습니다.
정상적으로 되지 않았을 때



#### \# ProductList.tsx (리액트) (05.상품.txt)
(pages - ProductList.tsx 생성)

- 코드 작성
```typescript
import { Card, Col, Container, Row } from "react-bootstrap";
import { useEffect, useState } from "react";
import type { Product } from "../types/Product";

import customAxios from './../api/axiosInstance';

import { API_BASE_URL } from "../config/config";


function App() {
    const [products, setProducts] = useState<Product[]>([]);

    useEffect(() => {
        const url = `${API_BASE_URL}/product/list`;
        customAxios.get(url)
            .then((response) => {
                console.log('응답 받은 데이터');
                console.log(response);
                setProducts(response.data);
            })
            .catch((error) => {
                console.log(error);
            });
    }, []);

    console.log('자바스크립트 코딩 영역');

    return (
        <Container className="my-4">
            <h1 className="my-4">상품 목록 페이지</h1>

            {/* 필드 검색 영역 */}

            {/* 자료 보여 주는 영역 */}
            <Row>
                {/* products는 상품 배열, item는 상품 1개를 의미 */}
                {products.map((item) => ( // 자바의 확장 for문과 같은 리액트 문법
                    <Col key={item.id} md={4} className="mb-4">
                        <Card className="h-100" style={{ cursor: 'pointer' }}>
                            <Card.Img
                                variant="top"
                                src={`${API_BASE_URL}/images/${item.image}`}
                                alt={item.name}
                                style={{ width: '100%', height: '200px' }}
                            />
                            <Card.Body>
                                <Card.Title>{item.name}({item.id})</Card.Title>
                                <Card.Text>가격 : {item.price.toLocaleString()} 원</Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                ))}
            </Row>

            {/* 페이징 처리 영역 */}

        </Container>
    );
};

export default App;
```



#### \# ProductRepository.java 수정 (스프링) (05.상품.txt)
(repository - ProductRepository)
상품 목록을 아이디 역순으로 조회하는 추상 메소드를 작성
List\<Product\> findProductByOrderByIdDesc();

- 코드 추가
```java
package com.coffee.repository;

import com.coffee.entity.Product;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface ProductRepository extends JpaRepository<Product, Long> {
    // 쿼리 메소드 findProductByOrderByIdDesc()
    // 상품(Product)들을 가져오는데, ID 번호가 큰 것부터(최신순으로) 정렬해서 다 가져와라!
    // Service가 이용하고 그걸 또 Controller가 이용함
    // find테이블By : 조회해라 (select)
    // Product : Product 테이블
    // OrderBy컬럼 : 컬럼을 기준으로 정렬해라
    // Id : Id 컬럼
    // Desc : 내림차순 (큰수부터 아래로) (최신순 정렬)
    List<Product> findProductByOrderByIdDesc();
}
```



#### \# ProductService.java (스프링) (05.상품.txt)
(service - ProductService 클래스 생성)
```java
public List<Product> getProductList()
```

- 코드 작성
```java
package com.coffee.service;

import com.coffee.entity.Product;
import com.coffee.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ProductService {
    @Autowired
    private ProductRepository productRepository ;

    // ProductRepository에서 만든 쿼리 메소드를 이용해서 메소드만들어서 Controller에 이용할 예정
    public List<Product> getProductList(){
        return this.productRepository.findProductByOrderByIdDesc();
    }
}
```



#### \# ProductController.java (스프링) (05.상품.txt)
(controller - ProductController 클래스 생성)
public List<Product> list() 메소드

- 코드 작성
```java
package com.coffee.controller;

import com.coffee.entity.Product;
import com.coffee.service.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;


@RestController
@RequestMapping("/product")
public class ProductController {
    @Autowired
    private ProductService productService ;

    @GetMapping("/list")
    public List<Product> list(){
        List<Product> products = this.productService.getProductList() ;
        return products ;
    }
}
```



#### \# 보안 설정 클래스 : SecurityConfig.java 파일 (스프링) (05.상품.txt)
(config 폴더에 - SecurityConfig 파일에 코드 추가)
(이미 추가 되어 있음)
배열 permitUrls에 ""/product/list" 항목 추가하기
(인증이 없어도 상품 보기 항목은 봐야하니까)



#### \# JwtTokenProvider.java (스프링) (05.상품.txt)
- return Jwts.setClaims() 부분 수정 (전부 덮어쓰기하는 메소드)
수정할 부분 : .setClaims(Map.of("role", member.getRole().name())) // 권한 정보
수정한 부분 : .claim("role", member.getRole().name()) // 권한 정보(전부 덮어쓰기하지 않게하기 위해서)

원래 token의 내용 부분인 claim 중 자주 쓰는 부분은 표준으로 만들어서 메소드명으로 만들어 놓았는데
추가적으로 개발자가 마음대로 claim에 내용을 넣고 싶을때 쓰는 메소드가 claim메소드
+ setSubject() 같은 메소드말고 setClaims() 안에 Map으로 한번에 모든 claim의 내용들을 넣을 수도 있지만
혹시라도 키값이 오타로 잘못입력되는 경우가 있어서 권장하지는 않음




#### \# 이벤트 버블링 방지 (리액트)
event.stopPropagation();
하위 개념이 상위 개념으로 계속해서 넘어가는 것


#### \# AppRoutes.tsx (리액트) (05.상품.txt)
ProductList 앱에 user 프롭스를 넘겨 줍니다.
```typescript
<Route path='/product/list' element={<ProductList user={user} />} />
```
의
user={user} 추가하기



#### \# ProductList.tsx (리액트) (05.상품.txt)
(pages - ProductList.tsx 파일 수정)
넘어온 user를 위한 ProductProps type를 정의
상품 등록을 위한 \<Link\>를 추가
수정, 삭제를 위한 \<Button\>을 추가

- 코드 작성
```typescript
import { Button, Card, Col, Container, Row } from "react-bootstrap";
import { useEffect, useState } from "react";
import type { Product } from "../types/Product";

import customAxios from './../api/axiosInstance';

import { API_BASE_URL } from "../config/config";
import type { User } from "../types/User";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";

// 넘어온 user를 위한 ProductProps type를 정의
```
type ProductProps = { // user: User는 자바의 객체: 클래스 정도로 이해하면 됨
```typescript
    user: User | null; // 로그인하면 의미 있는 객체, 아니면 null (로그인하면 App.tsx부터 정보를 넣고 내려옴)
};


function App({ user }: ProductProps) { // 프롭스 주입
    const [products, setProducts] = useState<Product[]>([]);

    useEffect(() => {
        const url = `${API_BASE_URL}/product/list`;
        customAxios.get(url)
            .then((response) => {
                console.log('응답 받은 데이터');
                console.log(response);
                setProducts(response.data);
            })
            .catch((error) => {
                console.log(error);
            });
    }, []);

    const navigate = useNavigate();

    const makeAdminButtons = (item: Product, user: User | null, navigate: any) => {
        if (user?.role !== 'ADMIN') return null;

        return (
            <div className="d-flex justify-content-center">
                <Button // 수정을 위한 <Button>을 추가합니다.
                    variant="warning"
                    className="mb-2"
                    size="sm"
                    onClick={(event) => {
                        // 이 코드가 없으면 수정버튼을 포함하고 있는 더 큰 영역을 클릭했을때
                        // 그 큰 영역도 onClick으로 다른 일을 해야하는데 그 일과 이 코드가 동시에 시작해버려서
                        // 문제가 생길 수도 있음
                        event.stopPropagation(); // 이벤트 버블링 방지
                        navigate(`/product/update/${item.id}`);
                    }}>
                    수정
                </Button>

                {/* 한 칸 공백 넣기 */}
                &nbsp;

                <Button // 삭제를 위한 <Button>을 추가합니다. (confirm 함수 이용)(alert과는 다름)
                    variant="danger"
                    className="mb-2"
                    size="sm"
                    onClick={async (event) => { // 백엔드를 거치고 일처리를 해야해서 async 붙임
                        event.stopPropagation(); // 이벤트 버블링 방지

                        const isDelete = window.confirm(`${item.name} 상품을 삭제하시겠습니까?`);

                        if (isDelete === false) {
                            /* sweet alert2 사이트에 이쁜거 많음 */
                            alert(`${item.name} 상품 삭제를 취소하였습니다.`)
                            return;
                        }

                        try { // 전체 배열에서 일부 데이터만 필터할 수 있음
                            const url = `${API_BASE_URL}/product/delete/${item.id}`;
                            await axios.delete(url); // 백엔드를 거치고 일처리를 해야해서 await 붙임
                            alert(`'${item.name}' 상품이 삭제되었습니다.`)

                            // 상품을 갱신해주는 setter
                            // 이전(prev) : 기존 state (삭제 전)
                            // filter() : true인 것만 따로 모아서 새로운 배열을 생성
                            // p : prev에 있는 기존 상품들
                            // p.id !== item.id : 기존 상품의 id와 삭제된 상품의 id가 다르다 -> 삭제된 상품이 아니다.
                            // 삭제된 상품이 아닌 것들만 따로 모아서 다시 products에 저장
                            setProducts(prev => prev.filter(p => p.id !== item.id));

                            navigate('/product/list');

                        } catch (error) {
                            console.log(error);
                            if (axios.isAxiosError(error)) {
                                alert(`상품 삭제 실패 : ${error.response?.data || error.message}`);
                            } else {
                                console.log('알수 없는 에러 : ' + error);
                            }
                        };
                    }}>
                    삭제
                </Button>
            </div>
        );
    };

    console.log('자바스크립트 코딩 영역');

    return (
        <Container className="my-4">
            <h1 className="my-4">상품 목록 페이지</h1>

            {/* 상품 등록을 위한 <Link>를 추가합니다. */}
            <Link to={`/product/insert`}>
                {/* 수정, 삭제를 위한 <Button>을 추가합니다. */}
                {user?.role === 'ADMIN' && (
                    <Button variant="primary" className="mb-3">
                        상품 등록
                    </Button>
                )}
            </Link>


            {/* 필드 검색 영역 */}

            {/* 자료 보여 주는 영역 */}
            <Row>
                {/* products는 상품 배열, item는 상품 1개를 의미 */}
                {products.map((item) => ( // 자바의 확장 for문과 같은 리액트 문법
                    <Col key={item.id} md={4} className="mb-4">
                        <Card className="h-100" style={{ cursor: 'pointer' }}>
                            <Card.Img
                                variant="top"
                                src={`${API_BASE_URL}/images/${item.image}`}
                                alt={item.name}
                                style={{ width: '100%', height: '200px' }}
                            />
                            <Card.Body>
                                <table style={{ width: '100%', borderCollapse: 'collapse', border: 'none' }}>
                                    <tbody>
                                        <tr>
                                            <td style={{ width: '70%', padding: '4px', border: 'none' }}>
                                                <Card.Title>{item.name}({item.id})</Card.Title>
                                            </td>
                                            <td rowSpan={2} style={{ padding: '4px', border: 'none', textAlign: 'center', verticalAlign: 'middle' }}>
                                                {makeAdminButtons(item, user, navigate)}
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style={{ width: '70%', padding: '4px', border: 'none' }}>
                                                <Card.Text>가격 : {item.price.toLocaleString()} 원</Card.Text>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>

                            </Card.Body>
                        </Card>
                    </Col>
                ))}
            </Row>

            {/* 페이징 처리 영역 */}

        </Container>
    );
};

export default App;
```



#### \# ProductService.java (스프링) (05.상품.txt)
(service - ProductService 수정)
```java
public boolean deleteProduct(Long id)
```
1\. 상품 id를 이용하여 상품 객체 확인
2\. 운영 체제 내의 상품 이미지 제거
3\. 데이터 베이스에서 1행 삭제

- 코드 작성
```java
package com.coffee.service;

import com.coffee.entity.Product;
import com.coffee.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.io.File;
import java.util.List;

@Service
public class ProductService {
    @Autowired
    private ProductRepository productRepository ;

    // ProductRepository에서 만든 쿼리 메소드를 이용해서 메소드만들어서 Controller에 이용할 예정
    public List<Product> getProductList(){
        return this.productRepository.findProductByOrderByIdDesc();
    }

    // application.properties에서 이미지가 있는 실제 위치 가져오기
    @Value("${productImageLocation}")
    private String productImageLocation ;

    // 상품 id를 이용한 삭제
    // 1) 삭제할 상품이 데이터 베이스에 실제로 존재하는지 id를 통해 확인
    // 2) 운영체제에서 상품 삭제
    // 3) 상품 자체를 삭제

    // 1) 상품이 존재 하는지 확인
    public boolean deleteProduct(Long id){
        // 상품 가져오기 / 상품 id에 맞는 상품이 없으면 오류가 나니까
        // orElse()을 넣어서 ()안에 있는 내용을 가져오기 (null)을 가져옴
        Product product = productRepository.findById(id).orElse(null) ;

        // 상품id에 맞는 상품이 없으면
        if(product == null){
            return false ; // 없는 상품을 삭제할 수 없으니 상품 삭제 메소드는 실패해서 (false)를 반환함
        }

        // 상품id에 맞는 상품이 있으면
        // 2) 이미지가 있는 c드라이브 폴더(운영체제 내)에 가서 이미지 지우기
        String fileName = product.getImage() ;
        if(fileName != null && !fileName.isEmpty()){ // 다시 한 번 정상적인 파일이름인지 확인하기
            // application.properties에서 가져온 이미지 위치 연결하기
            File file = new File(productImageLocation + fileName) ;

            System.out.println("삭제될 파일 이름");
            // ex) C:\\upload\images\americano.jpg
            System.out.println(file.getAbsolutePath()); // 절대 경로 보여주기

            if(file.exists()){ // 해당 경로에! 삭제를 원하는 그 파일이 존재하는지 확인
                // 실제로 해당 경로의 파일을 삭제하고
                // 성공하면 true / 실패하면 false 반환함
                boolean deleted = file.delete() ;

                if(!deleted){ // 조건이 성립되려면 deleted가 false여야 !deleted가 true여서 메소드가 시작됨
                    System.out.println("이미지 삭제 실패");
                }
            }
        }
        // 3) 데이터 베이스에서 상품 삭제하기
        // 운영체제에서 이미지 파일을 삭제했으니 데이터 베이스에서도 삭제하기
        productRepository.deleteById(id);
        return true; // deleteProduct() 메소드 반환
    }
}
```



#### \# ProductController.java (스프링) (05.상품.txt)
(controller - ProductController 수정)

- 코드 작성
```java
package com.coffee.controller;

import com.coffee.entity.Product;
import com.coffee.service.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@RestController
@RequestMapping("/product")
public class ProductController {
    @Autowired
    private ProductService productService ;

    @GetMapping("/list")
    public List<Product> list(){
        // 내림차순으로 Product테이블의 데이터를 정렬한 것들을 products에 넣고 프론트에 보냄(response)
        List<Product> products = this.productService.getProductList() ;
        return products ;
    }

    // {id}를 경로 변수라고 부르며, 가변 매개 변수라고 부름
    // 상품 50번 누르면 id가 50으로 바뀌듯 그때그때 상황에 따라 바뀜
    // 경로변수를 delete() 안에 넣고 @PathVariable이라는 경로변수 어노테이션도 작성하면
    // 매핑에 있는 경로 변수 id가 delete의 id로 들어옴
    @DeleteMapping("/delete/{id}")
    public ResponseEntity<String> delete(@PathVariable Long id){
        try {
            boolean isDeleted = this.productService.deleteProduct(id);

            if(isDeleted){ // isDeleted가 true면 삭제가 정상적으로 되었다는 뜻
                // 여기까지 왔다는 것은 에러없이 성공해서 내가 원하는 동작인 삭제가 된 것임
                return ResponseEntity.ok(id + "번 상품이 삭제되었습니다.");
            }else{ // 삭제를 할 상품 자체가 없는 상태
                return ResponseEntity.badRequest().body(id + "번 상품이 존재하지 않습니다.");
            }

        }catch (DataIntegrityViolationException err){// 데이터 베이스 무결성 위배되는 에러가 발생할때
            String message = "해당 상품은 장바구니에 포함이 되어 있거나, 이미 매출이 발생한 상품입니다. \n확인해 주세요." ;
            return ResponseEntity.internalServerError().body(message);

        }catch (Exception err){ // 두루뭉실한 예외처리
            return ResponseEntity.internalServerError().body("오류 발생 : " + err.getMessage());

        }
    }
}
```


#### \# AppRoutes.tsx (리액트) (05.상품.txt)
- 코드 추가
```typescript
import ProductInsertForm from './../pages/ProductInsertForm';

<Route path='/product/insert' element={<ProductInsertForm user={user} />} />
```



#### \# 전개 연산자 이용하기 (React 교안 PDF (P.41))
나열형 자료(배열, 객체 등)를 개별로 추출하거나 연결하고자 할 때 사용하는 연산자
1\. 개별로 추출
```typescript
const numbers = [1, 2, 3, 4, 5, 6];
const [one, two, ...rest] = numbers;
```

2\. 연결
```typescript
const initial_value = {
        name: '',
        price: '',
        category: '-',
        stock: '',
        image: '',
        description: '',
    };

const [product, setProduct] = useState(initial_value);

const ControlChange = (
        event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>
    ) => { // event.target : 해당 이벤트를 발생시킨 요소를 의미
const { name, value } = event.target; // 그 요소의 name과 value 변수를 가져옴

// ...product : 이전 product의 원소들 (initial_value의 속성(원소들))
// [name] : key값인 name은 그냥 name으로 적으면 문자열 "name"으로 인식해서 변수로 인식하려면 []을 해야 변수값을 넣어줌
// value : value는 그냥 변수 그대로 적어도 알아서 변수로 인식해서 값을 넣어줌
// 중복된 키가 있으면 가장 마지막에 추가된 키와 값으로 대체됨
setProduct({ ...product, [name]: value });
};
```


#### \# ProductInsertForm.tsx (리액트) (05.상품.txt)
(pages - ProductInsertForm.tsx 생성)

- 코드 작성
```typescript
import { Alert, Button, Col, Container, Form, Row } from "react-bootstrap";
import type { User } from "../types/User";
import React, { useState } from "react";

import axios from "axios";
import customAxios from './../api/axiosInstance';

import { useNavigate } from "react-router-dom";
import { API_BASE_URL } from "../config/config";

interface ProductInsertFormProps {
    user: User | null;
}

function App({ user }: ProductInsertFormProps) {
    const navigate = useNavigate();

    const comment = '상품 등록'; // 제목으로도 쓰고 버튼이름으로도 쓸거같아서 변수로 만든 것

    const initial_value = { // 스프링의 Entity보고 작성 (Long id / LocalDate inputdate는 스프링이 자동 생성함)
        name: '',
        price: '',
        category: '-',
        stock: '',
        image: '',
        description: '',
    };

    // 등록하고자하는 상품 정보
    // 초기 값은 initial_value
    const [product, setProduct] = useState(initial_value);

    const initialErrors = {
        name: '',
        price: '',
        category: '',
        stock: '',
        image: '',
        description: '',
        general: ''
    };

    // State를 만드는데 errors라는 이름으로 만들고 초기값은 initialErrors로 설정한다.
    const [errors, setErrors] = useState(initialErrors);

    // Change 이벤트가 발생하면 동작하는 함수
    // 폼 양식에서 어떠한 컨트롤의 값이 변경되었습니다.
    // ()는 매개변수 {}는 동작
    // HTMLInputElement 한 줄 입력상자
    // HTMLTextAreaElement 멀티라인 입력상자
    const ControlChange = (
        // HTMLInputElement : HTML부분의 input(jsx의 Control)의 요소 (한 줄 입력)
        // HTMLTextAreaElement : HTML부분의 textarea(jsx의 Control)의 요소 (여러 줄 입력)
        // HTMLSelectElement : HTML부분의 select(jsx의 Select)의 요소 (콤보박스 선택 입력)
        event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>
    ) => {
        // event.target : 해당 이벤트를 발생시킨 요소를 의미
        // event.target 객체가 가진 원소중 name과 value인 키의 값만 골라서 변수로 지정함
        // event.target.name : Form.Control의 속성인 name의 값
        // event.target.value : 사용자가 입력한 값
        const { name, value } = event.target;

        // Product가 객체여서 중괄호 사용
        // {[name]: value}만 적으면 name을 제외한 나머지 속성들이 휘발됨
        // 이를 방지하기 위해 ...product를 추가 (...product는 기존 product의 값을 가져오는 것)
        // ...product로 가져온 기존의 [name]의 value는 내가 새로 적은 value로 덮어쓰기 됨
        // (...은 전개 연산자로 불림 - 예약어) (...객체 or 배열 : 객체 or 배열의 원소들을 가져오는 문법)
        setProduct({ ...product, [name]: value });
    };

    const FileSelect = (
        event: React.ChangeEvent<HTMLInputElement>
    ) => {
        // event.target 객체가 가진 원소중 name과 files인 키의 값만 골라서 변수로 지정함
        // files가 첨부 파일(이미지)의 value라고 생각하면 됨
        const { name, files } = event.target;

        // 입력한 값이 파일(이미지)이 아닐때의 조건식과 동작
        // !files : 입력한 값이 파일이 아닐때 값이 비어있음
        // files.length === 0 : 값 자체는 존재하는데 기본값인 0일때 - 사실상 존재하지 않음
        if (!files || files.length === 0) {
            alert('이미지 파일을 선택해 주셔야 합니다.');
            return;
        }
        // 1) JS에서 만약 체크 박스가 있다고 할 때 2개를 체크하면 배열이 만들어짐
        // 2) 이미지 선택 양식을 의미하는 배열
        // 3) type이 file인 이미지는 선택하면 1개여도 객체 데이터 덩어리여서 무조건 배열로 생성이 됨
        // 파일을 선택하면 배열의 앞 부분에 추가됨
        // 4) files[0] : 이미지를 여러개 선택해도 우리는 이미지 1개가 필요해서
        // 제일 첫번째 이미지 오직 한개!를 선택하기 위해서
        // files배열의 인덱스 0번인 files[0]를 file에 넣은 것
        const file = files[0]; // type="file"로 작성한 첫번째 항목

        // FileReader : 이미지 파일(바이너리 바이트 데이터)을 읽어 들여서
        // JS가 알아듣게 텍스트 문장으로 변환해 주는 번역기
        const reader = new FileReader();

        // readAsDataURL() : 해당 이미지를 Base64 인코딩 문자열 형식으로 변환해서 reader 객체에 저장함
        // 사용 예시 : data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA...
        // 스프링에서 이 텍스트를 받고나서
        // 필요한 부분은 ,뒤에 있는 iVBORw0KGgoAAAANSUhEUgAAAAUA...이 부분이여서
        // String 클래스의 substring으로 추출해와야함
        reader.readAsDataURL(file);

        // readAsDataURL()은 시간이 걸리는 비동기 작업이라 끝났을때 알려주는 함수가 필요함
        // JS가 이해할 수 있도록 변경해주는 과정이 다 끝날을때 하는 동작을 지정하는 함수
        reader.onloadend = () => {
            // result안에는 data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA...
            // 이 값이 들어 있음
            const result = reader.result;

            // [name]는 name 변수의 값(image)
            setProduct({ ...product, [name]: result });
        }
    };

    const SubmitAction = async (event: React.SyntheticEvent<HTMLFormElement>) => {
        // 원래 취해야 할 동작을 못하게 하기
        event.preventDefault();

        if (product.category === '-') {
            alert('상품 카테고리는 반드시 선택해 주셔야 합니다.');
            return;
        }

        try {
            const url = `${API_BASE_URL}/product/insert`;
            const config = {
                headers: { 'Content-Type': 'application/json' }
            };

            const response = await customAxios.post(url, product, config);

            console.log('응답 데이터 : ');
            console.log(`${response.data}`);

            alert('상품 등록되었습니다.');
```

```typescript
            // 초기화 하기
            // 강제로 '/product/list'로 이동해서 초기화하지 않아도 되지만
            // 뒤로가기 버튼을 눌렀을때 입력했던 데이터가 남아있으니까 초기화 함
            setProduct(initial_value);
            setErrors(initialErrors);

            navigate('/product/list');

        } catch (error: unknown) {
            console.log(error);
            if (axios.isAxiosError(error) && error.response) {
                // 백엔드에서 전달받은 오류 메시지를 저장
                setErrors((prev) => ({
                    ...prev,
                    ...error.response?.data?.errors,
                    general: error.response?.data?.message || '상품 등록 중 오류가 발생했습니다.'
                }));
            } else {
                setErrors((prev) => ({
                    ...prev,
                    general: '서버와의 통신 중 오류가 발생했습니다.'
                }));
            }
        };
    };

    return (
        <Container style={{ marginTop: '30px' }}>
            <h1>{comment}</h1>

            {/* 일반 오류 메시지 */}
            {errors.general && <Alert variant="danger">{errors.general}</Alert>}

            {/* 특별한 말이 없으면 Form을 불러올때 bootstrap으로 하면 됨 */}
            <Form onSubmit={SubmitAction}> {/* id는 자동 생성하게 스프링에 만들어 놓아서 입력란에 넣을 필요는 없음 */}

                {/* 이름 입력창 */}
                {/* controlId="formName" 이건 필수는 아님 */}
                <Form.Group as={Row} className="mb-3" controlId="formName">
                    <Form.Label column sm={2}>
                        이름
                    </Form.Label>
                    <Col sm={10}> {/* Form.Control은 HTML의 form의 input같은 것 */}
                        <Form.Control
                            type="text"
                            placeholder="이름을(를) 입력해 주세요."

                            // 정확히 말하자면 name 속성이 아니고 id속성임
                            // 그래서 Form.Group태그의 controlId속성에 formName으로 설정함
                            // name이 price면 price로 바꾸고 formPrice로 하면 됨
                            name="name"
                            value={product.name}

                            // Change 이벤트 : 값이 변하면 동작하는 이벤트
                            onChange={ControlChange}

                            // 값을 정확하게 boolean 타입으로 만들어서 true나 false로 만들려고 !!사용
                            isInvalid={!!errors.name}
                        />

                        {/* 문제가 생기면 나오는 경고성 멘트 */}
                        <Form.Control.Feedback type="invalid">
                            {errors.name}
                        </Form.Control.Feedback>
                    </Col>
                </Form.Group>

                {/* 가격 입력창 */}
                <Form.Group as={Row} className="mb-3" controlId="formPrice">
                    <Form.Label column sm={2}>
                        가격
                    </Form.Label>
                    <Col sm={10}> {/* Form.Control은 HTML의 form의 input같은 것 */}
                        <Form.Control
                            type="number"
                            placeholder="가격을(를) 입력해 주세요."

                            // 정확히 말하자면 name 속성이 아니고 id속성임
                            name="price"
                            value={product.price}

                            // Change 이벤트 : 값이 변하면 동작하는 이벤트
                            onChange={ControlChange}

                            // 값을 정확하게 boolean 타입으로 만들어서 true나 false로 만들려고 !!사용
                            isInvalid={!!errors.price}
                        />

                        {/* 문제가 생기면 나오는 경고성 멘트 */}
                        <Form.Control.Feedback type="invalid">
                            {errors.price}
                        </Form.Control.Feedback>
                    </Col>
                </Form.Group>

                {/* 카테고리 입력창 */}
                {/* Form.Control말고 select로 콤보 박스 만들기 */}
                {/* 스프링의 constant폴더의 Category.java인 이용해서 */}
                {/* type, placeholder 삭제 */}
                <Form.Group as={Row} className="mb-3" controlId="formCategory">
                    <Form.Label column sm={2}>
                        카테고리
                    </Form.Label>
                    <Col sm={10}> {/* Form.Select는 HTML의 form의 select같은 것 */}
                        <Form.Select

                            // 정확히 말하자면 name 속성이 아니고 id속성임
                            name="category"
                            value={product.category}

                            // Change 이벤트 : 값이 변하면 동작하는 이벤트
                            onChange={ControlChange}
                            isInvalid={!!errors.category}
                        >
                            <option value="-">-- 상품 카테고리를 선택해 주세요.</option>
                            <option value="BREAD">빵</option>
                            <option value="BEVERAGE">음료수</option>
                            <option value="CAKE">케이크</option>
                            <option value="MACARON">마카롱</option>
                        </Form.Select>

                        {/* 문제가 생기면 나오는 경고성 멘트 */}
                        <Form.Control.Feedback type="invalid">
                            {errors.category}
                        </Form.Control.Feedback>
                    </Col>
                </Form.Group>

                {/* 재고 입력창 */}
                <Form.Group as={Row} className="mb-3" controlId="formStock">
                    <Form.Label column sm={2}>
                        재고
                    </Form.Label>
                    <Col sm={10}> {/* Form.Control은 HTML의 form의 input같은 것 */}
                        <Form.Control
                            type="number"
                            placeholder="재고 수량은 10개 이상 입력해 주셔야 합니다."

                            // 정확히 말하자면 name 속성이 아니고 id속성임
                            name="stock"
                            value={product.stock}

                            // Change 이벤트 : 값이 변하면 동작하는 이벤트
                            onChange={ControlChange}

                            // 값을 정확하게 boolean 타입으로 만들어서 true나 false로 만들려고 !!사용
                            isInvalid={!!errors.stock}
                        />

                        {/* 문제가 생기면 나오는 경고성 멘트 */}
                        <Form.Control.Feedback type="invalid">
                            {errors.stock}
                        </Form.Control.Feedback>
                    </Col>
                </Form.Group>

                {/* 이미지 입력창 */}
                {/* type을 text가 아니라 file로 바꾸기 */}
                {/* onChange={FileSelect}로 바꾸기 */}
                {/* placeholder, value 삭제 */}
                <Form.Group as={Row} className="mb-3" controlId="formImage">
                    <Form.Label column sm={2}>
                        이미지
                    </Form.Label>
                    <Col sm={10}> {/* Form.Control은 HTML의 form의 input같은 것 */}
                        <Form.Control
                            type="file"

                            // 정확히 말하자면 name 속성이 아니고 id속성임
                            name="image"

                            // Change 이벤트 : 값이 변하면 동작하는 이벤트
                            // file은 값이 아니고 객체(물건)으로 취급해서 다르게 해야 함
                            onChange={FileSelect}

                            // 값을 정확하게 boolean 타입으로 만들어서 true나 false로 만들려고 !!사용
                            isInvalid={!!errors.image}
                        />

                        {/* 문제가 생기면 나오는 경고성 멘트 */}
                        <Form.Control.Feedback type="invalid">
                            {errors.image}
                        </Form.Control.Feedback>
                    </Col>
                </Form.Group>

                {/* 설명 입력창 */}
                <Form.Group as={Row} className="mb-3" controlId="formDescription">
                    <Form.Label column sm={2}>
                        상품 설명
                    </Form.Label>
                    <Col sm={10}> {/* Form.Control은 HTML의 form의 input같은 것 */}
                        <Form.Control
                            type="text"
                            placeholder="상품 설명을(를) 입력해 주세요."

                            // 정확히 말하자면 name 속성이 아니고 id속성임
                            name="description"
                            value={product.description}

                            // Change 이벤트 : 값이 변하면 동작하는 이벤트
                            onChange={ControlChange}

                            // 값을 정확하게 boolean 타입으로 만들어서 true나 false로 만들려고 !!사용
                            isInvalid={!!errors.description}
                        />

                        {/* 문제가 생기면 나오는 경고성 멘트 */}
                        <Form.Control.Feedback type="invalid">
                            {errors.description}
                        </Form.Control.Feedback>
                    </Col>
                </Form.Group>

                <Button variant="primary" type="submit" size="lg">
                    {comment}
                </Button>

            </Form>
        </Container>

    );
};

export default App;
```




#### \# ProductService.java 수정 (스프링) (05.상품.txt)
(service - ProductService)

- 코드 수정
```java
package com.coffee.service;

import com.coffee.entity.Product;
import com.coffee.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.io.File;
import java.io.FileOutputStream;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Base64;
import java.util.List;

@Service
public class ProductService {
    @Autowired
    private ProductRepository productRepository ;

    // ProductRepository에서 만든 쿼리 메소드를 이용해서 메소드만들어서 Controller에 이용할 예정
    public List<Product> getProductList(){
        return this.productRepository.findProductByOrderByIdDesc();
    }

    // application.properties에서 이미지가 있는 실제 위치 가져오기
    @Value("${productImageLocation}")
    private String productImageLocation ;

    // 상품 id를 이용한 삭제
    // 1) 삭제할 상품이 데이터 베이스에 실제로 존재하는지 id를 통해 확인
    // 2) 운영체제에서 상품 삭제
    // 3) 상품 자체를 삭제

    // 1) 상품이 존재 하는지 확인
    public boolean deleteProduct(Long id){
        // 상품 가져오기 / 상품 id에 맞는 상품이 없으면 오류가 나니까
        // orElse()을 넣어서 ()안에 있는 내용을 가져오기 (null)을 가져옴
        Product product = productRepository.findById(id).orElse(null) ;

        // 상품id에 맞는 상품이 없으면
        if(product == null){
            return false ; // 없는 상품을 삭제할 수 없으니 상품 삭제 메소드는 실패해서 (false)를 반환함
        }

        // 상품id에 맞는 상품이 있으면
        // 2) 이미지가 있는 c드라이브 폴더(운영체제 내)에 가서 이미지 지우기
        String fileName = product.getImage() ;
        if(fileName != null && !fileName.isEmpty()){ // 다시 한 번 정상적인 파일이름인지 확인하기
            // application.properties에서 가져온 이미지 위치 연결하기
            File file = new File(productImageLocation + fileName) ;

            System.out.println("삭제될 파일 이름");
            // ex) C:\\upload\images\americano.jpg
            System.out.println(file.getAbsolutePath()); // 절대 경로 보여주기

            if(file.exists()){ // 해당 경로에! 삭제를 원하는 그 파일이 존재하는지 확인
                // 실제로 해당 경로의 파일을 삭제하고
                // 성공하면 true / 실패하면 false 반환함
                boolean deleted = file.delete() ;

                if(!deleted){ // 조건이 성립되려면 deleted가 false여야 !deleted가 true여서 메소드가 시작됨
                    System.out.println("이미지 삭제 실패");
                }
            }
        }
        // 3) 데이터 베이스에서 상품 삭제하기
        // 운영체제에서 이미지 파일을 삭제했으니 데이터 베이스에서도 삭제하기
        productRepository.deleteById(id);
        return true; // deleteProduct() 메소드 반환
    }

    /* 상품 등록 기능 */
    // 운영체제에 이미지 저장
    // 리액트가 보내주는 이미지의 Base64 인코딩 문자열을 변환하여 이미지로 만들고, 저장해주는 메소드입니다.
    // 운영체제에 이미지 저장하고 파일명 리턴하는 메소드
    private String saveProductImage(String base64Image) {
        // 데이터 베이스와 이미지 경로에 저장될 이미지의 이름
        // 현재 시각을 '년월일시분' 포맷으로 변환 (예: 202510171430)
        // formatter는 양식 데이터를 가지고 있음
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyyMMddHHmm");
        // formatter 양식에 맞춘 현재 시각 데이터를 formattedNow에 저장함
        String formattedNow = LocalDateTime.now().format(formatter);

        // 데이터 베이스와 이미지 경로에 저장될 이미지의 이름
        String imageFileName = "product_" + formattedNow + ".jpg";

        // String 클래스 공부 : endsWith(), split() 메소드
        // String 클래스의 split() 메소드는 2개를 쪼깨는 것인데 무조건 리턴값(결과값)은 배열로 생성이 됨
        // split() 소괄호 안에 분리하는 기준점을 적고 뒤에 [] 대괄호 안에 0은 전자 1은 후자라고 생각하고 적으면 됨
```

```java
        // 아직 운영체제에 실제 이미지 파일은 없음
        File imageFile = new File(productImageLocation + imageFileName);
        System.out.println("이미지 이름");
        System.out.println(imageFile.getName());

        // base64Image : JavaScript FileReader API에 만들어진 이미지의 문자열 데이터
        // 메소드 체이닝 : 점을 연속적으로 찍어서 메소드를 계속 호출하는 것
        // base64Image.split(",")[1] : 리액트에서 받아온 문자열 데이터의 값에서
        // ","을 기준으로 반으로 쪼개고 요소가 2개인 배열을 만들고 0(앞)과 1(뒤)중에 1을 선택함
        // (뒤가 우리가 필요한 이미지 데이터 텍스트임)
        // ex) data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA...
        // {data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAAUA...}
        // -> base64Image.split(",")[1] : iVBORw0KGgoAAAANSUhEUgAAAAUA...
        // 이렇게 가져온 이미지 데이터 텍스트를 다시 이미지 바이너리 바이트 데이터로 바꾸고
        // byte타입의 decodedImage 배열에 넣음
        byte[] decodedImage = Base64.getDecoder().decode(base64Image.split(",")[1]);

        // FileOutputStream는 바이트 파일을 처리해주는 자바의 Stream 클래스
        // new FileOutputStream(imageFile) : imageFile 경로에 빈 파일을 하나 생성 / 바이트 데이터 넣을 준비
        // 빈 파일의 객체에 이미지 바이너리 바이트 데이터를 넣어서 실제 이미지 파일로 생성
        // 파일 정보를 byte 단위로 변환하여 이미지를 복사합니다.
        try (FileOutputStream fos = new FileOutputStream(imageFile)) {
            fos.write(decodedImage);
            // 성공했으니 데이터 베이스에 기록할 파일명을 리턴함
            // -> insertProduct() 메소드에서 imageFileName 변수 사용이 가능해짐
            return imageFileName;
        } catch (Exception e) {
            throw new IllegalStateException("이미지 파일 저장 중 오류가 발생했습니다.");
        }
    }

    // 데이터 베이스에 새로운 상품 등록하기
    public Product insertProduct(Product product) {
        if (product.getImage() != null && product.getImage().startsWith("data:image")) {
            // saveProductImage() 메소드를 실행해서 운영체제에 이미지를 넣고
            // return받은 이미지 파일이름을 상품의 Image 컬럼에 넣기
            String imageFileName = saveProductImage(product.getImage());
            product.setImage(imageFileName);
        }

        product.setInputdate(LocalDate.now());
        System.out.println("서비스)상품 등록 정보");
        System.out.println(product);

        // save() 메소드는 CrudRepository에 포함되어 있습니다.
        return productRepository.save(product);
    }
}
```



#### \# ProductController.java 수정 (스프링) (05.상품.txt)
(controller - ProductController)
    public ResponseEntity<?> insert(@Valid @RequestBody Product product, BindingResult bindingResult) 메소드

- 코드 수정
```java
package com.coffee.controller;

import com.coffee.entity.Product;
import com.coffee.service.ProductService;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.BindingResult;
import org.springframework.validation.FieldError;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;


@RestController
@RequestMapping("/product")
public class ProductController {
    @Autowired
    private ProductService productService ;

    // 상품 보기 페이지
    @GetMapping("/list")
    public List<Product> list(){
        // 내림차순으로 Product테이블의 데이터를 정렬한 것들을 products에 넣고 프론트에 보냄(response)
        List<Product> products = this.productService.getProductList() ;
        return products ;
    }

    // 상품 삭제
    // {id}를 경로 변수라고 부르며, 가변 매개 변수라고 부름
    // 상품 50번 누르면 id가 50으로 바뀌듯 그때그때 상황에 따라 바뀜
    // 경로변수를 delete() 안에 넣고 @PathVariable이라는 경로변수 어노테이션도 작성하면
    // 매핑에 있는 경로 변수 id가 delete의 id로 들어옴
    @DeleteMapping("/delete/{id}")
    public ResponseEntity<String> delete(@PathVariable Long id){
        try {
            boolean isDeleted = this.productService.deleteProduct(id);

            if(isDeleted){ // isDeleted가 true면 삭제가 정상적으로 되었다는 뜻
                // 여기까지 왔다는 것은 에러없이 성공해서 내가 원하는 동작인 삭제가 된 것임
                return ResponseEntity.ok(id + "번 상품이 삭제되었습니다.");
            }else{ // 삭제를 할 상품 자체가 없는 상태
                return ResponseEntity.badRequest().body(id + "번 상품이 존재하지 않습니다.");
            }

        }catch (DataIntegrityViolationException err){// 데이터 베이스 무결성 위배되는 에러가 발생할때
            String message = "해당 상품은 장바구니에 포함이 되어 있거나, 이미 매출이 발생한 상품입니다. \n확인해 주세요." ;
            return ResponseEntity.internalServerError().body(message);

        }catch (Exception err){ // 두루뭉실한 예외처리
            return ResponseEntity.internalServerError().body("오류 발생 : " + err.getMessage());

        }
    }

    // 상품 등록
    @PostMapping("/insert")
    public ResponseEntity<?> insert(@Valid @RequestBody Product product, BindingResult bindingResult) {
        // bindingResult에 문제가 있으면
        // 다른 행동하지 않고 바로 에러 내용을 되돌림
        // 에러 내용은 엔티티에 적힌 오류 메시지 ("가격은 100원이상이어야 합니다." 같은것)임
        if (bindingResult.hasErrors()) {
            Map<String, String> errors = new HashMap<>();
            for (FieldError xx : bindingResult.getFieldErrors()) {
                errors.put(xx.getField(), xx.getDefaultMessage());
            }

            return new ResponseEntity<>(
                    Map.of(
                            "message", "상품 등록 유효성 검사에 문제가 있습니다.",
                            "errors", errors
                    ),
                    HttpStatus.BAD_REQUEST
            );
        }

        try { // 성공하면
            // 이미지를 운영체제에 저장하고 상품의 이미지 컬럼에 값을 넣고 데이터베이스에 상품을 저장함
            Product savedProduct = this.productService.insertProduct(product);

            if (savedProduct == null) {
                return ResponseEntity
                        .status(500)
                        .body(
                                Map.of(
                                        "message", "상품 등록에 실패하였습니다.",
                                        "error", "bad image file format"
                                )
                        );
            }

            return ResponseEntity.ok(
                    Map.of(
                            "message", "상품이 성공적으로 등록되었습니다.",
                            "image", savedProduct.getImage()
                    )
            );

        } catch (IllegalStateException err) { // 경로 또는 이미지 저장 문제
            return ResponseEntity
                    .status(500)
                    .body(
                            Map.of(
                                    "message", err.getMessage(),
                                    "error", "File Save Error"
                            )
                    );

        } catch (Exception err) { // 데이터 베이스 오류
            return ResponseEntity
                    .status(500)
                    .body(
                            Map.of(
                                    "message", err.getMessage(),
                                    "error", "Internet Server Error"
                            )
                    );

        }
    }
}
```



#### \# AppRoutes.tsx (리액트) (05.상품.txt)
(routes - AppRoutes)

- 코드 추가
```typescript
import ProductUpdateForm from './../pages/ProductUpdateForm';

	{/* ProductController의 @DeleteMapping("/delete/{id}")처럼 {id}를 경로 변수, 가변 매개 변수라고
    하는 것처럼 여기서 :기호도 id가 가변적인 변수라는 것을 의미하는 기호임
    실제로 주소창에는 :이 기호가 사라지고 순수한 id값만 오게됨 */}
    <Route path='/product/update/:id' element={<ProductUpdateForm user={user} />} />
```



#### \# ProductUpdateForm.tsx (리액트) (05.상품.txt)
(pages - ProductUpdateForm.tsx 생성)

- 코드 작성
```typescript
import axios from 'axios';
import customAxios from './../api/axiosInstance';

import { useEffect, useState } from 'react';
import { Alert, Button, Col, Container, Form, Row } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';
import { API_BASE_URL } from "../config/config";
// useParams 훅은 url에 들어 있는 동적 파라미터의 값을 챙길때 사용합니다.
import { useParams } from "react-router-dom";
import type { User } from '../types/User';

interface AppProps {
    user: User | null
}

function App({ user }: AppProps) {
    // 주소창(URL)에 파라미터 (id)이용하기
    // ProductList.tsx의 "navigate(`/product/update/${item.id}`);"와
    // AppRoutes.tsx의 "<Route path="/product/update/:id" element={<ProductUpdate />} />"로 설정해서 가능
    // 따라서 id는 선택한 item이자 사실상 product인 객체의 id요소임
    const { id } = useParams();
    console.log(`수정할 상품 번호 : ${id}`);

    const comment = '상품 수정';

    const initial_value = {
        name: '',
        price: '',
        category: '-',
        stock: '',
        image: '',
        description: ''
    }; // 상품 객체 정보

    // product는 백엔드에게 넘겨줄 상품 등록 정보를 담고 있는 객체
    const [product, setProduct] = useState(initial_value);

    // 오류 메시지 상태값 (서버 검증 오류용)
    const initialErrors = {
        name: '',
        price: '',
        category: '',
        stock: '',
        image: '',
        description: '',
        general: ''
    };

    // 오류 메시지 상태값 (서버 검증 오류용)
    const [errors, setErrors] = useState(initialErrors);

    const navigate = useNavigate();

    // id를 이용하여 기존에 입력한 상품 정보 가져오기
    useEffect(() => {
        if (!user || user.role !== 'ADMIN') { // 로그인하지 않았거나 관리자로 로그인하지 않으면
            alert(`${comment} 기능은(는) 관리자만 접근이 가능합니다.`);
            navigate('/'); // 메인 홈페이지로 돌아가기
        }

        // role이 ADMIN이면
        const url = `${API_BASE_URL}/product/update/${id}`;

        // 데이터 베이스에 저장되어 수정을 하려는 id의 객체를 가져옴 (get)
        customAxios
            .get(url)
            .then((response) => {
                setProduct(response.data);
            })
            .catch((error) => {
                console.log(`상품 ${id}번 오류 발생 : ${error}`);
                alert('해당 상품 정보를 읽어 오지 못했습니다.');
            });
        // 의존성 배열 : 해당 변수나 객체의 값이 바뀌면 새로 렌더링함
        // id : 수정하려는 상품이 바뀌면 새로 정보를 가져와야함 (백엔드에서 get으로)
        // user : role이 ADMIN이 아닌 사용자가 사용하려고 하면 막아야함
        // navigate : 상식적으로 navigate가 바뀔 수는 없지만 기본적으로
        // useEffect() 함수 외부에서 가져온 변수나 객체들을 의존성 배열에 넣어야해서 넣음
    }, [id, user, navigate]); // id 값이 변경될 때 마다 화면을 re-rendering 시켜야 합니다.


    // 폼 양식에서 어떠한 컨트롤의 값이 변경되었습니다.
    // ProductInsertFrom.tsx의 FileSelect() 함수와 동일
    const ControlChange = (
        event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>
    ) => {
        // event 객체는 change 이벤트를 발생시킨 폼 컨트롤입니다.
        const { name, value } = event.target;
        //console.log(`값이 바뀐 컨트롤 : ${name}, 값 : ${value}`);

        // 전개 연산자를 사용하여 이전 컨트롤의 값들도 보존하도록 합니다.
        setProduct({ ...product, [name]: value });
    }

    // ProductInsertFrom.tsx의 ControlChange() 함수와 동일
    const FileSelect = (
        event: React.ChangeEvent<HTMLInputElement>
    ) => {
        // 자바 스크립트는 모든 항목들을 배열로 취급하는 성질을 가지고 있습니다.
        const { name, files } = event.target;


        // null 및 길이 체크
        if (!files || files.length === 0) {
            return;
        }
        const file = files[0]; // type="file"로 작성한 1번째 항목

        // FileReader는 웹 브라우저에서 제공해주는 내장 객체로, 파일 읽기에 사용 가능합니다.
        // 자바 스크립트에서 파일을 읽고 이를 데이터로 처리하는 데 사용됩니다.
        const reader = new FileReader();

        // readAsDataURL() 함수는 file 객체를 문자열 형태(Base64 인코딩)로 반환하는 역할을 합니다.
        reader.readAsDataURL(file);

        // onloadend : 읽기 작업이 성공하면 자동으로 동작하는 이벤트 핸들러 함수
        reader.onloadend = () => {
            const result = reader.result;
            //console.log(result);

            // 해당 이미지는 Base64 인코딩 문자열 형식으로 state에 저장합니다.
            // 사용 예시 : data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA...
            setProduct({ ...product, [name]: result });
        };
    };

    // ProductInsertFrom.tsx의 SubmitAction() 함수와 url빼고 동일
    const SubmitAction = async (event: React.SyntheticEvent<HTMLFormElement>) => {
        event.preventDefault();

        if (product.category === "-") {
            alert('카테고리를 반드시 선택해 주셔야 합니다.');
            return; // 수정 중단
        }

        try {
            // 주의) 라우팅 규칙 때문에 ${id}를 제거하면 안됩니다.
            const url = `${API_BASE_URL}/product/update/${id}`;

            // Content-Type(Mime Type) : 문서의 종류가 어떠한 종류인지를 알려 주는 항목
            // 예시 : 'text/html', 'image/jpeg', 'application/json' 등등
            // 이 문서는 json 형식의 파일입니다.
            const config = {
                headers: { 'Content-Type': 'application/json' }
            };
            // put() 메소드는 리소스를 "수정"하고자 할 때 사용하는 메소드입니다.
            // 전체에서 일부를 바꿀 때 put() 메소드를 사용
            const response = await customAxios.put(url, product, config);

            console.log(`상품 수정 : [${response.data}]`);
            alert('상품이 성공적으로 수정 되었습니다.');

            // 상품 등록후 입력 컨트롤은 모두 초기화 되어야 합니다.
            setProduct(initial_value);
```

```typescript
            setErrors(initialErrors); // 오류 초기화

            // 등록이 이루어 지고 난 후 상품 목록 페이지로 이동합니다.
            navigate('/product/list');

        } catch (error: unknown) {
            if (axios.isAxiosError(error) && error.response) {
                // 백엔드에서 전달받은 오류 메시지를 저장
                setErrors((prev) => ({
                    ...prev,
                    ...error.response?.data?.errors,
                    general: error.response?.data?.message || '상품 수정 중 오류가 발생했습니다.'
                }));
            } else {
                setErrors((prev) => ({
                    ...prev,
                    general: '서버와의 통신 중 오류가 발생했습니다.'
                }));
            }
        };
    };

    return (
        <Container style={{ marginTop: '30px' }}>
            <h1>{comment}</h1>

            {/* 일반 오류 메시지 */}
            {errors.general && <Alert variant="danger">{errors.general}</Alert>}
            <Form onSubmit={SubmitAction}>

                {/* 이름 */}
                <Form.Group as={Row} className="mb-3" controlId="formName">
                    <Form.Label column sm={2}>이름</Form.Label>
                    <Col sm={10}>
                        <Form.Control
                            type="text"
                            placeholder="이름을(를) 입력해 주세요."
                            name="name"
                            value={product.name || ''}
                            onChange={ControlChange}
                            isInvalid={!!errors.name}
                        />
                        <Form.Control.Feedback type="invalid">{errors.name}</Form.Control.Feedback>
                    </Col>
                </Form.Group>

                {/* 가격 */}
                <Form.Group as={Row} className="mb-3" controlId="formPrice">
                    <Form.Label column sm={2}>가격</Form.Label>
                    <Col sm={10}>
                        <Form.Control
                            type="text"
                            placeholder="가격을(를) 입력해 주세요."
                            name="price"
                            value={product.price || ''}
                            onChange={ControlChange}
                            isInvalid={!!errors.price}
                        />
                        <Form.Control.Feedback type="invalid">{errors.price}</Form.Control.Feedback>
                    </Col>
                </Form.Group>

                {/* 카테고리 */}
                <Form.Group as={Row} className="mb-3" controlId="formCategory">
                    <Form.Label column sm={2}>카테고리</Form.Label>
                    <Col sm={10}>
                        <Form.Select
                            name="category"
                            value={product.category || ''}
                            onChange={ControlChange}
                            isInvalid={!!errors.category}
                        >
                            <option value="-">-- 카테고리를 선택해 주세요.</option>
                            <option value="BREAD">빵</option>
                            <option value="BEVERAGE">음료수</option>
                            <option value="CAKE">케이크</option>
                        </Form.Select>
                        <Form.Control.Feedback type="invalid">{errors.category}</Form.Control.Feedback>
                    </Col>
                </Form.Group>

                {/* 재고 */}
                <Form.Group as={Row} className="mb-3" controlId="formStock">
                    <Form.Label column sm={2}>재고</Form.Label>
                    <Col sm={10}>
                        <Form.Control
                            type="text"
                            placeholder="재고을(를) 입력해 주세요."
                            name="stock"
                            value={product.stock || ''}
                            onChange={ControlChange}
                            isInvalid={!!errors.stock}
                        />
                        <Form.Control.Feedback type="invalid">{errors.stock}</Form.Control.Feedback>
                    </Col>
                </Form.Group>

                {/* 이미지 */}
                <Form.Group as={Row} className="mb-3" controlId="formImage">
                    <Form.Label column sm={2}>이미지</Form.Label>
                    <Col sm={10}>
                        <Form.Control
                            type="file"
                            name="image"
                            onChange={FileSelect}
                            isInvalid={!!errors.image}
                        />
                        <Form.Control.Feedback type="invalid">{errors.image}</Form.Control.Feedback>
                    </Col>
                </Form.Group>

                {/* 상품 설명 */}
                <Form.Group as={Row} className="mb-3" controlId="formDescription">
                    <Form.Label column sm={2}>상품 설명</Form.Label>
                    <Col sm={10}>
                        <Form.Control
                            type="text"
                            placeholder="상품 설명을(를) 입력해 주세요."
                            name="description"
                            value={product.description || ''}
                            onChange={ControlChange}
                            isInvalid={!!errors.description}
                        />
                        <Form.Control.Feedback type="invalid">{errors.description}</Form.Control.Feedback>
                    </Col>
                </Form.Group>

                <Button variant='primary' type='submit' size='lg'>{comment}</Button>
            </Form>
        </Container >
    );
}

export default App;
```



#### \# ProductService.java (스프링) (05.상품.txt)
(service - ProductService)
프론트의 ProductUpdateForm.tsx의 get 요청에 대한 응답을 위한 코드 작성

- 코드 추가
```java
/* 상품 수정 기능 */
// 상품 수정하기 get 방식 시작 (id를 이용해서 특정 상품 정보 가져오기)
public Product getProductById(Long id) {
	// Optional : 해당 상품이 있을 수도 있지만, 경우에 따라서 없을 수도 있습니다.
	// findById()는 무조건 결과를 Optional 타입으로 돌려줌
	// id에 해당하는 데이터를 가져와서 product에 넣어주는데 오류를 방지하기 위해 Optional 타입으로 줌
	Optional<Product> product = this.productRepository.findById(id);

	// 의미 있는 데이터이면 그냥 넘기고, 그렇지 않으면 null을 반환해 줍니다.
	return product.orElse(null);
}
```



#### \# ProductController.java (스프링) (05.상품.txt)
(controller - ProductController)
프론트의 ProductUpdateForm.tsx의 get 요청에 대한 응답을 위한 코드 작성

- 코드 추가
```java
// 상품 수정 페이지 get 방식
// 프론트 앤드의 상품 수정 페이지에서 요청이 들어 왔습니다.
@GetMapping("/update/{id}") // 상품의 id 정보를 이용하여 해당 상품 Bean 객체를 반환해 줍니다.
public ResponseEntity<Product> getUpdate(@PathVariable Long id){
	System.out.println("수정할 상품 번호 : " + id);

	// id에 해당하는 상품 정보 가져오기
	Product product = this.productService.getProductById(id) ;

	if(product == null){ // 상품이 없으면 404 응답과 함께 null을 반환
		return ResponseEntity.status(HttpStatus.NOT_FOUND).body(null);

	}else{ // 해당 상품의 정보와 함께, 성공(200) 메시지를 반환합니다.
		return ResponseEntity.ok(product);
	}
}
```




#### \# ProductService.java (스프링) (05.상품.txt)
(service - ProductService)
프론트의 ProductUpdateForm.tsx의 put 요청에 대한 응답을 위한 코드 작성

- 코드 추가
```java
// 상품 수정하기 put 방식 시작
public Optional<Product> findById(Long id) {
	return productRepository.findById(id);
}

// 이전 이미지 파일을 삭제하는 메소드
private void deleteOldImage(String oldImageFileName) {
	if (oldImageFileName == null || oldImageFileName.isBlank()) {
		return;
	}

	File oldImageFile = new File(productImageLocation + oldImageFileName);

	if (oldImageFile.exists()) { // 예전파일이 운영체제에 존재하면 삭제함
		boolean deleted = oldImageFile.delete();
		if (!deleted) {
			System.err.println("기존 이미지 삭제 실패 : " + oldImageFileName);
		}
	}
}

// Product 수정
// 저장된 상품 정보를 들고와서 새로 수정된 상품 정보로 대체함
public Product updateProduct(Product savedProduct, Product updatedProduct) {
	savedProduct.setName(updatedProduct.getName());
	savedProduct.setPrice(updatedProduct.getPrice());
	savedProduct.setCategory(updatedProduct.getCategory());
	savedProduct.setStock(updatedProduct.getStock());
	savedProduct.setDescription(updatedProduct.getDescription());

	if (updatedProduct.getImage() != null && updatedProduct.getImage().startsWith("data:image")) {
		// 저장된 상품 정보의 이미지 파일 삭제
		deleteOldImage(savedProduct.getImage());
		// saveProductImage() : 운영체제에 이미지 저장하고 파일명 리턴하는 메소드를 재사용함
		String imageFileName = saveProductImage(updatedProduct.getImage());
		savedProduct.setImage(imageFileName);
	}

	// 새로운 정보를 사진 상품을 데이터 베이스에 다시 저장함
	return productRepository.save(savedProduct);
}
```





#### \# ProductController.java (스프링) (05.상품.txt)
(controller - ProductController)
프론트의 ProductUpdateForm.tsx의 put 요청에 대한 응답을 위한 코드 작성

- 코드 추가
```java
// 상품 수정 페이지 get 방식
@PutMapping("/update/{id}")
public ResponseEntity<?> putUpdate(@PathVariable Long id,
								   @Valid @RequestBody Product updatedProduct,
								   BindingResult bindingResult) {
	// 1. 유효성 검사
	if (bindingResult.hasErrors()) {
		Map<String, String> errors = new HashMap<>();
		for (FieldError error : bindingResult.getFieldErrors()) {
			errors.put(error.getField(), error.getDefaultMessage());
		}
		return new ResponseEntity<>(
				Map.of(
						"message", "상품 수정 유효성 검사에 문제가 있습니다.",
						"errors", errors
				),
				HttpStatus.BAD_REQUEST
		);
	}

	// 2. 상품 조회
	Optional<Product> findProduct = productService.findById(id);

	if (findProduct.isEmpty()) {
		// ResponseEntity.notFound().build(): 지울 대상이 없으므로 깔끔하게
		// HTTP 상태 코드 404 Not Found 봉투만 빌드(build())해서 리액트에게 던짐
		return ResponseEntity.notFound().build();
	}

	try { // findProduct의 타입이 Optional이여서 굳이 get()을 하고 Product타입의 변수에 다시 넣음
		Product savedProduct = findProduct.get();
		// 새로운 Product의 정보를 기존에 저장된 Product정보에 덮어쓰기함
		productService.updateProduct(savedProduct, updatedProduct);

		// 프론트에는 성공했다는 메시지를 보냄
		return ResponseEntity.ok(Map.of("message", "상품 수정 성공"));

	} catch (Exception err) {
		return ResponseEntity
				.status(HttpStatus.INTERNAL_SERVER_ERROR)
				.body(Map.of(
						"message", err.getMessage(),
						"error", "상품 수정 실패"
				));
	}
}
```



#### \# 제05장-07. 상세 보기 (05.상품.txt)
#### \# 상품 목록 페이지 (05.상품.txt)
#### \# ProductList.tsx (리액트) (05.상품.txt)
(pages - ProductList.tsx)

- 코드 추가 (Card 태그에 onClick 속성 추가)
```typescript
<Card className="h-100"
	onClick={() => navigate(`/product/detail/${item.id}`)} // 상세보기로 이동하기 위한 속성 추가
	style={{ cursor: 'pointer' }}>
```



#### \# AppRoutes.tsx (리액트) (05.상품.txt)
(routes - AppRoutes.tsx)

- 코드 추가
```typescript
import ProductDetail from './../pages/ProductDetail';

<Route path='/product/detail/:id' element={<ProductDetail user={user} />} />
```



#### \# 상품 상세 페이지 작성 (05.상품.txt)
#### \# ProductDetail.tsx (리액트) (05.상품.txt)
(pages - ProductDetail.tsx 생성)
(ProductDetail01.txt 파일 참조)

- 코드 작성
/\*
상품 상세 보기
전체 화면을 좌우측을 1대2로 분리합니다.
왼쪽은 상품의 이미지 정보, 오른쪽은 상품의 정보 및 `장바구니`와 `주문하기` 버튼을 만듭니다.
```typescript
*/

import customAxios from "./../api/axiosInstance";
import { useEffect, useState } from "react";
import { Button, Card, Col, Container, Row, Table } from "react-bootstrap";
import { useNavigate, useParams } from "react-router-dom";
import { API_BASE_URL } from "../config/config";
import type { Product } from "../types/Product";
import type { User } from "../types/User";
```

interface AppProps { // 사용자 권한을 나타내려고 쓰는 프롭스 (customAxios와 세트 느낌)
```typescript
    user: User | null
}

function App({ user }: AppProps) {
    // useParams() : ProductList의 ${item.id}를 통해 받은 AppRoutes의 :id의 키와 값을 가진 객체
    const { id } = useParams(); // id 파라미터 챙기기
    const [product, setProduct] = useState<Product | null>(null); // 백엔드에서 넘어온 상품 정보넣을 state 객체

    // 로딩 상태를 의미하는 state로, 값이 true이면 현재 로딩 중입니다.
    const [loading, setLoading] = useState(true);

    const navigate = useNavigate();

    // 파라미터 id가 갱신이 되면 화면을 다시 rendering 시킵니다.
    useEffect(() => {
        if (!user) { // 로그인하지 않아서 user의 데이터가 없을때
            alert('로그인이 필요한 서비스입니다.');
            navigate('/member/login');
            return;
        }

        const url = `${API_BASE_URL}/product/detail/${id}`;

        // 백엔드에서 id에 해당하는 데이터를 가져옴
        customAxios
            .get(url)
            .then((response) => {
                setProduct(response.data); // 백엔드에서 가져온 데이터를 Product state 객체에 넣음
                setLoading(false); // 상품 정보를 읽어 왔습니다. (false = 로딩이 완료됨)
            })
            .catch((error) => {
                console.log(error);

                if (error.response && error.response.status === 401) { // 401(UnAuthrized)
                    alert('로그인이 필요한 서비스입니다.');
                    navigate('/member/login'); // 로그인 페이지로 리다이렉트

                } else {
                    alert('상품 정보를 불러 오는 중에 오류가 발생하였습니다.');
                    navigate(-1); // 이전 페이지로 이동하기
                }
            });
    }, [id, user, navigate]);

    // 아직 backend에서 읽어 오지 못한 경우를 대비한 코딩입니다.
    if (loading === true) { // true = 로딩중이라는 뜻
        return (
            <Container className="my-4 text-center">
                <h3>
                    상품 정보를 읽어 오는 중입니다.
                </h3>
            </Container>
        );
    }

    // 상품에 대한 정보가 없는 경우를 대비한 코딩입니다.
    if (!product) {
        return (
            <Container className="my-4 text-center">
                <h3>
                    상품 정보를 찾을 수 없습니다.
                </h3>
            </Container>
        );
    }

    return (
        <Container className="my-4">
            <Card>
                <Row className="g-0">
                    {/* 좌측 상품 이미지 */}
                    <Col md={4}>
                        <Card.Img
                            variant="top"
                            src={`${API_BASE_URL}/images/${product.image}`}
                            alt={`${product.name}`}
                            style={{ width: '100%', height: '400px' }}
                        />
                    </Col>
                    {/* 우측 상품 정보 및 구매 관련 버튼 */}
                    <Col md={8}>
                        <Card.Body>
                            <Card.Title className="fd-3">
                                <h3>{product.name}</h3>
                            </Card.Title>
                            <Table striped>
                                <tbody>
                                    <tr>
                                        <td className="text-center">가격</td>
                                        <td>{product.price.toLocaleString()}원</td>
                                    </tr>
                                    <tr>
                                        <td className="text-center">카테고리</td>
                                        <td>{product.category}</td>
                                    </tr>
                                    <tr>
                                        <td className="text-center">재고</td>
                                        <td>{product.stock.toLocaleString()}개</td>
                                    </tr>
                                    <tr>
                                        <td className="text-center">설명</td>
                                        <td>{product.description}</td>
                                    </tr>
                                    <tr>
                                        <td className="text-center">등록일자</td>
                                        <td>{product.inputdate}</td>
                                    </tr>
                                </tbody>
                            </Table>


                            {/* 버튼(이전 목록) */}
                            <div className="d-flex justify-content-center mt-3">
                                <Button variant="primary" className="me-3 px-4" href="/product/list">
                                    이전 목록
                                </Button>
                            </div>
                        </Card.Body>
                    </Col>
                </Row>
            </Card>
        </Container>
    );
}

export default App;
```



#### \# ProductController.java (스프링) (05.상품.txt)
(controller - ProductController)
ProductDetail.tsx의 get매핑에 맞는 코드 작성

- 코드 추가
```java
// 상품 상세 페이지 get매핑 요청에 대한 응답을 위한 코드
@GetMapping("/detail/{id}")
public ResponseEntity<Product> detail(@PathVariable Long id){
	// Optional 타입인 product를 다시 Product 타입으로 선언
	Product product = productService.getProductById(id) ;

	if (product == null){ // product가 존재하지 않으면 오류코드를 만들어서 프론트에 응답함
		return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
	}else{ // 정상적인 데이터를 가진 product라면 프론트에 오류 없다는 상태 코드와 함께 응답함
		return ResponseEntity.ok(product);
	}
}
```



#### \# 제06장-01. 장바구니 공통 사항 (스프링) (06.장바구니.txt)
#### \# 카트(Cart) (스프링) (06.장바구니.txt)
(entity - Cart 클래스 생성)

- 코드 작성
```java
package com.coffee.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import java.util.List;

@Getter @Setter @ToString
@Entity
@Table(name = "carts")
public class Cart {
    @Id // 기본키(pk) 설정
    @GeneratedValue(strategy = GenerationType.AUTO) // 숫자 자동 생성
    @Column(name = "cart_id") // 실제 데이터 베이스 컬럼명은 cart_id
    private Long id ;

    // 연관 관계 매핑 (Entity간의 연관 관계 서술)
    // fetch : 데이터 베이스에서 데이터를 가져온다는 뜻
    // (우리는 axios를 사용하지만 자바의 기본 기능이 fetch)
    // FetchType.LAZY : 즉시로딩 말고 지연로딩을 의미함 (진짜 필요할때 - member에 접근할때 가져오기)
    // 부모자식 참조관계에서 일대일, 일대다, 다대일은 중요하지 않음
    // 어떤 관계든 자식이 부모의 PK를 FK로 가진다
    // 해당클래스(엔티티)to어노테이션이_붙은_컬럼 : to의 앞에가 해당 클래스고 to의 뒤에가 매핑된 엔티티(테이블)
    @OneToOne(fetch = FetchType.LAZY)
    // @JoinColumn은 자식 테이블에 적어야 하는 어노테이션임 (조인 어노테이션) (외래키 정의함)
    @JoinColumn(name = "member_id") // fk이름은 members테이블의 pk 컬럼명과 동일하게 적어야 함 (관례임)
    private Member member ; // carts테이블에 member_id라는 이름의 members테이블의 fk인 컬럼이 생성됨

    // 여기에는 @JoinColumn을 적지 않음. 왜? (부모 테이블이여서)
    // 카트안에는 카트상품이 여러개 담길 수 있어서 컬렉션(중에서도 List)로 변수 생성해야 함
    // 카트에는 여러 개의 '카트 상품'들이 담겨야 하므로 List가 좋습니다
    // mappedBy에는 자식 테이블의 적힌 부모 테이블인 클래스의 이름으로 된 맴버변수를 적음
    // (자식 테이블(엔티티)인 CartProduct에 있는 fk로 설정된 cart 맴버변수)

    // * 해당 변수의 값은 JPA가 Cart에 연결된 CartProduct들을 cart_products 테이블에서 찾아서
    // * List<CartProduct> cartProducts의 값에 채워 넣어줌
    // -> 한마디로 cart_products 테이블에서 cart_id 컬럼의 값이 이 Cart타입의 객체의 id와 같으면
    // 그 데이터들을 가지고 와서 이 Java 변수인 List<CartProduct> cartProducts에 넣음
    // FetchType.LAZY여서 실제로 Cart.getCartProducts()로 호출을 하는 순간 조회해서 넣어줌
    @OneToMany(mappedBy = "cart", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private List<CartProduct> cartProducts ;
}
```



#### \# 카트 상품(CartProduct) (스프링) (06.장바구니.txt)
(entity - CartProduct 클래스 생성)

- 코드 작성
```java
package com.coffee.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@ToString
@Entity
@Table(name = "cart_products")
public class CartProduct {
    @Id // 기본키(pk) 설정
    @GeneratedValue(strategy = GenerationType.AUTO) // 숫자 자동 생성
    @Column(name = "cart_product_id") // 실제 데이터 베이스 컬럼명은 cart_product_id
    private Long id;

    // 부모자식 참조관계에서 일대일, 일대다, 다대일은 중요하지 않음
    // 어떤 관계든 자식이 부모의 PK를 FK로(@JoinColumn) 가진다
    @ManyToOne(fetch = FetchType.LAZY)
    // @JoinColumn은 자식 테이블에 적어야 하는 어노테이션임 (조인 어노테이션)
    @JoinColumn(name = "cart_id") // carts테이블의 pk 컬럼명과 동일하게 적어야 함 (관례임)
    private Cart cart; // cart_products테이블에 cart_id라는 이름의 carts테이블의 fk인 컬럼이 생성됨

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "product_id", nullable = false)
    private Product product ;

    // 카트에 담길 상품들의 갯수
    @Column(nullable = false)
    private int quantity ;
}
```



#### \# 상품 상세 보기 페이지(ProductDetail.tsx) (리액트) (06.장바구니.txt)
1) quantity 스테이트 신규 선언(주의 : useEffect() 코딩 이전에 작성)
2) QuantityChange 이벤트 핸들러 함수(주의 : useEffect() 코딩 이전에 작성)
3) 구매 수량 관련 \<Form.Control\>의 onChange={QuantityChange} 속성과 연동시킵니다.
4)  addToCart 함수를 작성합니다.
5) \<Button\> '장바구니'의 onClick 속성에 addToCart 함수와 연동하는 코드를 작성합니다.

- 코드 추가
/\*
상품 상세 보기
전체 화면을 좌우측을 1대2로 분리합니다.
왼쪽은 상품의 이미지 정보, 오른쪽은 상품의 정보 및 `장바구니`와 `주문하기` 버튼을 만듭니다.
```typescript
*/

import customAxios from "./../api/axiosInstance";
import { useEffect, useState } from "react";
import { Button, Card, Col, Container, Form, Row, Table } from "react-bootstrap";
import { useNavigate, useParams } from "react-router-dom";
import { API_BASE_URL } from "../config/config";
import type { Product } from "../types/Product";
import type { User } from "../types/User";
import axios from "axios";
```

interface AppProps { // 사용자 권한을 나타내려고 쓰는 프롭스 (customAxios와 세트 느낌)
```typescript
    user: User | null
}

function App({ user }: AppProps) {
    // useParams() : ProductList의 ${item.id}를 통해 받은 AppRoutes의 :id의 키와 값을 가진 객체
    const { id } = useParams(); // id 파라미터 챙기기
    const [product, setProduct] = useState<Product | null>(null); // 백엔드에서 넘어온 상품 정보넣을 state 객체

    // 로딩 상태를 의미하는 state로, 값이 true이면 현재 로딩 중입니다.
    const [loading, setLoading] = useState(true);

    const navigate = useNavigate();

    // 수량 state변수
    // (주의 : useEffect() 코딩 이전에 작성) : Hook은 항상 컴포넌트 최상단에서 같은 순서로 호출되어야 함
    const [quantity, setQuantity] = useState(0);

    // 2) QuantityChange 이벤트 핸들러 함수(주의 : useEffect() 코딩 이전에 작성)
    const QuantityChange = (
        event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>
    ) => { // parseInt : int 타입으로 변환하는 함수
        const newValue = parseInt(event.target.value);
        setQuantity(newValue);
    };


    // 파라미터 id가 갱신이 되면 화면을 다시 rendering 시킵니다.
    useEffect(() => {
        if (!user) { // 로그인하지 않아서 user의 데이터가 없을때
            alert('로그인이 필요한 서비스입니다.');
            navigate('/member/login');
            return;
        }

        const url = `${API_BASE_URL}/product/detail/${id}`;

        // 백엔드에서 id에 해당하는 데이터를 가져옴
        customAxios
            .get(url)
            .then((response) => {
                setProduct(response.data); // 백엔드에서 가져온 데이터를 Product state 객체에 넣음
                setLoading(false); // 상품 정보를 읽어 왔습니다. (false = 로딩이 완료됨)
            })
            .catch((error) => {
                console.log(error);

                if (error.response && error.response.status === 401) { // 401(UnAuthrized)
                    alert('로그인이 필요한 서비스입니다.');
                    navigate('/member/login'); // 로그인 페이지로 리다이렉트

                } else {
                    alert('상품 정보를 불러 오는 중에 오류가 발생하였습니다.');
                    navigate(-1); // 이전 페이지로 이동하기
                }
            });
    }, [id, user, navigate]);

    // 아직 backend에서 읽어 오지 못한 경우를 대비한 코딩입니다.
    if (loading === true) { // true = 로딩중이라는 뜻
        return (
            <Container className="my-4 text-center">
                <h3>
                    상품 정보를 읽어 오는 중입니다.
                </h3>
            </Container>
        );
    }



    // 상품에 대한 정보가 없는 경우를 대비한 코딩입니다.
    if (!product) {
        return (
            <Container className="my-4 text-center">
                <h3>
                    상품 정보를 찾을 수 없습니다.
                </h3>
            </Container>
        );
    }

    // addToCart 함수를 작성
    const addToCart = async () => {
        if (!user) {
            alert('로그인이 필요합니다.');
            navigate('/member/login');
            return;
        }

        if (!product) return;

        if (quantity < 1) { // 최소수량 경고 문구 (min으로 설정해도 직접 숫자를 입력하면 0이 입력이 됨)
            alert(`구매 수량은 1개 이상이어야 합니다.`);
            return;
        }
        //alert(`${product.name} ${quantity} 개를 장바구니에 담기`);

        // memberId: user.id
        try {
            const parameters = {
                // 백엔드에서 일처리를 하는데 꼭 필요한 데이터를 파라미터로 보냄
                // 백엔드에서는 이 파라미터와 "이름"이 똑같은 맴버변수를 가진 dto를 만들어야 함
                // memberId: user.id : 누가 카트에 추가했는지는 보내지 않음
                // 이것은 백엔드에서 dto로 설정은 해놓고 controller에서 받을때는 dto의 변수의 값이
                // 프론트엔드에서 받은 값이 없어서 null이지만 데이터 베이스에 넣을때 service를 거치면서
                // 채워지게 됨 (따라서 백엔드의 dto에는 memberId 변수가 있기는 함)
                productId: product.id,
                quantity: quantity
            };

            const url = `/cart/insert`;
            const response = await customAxios.post(url, parameters);


            alert(response.data);
            navigate('/product/list'); // 상품 목록 페이지로 이동

        } catch (error) {
            console.log('오류 발생 : ' + error);

            if (axios.isAxiosError(error)) {
                console.log(error.response?.data);
                alert('장바구니 추가 실패');
            } else {
                console.log('예상치 못한 오류', error);
            }
        }
    }

    return (
        <Container className="my-4">
            <Card>
                <Row className="g-0">
                    {/* 좌측 상품 이미지 */}
                    <Col md={4}>
                        <Card.Img
                            variant="top"
                            src={`${API_BASE_URL}/images/${product.image}`}
                            alt={`${product.name}`}
                            style={{ width: '100%', height: '400px' }}
                        />
                    </Col>
                    {/* 우측 상품 정보 및 구매 관련 버튼 */}
                    <Col md={8}>
                        <Card.Body>
                            <Card.Title className="fd-3">
                                <h3>{product.name}</h3>
                            </Card.Title>
                            <Table striped>
                                <tbody>
                                    <tr>
                                        <td className="text-center">가격</td>
                                        <td>{product.price.toLocaleString()}원</td>
                                    </tr>
                                    <tr>
                                        <td className="text-center">카테고리</td>
                                        <td>{product.category}</td>
                                    </tr>
                                    <tr>
                                        <td className="text-center">재고</td>
                                        <td>{product.stock.toLocaleString()}개</td>
                                    </tr>
                                    <tr>
                                        <td className="text-center">설명</td>
                                        <td>{product.description}</td>
                                    </tr>
                                    <tr>
                                        <td className="text-center">등록일자</td>
                                        <td>{product.inputdate}</td>
                                    </tr>
                                </tbody>
                            </Table>

                            {/* 구매 수량 입력란 */}
                            {/* as={Row}는 렌더링시 기본 값인 <div> 말고 Row로 렌더링하도록 해줌 */}
                            <Form.Group as={Row} className="mb-3 align-items-center">
                                <Col xs={3} className="text-center">
                                    <strong>구매 수량</strong>
                                </Col>
                                <Col xs={5}>
                                    {/* 구매 수량 최소 1이상으로 설정 / user 모드에 따라서 분기 */}
                                    <Form.Control
                                        type="number"
                                        // 최솟값
                                        min="1"
                                        // 로그인이 되어있지 않으면 (!user) 비활성화됨
                                        disabled={!user}
                                        value={quantity}
                                        onChange={QuantityChange}
                                    />
                                </Col>
                            </Form.Group>


                            {/* 버튼(이전 목록, 장바구니, 주문하기) */}
                            <div className="d-flex justify-content-center mt-3">
                                <Button variant="primary" className="me-3 px-4" href="/product/list">
                                    이전 목록
                                </Button>
                                {/* 장바구니 버튼 */}
                                <Button variant="success" className="me-3 px-4"
                                    onClick={() => {
                                        // 로그인 하지 않았을때 누르면 alert 후 로그인 페이지로 이동
                                        if (!user) {
                                            alert('로그인이 필요한 서비스입니다');
                                            return navigate('/member/login');
                                        } else { // 로그인 했을때는 addToCart() 함수 실행
                                            addToCart();
                                        }
                                    }}
                                >
                                    장바구니
                                </Button>
                                <Button variant="danger" className="me-3 px-4"
                                // onClick={`일단오류무시`}
                                >
                                    주문하기
                                </Button>
                            </div>
                        </Card.Body>
                    </Col>
                </Row>
            </Card>
        </Container>
    );
}

export default App;
```



#### \# 카트 상품 DTO (스프링) (06.장바구니.txt)
(dto 폴더에 CartProductDto 클래스 생성)
    CartProductDto 신규 작성

프론트엔드에서 백엔드로 보낼때 주는 파라미터의 key와 변수명이 같은 맴버 변수를 작성해야함

- 코드 작성
```java
package com.coffee.dto;

import lombok.Getter;
import lombok.Setter;

// -> dto는 프론트엔드에서 받는 그릇이면서 service에 넘길 그릇이여서
// controller로 들어올때는 memberId의 값이 없어서 null이지만 결국 데이터베이스로 이동해야하기때문에
// 일단 controller 단계에서는 null값이지만 service를 거쳐 데이터 베이스로 이동될때는 memberId를 채워서 넣기때문에
// 일단 변수를 만들어 놓은 것임
// -> 따라서 프론트엔드에서 받을 파라미터와 반드시 100% 같은 갯수의 변수가 있어야 하는 것은 아니다.
// but! 프론트에서 줄 파라미터를 받으려면 변수명이 같아야 하긴 함
// * 변수명은 같아야 하고 /  변수 갯수는 달라도 됨 *

// 근데 사실상 Member findByEmail (String email); 이 함수로 인해서 email을 알면
// 그 email인 member의 id를 알 수 있어서 굳이 dto에 필요는 없을듯
@Getter @Setter
public class CartProductDto {
    private Long memberId ;
    private Long productId ;
    private int quantity ;
}
```



#### \# 서비스(MemberService) (스프링) (06.장바구니.txt)
(service - MemberService)
가장 밑에 추가함

    public Optional<Member> findMemberById(Long memberId) 메소드

- 코드 추가
```java
// 프론트의 ProductDetail.tsx의 addToCart() 함수에 의해? 필요함
// Optional은 값이 있을 수도 없을 수도 있음을 표현한 타입
// Optional 타입으로 되어있는 데이터는 사용할때 반드시 꺼내야함
// Member member = findMemberById(id).orElse(null); 이런식으로 꺼내던지
// Member member = findMemberById(id).orElseThrow(() -> new RuntimeException("회원 없음")); 이런식으로 함
// Member.id로 데이터 베이스에서 Member의 데이터를 찾는 함수
public Optional<Member> findMemberById(Long memberId) {
	return this.memberRepository.findById(memberId);
}
```



#### \# 서비스(ProductService) (스프링) (06.장바구니.txt)
(service - ProductService)
    public Optional<Product> findProductById(Long productId) 메소드

- 코드 작성
```java
// 프론트의 ProductDetail.tsx의 addToCart() 함수에 의해? 필요함
// Optional은 값이 있을 수도 없을 수도 있음을 표현한 타입
// Optional 타입으로 되어있는 데이터는 사용할때 반드시 꺼내야함
// Product product = findProductById(id).orElse(null); 이런식으로 꺼내던지
// Product product = findProductById(id).orElseThrow(() -> new RuntimeException("회원 없음")); 이런식으로 함
// Product.id로 데이터 베이스에서 Product의 데이터를 찾는 함수
public Optional<Product> findProductById(Long productId) {
	return productRepository.findById(productId);
}
```



#### \# 리포지터리(CartRepository) (스프링) (06.장바구니.txt)
(repository - CartRepository 인터페이스 생성)
   신규 작성
   Optional\<Cart\> findByMember(Member member) 메소드

- 코드 작성
```java
package com.coffee.repository;

import com.coffee.entity.Cart;
import com.coffee.entity.Member;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface CartRepository extends JpaRepository<Cart, Long> {
    // 이 member가 가진 카트 정보가 있는지 조회하는 메소드 (카트를 가지고 있는지 없는지)
    // SELECT * FROM carts WHERE member_id = ?;
    // carts 테이블의 member_id 컬럼이 ? 인 데이터를 다 조회해라
    // Java에서는 Member member 객체로 찾지만
    // Cart 엔티티를 보면 @JoinColumn(name = "member_id")으로 되어 있어서
    // JPA에 의해 매개변수 Member타입인 member를 자동으로 member_id로 변환해서 넣어주는 것처럼
    // DB에는 적용이 됨
    Optional<Cart> findByMember(Member member);
}
```



#### \# 리포지터리(CartProductRepository) : 신규 작성 (스프링) (06.장바구니.txt)
(repository - CartProductRepository 인터페이스 생성)

- 코드 작성
```java
package com.coffee.repository;

import com.coffee.entity.CartProduct;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CartProductRepository extends JpaRepository<CartProduct, Long> {
}
```




#### \# 서비스(CartProductService) 신규 작성 (스프링) (06.장바구니.txt)
(service - CartProductService 클래스 생성)
    public void saveCartProduct(CartProduct cp) 메소드

- 코드 작성
```java
package com.coffee.service;

import com.coffee.entity.CartProduct;
import com.coffee.repository.CartProductRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service // Service 객체 의미
@RequiredArgsConstructor
public class CartProductService {
    private final CartProductRepository cartProductRepository ;

    // 매개변수로 CartProduct타입의 cp를 하나 입력 받아서 cart_products 테이블에 저장
    public void saveCartProduct(CartProduct cp){
        this.cartProductRepository.save(cp);
    }
}
```



#### \# 서비스(CartService) 신규 작성 (스프링) (06.장바구니.txt)
(service - CartService 클래스 생성)
```java
    private final CartRepository cartRepository ;
    private final MemberService memberService ;
    private final ProductService productService ;
    private final CartProductService cartProductService ;
    private final MemberRepository memberRepository;
    private final ProductRepository productRepository;

    public Cart saveCart(Cart cart)
    private CartProduct findExistingProduct(Cart cart, Product product)
    public String addProductToCart(CartProductDto dto, String email)
```

- 코드 작성
```java
package com.coffee.service;

import com.coffee.dto.CartProductDto;
import com.coffee.entity.Cart;
import com.coffee.entity.CartProduct;
import com.coffee.entity.Member;
import com.coffee.entity.Product;
import com.coffee.repository.CartRepository;
import com.coffee.repository.MemberRepository;
import com.coffee.repository.ProductRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@RequiredArgsConstructor
public class CartService { // 필요한 변수들 생성
    private final CartRepository cartRepository ;
    private final MemberService memberService ;
    private final ProductService productService ;
    private final CartProductService cartProductService ;
    private final MemberRepository memberRepository ;
    private final ProductRepository productRepository ;

    // carts 테이블에 cart 객체 저장하는 함수 (+ 저장한 객체를 Cart 타입으로 반환도 함)
    public Cart saveCart(Cart cart){
        return cartRepository.save(cart);
    }

    // 매개변수 cart에 들어있는 카트상품이 매개변수 product와 같은 종류의 상품(product)인지 확인하는 함수
    // 맞으면 그 카트상품을 반환 / 아니면 null 반환
    private CartProduct findExistingProduct(Cart cart, Product product){
        // 해당 상품이 카트 내에 들어 있으면, 해당 상품 객체를 반환해주는 메소드
        // 동일한 상품이 이미 카트 내에 들어 있으면 수량을 누적할 목적임
        // cart.getCartProducts() : cart객체의 id를 cart_id이름의 fk인 컬럼의 데이터로 가진
        // CartProduct들을 가져와서 List 컬렉션에 넣고 반환함
        // -> 카트에 들어있는 카트 상품들을 객체로 컬렉션에 담아서 가져오는 것

        // 카트에 카드 상품이 없으면 null을 반환함
        if (cart.getCartProducts() == null) return null ;

        // 컬렉션안에 있는 객체들을 꺼내기 위해 사용하는 확장 for
        for(CartProduct cp : cart.getCartProducts()){
            // 카트에 담긴 카트 상품의 상품(상품종류)의 id가 매개변수인 product의 Id와 같으면
            // 그 카드 상품을 반환함
            if (cp.getProduct().getId().equals(product.getId())){
                return cp;
            }
        }
        return null ;
    }

    // @Transactional : 이 안에서 일어나는 모든 DB작업을 하나의 묶음(트랜잭션)으로 처리하라는 어노테이션
    // 중간에 에러, 예외가 터지면 그 전까지 했던 DB 변경을 전부 취소(롤백)하라는 의미
    // 이렇게 설정하는 이유는 중간 과정을 통틀어서 결국 최종 결과까지 가야하는데 중간에
    // 애매하게 바뀌고 결국 최종 결과까지 가지 못한상태로 DB가 변경이 되면 의미가 없고 꼬일 수 있기 때문에
    @Transactional
    public String addProductToCart(CartProductDto dto, String email){ // token의 claim에 있는 email을 사용함
        // dto : memberId(null) / productId, quantity는 프론트에서 값을 파라미터로 받음
        // 회원 조회 : email(아이디)을 이용해서 member를 찾음
        Member member = memberRepository.findByEmail(email) ;

        if (member == null) { // 회원이 없음
            throw new RuntimeException("회원 없음");
        }

        // 상품 조회 : 프론트에서 파라미터에서 가져온 productId 사용
        Product product = productRepository.findById(dto.getProductId())
                // 예외처리를 의도적으로 발생시키기 (Optional 타입이 반환되어서 .orElseThrow() 사용)
                .orElseThrow(() -> new RuntimeException("상품 없음")) ;


        // 재고 확인(주문 수량이 재고보다 많으면)
        // product.getStock() 상품의 재고 / dto.getQuantity() 프론트에서 받아온 유저가 선택한 주문수량
        if (product.getStock() < dto.getQuantity()){
            throw new RuntimeException("재고 수량이 부족합니다.");
        }

        // 장바구니 조회 또는 생성
        // 해당 맴버의 카트를 조회함 (cart는 member의 자식 테이블)
        // 해당 맴버의 카트를 객체에 저장함
        Cart cart = cartRepository.findByMember(member).orElse(null) ;

        if (cart == null){ // 카트가 구비 안된 고객
            Cart newCart = new Cart() ; // 새 카트 준비
            newCart.setMember(member); // 고객에게 할당
            // saveCart(Cart cart) : cartRepository.save(cart);
            cart = saveCart(newCart); // 해당 카트가 저장됨
        }

        // 기존 상품이 존재하는 지 확인 후 수량 처리
        // 카트에 있는 카트상품과 해당 상품을 비교해서 존재하면 해당 카트상품을 반환함
        CartProduct existingCartProduct = findExistingProduct(cart, product) ;

        if (existingCartProduct != null){ // 장바구니에 해당 상품이 들어 있으면
            // 기존 수량에 장바구니에서 요청항 수량을 누적합니다.
            // existingCartProduct.getQuantity() : 이미 카트에 들어 있는 값
            // dto.getQuantity() : 새로 추가 하는 값
            existingCartProduct.setQuantity(existingCartProduct.getQuantity()
                    + dto.getQuantity());

            // 서비스의 저장 메소드를 요청하여 database에 저장합니다.
            // 서비스를 요청하는데 이것이 Repository에 가서 database에 저장함
            // CartProductRepository.save(existingCartProduct);로 바로 DB에 저장해도 되지만
            // Service끼리는 Service끼리 소통해서 계층 구조를 지키려고 하는 것
            cartProductService.saveCartProduct(existingCartProduct);

        }else{ // 장바구니에 품목이 없는 경우
            CartProduct cp = new CartProduct();
```

            // 물건을 어떤 카트에 담을지 설정
            // cart : 해당 맴버의 카트
            cp.setCart(cart);

            // 어떤 물건 종류를 담을지 설정
            // product : 파라미터로 가져온 productId로 가져온 조회한 product (상품)
            cp.setProduct(product);

```typescript
            // 웹페이지에서 입력한 수량 입력하기
            // 파라미터에서 가져와서 dto에 넣은 quantity
            cp.setQuantity(dto.getQuantity());

            // Repository에 보내기
            cartProductService.saveCartProduct(cp);
        }

        return "요청하신 상품이 장바구니에 추가되었습니다." ;
    }
}
```




#### \# 컨트롤러(CartController) 신규 작성 (스프링) (06.장바구니.txt)
(controller - CartController 클래스 생성)
    public ResponseEntity<String> addToCart(@RequestBody CartProductDto dto) 메소드

- 코드 작성
```java
package com.coffee.controller;

import com.coffee.dto.CartProductDto;
import com.coffee.service.CartService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
@RequestMapping("/cart")
public class CartController {
    private final CartService cartService ;

    @PostMapping("/insert") // /cart/insert
    public ResponseEntity<String> addToCart(@RequestBody CartProductDto dto,
                                            Authentication authentication){
        // dto에는 productId와 quantity가 들어 있음 (memberId는 있지만 null값임)

        // JwtAuthenticationFilter.java 파일에서 만든
        // UsernamePasswordAuthenticationToken 타입의 객체인 auth를 만들때 넣은
        // 매개변수 email이 (이름만 email이지 사실상 들어온 token의 claim에서 subject(식별자)의 값을 넣은 변수임)
        // principal 위치에 있고
        // SecurityContextHolder.getContext().setAuthentication(auth); 으로
        // authentication은 그 값을 가지고 있는데 name을 principal의 위치에 있는 걸로 인식해서
        // getName() 함수를 실행하면 인증 객체의 principal(토큰에서 가져온 email 값)을 가져옴
        String email = authentication.getName() ;
        String message = cartService.addProductToCart(dto, email);

        return ResponseEntity.ok(message) ;
    }
}
```


#### \# 테스트 시나리오 (스프링) (06.장바구니.txt)
    사용자   상품 번호	담기   수량	최종 결과
    유영석  	1    	5		상품   1번 		8개
					1	    3		상품   2번 		4개
					2	    4

    곰돌이  	1	    4		상품   1번 		4개
					3    	2		상품   3번 		7개
					3	    5


#### \# 데이터 베이스 확인 (MySQL) (06.장바구니.txt)
```sql
-- 회원 id 확인
select member_id, email, name, role from members ;

-- 카트 정보 확인
select \* from carts ;

-- 카트 상품 정보 확인
select \* from cart_products ;

-- 최종 결과 확인
select m.member_id, m.name, c.cart_id, cp.cart_product_id, cp.product_id, cp.quantity, p.name, p.price, p.stock
from ((members m join carts c
on m.member_id = c.member_id) join cart_products cp
on c.cart_id = cp.cart_id) join products p
on cp.product_id = p.product_id ;
```




#### \# 제06장-02. 내 장바구니 목록 보기
#### \# 파일 : CartProduct.ts(신규 작성) (리액트) (06.장바구니.txt)
(types - CartProduct.ts 파일 생성)
리액트 앱 내부에서 사용하는 카트 상품 모델'을 처리해주는 타입 스크립트 인터페이스를 작성합니다.

- 코드 작성
```typescript
export interface CartProduct {
    // 백엔드 엔티티에 있는 변수
    cartProductId: number;
    productId: number;
    quantity: number;

    // 백엔드 엔티티에 있지만 .ts에는 없는 변수
    // cartId: number
```


    // 백엔드 엔티티에 없는 변수
    image: string;
    name: string;
    price: number;
    checked: boolean;
};



#### \# 라우팅 설정 (리액트) (06.장바구니.txt)
    AppRouters.tsx 수정
```typescript
        <Route path='/cart/list' element={<CartList user={user} />} />
```


- 코드 추가
```typescript
import CartList from './../pages/CartList';

<Route path='/cart/list' element={<CartList user={user} />} />
```




#### \# 카트 목록(폼 양식) (리액트) (06.장바구니.txt)
(pages - CartList.tsx 파일 생성)
    CartList.tsx 신규 작성

    cartProducts 배열 선언
    useEffect Hook 사용
    const navigate = useNavigate(); 선언
    fetchCartProducts() 함수 구현

파일 참조 : CartList02.txt

- 코드 작성 (복붙)
```typescript
import { Button, Container, Form, Table } from "react-bootstrap";

import type { User } from "../types/User";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import customAxios from './../api/axiosInstance';
import type { CartProduct } from "../types/CartProduct";
import { API_BASE_URL } from "../config/config";

type AppProps = {
    user: User | null; // user는 User 객체 혹은 null일 수도 있습니다.
}

function App({ user }: AppProps) {
    const thStyle = { fontSize: '1.2rem' }; // 테이블 헤더 스타일

    const [cartProducts, setCartProducts] = useState<CartProduct[]>([]);

    useEffect(() => { // user가 있고 user.id가 존재하면 해당 user의 cartlist를 가져옴
        if (user && user?.id) {
            fetchCartProducts();
        }
    }, [user]); // user가 바뀌면 화면 갱신하고 다시 그 user의 cartlist를 가져옴

    const navigate = useNavigate();

    const fetchCartProducts = async () => {
        try {
            const url = `${API_BASE_URL}/cart/list`;
            const response = await customAxios.get(url);
            console.log('카트 상품 조회 결과');
            console.log(response.data);

            setCartProducts(response.data || []);

        } catch (error) {
            console.log('오류 정보');
            console.log(error);
            alert(`'카트 상품' 정보가 존재하지 않아서 상품 목록 페이지로 이동합니다.`);
            navigate('/product/list');

        }
    };

    return (
        <Container className="mt-4">
            <h2 className="mb-4">
                {/* xxrem은 주위 글꼴의 xx배를 의미합니다. */}
                <span style={{ color: 'blue', fontSize: '2rem' }}>{user?.name}</span>
                <span style={{ fontSize: '1.3rem' }}>님의 장바구니</span>
            </h2>
            <Table striped bordered>
                <thead>
                    <tr>
                        <th style={thStyle}>
                            <Form.Check
                                type="checkbox"
                                label="전체 선택"
                            />
                        </th>
                        <th style={thStyle}>상품 정보</th>
                        <th style={thStyle}>수량</th>
                        <th style={thStyle}>금액</th>
                        <th style={thStyle}>삭제</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>xx</td>
                    </tr>
                </tbody>
            </Table>

            {/* 좌측 정렬(text-start), 가운데 정렬(text-center), 우측 정렬(text-end) */}
            <h3 className="text-end mt-3">총 주문 금액 : 0원</h3>
            <div className="text-end">
                <Button variant="primary" size="lg" >
                    주문하기
                </Button>
            </div>
        </Container>
    );
}

export default App;
```




#### \# 장바구니 품목(CartItemDto) 신규 작성 (스프링) (06.장바구니.txt)
(dto폴더에 CartItemDto 클래스 생성)
    해당 클래스는 `장바구니` 목록 페이지에서 목록 데이터 1개를 의미하는 자바 DTO 클래스입니다.
    리액트의 CartList.tsx 파일에서 fetchCartProducts() 함수 참조

- 코드 작성
```java
package com.coffee.dto;

/* 리액트의 CartProduct.ts에 맞게 작성
export interface CartProduct {
    cartProductId: number;
    productId: number;
    image: string;
    name: string;
    quantity: number;
    price: number;
    checked: boolean;
};
*/

import com.coffee.entity.CartProduct;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class CartItemDto {
    private Long cartProductId ;
    private Long productId ;
    private String name ;
    private String image ;
    private int price ;
    private int quantity ;
    private boolean checked ;

    public CartItemDto(CartProduct cartProduct) {
        this.cartProductId = cartProduct.getId();
        this.productId = cartProduct.getProduct().getId() ;
        this.name = cartProduct.getProduct().getName() ;
        this.image = cartProduct.getProduct().getImage() ;
        this.price = cartProduct.getProduct().getPrice() ;
        this.quantity = cartProduct.getQuantity() ;
    }
}
```



#### \# 서비스(CartService) (스프링) (06.장바구니.txt)
    특정 회원이 가지고 있는 카트 상품 목록을 조회해주는 메소드입니다.
    public List<CartItemDto> getCartItemsByMemberId(Long memberId) 메소드

- 코드 추가 (맨 밑에)
```java
// 해당 유저의 id를 이용해서 해당 유저의 카트에 들어 있는 카트 상품들을
// CartItemDto타입의 객체들로 담아서 프론트에 반환함
public List<CartItemDto> getCartItemsByMemberId(Long memberId){
	// 회원 조회
	Member member = memberService.findMemberById(memberId)
			.orElseThrow(() -> new RuntimeException("유효하지 않은 회원입니다.")) ;

	// 회원이 소유한 카트 정보 조회
	// 없으면 빈 카트 생성
	// Cart::new : () -> new Cart()를 줄인 것
	Cart cart = cartRepository.findByMember(member).orElseGet(Cart::new);

	// 가져온(혹은 생성한) 카트 객체에 들어있는 CartProduct 타입의 객체들을 빼서
	// 프론트엔드에 보낼 객체인 CartItemDto 객체로 만들어서 List 컬렉션에 객체들을 넣고 반환함
	List<CartItemDto> cartItemDtoList = new ArrayList<>();
	for (CartProduct cp : cart.getCartProducts()){
		cartItemDtoList.add(new CartItemDto(cp));
	}
	return cartItemDtoList ;

/* return cart.getCartProducts().stream()
		.map(CartItemDto::new).toList() ; */
}
```


#### \# 컨트롤러(CartController) (스프링) (06.장바구니.txt)
    public ResponseEntity<List<CartItemDto>> getCartProducts(Authentication authentication) 메소드

- 코드 추가 (맨 밑에)
```java
// 토큰으로 만든 인증 객체에 담긴 토큰의 subject인 email을 이용해서 member 객체를 DB에서 가져오기 위해 준비
private final MemberService memberService ;

@GetMapping("/list")
public ResponseEntity<List<CartItemDto>> getCartProducts(Authentication authentication){
	// 토큰으로 만든 인증 객체에 담긴 토큰의 subject인 email을 이용해서
	// 해당 email의 member 객체를 DB에서 가져옴
	String email = authentication.getName();

	Member member = memberService.findByEmail(email) ;

	if (member == null){
		new RuntimeException("사용자가 존재하지 않습니다.");
	}

	// 해당 맴버의 Id를 이용해 DB에서 해당 맴버의 cart에 들어있는 상품 객체들을
	// 프론트에서 받을 준비가 된 객체 타입인 CartItemDto 타입으로 담아서 반환함
	return ResponseEntity.ok(cartService.getCartItemsByMemberId(member.getId())) ;
}
```



#### \# 카트 목록(전체 선택 기능) (리액트) (06.장바구니.txt)
(pages - CartList.tsx 수정)
파일 참조 : CartList04.txt

- 프로그램 설계 진행
1) 스테이트 생성
```typescript
const [orderTotalPrice, setOrderTotalPrice] = useState(0);
```
2) refreshOrderTotalPrice 함수 작성
3) toggleAllCheckBox 함수 작성
전체 선택/해제 시 모든 상품 체크 상태를 일괄 적용하고 총 금액을 갱신하는 이벤트 핸들러 함수
4) 전체 선택 "checkbox"의 onChange 이벤트 구현
5) 하단 총 주문 금액
```typescript
<h3 className="text-end mt-3">총 주문 금액 : {orderTotalPrice.toLocaleString()}원</h3>
```

- 코드 전체
```typescript
import { Button, Col, Container, Form, Image, Row, Table } from "react-bootstrap";

import type { User } from "../types/User";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import customAxios from './../api/axiosInstance';
import type { CartProduct } from "../types/CartProduct";
import { API_BASE_URL } from "../config/config";

type AppProps = {
    user: User | null; // user는 User 객체 혹은 null일 수도 있습니다.
}

function App({ user }: AppProps) {
    const thStyle = { fontSize: '1.2rem' }; // 테이블 헤더 스타일

    const [cartProducts, setCartProducts] = useState<CartProduct[]>([]);

    useEffect(() => { // user가 있고 user.id가 존재하면 해당 user의 cartlist를 가져옴
        if (user && user?.id) {
            fetchCartProducts();
        }
    }, [user]); // user가 바뀌면 화면 갱신하고 다시 그 user의 cartlist를 가져옴

    const navigate = useNavigate();

    const fetchCartProducts = async () => {
        try {
            const url = `${API_BASE_URL}/cart/list`;
            const response = await customAxios.get(url);
            console.log('카트 상품 조회 결과');
            console.log(response.data);

            // 백엔드의 CartItemDto 타입(프론트의 CartProduct.ts 타입)으로 된 객체들이 담김
            setCartProducts(response.data || []);

        } catch (error) {
            console.log('오류 정보');
            console.log(error);
            alert(`'카트 상품' 정보가 존재하지 않아서 상품 목록 페이지로 이동합니다.`);
            navigate('/product/list');

        }
    };

    // 화면에 보여 주는 주문 총 금액을 위한 스테이트 (체크한 품목에 따라 값이 변해야 함)
    const [orderTotalPrice, setOrderTotalPrice] = useState(0);

    // 체크 박스의 상태가 Toggle될 때 마다, 전체 요금을 다시 재계산하는 함수
    // (총 주문 금액 변화)
    // products는 카트에 담긴 상품들을 의미 (백엔드에서 받아온 데이터)
    // CartProduct[]는 타입스크립트(설계도) - 스프링의 CartItemDto도 동일한지 확인해야 함
    const refreshOrderTotalPrice = (products: CartProduct[]) => {
        let total = 0; // 총 금액 변수 // 처음에는 초기화 해놓음

        // bean은 상품 하나를 의미
        products.forEach((bean) => {
            if (bean.checked) { // 선택된 체크 박스에 대하여
                total += bean.price * bean.quantity; // 총 금액 누적
            }
        });

        setOrderTotalPrice(total); // State 업데이트
    };

    // `전체 선택` 체크 박스를 Toggle 함
    const toggleAllCheckBox = (isAllCheck: boolean) => {
        // isAllCheck : `전체 선택` 체크 박스의 boolean 값
        setCartProducts((previous) => {
            // 모든 객체(카트 상품)들의 나머지 속성은 보존하고, 체크 상태(checked)를
            // `전체 선택` 체크 상태와 동일하게 설정합니다.
            // 장바구니에서 체크 상태만 바꾸지 장바구니에 있는 상품의 나머지 부분을 그대로 두기
            // ...product는 product가 가진 속성들 중 그대로 보존하려는 속성들
            const updatedProducts = previous.map((product) => ({
                ...product,
                checked: isAllCheck
            }));

            // 비동기적 렌더링 문제로 수정된 updatedProducts 항목을 매개 변수로 넘겨야 정상적으로 동작함
            refreshOrderTotalPrice(updatedProducts);

            return updatedProducts;
        });
    };

    return (
        <Container className="mt-4">
            <h2 className="mb-4">
                {/* xxrem은 주위 글꼴의 xx배를 의미합니다. */}
                <span style={{ color: 'blue', fontSize: '2rem' }}>{user?.name}</span>
                <span style={{ fontSize: '1.3rem' }}>님의 장바구니</span>
            </h2>
            <Table striped bordered>
                <thead>
                    <tr>
                        <th style={thStyle}>
                            <Form.Check
                                type="checkbox"
                                label="전체 선택"
                                // 4)전체 선택 "checkbox"의 onChange 이벤트 구현
                                onChange={(event) => toggleAllCheckBox(event.target.checked)}
                            />
                        </th>
                        <th style={thStyle}>상품 정보</th>
                        <th style={thStyle}>수량</th>
                        <th style={thStyle}>금액</th>
                        <th style={thStyle}>삭제</th>
                    </tr>
                </thead>
                <tbody>
                    {cartProducts.length > 0 ? (
                        cartProducts.map((product) => (
                            <tr key={product.cartProductId}>
                                <td className="text-center align-middle">
                                    <Form.Check
                                        type="checkbox"
                                        checked={product.checked}
                                    />
                                </td>
                                <td className="text-center align-middle">
                                    <Row> {/* 좌측 4칸은 이미지 영역, 우측 8칸은 상품 이름 영역 */}
                                        <Col xs={4}>
                                            <Image
                                                src={`${API_BASE_URL}/images/${product.image}`}
                                                thumbnail
                                                alt={product.name}
                                                width={`80`}
                                                height={`80`}
                                            />
                                        </Col>
                                        <Col xs={8} className="d-flex align-items-center">
                                            {product.name}
                                        </Col>
                                    </Row>
                                </td>
                                <td className="text-center align-middle">
                                    <Form.Control
                                        type="number"
                                        min={1}
                                        value={product.quantity}
                                        style={{ width: '80px', margin: '0 auto' }}
                                    />
                                </td>
                                <td className="text-center align-middle">
                                    {(product.price * product.quantity).toLocaleString()} 원
                                </td>
                                <td className="text-center align-middle">
                                    <Button variant="danger" size="sm"
                                    >
                                        삭제
                                    </Button>
                                </td>
                            </tr>
                        ))
                    ) : (
                        <tr><td>장바구니가 비어 있습니다.</td></tr>
                    )}
                </tbody>
            </Table>

            {/* 좌측 정렬(text-start), 가운데 정렬(text-center), 우측 정렬(text-end) */}
            {/* 하단 총 주문 금액 */}
            {/* JS영역의 데이터를 사용해서 {}중괄호 사용 */}
            {/* int인 orderTotalPrice를 HTML에 사용하기 위해 toLocaleString()로 String으로 변환 */}
            <h3 className="text-end mt-3">총 주문 금액 : {orderTotalPrice.toLocaleString()}원</h3>
            <div className="text-end">
                <Button variant="primary" size="lg" >
                    주문하기
                </Button>
            </div>
        </Container>
    );
}

export default App;
```




#### \# MenuItems.tsx에 코드 추가
사용자 이름 표시가 되게 return에
```typescript
<Nav className="me-auto">
```
밑에 아래 코드 추가

```typescript
{/* 사용자 이름 표시 */}
{user && (
	<Nav.Item className="text-white fw-bold fs-5 me-3 d-flex align-items-center">
		{user.name}님
	</Nav.Item>
)}
```



#### \# 카트 목록(개별 선택 기능) (리액트) (06.장바구니.txt)
(pages - CartList.tsx 수정)
파일 참조 : CartList05.txt

toggleCheckBox 함수
    특정 상품의 체크 박스 상태를 토글(선택/해제)하는 함수

개별 선택 "checkbox"의 onChange 이벤트 구현

- 코드 추가 (return위에)

```typescript
	// 개별 체크 박스를 클릭하였습니다.
    // 카트 목록(개별 선택 기능)
    const toggleCheckBox = (cartProductId: number) => {
        // 정보가 잘 가는지 간단하게 테스트하는 용도
        console.log(`카트 상품 아이디 : ${cartProductId}`);

		// previous로 인해 암시적으로 cartProducts의 이전 상태가 들어옴
        setCartProducts((previous) => {
		// !product.checked는 체크 상태를 toggle 시키는 역할을 합니다.
		const updatedProducts = previous.map((product) =>
			// 삼항 연산자 (조건 연산자 사용)
			// 나머지는 놔두고 check상태만 부호 반전시켜라
			product.cartProductId === cartProductId
				? { ...product, checked: !product.checked }
				: product
		);

		refreshOrderTotalPrice(updatedProducts);
		return updatedProducts;
	});
};
```





#### \# 제06장-03. 카트 상품 수량 변경하기
#### \# 카트 내 수량 변경 (리액트) (06.장바구니.txt)
(pages - CartList.tsx)
파일 참조 : CartList06.txt
1) changeQuantity() 함수
	장바구니에 담긴 상품의 수량을 변경하는 함수입니다.
2) 수량 변경 입력 상자
	함수 changeQuantity와 연동하기 위하여 onChange 코드를 작성합니다.

- 코드 전체
```typescript
import { Button, Col, Container, Form, Image, Row, Table } from "react-bootstrap";

import type { User } from "../types/User";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import customAxios from './../api/axiosInstance';
import type { CartProduct } from "../types/CartProduct";
import { API_BASE_URL } from "../config/config";

/*
```
구조 분해 할당 + 타입 지정

정석적인 표현은 이렇습니다.
```typescript
    function App(props: AppProps) {
        const user = props.user;
    }
```

줄여서 쓴 것이:
```typescript
    function App({ user }: AppProps)
*/

type AppProps = {
    user: User | null; // user는 User 객체 혹은 null일 수도 있습니다.
}

function App({ user }: AppProps) {
    const thStyle = { fontSize: '1.2rem' }; // 테이블 헤더 스타일

    // 보여 주고자하는 `카트 상품` 배열 정보
    const [cartProducts, setCartProducts] = useState<CartProduct[]>([]);

    useEffect(() => { // user가 있고 user.id가 존재하면 해당 user의 cartlist를 가져옴
        if (user && user?.id) {
            fetchCartProducts();
        }
    }, [user]); // user가 바뀌면 화면 갱신하고 다시 그 user의 cartlist를 가져옴

    const navigate = useNavigate();

    const fetchCartProducts = async () => {
        try {
            const url = `${API_BASE_URL}/cart/list`;
            const response = await customAxios.get(url);
            console.log('카트 상품 조회 결과');
            console.log(response.data);

            // 백엔드의 CartItemDto 타입(프론트의 CartProduct.ts 타입)으로 된 객체들이 담김
            setCartProducts(response.data || []);

        } catch (error) {
            console.log('오류 정보');
            console.log(error);
            alert(`'카트 상품' 정보가 존재하지 않아서 상품 목록 페이지로 이동합니다.`);
            navigate('/product/list');

        }
    };

    // 화면에 보여 주는 주문 총 금액을 위한 스테이트 (체크한 품목에 따라 값이 변해야 함)
    const [orderTotalPrice, setOrderTotalPrice] = useState(0);

    // 체크 박스의 상태가 Toggle될 때 마다, 전체 요금을 다시 재계산하는 함수
    // (총 주문 금액 변화)
    // products는 카트에 담긴 상품들을 의미 (백엔드에서 받아온 데이터)
    // CartProduct[]는 타입스크립트(설계도) - 스프링의 CartItemDto도 동일한지 확인해야 함
    const refreshOrderTotalPrice = (products: CartProduct[]) => {
        let total = 0; // 총 금액 변수 // 처음에는 초기화 해놓음

        // bean은 상품 하나를 의미
        products.forEach((bean) => {
            if (bean.checked) { // 선택된 체크 박스에 대하여
                total += bean.price * bean.quantity; // 총 금액 누적
            }
        });

        setOrderTotalPrice(total); // State 업데이트
    };

    // `전체 선택` 체크 박스를 Toggle 함
    const toggleAllCheckBox = (isAllCheck: boolean) => {
        // isAllCheck : `전체 선택` 체크 박스의 boolean 값
        setCartProducts((previous) => {
            // 모든 객체(카트 상품)들의 나머지 속성은 보존하고, 체크 상태(checked)를
            // `전체 선택` 체크 상태와 동일하게 설정함
            // 장바구니에서 체크 상태만 바꾸지 장바구니에 있는 상품의 나머지 부분을 그대로 두기
            // ...product는 product가 가진 속성들 중 그대로 보존하려는 속성들
            const updatedProducts = previous.map((product) => ({
                ...product,
                checked: isAllCheck
            }));

            // 비동기적 렌더링 문제로 수정된 updatedProducts 항목을 매개 변수로 넘겨야 정상적으로 동작합니다.
            refreshOrderTotalPrice(updatedProducts);

            return updatedProducts;
        });
    };

    // 개별 체크 박스를 클릭
    // 카트 목록(개별 선택 기능)
    const toggleCheckBox = (cartProductId: number) => {
        // 정보가 잘 가는지 간단하게 테스트하는 용도
        console.log(`카트 상품 아이디 : ${cartProductId}`);

        // previous로 인해 암시적으로 cartProducts의 이전 상태가 들어옴
        setCartProducts((previous) => {
            // !product.checked는 체크 상태를 toggle 시키는 역할
            const updatedProducts = previous.map((product) =>
                // 삼항 연산자 (조건 연산자 사용)
                // 나머지는 놔두고 check상태만 부호 반전시켜라
                product.cartProductId === cartProductId
                    ? { ...product, checked: !product.checked }
                    : product
            );

            refreshOrderTotalPrice(updatedProducts);
            return updatedProducts;
        });
    };

    // 카트 상품 목록에서 특정 상품의 구매 수량을 변경
    const changeQuantity = async (cartProductId: number, quantity: number) => {
        // NaN : Not A Number
        if (isNaN(quantity)) { // 숫자 형식이 아니면
            // 값을 0으로 변경한 다음, 함수를 반환하도록 함
            setCartProducts((previous) => {
                // 선택한 그 카트상품을 찾아서 양을 0으로 설정하려고 반복문 돌림
                return previous.map((product) =>
                    product.cartProductId === cartProductId
                        ? { ...product, quantity: 0 }
                        : product
                );
            });

            alert('변경 수량은 최소 1이상이어야 합니다.');
            return;
        }
        try {
            // 사용 예시 : 100번 항목을 10개로 수정해주세요.
            // http://localhost:9000/cart/edit/100?quantity=10
            const url = `${API_BASE_URL}/cart/edit/${cartProductId}?quantity=${quantity}`;

            // patch 동작은 전체가 아닌 일부 데이터를 변경하고자 할때 사용됨
            // 스프링의 WebConfig 클래스안의 addCorsMappings() 메소드를 참조하길 바람
            const response = await customAxios.patch(url, {}, {
                withCredentials: true  // ✅ 인증 정보를 함께 전송
            });

            console.log(response.data || '');

            // cartProducts의 수량 정보를 갱신
            setCartProducts((previous) => {
                const updatedProducts = previous.map((product) =>
                    product.cartProductId === cartProductId
                        ? { ...product, quantity: quantity }
                        : product
                );

                refreshOrderTotalPrice(updatedProducts);
                return updatedProducts;
            });

        } catch (error) {
            console.log('카트 상품 수량 변경 실패');
            console.log(error);
        }

    };

    return (
        <Container className="mt-4">
            <h2 className="mb-4">
                {/* xxrem은 주위 글꼴의 xx배를 의미 */}
                <span style={{ color: 'blue', fontSize: '2rem' }}>{user?.name}</span>
                <span style={{ fontSize: '1.3rem' }}>님의 장바구니</span>
            </h2>
            <Table striped bordered>
                <thead>
                    <tr>
                        <th style={thStyle}>
                            <Form.Check
                                type="checkbox"
                                label="전체 선택"
                                // 전체 선택 "checkbox"의 onChange 이벤트 구현
                                onChange={(event) => toggleAllCheckBox(event.target.checked)}
                            />
                        </th>
                        <th style={thStyle}>상품 정보</th>
                        <th style={thStyle}>수량</th>
                        <th style={thStyle}>금액</th>
                        <th style={thStyle}>삭제</th>
                    </tr>
                </thead>
                <tbody>
                    {cartProducts.length > 0 ? (
                        cartProducts.map((product) => (
                            <tr key={product.cartProductId}>
                                <td className="text-center align-middle">
                                    <Form.Check
                                        type="checkbox"
                                        checked={product.checked}
                                        // Check박스의 값이 바뀔때마다 해당 함수 실행 (해당 매개변수)
                                        onChange={() => toggleCheckBox(product.cartProductId)}
                                    />
                                </td>
                                <td className="text-center align-middle">
                                    <Row> {/* 좌측 4칸은 이미지 영역, 우측 8칸은 상품 이름 영역 */}
                                        <Col xs={4}>
                                            <Image
                                                src={`${API_BASE_URL}/images/${product.image}`}
                                                thumbnail
                                                alt={product.name}
                                                width={`80`}
                                                height={`80`}
                                            />
                                        </Col>
                                        <Col xs={8} className="d-flex align-items-center">
                                            {product.name}
                                        </Col>
                                    </Row>
                                </td>
                                <td className="text-center align-middle">
                                    <Form.Control
                                        type="number"
                                        min={1}
                                        value={product.quantity}
                                        style={{ width: '80px', margin: '0 auto' }}
                                        // 수량 변경 입력 상자
                                        onChange={(event) =>
                                            changeQuantity(
                                                product.cartProductId,

                                                // HTML에서 모든 양식에 있는 값을 String으로 생각함
                                                // event.target.value : 방금 수정한(change)한 값(숫자여도 문자열임)
                                                // 문자열인 해당 값을 정수형으로 바꿔줌
                                                parseInt(event.target.value)
                                            )}
                                    />
                                </td>
                                <td className="text-center align-middle">
                                    {(product.price * product.quantity).toLocaleString()} 원
                                </td>
                                <td className="text-center align-middle">
                                    <Button variant="danger" size="sm"
                                    >
                                        삭제
                                    </Button>
                                </td>
                            </tr>
                        ))
                    ) : (
                        <tr><td>장바구니가 비어 있습니다.</td></tr>
                    )}
                </tbody>
            </Table>

            {/* 좌측 정렬(text-start), 가운데 정렬(text-center), 우측 정렬(text-end) */}
            {/* 5) 하단 총 주문 금액 */}
            {/* JS영역의 데이터를 사용해서 {}중괄호 사용 */}
            {/* int인 orderTotalPrice를 HTML에 사용하기 위해 toLocaleString()로 String으로 변환 */}
            <h3 className="text-end mt-3">총 주문 금액 : {orderTotalPrice.toLocaleString()}원</h3>
            <div className="text-end">
                <Button variant="primary" size="lg" >
                    주문하기
                </Button>
            </div>
        </Container>
    );
}

export default App;
```



#### \# 서비스(CartProductService) (스프링) (06.장바구니.txt)
(service - CartProductService에 코드 추가)
```java
	public String editCartProductQuantity(Long cartProductId, Integer quantity) 메소드 구현
```

- 코드 추가 (맨 밑에)
```java
// 카트상품의 수량을 변경하는 함수
public String editCartProductQuantity(Long cartProductId, Integer quantity){
	// 수량 검증
	if(quantity == null || quantity < 1){
		return "오류 : 장바구니 품목은 최소 1개 이상이어야 합니다.";
	}

	// 해당 카트 상품 찾기
	// Optional이 java.util이라는 것을 무조건 외우기
	// service 코딩 중이니까 Repository한테 물어봐야 함
	// findById는 CrudRepository에 있음 (상속 느껴보기)
	Optional<CartProduct> cartProductOptional = cartProductRepository.findById(cartProductId);

	// Optional 클래스도 나중에 한 번 공부 해오기
	if (cartProductOptional.isEmpty()){
		return "오류 : 카트 품목을 찾을 수 없습니다.";
	}

	// 재고 수량 점검 및 수량 변경
	CartProduct cartProduct = cartProductOptional.get();

	int stock = cartProduct.getProduct().getStock() ;
	if (quantity > stock){ // 손님이 입력한 수보다 재고가 부족할 경우
		return "오류 : 재고 수량이 부족합니다.";
	}

	// 덮어쓰기하는 경우
	cartProduct.setQuantity(quantity);
	// 만약에 누적을 할 경우 (누적 변경시 다음과 같이 코딩합니다.)
	// cartProduct.setQuantity(cartProduct.getQuantity() + quantity);


	// 데이터 베이스에 저장
	cartProductRepository.save(cartProduct);

	// 성공 메시지 반환
	String message = "카트 상품 아이디 " + cartProductId + "번이 " + quantity + "개로 수정이 되었습니다." ;
	return message ;
}
```



#### \# 컨트롤러(CartController) (스프링) (06.장바구니.txt)
(controller - CartController에 코드 추가)
```java
public ResponseEntity<String> editCartProductQuantity(
            @PathVariable Long cartProductId,
            @RequestParam(required = false) Integer quantity)
```

- 코드 추가 (맨 밑에)
```java
private final CartProductService cartProductService ;

@PatchMapping("/edit/{cartProductId}")
public ResponseEntity<String> editCartProductQuantity(
		@PathVariable Long cartProductId, // url 경로 (필수) (Mapping 어노테이션에 url주소로 들어가야함)
		// 쿼리 파라미터 부가옵션 (선택) (url주소로 안들어가도 됨)
		@RequestParam(required = false) Integer quantity){
	System.out.println("카트 상품 아이디 : " + cartProductId);
	System.out.println("변경할 갯수 : " + quantity);

	String message = cartProductService.editCartProductQuantity(cartProductId, quantity) ;

	if (message.startsWith("오류")){// CartProductService에 해당 함수에 if문으로 오류가 return되는 경우 이용
		return ResponseEntity.badRequest().body(message) ;
	}else{
		return ResponseEntity.ok(message) ;
	}
}
```



 # 서비스(CartProductService) (스프링) (06.장바구니.txt) (이어서 작성)
(service - CartProductService에 코드 추가)
```java
	public String editCartProductQuantity(Long cartProductId, Integer quantity) 메소드 수정
```

- 코드 수정
```java
// 카트상품의 수량을 변경하는 함수
public String editCartProductQuantity(Long cartProductId, Integer quantity){
	// 수량 검증
	if(quantity == null || quantity < 1){
		return "오류 : 장바구니 품목은 최소 1개 이상이어야 합니다.";
	}

	// 해당 카트 상품 찾기
	// Optional이 java.util이라는 것을 무조건 외우기
	// service 코딩 중이니까 Repository한테 물어봐야 함
	// findById는 CrudRepository에 있음 (상속 느껴보기)
	Optional<CartProduct> cartProductOptional = cartProductRepository.findById(cartProductId);

	// Optional 클래스도 나중에 한 번 공부 해오기
	if (cartProductOptional.isEmpty()){
		return "오류 : 카트 품목을 찾을 수 없습니다.";
	}

	// 재고 수량 점검 및 수량 변경
	CartProduct cartProduct = cartProductOptional.get();

	int stock = cartProduct.getProduct().getStock() ;
	if (quantity > stock){ // 손님이 입력한 수보다 재고가 부족할 경우
		return "오류 : 재고 수량이 부족합니다.";
	}

	// 덮어쓰기하는 경우
	cartProduct.setQuantity(quantity);
	// 만약에 누적을 할 경우 (누적 변경시 다음과 같이 코딩합니다.)
	// cartProduct.setQuantity(cartProduct.getQuantity() + quantity);


	// 데이터 베이스에 저장
	cartProductRepository.save(cartProduct);

	// 성공 메시지 반환
	String message = "카트 상품 아이디 " + cartProductId + "번이 " + quantity + "개로 수정이 되었습니다." ;
	return message ;
}
```




#### \# url의 parameter 변수로 저장해서 이용 (리액트)
(pages - CartList에 코드 수정)

- 코드 수정 (코드 전체 복붙)
```typescript
import { Button, Col, Container, Form, Image, Row, Table } from "react-bootstrap";

import type { User } from "../types/User";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import customAxios from './../api/axiosInstance';
import type { CartProduct } from "../types/CartProduct";
import { API_BASE_URL } from "../config/config";

type AppProps = {
    user: User | null; // user는 User 객체 혹은 null일 수도 있습니다.
}

function App({ user }: AppProps) {
    const thStyle = { fontSize: '1.2rem' }; // 테이블 헤더 스타일

    // 보여 주고자하는 `카트 상품` 배열 정보
    const [cartProducts, setCartProducts] = useState<CartProduct[]>([]);

    useEffect(() => { // user가 있고 user.id가 존재하면 해당 user의 cartlist를 가져옴
        if (user && user?.id) {
            fetchCartProducts();
        }
    }, [user]); // user가 바뀌면 화면 갱신하고 다시 그 user의 cartlist를 가져옴

    const navigate = useNavigate();

    const fetchCartProducts = async () => {
        try {
            const url = `${API_BASE_URL}/cart/list`;
            const response = await customAxios.get(url);
            console.log('카트 상품 조회 결과');
            console.log(response.data);

            // 백엔드의 CartItemDto 타입(프론트의 CartProduct.ts 타입)으로 된 객체들이 담김
            setCartProducts(response.data || []);

        } catch (error) {
            console.log('오류 정보');
            console.log(error);
            alert(`'카트 상품' 정보가 존재하지 않아서 상품 목록 페이지로 이동합니다.`);
            navigate('/product/list');

        }
    };

    // 화면에 보여 주는 주문 총 금액을 위한 스테이트 (체크한 품목에 따라 값이 변해야 함)
    const [orderTotalPrice, setOrderTotalPrice] = useState(0);

    // 체크 박스의 상태가 Toggle될 때 마다, 전체 요금을 다시 재계산하는 함수
    // (총 주문 금액 변화)
    // products는 카트에 담긴 상품들을 의미 (백엔드에서 받아온 데이터)
    // CartProduct[]는 타입스크립트(설계도) - 스프링의 CartItemDto도 동일한지 확인해야 함
    const refreshOrderTotalPrice = (products: CartProduct[]) => {
        let total = 0; // 총 금액 변수 // 처음에는 초기화 해놓음

        // bean은 상품 하나를 의미
        products.forEach((bean) => {
            if (bean.checked) { // 선택된 체크 박스에 대하여
                total += bean.price * bean.quantity; // 총 금액 누적
            }
        });

        setOrderTotalPrice(total); // State 업데이트
    };

    // `전체 선택` 체크 박스를 Toggle 함
    const toggleAllCheckBox = (isAllCheck: boolean) => {
        // isAllCheck : `전체 선택` 체크 박스의 boolean 값
        setCartProducts((previous) => {
            // 모든 객체(카트 상품)들의 나머지 속성은 보존하고, 체크 상태(checked)를
            // `전체 선택` 체크 상태와 동일하게 설정함
            // 장바구니에서 체크 상태만 바꾸지 장바구니에 있는 상품의 나머지 부분을 그대로 두기
            // ...product는 product가 가진 속성들 중 그대로 보존하려는 속성들
            const updatedProducts = previous.map((product) => ({
                ...product,
                checked: isAllCheck
            }));

            // 비동기적 렌더링 문제로 수정된 updatedProducts 항목을 매개 변수로 넘겨야 정상적으로 동작합니다.
            refreshOrderTotalPrice(updatedProducts);

            return updatedProducts;
        });
    };

    // 개별 체크 박스를 클릭
    // 카트 목록(개별 선택 기능)
    const toggleCheckBox = (cartProductId: number) => {
        // 정보가 잘 가는지 간단하게 테스트하는 용도
        console.log(`카트 상품 아이디 : ${cartProductId}`);

        // previous로 인해 암시적으로 cartProducts의 이전 상태가 들어옴
        setCartProducts((previous) => {
            // !product.checked는 체크 상태를 toggle 시키는 역할
            const updatedProducts = previous.map((product) =>
                // 삼항 연산자 (조건 연산자 사용)
                // 나머지는 놔두고 check상태만 부호 반전시켜라
                product.cartProductId === cartProductId
                    ? { ...product, checked: !product.checked }
                    : product
            );

            refreshOrderTotalPrice(updatedProducts);
            return updatedProducts;
        });
    };

    // 카트 상품 목록에서 특정 상품의 구매 수량을 변경
    const changeQuantity = async (cartProductId: number, quantity: number, productId: number) => {
        // NaN : Not A Number
        if (isNaN(quantity)) { // 숫자 형식이 아니면
            // 값을 0으로 변경한 다음, 함수를 반환하도록 함
            setCartProducts((previous) => {
                // 선택한 그 카트상품을 찾아서 양을 0으로 설정하려고 반복문 돌림
                return previous.map((product) =>
                    product.cartProductId === cartProductId
                        ? { ...product, quantity: 0 }
                        : product
                );
            });

            alert('변경 수량은 최소 1이상이어야 합니다.');
            return;
        }
        try {

            // 주소 뒤에 적을 파라미터들 변수로 저장하기
            const parameter = `quantity=${quantity}&productId=${productId}`;

            // 사용 예시 : 100번 항목을 10개로 수정해주세요.
            // http://localhost:9000/cart/edit/100?quantity=10
            // 백엔드에서 @RequestParam을 사용해서 주소창에 ?quantity로 보내는 것임
            // @RequestBody로 하면 parameter로 객체 생성으로 보낼 수 있음
            const url = `${API_BASE_URL}/cart/edit/${cartProductId}?${parameter}`;

            // patch 동작은 전체가 아닌 일부 데이터를 변경하고자 할때 사용됨
            // 스프링의 WebConfig 클래스안의 addCorsMappings() 메소드를 참조하길 바람
            const response = await customAxios.patch(url, {}, {
                withCredentials: true  // ✅ 인증 정보를 함께 전송
            });

            console.log(response.data || '');

            // cartProducts의 수량 정보를 갱신
            setCartProducts((previous) => {
                const updatedProducts = previous.map((product) =>
                    product.cartProductId === cartProductId
                        ? { ...product, quantity: quantity }
                        : product
                );

                refreshOrderTotalPrice(updatedProducts);
                return updatedProducts;
            });

        } catch (error) {
            console.log('카트 상품 수량 변경 실패');
            console.log(error);
        }

    };

    return (
        <Container className="mt-4">
            <h2 className="mb-4">
                {/* xxrem은 주위 글꼴의 xx배를 의미 */}
                <span style={{ color: 'blue', fontSize: '2rem' }}>{user?.name}</span>
                <span style={{ fontSize: '1.3rem' }}>님의 장바구니</span>
            </h2>
            <Table striped bordered>
                <thead>
                    <tr>
                        <th style={thStyle}>
                            <Form.Check
                                type="checkbox"
                                label="전체 선택"
                                // 전체 선택 "checkbox"의 onChange 이벤트 구현
                                onChange={(event) => toggleAllCheckBox(event.target.checked)}
                            />
                        </th>
                        <th style={thStyle}>상품 정보</th>
                        <th style={thStyle}>수량</th>
                        <th style={thStyle}>금액</th>
                        <th style={thStyle}>삭제</th>
                    </tr>
                </thead>
                <tbody>
                    {cartProducts.length > 0 ? (
                        cartProducts.map((product) => (
                            <tr key={product.cartProductId}>
                                <td className="text-center align-middle">
                                    <Form.Check
                                        type="checkbox"
                                        checked={product.checked}
                                        // Check박스의 값이 바뀔때마다 해당 함수 실행 (해당 매개변수)
                                        onChange={() => toggleCheckBox(product.cartProductId)}
                                    />
                                </td>
                                <td className="text-center align-middle">
                                    <Row> {/* 좌측 4칸은 이미지 영역, 우측 8칸은 상품 이름 영역 */}
                                        <Col xs={4}>
                                            <Image
                                                src={`${API_BASE_URL}/images/${product.image}`}
                                                thumbnail
                                                alt={product.name}
                                                width={`80`}
                                                height={`80`}
                                            />
                                        </Col>
                                        <Col xs={8} className="d-flex align-items-center">
                                            {product.name}
                                        </Col>
                                    </Row>
                                </td>
                                <td className="text-center align-middle">
                                    <Form.Control
                                        type="number"
                                        min={1}
                                        value={product.quantity}
                                        style={{ width: '80px', margin: '0 auto' }}
                                        // 수량 변경 입력 상자
                                        onChange={(event) =>
                                            changeQuantity(
                                                product.cartProductId,

                                                // HTML에서 모든 양식에 있는 값을 String으로 생각함
                                                // event.target.value : 방금 수정한(change)한 값(숫자여도 문자열임)
                                                // 문자열인 해당 값을 정수형으로 바꿔줌
                                                parseInt(event.target.value),
                                                product.productId
                                            )}
                                    />
                                </td>
                                <td className="text-center align-middle">
                                    {(product.price * product.quantity).toLocaleString()} 원
                                </td>
                                <td className="text-center align-middle">
                                    <Button variant="danger" size="sm"
                                    >
                                        삭제
                                    </Button>
                                </td>
                            </tr>
                        ))
                    ) : (
                        <tr><td>장바구니가 비어 있습니다.</td></tr>
                    )}
                </tbody>
            </Table>

            {/* 좌측 정렬(text-start), 가운데 정렬(text-center), 우측 정렬(text-end) */}
            {/* 5) 하단 총 주문 금액 */}
            {/* JS영역의 데이터를 사용해서 {}중괄호 사용 */}
            {/* int인 orderTotalPrice를 HTML에 사용하기 위해 toLocaleString()로 String으로 변환 */}
            <h3 className="text-end mt-3">총 주문 금액 : {orderTotalPrice.toLocaleString()}원</h3>
            <div className="text-end">
                <Button variant="primary" size="lg" >
                    주문하기
                </Button>
            </div>
        </Container>
    );
}

export default App;
```



#### \# CartProductService / CartController (스프링) 둘다 코드 수정
-  CartProductService
```java
package com.coffee.service;

import com.coffee.entity.CartProduct;
import com.coffee.entity.Product;
import com.coffee.repository.CartProductRepository;
import com.coffee.repository.ProductRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service // Service 객체 의미 // 서비스는 로직을 처리함
@RequiredArgsConstructor
public class CartProductService {
    private final CartProductRepository cartProductRepository ;

    // 메소드의 3요소 (반환타입, 메소드명, 매개변수)를 만드는데 시간이 많이 걸림 (연습필요)
    public void saveCartProduct(CartProduct cp){ // CartProduct 하나 입력 받아서 저장
        this.cartProductRepository.save(cp);
    }

    private final ProductRepository productRepository ;

    public String editCartProductQuantity(Long cartProductId, Integer quantity, Long productId){
        // 수량 검증
        if(quantity == null || quantity <1){
            return "오류 : 장바구니 품목은 최소 1개 이상이어야 합니다.";
        }

        // 재고 수량 점검
        Optional<Product> productOptional = productRepository.findById(productId);
        if (productOptional.isEmpty()){ // 상품 재고가 없을때
            return "오류 : 상품 정보를 찾을 수 없습니다.";
        }

        int stock = productOptional.get().getStock();
        if (quantity > stock){ // 손님이 입력한 수보다 재고가 부족할 경우
            return "오류 : 재고 수량이 부족합니다.";
        }

        // 해당 카트 상품 찾기
        // Optional이 java.util이라는 것을 무조건 외우기
        // service 코딩 중이니까 Repository한테 물어봐야 함
        // findById는 CrudRepository에 있음 (상속 느껴보기)
        Optional<CartProduct> cartProductOptional = cartProductRepository.findById(cartProductId);

        // Optional 클래스도 나중에 한 번 공부 해오기
        if (cartProductOptional.isEmpty()){
            return "오류 : 카트 품목을 찾을 수 없습니다.";
        }

        // 수량 변경
        // 값을 가지고 있다는 전제하에
        // Optional클래스와 get()메소드는 거의 정형화된 패턴이여서 기억해두기
        CartProduct cartProduct = cartProductOptional.get();
        // 덮어쓰기하는 경우
        cartProduct.setQuantity(quantity);
        // 만약에 누적을 할 경우 (누적 변경시 다음과 같이 코딩합니다.)
        // cartProduct.setQuantity(cartProduct.getQuantity() + quantity);


        // 데이터 베이스에 저장
        cartProductRepository.save(cartProduct);

        // 성공 메시지 반환
        String message = "카트 상품 아이디 " + cartProductId + "번이 " + quantity + "개로 수정이 되었습니다." ;
        return message ;
    }
}
```


- CartController
```java
package com.coffee.controller;

import com.coffee.dto.CartItemDto;
import com.coffee.dto.CartProductDto;
import com.coffee.entity.Member;
import com.coffee.service.CartProductService;
import com.coffee.service.CartService;
import com.coffee.service.MemberService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequiredArgsConstructor
@RequestMapping("/cart")
public class CartController {
    private final CartService cartService ;

    @PostMapping("/insert") // /cart/insert
    public ResponseEntity<String> addToCart(@RequestBody CartProductDto dto,
                                            Authentication authentication){
        String email = authentication.getName() ;
        String message = cartService.addProductToCart(dto, email);

        return ResponseEntity.ok(message) ;
    }

    private final MemberService memberService ;

    @GetMapping("/list")
    public ResponseEntity<List<CartItemDto>> getCartProducts(Authentication authentication){
        String email = authentication.getName();

        Member member = memberService.findByEmail(email) ;

        if (member == null){
            new RuntimeException("사용자가 존재하지 않습니다.");
        }

        return ResponseEntity.ok(cartService.getCartItemsByMemberId(member.getId())) ;
    }

    private final CartProductService cartProductService ;

    // ""안에 있으면 {}라고 써도 문자열{}로 나올 줄 알았는데 아닌가봄
    @PatchMapping("/edit/{cartProductId}")
    public ResponseEntity<String> editCartProductQuantity(
            @PathVariable Long cartProductId,
            @RequestParam(required = false) Integer quantity,
            @RequestParam(required = false) Long productId){
        System.out.println("카트 상품 아이디 : " + cartProductId);
        System.out.println("변경할 갯수 : " + quantity);
        System.out.println("상품 아이디 : " + productId);

        String message = cartProductService.editCartProductQuantity(cartProductId, quantity, productId) ;

        if (message.startsWith("오류")){// CartProductService에 해당 함수에 if문으로 오류가 return되는 경우 이용
            return ResponseEntity.badRequest().body(message) ;
        }else{
            return ResponseEntity.ok(message) ;
        }
    }
}
```



#### \# 제06장-04. 카트 상품 삭제 기능
#### \# 카트 목록(삭제 함수) (리액트) (06.장바구니.txt)
(pages - CartList에 코드 추가)

파일 참조 : CartList06.txt

1) 카트 목록(삭제 함수)
deleteCartProduct() 함수
	장바구니에서 특정 상품을 삭제하는 기능을 담당하는 React 함수입니다.

2) 삭제 \<Button\>에 onClick 이벤트 연동하기
```typescript
<Button variant="danger" size="sm"
	onClick={() => deleteCartProduct(product.cartProductId)}
>
```


- 코드 추가
```typescript
// 1) 카트 목록(삭제 함수)
const deleteCartProduct = async (cartProductId: number) => {
	const isConfirmed = window.confirm('해당 카트 상품을 정말로 삭제하시겠습니까?');

	if (isConfirmed) {
		try {
			const url = `${API_BASE_URL}/cart/delete/${cartProductId}`;
			const response = await customAxios.delete(url);

			setCartProducts((previous) => {
				// cartProductId : 삭제할 상품
				// bean : 각각 한개
				// filter : 고른거 빼고 나머지 필터링
				const updatedProducts
					= previous.filter((bean) => bean.cartProductId !== cartProductId);

				return updatedProducts;
			});

			alert(response.data);

		} catch (error) {
			console.log('카트 상품 삭제 동작 오류');
			console.log(error);
		}
	} else {
		alert(`'카트 상품' 삭제를 취소하셨습니다.`);
	}
};
```


2) 삭제 \<Button\>에 onClick 이벤트 연동하기
```typescript
<Button variant="danger" size="sm"
	onClick={() => deleteCartProduct(product.cartProductId)}
>
	삭제
</Button>
```



#### \# 서비스(CartProductService) (스프링) (06.장바구니.txt)
(service - CartProductService에 코드 추가)
```java
	public void deleteCartProductById(Long cartProductId) 메소드 구현
```

- 코드 추가 (맨 밑에)
```java
public void deleteCartProductById(Long cartProductId){
	cartProductRepository.deleteById(cartProductId);
}
```


#### \# 컨트롤러(Cart) (스프링) (06.장바구니.txt)
(controller - CartController에 코드 추가)
```java
	public ResponseEntity<String> deleteCartProduct(@PathVariable Long cartProductId) 메소드 구현
```

- 코드 추가 (맨 밑에)
```java
@DeleteMapping("/delete/{cartProductId}")
public ResponseEntity<String> deleteCartProduct(@PathVariable Long cartProductId){
	System.out.println("삭제할 카트 상품 아이디 : " + cartProductId);

	cartProductService.deleteCartProductById(cartProductId);

	String message = "카트 상품 " + cartProductId + "번이 장바구니 목록에서 삭제되었습니다.";
	return ResponseEntity.ok(message) ;
}
```


#### \# 테스트 시나리오 (06.장바구니.txt)
	로그인한 고객의 장바구니에 담겨 있는 상품에 대하여 '삭제' 버튼으로 테스트를 진행해 보도록 합니다.



\---------------------------------------------------------------------------------------
2026.04.15(수).txt 까지 마무리 함
