---
title: 2026-04-02 React HomePage와 Member JPA/Security 시작
created: 2026-07-06
updated: 2026-07-15
type: summary
tags: [spring-boot, react, typescript, frontend, backend, auth, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md
status: growing
confidence: high
---

# 2026-04-02 React HomePage와 Member JPA/Security 시작

## 한 줄 요약

오전에는 Spring의 `/images/**` 응답을 React Bootstrap Carousel로 조립해 HomePage를 완성하고, 오후에는 MySQL/JPA 설정→`Role`·`Member` Entity→Validation→Spring Security→Repository 테스트와 DI로 회원 기능의 저장·보안 기반을 시작했다.

## 왜 이 순서로 배웠는가

전날 마련한 정적 이미지 경로가 실제 React UI에 쓰이는지 먼저 확인해 Fruit 연동 단원을 화면까지 마무리했다. 이후 회원 기능으로 전환해 DB 연결과 Entity 매핑을 만들고 입력 검증과 Security를 붙였다. Security 추가 직후 기존 이미지/API 접근이 막히는 결과를 관찰하고 허용 경로를 설정한 뒤 Repository와 PasswordEncoder를 주입해 저장 테스트로 이어갔다.

## 교시 흐름

### 1. 오전: Spring 이미지 응답을 HomePage에 사용

- Spring의 9000번 `/images/whitewine01_bigsize.png`를 직접 열어 resource handler가 이미지를 반환하는지 확인했다.
- `template.tsx`와 `HomePage.tsx`를 만들고 React Bootstrap의 `Carousel`을 사용했다.
- JSX에서는 HTML의 `class` 대신 `className`을 사용하고 `API_BASE_URL`과 `/images/` 경로를 표현식 안에서 조합해 이미지 URL을 구성했다.
- 여러 빵·커피·와인 이미지를 Carousel item으로 구성하고 `AppRoutes`의 `/` path를 `HomePage`에 연결했다.

### 2. 오후 전환: MySQL·JPA 설정

- MySQL connector와 Spring Data JPA 의존성을 확인하고 `coffee` DB URL, driver, SQL 출력, `ddl-auto=create`, MySQL dialect를 설정했다.
- ORM을 Java class/field와 DB table/column을 매핑하는 것으로 설명하고 JPA가 관리하는 클래스를 Entity라고 구분했다.
- `Role` enum에 `USER`, `ADMIN`을 두고 회원 한 명을 나타내는 `Member` 클래스를 만들었다.

### 3. `Member` Entity와 Validation

- `Member`를 `members` table에 매핑하고 자동 생성 id, name, unique·non-null email, password, address, role, regdate 필드를 구성했다.
- Validation 의존성을 추가한 뒤 이름·이메일·비밀번호·주소에 필수 입력, 이메일 형식, 비밀번호 길이·대문자·특수문자 조건을 붙였다.
- Spring Boot를 실행해 JPA가 table·column·constraint를 생성하도록 하고 MySQL Workbench에서 존재를 확인했다.

### 4. Spring Security 추가로 생긴 접근 변화

- Security 의존성을 추가하자 `/fruit`가 기본 login으로 redirect되고 React HomePage 이미지도 인증 정책 때문에 보이지 않는 현상을 확인했다.
- `SecurityConfig`에서 이미지·과일·정적 리소스·회원 가입/로그인 경로를 허용하고 나머지 요청에는 인증을 요구하도록 filter chain을 구성했다. CSRF는 수업 단계에서 비활성화하고 CORS를 활성화했다.
- 설정 뒤 React의 `/`, `/fruit`, `/fruit/list`와 이미지를 다시 확인했다. 이는 커스텀 로그인 완성이 아니라 Security 기본 동작과 허용 경로의 시작이다.

### 5. Repository 테스트와 DI

- `MemberRepository`가 `JpaRepository<Member, Long>`을 상속하도록 만들었다.
- `SecurityConfig`에 `PasswordEncoder` Bean을 등록하고 `MemberTest`가 Repository와 encoder를 생성자 주입받도록 구성했다.
- 테스트에서 관리자 Member를 만들고 비밀번호를 encode한 뒤 repository에 저장했다. Workbench에서 `members`의 한 행을 조회해 결과를 확인했다.

## 대표 artifact와 입력 → 처리 → 결과

| 구간 | 대표 artifact | 입력 | 처리 | 결과 |
|---|---|---|---|---|
| 홈 화면 | `HomePage.tsx`, `AppRoutes.tsx` | React `/` 진입 | Carousel이 API 기반 이미지 URL 렌더링 | 이미지가 순환하는 HomePage |
| JPA 매핑 | `Role`, `Member`, JPA 설정 | Entity annotation과 앱 실행 | class/field를 table/column·constraint로 매핑 | MySQL 회원 table 생성 |
| 접근 제어 | `SecurityConfig` | 이미지·Fruit·기타 URL 요청 | permit URL과 인증 필요 URL 분기 | 공개 화면 접근, 나머지는 login 요구 |
| 회원 저장 | `MemberRepository`, `PasswordEncoder`, `MemberTest` | 관리자 회원 값 | 비밀번호 encode 후 repository 저장 | `members` 한 행 확인 |

## 실제 혼동 원인

- 원본에서 `ddl-auto=create`와 `update`의 차이를 질문했다. 이날 실제 설정은 `create`였으며 실행 시 schema를 다시 만드는 방식이라 기존 데이터 보존을 전제로 하는 `update`와 같지 않다.
- Validation annotation은 Java 객체 입력값을 검사하고 `@Column`의 unique·nullable 설정은 DB schema 제약과 연결된다. 비슷해 보여도 실행 위치와 책임이 다르다.
- `PasswordEncoder` Bean은 테스트가 비밀번호를 평문 그대로 저장하지 않고 encode한 값을 만들 수 있도록 주입됐다. 이날은 저장 준비이며 JWT 로그인은 아직 구현하지 않았다.
- Security 의존성만 추가해도 기본 정책이 활성화된다. 전날 보이던 이미지와 JSON이 막힌 원인은 React나 CORS 코드가 사라진 것이 아니라 인증 filter가 앞에 생긴 것이다.
- 원본의 DI 설명 중 클래스명을 `Member.java`로 적은 구간이 있으나 실제 전체 코드와 파일 생성 절차는 `MemberTest.java`를 가리킨다.

## 이전·다음 연결과 범위 경계

- 이전: [[summaries/2026-04-01-react-router-spring-boot|04-01]]의 resource handler와 React/Spring 연결을 HomePage 이미지로 사용했다.
- 다음: [[summaries/2026-04-03-spring-member-seed-react-comments|04-03]]에는 SignupPage와 회원 Repository·Service·Controller, `BindingResult`를 연결한다.
- 직접 수업: React Bootstrap HomePage, Member JPA/Validation, Security 기본 정책·허용 경로, Repository 저장 테스트와 DI 시작까지다.
- 후속 확장: 04-03 회원가입, 04-06~07 JWT, 04-08 이후 Product/Cart/Order, Linux·AWS 배포는 별도 후속 수업이다.

## 관련 페이지

- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]
- [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]
- [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]]
- [[comparisons/authentication-vs-authorization|인증 vs 인가]]
- [[entities/react|React]]
- [[entities/spring-boot|Spring Boot]]
- [[entities/mysql|MySQL]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md`
