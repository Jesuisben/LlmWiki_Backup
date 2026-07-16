---
title: FrontEnd_BackEnd 내용 재고도화 전수 재고와 실행 분할 계획
created: 2026-07-15
updated: 2026-07-16
type: meta
tags: [spring-boot, react, typescript, frontend, backend, auth, curriculum, study-log]
sources:
  - AGENTS.md
  - wiki/index.md
  - wiki/log.md
  - wiki/_meta/wiki-content-rehighquality-work-plan.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md
status: growing
confidence: high
---

# FrontEnd_BackEnd 내용 재고도화 전수 재고와 실행 분할 계획

## 문서 상태와 범위

이 문서는 내용 재고도화 단계 4 `FrontEnd_BackEnd`의 세션 1 재고·분할 계획과 세션 2~16 실행·고정점 결과를 함께 보존한다.

- 세션 16 수정 범위: 확인된 오류가 있던 지식 페이지 7개, 이 meta 문서, 상위 계획, `wiki/index.md`, `wiki/log.md`
- 세션 16에서 수정하지 않은 범위: `raw/`, 오류가 확인되지 않은 기존 지식 페이지 본문
- 과목 완료 상태: **완료 — 세션 16 고정점 통과**
- 다음 과목: 단계 5 Linux는 시작하지 않음
- 완료 선언 시점: 2026-07-16 세션 16의 원문 provenance·구조 고정점 검증 통과 뒤

## 시작 기준선

- 직전 완료 단계: 단계 3 UI&UX 최종 재검증
- UI&UX 최종 수치: raw 96/96, 지식 페이지 24개, code fence 39/39 원문 대조
- 현재 FrontEnd_BackEnd raw scoped Git 상태: 변경 0건
- 현재 FrontEnd_BackEnd raw scoped diff: 변경 0건
- 저장소 전체에는 기존 Java·Oracle·UI&UX wiki 변경과 Python raw 변경이 있으므로 이번 과목 작업과 분리해 보호한다.
- 56개 직접 대응 페이지 중 시작 전부터 diff가 있던 과목 경계 페이지는 5개다: `comparisons/jpql-vs-sql`, `concepts/database-normalization-functional-dependency`, `concepts/oracle-sequence`, `entities/intellij-idea`, `entities/oracle-database`.
- 위 5개는 앞선 Java·Oracle 재고도화 변경이며 이번 세션에서 수정하지 않았다. 나머지 FrontEnd_BackEnd 직접 대응 지식 페이지의 diff는 0개다.

## raw 전수 재고 요약

- 실제 파일: 34개
- Markdown: 19개
  - 날짜별 수업 MD: 18개
  - 과목 총정리 MD: 1개
- PDF: 10개
- PNG: 5개
- 독립 HTML/CSS/JavaScript/Java/TypeScript/SQL/설정 파일: 0개
- 코드·설정 근거는 날짜별 MD와 총정리 MD 안의 fence에 포함되어 있다.
- 0바이트 파일: 0개
- 과목 내부 byte-identical 중복: 0개
- 과목 외부와의 byte-identical 중복: `IntelliJ 교안.pdf` 1건이며 Java 과목의 동일 파일과 같다.

## raw 전체 경로와 역할

### 날짜별 Markdown과 총정리

| ID | 실제 전체 경로 | 실제 수업일 | 핵심 역할·대표 artifact |
|---|---|---|---|
| R01 | `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md` | 2026-03-30 | Spring Boot·React·MySQL·Node.js·VS Code 환경, Vite, `pom.xml`, `application.properties`, Fruit Entity |
| R02 | `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md` | 2026-03-31 | `FruitHtmlController`, template HTML, REST/JSON, `FruitController`, React 진입과 Router |
| R03 | `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md` | 2026-04-01 | `MenuItems`, `Fruit.ts`, `FruitOne`, axios response, CORS, `WebConfig` |
| R04 | `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md` | 2026-04-02 | React Bootstrap HomePage/Carousel, Member JPA, MySQL 연결, Spring Security 시작 |
| R05 | `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md` | 2026-04-03 | SignupPage, JSX event, Repository/Service/Controller, `BindingResult`, 상태 코드 |
| R06 | `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md` | 2026-04-06 | Cookie/Session/JWT, SPA/MPA, stateful/stateless, `axiosInstance`, LoginPage, `JwtTokenProvider` |
| R07 | `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md` | 2026-04-07 | String/Bearer 처리, `JwtAuthenticationFilter`, `SecurityContextHolder`, CORS/SecurityConfig, 로그인 테스트 |
| R08 | `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md` | 2026-04-08 | Category/Product Entity, repository·seed·단위 테스트, Product 목록 API와 React 타입 |
| R09 | `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md` | 2026-04-09 | 상품 삭제, event bubbling, ProductService/Controller, `ProductInsertForm` |
| R10 | `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md` | 2026-04-10 | React Event Object·spread, 상품 등록 state, 수정 화면과 등록/수정 차이 |
| R11 | `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md` | 2026-04-13 | 상품 수정·상세, `useEffect`, GET/PUT 테스트, Cart/CartProduct 연관관계 시작 |
| R12 | `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md` | 2026-04-14 | `CartProductService`, `CartService`, `CartController`, `CartItemDto`, 장바구니 목록 |
| R13 | `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md` | 2026-04-15 | 장바구니 전체/개별 선택, props, 수량 변경, URL parameter, 삭제 |
| R14 | `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md` | 2026-04-16 | 장바구니 재고 보정, OrderStatus, Order/OrderProduct/DTO, cascade, 주문 생성 |
| R15 | `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md` | 2026-04-17 | `Array.some`, 장바구니 합계·주문 함수, OrderList와 주문 상세 DTO/API |
| R16 | `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md` | 2026-04-20 | 주문 목록·상태 변경·완료·취소, 재고 복원, 대표 상품 carousel, JPQL |
| R17 | `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md` | 2026-04-21 | React paging, FieldSearch/SearchCondition, SearchDto, ProductSpecification, CSR/SSR |
| R18 | `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md` | 2026-04-22 | `ProductRepository`, Specification+Pageable Service/Controller, MySQL 검색 시나리오 |
| R19 | `raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md` | 2026-03-30~04-22 복습 | 환경→Fruit→Member/JWT→Product→Cart→Order→검색의 과목 허브; 날짜 MD를 대체하지 않는 보조 복습 원본 |

### PDF 교육자료

| ID | 실제 전체 경로 | 역할·중복 처분 |
|---|---|---|
| P01 | `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/FrontEnd&BackEnd.pdf` | Frontend/Backend 역할과 요청 흐름 보조 교안; 날짜 MD의 직접 실습을 대체하지 않음 |
| P02 | `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/IntelliJ 교안.pdf` | IDE 보조 교안; `raw/KoreaICT/1. Java/교육 자료/IntelliJ 교안.pdf`와 byte-identical이므로 중복 교육자료로 보존하고 별도 사실을 중복 생성하지 않음 |
| P03 | `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/IT 관련 용어.pdf` | JSON·REST·HTTP·CORS·Cookie/Session·상태 코드·MIME·CSR/SSR 용어 보조 근거 |
| P04 | `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/JWT(이론).pdf` | SPA/MPA, Session/JWT, stateful/stateless, JWT 구조·Claims 보조 근거 |
| P05 | `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/My-Sql 설치&설정.pdf` | MySQL 설치·Workbench·초기 DB 연결 보조 근거 |
| P06 | `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/NodeJs.pdf` | Node.js 설치와 React 개발 도구 실행환경 보조 근거 |
| P07 | `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf` | event, spread, Router, Hook, axios 등 React 개념 보조 근거 |
| P08 | `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf` | Spring 구조, JPA, Repository, Security, 연관관계, Pageable 등 백엔드 보조 근거 |
| P09 | `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/VisualStudioCode.pdf` | VS Code 설치·편집 기능 보조 근거 |
| P10 | `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/필드 검색 기능.pdf` | SearchDto·Specification·Pageable 필드 검색의 집중 보조 교안 |

### 이미지 교육자료

| ID | 실제 전체 경로 | 역할 |
|---|---|---|
| I01 | `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 01.png` | 1719×849, CartProduct 중심 다대일 매핑 구조 보조 |
| I02 | `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 02.png` | 1513×701, Cart/CartProduct/Product 매핑 후속 그림 |
| I03 | `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/라우터 설명 그림.png` | 1444×713, React Router를 화면 선택 안내자로 설명하는 비유 |
| I04 | `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/쇼핑 카트 데이터 구조 다이어그램.png` | 1532×981, Member–Cart–CartProduct–Product 관계와 수량 속성 구조 |
| I05 | `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/프로그램 흐름 그림.png` | 1193×675, Controller→Service→Repository→Database와 프로젝트 구성 요소 |

## 중복·보조자료·부재 artifact 경계

- 날짜별 MD가 학습일·실습 순서의 최우선 근거다. PDF와 PNG는 개념·도식·페이지 인용을 보강하지만 날짜 귀속을 새로 만들지 않는다.
- `FrontEnd_BackEnd 총정리.md`는 18개 날짜 MD를 연결하는 복습 허브이며 날짜 summary의 대체 원본이 아니다.
- `IntelliJ 교안.pdf`의 과목 간 중복은 파일 삭제·통합 대상이 아니라 보존해야 할 교육자료 중복이다.
- 날짜 MD가 언급하는 `03.기본기 다지기.txt`, `04.회원.txt`, `05.상품.txt`, `06.장바구니.txt`, `07.주문.txt`, `08.페이징과 필드 검색.txt`, `장바구니.zip`은 현재 과목 폴더의 독립 파일 재고에 없다. 따라서 현재 wiki는 날짜 MD에 전사된 내용과 실제 보유 PDF/PNG까지만 직접 근거로 삼는다.
- 독립 소스 코드·설정 파일이 없으므로 향후 code fence provenance는 해당 날짜 MD 또는 총정리 MD의 공백 정규화 연속 부분문자열로 검증한다. 서로 다른 날짜의 조각을 합성하지 않는다.

## 기존 wiki 대응 범위

직접 범위는 frontmatter `sources`에서 `raw/KoreaICT/4. FrontEnd_BackEnd`를 실제 참조하는 지식 페이지 전수다. 직접 source가 없고 단순히 React·Spring·상품 같은 단어만 등장하는 타 과목 페이지는 이번 직접 범위에서 제외했다. 직접 범위는 56개이며 query는 0개다.

- summary: 19개
- concept: 20개
- entity: 9개
- comparison: 8개
- query: 0개

## 기존 summary 대응 및 분류 초안

19개 summary는 모두 50~56줄의 1차 요약으로, 수백 줄짜리 날짜 MD의 실제 교시 흐름·대표 코드 단위·입력→처리→결과·다음 날 연결을 충분히 복원하지 못한다. 따라서 전면 재작성 초안으로 분류한다.

| wiki 페이지 | raw·수업일 | 대표 artifact | 분류 | 주요 누락 | 직접 수업 / 후속 확장 경계 |
|---|---|---|---|---|---|
| `summaries/2026-03-30-fullstack-environment-setup` | R01, 03-30 | Vite·MySQL·Fruit·Spring 설정 | 전면 재작성 | 설치 나열보다 실제 생성·실행·DB 연결 순서와 설정 역할 부족 | UI&UX 이후 풀스택 시작 / Linux·AWS 배포는 후속 |
| `summaries/2026-03-31-spring-boot-controller-html` | R02, 03-31 | FruitHtmlController·template·REST JSON·Router | 전면 재작성 | MVC HTML과 REST JSON 전환, FruitList/One 연결 과정 부족 | 직접 Controller/React 입문 / 보안·도메인은 후속 |
| `summaries/2026-04-01-react-router-spring-boot` | R03, 04-01 | MenuItems·Fruit type·axios·CORS | 전면 재작성 | Router→axios→CORS→응답 렌더링과 props/model 혼동 부족 | 직접 Fruit 연동 / Member·JWT는 후속 |
| `summaries/2026-04-02-react-bootstrap-homepage` | R04, 04-02 | HomePage Carousel·Member JPA·Security | 전면 재작성 | 오전 React와 오후 Member/JPA/Security 전환이 제목·본문에서 축약됨 | HomePage와 Member 시작 직접 / 로그인 완성은 후속 |
| `summaries/2026-04-03-spring-member-seed-react-comments` | R05, 04-03 | SignupPage·BindingResult·계층 구현 | 전면 재작성 | 단순 JSX 주석보다 회원가입 요청·검증·저장·응답 흐름이 핵심인데 누락 | 회원가입 직접 / JWT 로그인은 후속 |
| `summaries/2026-04-06-login-jwt-session-cookie` | R06, 04-06 | axiosInstance·LoginPage·JwtTokenProvider | 전면 재작성 | 이론→React 저장→Spring 토큰 생성 연결과 보안 경계 부족 | 수업 JWT 로그인 직접 / Passwordless는 후속 과목 |
| `summaries/2026-04-07-member-api-string-token` | R07, 04-07 | Bearer 파싱·JWT Filter·SecurityContext | 전면 재작성 | Filter chain과 인증 객체 설정, CORS/SecurityConfig 역할 분리 부족 | JWT 필터 직접 / 운영 secret 관리는 후속 |
| `summaries/2026-04-08-product-domain-oci` | R08, 04-08 | Category/Product·GenerateData·목록 API | 전면 재작성 | OCI보다 상품 도메인·seed·테스트→목록 연결이 핵심인데 축약 | 상품 시작 직접 / Oracle Cloud 운영은 범위 밖 |
| `summaries/2026-04-09-product-delete-routing-jsx-table` | R09, 04-09 | 삭제 API·버블링 방지·ProductInsertForm | 전면 재작성 | 삭제→목록 갱신과 등록 폼 전환의 기능 흐름 부족 | Product CRUD 직접 / 일반 HTML table은 UI&UX 선행 |
| `summaries/2026-04-10-react-event-spread-product-form` | R10, 04-10 | event·spread·등록/수정 state | 전면 재작성 | 이벤트→state merge→request body와 등록/수정 공통점·차이 부족 | React 상품 폼 직접 / 전역 상태관리는 후속 범위 밖 |
| `summaries/2026-04-13-product-detail-useeffect-service` | R11, 04-13 | GET/PUT·useEffect·Cart 관계 시작 | 전면 재작성 | 상품 수정·상세 완료 뒤 장바구니 관계로 넘어가는 하루 전환 누락 | Product 마무리와 Cart 시작 직접 |
| `summaries/2026-04-14-cart-service` | R12, 04-14 | CartService·CartItemDto·CartList | 전면 재작성 | add/list 두 use case의 DTO 변환과 인증 사용자 기준 부족 | 장바구니 조회 직접 / 주문은 후속 |
| `summaries/2026-04-15-cart-list-selection-typescript` | R13, 04-15 | 전체/개별 선택·props·수량·삭제 | 전면 재작성 | 선택 상태와 서버 수량/삭제 요청의 양방향 연결 부족 | Cart UI/API 직접 |
| `summaries/2026-04-16-cart-quantity-stock` | R14, 04-16 | 재고 검증·Order Entity/DTO/cascade | 전면 재작성 | 제목이 주문 도메인 시작을 충분히 드러내지 않고 snapshot/cascade 경계 부족 | Cart 보정과 Order 시작 직접 |
| `summaries/2026-04-17-cart-total-array-some` | R15, 04-17 | `some`·총액·주문 함수·OrderList | 전면 재작성 | 장바구니 선택→주문 생성→주문 목록 조회 전환 부족 | Cart→Order 직접 |
| `summaries/2026-04-20-order-list-scenario` | R16, 04-20 | 주문 상태·완료/취소·재고 복원·대표 상품 | 전면 재작성 | 관리자/사용자 시나리오, 상태 전이, 재고 복원과 홈 대표 상품 전환 부족 | Order 마무리와 검색 전단계 직접 |
| `summaries/2026-04-21-product-pagination-search-react` | R17, 04-21 | Paging·FieldSearch·SearchDto·Specification | 전면 재작성 | React parameter→DTO→Specification의 절반 흐름과 CSR/SSR 경계 부족 | 검색 frontend+backend 시작 직접 |
| `summaries/2026-04-22-product-repository-pageable-search` | R18, 04-22 | Repository·Pageable·다중 조건 테스트 | 전면 재작성 | 조건 조립→DB 테스트 시나리오와 null/type 비교 혼동 부족 | 검색 완성 직접 / Linux 시작은 다음 과목 |
| `summaries/2026-04-03-frontend-backend-subject-review` | R01~R19 | 전체 쇼핑몰 기능 흐름 | 전면 재작성 | 18개 날짜 전체 source 선언, 기능별 대표 artifact, 직접 구현/교안/후속 배포 경계 부족 | 4과목 전체 직접 / Linux·AWS·CI/CD·Passwordless 후속 |

## 기존 concept 대응 및 분류 초안

| wiki 페이지 | 주 raw·수업일 | 대표 artifact | 분류 | 주요 누락·판정 | 직접 수업 / 후속 확장 경계 |
|---|---|---|---|---|---|
| `concepts/axios-interceptor-error-handling` | R06, R10, R19 | axiosInstance·로그인/폼 오류 | 전면 재작성 | 재검증 메모 중심이며 interceptor·401·BindingResult 오류의 실제 경로가 얕음 | JWT/폼 오류 직접 / 공통 운영 정책은 후속 |
| `concepts/database-normalization-functional-dependency` | R01, R14 | MySQL 설계·주문 관계 | 유지 | Oracle 단계에서 이미 원리·오해를 고도화함; 4과목은 적용 사례만 경계 확인 | Oracle 직접 학습 / 4과목 JPA 적용 |
| `concepts/dto-entity-service-controller` | R02, R12, R18, P08, I04 | CartItemDto·Entity·계층 | 부분 보강 | 날짜별 역할 변화와 실제 변환 지점 추가 필요 | 4과목 직접 |
| `concepts/frontend-backend-architecture` | R01~R03, P01, P08, I05 | Controller→Service→Repository→DB | 전면 재작성 | 일반 구조와 실제 Fruit/Member/Product 요청 흐름을 더 명확히 분리해야 함 | 4과목 직접 / 배포 topology는 후속 |
| `concepts/fullstack-project-flow` | R19 | 전체 기능 요청 왕복 | 통합 후보 | architecture 페이지와 중복이 크고 재검증 메모가 실제 provenance를 대신함 | 기능 오케스트레이션 역할이 독립적인지 실행 시 결정 |
| `concepts/jpa-relationship-mapping` | R11, R12, R14, R19, I01~I04 | CartProduct·OrderProduct 관계 | 전면 재작성 | owning side, FK, join entity, cascade/snapshot 경계와 그림 provenance 부족 | JPA 직접 / DB ON DELETE와 구분 |
| `concepts/jwt-session-cookie-auth` | R06, R07, P03, P04, P08 | token 발급·저장·filter | 부분 보강 | 브라우저 저장→Bearer→Filter→SecurityContext 전체 왕복 보강 필요 | JWT 직접 / Passwordless 후속 |
| `concepts/oracle-sequence` | R01 | Oracle→MySQL 전환 언급 | 유지 | Oracle 단계에서 고도화 완료; 4과목 출처는 DB 전환 경계만 보존 | Oracle 직접 / MySQL auto increment·JPA는 후속 적용 |
| `concepts/order-flow` | R14~R16 | Order/OrderProduct·상태·재고 | 전면 재작성 | 주문 snapshot, 상태 전이, 취소 재고 복원, 사용자/관리자 흐름 부족 | 4과목 직접 |
| `concepts/pagination-search` | R17, R18, P10 | React paging→Specification/Pageable | 통합 후보 | specification/pageable·spring-product-search와 중복 역할 재설계 필요 | frontend/backend 통합 허브 여부 결정 |
| `concepts/product-domain-flow` | R08~R11, R17, R18 | Product CRUD·검색 | 전면 재작성 | seed→CRUD→상세→대표 상품→검색의 날짜 흐름과 실제 code provenance 부족 | 4과목 직접 |
| `concepts/react-form-state-event` | R05, R10, P07 | Signup/Product form event+spread | 부분 보강 | 회원가입과 상품 폼의 공통/차이, request body·오류 표시 연결 필요 | React 직접 |
| `concepts/react-typescript-basics` | R03, R10, R13, R17, P07, I03 | type·props/state·Router | 부분 보강 | 수업 날짜별 학습 이력과 JSX/className·generic·CSR 경계 보강 | React/TS 직접 |
| `concepts/react-useeffect-data-fetching` | R11, R17, P07 | 상세 조회·목록 재조회 | 부분 보강 | dependency와 사용자 action 호출의 차이, stale/반복 요청 혼동 보강 | React 직접 |
| `concepts/shopping-cart-flow` | R11~R15, I01~I04 | Cart/CartProduct·선택·수량·재고 | 전면 재작성 | 관계→추가→목록 DTO→선택→수량/삭제→주문 연결을 복원해야 함 | 4과목 직접 |
| `concepts/spring-boot-rest-api` | R02, R07, R18, P03, P08 | JSON·Controller·ResponseEntity | 부분 보강 | HTML controller와 REST controller 전환, HTTP method/status·검증 경계 추가 | 4과목 직접 |
| `concepts/spring-data-jpa-repository` | R18 | ProductRepository | 부분 보강 | 04-03 Member, 04-08 Product, 04-16 Order, 04-22 search의 누적 이력 부족 | 4과목 직접 |
| `concepts/spring-data-jpa-specification-pageable` | R18, P08, P10 | 동적 조건·PageRequest | 부분 보강 | R17 frontend parameter와 R18 DB 테스트까지 연결 필요 | 4과목 직접 |
| `concepts/spring-product-search-flow` | R18 | Repository→Service→Controller·SQL 테스트 | 부분 보강 | 내용은 가장 구체적이나 모든 fence의 R18 연속 원문 여부와 실제 변수명 재검증 필요 | 4과목 직접 |
| `concepts/spring-security-jwt-filter` | R07, P04, P08 | JwtAuthenticationFilter·SecurityContext | 전면 재작성 | 재검증 메모 대신 filter chain, 실패/통과, 사용자 조회, 인증 저장의 실제 순서 필요 | 4과목 직접 / 운영 보안은 후속 |

## 기존 entity 대응 및 분류 초안

| wiki 페이지 | 주 raw·수업일 | 대표 artifact | 분류 | 주요 누락·판정 | 직접 수업 / 후속 확장 경계 |
|---|---|---|---|---|---|
| `entities/intellij-idea` | P02 및 R01~R18의 Spring 작업 | Spring Boot IDE | 유지 | Java 단계 고도화 결과 유지; 4과목 학습 이력 source 보완 여부만 확인 | Java 첫 등장 / Spring 후속 활용 |
| `entities/jwt` | R06, R07, P04 | JwtTokenProvider·Filter | 부분 보강 | 04-06 발급과 04-07 검증 이력, 구조/서명/Claims 경계 보강 | 4과목 직접 / Passwordless와 별개 |
| `entities/mysql` | R01~R18 다수, P05 | Workbench·JPA·도메인 테스트 | 부분 보강 | 설치→Member/Product/Cart/Order/Search의 날짜 이력을 실제 기능으로 정리 | 4과목 직접 / Oracle과 다른 runtime |
| `entities/node-js` | R01 중심, P06 | Vite/React 개발 서버 | 전면 재작성 | 실제 핵심 등장은 환경 구성인데 여러 날짜 source가 과도하며 Node와 React 역할 경계가 얕음 | 개발 도구 직접 / 백엔드 runtime으로 가르친 근거 없음 |
| `entities/oracle-database` | R01의 DB 전환 경계 | Oracle→MySQL 비교 언급 | 유지 | Oracle 단계 고도화 완료; 4과목 source는 MySQL 전환 경계만 유지 | Oracle 직접 / 4과목 runtime은 MySQL |
| `entities/react` | R03~R18, P07 | Router·state·Hook·도메인 화면 | 전면 재작성 | 4개 source와 재검증 메모만으로 4월 전체 학습 이력을 대표하지 못함 | 4과목 직접 |
| `entities/spring-boot` | R01~R18, P08 | API·JPA·Security·업무 계층 | 전면 재작성 | 실제 날짜별 역할이 다섯 source에 축약되고 재검증 메모가 이력을 대신함 | 4과목 직접 / Linux·AWS 배포 후속 |
| `entities/typescript` | R03, R13, R18, P07 | interface·props·검색 타입 | 전면 재작성 | 상품·Cart·SearchCondition 타입 학습 이력과 runtime/type-only 경계 부족 | 4과목 직접 |
| `entities/visual-studio-code` | R01~R18 다수, P09 | React/TS 편집 환경 | 부분 보강 | 설치·단축키보다 실제 React 프로젝트 역할 중심으로 source를 정리할 필요 | 4과목 직접 / 일반 편집기 정의는 보조 |

## 기존 comparison·query 대응 및 분류 초안

| wiki 페이지 | 주 raw·수업일 | 대표 artifact | 분류 | 주요 누락·판정 | 직접 수업 / 후속 확장 경계 |
|---|---|---|---|---|---|
| `comparisons/authentication-vs-authorization` | R06, 후속 Passwordless | 로그인·권한 | 부분 보강 | 4과목은 인증 구현 중심이고 인가 사례는 제한적이라는 근거 경계 필요 | 인증 직접 / 인가·Passwordless 후속 |
| `comparisons/controller-service-repository` | R12, R18 | Cart와 Search 계층 | 부분 보강 | 내용은 구체적이나 축약·합성 fence를 배제하고 Product/Cart 실제 원문으로 교체·검증 필요 | 4과목 직접 |
| `comparisons/entity-vs-dto` | R06, R12, R18 | LoginDto·CartItemDto·Entity | 부분 보강 | Entity 응답 위험, DTO 변환 지점, Order snapshot 사례 보강 필요 | 4과목 직접 |
| `comparisons/jpql-vs-sql` | R01, R16, R18, Oracle R03 | Order JPQL·MySQL 테스트 SQL | 유지 | Oracle 단계에서 직접 SQL/후속 JPA 경계를 고도화함 | Oracle 직접 / 4과목 JPQL 적용 |
| `comparisons/mpa-vs-spa` | R06, P04 | Session/JWT 구조 | 부분 보강 | 렌더링 방식과 인증 저장 방식을 같은 것으로 보는 오해 방지 필요 | 4과목 이론 직접 |
| `comparisons/props-vs-state` | R10, R13, P07 | Product form·Cart selection | 부분 보강 | 부모 전달/로컬 변경의 실제 두 상황과 callback 관계 보강 | 4과목 직접 |
| `comparisons/react-router-vs-spring-api-url` | R03, R12, R17, P01, I03 | screen path vs API URL | 부분 보강 | Fruit·Cart·Paging의 실제 URL 쌍과 CORS 관계 보강 | 4과목 직접 |
| `comparisons/session-vs-cookie-vs-jwt` | R06, R07, P03, P04 | 상태 저장·전달·검증 | 부분 보강 | cookie는 저장/전달 수단이고 session/JWT는 인증 상태 설계라는 층위 보강 | 4과목 직접 / Passwordless 별도 |

- 기존 query: 0개
- 실제 사용자 질문 기록을 별도로 검토하기 전에는 query를 임의 생성하지 않는다.

## 신규 필요 후보 초안

신규 페이지는 아직 만들지 않았다. 다음 실행 세션에서 기존 페이지가 수용하지 못하는 독립 학습축인지 재검증한다.

| 후보 | 권장 type | 주 raw | 신규 필요 판단 | 흡수 가능성 |
|---|---|---|---|---|
| HTTP 요청·JSON·CORS 전체 흐름 | concept | R02~R05, P03 | Fruit→Member 전환에서 반복되고 frontend/backend 경계의 핵심 | `spring-boot-rest-api`와 `frontend-backend-architecture` 보강으로 흡수 가능 |
| Spring Validation과 BindingResult 오류 응답 | concept | R04, R05, R10, P08 | 회원가입·상품 폼의 검증이 반복되며 Axios 오류 처리와 연결 | `axios-interceptor-error-handling` 또는 DTO 계층 페이지에 흡수 가능 |
| CartProduct vs OrderProduct | comparison | R11~R16, I01~I04 | 현재 장바구니 관계와 주문 snapshot의 생명주기 차이가 반복 혼동 축 | cart/order concept 양쪽 보강으로 흡수 가능 |
| JPA cascade vs DB ON DELETE | comparison | R14, Oracle raw, P08 | 영속성 전이와 DB FK 삭제 규칙을 같은 것으로 오해하기 쉬움 | `jpa-relationship-mapping`과 `on-delete-set-null-vs-cascade` 연결로 흡수 가능 |

현재 신규 필요 후보 수는 4개이며, 최종 신규 생성 수는 0~4개다. 신규 생성 여부는 해당 유형 실행 세션에서 중복·직접 근거·탐색 역할을 다시 확인한 뒤 결정한다.

## 분류 수치

### 기존 페이지 56개

- 유지: 5개
- 부분 보강: 19개
- 전면 재작성: 30개
- 통합 후보: 2개
- 근거 부족: 0개
- 미분류: 0개

### 신규 후보

- 신규 필요 후보: 4개
- query 후보: 0개

## 실행 세션 분할

과목 완료까지 총 16개 세션으로 계획한다. 현재 세션이 세션 1이며, 세션 2~15는 지식 페이지 실행 묶음, 세션 16은 전체 대응·provenance·구조 고정점 검증이다. 각 세션은 지정한 페이지와 주 raw만 처리하고 다음 묶음을 자동 실행하지 않는다.

| 세션 | 구간·유형 | 대상 페이지 | 주 raw |
|---:|---|---|---|
| 1 | 재고·대응·분류·분할 | 이 meta 계획만 작성 | R01~R19, P01~P10, I01~I05 |
| 2 | Summary 전반부 A | `summaries/2026-03-30-fullstack-environment-setup`, `summaries/2026-03-31-spring-boot-controller-html`, `summaries/2026-04-01-react-router-spring-boot`, `summaries/2026-04-02-react-bootstrap-homepage` | R01~R04, P01~P09, I03·I05 |
| 3 | Summary 전반부 B | `summaries/2026-04-03-spring-member-seed-react-comments`, `summaries/2026-04-06-login-jwt-session-cookie`, `summaries/2026-04-07-member-api-string-token`, `summaries/2026-04-08-product-domain-oci` | R05~R08, P03·P04·P07·P08 |
| 4 | Summary 중반부 | `summaries/2026-04-09-product-delete-routing-jsx-table`, `summaries/2026-04-10-react-event-spread-product-form`, `summaries/2026-04-13-product-detail-useeffect-service`, `summaries/2026-04-14-cart-service` | R09~R12, P07·P08, I01~I04 |
| 5 | Summary 후반부 A | `summaries/2026-04-15-cart-list-selection-typescript`, `summaries/2026-04-16-cart-quantity-stock`, `summaries/2026-04-17-cart-total-array-some`, `summaries/2026-04-20-order-list-scenario` | R13~R16, P03·P08, I01~I04 |
| 6 | Summary 후반부 B·허브 | `summaries/2026-04-21-product-pagination-search-react`, `summaries/2026-04-22-product-repository-pageable-search`, `summaries/2026-04-03-frontend-backend-subject-review` | R17~R19, P03·P08·P10, I01~I05 |
| 7 | Concept Frontend/React/TypeScript A | `frontend-backend-architecture`, `fullstack-project-flow`, `react-typescript-basics`, `react-form-state-event`, `react-useeffect-data-fetching` | R01~R05, R10~R13, R17, R19, P01·P07, I03·I05 |
| 8 | Concept Frontend/React/TypeScript B | `axios-interceptor-error-handling`, `product-domain-flow`, `shopping-cart-flow`, `order-flow`, `pagination-search`; HTTP/CORS·Validation 신규 후보 흡수 판단 | R06~R18·R19, P03·P07·P08·P10, I01~I04 |
| 9 | Concept Backend/Spring/인증 A | `spring-boot-rest-api`, `dto-entity-service-controller`, `jwt-session-cookie-auth`, `spring-security-jwt-filter`, `spring-data-jpa-repository` | R02~R08, R12, R18, P03·P04·P08 |
| 10 | Concept Backend/Spring/데이터 B | `jpa-relationship-mapping`; 세션 8에서 완료한 Product·Cart·Order·Paging concept는 재처리하지 않음 | R11·R12·R14·R19, P08, I01~I04 |
| 11 | Concept Backend/Spring/데이터 C | `spring-data-jpa-specification-pageable`, `spring-product-search-flow`, `database-normalization-functional-dependency`, `oracle-sequence` | R01, R14, R17, R18, P08·P10; Oracle 선행 페이지 경계 |
| 12 | Entity A | `spring-boot`, `react`, `typescript`, `jwt`, `mysql` | R01~R18, P04·P05·P07·P08 |
| 13 | Entity B | `node-js`, `visual-studio-code`, `intellij-idea`, `oracle-database` | R01~R05 중심, P02·P06·P09; Java·Oracle 선행 경계 |
| 14 | Comparison A | `controller-service-repository`, `entity-vs-dto`, `props-vs-state`, `react-router-vs-spring-api-url`, `mpa-vs-spa`, `session-vs-cookie-vs-jwt` | R03, R06, R07, R10, R12~R18, P01·P03·P04·P07·P08, I03 |
| 15 | Comparison/Query B | `authentication-vs-authorization`, `passwordless-vs-password-login`, `why-shopping-cart-order-flow-is-complex`, `jwt-role-ui-vs-server-authorization` | R06·R07·R12~R16, P04, I01·I02·I04; Passwordless·중간 프로젝트 경계 |
| 16 | 과목 전체 고정점 | 최종 생성·수정된 FrontEnd_BackEnd 지식 페이지, index, log, 상위 계획 완료 기록 | R01~R19, P01~P10, I01~I05 전수 |

## 실행 세션 공통 완료 게이트

- 지정한 대상 페이지 수와 분류 결과가 일치하고 미분류가 없어야 한다.
- summary는 실제 교시 흐름, 대표 artifact, 입력→처리→결과, 이전·다음 날짜 연결을 갖춰야 한다.
- concept/entity/comparison은 실제 수업 날짜·코드·도식과 직접 수업/후속 확장 경계를 갖춰야 한다.
- 새 code fence는 원본에 이미 있는 연속 코드가 필요한 경우에만 다음 실행 세션에서 작성하며, 합성 예제를 수업 코드로 만들지 않는다.
- 모든 fence는 해당 페이지가 선언한 텍스트 source의 공백 정규화 연속 부분문자열로 검증한다. PDF/PNG 근거는 별도 수동 예외로 기록한다.
- 기록한 raw 경로는 모두 실제로 존재해야 한다.
- 새 지식 페이지를 만들면 index 등록, Total pages 재계산, log 기록을 같은 세션에서 처리한다.
- `raw/KoreaICT/4. FrontEnd_BackEnd` scoped status/diff를 시작·종료 시 확인하고 Agent 도구로 수정하지 않는다.
- 각 세션의 scoped tracked/untracked diff와 `git diff --check`를 확인한다.
- 세션 16 전에는 단계 4 완료 행을 상위 계획에 쓰지 않고 단계 5 Linux도 시작하지 않는다.

## 실행 기록

### 세션 2 — Summary 전반부 A

- 처리일: 2026-07-15
- 처리 대상: `2026-03-30-fullstack-environment-setup`, `2026-03-31-spring-boot-controller-html`, `2026-04-01-react-router-spring-boot`, `2026-04-02-react-bootstrap-homepage` 4개
- raw 대응: R01~R04를 4/4로 읽고 각 날짜의 전체 교시 순서를 우선 근거로 삼았다.
- 보조자료 확인: I03에서 Router가 관객을 알맞은 상영관으로 안내하는 비유를, I05에서 template↔Controller↔Service↔Repository와 JPA Repository↔DB 흐름을 확인했다. P01~P09는 날짜 MD에 필요한 설명과 artifact가 충분히 전사되어 있어 별도 주장·fence source로 추가하지 않았다.
- 실제 처리: 4개 모두 50줄 1차 요약에서 전면 재작성했다. 03-30은 환경→Spring/MySQL→Vite/React→Fruit, 03-31은 HTML/Model/Thymeleaf→REST/JSON→React Router, 04-01은 type→axios/state/effect→CORS/WebConfig→렌더링, 04-02는 HomePage→Member JPA/Validation→Security→Repository/DI 흐름을 복원했다.
- 내용 게이트: 각 summary에 날짜, 이전·다음 날짜 링크, 대표 artifact, 입력→처리→결과 표, 실제 혼동 원인, 직접 수업과 후속 Member/JWT/Product/Linux/AWS 경계를 포함했다.
- provenance: 새 code fence를 만들지 않아 검증 대상 fence는 0개다. 원본 코드의 식별자·동작·실행 결과는 R01~R04에 실제 등장한 범위만 서술했다.
- 구조 검증: summary 4개와 raw 4개가 4/4 대응했고 frontmatter·source 실경로·허용 태그·위키링크·index 설명·placeholder 검사 오류는 0건이다. code fence는 0개라 원문 대조 대상도 0개이며, scoped tracked/untracked whitespace 검사와 `git diff --check`를 통과했다. FrontEnd_BackEnd raw scoped status는 항목 0건, diff exit 0이다.
- 과목 상태: 미완료. 세션 2 완료 뒤 세션 3을 자동 실행하지 않았고, 단계 4 완료 행을 상위 계획에 기록하지 않았으며 단계 5 Linux도 시작하지 않았다.

### 세션 3 — Summary 전반부 B

- 처리일: 2026-07-15
- 처리 대상: `2026-04-03-spring-member-seed-react-comments`, `2026-04-06-login-jwt-session-cookie`, `2026-04-07-member-api-string-token`, `2026-04-08-product-domain-oci` 4개
- raw 대응: R05~R08을 4/4로 읽고 각 날짜의 1~8교시 순서를 최우선 근거로 삼았다.
- 보조자료 판단: R05~R08에 P03·P04·P07·P08의 필요한 개념·페이지 인용과 실습 코드가 이미 전사되어 있어, PDF에서만 가져오는 별도 주장이나 code fence는 추가하지 않았다.
- 실제 처리: 4개 모두 50줄 1차 요약에서 전면 재작성했다. 04-03은 Member seed→SignupPage event/오류 표시→Repository/Service/Controller→Validation·중복 확인·저장·응답, 04-06은 Cookie/Session/JWT·MPA/SPA→axiosInstance/User/LoginPage→LoginDto/JwtTokenProvider, 04-07은 String/Bearer→JwtAuthenticationFilter/SecurityContext와 MemberDetailsService 사용자 조회 경로→CORS/SecurityConfig→Controller login·테스트·logout, 04-08은 Category/Product→File/Random 보충→GenerateData/단위 테스트 seed→Repository/Service/Controller 목록→React Product/ProductList 순서를 복원했다.
- 핵심 경계: 04-07에서 JWT filter가 Repository를 직접 조회하는 것처럼 합치지 않고, login 시 `MemberDetailsService` 사용자 조회와 후속 요청의 token→SecurityContext 경로를 분리했다. 04-08은 OCI를 raw의 한 줄 소개·가입 자료 안내까지만 보존하고 실제 Product 기능을 중심으로 정리했다.
- 내용 게이트: 각 summary에 날짜, 이전·다음 날짜 링크, 전체 교시 흐름, 대표 artifact, 입력→처리→결과, 실제 혼동 원인과 직접 수업/후속 Product·Cart·Order·Linux·AWS·CI/CD·Passwordless 경계를 포함했다.
- provenance: code fence는 0개, 선언한 텍스트 raw 원문 검증 0개, PDF/PNG 수동 예외 0개다. 원본에 없는 클래스·메서드·출력·상태 코드·사용자 질문과 여러 원본 조각을 합친 코드를 만들지 않았다.
- 구조 검증: summary 4개와 raw 4개가 4/4 대응했고 frontmatter·source 실경로·허용 태그·위키링크·index 설명·placeholder·scoped diff와 `git diff --check`를 확인했다. FrontEnd_BackEnd raw scoped status/diff도 다시 확인했다.
- 과목 상태: 미완료. 세션 3 완료 뒤 세션 4를 자동 실행하지 않았고, 단계 4 완료 행을 상위 계획에 기록하지 않았으며 단계 5 Linux도 시작하지 않았다.

### 세션 4 — Summary 중반부

- 처리일: 2026-07-16
- 처리 대상: `2026-04-09-product-delete-routing-jsx-table`, `2026-04-10-react-event-spread-product-form`, `2026-04-13-product-detail-useeffect-service`, `2026-04-14-cart-service` 4개
- raw 대응: R09~R12를 4/4로 읽고 각 날짜의 1~8교시 흐름을 최우선 근거로 삼았다.
- 보조자료 확인: I03은 Router가 선택한 화면으로 안내하는 비유만 04-09에 사용했다. I01·I02·I04는 Member–Cart 1:1, Cart–CartProduct 1:N, CartProduct–Product N:1과 품목별 quantity 구조만 04-13·04-14에 보조했다. P07·P08의 event·spread·useEffect·연관관계 내용은 날짜 MD에 필요한 페이지 인용과 코드가 전사되어 있어 PDF-only 주장이나 fence source를 추가하지 않았다.
- 실제 처리: 4개 모두 50줄 1차 요약에서 전면 재작성했다. 04-09는 관리자 삭제 클릭→버블링 방지→Service의 이미지/DB 처리→Controller 응답→목록 state 갱신→등록 route/form 시작, 04-10은 event target→spread state 갱신→FileReader→POST body→Spring 이미지 저장·Validation 오류→수정 form 시작, 04-13은 수정 GET/PUT→상세 GET/useEffect→Cart/CartProduct 관계→상세 화면 장바구니 요청 준비, 04-14는 인증 email→Cart 조회/생성→동일 품목 수량 누적/신규 저장→CartItemDto 목록→React CartList 표시 순서를 복원했다.
- 핵심 경계: 04-09의 일반 table/JSX 보충과 실제 Product 기능, 04-10의 등록/수정 공통 form과 id·기존 조회·요청 목적 차이, 04-13의 Product 마무리와 Cart 시작, 04-14의 입력 `CartProductDto`와 출력 `CartItemDto`를 분리했다. Cart 선택·수량 변경·삭제, Order, 검색/페이징, Linux·AWS·CI/CD·Passwordless는 후속 범위로 명시했다.
- 내용 게이트: 각 summary에 날짜, 이전·다음 날짜 링크, 전체 교시 흐름, 대표 artifact, 입력→처리→결과, 실제 혼동 원인, 직접 수업/후속 확장 경계를 포함했다.
- provenance: code fence는 0개, 선언한 텍스트 raw 원문 검증 0개, 수동 fence 예외 0개다. 이미지는 표시된 관계·quantity·Router 비유만 서술 근거로 사용했으며 원본에 없는 코드·클래스·메서드·출력·상태 코드·사용자 질문을 만들지 않았다.
- 구조 검증: summary 4개와 raw 4개가 4/4 대응했고 frontmatter 필수 키·source 실경로·허용 태그·위키링크·index 설명·placeholder·필수 섹션과 scoped diff를 확인했다. 대상 4개는 각각 0 fence이며 `git diff --check`를 통과했고, FrontEnd_BackEnd raw scoped status는 항목 0건·diff exit 0이다.
- 과목 상태: 미완료. 세션 4 완료 뒤 세션 5를 자동 실행하지 않았고, 단계 4 완료 행을 상위 계획에 기록하지 않았으며 단계 5 Linux도 시작하지 않았다.

### 세션 5 — Summary 후반부 A

- 처리일: 2026-07-16
- 처리 대상: `2026-04-15-cart-list-selection-typescript`, `2026-04-16-cart-quantity-stock`, `2026-04-17-cart-total-array-some`, `2026-04-20-order-list-scenario` 4개
- raw 대응: R13~R16을 4/4로 읽고 각 날짜의 1~8교시 순서와 기능이 실제 연결된 시점을 최우선 근거로 삼았다.
- 보조자료 판단: R13~R16에 P03의 parameter·REST mapping, P08의 cascade·JPA·Repository, I01~I04가 보조하는 Cart/Product 관계의 필요한 내용이 충분히 전사되어 있었다. PDF/이미지에서만 가져오는 별도 주장·code fence가 필요하지 않아 해당 artifact를 새 source로 추가하지 않았다.
- 실제 처리: 4개 모두 50줄 1차 요약에서 전면 재작성했다. 04-15는 user props·구조 분해→전체/개별 선택·합계→수량 input/PATCH·재고 검증 중간 보정→삭제 백엔드 기반, 04-16은 CartProduct 연결 Product를 이용한 수량 보정·React 삭제→OrderStatus/cascade→Order/OrderProduct·요청 DTO→선택 Cart 품목 POST→회원·상품·재고 검증·OrderProduct 구성·재고 차감·Cart 삭제·Order 저장, 04-17은 stock DTO/type→`some`·오류 Alert→상품 상세 즉시 주문→OrderDetailDto·역할별 PENDING 조회→OrderList 초기 화면, 04-20은 주문 카드·역할별 버튼→완료 PUT→취소 DELETE·재고 복원→Home 대표 상품→Paging 타입/컴포넌트 순서를 복원했다.
- 핵심 경계: 04-15에서 checkbox·수량·삭제·주문 control의 표시와 실제 handler/API 연결 단계를 구분했다. 04-16의 Cart 삭제와 주문 저장은 같은 날 직접 구현됐음을, 04-17의 일반 `some` 설명과 Cart quantity 0 검사를 분리했다. 04-20은 Order Entity·생성 DTO/API가 아니라 전날까지 만든 목록의 렌더링·완료·취소를 다룬 날이며, 후반 대표 상품·페이징을 Order 처리와 합치지 않았다.
- 내용 게이트: 각 summary에 날짜, 이전·다음 날짜 링크, 전체 교시 흐름, 대표 artifact, 입력→처리→결과, 실제 혼동 원인, 직접 수업/후속 검색·페이징·Linux·AWS·CI/CD·Passwordless 경계를 포함했다.
- provenance: code fence는 전체 0개, 선언한 텍스트 raw 원문 검증 0개, 수동 fence 예외 0개다. 원본에 없는 코드·클래스·메서드·출력·상태 코드·사용자 질문을 만들지 않았고 서로 다른 원본 조각을 수업 코드로 합성하지 않았다.
- 구조 검증: summary 4개와 raw 4개가 4/4 대응했고 frontmatter 필수 키·source 실경로·허용 태그·위키링크·index 설명·placeholder·필수 섹션과 scoped diff를 확인했다. 대상 4개는 각각 0 fence이며 `git diff --check`를 통과했고, FrontEnd_BackEnd raw scoped status는 항목 0건·diff exit 0이다.
- 과목 상태: 미완료. 세션 5 완료 뒤 세션 6을 자동 실행하지 않았고, 단계 4 완료 행을 상위 계획에 기록하지 않았으며 단계 5 Linux도 시작하지 않았다.

### 세션 6 — Summary 후반부 B·허브

- 처리일: 2026-07-16
- 처리 대상: `2026-04-21-product-pagination-search-react`, `2026-04-22-product-repository-pageable-search`, `2026-04-03-frontend-backend-subject-review` 3개
- raw 대응: R17·R18·R19를 3/3으로 읽었다. 날짜별 고도화 Summary 18개도 직접 대조해 허브의 R01~R18 날짜 귀속을 바로잡았다. R19는 제목 표기와 달리 04-15 Cart 삭제까지 기록되고 04-16~04-22 Order·대표 상품·검색은 포함하지 않는다는 실제 끝 경계를 확인했다.
- 보조자료 판단: P03·P08·P10과 I01~I05에서 필요한 용어·계층·관계는 날짜 MD·R19와 이미 고도화된 날짜 Summary에 충분히 전사되어 있었다. PDF/이미지 전용 주장이나 source를 추가하지 않았다.
- 실제 처리: 04-21은 전날 Paging UI 준비→React page parameter·Spring Page 응답→단순 Pageable Service/Controller→MySQL page 확인→SearchCondition/FieldSearch→검색 request parameter→SearchDto→CSR/SSR 보충→LIKE/ProductSpecification 시작 순서로 전면 재작성했다. 04-22는 ProductRepository→Java String 비교 보충→Service Specification 조립·sort/PageRequest→Controller parameter/SearchDto/Page 응답→검색용 날짜 데이터→기간·카테고리·다중 조건 MySQL 시나리오 순서로 전면 재작성했다.
- 허브 처리: 환경→Fruit→Member/회원가입→JWT→Product CRUD→Cart→Order→대표 상품→페이징/검색의 18일 흐름을 날짜 Summary 링크, 기능별 대표 artifact, 입력→처리→결과 왕복과 반복 혼동 기준으로 재구성했다. R19 직접 범위, 교안 보충, Linux·AWS·CI/CD·Passwordless·중간 프로젝트 확장을 분리했다.
- 핵심 경계: 04-20의 Paging control 준비, 04-21의 page 왕복과 검색 UI/request·DTO/개별 Specification 준비, 04-22의 Controller→Service→Repository 검색 완성을 구분했다. UI control 존재와 실제 request/response 연결, Querydsl 용어 언급과 실제 Specification 구현도 분리했다.
- provenance: 대상 Summary code fence는 전체 0개, 선언 텍스트 raw 원문 검증 0개, 수동 fence 예외 0개다. 원본에 없는 코드·클래스·메서드·출력·상태 코드·사용자 질문이나 합성 코드를 만들지 않았다.
- 구조 검증: 대상 Summary 3개와 주 raw 3개를 3/3 대응했다. frontmatter 필수 키·source 실경로·허용 태그·위키링크·index 설명·placeholder·필수 내용 구조, scoped diff와 `git diff --check`, FrontEnd_BackEnd raw scoped status/diff를 기록 파일 수정 후 다시 검사했다.
- 과목 상태: 미완료. 세션 6 완료 뒤 세션 7을 자동 실행하지 않았고, 단계 4 완료 행을 상위 계획에 기록하지 않았으며 단계 5 Linux도 시작하지 않았다.

### 세션 7 — Concept Frontend/React/TypeScript A

- 처리일: 2026-07-16
- 처리 대상: `frontend-backend-architecture`, `fullstack-project-flow`, `react-typescript-basics`, `react-form-state-event`, `react-useeffect-data-fetching` concept 5개
- raw 대응: R01~R05·R10~R13·R17·R19와 P01·P07·I03·I05의 실제 경로를 15/15로 확인했다. 날짜별 직접 구현 순서는 raw 날짜 MD와 세션 2~6에서 고도화한 날짜 Summary를 우선했고, R19가 실제로 04-15 Cart 삭제에서 끝나는 범위를 유지했다.
- 실제 처리: architecture는 React 화면/Router/axios→Spring Controller/Service/Repository/JPA→MySQL과 JSON·CORS·DTO·state 경계를 Fruit·Member·Product·Cart·Order로 재구성했다. project-flow는 날짜 허브를 복제하지 않고 환경→Fruit 최소 왕복→Member/JWT→Product→Cart→Order→대표 상품→검색으로 복잡성을 늘리는 반복 구현 절차를 설명하도록 독립 책임을 확정했다.
- React/TypeScript 처리: basics는 component·JSX·props/state·interface/type·event type·배열 state·optional chaining을 Fruit/Product/Cart/Page 응답에 연결하고 TypeScript type과 Java class/Entity/DTO/runtime JSON을 분리했다. form은 SignupPage·ProductInsertForm/ProductUpdateForm·Cart 수량에서 controlled input·name/value·spread·FileReader·오류 state/Spring Validation을 구분했다. useEffect는 Fruit·Product·Cart·Order·page/search의 mount·id/user/page/search dependency와 실제 요청 함수 호출·loading/error/state·UI/request/backend 소비 단계를 구분했다.
- 역할 중복 판정: architecture=계층/데이터 경계, project-flow=기능 확장 절차, basics=React/TS 표현 도구, form=사용자 입력 처리, useEffect=조회 실행 시점과 재요청 조건으로 중심 책임을 고정하고 세부 도메인은 기존 Product/Cart/Order/Paging concept에 위임했다.
- provenance: 대상 5개 code fence는 전체 0개, 선언 텍스트 raw 원문 검증 0개, 수동 fence 예외 0개다. PDF·이미지는 기존 구조/Router 설명을 유지하는 보조 source로만 사용했고 날짜별 직접 구현이나 새 코드를 만들지 않았다.
- 구조 검증: concept 5개 모두 필수 frontmatter·실재 source·허용 태그·위키링크·placeholder·실제 날짜·artifact·입력→처리→결과·혼동·선행/후속·직접/교안/후속 경계를 확인했다. 주 raw 매핑 15/15, index 설명 3개 갱신, scoped diff와 `git diff --check`, FrontEnd_BackEnd raw scoped status/diff를 기록 파일 반영 전 확인했다.
- 과목 상태: 미완료. 세션 7 완료 뒤 세션 8을 자동 실행하지 않았고, 단계 4 완료 행을 상위 계획에 기록하지 않았으며 단계 5 Linux도 시작하지 않았다.

### 세션 8 — Concept Frontend/React/TypeScript B

- 처리일: 2026-07-16
- 처리 대상: `axios-interceptor-error-handling`, `product-domain-flow`, `shopping-cart-flow`, `order-flow`, `pagination-search` concept 5개. 사용자의 세션 8 범위 재지정에 따라 기존 분할표의 데이터 concept 4개를 이번 묶음으로 앞당겼고, 세션 10에는 `jpa-relationship-mapping`만 남기도록 실행표를 맞췄다.
- raw 대응: R06~R18·R19, P03·P07·P08·P10, I01~I04의 실제 경로 매핑 22/22를 확인했다. 페이지별 직접 근거는 axios=R06·R07·R09~R12·R14~R16·R19, Product=R08~R11·R16~R19, Cart=R11~R15·R19, Order=R14~R16과 R19 끝 경계, Paging/Search=R16~R18과 R19 끝 경계로 대응했다.
- 보조자료 판단: P03·P07·P08·P10과 I01~I04의 HTTP/React/Spring/Pageable·Cart 관계 내용은 날짜 MD와 세션 2~6에서 고도화한 날짜 Summary에 필요한 구현 순서가 충분히 전사되어 있었다. PDF·이미지 전용 주장이나 code fence가 필요하지 않아 대상 페이지 source에 억지로 추가하지 않았다.
- 실제 처리: axios는 공통 요청 설정·Bearer token·로그인 외 401과 Signup/Product field Validation을 분리하고 Member·Product·Cart·Order 요청에서 frontend interceptor와 Spring filter/Service의 계층을 구분했다. Product는 Category/Product seed→목록→삭제→등록→수정→상세→대표 상품→페이징/검색의 날짜별 생명주기를 복원했다.
- Cart·Order 처리: Cart는 Product 상세 추가→관계/동일 품목 누적→입력 `CartProductDto`/출력 `CartItemDto`→checked/합계→quantity/stock→삭제→선택 주문 전환을 정리했다. Order는 04-16 Entity·생성 API, 04-17 즉시 주문·PENDING 목록, 04-20 역할별 카드·완료·취소·재고 복원을 분리하고 화면 버튼 표시와 실제 API 연결 시점도 구분했다.
- Paging/Search 처리: 04-20 Paging UI 준비, 04-21 page parameter·Page content/metadata와 검색 form/request·DTO·개별 Specification 준비, 04-22 Controller→Service 조건 조립→Repository Specification+Pageable 호출 코드 작성을 분리했다. Querydsl 용어 언급과 실제 Specification 구현을 구분하고, `JpaSpecificationExecutor` 상속·날짜 타입 정합성이 확인되지 않아 실행 성공은 미확정으로 남겼다.
- 역할 중복 판정: axios=공통 HTTP 요청·인증 오류, Product=상품 생명주기, Cart=관계·선택·수량, Order=생성·상태·재고, Paging=목록 분할·검색 조건 왕복으로 책임을 고정했다. 세션 7의 architecture=계층 경계, project-flow=반복 구현 절차, React/TypeScript=표현 도구, form=사용자 입력, useEffect=조회 실행 시점과 세부 책임을 중복하지 않도록 링크로 연결했다.
- 신규 후보 판단: HTTP/CORS 공통 흐름은 `frontend-backend-architecture`와 axios 페이지, Spring Validation은 `react-form-state-event`와 axios/Product 페이지에 흡수해 신규 지식 페이지를 만들지 않았다. CartProduct/OrderProduct 차이도 Cart·Order 페이지의 생명주기 경계로 흡수했다.
- 비동기 근거 감사 반영: raw 줄 범위 교차대조 후 04-09 Product 삭제의 일반 `axios` 사용, 04-10 `insertProduct()`의 저장 후 `null` 반환과 Controller 500 불일치, 04-14 동일 Cart 품목 누적 시 요청 quantity만 재고와 비교한 한계, 04-16 주문 함수/API와 04-17 실제 버튼 연결, Cart `some`의 quantity 0 전용 검사, client `memberId`·`role`과 서버 인가 미확인 경계를 추가 교정했다.
- 최종 독립 감사 반영: Signup의 field map body와 Product의 `{message, errors}` body를 분리하고, axios 페이지의 Order 목록·상태 주장에 R15·R16을 source로 추가했다. 04-22 검색은 backend 코드 연결과 실행 검증 완료를 구분해 조건부 통과 3건을 모두 해소했다.
- R19 경계: R19 본문이 실제로 04-15 Cart 삭제에서 끝나는 범위를 유지했다. 04-16 이후 Order·대표 상품·Paging/Search는 R14~R18 날짜 MD와 해당 Summary에만 귀속하고 R19에는 소급하지 않았다.
- provenance·구조 검증: 대상 5개 code fence는 전체 0개, 선언 텍스트 raw 원문 검증 0개, 수동 예외 0개다. 5개 모두 필수 frontmatter·실재 source·허용 태그·실재 위키링크·placeholder·날짜·artifact·입력→처리→결과·혼동·선행/후속·직접/교안/후속 경계를 확인했다. index의 기존 5개 설명은 현재 중심 책임과 명백히 어긋나지 않아 수정하지 않았다.
- 과목 상태: 미완료. 세션 8 완료 뒤 세션 9를 자동 실행하지 않았고, 단계 4 완료 행을 상위 계획에 기록하지 않았으며 단계 5 Linux도 시작하지 않았다.

### 세션 9 — Concept Backend/Spring A

- 처리일: 2026-07-16
- 처리 대상: `spring-boot-rest-api`, `dto-entity-service-controller`, `jwt-session-cookie-auth`, `spring-security-jwt-filter`, `spring-data-jpa-repository` concept 5개
- 주 raw 대응: R02~R08·R12·R18과 P03·P04·P08의 실제 경로 매핑을 12/12로 확인했다. 날짜별 직접 구현은 raw 날짜 MD와 세션 2~6의 고도화 Summary를 우선했으며, P03·P04·P08의 필요한 내용이 텍스트 raw에 전사되어 PDF를 대상 페이지 source에 억지로 추가하지 않았다. Product CRUD·Cart·Order·Page 및 Repository 확장 날짜 확인에는 R01·R09~R11·R13~R17을 보조 직접 근거로 사용했다.
- REST 처리: 03-31 HTML/Model과 REST/JSON 분기→04-01 axios·CORS 왕복→Member Signup/Login→Product CRUD→Cart→Order→Page로 확장된 method·URL·path/query/body·status/body shape를 복원했다. Signup field map과 Product `{message, errors}`를 분리하고 UI control 표시일과 실제 API 연결일을 구분했다.
- 데이터 모양 처리: Fruit·Member·Product·Cart·Order에서 React TypeScript 선언, runtime JSON, Java 요청/응답 DTO·map, JPA Entity, Controller·Service 전달을 분리했다. `CartProductDto`/`CartItemDto`, `OrderDto`·`OrderProductDto`/`OrderDetailDto`의 입력·출력 방향을 구분하고 client memberId/role을 서버 인증·인가 완료로 보지 않았다.
- 인증/Security 처리: 04-06의 Session·Cookie·JWT 비교와 구성 작성을 04-07 login/logout·filter/API 실제 연결과 분리했다. request interceptor의 Bearer 부착→filter의 prefix 제거·검증·Authentication/SecurityContext 구성→Controller/Service 업무 처리를 계층별로 나누고, role UI·client role·token authority·endpoint authorization을 구분했다.
- Repository 처리: 03-30~31 Fruit를 JPA 이전 baseline으로 두고 04-02 Member `JpaRepository`, 04-03 seed/derived query, 04-08 Product, 04-14 Cart, 04-16~20 Order, 04-21~22 Pageable/Specification 호출로 확장했다. 04-17 Repository 선언명과 Service 호출명 불일치를 그대로 보존했으며 04-22 `JpaSpecificationExecutor` 상속 미확인, `LocalDate`/`LocalDateTime` 정합성, 실행 성공 미확정 경계를 명시했다.
- 역할 중복 판정: REST=HTTP 왕복, DTO/Entity=계층 사이 데이터 모양, JWT=인증 방식/token 생명주기, Security filter=token 검증·SecurityContext, Repository=선언·DB 접근으로 책임을 고정했다. 세션 7의 architecture/project-flow/React/form/useEffect와 세션 8의 axios/Product/Cart/Order/Paging 세부는 반복하지 않고 링크로 위임했다.
- R19 경계: R19 끝부분의 실제 마지막 기록이 04-15 Cart 삭제·테스트와 `2026.04.15(수).txt 까지 마무리 함`임을 확인했다. 04-16 이후 Order·대표 상품·검색을 R19에 소급하지 않았다.
- provenance·최종 검증: 대상 5개 code fence는 전체 0개, 텍스트 raw 원문 검증 0개, 수동 예외 0개다. 필수 frontmatter·source 실경로·허용 태그·위키링크·placeholder·날짜·artifact·입력→처리→결과·혼동·선행/후속·직접/교안/후속 경계를 확인했다. 현재 내용과 명백히 어긋난 index 설명 5개를 갱신했고, 기록 파일 반영 뒤 scoped `git diff --check`와 FrontEnd_BackEnd raw status/diff를 통과했다.
- 과목 상태: 미완료. 세션 9만 처리했으며 세션 10과 단계 5 Linux는 시작하지 않았다. 단계 4 완료 행도 상위 계획에 기록하지 않았다.

### 세션 10 — Concept Backend/Spring/데이터 B

- 처리일: 2026-07-16
- 처리 대상: `jpa-relationship-mapping` concept 1개만 전면 고도화했다. 세션 8의 `product-domain-flow`, `shopping-cart-flow`, `order-flow`, `pagination-search`와 다른 지식 페이지 본문은 재처리하지 않았다.
- raw·artifact 매핑: R11·R12·R14·R19, P08, I01~I04의 실제 경로를 9/9 확인했다. 관계의 직접 구현 순서는 R11·R12·R14와 고도화된 04-13·04-14·04-16 Summary를 우선했다. 03-30 Fruit·04-02 Member·04-08 Product는 R01·R04·R08을 선행 배경 source로만 추가했다.
- 이미지·교안 판단: I01은 회원 Cart와 품목별 수량 비유, I02는 Cart→CartProduct→Product 분리, I04는 Member 1:1 Cart·Cart 1:N CartProduct·CartProduct N:1 Product와 quantity를 직접 확인해 source에 선언했다. I03은 React Router 그림이라 JPA 근거에서 제외했다. P08의 cascade·orphan removal은 R11·R14에 필요한 페이지·설명이 전사돼 PDF 자체를 열거나 source에 추가하지 않았다.
- 관계·FK 확정: Cart가 `member_id`, CartProduct가 `cart_id`·`product_id`, Order가 `member_id`, OrderProduct가 `order_id`·`product_id` FK를 관리하는 owning side임을 실제 Entity 코드로 확인했다. `Cart.cartProducts`의 `mappedBy = "cart"`, `Order.orderProducts`의 `mappedBy = "order"`는 반대편 Java 필드를 가리키며, Member/Product 쪽 반대편 컬렉션은 원본에서 확인되지 않는다고 경계를 남겼다.
- 날짜별 흐름: 04-13은 관계 Entity·quantity·Repository·상품 상세 Cart 요청 준비, 04-14는 인증 email→Member→Cart 조회/생성→Product·동일 품목 탐색→quantity 누적/신규 CartProduct 저장→CartItemDto 목록, 04-16은 별도 Order/OrderProduct·DTO와 Service의 관계 조립→재고 차감→CartProduct 후속 삭제→Order 저장으로 구분했다.
- 생명주기·신규 후보 판단: CartProduct는 주문 전 수정·삭제 가능한 Cart 관계, OrderProduct는 주문 생성 때 Product·quantity로 새로 만든 주문 품목으로 분리했다. 가격 snapshot 필드는 확인되지 않는다고 명시했다. `CartProduct vs OrderProduct`와 `JPA cascade vs DB ON DELETE` 후보는 이 페이지와 기존 Cart/Order concept·Oracle comparison으로 흡수하고 신규 페이지는 만들지 않았다.
- cascade 경계: Cart·Order 컬렉션의 `CascadeType.ALL`, Order에만 확인되는 `orphanRemoval = true`, Oracle DB FK의 `ON DELETE`를 JPA EntityManager와 DB 엔진이라는 다른 동작 주체·계층으로 분리했다. CartProduct의 직접 Repository 저장과 Order 저장 시 자식 전이도 Service 흐름에 맞춰 구분했다.
- R19·provenance: R19는 실제 04-15 Cart 삭제에서 끝나는 범위만 사용하고 04-16 Order를 소급하지 않았다. 대상 code fence는 전체 0개/선언 텍스트 raw 원문 검증 0개/수동 fence 예외 0개다.
- 구조 검증: concept 1개에 정의·중요성·첫/확장 날짜·artifact·입력→처리→결과·6개 관계의 owning side/FK·미확정 반대편·두 관계 Entity 비교·cascade/DB 경계·혼동·선행/후속·직접/교안/후속 과목 경계를 확인했다. frontmatter·source 10/10 실경로·허용 태그·위키링크·placeholder·index 설명·scoped diff를 검사했고, 기존 index 설명은 현재 중심 책임과 어긋나지 않아 유지했다.
- 과목 상태: 미완료. 세션 10만 처리했으며 세션 11과 단계 5 Linux를 시작하지 않았다. 단계 4 완료 행도 상위 계획에 기록하지 않았다.

### 세션 11 — Concept Backend/Spring/데이터 C

- 처리일: 2026-07-16
- 처리 대상: `spring-data-jpa-specification-pageable`, `spring-product-search-flow`, `database-normalization-functional-dependency`, `oracle-sequence` concept 4개만 고도화했다. 세션 8의 Product·Cart·Order·Paging concept와 세션 10의 `jpa-relationship-mapping`, 다른 지식 페이지 본문은 재처리하지 않았다.
- raw·교안 매핑: R01·R14·R17·R18·P08·P10의 실제 경로를 6/6 확인했다. 검색의 직접 구현은 R17·R18, 정규화 후속 적용은 R01·R14, sequence 전환 경계는 R01·R14와 04-02 Member의 GeneratedValue를 사용했다. Oracle 직접 근거는 03-16~03-18 sequence와 03-20 함수 종속성·정규화 raw/고도화 페이지를 유지했다. P08·P10의 필요한 내용은 날짜 MD와 Summary에 충분히 전사되어 PDF를 직접 열거나 대상 source에 추가하지 않았다.
- 검색 객체 처리: `spring-data-jpa-specification-pageable`은 04-20 Paging UI 준비, 04-21 단순 Pageable 왕복·검색 state/request/DTO/개별 Specification 준비, 04-22 조건 조립·Sort·PageRequest·Specification+Pageable 호출을 날짜별로 분리했다. Specification=동적 조건, Pageable/PageRequest=page·size·sort 전달, Page=결과 wrapper로 책임을 고정했다.
- 검색 왕복 처리: `spring-product-search-flow`은 control/state→request parameter→Controller 수신→SearchDto→Service Specification 조립→Repository 호출→Page 응답→MySQL SQL 대조를 단계별로 나눴다. Querydsl 용어·보충과 실제 Specification 구현을 분리하고 화면·요청·backend 소비·DB 결과를 한 완료 상태로 합치지 않았다.
- 실행 미확정 경계: 04-22 ProductRepository의 `JpaSpecificationExecutor<Product>` 상속이 확인되지 않고 Product `inputdate`는 `LocalDate`, 날짜 조건 비교값은 `LocalDateTime`임을 명시했다. Repository 호출 코드와 MySQL 시나리오는 확인되지만 실제 Specification API 성공 응답·확정 결과 건수는 없어 runtime 검색 성공을 단정하지 않았다.
- Oracle 원리·후속 경계: `database-normalization-functional-dependency`는 함수 종속성→정규화/분해→PK/FK→JOIN→JPA Entity 관계를 서로 다른 계층으로 구분하고 R14 Order/OrderProduct는 후속 적용 사례로만 연결했다. owning side·mappedBy·cascade 생명주기는 `jpa-relationship-mapping`에 위임했다. `oracle-sequence`는 Oracle 독립 schema 객체·NEXTVAL·USER_SEQUENCES와 MySQL/JPA GeneratedValue(AUTO)를 같은 구현으로 합치지 않고, 실제 MySQL AUTO_INCREMENT/GenerationType별 동작은 미확정으로 남겼다.
- provenance·구조 검증: 대상 4개 code fence는 전체 0개/선언 텍스트 raw 원문 검증 0개/수동 예외 0개다. 4개 모두 정의·중요성·첫/확장 날짜·artifact·입력→처리→결과·확인/미확정 범위·혼동·선행/후속·직접/교안/후속 경계를 갖췄고, frontmatter·실재 source·허용 태그·실재 위키링크·placeholder 검사 오류는 0건이다. 현재 내용과 명백히 어긋난 index 설명 4개만 갱신했다.
- 과목 상태: 미완료. 세션 11만 처리했으며 세션 12와 단계 5 Linux를 시작하지 않았다. 단계 4 완료 행도 상위 계획에 기록하지 않았다.

### 세션 12 — Entity A

- 처리일: 2026-07-16
- 처리 대상: `spring-boot`, `react`, `typescript`, `jwt`, `mysql` Entity 5개만 전면 고도화했다. 세션 7~11의 Summary·Concept와 다른 Entity·Comparison·Query 본문은 재처리하지 않았다.
- raw·교안 매핑: R01~R18과 P04·P05·P07·P08의 실제 경로를 22/22 확인했다. 날짜별 기술 이력과 직접 구현은 R01~R18 날짜 MD와 세션 2~6에서 고도화한 날짜 Summary를 우선했다. PDF 4개는 필요한 내용이 날짜 MD/Summary에 충분히 전사되어 있어 직접 열거나 Entity source에 추가하지 않았다.
- Spring Boot: 03-30 생성 시 선택한 DevTools·Lombok·Data JPA·MySQL Driver·Thymeleaf·Web·Web Services·H2와 실제 사용 날짜를 분리했다. Fruit HTML/JSON→Member/JWT→Product→Cart→Order→Pageable/Specification으로 확장된 Controller·Service·Repository·Security 이력을 복원하고, H2/Web Services 사용·04-10 반환 불일치·04-17 Repository 명칭·04-22 executor/날짜 type/runtime 검색 성공의 미확정 경계를 보존했다.
- React·TypeScript: React 자체의 component/state/rendering과 Router·axios·Bootstrap·TypeScript를 구분하고, 03-30 Vite→04-01 Fruit 왕복→Member/Product/Cart/Order→Paging/Search UI 이력을 정리했다. TypeScript는 Fruit/Product/User/Cart/Order/Page/Search type, props/state, event type, 배열·optional chaining을 compile-time 계약으로 설명하고 runtime JSON·Java DTO/Entity·DB 행과 분리했다.
- JWT: 04-06의 Cookie/Session/JWT 이론·dependency·provider·LoginPage/axiosInstance 준비와 04-07 login 인증·token 응답·Bearer filter·SecurityContext·logout 연결을 분리했다. localStorage token, React role UI, token authority, server endpoint authorization을 같은 완료 상태로 합치지 않았다.
- MySQL: 03-30 Oracle 직접 SQL에서 로컬 MySQL/JPA runtime으로의 전환, datasource/dialect, Member·Product·Cart·Order 데이터 흐름과 04-21 LIMIT/OFFSET·04-22 기간/category/LIKE 검색 SQL을 날짜별로 정리했다. Oracle sequence/SQL과 GeneratedValue/MySQL SQL을 구분하고, 원본에 없는 Order table 구조·query 결과·API 확정 건수를 만들지 않았다.
- 책임 경계: Entity는 기술의 첫 등장·날짜별 확장·과목/후속 경계를 맡고, architecture/project-flow/React 표현·입력·조회 시점/JWT 비교·Security filter/Repository/Product·Cart·Order·검색/JPA 관계의 원리와 세부 흐름은 세션 7~11 Concept 링크로 위임했다.
- provenance·구조 검증: Entity 5개의 code fence는 전체 0개/선언 텍스트 raw 원문 검증 0개/수동 예외 0개다. Entity source union은 R01~R18 18/18, P 매핑은 4/4이며 PDF는 미사용 보조자료로 종결했다. 5개 모두 필수 frontmatter·실재 source·허용 태그·실재 위키링크·placeholder·정의·중요성·첫/확장 날짜·artifact·입력→처리→결과·확인/미확정·혼동·선행/후속·직접/교안/후속 경계를 확인했다. index는 명백히 일반 정의에 머물던 MySQL 설명 1개만 갱신했다.
- 변경 기준선: 5개 Entity는 시작 전 diff 0건으로 이번 세션 신규 변경이다. inventory/index/log는 시작 전부터 앞선 세션 변경이 누적돼 있어 기존 내용을 보존하고 세션 12 항목만 추가했다.
- 과목 상태: 미완료. 세션 12만 처리했으며 세션 13과 단계 5 Linux를 시작하지 않았다. 단계 4 완료 행도 상위 계획에 기록하지 않았다.

### 세션 13 — Entity B

- 처리일: 2026-07-16
- 처리 대상: `node-js`, `visual-studio-code`, `intellij-idea`, `oracle-database` Entity 4개만 고도화했다. 세션 2~12의 Summary·Concept·Entity A와 다른 Comparison·Query 본문은 재처리하지 않았다.
- raw·교안 매핑: R01~R05와 P02·P06·P09의 실제 경로 매핑을 8/8 확인하고 Java 02-26~27 IntelliJ, Oracle 03-13~20 직접 수업 경계를 대조했다. Node.js·VS Code의 실제 설치·사용 이력은 R01~R05와 고도화 Summary에 충분히 전사되어 P06·P09를 직접 열거나 source에 추가하지 않았다.
- Node.js: 03-30 설치·npm 11.11.0 확인→Vite React/TypeScript scaffold→npm package 설치→Vite development server 5173 화면을 하나의 개발환경 흐름으로 정리했다. Node.js runtime, npm package manager, Vite project/dev/build tool, React browser rendering을 분리하고 production build 산출물은 미확정으로 보존했다.
- editor·IDE: VS Code는 03-30 설치와 03-31 project open, 04-01 Fruit type/API 화면, 04-02~03 HomePage·SignupPage 편집 이력을 구분했다. IntelliJ는 Java `MyJava` project·Run에서 03-30 Spring `spring_cafe` open/JDK 21/application 실행, 03-31 Controller, 04-02~03 Member 계층 작성으로 확장했다. npm·Vite·React와 Java·JVM·Maven·Spring Boot의 실행 책임을 editor/IDE 기능으로 합치지 않았다.
- P02 중복 경계: FrontEnd_BackEnd P02와 Java `IntelliJ 교안.pdf`의 SHA-256이 모두 `f1280e7ced57aa898acf77d0f18e8b9b57382c96e9fb205958f9487297f01fb4`이고 byte comparison도 일치함을 재확인했다. Java 단계의 동일 교안을 기존 source로 유지하고 P02를 중복 source로 선언하거나 새 사실을 만들지 않았다.
- Oracle 경계: 03-13~20 Oracle XE·DBeaver·직접 SQL·schema·sequence·constraint·transaction·JOIN/설계를 선행 이력으로 유지하고, 03-30부터 MySQL Server·Workbench·Driver·Spring Data JPA runtime으로 전환됐음을 강화했다. Oracle `NEXTVAL`과 JPA `GeneratedValue(AUTO)`, Oracle SQL/schema와 MySQL `coffee` DB·검색 SQL을 같은 구현으로 합치지 않았으며 AUTO의 구체 DB 동작은 미확정으로 남겼다.
- 책임 중복 판정: Entity는 기술·도구의 첫 등장과 날짜별 사용 이력·직접/후속 경계를 맡는다. 전체 계층, 반복 구현 절차, React/TypeScript 표현, Spring Boot·React·MySQL의 세부 기능, sequence·JPQL/SQL 원리는 기존 architecture/project-flow/Concept/Entity A 페이지에 링크로 위임했다.
- provenance·구조 검증: 대상 4개 code fence는 전체 0개/선언 텍스트 raw 원문 검증 0개/수동 예외 0개다. 4개 모두 필수 frontmatter·실재 source·허용 태그·실재 위키링크·placeholder·정의·중요성·첫/확장 날짜·artifact·입력→처리→결과·확인/미확정·혼동·선행/후속·직접/교안/후속 경계를 확인했다. 현재 내용과 명백히 어긋난 index Entity 설명 4개만 갱신했다.
- 변경 기준선: 세션 시작 시 live scoped diff에서 대상 Entity 4개 모두 diff 0건이었다. 따라서 4개 Entity는 모두 이번 세션 신규 변경이며, inventory/index/log는 앞선 세션 변경이 누적된 파일에 세션 13 기록만 추가했다. 사용자 메시지의 failed mutation verifier에 나온 `spring-boot`·`typescript` 삭제 실패도 live Git 상태에서 실제 삭제·추가 변경이 없음을 확인했다.
- 과목 상태: 미완료. 세션 13만 처리했으며 세션 14와 단계 5 Linux를 시작하지 않았다. 단계 4 완료 행도 상위 계획에 기록하지 않았다.

### 세션 14 — Comparison A

- 처리일: 2026-07-16
- 처리 대상: `controller-service-repository`, `entity-vs-dto`, `props-vs-state`, `react-router-vs-spring-api-url`, `mpa-vs-spa`, `session-vs-cookie-vs-jwt` Comparison 6개만 고도화했다. 세션 2~13의 Summary·Concept·Entity와 세션 15의 Comparison/Query 본문은 재처리하지 않았다.
- raw 매핑: 주 범위 R03·R06·R07·R10·R12~R18의 실제 경로를 source union 11/11로 대응했다. 첫 비교 시점과 Fruit HTML→REST 전환 확인에는 R01·R02·R05를 필요한 페이지에서만 보조 사용했다.
- 교안·이미지 판단: P01·P03·P04·P07·P08의 역할과 실제 경로를 5/5 확인했다. 필요한 설명은 날짜 MD와 고도화 Summary에 충분히 전사되어 PDF를 직접 열거나 source에 추가하지 않았다. I03은 실제 이미지를 열어 Audience를 ticket에 맞는 Theater로 안내하는 Router 비유만 확인했고, Spring API·server·DB 근거로 확대하지 않은 채 Router comparison source에 선언했다.
- 계층·데이터 경계: Controller의 HTTP 입력·응답, Service의 업무 흐름·검증·transaction, Repository의 DB 접근을 Member→Product→Cart→Order→검색 날짜로 비교했다. Entity·요청/응답 DTO·Map 응답·React TypeScript type·runtime JSON·DB row를 분리하고 Product Entity 직접 수신, Cart 입력/출력 DTO, Order Entity→DTO 변환을 실제 구현대로 보존했다.
- React·URL 경계: props/state의 소유권과 변경을 callback·setter·API·DB 저장과 분리했다. React Router path와 Spring API URL은 Fruit·Cart·Product에서 문자열이 같아도 runtime·port·요청 주체·결과가 다름을 설명했고, CORS를 다른 origin 간 browser 정책으로 분리했다.
- rendering·인증 경계: MPA/SPA는 03-31 Thymeleaf HTML→REST/React와 04-06 이론을 rendering 축으로 정리하고 Session/JWT와 일대일 대응시키지 않았다. Cookie=browser 저장·전달, Session=server 상태, JWT=서명 token 층위를 나누고 04-06 이론·구성 준비와 04-07 login·localStorage·Bearer filter·SecurityContext 실제 연결을 분리했다.
- 완료 경계: 모든 기능에서 세 계층·transaction·DTO·authorization이 완성됐다고 소급하지 않았다. 04-17 transaction 추가 시점, 04-22 Specification executor/날짜 type/runtime 검색 미확정, cookie option·session 저장 위치·전 endpoint authorization 미확정을 보존했다.
- 독립 감사 반영: 비동기 raw 교차감사 뒤 props의 04-06 `onLogin` callback, Router의 03-31 자리표시→04-01 첫 실제 API 왕복과 04-07 Security CORS 이동, Session/JWT의 04-14 인증 email 소비·04-17 role/memberId 미확정 경계를 추가했다. 03-31 Thymeleaf는 완성 MPA 전체가 아니라 server-rendered HTML 응답 패턴으로 한정하고, JWT claim 구성 코드와 관찰된 runtime token 내용을 분리했다.
- provenance·구조 검증: 대상 code fence는 전체 0개/선언 텍스트 raw 원문 검증 0개/수동 fence 예외 0개다. Comparison 6개 모두 비교 목적·첫/확장 날짜·표·선택 상황 2개 이상·입력→처리→결과·공존 관계·확인/미확정·동일시 교정·선행/후속·직접/후속 경계와 frontmatter·실재 source·허용 태그·위키링크·placeholder를 통과했다. 현재 내용과 명백히 어긋난 index 설명 6개만 갱신했다.
- 변경 기준선: 대상 Comparison 6개는 세션 시작 전 live diff 0건으로 이번 세션 신규 변경이다. inventory/index/log는 앞선 세션 변경과 병행해 생성된 학습 가이드 기록을 보존하고 세션 14 기록만 추가했다.
- 과목 상태: 미완료. 세션 14만 처리했으며 세션 15와 단계 5 Linux를 시작하지 않았다. 단계 4 완료 행도 상위 계획에 기록하지 않았다.

### 세션 15 — Comparison/Query B

- 처리일: 2026-07-16
- 처리 대상: 기존 `authentication-vs-authorization`, `passwordless-vs-password-login` Comparison 2개를 고도화하고 `why-shopping-cart-order-flow-is-complex`, `jwt-role-ui-vs-server-authorization` Query 2개를 신규 생성했다. 세션 2~14의 Summary·Concept·Entity·Comparison A 본문은 재처리하지 않았다.
- raw·교안·이미지 매핑: R06·R07은 비밀번호 login/JWT 준비와 credential·Bearer 인증 연결, R12~R16은 Cart·Order 관계·선택·수량·재고·생성·상태·취소 및 role UI 경계로 대응했다. P04·I01·I02·I04는 날짜 MD와 현재 고도화된 Summary/Concept에 필요한 내용이 충분히 전사되어 PDF·이미지를 직접 열거나 새 페이지 source에 중복 추가하지 않았다.
- 인증/인가 경계: 04-06의 LoginPage·JWT provider·role UI 준비와 04-07의 `AuthenticationManager` login·Bearer filter·`GrantedAuthority`·SecurityContext 실제 연결을 분리했다. React `user.role`, localStorage user, JWT role Claim, Spring authority, SecurityContext Authentication, endpoint authorization을 계층별로 나눴다.
- 확인/미확정 경계: 04-07 `SecurityConfig`의 `permitAll`·`authenticated`는 확인했지만 endpoint별 role 정책은 만들지 않았다. 04-17~20의 client memberId·role과 role별 버튼은 UI/API 시나리오로 기록하고 JWT principal·authority 대조, ADMIN·주문 소유자 검사는 미확정으로 보존했다.
- Passwordless 경계: 04-06~07 email/password→AuthenticationManager→JWT 직접 구현을 기준선으로 두고 05-14·05-18·05-21의 X1280 개념·샘플·Postman API와 중간 프로젝트 적용 가이드를 후속 경계로만 비교했다. FrontEnd_BackEnd에서 Passwordless를 직접 구현한 것으로 소급하지 않았다.
- Cart/Order 복잡성: Member·Product·Cart·CartProduct·Order·OrderProduct 관계, 입력/출력 DTO, React `checked`, Cart/Order `quantity`, Product `stock`, Cart 삭제·Order 저장, transaction, PENDING 목록·완료·취소·재고 복원을 서로 다른 데이터 모양·생명주기·저장 책임으로 추적했다.
- provenance·구조 검증: 4개 페이지 모두 frontmatter·실재 source·허용 태그·실재 위키링크·placeholder와 Comparison/Query 필수 구조를 통과했다. code fence는 전체 0개/선언 텍스트 raw 원문 검증 0개/수동 예외 0개다. 신규 Query 2개는 `wiki/index.md`에 등록하고 Total pages를 269로 갱신했다.
- 변경 기준선: 시작 전 기존 변경은 Comparison 2개·Query 2개 모두 0건이었다. 이번 세션 지식 페이지 변경은 이 4개뿐이며, inventory/index/log에는 세션 15 기록만 추가한다. 종료 시 scoped diff·`git diff --check`·raw 비수정을 다시 검증한다.
- 과목 상태: 미완료. 세션 15만 처리했으며 세션 16과 단계 5 Linux를 시작하지 않았다. 단계 4 완료 행도 상위 계획에 기록하지 않았다.

### 세션 16 — 과목 전체 고정점

- 처리일: 2026-07-16
- 기준선·대상: FrontEnd_BackEnd 직접 source를 가진 최종 지식 페이지 59개를 `summary 19 / concept 20 / entity 9 / comparison 9 / query 2`로 재계산했다. 신규 페이지는 없으며 `wiki/index.md`의 Total pages는 269를 유지한다.
- raw 전수 대응: R01~R19는 실제 MD 19개·총 22,838행을 다시 열어 읽었고, P01~P10은 PDF 10개 모두 텍스트 추출이 가능한 실제 파일임을 확인했으며, I01~I05는 5개 이미지의 크기·hash와 앞선 실제 판독 결과를 다시 대응했다. 직접 구현 날짜는 R01~R18, R19는 04-15 Cart 삭제에서 끝나는 보조 복습 경계로 유지했다.
- 내용 고정점: Fruit→Member/JWT→Product→Cart→Order→Pageable/검색의 최초 등장·후속 확장, React/Spring/DB 책임, 04-06 준비→04-07 인증 연결, 04-16 생성→04-17 목록→04-20 상태 처리, 04-21 frontend→04-22 backend 검색 코드와 실행 미확정 경계를 전수 확인했다. Passwordless·Linux·AWS·CI/CD·중간 프로젝트를 4과목 직접 구현으로 소급하지 않았다.
- 최소 교정: `jpql-vs-sql`의 SQL·JPQL fence 2개를 실제 raw의 공백·주석·한 줄 method 선언과 일치시켰다. 신규 Query 2개와 세션 15 Comparison 2개가 Summary·Concept·Entity에서 역링크를 갖도록 관련 페이지 6곳에 링크 10개만 보강했다. 그 외 세션 2~15 본문은 재작성하지 않았다.
- 구조 고정점: 59개 모두 필수 frontmatter·실재 source·허용 태그·index 등록·위키링크·비고립·placeholder 검사를 통과했다. code fence는 전체 2개이며 원문 연속 대조 2/2, 실패 0개다. 신규 Query와 세션 15 Comparison은 각각 Summary·Concept·Entity 역링크를 최소 1개 이상 갖는다.
- 과목 상태: **최종 완료**. 상위 계획 완료 행과 index/log를 함께 갱신했으며 단계 5 Linux는 시작하지 않았다.

## 관련 페이지

- [[_meta/wiki-content-rehighquality-work-plan|LLM Wiki 내용 재고도화 작업 계획]]
- [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]
- [[concepts/product-domain-flow|상품 도메인 기능 흐름]]
- [[concepts/shopping-cart-flow|장바구니 기능 흐름]]
- [[concepts/order-flow|주문 기능 흐름]]
- [[concepts/pagination-search|페이징과 검색]]
