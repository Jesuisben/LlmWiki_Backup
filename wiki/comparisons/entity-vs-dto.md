---
title: Entity vs DTO
created: 2026-07-02
updated: 2026-07-09
type: comparison
tags: [spring-boot, backend, java]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: high
---

# Entity vs DTO

## 비교 목적

Spring Boot 수업에서 Entity와 DTO는 계속 같이 등장한다. 둘 다 Java 클래스라서 처음에는 비슷해 보이지만, 목적이 다르다.

- Entity는 DB와 가까운 객체다.
- DTO는 요청/응답 데이터를 옮기기 위한 객체다.

이 차이를 이해해야 Controller, Service, Repository의 역할도 함께 정리된다.

## 한눈에 보기

| 항목 | Entity | DTO |
|---|---|---|
| 주된 역할 | DB 테이블과 연결되는 도메인 객체 | 계층 간 데이터 전달 |
| 위치 | 보통 `entity` 패키지 | 보통 `dto`, `types` 등 전달 모델 위치 |
| DB와의 관계 | 강함 | 약함 또는 없음 |
| 외부 요청/응답 노출 | 직접 노출을 피하는 경우가 많음 | 요청/응답에 맞게 설계 |
| 수업 예시 | `Product`, `Cart`, `CartProduct`, `Member` | `CartProductDto`, `SearchDto`, `LoginResponse` |

## Entity

Entity는 DB 테이블과 가까운 Java 객체다. 예를 들어 장바구니 수업에서는 다음 Entity들이 등장했다.

- `Cart`
- `CartProduct`
- `Member`
- `Product`

Service 코드에서는 Repository를 통해 Entity를 조회하고 저장했다.

```java
Member member = memberRepository.findByEmail(email);

Product product = productRepository.findById(dto.getProductId())
        .orElseThrow(() -> new RuntimeException("상품 없음"));
```

여기서 `Member`와 `Product`는 DB에 저장된 회원/상품 데이터를 표현하는 객체다.

## DTO

DTO(Data Transfer Object)는 데이터를 전달하기 위한 객체다. DB 테이블 구조를 그대로 반영하기보다, 특정 요청이나 응답에 필요한 데이터만 담는다.

장바구니 수업에서는 `CartProductDto`가 등장했다.

```java
public String addProductToCart(CartProductDto dto, String email)
```

`CartProductDto`는 프론트엔드에서 “어떤 상품을 몇 개 담을지” 같은 요청 데이터를 전달하는 역할을 한다.

상품 검색 수업에서는 `SearchDto`가 등장했다.

```java
SearchDto searchDto = new SearchDto(searchDateType, category, searchMode, searchKeyword);
```

이 DTO는 검색 조건을 하나로 묶어서 Service에 전달한다.

로그인 수업에서는 React 쪽에서 `LoginResponse` 같은 타입도 등장했다.

```typescript
export interface LoginResponse extends User {
    accessToken: string;
}
```

이것도 서버 응답 데이터를 프론트엔드에서 다루기 위한 전달 모델로 볼 수 있다.

## 언제 무엇을 쓰는가

| 상황 | 적절한 선택 |
|---|---|
| DB에 저장되는 회원/상품/장바구니를 표현 | Entity |
| 프론트에서 상품 id와 수량만 받아오기 | DTO |
| 검색 조건 여러 개를 하나로 묶기 | DTO |
| Repository로 DB 조회/저장하기 | Entity |
| API 응답에서 필요한 필드만 보내기 | DTO |

## 헷갈리기 쉬운 포인트

### DTO와 Entity가 필드가 비슷할 수 있다

둘 다 `id`, `name`, `quantity` 같은 필드를 가질 수 있다. 하지만 목적이 다르다.

- Entity는 DB의 실제 구조와 생명주기에 가깝다.
- DTO는 화면/API/요청/응답에 맞춘 전달용 모양이다.

### Entity를 그대로 응답하면 안 되는 경우가 있다

Entity를 그대로 외부에 보내면 DB 구조가 노출되거나, 필요 없는 필드까지 응답될 수 있다. 그래서 실무에서는 DTO로 변환해서 보내는 경우가 많다.

### DTO는 저장소가 아니다

DTO는 데이터를 잠깐 담아 옮기는 객체다. DB 저장과 조회는 Repository와 Entity의 영역이다.

## 관련 페이지

- [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]
- [[comparisons/controller-service-repository|Controller vs Service vs Repository]]
- [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]
- [[summaries/2026-04-06-login-jwt-session-cookie|2026-04-06 로그인, JWT, 세션과 쿠키]]
- [[summaries/2026-04-14-cart-service|2026-04-14 장바구니 Service와 DTO]]
- [[summaries/2026-04-22-product-repository-pageable-search|2026-04-22 ProductRepository와 Pageable 검색]]

## 4과목 현재 raw MD 기준 재검증 메모

- 2026-07-09에 `raw/KoreaICT/4. FrontEnd_BackEnd` 날짜별 MD 18개와 `FrontEnd_BackEnd 총정리.md`를 기준으로 다시 대조했다.
- 이 페이지는 단순 일반론이 아니라 Spring Boot Controller/Service/Repository, React Router/page/state, JWT 인증, Product/Cart/Order/Pageable 기능 흐름과 연결해 읽어야 한다.
- 핵심 복습 순서는 환경 세팅 → REST API/JSON/CORS → Member/JWT → Product → Cart → Order → Pageable/검색이다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
