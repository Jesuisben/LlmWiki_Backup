---
title: Controller vs Service vs Repository
created: 2026-07-02
updated: 2026-07-02
type: comparison
tags: [spring-boot, backend, java]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: high
---

# Controller vs Service vs Repository

## 비교 목적

Spring Boot 프로젝트에서는 기능이 커질수록 코드를 역할별로 나눠야 한다. 2026-04-14 장바구니 수업과 2026-04-22 상품 검색 수업에서는 Controller, Service, Repository가 함께 등장했다.

이 세 계층의 차이를 이해하면 “이 코드를 어느 파일에 써야 하지?”라는 혼란이 줄어든다.

## 한눈에 보기

| 계층 | 역할 | 수업 예시 |
|---|---|---|
| Controller | HTTP 요청을 받고 응답을 반환 | `/cart/insert`, `/product/list` 요청 처리 |
| Service | 업무 흐름과 검증 처리 | 장바구니에 상품 추가, 검색 조건 조립 |
| Repository | DB 접근 | `save`, `findById`, `findAll(spec, pageable)` |

## Controller

Controller는 프론트엔드나 브라우저에서 들어온 요청을 받는 입구다.

장바구니 수업에서는 다음과 같은 Controller가 등장했다.

```java
@PostMapping("/insert")
public ResponseEntity<String> addToCart(@RequestBody CartProductDto dto,
                                        Authentication authentication) {
    String email = authentication.getName();
    String message = cartService.addProductToCart(dto, email);
    return ResponseEntity.ok(message);
}
```

Controller가 하는 일은 다음 정도로 제한하는 것이 좋다.

- URL 매핑
- 요청 데이터 받기
- 로그인 사용자 정보 받기
- Service 호출
- 응답 반환

## Service

Service는 실제 업무 흐름을 처리한다.

장바구니 수업에서 `CartService`는 다음 일을 했다.

- 회원 조회
- 상품 조회
- 재고 확인
- 장바구니 조회 또는 생성
- 이미 담긴 상품인지 확인
- 수량 누적 또는 새 품목 저장

```java
@Transactional
public String addProductToCart(CartProductDto dto, String email) {
    Member member = memberRepository.findByEmail(email);
    Product product = productRepository.findById(dto.getProductId())
            .orElseThrow(() -> new RuntimeException("상품 없음"));

    if (product.getStock() < dto.getQuantity()) {
        throw new RuntimeException("재고 수량이 부족합니다.");
    }

    // 장바구니 조회/생성, 기존 상품 확인, 저장 흐름
    return "요청하신 상품이 장바구니에 추가되었습니다.";
}
```

상품 검색 수업에서는 Service가 `Specification`과 `Pageable`을 조립했다.

## Repository

Repository는 DB 접근 담당이다.

장바구니 수업에서는 다음 Repository들이 Service에 주입됐다.

```java
private final CartRepository cartRepository;
private final MemberRepository memberRepository;
private final ProductRepository productRepository;
```

상품 검색 수업에서는 Repository에 다음 메서드가 추가됐다.

```java
Page<Product> findAll(Specification<Product> spec, Pageable pageable);
```

Repository는 저장, 조회, 삭제처럼 DB와 직접 연결되는 작업을 담당한다.

## 언제 어디에 코드를 둘까

| 상황 | 적절한 위치 |
|---|---|
| URL을 추가한다 | Controller |
| 요청 파라미터를 받는다 | Controller |
| 로그인 사용자 이메일을 꺼낸다 | Controller 또는 인증 관련 계층 |
| 재고가 충분한지 검사한다 | Service |
| 기존 장바구니 품목을 찾고 수량을 누적한다 | Service |
| DB에서 상품을 찾는다 | Repository |
| 검색 조건을 조립한다 | Service |
| `findAll`, `save` 같은 DB 메서드를 호출한다 | Repository 또는 Service에서 Repository 호출 |

## 헷갈리기 쉬운 포인트

Controller가 DB를 직접 다루기 시작하면 처음에는 편해 보이지만, 기능이 커질수록 코드가 복잡해진다. 반대로 Service는 단순히 Repository를 한 번 호출하는 파일이 아니라, 업무 규칙과 검증을 담는 곳이다.

장바구니 예시에서 재고 확인이나 기존 상품 수량 누적은 단순 DB 조회가 아니라 업무 규칙이므로 Service에 있는 것이 자연스럽다.

## 관련 페이지

- [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]
- [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[summaries/2026-04-14-cart-service|2026-04-14 장바구니 Service와 DTO]]
- [[summaries/2026-04-22-product-repository-pageable-search|2026-04-22 ProductRepository와 Pageable 검색]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
