---
title: 2026-04-08 Category·Product 도메인과 상품 목록 시작
created: 2026-07-06
updated: 2026-07-15
type: summary
tags: [spring-boot, react, backend, frontend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md
status: growing
confidence: high
---

# 2026-04-08 Category·Product 도메인과 상품 목록 시작

## 한 줄 요약

`Category`와 `Product`로 상품 데이터 구조를 정의하고 이미지 파일 기반 초기 데이터를 Repository 단위 테스트로 저장한 뒤, Repository → Service → Controller 목록 API와 React `Product` type → `ProductList` 화면을 연결해 상품 도메인의 첫 조회 흐름을 만들었다.

## 수업 위치와 날짜 연결

- 이전: [[summaries/2026-04-07-member-api-string-token|2026-04-07]]에 JWT 로그인·요청 인증 흐름을 연결했다.
- 오늘: 회원 기능 다음 핵심 업무인 상품 도메인을 만들고 목록 API·화면까지 첫 왕복을 구현했다.
- 다음: [[summaries/2026-04-09-product-delete-routing-jsx-table|2026-04-09]]에는 상품 삭제와 목록 갱신, 상품 등록 form으로 CRUD 범위를 넓힌다.

## 실제 교시 흐름

### 1교시 — 자료 준비, OCI 소개, Category

- 상품 실습용 Spring·React 자료와 이미지 자료를 준비했다.
- OCI는 “Oracle에서 제공하는 AWS 같은 것”이라는 짧은 소개와 가입 자료 안내만 있었다. 이날의 중심 구현은 OCI가 아니라 상품 기능이다.
- `Category` enum에 전체·빵·음료수·케이크·마카롱 값을 두고, 각 상수의 한글 설명을 생성자와 `getDescription()`으로 꺼낼 수 있게 했다.

### 2교시 — Product Entity와 DB 테이블

- `Product` Entity를 `products` 테이블에 연결하고 id·name·price·category·stock·image·description·inputdate 필드를 정의했다.
- name/image/description의 빈 값, price/stock 범위, category null, description 길이에 Validation annotation을 붙였다.
- category는 `EnumType.STRING`, inputdate는 날짜 JSON 형식으로 매핑했다.
- 애플리케이션을 실행해 Hibernate의 products table 생성 구문을 확인하고 MySQL Workbench의 `desc products`로 실제 컬럼 구조를 확인했다.
- 이미지 초기 데이터 준비를 위해 로컬 이미지 폴더를 마련했다.

### 3~4교시 — File·String·Random 보충 실습

- `FileTest`에서 이미지 폴더가 실제로 존재하는지, directory인지, 내부 항목이 file인지 순서대로 검사했다.
- `.jpg`로 끝나는 파일을 골라 `lastIndexOf()`와 `substring()`으로 파일명과 확장자를 분리했다. 전날 배운 `String` 처리가 상품 이미지 데이터 준비에 다시 사용됐다.
- `RandomTest`에서는 boolean, 주사위 범위, 배열 항목, 가격 범위를 무작위로 만드는 방법을 연습했다.

### 5교시 — Repository·GenerateData·단위 테스트 seed

- `ProductRepository`를 `JpaRepository<Product, Long>` 기반으로 만들었다.
- `GenerateData`는 이미지 폴더의 파일명으로 Product 데이터를 만드는 유틸리티 역할을 맡았다.
- `ProductTest.createProductMany()`가 이미지 파일명 목록을 받고, 각 항목으로 Product를 만든 뒤 Repository `save()`를 반복해 products table의 초기 데이터를 채웠다.

### 6교시 — React 상품 화면의 경로와 type

- `MenuItems.tsx`의 상품 보기 메뉴를 `/product/list`로 연결했다.
- `AppRoutes.tsx`에 `ProductList` route를 추가했다.
- Spring `Product` Entity를 기준으로 React `Product` interface를 만들었다. Java enum은 JSON에서 string, `LocalDate`는 string으로 받는 형태를 적었다.

### 7교시 — 목록 화면과 Spring 목록 API

- `ProductList.tsx`에서 `Product[]` state를 만들고 첫 render 뒤 axios GET으로 `/product/list`를 요청했다.
- 성공 응답은 `setProducts(response.data)`로 state에 넣고, `map()`으로 상품 image·name·id·price를 card 목록에 표시했다. 실패는 console에 기록했다.
- `ProductRepository.findProductByOrderByIdDesc()`로 id 역순 상품 목록을 조회했다.
- `ProductService.getProductList()`가 Repository 조회를 호출하고, `ProductController.list()`가 `/product/list` GET 응답으로 목록을 반환했다.

### 8교시 — 상품 목록 공개 경로 확인

- `SecurityConfig`의 허용 URL 배열에 상품 경로가 이미 추가되어 있는지 확인했다.

## 대표 artifact

| 단계 | 대표 artifact | 역할 |
|---|---|---|
| 도메인 | `Category`, `Product` | 카테고리 값과 상품 필드·Validation·JPA 매핑 정의 |
| 파일 준비 | `FileTest`, `RandomTest`, `GenerateData` | 이미지명 추출과 초기 Product 데이터 생성 지원 |
| 저장 검증 | `ProductRepository`, `ProductTest.createProductMany()` | products table에 초기 상품을 반복 저장 |
| 목록 API | `findProductByOrderByIdDesc()`, `ProductService`, `ProductController` | 최신 id 순 조회를 `/product/list` GET으로 반환 |
| React 화면 | `Product.ts`, `ProductList.tsx` | JSON shape 선언, 목록 요청, state 저장, card 렌더링 |

## 입력 → 처리 → 결과

| 입력 | 처리 | 결과 |
|---|---|---|
| 이미지 폴더의 `.jpg` 파일명 | `File` 검사와 String 분리, `GenerateData.createProduct()` | 초기 Product 객체 생성 |
| Product 객체 목록 | `ProductRepository.save()` 반복 | MySQL products table에 seed 데이터 저장 |
| React의 `/product/list` GET | Controller → Service → Repository의 id 역순 조회 | Product JSON 목록 응답 |
| Product JSON 배열 | React `Product[]` state에 저장 후 `map()` | 이미지·상품명·id·가격 card 목록 표시 |

## 실제로 헷갈리기 쉬운 지점

- **`Category` enum과 category 테이블은 같은 것이 아니다.** 이날은 별도 Category Entity/table이 아니라 Java enum을 `Product.category`에 문자열로 저장하는 구조를 사용했다.
- **Entity와 React type은 같은 파일이 아니다.** Spring Entity가 DB·Validation·JSON 출발점을 담당하고, React interface는 응답을 화면 코드에서 다룰 shape를 선언한다.
- **초기 데이터 생성과 목록 API는 다른 단계다.** `ProductTest`·`GenerateData`는 DB를 채우고, Repository query·Service·Controller는 채워진 데이터를 읽어 반환한다.
- **React 화면만 만들어서는 상품이 보이지 않는다.** route, GET 요청, 공개 경로, backend 목록 API, DB seed가 모두 연결되어야 card가 렌더링된다.
- **OCI 소개가 상품 수업 전체를 대표하지 않는다.** raw에서 OCI는 가입 자료와 한 줄 개념 소개 범위이며, 실제 교시 대부분은 Product 구현이었다.

## 직접 수업과 후속 확장 경계

- 직접 구현: Category/Product, Validation·JPA table, 이미지 기반 seed, Product Repository·Service·Controller 목록, React Product type·목록 화면.
- 다음 날짜 직접 확장: 상품 삭제·등록, 이후 수정·상세·검색·페이징으로 Product 기능이 넓어진다.
- 후속 도메인: Cart와 Order는 Product를 참조하지만 이날 직접 구현하지 않았다.
- 후속 운영: Linux·AWS·CI/CD에서 서버 실행·배포·cloud를 다룬다. 이날의 OCI는 짧은 사전 안내이며 실제 OCI 배포 실습으로 확대하지 않는다. Passwordless도 후속 별도 인증 범위다.

## 관련 페이지

- [[concepts/product-domain-flow|상품 도메인 기능 흐름]]
- [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]
- [[comparisons/controller-service-repository|Controller vs Service vs Repository]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[concepts/shopping-cart-flow|장바구니 기능 흐름]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md`