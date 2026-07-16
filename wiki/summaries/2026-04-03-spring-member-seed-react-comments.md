---
title: 2026-04-03 React 회원가입과 Spring 검증·저장 흐름
created: 2026-07-06
updated: 2026-07-15
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md
status: growing
confidence: high
---

# 2026-04-03 React 회원가입과 Spring 검증·저장 흐름

## 한 줄 요약

Member 테스트 데이터를 정리한 뒤 React `SignupPage`의 입력·검증 표시를 Spring의 `MemberRepository` → `MemberService` → `MemberController`와 연결해, 회원가입 요청이 검증·중복 확인·암호화 저장·HTTP 응답으로 끝나는 흐름을 만들었다.

## 수업 위치와 날짜 연결

- 이전: [[summaries/2026-04-02-react-bootstrap-homepage|2026-04-02]]에 `Member` Entity, Validation, Security, Repository를 시작했다.
- 오늘: 이미 만든 회원 도메인을 실제 React 회원가입 화면과 POST API로 연결했다.
- 다음: [[summaries/2026-04-06-login-jwt-session-cookie|2026-04-06]]에는 가입된 회원으로 로그인하고 JWT를 발급·저장하는 흐름으로 확장한다.

## 실제 교시 흐름

### 1교시 — Member 테스트 데이터와 편집 기본기

- VS Code 한 줄 복사와 JSX 주석 방식을 확인했다.
- `MemberTest`에 회원 두 명을 더 작성하고, 기존 데이터까지 포함해 Repository 저장을 다시 실행했다.
- 같은 unique 데이터를 반복 저장하면 오류가 나므로 MySQL의 기존 `members` 데이터를 지운 뒤 테스트를 실행했고, 총 3개 데이터가 추가되는 흐름을 확인했다.
- `save()`가 `CrudRepository` 계층에서 제공된다는 점을 짚었다.

### 2교시 — CRUD에서 회원가입 화면·라우팅으로 이동

- Create/Read/Update/Delete와 INSERT/SELECT/UPDATE/DELETE의 대응을 확인했다.
- `MenuItems.tsx`에 회원가입 메뉴를 추가하고, `AppRouters.tsx`에서 `/member/signup`을 `SignupPage`와 연결했다.
- Spring `Member.java`를 보며 화면에서 받아야 할 회원가입 항목을 맞췄다.
- 성공 응답을 판단할 때 사용할 200번대 HTTP status code를 확인했다.

### 3~4교시 — JSX event와 오류 표시

- JSX가 XML 문법을 따르며 React event 이름은 `onChange`처럼 `on` 뒤 첫 글자를 대문자로 쓴다는 점을 배웠다.
- 입력 변경 시 event 객체의 `target.value`를 state setter에 전달해 화면 입력과 state를 연결했다.
- `!!errors.name`으로 오류 값의 truthy/falsy를 boolean으로 바꾸고, `isInvalid`와 `Form.Control.Feedback`으로 필드 오류를 표시했다.
- form submit에서는 `event.preventDefault()`로 브라우저 기본 제출 동작을 막고 React 함수가 요청을 담당하게 했다.

### 5교시 — Repository에서 Service로

- `MemberRepository`에 이메일로 회원을 찾는 query method `findByEmail(String email)`을 선언했다.
- `MemberService.findByEmail()`은 Repository 조회를 위임했다.
- `MemberService.insert()`는 가입 요청으로 받은 `Member`에 `Role.USER`와 등록일을 설정하고, 비밀번호를 `PasswordEncoder`로 인코딩한 뒤 Repository에 저장했다.

### 6교시 — Controller에서 JSON 요청 검증

- `MemberController`의 `/member/signup` POST endpoint가 JSON 요청을 `@RequestBody Member`로 받도록 했다.
- `@Valid`와 `BindingResult`를 붙여 Entity에 선언한 Validation 결과를 Controller에서 확인했다.
- 이 단계의 첫 Controller는 오류 여부를 console에 확인하는 형태였고, 다음 교시에서 실제 오류 응답으로 확장했다.

### 7~8교시 — 필드 오류 Map과 가입 결과 응답

- `Map<String, String>`을 별도 Java 실습으로 확인한 뒤, Validation 오류의 필드명과 기본 메시지를 Map에 담았다.
- 잘못된 이름·비밀번호·이메일로 가입을 시도해 Spring console에 필드별 오류가 모이는 것을 확인했다.
- 오류가 있으면 `FieldError` 목록을 Map으로 바꾸어 `BAD_REQUEST`로 반환했다.
- Validation을 통과하면 이메일 중복을 조회하고, 이미 존재하면 email 오류 Map을 `BAD_REQUEST`로 반환했다.
- 중복이 아니면 Service가 회원을 저장하고 `OK`와 `회원 가입 성공`을 반환하도록 완성했다.

## 대표 artifact

| 계층 | 대표 artifact | 오늘 맡은 역할 |
|---|---|---|
| React | `SignupPage.tsx` | 입력 state 갱신, submit 기본 동작 방지, 필드 오류 표시 |
| Routing | `MenuItems.tsx`, `AppRouters.tsx` | 회원가입 메뉴와 `/member/signup` 화면 연결 |
| Repository | `MemberRepository.findByEmail()` | 이메일로 기존 회원 조회 |
| Service | `MemberService.findByEmail()`, `insert()` | 중복 확인 지원, 역할·등록일 설정, 비밀번호 인코딩, 저장 |
| Controller | `MemberController.signup()` | JSON 변환, Validation 결과 수집, 중복 분기, HTTP 응답 |

## 입력 → 처리 → 결과

| 입력 | 처리 | 결과 |
|---|---|---|
| React 회원가입 form의 name·email·password·address | event의 `target.value`로 state 갱신 후 `/member/signup`에 POST | Spring이 JSON을 `Member`로 변환 |
| Validation에 맞지 않는 값 | `@Valid` → `BindingResult` → `FieldError`를 Map으로 변환 | 필드별 오류와 `BAD_REQUEST` 응답 |
| 이미 저장된 email | Service/Repository의 `findByEmail()` 조회 | email 중복 오류와 `BAD_REQUEST` 응답 |
| 유효하고 중복되지 않은 회원 | Service가 role·regdate 설정, password 인코딩, Repository 저장 | `회원 가입 성공`과 `OK` 응답 |

## 실제로 헷갈리기 쉬운 지점

- **화면 오류 표시와 서버 검증은 같은 단계가 아니다.** `isInvalid`는 React가 오류를 보여 주는 방식이고, 실제 가입 허용 여부는 Spring Validation·중복 조회 결과로 결정된다.
- **Controller와 Service의 책임이 다르다.** Controller는 JSON·검증·HTTP 응답을 다루고, Service는 역할·등록일·비밀번호 인코딩·저장을 담당했다.
- **`@RequestBody`는 검증 자체가 아니다.** JSON을 Java 객체로 바꾸는 역할이며, 검증 결과는 `@Valid`와 `BindingResult`로 확인한다.
- **테스트 데이터 초기화는 가입 기능이 아니다.** 오전의 `MemberTest` seed는 실습 준비이고, 오후의 `SignupPage` → Controller 흐름이 실제 회원가입 요청 처리다.

## 직접 수업과 후속 확장 경계

- 직접 구현: Member seed, React 회원가입 화면·event, Repository query method, Service 저장, Controller Validation·중복 확인·응답.
- 다음 수업의 직접 확장: Cookie·Session·JWT 비교, LoginPage, 토큰 생성과 로그인 응답.
- 후속 과목 확장: Product·Cart·Order는 같은 계층 구조를 다른 도메인에 적용한다. Linux·AWS·CI/CD는 이 애플리케이션의 실행·배포 단계이며 오늘 구현한 회원가입 자체가 아니다. Passwordless는 별도 후속 인증 과목이다.

## 관련 페이지

- [[concepts/react-form-state-event|React 폼 상태와 이벤트]]
- [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]
- [[comparisons/controller-service-repository|Controller vs Service vs Repository]]
- [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]
- [[concepts/axios-interceptor-error-handling|Axios interceptor와 API 오류 처리]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md`