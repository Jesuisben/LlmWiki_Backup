---
title: React 폼 상태와 이벤트
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [react, typescript, frontend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf
status: growing
confidence: high
---

# React 폼 상태와 이벤트

## 정의

React의 controlled form은 input/select의 현재 값을 state가 보유하고, `onChange` event가 state를 갱신하며, submit·click handler가 그 state로 API 요청을 만드는 방식이다. 이 수업에서는 회원가입, 상품 등록·수정, 상품 상세·Cart 수량 입력에서 같은 원리가 반복되었다.

## 왜 중요한가

브라우저 입력값, React state, 요청 JSON, Spring이 검증한 Java 객체가 서로 어긋나면 화면에는 값이 보여도 저장이 실패하거나 오류가 잘못 표시된다. 특히 text/select input과 file input, 빈 등록 form과 기존값 수정 form, React 오류 표시와 Spring Validation은 처리 경로가 다르므로 분리해서 봐야 한다.

## 처음 등장한 날짜와 이후 확장

| 날짜 | form/event 확장 | 대표 artifact |
|---|---|---|
| [[summaries/2026-04-03-spring-member-seed-react-comments|04-03]] | 회원가입 입력·submit 기본 동작 방지·필드 오류 표시 | `SignupPage`, `isInvalid`, `Form.Control.Feedback` |
| [[summaries/2026-04-10-react-event-spread-product-form|04-10]] | name/value 공통 handler, spread, file input, 등록 POST, 수정 form 시작 | `ControlChange`, `FileSelect`, `ProductInsertForm` |
| [[summaries/2026-04-13-product-detail-useeffect-service|04-13]] | 수정 기존값·PUT, 상세 quantity input과 Cart POST | `ProductUpdateForm`, `QuantityChange`, `addToCart` |
| [[summaries/2026-04-15-cart-list-selection-typescript|04-15]] | number input 문자열을 정수로 바꾸고 수량 PATCH | `changeQuantity`, Cart quantity control |

## controlled input의 공통 흐름

1. state가 현재 form 값을 보유하고 input의 `value`에 연결된다.
2. `onChange`가 event 객체를 handler에 전달한다.
3. handler가 `event.target`에서 필요한 값을 읽는다.
4. 기존 객체/배열의 다른 필드는 보존하고 바뀐 필드만 새 값으로 교체한다.
5. submit 또는 button handler가 현재 state를 body·parameter로 만들어 API를 호출한다.
6. 성공하면 초기화·화면 이동·목록 갱신을 하고, 실패하면 오류 state를 갱신한다.

## text/select input: target, name/value, spread

`ProductInsertForm`과 `ProductUpdateForm`의 `ControlChange`는 input·textarea·select의 change event를 함께 받았다. `event.target`에서 `name`과 `value`를 꺼내고, 기존 product를 spread한 뒤 `[name]`에 새 value를 덮어썼다.

- `name`은 Product의 어느 field를 바꿀지 고르는 key다.
- `value`는 브라우저 control에서 읽은 현재 문자열 값이다.
- 기존 객체를 먼저 펼치지 않고 `[name]`만 가진 새 객체를 만들면 다른 입력값이 사라진다.
- 이 spread는 1단계 속성을 복사하는 얕은 복사이며 중첩 객체 전체의 깊은 복사를 뜻하지 않는다.

## SignupPage: 입력과 서버 오류 표시

04-03의 회원가입은 name·email·password·address 입력을 각각 state에 연결하고 submit에서 기본 브라우저 제출을 막은 뒤 JSON body로 POST했다. Spring이 반환한 필드 오류 Map은 React errors state의 같은 key에 들어가 `isInvalid`와 feedback 문구를 켰다.

여기서 React는 오류를 **표시**하지만 가입 허용 여부를 최종 결정하지 않는다. Spring의 `@Valid`·`BindingResult`, 이메일 중복 조회, Service 저장 규칙이 서버 판단을 수행했다.

## ProductInsertForm: 일반 입력과 file input

상품명·가격·카테고리·재고·설명은 name/value 공통 handler를 사용했다. image file은 같은 방식으로 처리하지 않았다.

- file input은 `event.target.files`를 확인하고 첫 파일을 선택했다.
- `FileReader.readAsDataURL`로 읽은 결과를 image field state에 넣었다.
- 등록 submit은 product state를 JSON body로 보냈고 Spring Service가 Data URL에서 image 데이터를 분리해 파일과 DB 파일명을 저장했다.
- 성공하면 product/errors state를 초기화하고 목록으로 이동했으며, 실패하면 서버의 필드 오류와 일반 message를 오류 state에 합쳤다.

## ProductUpdateForm: 등록 form과의 공통점·차이

| 구분 | 등록 | 수정 |
|---|---|---|
| 시작 값 | 빈 product state | route id로 GET한 기존 product state |
| 공통 처리 | `ControlChange`, `FileSelect`, 오류 표시 | `ControlChange`, `FileSelect`, 오류 표시 |
| 요청 목적 | 새 Product POST | 기존 id의 Product PUT |
| image control | 새 파일 선택 | 기존 image 정보와 새 file input을 분리 |
| 완료 날짜 | 04-10 등록 왕복 | 04-10 화면 시작, 04-13 GET/PUT 완성 |

브라우저 보안상 file input에 기존 파일 경로를 기본값으로 넣지 못한다. Product state가 기존 image 이름을 알고 있는 것과 file control에 값이 보이는 것은 다른 문제다.

## Cart 수량 입력

상품 상세에서는 quantity change event의 문자열 값을 정수로 바꿔 Cart 추가 body에 넣었다. CartList에서는 number input의 문자열을 `parseInt`한 뒤 CartProduct id·quantity를 PATCH 요청으로 보냈고, 성공하면 해당 품목의 local quantity와 합계를 갱신했다.

Cart의 checkbox `checked`와 quantity는 모두 form control처럼 보이지만 책임이 다르다. `checked`는 주문 대상을 고르는 frontend state였고 DB에 저장하지 않았다. quantity는 CartProduct의 서버 상태를 바꾸는 API와 연결됐다.

## 대표 입력 → 처리 → 결과

| 실제 form | 입력 | 처리 | 결과 |
|---|---|---|---|
| `SignupPage` | 회원 text input | target.value→state→POST→Spring Validation/중복 확인 | 성공 응답 또는 필드 오류 표시 |
| `ProductInsertForm` 일반 control | name/value | 기존 product spread→해당 field 교체 | 등록 JSON body의 최신 값 |
| Product file input | `files[0]` | FileReader→Data URL→image state | Spring이 파일 저장에 사용할 문자열 |
| `ProductUpdateForm` | route id와 기존/변경값 | GET으로 채움→같은 handler→PUT | 기존 Product와 필요 시 image 변경 |
| Cart quantity input | 문자열 수량 | 정수 변환→최소값/재고 검사→POST/PATCH | Cart 추가 또는 화면·DB 수량 갱신 |

## 자주 헷갈리는 원인

- `event.target`은 실제 event 발생 요소이고 `currentTarget`은 handler가 연결된 요소다. 이 수업의 form 값 읽기는 target을 중심으로 했다.
- submit의 `preventDefault`는 브라우저 기본 제출·새로고침을 막는 것이고, 04-09 상품 card 삭제에서 사용한 `stopPropagation`은 상위 클릭으로 번지는 것을 막는 것이다.
- `event.target.value`는 number input에서도 문자열이다. 숫자 업무 규칙에 쓰기 전에 변환과 실패 처리가 필요하다.
- FileReader 결과가 곧 서버 파일은 아니다. React는 문자열을 준비하고 Spring이 실제 파일 저장을 처리했다.
- `isInvalid`가 보인다는 사실과 Spring Validation이 통과했다는 사실은 다르다. 화면 오류 state와 backend 검증 결과의 key를 맞춰 연결한 것이다.
- 등록과 수정은 form 모양이 비슷해도 기존 id·초기 GET·요청 목적이 다르다.

## 이전 개념과 이후 기능 연결

- 이전: UI&UX의 HTML form과 JavaScript event가 React controlled state와 typed event로 확장됐다.
- 기반 문법: component·props/state·event type은 [[concepts/react-typescript-basics|React와 TypeScript 기본]]에서 설명한다.
- 이후: 같은 입력→state→요청 구조가 Product CRUD, Cart, 검색 form으로 확장됐다. API 오류와 interceptor 책임은 [[concepts/axios-interceptor-error-handling|Axios interceptor와 API 오류 처리]]가 맡는다.

## 직접 수업·교안 보충·후속 범위

- **직접 수업:** SignupPage, ProductInsertForm/ProductUpdateForm, ProductDetail·CartList 수량 입력에서 실제 사용한 event·state·FileReader·오류 표시다.
- **교안 보충:** React 교안의 event object와 spread 설명은 실제 form handler를 이해하는 보조 근거다.
- **후속 범위:** 전역 form library·전역 상태관리 도입 근거는 이 raw에 없다. Linux·AWS·CI/CD는 form 구현이 아니라 실행·배포 확장이고, Passwordless·중간 프로젝트 form은 별도 후속 구현이다.

## 관련 페이지

- [[summaries/2026-04-10-react-event-spread-product-form|04-10 React 이벤트 객체와 전개 연산자]]
- [[summaries/2026-04-15-cart-list-selection-typescript|04-15 장바구니 목록과 TypeScript props]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[concepts/react-useeffect-data-fetching|React useEffect와 데이터 요청]]
- [[comparisons/props-vs-state|props vs state]]
- [[concepts/product-domain-flow|상품 도메인 기능 흐름]]

## 출처

- 위 frontmatter의 04-03·04-10·04-13·04-15 날짜 MD, `FrontEnd_BackEnd 총정리.md`, React 교안