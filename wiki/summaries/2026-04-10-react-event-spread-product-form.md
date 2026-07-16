---
title: 2026-04-10 React 이벤트 객체와 전개 연산자
created: 2026-07-06
updated: 2026-07-16
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
status: growing
confidence: high
---

# 2026-04-10 React 이벤트 객체와 전개 연산자

## 한 줄 요약

React event object와 전개 연산자로 상품 등록 form state를 갱신하고 이미지를 Base64 문자열로 읽어 POST body로 보낸 뒤, Spring의 이미지 저장·Validation 응답과 React의 필드별 오류 표시를 연결하고 수정 화면을 시작한 날이다.

## 이전 수업과 오늘의 위치

- 전날 [[summaries/2026-04-09-product-delete-routing-jsx-table|2026-04-09]]에는 상품 삭제 왕복을 완성하고 `ProductInsertForm`의 state·입력 control·오류 영역을 만들었다.
- 오늘은 비어 있던 change/file/submit 함수를 채워 브라우저 입력이 request body가 되고, 서버 검증 결과가 다시 form에 표시되는 전체 등록 흐름을 연결했다.
- 다음 수업 [[summaries/2026-04-13-product-detail-useeffect-service|2026-04-13]]에서는 수정 화면의 GET/PUT 백엔드를 완성하고 상품 상세 조회 뒤 Cart 관계로 전환한다.

## 왜 이 흐름으로 배웠는가

여러 입력 control을 각각 별도 함수로 처리하기보다 event가 알려 주는 `name`과 `value`로 한 객체 state의 특정 필드만 바꾸면 같은 폼 구조를 등록과 수정에 재사용할 수 있다. 그 state를 서버로 보낸 뒤에는 Spring Validation의 필드 이름과 React 오류 state의 키가 맞아야 사용자가 어느 입력을 고쳐야 하는지 볼 수 있다.

## 실제 교시 흐름

1. **1교시 — event object와 spread:** `event.target`이 event를 발생시킨 요소라는 점을 확인하고, 배열 구조 분해 예제와 객체 전개를 거쳐 `ControlChange`에서 `name`·`value`를 추출했다. 기존 `product`를 펼친 뒤 계산된 property 이름을 덮어써 다른 필드가 사라지지 않게 했다.
2. **2교시 — 이미지 선택:** file input의 `files`를 검사하고 첫 파일을 `FileReader.readAsDataURL`로 읽었다. 읽기가 끝난 결과를 image 필드 state에 저장해 서버로 보낼 Base64 형식 문자열을 준비했다.
3. **3교시 — 등록 제출:** form 기본 동작을 막고 카테고리를 확인한 다음, 현재 `product` 객체를 JSON request body로 POST했다. 성공하면 상품·오류 state를 초기화하고 목록으로 이동하며, 실패하면 서버가 보낸 `errors`와 `message`를 기존 오류 state에 합쳤다.
4. **4교시 — `ProductService` 등록 처리:** Base64 문자열에서 실제 image 데이터를 분리·decode해 파일로 저장하고, 생성한 파일명을 Product에 반영한 뒤 등록일과 함께 Repository 저장으로 이어지게 했다.
5. **5교시 — `ProductController`와 Validation:** `@Valid`, `BindingResult`, `FieldError`를 이용해 필드별 오류 map을 만들고, 이미지 형식·파일 저장·기타 실패를 나누는 응답 구조를 작성했다. 원본 코드의 `insertProduct` 반환과 Controller의 `savedProduct` 판정은 함께 확인해야 할 지점으로 남아 있다.
6. **6교시 — 등록과 수정 비교·routing:** 입력 폼과 이미지 처리 방식은 공통이지만, 등록은 빈 폼·자동 id·INSERT이고 수정은 기존 값·기존 id·UPDATE라는 차이를 표로 정리했다. `/product/update/:id` route와 `ProductUpdateForm`을 연결했다.
7. **7교시 — 수정 화면 시작:** 등록 폼을 바탕으로 `useParams`의 id, 관리자 접근 확인, 기존 상품 GET, 같은 `ControlChange`·`FileSelect`, id가 들어간 PUT 요청과 수정 오류 state를 갖는 화면을 작성했다. 백엔드 GET/PUT 완성은 다음 수업으로 이어졌다.
8. **8교시 — 다음 범위 공지:** 상품 수정·상세, 장바구니, 주문으로 이어질 일정과 React 시험·상담·OCI 가입 일정을 확인했다. 이 공지는 후속 범위이며 오늘 구현 완료로 보지 않는다.

## 대표 artifact

- **`ProductInsertForm.tsx`:** 일반 입력 변경, 파일 선택, 제출, 성공 초기화, 서버 오류 표시가 하나의 form state를 중심으로 연결된다.
- **`ProductService.saveProductImage`·`insertProduct`:** React에서 보낸 image 문자열을 파일과 DB 파일명으로 분리해 저장한다.
- **`ProductController.insert`:** Product Validation 결과를 필드 오류 map으로 만들어 React가 다시 표시할 수 있게 한다.
- **`ProductUpdateForm.tsx`:** 등록 form의 공통 부분을 재사용하되 id·기존 데이터 조회·PUT이라는 수정 전용 부분을 추가한 시작본이다.

## 입력 → 처리 → 결과

| 단계 | 입력 | 처리 | 결과 |
|---|---|---|---|
| 일반 control 변경 | event가 발생한 input/select의 name·value | 기존 product를 펼치고 해당 name의 값만 교체 | 나머지 필드를 보존한 새 form state |
| 이미지 선택 | file input의 `files[0]` | FileReader가 Data URL 형식 문자열로 읽어 image state에 반영 | JSON body에 포함할 image 문자열 |
| 등록 제출 | product state | POST→Controller Validation→Service의 image file/DB 저장 | 성공 시 초기화·목록 이동, 실패 시 field/general 오류 표시 |
| 수정 화면 준비 | URL의 기존 상품 id | route 선택→GET으로 기존 상품 조회→state 반영 | 값이 채워진 수정 form; PUT 구현은 04-13에 백엔드와 완성 |

## 상품 등록과 수정의 공통점·차이

| 구분 | 등록 | 수정 |
|---|---|---|
| 공통 | 같은 입력 폼 구조, `ControlChange`, `FileSelect`, Validation 오류 표시 | 같은 입력 폼 구조, `ControlChange`, `FileSelect`, Validation 오류 표시 |
| 시작 state | 빈 입력값 | id로 조회한 기존 상품값 |
| id | 새 상품이므로 입력 폼에서 보내지 않음 | route의 기존 id를 사용 |
| 요청 목적 | 새 상품 등록 | 기존 상품 변경 |
| 오늘의 완성 범위 | React POST와 Spring 등록 처리까지 연결 | React 수정 화면과 GET/PUT 호출 구조를 시작; Spring GET/PUT은 04-13에 이어짐 |

## 헷갈린 점 / 질문

- **왜 `[name]`만 넣으면 안 되는가:** 새 객체에 해당 필드 하나만 남고 다른 상품 입력값이 사라진다. 기존 product를 먼저 펼친 뒤 마지막에 변경 필드를 덮어써야 한다.
- **전개 연산자는 깊은 복사인가:** 오늘 예제는 객체의 1단계 속성을 새 객체에 펼치는 얕은 복사다. 중첩 객체까지 독립 복사한다고 일반화하지 않는다.
- **file input도 `value`로 처리하는가:** 파일은 `files` 배열에서 첫 파일을 꺼내 FileReader로 읽는다. 일반 text/select의 name·value 처리와 입력 경로가 다르다.
- **Validation 오류는 어디서 만들어지는가:** Spring은 `BindingResult`의 필드 오류를 응답에 담고, React는 그 응답의 `errors`와 `message`를 오류 state에 합쳐 `isInvalid`와 feedback에 반영한다.
- **등록과 수정은 같은 기능인가:** 폼·event 처리는 비슷하지만 기존 id와 데이터 조회 여부, 요청 목적이 다르다.

## 직접 수업과 후속 확장 경계

- **직접 수업:** React event/spread·FileReader·등록 POST·오류 state, Spring 이미지 저장·Validation·등록 Controller, 수정 화면 시작이다.
- **후속 수업:** 수정 GET/PUT과 상세는 04-13, Cart 수량·삭제는 04-15 이후, Order는 04-16 이후, 검색/페이징은 04-21~04-22다.
- 전역 상태 관리, Linux·AWS·CI/CD·Passwordless는 오늘 원본의 상품 form 직접 수업 범위가 아니다.

## 관련 페이지

- [[concepts/react-form-state-event|React 폼 상태와 이벤트]]
- [[concepts/product-domain-flow|상품 도메인 기능 흐름]]
- [[concepts/axios-interceptor-error-handling|Axios interceptor와 API 오류 처리]]
- [[comparisons/props-vs-state|props vs state]]
- [[concepts/react-useeffect-data-fetching|React useEffect와 데이터 요청]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md`
