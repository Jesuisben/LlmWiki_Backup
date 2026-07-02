# \# 순서
###### \# 0부: 준비하기


###### \# 1부: 백엔드 먼저 성공
\[1단계] 백엔드 코드 수정 (properties + Dockerfile)
\[2단계] Docker Hub에 백엔드 저장소 만들기
\[3단계] AWS 구축 (VPC~EC2~RDS)
\[4단계] EC2에 Docker 설치
\[5단계] GitHub Secrets 등록
\[6단계] ci.yml / cd.yml 작성 → push → 자동배포
\[7단계] ★ 백엔드 API 서버에서 도는지 확인



###### \# 2부: 프론트 얹기
\[8단계] React 코드 수정 (API 주소 + nginx)
\[9단계] Docker Hub에 프론트 저장소 추가
\[10단계] 프론트 배포 + nginx 프록시 연결
\[11단계] ★ 도메인 하나로 전체 접속 완성



###### \# 3부: 마무리
\[12단계] 파일을 넣을 로컬 파일 수정
\[13단계] 파일 저장소를 S3로 전환
\[14단계] 도메인 설정
\[15단계] 웹페이지 확인하기
\[16단계] 내 컴퓨터의 MySQL Workbench에 EC2에 설치된 MySQL 컨테이너 연결하기



# \# 0부: 준비하기
###### 1. WebConfig.java 수정
- 코드 복붙
```java
package com.backend_semi.config;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {

    // 임시 방편으로 만들어 놓은 설정
    // CorsConfig.java에 다시 설정해놓음
    /*@Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**")
                .allowedOrigins("http://localhost:5173", "http://localhost:9000")
                .allowedMethods("GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH")
                .allowCredentials(true) ;
    }*/

    @Value("${uploadPath}")
    private String uploadPath ;

    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        registry
                .addResourceHandler("/images/**")
                .addResourceLocations(uploadPath);

    }
}
```


###### 2. CorsConfig.java 생성 및 코드 복붙
- 코드 복붙
```java
package com.backend_semi.config;

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
        // 도메인 주소로 수정
        configuration.setAllowedOriginPatterns(List.of(
                "http://localhost:5173",
                "http://127.0.0.1:5173"
                // 나중에 도메인 주소 추가해야함
                // ex) "https://jesuisben.store" / "https://*.jesuisben.store"
        ));

        // 허용 HTTP 메소드
        // 조회(GET), 등록(POST), 수정(PUT, PATCH), 삭제(DELETE), 예비 요청(OPTIONS)
        configuration.setAllowedMethods(List.of(
                "GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"
        ));

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


###### 3. JWT키 허브에 올리지 않게 설정하기
1) .gitignore
(backend_semi/.gitignore 파일 생성)
- 코드 복붙
\#\# SECRET KEY!!! \#\#
secrets/

2) .dockerignore
(backend_semi/.dockerignore 파일 생성)
- 코드 복붙
secrets/
target/
.git/
\*.md



# \# 1부: 백엔드 먼저 성공
#### \[1단계] 백엔드 코드 수정 (properties + Dockerfile)
###### - application.properties 교체
```java
spring.application.name=backend_semi
server.port=9000

spring.devtools.restart.enabled=true
spring.devtools.livereload.enabled=true

# ${환경변수:기본값} : 환경변수가 있으면 그 환경변수를 사용하고 환경변수가 없다면 기본 값을 사용함
# 로컬에서도 동일하게 돌아가게 하기 위한 설정
# 이미지 경로: 로컬은 C:\shop\images\, 서버는 환경변수로 덮어씀 (S3 전환은 나중에)
productImageLocation=${IMAGE_PATH:C:\\shop\\images\\}
uploadPath=${UPLOAD_PATH:file:///C:/shop/images/}

# DB: 로컬은 내 MySQL, 서버는 RDS 정보를 환경변수로 주입
spring.datasource.url=jdbc:mysql://localhost:3306/wls?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=Asia/Seoul&characterEncoding=UTF-8
spring.datasource.username=${DB_USERNAME:root}
spring.datasource.password=${DB_PASSWORD:mysql}
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver

allowPublicKeyRetrieval=true

spring.jpa.properties.hibernate.show_sql=true
spring.jpa.properties.hibernate.format_sql=true
logging.level.org.hibernate.type.descriptor.sql=trace
spring.jpa.hibernate.ddl-auto=update
spring.jpa.database-platform=org.hibernate.dialect.MySQL8Dialect

# 배포할때 사용할 github의 시크릿에서 가져올 공개키와 비밀키
# 값이 비어있으면 알아서 로컬에서 사용하는 키들의 경로를 이용하게 조건식을 JwtUtil.java에 만들 예정
jwt.private-key=${JWT_PRIVATE_KEY:}
jwt.public-key=${JWT_PUBLIC_KEY:}

# 로컬에서 사용할때 쓰는 키들의 경로
jwt.private-key-path=backend_semi/secrets/jwt-private.pem
jwt.public-key-path=backend_semi/secrets/jwt-public.pem
jwt.expiration=3600000

server.servlet.session.timeout=120m
```


###### - JwtUtil.java 수정
```java
package com.backend_semi.security;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import java.nio.file.Files;
import java.nio.file.Path;
import java.security.KeyFactory;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.spec.PKCS8EncodedKeySpec;
import java.security.spec.X509EncodedKeySpec;
import java.util.Base64;
import java.util.Date;

@Component
public class JwtUtil {

    private final PrivateKey privateKey;
    private final PublicKey publicKey;
    private final long expiration;

    public JwtUtil(
            // 배포할때 사용할 jwt키를 가져오기
            @Value("${jwt.private-key:}") String privateKeyContent,
            @Value("${jwt.public-key:}") String publicKeyContent,
            @Value("${jwt.private-key-path}") String privateKeyPath,
            @Value("${jwt.public-key-path}") String publicKeyPath,
            @Value("${jwt.expiration}") long expiration
    ) {
        try { // 키가 존재하면 키 사용, 키가 없으면 키의 경로로 키를 가져옴
            this.privateKey = loadPrivateKey(resolveKey(privateKeyContent, privateKeyPath));
            this.publicKey = loadPublicKey(resolveKey(publicKeyContent, publicKeyPath));
            this.expiration = expiration;
        } catch (Exception e) {
            throw new IllegalStateException("JWT 키 파일을 읽는 중 오류가 발생했습니다.", e);
        }
    }

    // 키가 있으면 키를 쓰고 키가 없으면 키의 경로를 가져와서 키를 가져오는 함수
    // 이 클래스의 맴버변수의 값을 어떤걸로 넣을지를 결정함
    // 내용이 있으면 그대로, 없으면 경로에서 파일을 읽어 내용 반환
    private String resolveKey(String content, String path) throws Exception {
        if (content != null && !content.isBlank()) {
            return content;
        }
        // 로컬의 경로에 있는 파일을 가져와서 그 내용을 string으로 만들어서 후 처리 안하게 함
        return Files.readString(Path.of(path));
    }

    // 토큰을 만드는 메서드. 회원번호와 아이디, 이름, 그리고 회원롤을 받아서 만든다.
    public String createAccessToken(Long memberId, String loginId, String name, String role) {
        Date now = new Date();
        Date expiryDate = new Date(now.getTime() + expiration);

        return Jwts.builder()
                .subject(String.valueOf(memberId))
                .claim("loginId", loginId)
                .claim("name", name)
                .claim("role", role)
                .issuedAt(now)
                .expiration(expiryDate)
                .signWith(privateKey, Jwts.SIG.RS256) // RS256 알고리즘 사용
                .compact();
    }

    public String getRole(String token){
        Claims claims = parseToken(token);
        return claims.get("role", String.class);
    }

    public Claims parseToken(String token) {
        return Jwts.parser()
                .verifyWith(publicKey)
                .build()
                .parseSignedClaims(token)
                .getPayload();
    }

    public Long getMemberId(String token) {
        Claims claims = parseToken(token);
        return Long.valueOf(claims.getSubject());
    }

    public String getLoginId(String token) {
        Claims claims = parseToken(token);
        return claims.get("loginId", String.class);
    }

    public String getName(String token) {
        Claims claims = parseToken(token);
        return claims.get("name", String.class);
    }

    private PrivateKey loadPrivateKey(String privateKeyContent) throws Exception {
        String key = privateKeyContent
                .replace("-----BEGIN PRIVATE KEY-----", "")
                .replace("-----END PRIVATE KEY-----", "")
                .replaceAll("\\s", "");

        byte[] decodedKey = Base64.getDecoder().decode(key);
        PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(decodedKey);
        KeyFactory keyFactory = KeyFactory.getInstance("RSA");
        return keyFactory.generatePrivate(keySpec);
    }

    private PublicKey loadPublicKey(String publicKeyContent) throws Exception {
        System.out.println("현재 실행 위치 = " + System.getProperty("user.dir"));

        String key = publicKeyContent
                .replace("-----BEGIN PUBLIC KEY-----", "")
                .replace("-----END PUBLIC KEY-----", "")
                .replaceAll("\\s", "");

        byte[] decodedKey = Base64.getDecoder().decode(key);
        X509EncodedKeySpec keySpec = new X509EncodedKeySpec(decodedKey);
        KeyFactory keyFactory = KeyFactory.getInstance("RSA");
        return keyFactory.generatePublic(keySpec);
    }
}
```


###### - pom.xml에 finalName 추가 (\<build> 바로 아래에 추가)
```xml
<!-- 빌드한 파일명을 설정함(cafe.jar) / 기본값은 (cafe-0.0.1-SNAPSHOT.jar) 같은 거임 -->
<finalName>project_test</finalName>
```


###### - SpringDockerfile 생성 (위치 : backend_semi/SpringDockerfile)
```SpringDockerfile
# ===== 1단계: 빌드용 컨테이너 (Maven + JDK 21로 jar 만들기) =====
# eclipse-temurin:21-jdk = "자바21 개발환경"이라는 재료 이미지를 빌려옴
FROM eclipse-temurin:21-jdk AS build
WORKDIR /app

# 메이븐 래퍼와 설정 먼저 복사 (의존성 캐시 활용해서 빌드 빨라짐)
COPY .mvn/ .mvn/
COPY mvnw pom.xml ./
RUN chmod +x mvnw && ./mvnw dependency:go-offline -B || true

# 소스 전체 복사 후 빌드 → target/cafe.jar 생성 (finalName으로 이름 고정했음)
COPY src/ src/
RUN ./mvnw clean package -DskipTests

# ===== 2단계: 실행용 컨테이너 (가벼운 JRE만) =====
# 빌드 도구는 빼고 실행환경만 있는 가벼운 이미지로 갈아탐
FROM eclipse-temurin:21-jre
WORKDIR /app

# 1단계(build)에서 만든 jar만 가져옴
COPY --from=build /app/target/project_test.jar app.jar

# 이미지 임시 폴더 (S3 전환 전까지 임시용)
RUN mkdir -p /app/images

# 컨테이너가 9000번 포트를 쓴다고 표시 (application.properties의 server.port=9000과 일치)
EXPOSE 9000

# 컨테이너가 시작되면 이 명령으로 스프링 실행 (java -jar app.jar)
ENTRYPOINT ["java", "-jar", "app.jar"]
```


###### - mvnw 존재 확인 (중요!)
Dockerfile이 mvnw(메이븐 래퍼)를 사용함.
spring_cafe_ex 폴더에 아래 3개가 있어야 함

mvnw
mvnw.cmd
.mvn/ (폴더)


###### - 로컬에서 실행 테스트 (제일 중요!)
확인해야함



#### \[2단계] Docker Hub에 백엔드 저장소 만들기
###### - 도커 허브 접속 (https://hub.docker.com)
로그인 후 Create repository로 생성
Repository Name : project-test-backend (백엔드 이미지 보관 칸 이름)
Visibility : Public (EC2가 받아갈 수 있게 공개 (학습용))
Description : Spring Boot backend (test) (설명 (선택))

도커 허브 리파지토리 주소가 생성됨 : rktngusals/project-test-backend
나중에 ci.yml에서 어디에 도커 이미지를 올릴지 설정하기 위해서
도커 허브의 리파지토리 주소가 쓰임



#### \[3단계] AWS 구축 (VPC~EC2)
###### - 만들 것들 프리뷰
1. VPC          (네트워크 울타리)
2. 인터넷 게이트웨이 (인터넷 연결 통로)
3. 서브넷        (울타리 안 구역)  - 이번엔 1개면 충분함 RDS 안 쓰니까
4. 라우팅 테이블  (길 안내판)
5. 보안 그룹      (방화벽 - 어떤 문을 열지)
6. 키 페어       (서버 출입 열쇠)
7. EC2          (실제 서버 컴퓨터) - 여기에 다 들어감
8. 탄력적 IP     (고정 주소)



###### - AWS 콘솔 접속해서 로그인하기
(https://aws.amazon.com/ko/)


###### - 1. VPC (네트워크 울타리) (오른쪽 위 지역(Region)이 아시아 태평양(서울) ap-northeast-2인지 확인하기)
1) 개념
AWS 안에 "울타리 친 나만의 네트워크 공간"
앞으로 만들 EC2, RDS가 다 이 울타리 안에 들어감
집 짓기 전에 "땅 구획"부터 정하는 것

2) 실습
VPC 생성
VPC만
이름 태그 : TEST-VPC
IPv4 CIDR 블록 : IPv4 CIDR 수동 입력
IPv4 CIDR : 10.250.0.0/16

나머지는 기본 값 -> VPC 생성


###### - 2. 인터넷 게이트웨이 (인터넷 연결 통로)
1) 개념
VPC(울타리)는 기본적으로 바깥 인터넷이랑 단절되어 있음
인터넷 게이트웨이는 "울타리에 인터넷으로 통하는 대문을 다는 것"
이게 있어야 우리 서버가 인터넷에 연결됨

2) 실습
2-1) 생성
이름 태그: TEST-IGW
인터넷 게이트웨이 생성

2-2) VPC에 연결
작업 - VPC에 연결 - 사용 가능한 VPC (TEST-VPC) - 인터넷 게이트웨이 연결
상태 : Attached 확인


###### - 3. 서브넷 (울타리 안 구역)
1) 개념
VPC라는 큰 울타리 안을 더 잘게 나눈 "구역"
실제 서버(EC2)는 이 구역 안에 들어감
큰 땅(VPC)에 "여기다 집 지을게" 하고 표시한 구획

2) 실습
2-1)
서브넷 클릭 -> 서브넷 생성됨
VPC ID : TEST-VPC
서브넷 이름 : TEST-PUBLIC-SBN-2A
가용 영역 : 아시아 태평양(서울) / ap-northeast-2a
IPv4 서브넷 CIDR 블록 : 10.250.1.0/24 (VPC 범위(10.250.0.0/16) 안의 한 조각. 약 251개 IP를 쓸 수 있음)


###### - 4. 라우팅 테이블  (길 안내판)
1) 개념
라우팅 테이블은 "어디로 가려면 어느 문으로 나가라"는 길 안내판
지금은 서브넷을 만들어도 "인터넷 가려면 게이트웨이로 나가" 라는 안내가 없어서
만들어둔 대문(IGW)을 못 씀. 그 길을 연결해주는 단계

2) 실습
2-1) 생성
라우팅 테이블 클릭 → 라우팅 테이블 생성
이름 : TEST-PUBLIC-RT
VPC : TEST-VPC
-> 라우팅 테이블 생성

(인터넷 게이트웨이 연결)
작업 - 라우팅 편집 - 라우팅 추가
대상 : 0.0.0.0/0
타겟 : 인터넷 게이트웨이 → TEST-IGW 선택
->
0.0.0.0/0 = "모든 목적지(=인터넷 전체)". 즉 "인터넷 어디로든 가려면 TEST-IGW 대문으로 나가라"는 뜻

(서브넷 연결)
작업 - 서브넷 연결 편집 - TEST-PUBLIC-SBN-2A 체크 - 연결 저장


###### - 5. 보안 그룹 (방화벽 - 어떤 문을 열지)
1) 개념
서버로 들어오는 "문"을 어떤 것만 열어둘지 정하는 방화벽
기본적으로 모든 문이 잠겨 있어서, 우리가 쓸 문(포트)만 콕 집어 열어줘야함

2) 실습
보안 그룹 클릭 → 보안 그룹 생성
보안 그룹 이름: TEST-PUBLIC-SG-2A
설명: test security group
VPC: TEST-VPC 선택

인바운드 규칙(들어오는 문) 에서 **규칙 추가**를 눌러 아래 5개를 추가:
유형 | 포트 | 소스 | 무슨 문이냐
SSH | 22 | 0.0.0.0/0 | 서버에 원격 접속(MobaXterm)할 문
HTTP | 80 | 0.0.0.0/0 | 웹사이트 접속 문 (프론트)
HTTPS | 443 | 0.0.0.0/0 | 보안 웹 접속 문
사용자 지정 TCP | 9000 | 0.0.0.0/0 | 백엔드(스프링)가 쓰는 문
사용자 지정 TCP | 3306 | 0.0.0.0/0 | MySQL DB

-> 보안 그룹 생성


###### - 6. 키 페어 (서버 출입 열쇠)
1) 개념
나중에 EC2 서버에 원격 접속할 때 쓰는 "열쇠 파일"
비밀번호 대신 이 열쇠로 서버에 들어감
.pem 파일 (만들 때 딱 한 번만 다운로드됨)
GitHub Secrets에서 이 파일 내용을 통째로 사용 -> 어디 저장했는지 기억하기

2) 실습
EC2 입력 → EC2 서비스로 이동
키 페어 -> 키 페어 생성
이름 : test-keypair
키 페어 유형 : RSA
프라이빗 키 파일 형식 : .pem
-> 키 페어 생성 -> 파일 저장


###### - 7. EC2 (실제 서버 컴퓨터)
1) 개념
지금까지 만든 울타리(VPC)·구역(서브넷)·방화벽(보안그룹) 안에 들어갈 실제 서버 컴퓨터
여기에 우리 도커 컨테이너(백엔드/프론트/MySQL)가 돌아감
진짜 서버를 켜는 것

2) 실습
EC2 - 인스턴스 - 인스턴스 시작
이름 : TEST-PUBLIC-EC2-2A
애플리케이션 및 OS 이미지(Amazon Machine Image) : ubuntu
키 페어 : test-keypair

네트워크 설정 (중요) - 편집 버튼 클릭
VPC : TEST-VPC
서브넷 : TEST-PUBLIC-SBN-2A
퍼블릭 IP 자동 할당 : 활성화 (꺼져 있으면 인터넷에서 서버에 접속을 못함)
방화벽(보안 그룹) : 기존 보안 그룹 선택 → TEST-PUBLIC-SG-2A

스토리지 구성 (저장 용량)
기본값(8GB) -> (14GB로 늘려야 백, 프론트, MySQL 돌아감)

-> 인스턴스 시작

3) 점검
EC2 콘솔 → 인스턴스 → 방금 만든 TEST-PUBLIC-EC2-2A 클릭 → 아래 세부 정보 탭에서:
상태 : 실행 중(running)
퍼블릭 IPv4 주소 : (예: 3.34.xxx.xxx) - 비어 있으면 안됨
VPC: TEST-VPC
서브넷: TEST-PUBLIC-SBN-2A
보안 그룹: TEST-PUBLIC-SG-2A


###### - 8. 탄력적 IP (고정 주소) (EC2에 연결돼 있을 때만 무료)
1) 개념
EC2의 퍼블릭 IP는 서버를 껐다 켜면 바뀜
주소가 자꾸 바뀌면 곤란함 (도메인 연결, 접속 설정이 다 틀어짐)
탄력적 IP는 "안 바뀌는 고정 주소"를 서버에 붙여주는 것

2) 실습
EC2 - 탄력적 IP
탄력적 IP 주소 할당 클릭 → 그대로 할당 클릭
작업 → 탄력적 IP 주소 연결
인스턴스: TEST-PUBLIC-EC2-2A 선택
프라이빗 IP: 자동으로 뜨는 거 선택
-> 연결

탄력적 IP 주소 : 54.116.102.181

연결되면 이 고정 IP가 서버 주소가 됨
나중에 5단계(GitHub Secrets의 EC2_HOST)랑 브라우저 접속에 사용하는 IP주소임



#### \[4단계] EC2에 Docker 설치
###### 1. MobaXterm 실행 + EC2 접속
1) Session - SSH
Remote host : 54.116.102.181 (본인 탄력적 IP)
Specify username 체크 : ubuntu


###### - Advanced SSH settings 탭 클릭
Use private key 체크 → 폴더 아이콘 눌러서 test-keypair.pem 파일 선택
ok 클릭

\*\* 중요!!! 스왑 메모리 생성 \*\*
아래 코드 복붙해서 스왑메모리 2GB 생성하기

```bash
sudo swapoff /swapfile 2>/dev/null
sudo rm -f /swapfile
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

free -h
```

