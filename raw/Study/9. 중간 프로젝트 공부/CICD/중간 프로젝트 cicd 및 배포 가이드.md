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
```dockerfile
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
##### 1. MobaXterm 실행 + EC2 접속
1) Session - SSH
Remote host : 54.116.102.181 (본인 탄력적 IP)
Specify username 체크 : ubuntu

###### - Advanced SSH settings 탭 클릭
Use private key 체크 → 폴더 아이콘 눌러서 test-keypair.pem 파일 선택
ok 클릭

\*\* 중요!!! 스왑 메모리 생성 \*\*
아래 코드 복붙해서 스왑메모리 2GB 생성하기

```shell
sudo swapoff /swapfile 2>/dev/null
sudo rm -f /swapfile
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

free -h
```


##### 2. EC2 서버 도커 설치
###### - 최신 상태 업데이트
sudo apt update

###### - Docker 설치
1) 도커를 받기 위한 기본 도구(인증서, 다운로드 도구 등) 설치
sudo apt install -y ca-certificates curl gnupg

2) 도커 공식 키 등록 (도커를 안전하게 받기 위한 공식 서명 키 등록) (진짜 도커임을 확인하는 용도)
```shell
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

3) 도커 저장소 추가 (도커를 어디서 받을지 주소 등록 및 목록 갱신)
```shell
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
```

4) 도커 설치
```shell
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

(설치 확인)
```shell
sudo docker --version
```

(sudo 없이 docker 쓰게 설정 (편의용))
```shell
sudo usermod -aG docker $USER
```


##### 3. MySQL 컨테이너 띄우기 (자동으로 MySQL 도커 이미지도 설치 됨)
```shell
sudo docker run -d \
  --name mysql-db \
  -e MYSQL_ROOT_PASSWORD='root' \
  -e MYSQL_DATABASE=wls \
  -p 3306:3306 \
  --restart unless-stopped \
  mysql:8.0
```

(설명)
docker run -d : 컨테이너를 백그라운드로 실행 (-d = 뒤에서 조용히 돌기)
--name mysql-db : 컨테이너 이름을 mysql-db로 (나중에 이 이름으로 접속)
-e MYSQL_ROOT_PASSWORD=... : DB 비밀번호 설정 → 이거 메모! 5단계에서 씀 (root)
-e MYSQL_DATABASE=coffee : wls라는 빈 DB를 자동 생성 (우리 프로젝트 DB 이름)
-p 3306:3306 : 외부 3306 포트 ↔ 컨테이너 3306 포트 연결
--restart unless-stopped : 서버 재부팅돼도 자동으로 다시 켜짐
mysql:8.0 : MySQL 8.0 이미지 사용 (없으면 자동 다운로드) (도커 이미지)

(확인용)
sudo docker ps


##### 4. MySQL 컨테이너 잘 돌아가는지 확인용
1)  MySQL 컨테이너 안으로 들어가기
```sql
sudo docker exec -it mysql-db mysql -u root -p
```
-> 비밀번호 입력 (root)

2) SQL 프롬프트가 뜨면 입력
```sql
show databases;
```
-> wls 데이터베이스 목록이 나오면 성공

3) 확인하고 나가기
```sql
exit;
```



#### \[5단계] GitHub Secrets 등록
##### 1. GitHub Secrets에 사용하는 정보들 정리
EC2 서버 IP (탄력적 IP) : 
DB 비밀번호 : 
DB 이름 : 
DB 사용자 : 
Docker Hub 백엔드 저장소 : 
키페어 파일 : (위치 기억)


##### 2. 입력하기
1) GitHub 리파지토리 접속 -> Settings -> Secrets and variables -> Actions
-> New repository secret 버튼으로 하나씩 추가하기

| Name            | Secret                 |
| --------------- | ---------------------- |
| DOCKER_USERNAME | {도커 계정 이름}             |
| DOCKER_PASSWORD | {Docker Hub 토큰}        |
| BACKEND_IMAGE   | {도커 허브 리파지토리주소}:latest |
| EC2_HOST        | {EC2 탄력적 IP}           |
| EC2_KEY         | {keypair.pem 내용 전체}    |
| DB_URL          | {DB 주소}                |
| DB_USERNAME     | {DB 관리자 이름}            |
| DB_PASSWORD     | {DB 관리자 비밀번호}          |
| JWT_PRIVATE_KEY | {private.pem 내용 전체}    |
| JWT_PUBLIC_KEY  | {public.pem 내용 전체}     |

2) 도커 허브 로그인 엑세스 토큰 생성
Docker Hub 로그인 → 우측 위 계정 → Account settings → Personal access tokens → Generate new token
설명 : test-access-token
권한 : Read & Write
-> 생성 (한번만 보여주니까 복사해놓기)



#### \[6단계] Spring_ci.yml / Spring_cd.yml 작성 → push → 자동배포
##### 1. 만들 파일 정리 (최상단 루트에 있어야 함!!)
.github/workflows/Spring_ci.yml — 빌드 + 도커 이미지 만들어 Docker Hub에 push (CI)
.github/workflows/Spring_cd.yml — EC2가 이미지 받아서 컨테이너 실행 (CD)


##### 2. Spring_ci.yml
- 코드 작성
```yml
name: Spring CI - Build and Push
# master에 push되고, spring_cafe_ex 폴더가 바뀔 때만 실행
on:
  push:
    branches:
      - master
    paths:
      - 'backend_semi/**'
      - '.github/workflows/Spring_ci.yml'
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      # 1. 코드 가져오기
      - name: Checkout source
        uses: actions/checkout@v4
      # 2. JDK 21 설정
      - name: Set up JDK 21
        uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'
      # 3. Docker Hub 로그인
      - name: Login to DockerHub
        run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin
      # 4. 백엔드 폴더(spring_cafe_ex)의 Dockerfile로 이미지 빌드
      - name: Build Docker Image
        run: docker build -t "${{ secrets.BACKEND_IMAGE }}" -f ./backend_semi/SpringDockerfile ./backend_semi
      # 5. Docker Hub에 push
      - name: Push Docker Image
        run: docker push "${{ secrets.BACKEND_IMAGE }}"
```


##### 3. Spring_cd.yml
- 코드 작성
```yml
name: Spring CD - Deploy to EC2
# CI 워크플로우("Spring CI - Build and Push")가 성공적으로 끝나면 자동 실행
on:
  workflow_run:
    workflows: ["Spring CI - Build and Push"]
    types:
      - completed
jobs:
  deploy:
    runs-on: ubuntu-latest
    # CI가 성공(success)했을 때만 배포 진행
    if: ${{ github.event.workflow_run.conclusion == 'success' }}
    steps:
      # EC2에 SSH 접속해서 배포 명령 실행
      - name: Deploy to EC2
        uses: appleboy/ssh-action@v1.0.3
        with:
          host: ${{ secrets.EC2_HOST }}
          username: ubuntu
          key: ${{ secrets.EC2_KEY }}
          script: |
            # 1. Docker Hub 로그인
            echo "${{ secrets.DOCKER_PASSWORD }}" | sudo docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin
            # 2. 최신 이미지 받기
            sudo docker pull "${{ secrets.BACKEND_IMAGE }}"
            # 3. 기존 백엔드 컨테이너 삭제 (없으면 그냥 넘어감)
            sudo docker rm -f backend-app || true
            # 4. 새 백엔드 컨테이너 실행
            #    --network host: EC2 네트워크 공유 → localhost:3306으로 mysql-db에 연결
            sudo docker run -d \
              --name backend-app \
              --network host \
              --restart unless-stopped \
              -e DB_URL="${{ secrets.DB_URL }}" \
              -e DB_USERNAME="${{ secrets.DB_USERNAME }}" \
              -e DB_PASSWORD="${{ secrets.DB_PASSWORD }}" \
              -e JWT_PRIVATE_KEY="${{ secrets.JWT_PRIVATE_KEY }}" \
              -e JWT_PUBLIC_KEY="${{ secrets.JWT_PUBLIC_KEY }}" \
              "${{ secrets.BACKEND_IMAGE }}"
            # 5. 안 쓰는 옛날 이미지 정리
            sudo docker image prune -f
```


##### 4. 디스크 부족 현상 해결 / 디스크 크기 8GB -> 20GB
\*\* 디스크 부족이 일어나면 생성하기
1) AWS 콘솔에서 볼륨 크기 늘리기
AWS 콘솔 → EC2
왼쪽 메뉴 Elastic Block Store → 볼륨 클릭
작업 → 볼륨 수정
8 → 20 으로 변경
변경 → 확인

2) 리눅스에서 늘어난 공간 인식시키기 (MobaXterm)
```shell
df -h /
lsblk
sudo growpart /dev/nvme0n1 1
sudo resize2fs /dev/nvme0n1p1

df -h /
```

3) 다시 배포하기
GitHub → Actions → "CI - Build and Push" → 최근 실행 → "Re-run all jobs"



#### \[7단계] ★ 백엔드 API 서버에서 도는지 확인
확인하기



# \#2부: 프론트 얹기
#### \[8단계] React 코드 수정 (API 주소 + nginx)
##### 1. 백엔드에 요청하는 주소를 수정하기 (config.tsx)
1) 개념
nginx의 리버스 프록시로 인해 스프링(백엔드)와 리액트(프론트)가 같은 포트번호를 사용하게 되어서
전에 쓰던 API_BASE_URL = `http://localhost:9000`; 은 사용이 안되고
그렇다고 백엔드에 요청하는 API 주소를 ""으로 넣자니 프론트랑 주소가 겹쳐서 문제가 됨
따라서 실무에서는 보통 백엔드에 요청하는 주소는 앞에 /api를 붙여서 사용
그러면 백엔드(controller에 있는 요청주소)의 API 주소를 /api로 다 바꿔야하나 라고 고민이 될 거 같은데
nginx에서 백엔드로 해당 주소 /api\~\~\~로 보낼때 그 주소에 /api를 자동으로 삭제하고 요청하는 설정을 할 수 있어서
백엔드의 컨트롤러 주소도 그냥 놔두면 됨

1-1) 참고로 이렇게 바꾸면 로컬에서는 테스트를 못하기 때문에 로컬 개발용으로 proxy를 하나 만들어서
로컬에서도 돌아가는지 개발용 파일을 만들어서 주소 연결하게 할 예정
따라서 설정 파일을 "로컬 개발용" / "배포용"으로 나눠서 서버 주소를 설정할 예정


2) 실습
(src/config/config.tsx)
API_BASE_URL을 http:\//localhost:9000 → "/api"로 변경.
- 코드 전체 교체
```typescript
// 백엔드 API 요청용 기본 주소
//
// 배포 환경: nginx가 /api 로 시작하는 요청을 백엔드(9000)로 넘겨줌 (/api는 떼고)
// 로컬 개발: vite.config.ts의 proxy가 /api를 localhost:9000으로 넘겨줌
//
// 그래서 절대주소(http://localhost:9000) 대신 상대경로 "/api"를 씀
// → 프론트와 백엔드가 같은 주소로 서비스되므로 호스트/포트를 적을 필요가 없음
export const API_BASE_URL = "/api";

// 앞으로 http://localhost:9000 대신 API_BASE_URL를 사용하면 됨
// 예: `${API_BASE_URL}/product/list` → "/api/product/list"
```


##### 2. 로컬 개발용 주소 설정하는 파일 (vite.config.ts (로컬 개발용))
1) 개념
npm run dev로 로컬에서 띄울 때, /api 요청을 localhost:9000으로 넘기는 proxy
rewrite로 /api를 떼고 넘김 → 백엔드는 원래 경로(/product/list)로 받음.
배포 환경엔 영향 없음 (개발 서버 전용 설정).

2) 실습
(경로 : frontend_semi/vite.config.ts)
문제 생기면 cmd로 react 폴더 찾아가서
npm install -D @rolldown/plugin-babel babel-plugin-react-compiler
모듈 설치 코드 입력

- 코드 전체 교체
```typescript
import { defineConfig } from 'vite'
import react, { reactCompilerPreset } from '@vitejs/plugin-react'
import babel from '@rolldown/plugin-babel'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(),
    babel({ presets: [reactCompilerPreset()] })
  ],
  // 로컬 개발(npm run dev) 시 proxy 설정
  // 프론트가 /api로 요청하면, vite 개발서버가 localhost:9000(백엔드)로 넘겨줌
  // 그리고 /api는 떼고 넘김 (rewrite) → 백엔드는 /product/list 로 받음
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:9000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
      // 이미지 경로도 백엔드로 넘김 (백엔드 WebConfig의 /images/** 처리용)
      '/images': {
        target: 'http://localhost:9000',
        changeOrigin: true,
      },
    },
  },
})
```


##### 3. 배포용 주소 설정하는 파일 (nginx.conf (배포용))
1) 개념
백엔드에 넘길때 백엔드와 프론트가 같은 포트 번호를 사용하게 되어서
백엔드에 요청하는 주소는 /api 넣어서 요청하기로 했는데 프론트에서 백엔드로 요청은 /api를 넣은 주소로 하지만
그걸 실제로 백엔드에 주소로 넘길때는 /api를 제거하고 넣어서 굳이 백엔드의 요청을 받는 컨트롤러의 url을 안바꿔도 되게 하는 설정

-> 나중에 EC2에서 nginx 컨테이너의 설정용 파일에 덮어쓰기 함

1-1) 개념 by 클로드
/api/... → 백엔드(9000)로 넘김 (proxy_pass 끝 / 로 /api 제거)
/images/... → 백엔드로 넘김 (이미지용)
그 외 / → React 화면 (try_files로 SPA 라우팅 처리)

2) 실습
(경로 : frontend_semi/nginx.conf 파일 생성)
- 코드 작성
```nginx
server {
    listen 80;
    server_name _;

    # React 빌드 결과물이 있는 위치
    root /usr/share/nginx/html;
    index index.html;

    # 1) API 요청: /api로 시작하면 백엔드(9000)로 넘김
    #    proxy_pass 끝의 / 가 핵심 → /api를 떼고 넘김
    #    예: /api/product/list → 백엔드는 /product/list 로 받음
    location /api/ {
        proxy_pass http://localhost:9000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # 2) 이미지 요청: /images로 시작하면 백엔드로 넘김
    #    (백엔드 WebConfig가 /images/** 를 처리함. S3 전환 전까지)
    location /images/ {
        proxy_pass http://localhost:9000/images/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    # 3) 그 외 모든 요청: React 화면으로
    #    React Router 때문에 새로고침해도 404 안 나게 index.html로 fallback
    location / {
        try_files $uri $uri/ /index.html;
    }
}
```


##### 4. ReactDockerfile 생성
1) 개념
도커 이미지 빌드용 도커 파일

2) 실습
(경로 : frontend_semi/ReactDockerfile)
- 코드 작성
```dockerfile
# ===== 1단계: React 빌드 =====
# node 환경에서 npm install + npm run build → dist 폴더 생성
FROM node:20 AS build
WORKDIR /app

# package.json 먼저 복사해서 의존성 설치 (캐시 활용)
COPY package*.json ./
RUN npm install

# 소스 전체 복사 후 빌드
COPY . .
RUN npm run build

# ===== 2단계: nginx에 빌드 결과물 담기 =====
FROM nginx:alpine

# 1단계에서 만든 빌드 결과물(dist)을 nginx 웹 폴더로 복사
COPY --from=build /app/dist /usr/share/nginx/html

# 우리가 만든 nginx 설정으로 교체 (기본 설정 덮어씀)
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```



#### \[9단계] Docker Hub에 프론트 저장소 추가
##### 1. Docker Hub에 프론트 저장소(project-test-frontend) 만들기
이름 : project-test-frontend
설명 : React frontend (test)
Visibility : Public


##### 2. GitHub Secrets에 프론트 이미지 주소 추가
GitHub → Settings → Secrets and variables → Actions → New repository secret:
Name : FRONTEND_IMAGE
Secret : (도커 허브 프론트엔드 리파지토리 주소):latest


##### 3. 프론트용 React_ci.yml, React_cd.yml 만들기
(WLS-Project/.github/workflows/이 경로에 React_ci.yml, React_cd.yml 생성)
1) React_ci.yml
- 코드 작성
```yml
name: React CI - Build and Push

# master에 push되고, frontend_semi 폴더가 바뀔 때만 실행
on:
  push:
    branches:
      - master
    paths:
      - 'frontend_semi/**'
      - '.github/workflows/React_ci.yml'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout source
        uses: actions/checkout@v4

      - name: Login to DockerHub
        run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin

      # 프론트 폴더(frontend_semi)의 ReactDockerfile로 이미지 빌드
      - name: Build Docker Image
        run: docker build -t "${{ secrets.FRONTEND_IMAGE }}" -f ./frontend_semi/ReactDockerfile ./frontend_semi

      - name: Push Docker Image
        run: docker push "${{ secrets.FRONTEND_IMAGE }}"
```


2) React_cd.yml
```yml
name: React CD - Deploy to EC2

# React CI가 성공으로 끝나면 자동 실행
on:
  workflow_run:
    workflows: ["React CI - Build and Push"]
    types:
      - completed

jobs:
  deploy:
    runs-on: ubuntu-latest
    if: ${{ github.event.workflow_run.conclusion == 'success' }}
    steps:
      - name: Deploy to EC2
        uses: appleboy/ssh-action@v1.0.3
        with:
          host: ${{ secrets.EC2_HOST }}
          username: ubuntu
          key: ${{ secrets.EC2_KEY }}
          script: |
            # 1. Docker Hub 로그인
            echo "${{ secrets.DOCKER_PASSWORD }}" | sudo docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin

            # 2. 최신 프론트 이미지 받기
            sudo docker pull "${{ secrets.FRONTEND_IMAGE }}"

            # 3. 기존 프론트 컨테이너 삭제 (없으면 그냥 넘어감)
            sudo docker rm -f frontend-app || true

            # 4. 새 프론트 컨테이너 실행 (nginx, 80포트)
            #    --network host: nginx가 localhost:9000(백엔드)로 /api 요청 넘김
            sudo docker run -d \
              --name frontend-app \
              --network host \
              --restart unless-stopped \
              "${{ secrets.FRONTEND_IMAGE }}"

            # 5. 안 쓰는 옛날 이미지 정리
            sudo docker image prune -f
```



#### \[10단계] 프론트 배포 + nginx 프록시 연결
push → 프론트 배포



#### \[11단계] ★ 도메인 하나로 전체 접속 완성
성공



# \#3부: 마무리
#### \[12단계] 파일을 넣을 로컬 파일 수정
##### 1. pom.xml — S3 SDK 의존성 추가
backend_semi/pom.xml의 \<dependencies> 안에 추가하고 Maven 새로고침하기
(로컬 단계에선 안 쓰지만 미리 넣어두면 S3 전환 때 안 건드려도 됨)

- 코드 추가
```xml
<!-- AWS S3 SDK v2 (파일을 S3에 업로드/삭제) -->
<dependency>
    <groupId>software.amazon.awssdk</groupId>
    <artifactId>s3</artifactId>
    <version>2.46.5</version>
</dependency>
```


##### 2. application.properties — 파일/S3 설정 추가
backend_semi/src/main/resources/application.properties 맨 아래에 추가.
핵심은 S3_ACCESS_KEY의 기본값이 비어있다(:})는 것
로컬에선 환경변수를 안 주니까 빈 값 → 로컬 모드.\
배포 서버에선 GitHub Secrets로 키를 주입 → S3 모드.

C드라이브에 /upload/files 경로에 폴더 생성하기 (로컬 저장 폴더)

- 코드 추가
```java
# ===== 파일 업로드 설정 =====
# 로컬 저장 폴더 (서버에선 환경변수로 덮어씀)
file.upload-dir=${FILE_UPLOAD_DIR:C:/upload/files}
# 브라우저 접근 경로 접두사
file.access-prefix=/files

# 멀티파트 용량 제한 (기본 1MB라 일반 파일엔 너무 작음)
spring.servlet.multipart.max-file-size=100MB
spring.servlet.multipart.max-request-size=100MB

# ===== AWS S3 설정 (로컬 땐 키가 비어있어서 로컬 모드로 동작) =====
# 키가 채워지면 자동으로 S3 모드로 전환됨
cloud.aws.s3.bucket=${S3_BUCKET:}
cloud.aws.region=${S3_REGION:ap-northeast-2}
cloud.aws.credentials.access-key=${S3_ACCESS_KEY:}
cloud.aws.credentials.secret-key=${S3_SECRET_KEY:}
```


##### 3. FileService.java — 새로 생성 (이거 하나가 핵심) (이해하기 어려움)
(backend_semi/src/main/java/com/backend_semi/service/FileService.java)
로컬/S3 분기를 이 안에서 if 하나로 처리해. 컨트롤러는 이게 로컬인지 S3인지 몰라도 됨.
- 코드 작성
```java
package com.backend_semi.service;

import jakarta.annotation.PostConstruct;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;
import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.DeleteObjectRequest;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;

import java.io.File;
import java.io.IOException;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.UUID;

@Service
public class FileService {

    // ===== 로컬 저장용 =====
    @Value("${file.upload-dir}")
    private String uploadDir;        // 실제 저장 폴더
    @Value("${file.access-prefix}")
    private String accessPrefix;     // 브라우저 접근 경로 (/files)

    // ===== S3용 (키가 비어있으면 로컬 모드) =====
    @Value("${cloud.aws.s3.bucket:}")
    private String bucket;
    @Value("${cloud.aws.region:}")
    private String region;
    @Value("${cloud.aws.credentials.access-key:}")
    private String accessKey;
    @Value("${cloud.aws.credentials.secret-key:}")
    private String secretKey;

    // 환경변수로 만들어진 S3 클라이언트
    private S3Client s3Client;

    // 액세스 키가 있을 때만 S3 클라이언트를 미리 만들어둠
    @PostConstruct
    public void init() {
        if (isS3Mode()) {
            AwsBasicCredentials credentials = AwsBasicCredentials.create(accessKey, secretKey);
            this.s3Client = S3Client.builder()
                    .region(Region.of(region))
                    .credentialsProvider(StaticCredentialsProvider.create(credentials))
                    .build();
            System.out.println("[FileService] S3 모드로 동작합니다. bucket=" + bucket);
        } else {
            System.out.println("[FileService] 로컬 모드로 동작합니다. dir=" + uploadDir);
        }
    }

    // 키가 채워져 있으면 S3 모드, 비어있으면 로컬 모드
    // 위에 init() 함수에서 사용
    private boolean isS3Mode() {
        return accessKey != null && !accessKey.isBlank();
    }

    // 파일 저장 → 접근 가능한 URL(또는 경로) 반환
    public String upload(MultipartFile file) {
        if (file == null || file.isEmpty()) {
            throw new IllegalArgumentException("업로드할 파일이 없습니다.");
        }

        // 원본 확장자 추출 (ex : report.pdf → .pdf)
        String original = file.getOriginalFilename();
        String ext = "";
        if (original != null && original.contains(".")) {
            ext = original.substring(original.lastIndexOf("."));
        }

        // 겹치지 않는 파일명 (시간 + 랜덤 + 확장자)
        String time = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyyMMddHHmmss"));
        String savedName = "file_" + time + "_" + UUID.randomUUID().toString().substring(0, 8) + ext;

        if (isS3Mode()) {
            // ----- S3 업로드 -----
            // 원본 파일명을 다운로드 시 보여줄 이름으로 사용 (한글 안전하게 인코딩)
            String downloadName = (original != null && !original.isBlank()) ? original : savedName;
            String encodedName = URLEncoder.encode(downloadName, StandardCharsets.UTF_8)
                    .replaceAll("\\+", "%20");

            try {
                PutObjectRequest request = PutObjectRequest.builder()
                        .bucket(bucket)
                        .key(savedName)
                        .contentType(file.getContentType())
                        // 브라우저가 열지 말고 무조건 다운로드하게 강제 (한글 파일명 유지)
                        .contentDisposition("attachment; filename*=UTF-8''" + encodedName)
                        .build();
                s3Client.putObject(request, RequestBody.fromBytes(file.getBytes()));
            } catch (IOException e) {
                throw new RuntimeException("S3 업로드 실패: " + e.getMessage(), e);
            }
            return "https://" + bucket + ".s3." + region + ".amazonaws.com/" + savedName;
            
        } else {
            // ----- 로컬 저장 -----
            File dir = new File(uploadDir);
            if (!dir.exists()) {
                dir.mkdirs();
            }
            try {
                file.transferTo(new File(dir, savedName));
            } catch (IOException e) {
                throw new RuntimeException("파일 저장 실패: " + e.getMessage(), e);
            }
            // 브라우저 접근 경로 반환 (/files/file_xxx.pdf)
            return accessPrefix + "/" + savedName;
        }
    }

    // 파일 삭제 (URL이든 파일명이든 받아서 처리)
    public void delete(String fileUrlOrName) {
        if (fileUrlOrName == null || fileUrlOrName.isBlank()) {
            return;
        }
        // 마지막 / 뒤가 파일명(=S3 키)
        String fileName = fileUrlOrName.substring(fileUrlOrName.lastIndexOf("/") + 1);

        if (isS3Mode()) {
            try {
                s3Client.deleteObject(DeleteObjectRequest.builder()
                        .bucket(bucket)
                        .key(fileName)
                        .build());
            } catch (Exception e) {
                System.out.println("S3 파일 삭제 실패: " + e.getMessage());
            }
        } else {
            File target = new File(uploadDir, fileName);
            if (target.exists()) {
                target.delete();
            }
        }
    }
}
```


##### 4. NoticeController.java — createNotice를 multipart로 수정
1) 기존 createNotice 메서드만 고치면 됨.
@RequestBody(JSON) → @RequestPart(파일 + 데이터)로 바꾸는 게 핵심.

- 기존 코드
```java
@PostMapping
public ResponseEntity<Long> createNotice(
        Authentication authentication,
        @RequestBody NoticeRequestDto request
) {
    String loginId = (String) authentication.getDetails();
    Long noticeId = noticeService.createNotice(loginId, request);
    return ResponseEntity.ok(noticeId);
}

- 수정한 코드 (수정도 동일하게 multipart로 바꿔야함)
// consumes 명시: multipart로 받음 (데이터 + 파일)
@PostMapping(consumes = MediaType.MULTIPART_FORM_DATA_VALUE)
public ResponseEntity<Long> createNotice(
        Authentication authentication,
        // 공지 데이터(JSON 문자열) — 프론트가 "data"라는 파트로 보냄
        @RequestPart("data") NoticeRequestDto request,
        // 첨부파일 — 없을 수도 있으니 required = false
        @RequestPart(value = "file", required = false) MultipartFile file
) {
    String loginId = (String) authentication.getDetails();
    Long noticeId = noticeService.createNotice(loginId, request, file);
    return ResponseEntity.ok(noticeId);
}
```


2) updateNotice (코드 수정)
- 코드 수정
```java
@PutMapping(value = "/{noticeId}", consumes = MediaType.MULTIPART_FORM_DATA_VALUE)
public ResponseEntity<Void> updateNotice(
        Authentication authentication,
        @PathVariable Long noticeId,
        @RequestPart("data") NoticeRequestDto request,
        @RequestPart(value = "file", required = false) MultipartFile file
){
    String loginId = (String) authentication.getDetails();
    noticeService.updateNotice(loginId, noticeId, request, file);
    return ResponseEntity.ok().build();
}
```


##### 5. NoticeService.java — 파일 받아서 업로드 후 URL 저장
FileService 주입받고, createNotice/updateNotice 시그니처에 MultipartFile file을 추가해서 처리.
1) 먼저 필드에 주입 추가
@RequiredArgsConstructor를 쓰고 있으면 final 필드만 추가하면 자동 주입됨
안 쓰면 생성자에 추가해야 함

- 코드 추가
```java
private final FileService fileService;
```


2) createNotice (파일 있으면 올리고 URL을 request에 세팅)
- 코드 수정
```java
@Transactional
public Long createNotice(String loginId, NoticeRequestDto request, MultipartFile file) {
	Member member = memberRepository.findByLoginId(loginId)
			.orElseThrow(() -> new IllegalArgumentException("회원을 찾을 수 없습니다!"));

	if (member.getRole() != Role.ADMIN) {
		throw new IllegalArgumentException("관리자만 공지사항을 작성할 수 있습니다!");
	}

	NoticeCategory noticeCategory = noticeCategoryRepository.findById(request.getNoticeCategoryId())
			.orElseThrow(() -> new IllegalArgumentException("공지사항 카테고리를 찾을 수 없습니다!"));

	// 파일이 있으면 업로드하고 URL을 attachmentUrl로 세팅
	String attachmentUrl = null;
	if (file != null && !file.isEmpty()) {
		attachmentUrl = fileService.upload(file);
	}

	Notice notice = new Notice(
			noticeCategory,        // ← 카테고리를 먼저
			member,                // ← 멤버를 두 번째
			request.getTitle(),
			request.getContents(),
			attachmentUrl
	);

	Notice saved = noticeRepository.save(notice);
	return saved.getNoticeId();
}
```


3) updateNotice 수정 — 새 파일 오면 기존 파일 삭제 후 교체:

- 코드 수정