---
title: FrontEnd_BackEnd 내용 재고도화 전수 재고와 실행 분할 계획
created: 2026-07-15
updated: 2026-07-15
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

이 문서는 내용 재고도화 단계 4 `FrontEnd_BackEnd`의 세션 1 결과다. 실제 지식 페이지 고도화 전의 읽기 감사·대응표·실행 분할 계획만 보존한다.

- 이번 세션에서 수정한 범위: 이 meta 문서, `wiki/index.md`, `wiki/log.md`
- 이번 세션에서 수정하지 않은 범위: `raw/`, 기존 summary/concept/entity/comparison/query 본문
- 과목 완료 상태: 미완료
- 다음 과목: 단계 5 Linux는 시작하지 않음
- 완료 선언 시점: 아래 세션 2~16의 수정·원문 provenance·최종 고정점 검증이 모두 끝난 뒤

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
| 8 | Concept Frontend/React/TypeScript B | `axios-interceptor-error-handling`; HTTP/CORS·Validation 신규 후보 판단 | R02~R07, R10, R19, P03·P07·P08 |
| 9 | Concept Backend/Spring/인증 A | `spring-boot-rest-api`, `dto-entity-service-controller`, `jwt-session-cookie-auth`, `spring-security-jwt-filter`, `spring-data-jpa-repository` | R02~R08, R12, R18, P03·P04·P08 |
| 10 | Concept Backend/Spring/데이터 B | `jpa-relationship-mapping`, `product-domain-flow`, `shopping-cart-flow`, `order-flow`, `pagination-search` | R08~R18, P08·P10, I01~I04 |
| 11 | Concept Backend/Spring/데이터 C | `spring-data-jpa-specification-pageable`, `spring-product-search-flow`, `database-normalization-functional-dependency`, `oracle-sequence` | R01, R14, R17, R18, P08·P10; Oracle 선행 페이지 경계 |
| 12 | Entity A | `spring-boot`, `react`, `typescript`, `jwt`, `mysql` | R01~R18, P04·P05·P07·P08 |
| 13 | Entity B | `node-js`, `visual-studio-code`, `intellij-idea`, `oracle-database` | R01~R05 중심, P02·P06·P09; Java·Oracle 선행 경계 |
| 14 | Comparison A | `controller-service-repository`, `entity-vs-dto`, `props-vs-state`, `react-router-vs-spring-api-url`, `mpa-vs-spa`, `session-vs-cookie-vs-jwt` | R03, R06, R07, R10, R12~R18, P01·P03·P04·P07·P08, I03 |
| 15 | Comparison/Query B | `authentication-vs-authorization`, `jpql-vs-sql`; CartProduct/OrderProduct·JPA cascade/DB ON DELETE 신규 후보와 실제 query 기록 판단 | R06, R11~R18, P04·P08, I01~I04; Oracle·Passwordless 경계 |
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
