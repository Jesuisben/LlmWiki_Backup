---
title: 2026-04-22 Specification·Pageable 상품 검색 완성
created: 2026-07-06
updated: 2026-07-16
type: summary
tags: [spring-boot, react, typescript, backend, frontend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: high
---

# 2026-04-22 Specification·Pageable 상품 검색 완성

## 한 줄 요약

전날 React가 보내기 시작한 page·검색 parameter를 Controller의 `SearchDto`로 묶고, Service에서 여러 `Specification`을 조립한 뒤 정렬·`Pageable`과 함께 `ProductRepository`에 넘겨 Page 응답으로 돌려주며 상품 페이징·검색의 백엔드 경로를 완성했다.

## 이전 수업과 오늘의 위치

- 이전 [[summaries/2026-04-21-product-pagination-search-react|2026-04-21]]에는 page 요청·Page 응답 왕복을 먼저 완성하고, 검색 form state와 GET parameter, `SearchDto`, `ProductSpecification`의 개별 조건을 준비했다.
- 오늘은 그 준비물을 Repository→Service→Controller 순으로 연결해 검색 parameter가 실제 조건부 DB 조회에 도달하게 했다.
- 다음 커리큘럼은 [[summaries/2026-04-22-linux-install-ssh-cli|2026-04-22 Linux 설치와 SSH]]로 전환한다. 같은 날짜에 Linux 수업이 시작됐지만 FrontEnd_BackEnd 검색 구현과는 별도 과목·원본이다.

## 왜 이 순서로 배웠는가

검색 화면에서 네 값을 보내더라도 Repository가 조건과 page 정보를 함께 처리하지 않으면 결과는 달라지지 않는다. 그래서 Repository의 최종 조회 모양을 먼저 선언하고, Service가 선택된 조건만 이어 붙이며 sort와 page를 만든 다음, Controller가 React parameter를 정확히 받아 Service를 호출하는 순서로 닫힌 왕복을 만들었다.

## 실제 교시 흐름

1. **1교시 — ProductRepository의 최종 조회 입구:** `Specification<Product>`와 `Pageable`을 함께 받는 `findAll`을 추가했다. 검색 WHERE 조건은 Specification에, page 크기·번호·정렬은 Pageable에 담겨 한 Repository 호출로 전달된다.
2. **2교시 전반 — Java type 비교 보충:** 기본 자료형은 `==`, 참조 자료형은 내용 비교 메서드를 사용하는 설명을 거쳐, `searchMode` 문자열을 `"name".equals(searchMode)`로 비교하는 이유를 확인했다. 이 복습은 검색 분기에서 null에 안전한 비교를 하기 위한 준비다.
3. **2교시 — ProductService 조건 조립:** 빈 Specification에서 시작해 기간 값이 있으면 날짜 범위 조건, 카테고리가 있으면 카테고리 조건을 `and`로 추가했다. 검색 mode와 keyword가 모두 있을 때 mode가 name이면 상품명 포함 조건, description이면 설명 포함 조건을 붙였다.
4. **2교시 — 정렬과 Pageable:** 상품 id 내림차순 sort를 만들고 `pageNumber`, `pageSize`, sort를 `PageRequest`에 넣었다. 조립된 Specification과 Pageable을 Repository의 `findAll`에 함께 넘겨 `Page<Product>`를 반환했다.
5. **2교시 — ProductController parameter 연결:** `/product/list`가 page 번호·크기와 기간·카테고리·mode·keyword를 받았다. 네 검색값으로 `SearchDto`를 만들고 Service를 호출한 뒤 Page 결과를 응답했다. React가 전날 사용한 parameter 이름과 Controller 변수 이름을 맞추는 것이 연결 조건이었다.
6. **2교시 후반 — 검색용 날짜 데이터 준비:** MySQL에서 기존 Product 입고일을 초기화한 뒤 행 순서에 따라 날짜 차이를 두도록 갱신하고 다시 조회했다. 이는 1일·1주·1개월 같은 기간 조건이 서로 다른 결과를 내도록 만드는 테스트 fixture다.
7. **3교시 — MySQL 검색 시나리오:** 기간 1일·1주·1개월, 특정 카테고리, 카테고리와 상품명 포함, 카테고리와 설명 포함을 SQL로 각각 확인했다. 다중 조건은 `AND`로 결합해 Service의 Specification 조립과 같은 의도를 DB에서 비교했다.
8. **4~8교시:** FrontEnd_BackEnd 원본에 새 수업 내용이 기록되어 있지 않다. 빈 교시를 기능 구현으로 추정하지 않는다.

## 대표 artifact

| 계층 | 대표 artifact | 오늘 맡은 역할 |
|---|---|---|
| React 연결점 | 전날 ProductList GET parameters | page·기간·카테고리·mode·keyword를 같은 목록 endpoint로 전송 |
| Controller | `ProductController.listProducts` | request parameter를 받고 `SearchDto`를 만든 뒤 Service에 전달, Page 응답 반환 |
| DTO | `SearchDto` | 네 검색 조건을 한 객체로 묶어 Service에 전달 |
| 조건 생성 | `ProductSpecification` | 날짜·카테고리·상품명·설명 Predicate 제공 |
| Service | `ProductService.listProducts` | 선택된 조건을 `and`로 조립하고 id 내림차순 `Pageable` 생성 |
| Repository | `ProductRepository.findAll` | Specification과 Pageable을 적용한 Product Page 조회 |
| 검증 | MySQL 날짜 갱신·검색 SQL | 기간·카테고리·keyword·다중 조건 결과 대조 |

## 입력 → 처리 → 결과

| 입력 | 처리 | 결과 |
|---|---|---|
| React의 page 번호·크기와 네 검색 parameter | Controller가 기본값을 적용하고 `SearchDto` 생성 | Service가 사용할 검색 조건과 page 정보 확보 |
| `SearchDto`와 page 정보 | Service가 필요한 Specification만 `and`로 결합→id 내림차순 sort→`PageRequest` 생성 | Repository에 동적 WHERE 조건과 page/sort가 함께 전달 |
| Specification과 Pageable | ProductRepository의 `findAll` 조회 | 조건에 맞는 `Page<Product>` 반환 |
| Page 응답 | Controller가 OK body로 반환→전날 ProductList 처리 경로 | React는 `content`를 카드로, metadata를 Paging 상태로 표시 |
| 기간·카테고리·포함 문자열 | MySQL에서 같은 의도의 WHERE·LIKE·AND 조건 실행 | 애플리케이션 검색 결과를 비교할 기준 마련 |

## 04-21 프론트 준비와 04-22 백엔드 완성의 경계

- 04-21: SearchCondition·FieldSearch가 입력을 state에 저장하고 ProductList가 검색 parameter를 전송했다. SearchDto와 개별 Specification도 작성했지만 검색 조회 계층은 아직 연결되지 않았다.
- 04-22: Controller가 검색 parameter를 받고, Service가 조건을 조립하고, Repository가 Specification과 Pageable로 조회했다.
- 따라서 page 조회는 04-21에 이미 단순 Pageable 왕복이 연결됐고, **검색 조건이 포함된 page 조회**는 04-22에 완성됐다.

## MySQL·API 테스트에서 확인한 범위

- 원본은 MySQL에서 입고 날짜를 분산시킨 뒤 기간별 조회 결과를 비교했다.
- 카테고리 단독과 카테고리+상품명, 카테고리+설명 조합을 확인했다.
- SQL의 설명 한 곳은 “설명에 상큼”이라고 적었지만 실제 변수 값은 다른 문자열이므로, 특정 결과를 단정하지 않고 설명 포함 다중 조건을 시험한 사실만 보존한다.
- 원본에는 별도 API client 응답 전문이나 특정 결과 건수 확정이 없다. Controller console 출력 항목은 있지만 실제 출력값을 만들어 적지 않는다.

## 헷갈린 점 / 질문

- **Specification과 Pageable:** Specification은 검색 조건, Pageable은 page·size·sort다. 둘을 함께 넘기지만 같은 책임의 객체가 아니다.
- **빈 조건 처리:** 조건 값이 없으면 해당 Specification을 붙이지 않는다. `category`의 빈 기본값이 enum parameter로 어떻게 변환되는지는 실행환경에 따라 확인이 필요한 지점이므로 원본 이상의 성공을 단정하지 않는다.
- **문자열 비교:** `"name".equals(searchMode)`는 searchMode가 null이어도 호출 자체가 안전하다. 참조 자료형 전체를 항상 equals 하나로 비교한다고 일반화하기보다 문자열 분기 맥락으로 이해한다.
- **다중 조건:** 카테고리와 name/description 조건은 `and`로 함께 적용된다. 여러 선택지가 있다는 사실과 여러 조건이 실제 결합됐다는 사실을 구분해야 한다.
- **Repository method:** Spring Data JPA 기반 Repository가 Specification executor 기능을 이미 갖춘 구성인지가 전제다. 날짜 원본에는 interface 전체 상속 선언보다 추가한 method가 중심이다.

## 직접 수업과 후속 확장 경계

- 직접 구현: ProductRepository의 Specification+Pageable 조회, Service 조건 조립·sort/page 생성, Controller parameter·DTO·Page 응답, MySQL 기간·카테고리·다중 조건 테스트.
- 전날 직접 구현: React 검색 form/state/request parameter와 개별 Specification 준비.
- 다음 과목: Linux에서 VM·SSH·CLI와 서버 운영 기반을 배우고, 이후 AWS·CI/CD에서 배포로 확장한다. Passwordless와 중간 프로젝트 인증 적용은 이 검색 기능과 별도 후속 범위다.

## 관련 페이지

- [[concepts/spring-data-jpa-specification-pageable|Spring Data JPA Specification과 Pageable]]
- [[concepts/spring-product-search-flow|Spring 상품 검색 흐름]]
- [[concepts/pagination-search|페이징과 검색]]
- [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]
- [[comparisons/controller-service-repository|Controller vs Service vs Repository]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
