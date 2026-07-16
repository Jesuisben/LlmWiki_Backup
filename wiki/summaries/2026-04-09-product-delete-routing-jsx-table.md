---
title: 2026-04-09 상품 삭제, 라우팅, JSX와 표
created: 2026-07-06
updated: 2026-07-16
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/라우터 설명 그림.png
status: growing
confidence: high
---

# 2026-04-09 상품 삭제, 라우팅, JSX와 표

## 한 줄 요약

JWT claim 설정을 짧게 보정한 뒤, 관리자 상품 목록의 삭제 클릭을 React 상태·Spring Service/Controller·DB와 이미지 파일 삭제까지 연결하고 상품 등록 라우트와 `ProductInsertForm` 작성으로 넘어간 날이다.

## 이전 수업과 오늘의 위치

- 전날 [[summaries/2026-04-08-product-domain-oci|2026-04-08]]에는 Category/Product Entity, seed 데이터, 상품 목록 API와 React card 목록을 만들었다.
- 오늘은 그 목록을 관리 기능으로 확장했다. 먼저 삭제 요청의 프론트·백엔드 처리를 완성하고, 오후에는 다음 기능인 상품 등록 화면의 경로와 폼 뼈대를 만들었다.
- 다음 수업 [[summaries/2026-04-10-react-event-spread-product-form|2026-04-10]]에서는 빈 `ProductInsertForm`의 change/file/submit 동작을 구현해 실제 등록 요청과 Validation 오류 표시까지 연결한다.

## 왜 이 흐름으로 배웠는가

상품 목록에 버튼만 붙이면 삭제 기능이 완성되는 것이 아니다. 카드 클릭은 상세 이동, 수정 버튼은 수정 라우트, 삭제 버튼은 삭제 요청이라는 서로 다른 동작을 분리해야 하고, 삭제 성공 뒤 화면 배열·DB 행·운영체제 이미지 파일도 같은 결과를 반영해야 한다. 이 왕복을 확인한 뒤 같은 관리자 기능인 등록 화면으로 진행했다.

## 실제 교시 흐름

1. **1교시 — JWT claim 보정과 삭제 화면 진입:** `JwtTokenProvider`에서 전체 claims를 덮어쓰는 방식 대신 role claim 하나를 추가하는 방식으로 수정했다. `AppRouters.tsx`에서는 `ProductList`에 `user`를 전달해 관리자용 기능을 판단할 기반을 마련했다.
2. **2교시 — ProductList 관리자 버튼:** 일반 HTML 표의 `rowSpan`·`colSpan` 의미와 JSX의 `{}`·객체용 `{{}}` 표기를 보충한 뒤, 실제 Product card 안의 표에 수정·삭제 버튼 영역을 배치했다. 관리자일 때만 등록·수정·삭제 버튼을 보이게 하고, 수정·삭제 클릭에는 `event.stopPropagation()`을 두었다.
3. **3~4교시 — `ProductService.deleteProduct`:** 상품 id로 존재 여부를 확인하고, 상품 이미지 이름이 있으면 설정된 이미지 경로에서 파일 삭제를 시도한 뒤 Repository에서 상품을 삭제하도록 구성했다.
4. **5교시 — `ProductController.delete`:** 경로의 id를 받아 Service 결과에 따라 성공·상품 부재·무결성 위반·기타 오류 응답을 나누었다. 실제 테스트에서는 웹 화면과 DB에서는 삭제됐지만 이미지 파일이 남았고, 출력된 경로가 `images`와 파일명 사이 구분자 없이 이어진 것을 확인해 이미지 위치 설정을 보정했다.
5. **6~8교시 — 상품 등록 시작:** `MenuItems.tsx`와 `AppRouters`에 상품 등록 이동 경로를 연결하고 `ProductInsertForm.tsx`를 만들었다. 상품명·가격·카테고리·재고·이미지·설명 state와 필드별/general 오류 state, Bootstrap form과 feedback 영역을 먼저 구성했으며 `ControlChange`와 `FileSelect`의 구현은 다음 날로 남겼다.

## 대표 artifact

- **`ProductList.tsx`:** 관리자 버튼, 삭제 확인, 버블링 방지, 삭제 성공 후 `filter`를 이용한 목록 state 갱신을 한곳에서 연결했다.
- **`ProductService.deleteProduct` + `ProductController.delete`:** 화면의 DELETE 요청을 상품 조회→이미지 파일 처리→DB 삭제로 이어 주었다.
- **`ProductInsertForm.tsx`:** 다음 날 이벤트와 요청 로직을 붙일 상품 등록 폼의 state·오류 표시·입력 control 구조를 만들었다.

라우터 설명 그림은 Router를 관객이 선택한 영화에 맞는 상영관으로 안내하는 역할에 비유한다. 오늘의 `/product/insert`와 수정 경로도 화면을 선택하는 React Router 주소이며, 상품을 삭제하는 Spring API 주소와 역할이 다르다.

## 입력 → 처리 → 결과

| 기능 | 입력 | 처리 | 결과 |
|---|---|---|---|
| 상품 삭제 | 관리자가 상품 card의 삭제 버튼 클릭·확인 | 버블링 중단→DELETE 요청→Controller→Service에서 상품/이미지/DB 처리 | 성공 알림 후 삭제한 id를 제외해 상품 목록 state 갱신 |
| 상품 수정 이동 | 관리자가 수정 버튼 클릭 | 버블링 중단 후 상품 id가 포함된 화면 경로로 이동 | 다음 수정 폼 화면 선택 |
| 상품 등록 준비 | 메뉴·등록 Link 클릭 | Router가 `ProductInsertForm`을 선택하고 초기 state로 form 렌더링 | 빈 상품 입력 폼과 오류 표시 영역 제공 |

## 일반 HTML/JSX 보충과 Product 기능의 구분

- `rowSpan`·`colSpan`은 표의 행·열 병합을 설명한 일반 HTML/JSX 보충이다. 실제 Product 기능에서는 card 안 표의 버튼 셀 배치에 `rowSpan`이 쓰였다.
- JSX의 `{}`는 JavaScript 표현식을 넣는 문법이고 `{{}}`는 그 표현식 안에 객체 literal을 넣는 모습이다. 이것 자체가 삭제 업무 로직은 아니다.
- 삭제·수정 버튼에서 `stopPropagation()`을 쓴 이유는 부모 card의 상세 이동 클릭과 관리자 버튼 동작이 동시에 실행되는 것을 막기 위해서다.

## 헷갈린 점 / 질문

- **버튼 클릭이 왜 상세 페이지까지 이동하는가:** 클릭 event가 부모 card로 전파되기 때문이다. 삭제·수정 버튼의 목적은 card 클릭과 다르므로 전파를 중단한다.
- **삭제 성공인데 이미지가 왜 남는가:** React 목록 갱신과 DB 행 삭제가 성공해도 파일 경로가 잘못 결합되면 운영체제 파일 삭제는 실패할 수 있다. 세 저장 상태를 따로 확인해야 한다.
- **화면에서 관리자 버튼을 숨기면 권한 검사가 끝나는가:** 오늘 원본은 role에 따른 화면 표시를 구현했다. 화면 숨김은 UI 제어이며 백엔드 권한 검사의 전체 완성으로 확대해 해석하지 않는다.
- **등록 폼이 오늘 완성됐는가:** 오늘은 route·state·입력 양식과 오류 영역을 만든 단계다. 실제 입력 변경, 파일 변환, POST와 오류 반영은 04-10 범위다.

## 직접 수업과 후속 확장 경계

- **직접 수업:** JWT claim 한 줄 보정, ProductList 관리자 UI, 삭제 요청·Service·Controller·파일 경로 점검, 상품 등록 route와 form 시작이다.
- **후속 수업:** 등록/수정 요청 완성은 04-10~04-13, Cart 수량·삭제는 04-15 이후, Order는 04-16 이후, 검색/페이징은 04-21~04-22에 진행된다.
- Linux·AWS·CI/CD·Passwordless는 이 Product 기능을 서버 운영·배포·다른 인증 방식으로 확장하는 뒤 과목이며 오늘 직접 구현 범위가 아니다.

## 관련 페이지

- [[concepts/product-domain-flow|상품 도메인 기능 흐름]]
- [[concepts/react-form-state-event|React 폼 상태와 이벤트]]
- [[comparisons/react-router-vs-spring-api-url|React Router 주소 vs Spring API 주소]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[entities/spring-boot|Spring Boot]]
- [[entities/react|React]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/라우터 설명 그림.png` — Router의 화면 안내 비유만 보조 확인
