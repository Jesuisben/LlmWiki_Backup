---
title: 2026-03-25 Bootstrap과 HTML Form
created: 2026-07-02
updated: 2026-07-15
type: summary
tags: [html, css, bootstrap, frontend, curriculum]
sources:
  - "raw/KoreaICT/3. UI&UX/2026.03.25(수)/2026.03.25(수).md"
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
  - "raw/KoreaICT/3. UI&UX/교육 자료/웹 서비스 Ui&UX.pdf"
  - "raw/KoreaICT/3. UI&UX/교육 자료/HTML&JS&CSS 이론(new).pdf"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/CartList.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/CartList.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/ProductInsertForm.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductInsertForm.html"
status: growing
confidence: high
---

# 2026-03-25 Bootstrap과 HTML Form

## 한 줄 요약

[[entities/bootstrap|Bootstrap]]을 CDN으로 연결해 표·버튼·그리드·Form을 빠르게 꾸미고, 상품 등록 화면의 입력 양식을 만들며 이후 상품 목록/상세 페이지 실습의 화면 기반을 준비한 날이다.

## 배운 내용

### 1. Bootstrap을 왜 쓰는가

원본은 W3Schools Bootstrap 5 문서를 참고해 `CartList.html`을 Bootstrap 방식으로 다시 구성한다. 전날까지는 직접 CSS를 작성했지만, Bootstrap은 이미 만들어진 CSS class를 가져다 쓰는 방식이다.^[raw/KoreaICT/3. UI&UX/2026.03.25(수)/2026.03.25(수).md]

예를 들어 `btn`, `btn-primary`, `table`, `container`, `row`, `col-sm-*`, `form-control` 같은 class는 직접 정의하지 않아도 Bootstrap CSS가 의미를 알고 있다.

### 2. CDN 연결

Bootstrap 실습은 CDN 링크를 HTML에 넣는 방식으로 진행한다. CDN은 라이브러리 파일을 내 프로젝트에 복사하지 않고 외부 주소에서 불러오는 방식이다. 이 방식은 빠르게 시작하기 좋지만, 실제 서비스에서는 버전 고정과 네트워크 의존성을 신경 써야 한다.

### 3. Grid system

`container → row → col` 흐름은 Bootstrap 레이아웃의 기본이다.

- `container`: 화면 가운데 정렬과 기본 여백을 잡는 큰 틀
- `row`: 가로 한 줄
- `col-sm-1`, `col-sm-9`: 12칸 기준으로 차지할 폭을 나누는 열

이날 `ProductInsertForm`에서 label과 input의 공간 분리를 하며 grid를 사용했다.

### 4. Form과 버튼

`form`은 입력 양식이다. 원본은 `<form id="productform">`, `<input>`, `<select>`, `<button>`을 이용해 상품 등록 폼을 만든다.

버튼은 `type`에 따라 의미가 달라진다.

| 버튼 | 의미 |
|---|---|
| `type="submit"` | form 데이터를 제출 |
| `type="button"` | 아무 기본 동작이 없는 일반 버튼 |
| `type="reset"` | form 입력값 초기화 |

원본은 “버튼은 양식(form) 안에 있어야 양식 안 데이터들을 이용해 정상 작동한다”는 점을 강조한다.

## 핵심 실습

### Bootstrap CartList

`B.nobootstrap/CartList.html`과 `C.yesbootstrap/CartList.html`을 비교하며 직접 CSS와 Bootstrap class의 차이를 경험했다. 전자는 `.container`, `.row`, `.btn` 규칙을 문서에서 직접 정의하고, 후자는 CDN을 연결한 뒤 `table-striped`, `table-bordered`, `align-middle`, `form-control`, `btn-sm`을 조합한다. 이 실습은 [[comparisons/custom-css-vs-bootstrap|직접 CSS 구현 vs Bootstrap]]과 [[comparisons/library-vs-framework|Library vs Framework]] 감각으로 연결된다.

### ProductInsertForm

상품명, 카테고리, 가격 같은 입력을 받을 form을 만들고 `form-control`, `btn`, `row`, `col-*` class를 붙였다. 이후 Spring/React의 상품 등록 폼을 이해할 때 이 HTML form 경험이 배경이 된다.

날짜별 원본의 실제 진행 순서는 먼저 `B_nobootstrap/ProductInsertForm`으로 HTML form 구조를 익힌 뒤, 오후에 `C_yesbootstrap/ProductInsertForm`에 Bootstrap class를 적용하는 방식이었다. 다음 코드는 원본에 기록된 Bootstrap 적용 예다.

```html
<form id="productform">
	<div class="mb-3 mt-3">
		<label for="name">이름</label>
		<input type="text" class="form-control" id="name" placeholder="이름 입력" name="name">
		<div class="invalid-check">이름 오류</div>
	</div>

	<button type="submit" class="btn btn-primary">Submit</button>
</form>
```

이날 구현은 브라우저 안의 입력 양식과 배치까지다. 실제 서버 저장, 유효성 검증 응답, React 상태 관리는 이 수업에서 구현한 범위가 아니라 후속 Spring/React 프로젝트에서 확장되는 지점이다.

날짜 노트와 현재 교육 HTML은 그대로 같은 버전이 아니다. 날짜 노트에는 `id="productform"`, `col-sm-1/9`, `invalid-check`가 기록되어 있지만 현재 `C.yesbootstrap/ProductInsertForm.html`은 `id="productForm"`, `col-sm-2/10`, `invalid-feedback`을 사용한다. 따라서 위 fence는 **날짜 노트 코드**이고, 현재 보존된 교육 artifact의 최종 형태와 조용히 합치지 않는다.

현재 교육 HTML에는 `FileReader`, `FormData`, `preventDefault()`도 들어 있지만 날짜 노트는 이 전체 JavaScript를 이날 직접 구현했다고 기록하지 않는다. 이 페이지의 직접 학습 중심은 form control과 Bootstrap grid/class이며, submit event의 확장은 [[concepts/html-form-controls-submission]]에서 artifact 근거와 함께 구분한다.

## 헷갈린 점 / 질문

- Bootstrap class는 “HTML class 속성”을 쓰지만, 실제 의미는 Bootstrap CSS 파일 안에 정의되어 있다.
- `form`은 입력 양식이고, 단순 목록/표를 보여줄 때는 `table`이나 `div/card` 구조가 더 적절하다.
- `submit` 버튼은 나중에 `action`, JavaScript 이벤트, Spring Controller/API와 연결될 때 실제 전송 흐름을 갖는다.
- 일반 `button`은 form 밖에서도 사용할 수 있다. form과 직접 연결되는 기본 동작은 주로 `submit`과 `reset`이다.

## 관련 페이지

- [[concepts/bootstrap-basics]]
- [[concepts/html-css-basics]]
- [[entities/bootstrap]]
- [[comparisons/library-vs-framework]]
- [[comparisons/get-vs-post]]
- [[comparisons/custom-css-vs-bootstrap]]
- [[concepts/html-form-controls-submission]]

## 출처

- `raw/KoreaICT/3. UI&UX/2026.03.25(수)/2026.03.25(수).md`
- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
