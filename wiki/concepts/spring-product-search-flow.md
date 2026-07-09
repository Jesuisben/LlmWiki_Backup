---
title: Spring 상품 검색 흐름
created: 2026-07-02
updated: 2026-07-09
type: concept
tags: [spring-boot, backend, frontend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: high
---
# Spring 상품 검색 흐름

## 수업에서 배운 전체 흐름

### 1. Repository에 검색 + 페이징 메서드 추가

`ProductRepository`에는 다음 메서드가 추가됐다.

```java
Page<Product> findAll(Specification<Product> spec, Pageable pageable);
```

이 메서드는 검색 조건 `spec`과 페이징 조건 `pageable`을 함께 사용해 상품 목록을 조회한다.

- `Specification`: 조건을 누적해서 만든 검색 필터
- `Pageable`: 몇 번째 페이지를, 몇 개씩, 어떤 정렬로 가져올지 담은 객체
- `Page<Product>`: 페이징 결과와 전체 개수/페이지 수 같은 정보를 함께 담은 결과

### 2. Service에서 검색 조건 조립

`ProductService`의 `listProducts` 메서드는 프론트에서 넘어온 검색 DTO와 페이지 정보를 받아 조건을 만든다.

```java
public Page<Product> listProducts(SearchDto searchDto, int pageNumber, int pageSize) {
    Specification<Product> spec = Specification.unrestricted();

    String searchDateType = searchDto.getSearchDateType();
    if (searchDateType != null) {
        spec = spec.and(ProductSpecification.hasDateRange(searchDateType));
    }

    Category category = searchDto.getCategory();
    if (category != null) {
        Category categoryEnum = Category.valueOf(category.toString().toUpperCase());
        spec = spec.and(ProductSpecification.hasCategory(categoryEnum));
    }

    String searchMode = searchDto.getSearchMode();
    String searchKeyword = searchDto.getSearchKeyword();

    if (searchMode != null && searchKeyword != null) {
        if ("name".equals(searchMode)) {
            spec = spec.and(ProductSpecification.hasNameLike(searchKeyword));
        } else if ("description".equals(searchMode)) {
            spec = spec.and(ProductSpecification.hasDescriptionLike(searchKeyword));
        }
    }

    Sort sort = Sort.by(Sort.Order.desc("id"));
    Pageable pageable = PageRequest.of(pageNumber, pageSize, sort);

    return this.productRepository.findAll(spec, pageable);
}
```

이 코드의 핵심은 `spec = spec.and(...)` 형태다. 검색 조건이 있으면 기존 조건에 하나씩 덧붙인다.

예를 들면 다음과 같은 조건 조합이 가능하다.

- 기간 검색만 적용
- 카테고리만 적용
- 상품명 검색만 적용
- 기간 + 카테고리 + 상품명 검색 모두 적용

### 3. Controller에서 프론트엔드 요청 파라미터 받기

Controller는 React 상품 목록 화면에서 넘어오는 파라미터를 받는다.

```java
@GetMapping("/list")
public ResponseEntity<Page<Product>> listProducts(
        @RequestParam(defaultValue = "0") int pageNumber,
        @RequestParam(defaultValue = "6") int pageSize,
        @RequestParam(defaultValue = "all") String searchDateType,
        @RequestParam(defaultValue = "") Category category,
        @RequestParam(defaultValue = "") String searchMode,
        @RequestParam(defaultValue = "") String searchKeyword
) {
    SearchDto searchDto = new SearchDto(searchDateType, category, searchMode, searchKeyword);
    Page<Product> productPage = productService.listProducts(searchDto, pageNumber, pageSize);
    return ResponseEntity.ok(productPage);
}
```

원본 노트에서 중요한 포인트는 **프론트에서 요구하는 파라미터명과 Controller의 변수명을 맞춰야 한다**는 점이다.

예를 들어 React 쪽 `ProductList.tsx`에서 보내는 URL parameter와 Spring Controller의 `@RequestParam` 이름이 대응되어야 한다.

## Java 기본 자료형/참조 자료형과 연결되는 지점

이날 수업에는 Java 타입 비교도 함께 등장했다.

- 기본 자료형: `int`, `double`, `boolean`, `char`
- 참조 자료형: 클래스, 배열, 인터페이스

기본 자료형은 `==`으로 비교할 수 있지만, 문자열 같은 참조 자료형은 보통 `equals()`를 사용한다.

```java
"name".equals(searchMode)
```

이 코드가 중요한 이유는 `searchMode.equals("name")`보다 안전하기 때문이다. `searchMode`가 `null`이면 `searchMode.equals(...)`는 오류가 날 수 있지만, 문자열 리터럴인 `"name"`은 `null`이 아니므로 `"name".equals(searchMode)`가 더 안전하다.

## MySQL 테스트 시나리오와 연결

검색 기능은 백엔드 코드만 작성해서 끝나는 것이 아니라, DB 데이터가 검색 조건에 맞게 준비되어 있어야 테스트할 수 있다.

수업에서는 상품 입고일을 조정한 뒤 다음 조건들을 테스트했다.

- 기간 선택: 1일
- 기간 선택: 1주일
- 기간 선택: 1개월
- 특정 카테고리 검색: `beverage`, `cake`
- 카테고리 + 상품명 다중 조건
- 카테고리 + 설명 다중 조건

예시 SQL은 다음과 같다.

```sql
select * from products
WHERE inputdate >= NOW() - INTERVAL 1 WEEK
ORDER BY product_id DESC;
```

```sql
select * from products
WHERE name LIKE @myname
AND category = upper(@category)
ORDER BY product_id DESC;
```

이 테스트 시나리오는 Spring의 `Specification` 조건이 실제 DB 조건과 맞게 동작하는지 확인하기 위한 기준이 된다.

## 관련 페이지

- [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]
- [[concepts/pagination-search|페이징과 검색]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
