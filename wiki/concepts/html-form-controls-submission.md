---
title: HTML Form control과 제출 흐름
created: 2026-07-15
updated: 2026-07-15
type: concept
tags: [html, javascript, frontend]
sources:
  - "raw/KoreaICT/3. UI&UX/2026.03.24(화)/2026.03.24(화).md"
  - "raw/KoreaICT/3. UI&UX/2026.03.25(수)/2026.03.25(수).md"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/ProductInsertForm.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductInsertForm.html"
status: growing
confidence: high
---

# HTML Form control과 제출 흐름

## 정의

HTML `form`은 사용자의 입력을 하나의 제출 단위로 묶는다. `input`, `select`, `button`은 form control이며, `name`은 제출 데이터의 key, 사용자가 입력하거나 고른 값은 value가 된다.

## 왜 중요한가

상품 등록, 로그인, 회원가입은 모두 “사용자가 값을 입력하고 서버로 보낸다”는 구조를 가진다. UI&UX 수업에서는 HTML control의 의미를 먼저 배우고, 직접 CSS와 Bootstrap으로 상품 등록 화면을 만든 뒤, JavaScript의 submit event와 `FormData`로 입력 데이터를 확인했다.

## 핵심 설명

### 입력 목적에 맞는 control을 고른다

- `input type="text"`: 이름·가격·재고처럼 한 줄 값을 입력한다.
- `input type="file"`: 파일을 선택한다.
- `select`와 `option`: 정해진 후보 중 하나를 고른다.
- `button type="submit"`: form 제출을 시작한다.
- `button type="reset"`: form control 값을 초기 상태로 되돌린다.
- `button type="button"`: 기본 제출 없이 JavaScript 동작을 연결할 때 쓴다.

```html
<select name="category" class="form-select">
    <option value="-">-- 카테고리를 선택해 주세요.</option>
    <option value="BREAD">빵</option>
    <option value="BEVERAGE">음료수</option>
    <option value="CAKE">케이크</option>
</select>
<div class="invalid-feedback">카테고리 오류</div>
```

### `name`과 `value`가 제출 데이터를 만든다

화면에 보이는 label이나 placeholder는 사용자를 안내하지만, 제출 데이터의 이름은 control의 `name`이 정한다. 예를 들어 `name="category"`인 select에서 `BREAD`를 고르면 category라는 key와 BREAD라는 value의 관계가 만들어진다.

### submit event는 제출 직전에 개입한다

교육자료의 상품 등록 예제는 실제 서버 전송 대신 submit event를 가로채 `FormData`를 만들고 값을 검사한다.

```javascript
form.addEventListener("submit", function(e) {
    e.preventDefault();

    const formData = new FormData(form);
    const category = formData.get("category");

    // 간단한 검증
    if (category === "-") {
        alert("카테고리를 선택해 주세요.");
        return;
    }
```

`preventDefault()`는 브라우저의 기본 제출을 막는다. 따라서 이 코드만으로 서버에 등록되는 것은 아니며, 교육자료도 실제 전송 대신 콘솔 출력과 alert로 끝난다.

## 수업 흐름

1. 2026-03-24에 여러 `input` type과 form control을 확인했다.
2. 2026-03-25에 Bootstrap 미적용 상품 등록 form을 먼저 만들었다.
3. 같은 구조에 Bootstrap grid와 form class를 적용했다.
4. 교육 HTML은 `FileReader`로 이미지 미리보기를 만들고, submit event에서 `FormData`를 확인한다.
5. 이후 GET/POST, React form state, Spring Controller의 요청 처리로 확장된다.

## 자주 헷갈리는 점

- placeholder는 label을 대체하지 않는다. 값 입력 후 사라지므로 control의 목적을 계속 보여 주지 못한다.
- `button`은 form 안에서만 쓸 수 있는 태그가 아니다. 다만 submit/reset의 기본 동작은 연결된 form과 관계가 있다.
- `type="submit"` 버튼을 눌렀다고 서버 저장이 자동 완성되는 것은 아니다. `action`, `method` 또는 JavaScript 요청과 서버 처리 로직이 필요하다.
- POST body가 주소창에 보이지 않는다는 사실만으로 안전하지 않다. HTTPS, 서버 검증, 인증·인가가 별도로 필요하다.
- 클라이언트 검증은 사용자 편의를 높이지만 우회할 수 있으므로 서버 검증을 대신하지 않는다.

## 관련 개념

- [[concepts/html-css-basics]]
- [[concepts/bootstrap-basics]]
- [[comparisons/get-vs-post]]
- [[comparisons/custom-css-vs-bootstrap]]
- [[summaries/2026-03-25-bootstrap-form]]
- [[concepts/react-form-state-event]]

## 출처

- `raw/KoreaICT/3. UI&UX/2026.03.24(화)/2026.03.24(화).md`
- `raw/KoreaICT/3. UI&UX/2026.03.25(수)/2026.03.25(수).md`
- `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/ProductInsertForm.html`
- `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductInsertForm.html`
