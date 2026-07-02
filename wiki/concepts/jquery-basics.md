---
title: jQuery 기본
created: 2026-06-30
updated: 2026-07-02
type: concept
tags: [jquery, javascript, frontend]
sources:
  - raw/Study/3. UI&UX/2026.03.27(금)/2026.03.27(금).md
status: growing
confidence: high
---

# jQuery 기본

## 정의

jQuery는 JavaScript DOM 선택, 이벤트 처리, class/속성 조작, 표시/숨김 같은 작업을 짧고 일관된 문법으로 작성하게 해주는 JavaScript 라이브러리다. 수업에서는 CSS 선택자 감각과 JavaScript DOM 조작을 합쳐 이미지 토글, 선택 강조, 카테고리 필터, 썸네일 변경, 이미지 회전 같은 UI 상호작용을 만들었다.

## 이 수업에서의 맥락

2026-03-27 수업은 JavaScript DOM을 배운 다음날 진행되었다. 전날 `document.getElementById`, `createElement`, `appendChild`, 이벤트, URL 파라미터를 배웠고, 이날은 그 DOM 조작을 jQuery의 `$()` 선택자와 메서드로 더 간결하게 작성했다. 원본 노트는 jQuery를 “JS의 라이브러리”이자 “CSS 선택자와 JS를 묶어서 코딩하는 것을 집대성한 형태”로 설명했다. ^[raw/Study/3. UI&UX/2026.03.27(금)/2026.03.27(금).md]

## 핵심 설명

### jQuery는 CDN으로 불러와 사용한다

수업에서는 HTML `<head>`에 jQuery CDN을 먼저 넣고, 그 아래 Bootstrap CDN을 넣는 기본 골조를 만들었다.

```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
```

Bootstrap과 jQuery의 관계에 대해 노트에는 “부트스트랩의 전제가 jQuery의 존재라서 Bootstrap을 쓴다면 jQuery를 적어주는 것이 좋다”라고 적혀 있다. 다만 현대 Bootstrap 5는 예전 버전과 달리 jQuery가 필수는 아니다. 이 위키에서는 원본 수업 맥락은 보존하되, 버전에 따라 의존성이 달라질 수 있음을 함께 기억한다. ^[raw/Study/3. UI&UX/2026.03.27(금)/2026.03.27(금).md]

### `$`는 jQuery를 부르는 기호다

수업에서는 `$` 기호를 jQuery를 부르는 기호로 설명했다.

```javascript
$("#grayImg")
```

위 코드는 CSS 선택자처럼 id가 `grayImg`인 요소를 선택한다. `$(".select-img")`는 class가 `select-img`인 요소들을 선택한다. 즉 jQuery 선택자는 CSS 선택자 지식과 직접 연결된다.

### `$(function(){ ... })`은 DOM 준비 후 실행이다

표준 JavaScript의 `DOMContentLoaded`와 비슷하게, jQuery에서는 다음처럼 HTML 문서를 다 읽은 뒤 실행할 코드를 작성한다.

```javascript
$(function () {
    // 여기에 할 일 작성
});
```

이 구조 안에 이벤트 등록 코드를 넣으면, 아직 HTML 요소가 만들어지기 전에 선택하려다 실패하는 일을 줄일 수 있다. ^[raw/Study/3. UI&UX/2026.03.27(금)/2026.03.27(금).md]

### click과 toggleClass로 상태를 바꾼다

흑백 토글 예제에서는 이미지를 클릭할 때마다 class를 붙였다 떼었다.

```javascript
$(function () {
    $("#grayImg").click(function () {
        $(this).toggleClass("gray");
    });
});
```

- `click(function(){ ... })`: 클릭 이벤트가 발생하면 함수 실행
- `$(this)`: 이벤트가 발생한 바로 그 요소
- `toggleClass("gray")`: `gray` class가 없으면 추가하고, 있으면 제거

이 예제는 “상태를 class로 표현하고, class 유무에 따라 CSS가 화면을 바꾼다”는 프론트엔드 기본 패턴을 보여준다. ^[raw/Study/3. UI&UX/2026.03.27(금)/2026.03.27(금).md]

### addClass와 removeClass로 선택 상태를 하나만 유지한다

선택 이미지 강조 실습에서는 여러 이미지 중 하나만 활성화되도록 만들었다.

```javascript
$(".select-img").click(function () {
    $(".active").removeClass("active");
    $(this).addClass("active");
});
```

원본에는 선생님 코드와 사용자 작성 코드가 함께 있었다. 선생님 코드는 `.select-img` 전체에서 `active`를 제거했고, 사용자 코드는 현재 `.active`인 요소만 찾아 제거했다. 기능은 비슷하지만, 이미 활성화된 요소만 찾는 방식이 더 좁은 범위를 대상으로 한다는 점을 배울 수 있다. ^[raw/Study/3. UI&UX/2026.03.27(금)/2026.03.27(금).md]

### change, val, show, hide로 카테고리 필터를 만든다

콤보박스는 클릭보다 값이 바뀌었는지를 보는 `change` 이벤트가 잘 맞는다.

```javascript
$("#categorySelect").change(function () {
    const selected = $(this).val();

    if (selected === "all") {
        $(".combo-image").show();
    } else {
        $(".combo-image").hide();
        $(".combo-image[data-category='" + selected + "']").show();
    }
});
```

이 예제에서 핵심은 속성 선택자다.

```javascript
$(".combo-image[data-category='" + selected + "']")
```

의미는 “`combo-image` class를 가진 요소 중 `data-category` 속성값이 선택된 값과 같은 요소”를 찾는 것이다. 원본 노트에는 문자열 결합 후 최종 선택자가 `.combo-image[data-category='all']`처럼 완성되는 과정이 자세히 적혀 있다. 공백이 들어간 값까지 안전하게 다루려면 속성값을 따옴표로 감싸는 습관이 좋다. ^[raw/Study/3. UI&UX/2026.03.27(금)/2026.03.27(금).md]

### attr로 HTML 속성을 읽고 바꾼다

썸네일을 클릭하면 큰 이미지가 바뀌는 예제에서는 `attr("src")`로 이미지 경로를 읽고 다시 설정했다.

```javascript
$(".thumb-image").click(function () {
    const newSrc = $(this).attr("src");
    $("#mainImage").attr("src", newSrc);
    $(".active-thumb").removeClass("active-thumb");
    $(this).addClass("active-thumb");
});
```

`attr`은 attribute의 줄임말로, HTML 속성을 읽거나 바꿀 때 사용한다. 이 예제는 이미지 경로, class 상태, 클릭 이벤트가 함께 결합된 UI 패턴이다. ^[raw/Study/3. UI&UX/2026.03.27(금)/2026.03.27(금).md]

### method chaining은 여러 동작을 이어 쓰는 방식이다

수업 마지막에는 `removeClass().addClass()`처럼 동작을 이어 쓰는 method chaining을 배웠다.

```javascript
myImage.removeClass().addClass("img-fluid");
```

같은 대상에 대해 여러 메서드를 연속으로 호출하므로 코드가 짧아진다. 다만 초보 단계에서는 각 메서드가 어떤 대상을 반환하는지 이해해야 한다.

## 자주 헷갈리는 점

### jQuery는 JavaScript를 대체하는 언어가 아니다

jQuery는 JavaScript 위에서 동작하는 라이브러리다. 따라서 변수, 함수, 배열, 객체, 조건문, 이벤트 개념은 그대로 필요하다.

### `$()` 안에는 CSS 선택자처럼 문자열을 넣는 경우가 많다

`$("#id")`, `$(".class")`, `$("input[name='imgStyle']")`처럼 CSS 선택자 문법을 사용한다. 원본 노트에서 속성 선택자 문자열 결합을 자세히 풀어쓴 이유도, 최종적으로 `$()` 안에 들어갈 선택자 문자열이 정확해야 하기 때문이다.

### click보다 change가 자연스러운 요소가 있다

체크박스, 라디오, 콤보박스는 “클릭했는가”보다 “값이 바뀌었는가”가 더 중요한 경우가 많다. 그래서 수업에서도 `select`와 `radio`에는 `change` 이벤트를 쓰는 경향이 있다고 정리했다.

### Bootstrap 5와 jQuery 의존성은 버전을 확인해야 한다

원본 수업에서는 Bootstrap과 jQuery를 함께 넣는 흐름으로 배웠지만, Bootstrap 버전에 따라 jQuery가 필수인지 여부가 다르다. 프로젝트에서 실제로 사용할 때는 사용하는 Bootstrap 버전의 문서를 확인한다.

## 이전/이후 학습과의 연결

- 이전: [[concepts/javascript-dom|JavaScript와 DOM]]에서 `document.getElementById`, 이벤트, `appendChild`, `style.display`를 배웠다.
- 이전: [[concepts/html-css-basics|HTML/CSS 기본]]에서 id/class/속성 선택자를 배웠다.
- 같은 흐름: [[concepts/bootstrap-basics|Bootstrap 기본]] class와 함께 UI 요소를 꾸몄다.
- 이후: React에서는 직접 DOM을 조작하기보다 state와 렌더링으로 화면을 바꾸지만, 이벤트와 class 상태 전환의 기본 감각은 이어진다.

## 관련 개념

- [[entities/jquery|jQuery]]
- [[concepts/javascript-dom|JavaScript와 DOM]]
- [[concepts/html-css-basics|HTML/CSS 기본]]
- [[concepts/bootstrap-basics|Bootstrap 기본]]
- [[summaries/2026-03-27-jquery-ui-interaction|2026-03-27 jQuery와 UI 상호작용]]

## 출처

- `raw/Study/3. UI&UX/2026.03.27(금)/2026.03.27(금).md`
