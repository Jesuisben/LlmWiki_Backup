UI&UX 총정리 (2026.03.23(월) ~ 2026.00.00(00))


#### \# 추천하는 공부하는 사이트 (W3Schools)
https://www.w3schools.com/



#### \# IT 관련 용어 교안 설명
- UI (User Interface)
디자인, 시각적 요소, 사용자가 보는 것

- UX (User Experience)
유용성, 만족감, 사용자가 느끼는 것



#### \# HTML (Hyper Text Markup Language) (HTML&JS&CSS 이론(new) 교안 (P.2))
- 개념
웹페이지를 꾸미기위한 언어

- 하이퍼 텍스트 (Hyper Text)
텍스트에 하이퍼 링크 설정이 가능하고 텍스트들이 서로 연결되어 있는 것

- 마크업 (Markup)
특정한 글꼴이나 색을 지정하는 것

- 확장자
html, htm



#### \# HTML 관련 용어 (HTML&JS&CSS 이론(new) 교안 (P.3))
- 태그(Tag)
<>를 이용하여 표현하는 것들
ex) \</body\> : body 태그

- 요소(Element)
시작 태그와 종료 태그의 조합
ex) \<head\> ..... \</head\>

- 셀프 클로징 태그
태그의 조합말고 혼자서도 요소가 되는 것
ex) \<head\> ..... \</head\>같이 2개가 필요한 것이 아니라
\<br\> 처럼 하나로도 요소 역할을 하는 것

- 속성(Attribute)(Property), (속성)값(Value)
```html
<body bgcolor = "yellow" text="black">
```
속성 : bgcolor, text
속성값 : "yellow", "black"

- top-down방식
html은 위에서부터 아래로 순차적으로 진행이 됨



#### \# 화이트 캐릭터
엔터 같은 것들은 눈에 안보이기 때문에 이렇게 부름
아무리 엔터를 쳐도 html에서는 안보임 (적용 안됨)



#### \# 단축키
- Ctrl + Alt + L
자동 들여쓰기

- Ctrl + Shift + /
주석 on/off



#### \# 태그들
- \<br\>
줄바꿈 태그

- \<!-- ..... --\>
주석 태그

- \<hn\>
목차 생성 태그, 제목 생성 태그
\<h1\> - 가장 크기가 큼
\<h2\>, \<h3\>, \<h4\>, \<h5\>
\<h6\> - 가장 크기가 작음
자동 줄바꿈 O

- \<span\>
텍스트 일부분에 스타일을 줄 때 사용하는 인라인 요소
주 목적 : 속성 추가하여 글자, 문구에 색 지정, 크기 지정
인라인(Inline) 요소 : 줄바꿈 X
문법 :
```html
<span 속성="CSS속성:CSS속성값;">글씨</span>
```
 ex)
```html
 <span style="font-size: 30px; color: red;">하하하</span><br>
```
 -> 이런 행위를 스타일 속성을 이용해서 "스타일을 입힌다"라고 표현한다. (중요!!)
\* 속성을 많이 알수록 잘하는 거임 *

- \<hr\> : 수평 가로 구분선 태그, Horizontal Rule의 약자
전체를 100%로 봄
기본 값이 가운데 정렬
ex) 너비가 30%인 줄 생성
```html
<hr style="width: 30%;">
```
단위 : %, px 등

- \<ol\> : 순서가 있는 목록 태그, Ordered list의 약자
기본값 : 숫자로 목록 표시
\<ol\>태그 안에 \<li\>태그를 넣어 함께 사용

- \<ul\> : 순서가 없는 목록 태그, Unordered List의 약자
기본값 : 검은색 동그라미
\<ul\>태그 안에 \<li\>태그를 넣어 함께 사용

-  \<li\> : 목록의 항목 태그, List Item의 약자 (목록 안에 들어가는 하나하나의 내용)
ex)
```html
<ol> <!-- ordered list -->
    <li>티포트에 드라이 허브 3g을 넣는다.</li>
    <li>끓는 물 200ml를 붓고 뚜껑을 닫아 3~5분 정도 우려낸다.
    허브티는 꼭 끓는 물로 우리는 것이 포인트다.</li>
    <li>거름망을 이용해 찻잔에 따른다.</li>
</ol>
```

- \<head\>태그
공통적으로 참조할만한 것들을 넣는 곳
ex)
```html
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        li {
            font-size: 12px;
            color: purple;
        }
    </style>
</head>
```
-> li 태그들 전부다 12px로 바꿔라

- \<body\> 태그
내용을 넣는 곳

- \<img\>태그
이미지 가져오기



#### \# 속성들
- font-size
폰트 크기
단위 : px

- color
단위 : 영문

- src
이미지 폴더 경로

- font-weight: bold;
폰트 두께 - 두껍게
bolder는 더 두껍게

- font-face: 굴림;
글꼴

- text-decoration: underline;
글자 장식에서 밑줄 장식



#### \# W3Schools 사이트에서 공부하기
- entity
"Some Useful HTML Character Entities"
https://www.w3schools.com/htmL//html_entities.asp

- 색상 RGB값 찾기
-> 좌측상단 Tutorials - HTML and CSS - Learn Colors - 좌측 Color Names
https://www.w3schools.com/colors/colors_names.asp

- HTML 이미지
검색창에 img 검색 - HTML Images
https://www.w3schools.com/html/html_images.asp

- text-decoration 속성값
attribute (속성) / property (속성)
CSS text-decoration Property 클릭
https://www.w3schools.com/cssref/pr_text_text-decoration.php



#### \# 문단 꾸미기 - 문자 엔티티 (HTML&JS&CSS 이론(new) 교안 (P.13))
\* (중요함!!)HTML에서 \<는 비교 연산자 느낌이 아니라 태그로 인식하기에 주의해야 함 \*
- 엔티티
문법 :
```
&.....;
```

- &nbsp;
공백 문자 하나, non-breaking space의 줄인 말

- &lt;
<, Less than의 줄인 말

- &gt;
\>, Greater than의 줄인 말

- &amp;
&, Ampersand의 줄인 말

- &quot;
", 	double quotation maker의 줄인 말

- &apos;
', single quotation mark의 줄인 말

- &copy;
ⓒ, 저작권, 판권을 표시, Copyright의 줄인 말

- &trade;
TM, 상표를 표시, Trademark의 줄인 말



#### \# 색상 표기법 (HTML&JS&CSS 이론(new) 교안 (P.5))
1) 영문의 색상명으로 표기하는 방법

2) 16진수 RGB 값으로 표기하는 방법
R(red) 2자리, G(green) 2자리, B(blue) 2자리 총 6자리로 구성
각 색상은 0부터 255(FF)까지 총 256의 색상을 가지고 조합
문법:
\# RRGGBB
ex)
순 빨간색
\#FF0000



#### \# inline style(인라인 스타일)
HTML 태그 안에 직접 style 속성을 사용해서 디자인을 입히는 방식
ex)
```html
<span style="color: yellow">호호호</span>
```



#### \# CSS 선택자 (Selector) 3개 (태그 선택자, class 선택자, id 선택자)
선택자란?
CSS 스타일을 적용할 HTML 대상을 지목하는 문법입니다.

1\. 태그 선택자 (style태그) (내장 style 방식) \<-\> 외장 style 방식 (안배움)
특정 태그 전체에 스타일을 적용
head태그 안에 적는 것이 일반적, but! 반드시는 아님
문법 :
```html
<style>
	특정태그명{
		속성: 속성값;
		속성: 속성값;
	}
</style>
```

ex)
```html
<style>
	li{
		font-size: 12px;
		color: purple;
	}
</style>
```
-> li태크의 내용의 폰트 크기를 12px로, 색은 보라색으로


2\. class 선택자 (전체에서 몇개만 그룹핑할때 사용)
식별자, 심벌 :
. (dot) (점)
2개 이상의 속성을 가질 수 있음 (구분자 : 스페이스) (중요!!!)
- 만들어진 이유 :
```html
<style>
	ol{list-style-type: upper-alpha;}
</style>
```
-> 이렇게 하면 ol 전체가 다 list-style-type: upper-alpha;가 됨
-> * ol의 몇개만 그룹핑해서 속성을 부여하기 위해 만들어짐 *

- 문법 :
1) 태그 선택자 내부
1-1) 일반적인 상황
```html
.속성명{CSS속성: CSS속성값;}
```
1-2) 속한 태그명을 강조하고 싶을때
```html
태그명.속성명{CSS속성: CSS속성값;}
```

2) \<body\>태그 내부
\* ; (세미콜론)을 사용하지 않는다는 걸 기억하기!!!(중요!!) *
```html
<태그명 class="속성명">.....</태그명>
```

- ex) 전체에서 몇개만 그룹핑할때
1) 태그 선택자 내부
```html
<style>
	.myyellow{color: yellow;background-color: black;}
</style>
```

2) \<body\>태그 내부
```html
<ol class="upper-alpha">
    <li class="myyellow">파인 애플</li>
    <li>바나나</li>
    <li class="myyellow">사과</li>
</ol>
```

- ex) class가 2개의 속성을 가질때
1) 태그 선택자 내부에 속성명을 따로 적어 줘야 함
(\<head\>)
```html
<style>
	.myyellow{color: yellow;background-color: black;}
	.myblue{color: blue;}
</style>
```
-> top-down 방식이라서 blue값이 설정됨 (중요!)

2) \<body\>태그 내부에서는 스페이스로 구분하여 2개를 적음
(\<body\>)
```html
<li class="myyellow myblue">사과</li>
```


3\. id 선택자
DB의 primary key와 같이 식별할때 쓰는것
무조건 한 번만 등장(중복 불가)
식별자, 심벌 :
\# (hash) (샵)
\* class 선택자와 다른점은 1) .(dot)대신 #(샵)을 사용하는 것, 2) 중복불가 *

- id의 중복
id의 값이 중복이면 Java에서는 안돌아가지만
html에서는 돌아가긴함
top-down 방식이기에 가장 위에 있는 id의 값을 id로 인식함

- 문법 :
1) 태그 선택자 내부
1-1) 일반적인 상황
```html
#속성명{CSS속성: CSS속성값;}
```
1-2) 속한 태그명을 강조하고 싶을때
```html
태그명#속성명{CSS속성: CSS속성값;}
```

2) \<body\>태그 내부
\* ; (세미콜론)을 사용하지 않는다는 걸 기억하기!!!(중요!!) *
```html
<태그명 id="속성명">.....</태그명>
```

- ex)
1) 태그 선택자 내부
```html
<style>
	#upper-roman{list-style-type: upper-roman;}
</style>
```

2) \<body\>태그 내부
```html
<ol id="upper-roman">
    <li>티포트에 프레시 허브를 잘게 찢어 넣는다.</li>
    <li>끓는 물 200ml를 붓고 뚜껑을 닫아 3~5분 정도 우려낸다.</li>
    <li>거름망을 이용해 찻잔에 따른다.</li>
</ol>
```



#### \# 헷갈리지 말기
-  인라인(inline) 스타일        VS          태그 선택자 이용
```
<li style="color: purple;">    VS      <style>    li{color: purple;}    </style>
```

- 태그 선택자 + class 선택자
1) 태그 선택자 내부
```html
<style>
	.myyellow{color: purple;}
</style>
```

2) \<body\>태그 내부
```html
<li class="myyellow">.....</li>
```



#### \# table 태그 (중요함!!!!)
html에서 표를 만드는 것
1\. \<table\>태그 안에 들어가는 것들
- \<caption\>태그 : 테이블의 하위 개념
테이블(표)의 제목 느낌
문법 :
```html
<caption>.....</caption>
```

- \<thead\>태그 : table head의 약자 / 테이블의 \<head\>영역
1) \<tr\>태그 : table row의 약자 / 테이블의 행(가로줄)
1-1) \<th\>태그 : table header의 약자 / table head의 열(세로줄)

- \<tbody\>태그 : table body의 약자 / 테이블의 \<body\>영역
2) \<tr\>태그 : table row의 약자 / 테이블의 행(가로줄)
2-1) \<td\>태그 : table data의 약자 / 테이블의 일반셀(열)(세로줄)

2\. \<table\>태그 그림 표현
```html
<caption>.....</caption>
```
thead - tr ->	th		th		th

tbody - tr ->	td		td		td

ex)
```html
<body>
    <table>
        <caption>캡션내용</caption>
        <thead>
            <tr> // thead의 1행
                <th>컬럼</th>
                <th>컬럼</th>
                <th>컬럼</th>
            </tr>
        </thead>
        <tbody>
            <tr> // tbody의 1행
                <td>데이터</td>
                <td>데이터</td>
                <td>데이터</td>
            </tr>
            <tr> // tbody의 2행
                <td>데이터</td>
                <td>데이터</td>
                <td>데이터</td>
            </tr>
            <tr> // tbody의 3행
                <td>데이터</td>
                <td>데이터</td>
                <td>데이터</td>
            </tr>
        </tbody>
    </table>
</body>
```



#### \# images 파일 가져오기
<img>태그와 src속성 이용
문법 :
```html
<img src="이미지파일_폴더경로">
```
ex) img태그 src속성 "/images/basil.jpg"속성값
```html
<img src="/images/basil.jpg">
```



#### \# 하이퍼 링크 연결하기
\<a\>태그 (앵커 태그)와 href속성 이용 (href : Hypertext Reference)
문법 :
```html
<a href="인터넷_주소명">.....</a>
```
ex) \<a\>태그 href속성 "https://www.naver.com" 속성값
```html
<td><a href="https://www.naver.com">바질</a></td>
```



#### \# 그림 안나올때(액박날때) 대안으로 나오는 것 설정
\<alt\>태그 (alterative의 약자)
문법 :
```html
<alt="속성값">
```
ex)
```html
<td><img src="/images/basil.jpg" alt="바질"></td>
```



#### \# \<title\>태그
주소창 위에 오는 것 (이름)



#### \# 태그 선택자안에서 CSS설정하기
1\. 백그라운드 이미지 설정, 반복, 고정
ex)
```html
<style>
	body{
		background-image: url("/images/milk.jpg");
		/* x축 (가로축)에 반복 */
		background-repeat: repeat-x;
		/* 배경 고정 (마우스 휠 내릴때 배경이미지가 움직이지 않게) */
		background-attachment: fixed;
	}
</style>
```

2\. \<table\>의 가로폭 지정
단위 : px, %
ex)
```html
<style>
	table{
		width: 100px;
	}
</style>
```




#### \# Box Model (중요함!!) (HTML&JS&CSS 이론(new) 교안 (P.86))
모든 HTML 요소를 하나의 "박스"로 보고, 그 구조와 크기를 정의하는 개념
\* 꼭! 교안 이미지 확인하기 *
태그 선택자 안에서 CSS설정하기

1) 내용(content) 요소에 포함되어 있는 내용을 말합니다

2) 패딩(padding) 내용과 보더 사이의 여백(내부 여백)
-> 데이터가 들어가는 칸 안의 여백

3) 보더(border) (내용 + 패딩)의 테두리 선

4) 마진(margin) 보더와 다른 요소 사이의 여백(외부 여백)

5) top / bottom / left / right - ex) border-top

ex)
```html
<style>
	body{
		background-image: url("/images/milk.jpg");
		background-repeat: repeat-x;
		background-attachment: fixed;
	}
	table{
		width: 500px;
		border-top: 1px solid darkgreen;
		border-left: 1px solid darkgreen;
	}
	thead{
		background: darkgreen;
		color: white;
		font-size: 12px;
	}
	tbody{
		color: green;
		font-size: 12px;
	}
	th{
		border-right: 1px solid white;
		padding: 10px;
	}
	td{
		border-right: 1px solid darkgreen;
		border-bottom: 1px solid darkgreen;
		padding: 10px;
	}
</style>
```



#### \# 크롬의 개발자 도구 이용해서 코드 보기
tableExam 파일을 크롬으로 열기
F12번 누르기 (개발자 도구) (DevTool)

- 코드 보기
Elements 탭
코드에 마우스를 가져다 대면 해당부분이 하이라이트 됨
\<html lang="en"\>을 우클릭 후 Expand recursively하면 코드들이 다 나옴

- (select an element in the page to inspect it - Ctrl + Shift + C) 버튼
Elements 왼쪽 왼쪽 아이콘 클릭 후 화면으로 오면 그 부분이 하이라이트 되는데
그때 클릭하면 그 부분의 코드로 이동함
그렇게 나온 코드 우클릭 후 copy - copy element해서 메모장에 붙여넣기
ex) 캐모마일 글씨 선택
```html
<a href="https://www.daum.net">캐모마일</a>
```

ex) 테이블 선택
```html
<table>
	<caption>주요 허브 소개</caption>
	<thead>
		<tr>
			<th>이름</th>
			<th>사진</th>
			<th>설명</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><a href="https://www.naver.com">바질</a></td>
			<td><img src="/images/basil.jpg" alt="바질"></td>
			<td>두통, 신경과민 등에...</td>
		</tr>
		<tr>
			<td><a href="https://www.daum.net">캐모마일</a></td>
			<td><img src="/images/chamomile.jpg" alt="캐모마일"></td>
			<td>목욕제로 쓰면 심신의 긴장을 완화...</td>
		</tr>
		<tr>
			<td><a href="https://www.google.com">레몬밤</a></td>
			<td><img src="/images/lemonbalm.jpg" alt="레몬밤"></td>
			<td>레몬밤의 차는 뇌의 활동 강화..</td>
		</tr>
	</tbody>
</table>
```

- Console
결과물 출력되는 곳



#### \# \<p\>태그 (단락, pharagraph의 약자)
문법 :
```html
<p> 단락 </p>
```



#### \# text-decoration 속성 (HTML&JS&CSS 이론(new) 교안 (P.79))
- 속성값
none : 선도 없고 깜빡이지도 않는 글자 상태를 의미합니다.
underline : 글자에 밑줄이 그어진 상태를 의미합니다.
overline : 윗 줄이 있는 글자 상태로 지정합니다
line-through : 가운데 줄(취소선)이 있는 글자 상태로 지정합니다.
blink : firefox와 opera에서만 깜빡인다.



#### \# 값과 단위 (HTML&JS&CSS 이론(new) 교안 (P.68))
- px (픽셀)
주로 사용하는 단위

- em
주어진 폰트의 font-size 값과 동일한 값이 1em
ex) 주어진 font-size가 14px이면 1em은 14px

- rem
HTML의 기본 사이즈에 비해서 커짐(곱셈)



#### \# Element의 종류
1) block element (블록 요소)
일정 영역을 지정하는 요소 - 데이터가 없어도 일정 영역 차지
자동으로 줄 바뀜
크기 조절 가능 : width, height 이용
ex)
```
<div>, <h1>~<h6>, <p>, <ul>, <li>, <table>
```

2) inline element (인라인 요소)
텍스트 영역을 지정하는 요소 - 데이터가 없으면 차지하는 영역 없음
옆으로 나란히 붙음
크기 조절 불가 : width, height 무시
ex)
```
<span>, <a>, <img>, <strong>, <input>
```



#### \# \<div\>태그 (Division의 약자)
웹 페이지에서 논리적인 구역이나 섹션을 나누는 상자(Container) 역할
무색무취의 태그
컨테이너 역할
block element의 \<div\> = inline element의 \<span\>       -> 이런 느낌



#### \# boxModelTest 해보기 (웹 서비스 Ui&UX 교안(P.8))
- 웹 페이지 좌표
좌측 상단 : (0, 0) -> 아무리 (0, 0)이라도 약간의 여백 존재
우측으로 이동 : x좌표 상승
하단으로 이동 : y좌표 상승

```html
<div id="mydiv">
  <div class="test1">소녀 시대</div>
  <div class="test2">원더 걸스</div>
  <div class="test3">원더 걸스</div>
  <div class="test4">원더 걸스</div>
</div>
```

- \<div id="mydiv"\> : 부모역할
1) \<div\>태그가 블록 요소이기에 직사각형 영역이고 웹페이지에서 자신의 위치, 너비, 높이를 정하고 그 직사각형 안에서 test1~4가 존재함 (test1~4입장에서는 \<div id="mydiv"\>자체가 커다란 웹페이지 느낌)

2) \<div\>안에 있는 예)div class들 의 기본 양식을 정함
	But class에 또 다른 속성들을 지정한다면 따로 지정한 속성들이 class의 속성이 됨
	따라서 class들도 각자 자신의 위치, 너비, 높이를 정할 수 있음
	만약 부모 div보다 커지면 overflow현상이 일어남

- position : 위치의 기준 (절대좌표, 상대좌표)
1) relative : 상대좌표
지금 내가 원래 있어야 할 자리를 기준으로 이동
\*주로 자식 요소의 absolute 기준점을 잡기 위한 '부모 가이드' 역할로 가장 많이 씁니다.*
-> 부모태그에 relative라고 설정하면 자식 태그들은 부모태그 안에서 좌표가 시작됨

2) absolute : 절대좌표
가장 가까운 부모(static이 아닌)를 기준으로 이동
부모 요소 중 position: relative가 걸려 있는 곳을 찾아 그곳의 (0,0) 좌표부터 시작
부모 중에 아무도 없다면 브라우저 화면(body)을 기준으로 시작

- 테두리 선 만들기
border : 보더(border) (내용 + 패딩)의 테두리 선
border: 1px solid red; - (단축) 속성 표기법
-> 테두리 선 두께를 1px / solid(실선) / 빨간색

- 자식 태그의 위치 계산
(부모)
```css
div#mydiv{
	top: 10px;
	left: 10px
}
```

(자식)
```css
.test1{
  top:20px;
  left: 0px;
}
```

부모의 위치 + 자식의 위치 = 자신의 위치
-> (10, 10) + (0, 20) = (10, 30)



#### \# overflow
요소의 가로와 세로 크기 범위를 넘어 내용이 삽입되었을 경우 표시 방식을 지정
속성값 :
- visible (기본값)
넘치는 내용 그대로 다 보여줌 / 박스 테두리 밖으로 글자가 삐져나오게 됨

- hidden
박스 크기를 벗어나는 부분은 칼로 자른 듯이 보이지 않게 만듬
-> border-radius를 적용해서 둥근 모서리를 만들었을때 주로 사용자

- scroll
내용이 박스보다 크든 작든 항상 스크롤바 생성함

- auto
내용이 박스보다 클 때만 필요에 따라 스크롤바를 보여줌



#### \# display
요소들을 세로로 쌓을지, 가로로 나열할지 결정하는 '성질' 그 자체를 정의
속성값 :
- block
가로 너비(width)를 100% 차지
다음에 오는 요소는 무조건 다음 줄로 밀려남
width, height, margin, padding 값 조절가능

- inline
필요한 너비만큼 차지, 옆으로 나란히 배치 (글자취급)
width와 height를 지정 불가
margin-top/bottom 적용 불가

- inline-block
inline처럼 배치, block처럼 크기 조절 가능
옆으로 나란히 배치, width와 height, margin 값 조절가능
-> 버튼(Button), 내비게이션 메뉴 아이템을 가로로 나열할 때 가장 많이 사용

- list-item
목록 점이 있는 블록
기본적으로 block과 같지만, 앞에 목록 점이나 숫자같은 마커가 생성
-> 주로 \<li\>태그의 기본값으로 사용됨

- none
존재 자체를 지움
화면에서 아예 사라지고, 요소가 차지하던 공간조차 남지 않음
투명도 조절과는 완전히 다름



#### \# z-index
어떤걸 앞쪽에 배치할 것인지
(PPT의 맨 앞으로 가져오기, 뒤로 보내기 기능)
속성값 :
auto (기본값)
숫자 - 높을 수록 더 위에 보임
\* 반드시 position 속성이 설정되어 있어야 작동함 *



#### \# 그룹 선택자 (콤마 선택자)
태그나 선택자들을 여러 개 동시 지정할때 사용
ex)
(태그선택자 내부)
```css
#content1, #content2{

}
```



#### \# 여백 설정하기
문법 :
```css
여백명: 위 오른쪽 아래 왼쪽
```
ex)
```css
padding: 10px 10px 5px 10px;
```

padding(내부여백) / margin(외부여백)



#### \# 사진 위치 조정하기
서로 다른 성질의 요소가 있을때 (사진, 텍스트)
문법 :
```css
float: 위치
```
속성값 :
right, left 등



#### \# \<ul\>태그
- 이미지 넣기
```css
list-style-image: url(사진경로);
```
ex)
```css
ul{
	list-style-image: url(/images/mybu.gif);
}
```

- 목록표시 기호의 위치 설정
문법 :
```css
list-style-position: 속성값;
```
기본값 : outside
ex)
```css
ul.in{
	list-style-position: inside;
}
```



#### \# \<ol\>태그 숫자 스타일 바꾸기
```css
list-style-type: 속성값;
```
ex)
```css
ol{
	list-style-type: lower-roman;
}
```



#### \# (단축)속성 표기법
ex) border: 1px solid black; -> 단축 속성 (Shorthand Property) vs 개별 속성 (속성 하나하나 다 적는 것)
같은 표기법
순서대로
1) border-width : 1px
2) border-style : solid
3) border-color : black

\* 다른 속성들의 단축 속성 표기법 만들때의 순서는 W3Schools에 검색하면 나옴 (CSS Syntax 부분) *



#### \# CSS에 태그 적는 순서
무조건은 아니지만 통상적으로
공통적인 순서 먼저 적고 나중에 개별적인 태그 순서대로 적음



#### \# 폰트 스택 (font stack)
브라우저가 첫 번째 폰트를 사용할 수 없을 때 대비책으로 준비해두는 '예비군 리스트'
콤마로 연결
문법 :
```css
font-family: "폰트1", "폰트2", "폰트3";
```
ex)
font-family: "Gulim", "굴림", serif
영문 "Gulim"을 적용하라
없으면 "굴림"을 적용하라
그래도 없으면 serif라는 글꼴을 적용해라
(보통 마지막 글꼴은 일반적으로 다 존재하는 보편적인것을 적는 것이 좋음)



#### \# 줄 간격
```css
line-height: 1.6;
```
줄 간격을 1.6으로 해라



#### \# 특정한 한 부분을 작업할때
\<span\>태그를 사용하면 좋음
ex) "카카오" 글자만 작업
(CSS)
```css
#font1{
	font-family: "궁서체", serif;
	font-size: x-large; /* 옷 사이즈 처럼 폰트 사이즈로 x-large가 있음 */
	font-weight: bold; /* 폰트 굵기를 bold로 */
}
```

(\<body\>)
```html
<p>
    밀크 초콜릿은 블랙 초콜릿에 비해 카카오 함유량(최소 30%)이 적고<br>
    <span id="font1">카카오</span>가 우유와 결합했을 때 생기는
    부드러움이 특징이다.
</p>
```



#### \# 하이라이트 표시 (형광펜 표시)
background로 하면 됨
ex)
```css
#light1{
	background: #FFFF00;
}
```



#### \# 글씨 기울임 표시
```css
#font2{
	font-style: italic;
}
```



#### \# 부트스트랩은 대부분 선택자를 class선택자를 사용함



#### \# HTML에서 caps가 나오면 무조건 대소문자와 관계가 있다. (Capital letters(대문자))
- 대문자를 굵게 보여주기
```css
font-variant: small-caps;
```



#### \# JavaScript (웹 서비스 Ui&UX 교안 (P.12))
CSS가 HTML파일 내부의 \<head\>태그안에 태그 선택자인 \<style\>를 이용해서 작성한다면
JS(JavaScript)도 HTML파일 내부에 \<Script\>태그를 이용해서 작성함

- \<Script\>태그 데이터들의 기본값 : undefined
-> JavaScript에서 HTML로 데이터를 줬는데 값이 없으면 웹페이지에서 undefined로 나옴 (중요!!)

- \<Script\>태그 안에서는 Java의 주석을 입력하는 방식인 //로 주석 추가 가능

- \<Script\>태그를 여러번 작성 가능

- 객체
(중요!!) * document은 HTML문서 자체인 객체 *
1) 구성요소 : 속성(Property), 함수(Function)
Java의 맴버변수와 맴버메소드같은 것들

1-1) 속성(Property)
객체가 가지고 있는 데이터

1-2) 함수(Function)
객체가 수행할 수 있는 동작

- 변수선언문
타입이 아니고 이 변수의 이름은 이거야!라고 선언을 해주는 것
1) let (Variable: 변수)
재선언 불가, 재할당 가능
용도 : 장바구니에 담긴 상품 개수, 현재 스크롤 위치, 입력창에 타이핑 중인 텍스트 등
ex)
```javascript
let currentWatt = 20;
currentWatt = 25; // 성공 - 재할당X
```

2) const (Constant: 상수)
재선언 불가, 재할당 불가
용도 : 서비스 로고 이름, API 주소, 디자인 시스템에서 정한 고정 컬러 값 등
ex)
```javascript
const brandColor = "#FF5733"; 
brandColor = "#000000"; // 에러 - 재할당X
```

3) var (Variable: 옛날 방식) ("규칙이 느슨해서 버그를 만들기 쉬운 과거의 유물")
재선언 가능, 재할당 가능
\*요즘은 거의 사용하지 않습니다. 오래된 강의나 코드에서 보더라도 직접 쓰지는 마세요.\*

- 문자열 입력
외따옴표, 쌍따옴표 둘다 사용 가능
( ' ' ), ( " " )
ex)
```javascript
let mytitle = '자바스크립트';
```

- 객체 이용 + 변수선언문 사용 (let)
문법 :
```javascript
let 변수명 = 객체.함수명()
```
ex)
```javascript
<script>
	let output = document.getElementById("output");
</script>
```

- getElementById() 함수
1) HTML에 id선택자를 \<script\>태그 안으로 불러들여옴
2) 가져온 id선택자의 능력을 가져와서 할당된 변수가 id선택자의 데이터 값도 가지고
id선택자가 속한 태그의 객체의 속성과 함수도 사용가능하다
문법 :
```javascript
변수명.속성or함수()
```

ex)
```html
<body>
    <div id="output"></div>
    <script>
        let output = document.getElementById("output")
    </script>
</body>
```

-> document.getElementById("output")이걸로 id가 "output"인걸 가져왔는데
id가 "output"인 것은 \<div id="output"\>\</div\> 이거인데
이 안에는 보다시피 아무것도 없이 비어있음
따라서 let output의 값은 아무것도 없는 상태임
또한 let ouput은 \<div id="output"\>\</div\>의 객체의 역할을하면서 속성과 함수를 사용가능하다


- innerHTML 속성
1) 본인의 객체의 태그안의 데이터를 나타내는 속성
```html
<body>
    <div id="output"></div>
    <script>
        let output = document.getElementById("output")
        let mytitle = '자바스크립트';
        output.innerHTML += '타이틀 : ' + mytitle;
    </script>
</body>
```

-> 현재 innerHTML은 데이터 값이 하나도 존재하지 않는 상태


- \<script\>태그 안에 top-down + if 사용
1\. myname 변수에 값을 할당하지 않았을때
(JS)
```javascript
let myname ;
output.innerHTML += '이름 : ' + myname ;
```

(웹페이지)
이름 : undefined

2\. myname 변수에 값을 할당하지 않고 나중에 할당했을때
(JS)
```javascript
let myname ;

if(myname == undefined){
	output.innerHTML += '결과 : no<br>';
}else{
	output.innerHTML += '결과 : yes<br>';
}

myname = "김철수";

output.innerHTML += '이름(값할당) : ' + myname + '<br>' ;
```

(웹페이지)
결과 : no
이름(값할당) : 김철수

-> 결과값이 이렇게 됨(할당되기전이랑 할당된 후가 나뉘어짐)



#### \# 엄격한 일치 연산자 (\=\=\=)
(JS)
```javascript
let num = 1 ;
let str = "1" ;
// 암시적인 형변환이 이루어짐
output.innerHTML += '== 비교 : ' + (num == str) + '<br>';
// 형변환이 이루어지지 않고 엄격하게 타입을 나눔
output.innerHTML += '=== 비교 : ' + (num === str) + '<br>';
```

(웹페이지)(결과창)
== 비교 : true
=== 비교 : false

- \=\=뜻 : 같은... (equal to)
- \=\=\=뜻 : 같은 값과 같은 타입 (equal value and equal type)



#### \# JavaScript에서의 객체의 데이터
JS에서 중괄호가 나오면 무조건 객체임
- 객체의 데이터
문법 :
```javascript
변수선언문 객체명 = {객체에 데이터로 담길 것들};
```

(JS)
```javascript
const hong = {name: '홍길동'};
output.innerHTML += '객체의 이름 : ' + hong.name + '<br>' ;
```
(웹페이지)
객체의 데이터 : 홍길동
-> # output.innerHTML로 넣은 데이터들이 가는 곳 (중요!!)
\<body\> 안에 있는 \*\*\<div id="output"\>\</div\>\*\*라는 빈 상자 안으로 데이터들이 들어가게 됨

(풀이)
hong이라는 이름의 객체에 '홍길동'이라는 데이터를 대입했다.



#### \# JavaScript에서의 객체의 배열
JS에서 대괄호가 나오면 무조건 배열임
- 객체의 배열
문법 :
```javascript
변수선언문 배열명 = [배열에 데이터로 담길 것들];
```

(JS)
```javascript
const members = ['김철수', '이규철', '박진섭'];
output.innerHTML += '배열의 0번째 요소 : ' + members[0] + '<br>' ;
```

(웹페이지)
배열의 0번째 요소 : 김철수
-> # output.innerHTML로 넣은 데이터들이 가는 곳 (중요!!)
\<body\> 안에 있는 \*\*\<div id="output"\>\</div\>\*\*라는 빈 상자 안으로 데이터들이 들어가게 됨

(풀이)
members라는 이름의 배열에 '김철수, 이규철, 박진섭'이라는 세 가지 정보를
배열요소로서 순서대로 대입했다.



#### \# bootstrap의 행렬
행 : row
열 : col(umn)



#### \# 테이블의 \<th\>, \<td\>(행)내의 가로 정렬 변환
(CSS)
```css
.row { /* <div>태그인 class선택자인 행(row) */
	display: flex; /* 기본 정렬이 세로 정렬을 가로 정렬로 변환 */
	align-items: center; /* 세로 영역의 가운데 정렬 */
}
```
(\<body\>)
```html
<td>
	<div class="row">
		아메리카노
	</div>
</td>
```



#### \# 테이블의 \<th\>, \<td\>내의 영역 나누기
```css
.row {
	display: flex;
	align-items: center;
}
.col-4 {
	width: 30%; /* <div>태그인 row class선택자 안에 있는 */
}
.col-8 {
	width: 70%;
	display: flex;
	align-items: center;
}
```

(\<body\>)
```html
<td>
	<div class="row">
		<div class="col-4">
			<!-- 이미지를 넣을때는 꼭! alt를 생활화하기 -->
			<img class="product" src="/images/americano01.png" alt="아메리카노">
		</div>
		<div class="col-8">
			아메리카노
		</div>
	</div>
</td>
```
-> \<td\>안에 \<div\> row안에 2개의 \<div\> 입력후 CSS에 width를 이용하여 %로 각 영역을 지정함
30%영역에는 이미지 / 70%영역에는 텍스트 입력



#### \# margin: 30px auto; -> margin: 30px auto 30px auto;랑 같은 결과 값이 나옴
위부터 시작해서 시계방향으로 외부여백을 설정 (위 우 아래 좌 - 30px auto 30px auto)



#### \# 칸 나누기 선 생성, 칸 나누기 선 합치기
```css
table{ /* 데이터를 넣을 칸의 테두리가 이중선으로 바뀌어서 그걸 한개의 선으로 합치기 */
	width: 100%; /* table이 .container안에 있는데 container는 전체의 80%니가 table이 100%여도 사실상 전체이 80%임 (중요!!) */
	border-collapse: collapse; /* 기본값은 seperate */
}
table, th, td{ /* 각 데이터를 넣을 칸의 테두리 선 만들기 */ /* 질문 : 왜 th와 td의 테두리 선을 만드는걸까 행인 tr을 넣어도 되지 않을까 */
	border: 1px solid #CCCCCC;
}
```


#### \# vertical-align: middle; (세로 가운데 정렬)
세로 정렬 : vertical-align / center가 아니고 middle



#### \# border-radius: 속성값;
px
사각형의 뾰족한 부분을 둥글게 만들기 (테두리 반경)
-> 픽셀을 많이 주면 거의 원처럼 됨



#### \# 속성 선택자
태그중에 특정한 속성만 가진 것 지정
```css
태그[속성="속성값"]{.....}
```
ex)
```css
/* input 태그중 type 속성이 number인 항목들 */
input[type="number"] {
	width: 80px;
	text-align: center;
}
```



#### \# 체크박스 체크한 상태를 기본값으로 설정
```html
<input type="checkbox" checked>
```
checked사용



#### \# FlexBox Container

(실습)
```css
.col-8 {
	width: 70%;
	display: flex;
	align-items: center;
}
```

(예시01)
```css
.flex-container {
  display: flex;
  flex-direction: row;
}
```
왼쪽 정렬 / 행 나열

(예시02)
```css
.flex-container {
  display: flex;
  flex-direction: column;
}
```
왼쪽 정렬 / 열 나열

(예시03)
```css
.flex-container {
  display: flex;
  flex-direction: row-reverse;
}
```
오른쪽 정렬 / 행 나열 (순서 반대)

(예시04)
```css
.flex-container {
  display: flex;
  flex-direction: column-reverse;
}
```
왼쪽 정렬 / 열 나열 (순서 반대)

(예시05)
```css
.flex-container {
  display: flex;
  justify-content: center;
}
```
중앙 정렬 / 행 나열



#### \# pseudo 클래스 (선택자의 일종)
선택자에 추가되어 특별한 상태를 뜻하게 하는 키워드 (콜론 사용)
문법 :
```css
태그:pseudo클래스 {.....}
```
- 종류
hover : 마우스가 요소 위에 있을때
focus - When an element has focus
active - 요소가 작동되었을때
link : 방문하지 않은 링크
visited : 방문한 링크



#### \# hover효과
ex)
```css
/* 가상(pseudo) 클래스 */
tr:hover { /* tr 택에 마우스가 영역 안으로 들어 오면 ... */
	background-color: #f5f5f5; /* hover 효과 */
}
```



#### \# first-child
태그안의 처음있는? 태그
ex)
```html
<thead>
	<tr>
		<th>아이디</th>
		<th>상품명</th>
		<th>단가</th>
	</tr>
</thead>
```

\<thead\>태그의 first-child : \<tr\>
\<thead\>태그의 last-child : \<th\>



#### \# Bootstrap (부트스트랩)
HTML, CSS, JS의 프레임워크

- responsive (반응형)
장치의 크기에 따라 화면을 다르게 보여준다
ex) 장치의 크기가 달라지면 메뉴가 보이거나 메뉴가 없어지고 메뉴버튼이 생성되거나

- 모바일이 우선인 프레임워크
웹도 있지만...

- CDN (Content Delivery Network)
연결방식
거리가 멀면 소스코드를 다운로드 받는 게 느림
따라서 똑같은 소스코드의 복제본을 전세계에 퍼트려 놓고
가장 가까운 곳에서 유저가 소스코드를 가져올 수 있게 하기

장점 : 프레임워크가 실시간으로 업데이트 되면 가장 최신의 소스코드를 받을 수 있음
단점 : 인터넷이 안되면 사용 불가

링크를 이용해서 그대로 사용 가능
직접 프레임워크를 다운받아서 사용도 가능

사용법 : HTML파일의 \<head\>태그에 \<link href부분을 복붙하기
CSS는 link href ~ .css
JS는 script src ~ .js
\* 프레임워크 한개에 소스코드들이 다 들어있으니까 W3Schools의 한개마다 프레임워크를 중복해서 넣을 필요 없음 *



#### \# grid 개념
- 개념 :
영역을 가지는 (넓이, 높이 조절이 가능한) block element들만 가지는 개념
영역을 행(row)과 열(column)쪼개는 것
행(row)는 무제한으로 쪼갤 수 있지만
열(column)은 최대 12개로 제한함 (12개 이하도 가능)
(12컬럼인 이유는 이 숫자가 가장 쪼개기 편리한 숫자여서 + 역사적 이유)

- 사용법
ex) 한 영역에 사진과 텍스트를 동시에 넣을때

- 실습
ex)
(CSS)
```css
.row { /* 행 class */
	display: flex; /* 가로 정렬로 변환 */
}
.col-4 { /* col(umn)을 4로 */
	width: 30%; /* row행 내부의 영역의 30%사용 - 30%가 대략 4임 */
}
.col-8 { /* col(umn)을 8로 */
	width: 70%; /* row행 내부의 영역의 70%사용 - 70%가 대략 8임 */
}
```

(HTML)
```html
<td>
	<div class="row"> <!-- 가로 정렬로 변환된 row(행)인 영역 <div> -->
		<div class="col-4"> <!-- col(umn)을 4인 영역에는 이미지 삽입 -->
			<img class="product" src="/images/americano01.png" alt="아메리카노">
		</div>
		<div class="col-8"> <!-- col(umn)을 8인 영역에는 텍스트 삽입 -->
			아메리카노
		</div>
	</div>
</td>
```

- 예외사항
만약 영역을 나누었을때 1 / 9로 나누면 10이여서 12가 안되는 경우
남은 2컬럼 영역은 빈칸이 됨
왼쪽부터 순서대로 영역이 배치되어서 1 / 9 / 남은2영역이 됨



#### \# \<form\>태그 사용 (입력 양식을 만들때 사용)
- 개념 :
table이 표를 만드는 것이라면 / form은 사용자가 입력할 양식을 만드는 것
라벨(label)과 입력상자(input-area)의 조합

- label과 input-area
사실상 label과 input-area라는 클래스의 이름은 개발자들끼리의 약속이기에
이름을 바꿔도 상관없음
but! label이 클래스 이름이 아니고 \<label\>이라면 이 태그 안에 input이 있고
input안에 있는 것을 조작해야 한다라고 미리 알려주는 느낌의 태그가 됨

- input태그의 속성들
1) \<form\>\</form\>
폼 양식의 시작과 끝

2) \<input type="text"\> : 한 줄 입력 상자
3) \<input type="password"\> : *로 표시되는 암호 입력 상자
4) \<input type="radio"\> : 라디오 버튼
5) \<input type="checkbox"\> : 체크 상자
ex)
```html
<th style="font-size: 1.2rem;">
	<input type="checkbox"> 전체 선택
</th>
```
-> "전체 선택" 텍스트 앞에! 체크박스가 생김

6) \<input type="button"\> : 일반 버튼
6-1) \<button\>태그와의 차이점
input type="button"은 value=""로 속성을 넣고 오직 텍스트만 넣을 수 있음
\<button\>태그는 태그 안에 텍스트를 넣고 이미지나 다른 태그들을 넣을 수 있음
-> 요즘은 \<button\>태그를 더 많이 사용함
(\<button\>태그도 \<form\>태그 안에 사용 가능)

7) \<input type="number"\> : 숫자 입력 상자
ex) \<input type="number" value="1" min="1"\>
value : 기본으로 적혀 있는 값
min : 최소값이 1

- 영역 쪼개기
table에서 grid영역을 쪼갠것과 동일함

- placeholder (input)속성
어떤 걸 사용자가 입력할지에 대한 일종의 가이드라인
아무것도 입력하지 않았을때 나오는 글씨



#### \# 콤보 박스(ComboBox) (The \<select\> Element이 정석 이름)
옵션 선택하는 박스
- 개념
select태그 : 부모
option태그 : 자식

가장 첫번째 옵션이 기본으로 보임 (placeholder처럼)

ex)
```html
<select id="category" name="category">
	<option value="bread">빵</option>
	<option value="beverage">음료수</option>
	<option value="cake">케이크</option>
	<option value="macaron">마카롱</option>
</select>
```



#### \# 버튼 설명 (양식(form)안에 있어야 양식 안에 있는 데이터들을 이용해서 버튼들이 정상작동함) (중요!!)
\* type을 적지 않을시 type="submit"이 기본값임

```html
<button type="submit" class="btn">상품 등록</button>
```
-> 제출 버튼 -> 나중에 제출 받을 곳을 지정해주면 그곳으로 form안에 입력한 데이터들이 날아감

```html
<button type="button" class="btn">그냥 등록</button>
```
-> 진짜 그냥 버튼

```html
<button type="reset" class="btn">리셋 등록</button>
```
-> 진짜 리셋 버튼 (입력한 양식(form)안의 데이터 리셋)



#### \# label for의 사용
for속성은 label과 output태그만 사용 가능!
- 개념 :
1) \<label for="ABC"\>라는 코드를 읽으면,
페이지 전체를 뒤져서 id="ABC"를 가진 요소를 찾음

2) 찾게 되면 두 요소(\<label\>태그와 id="ABC")는 논리적으로 하나로 묶임
사용자가 \<label\>을 클릭하는 행위는 곧 id="ABC"인 입력을 클릭하는 것과 같은 효과를 냄

ex)
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

(풀이)
-> \<label\>태그의 영역을 클릭하면 for="name"때문에
id="name"인 영역을 클릭한 것과 같은 효과를 냄



#### \# JS의 배열 (배열요소(원소)에 다중속성 넣기)
문법 :
```javascript
변수선언문 배열명 = [
	{0번 배열 요소의 속성들}
	{0번 배열 요소의 속성들}
]
```
ex)
```html
<script>
    // 상품_목록
    const products = [ // products배열
	    // 원소 하나 생성
      { id:1, name:'아메리카노', price:4000, image:'/images/americano01.png'}
    ];
</script>
```
- 배열요소(원소)들은 객체로 사용됨
ex)
products\[0\].id는 1임



#### \# JS의 객체 (객체에 다중속성 넣기)
세미콜론 사용하지 말기!
문법 :
```javascript
변수선언문 객체명 = {
	객체의 속성
	객체의 속성
}
```
ex)
```javascript
/* 사용자 정보 */
const user = {
  role: 'ADMIN' // USER, ADMIN
}
```
- 객체로 속성이나 함수를 사용함
ex)
user.role은 'ADMIN'



#### \# role 속성
- 개념 :
사실 내가 그렇게 이름을 정한거지 name: 과 별 다를바 없이 특별한 자체 기능은 없고
그냥 관례적으로 role이라고 적은 것

- 역할 정의 :
시스템 내에서 허용된 행동의 범위를 결정함

- 권한 제어
예를 들어, 게시글을 지우거나 사용자 목록을 볼 수 있는 권한은
role: 'ADMIN'인 사용자에게만 주도록 로직을 짤 수 있음.
-> 로직을 짜기 전까지는 name과 같이 특별한 기능이 없는 그냥 이름임



#### \# 관리자 전용 버튼이 관리자한테만 보이게 설정하기
- role에 로직 더하기 : role이 ADMIN일때만 "관리자 전용 버튼"이 보이게 설정
\* bootstrap의 경우 container라고 class명을 붙여야 레이아웃을 맞춰줌 *
ex)
```html
<div class="container my-4"></div>

```

1) 관리자 전용 버튼 생성
```html
<div class="d-flex justify-content-start">
	<a href="/product/insert"> <!-- "/product/insert"으로 이동한다. -->
		<!-- 링크로 이동하는 버튼 생성 -->
	  <button id="insertBtn" class="btn btn-primary mb-3">상품 등록</button>
	</a>
</div>
```

2) if문 사용
(JS)
```javascript
/* 사용자 정보 */
const user = {
	role: 'ADMIN' // USER, ADMIN
}

if(user.role !== 'ADMIN'){
  // 화면에서 안보이고, 실제 공간도 없어짐
  document.getElementById("insertBtn").style.display = "none";
}
```
-> document는 기본 객체(HTML의 객체)
-> getElementById("insertBtn")가 사실상 \<button id="insertBtn"\> 버튼을 의미함
-> document.getElementById("insertBtn")로 \<button\>태그라는 객체를 가져왔으니
\<button\>이라는 객체의 속성인 style을 사용하고 그 style의 CSS속성인 display를 또 가져온 것
-> 사실상 <button style="display: none";></button>과 같은 효과 (중요!!)
따라서 웹페이지 상에서 button이 사라짐



#### \# Template Strings (템플릿 스트링)
Java의 printf와 같이 포맷형 문자열을 사용하여 결합하는 것

- 문자열이 아닌 형태를 포맷형 문자열로 바꾸기
문법 : \` \`(백틱-Backtick) / $ / {} 이용하기
```
`${.....}`
```
ex)
(JS)
```javascript
let firstName = "John";
let lastName = "Doe";
let text = `Welcome ${firstName}, ${lastName}!`;
```

(웹페이지)
Welcome John, Doe!



#### \# 함수 생성 방법
보통 함수는 재할당하지 않으므로 변수선언문 const를 많이 사용함
(JS)
```javascript
변수선언문 함수명 = function(매개변수){수행할 동작};
```



#### \# Arrow Functions (=>) (화살표 함수) (예시가 너무 다양하지만 기본만 공부하기)
기존 함수의 문법을 약식으로 바꾼 새로운 문법
ex)
기존 함수 생성 방법
```javascript
const multiply = function(a, b) {return a * b}
```
-> 함수명 : multiply / 매개변수 : a, b / 반환타입 : a * b의 타입

약식 함수 생성 방법 (return반환값이 있을때)
```javascript
const multiply = (a, b) => a * b;
```
-> 함수명 : multiply / 매개변수 : a, b / a * b의 타입

약식 함수 생성 방법 (return반환값이 이름 없는 객체일때)
```javascript
const multiply = (a, b) =>({ id: 1 }); // 꼭! 소괄호 사용
```
-> 함수명 : multiply / 매개변수 : a, b / {id: 1}라는 객체 반환

약식 함수 생성 방법 (return반환값이 이름 있는 객체일때)
```javascript
const multiply = (a, b) => 객체명;
```
-> 함수명 : multiply / 매개변수 : a, b / 객체명 : 객체명을 써서 바로 반환

약식 함수 생성 방법 (return반환값이 없을때)
```javascript
const multiply = (a, b) => {수행할 동작};
```
-> 함수명 : multiply / 매개변수 : a, b / {} : 수행할 동작

\* {id: 1}은 속성id가 속성값1을 가진 "객체"!이고
id: 1은 그냥 객체가 가진 속성과 속성값을 나타내는 것임



#### \# 상품 배열을 반복하여 목록 생성하기 (JS의 forEach 이용)
- forEach함수
JS의 forEach함수는 Java의 향상된 for구문과 비슷한 느낌
원소 각각을 개별적으로 동작시켜서 결과값을 추출한다.



#### \# console객체
기본으로 제공되는 객체
log()함수 : 브라우저의 console창에 출력하는 기능

- 문법 :
```javascript
배열명.forEach( (지역변수명, 인덱스) => {
    // 각 요소마다 실행할 코드 
} );
```
-> 인덱스를 이용해서 지금 forEach에 돌아가고 있는 배열 원소를 알 수 있음

ex) if문 사용해서
```javascript
if (index === 1) {
	console.log(`찾았다! ${index}번에 있는 ${product}`);
}
```
이런식으로 특정 인덱스인 배열 원소한테는 특정한 동작을 따로 시킬 수 있음

- 기본 형태 예시
ex) products라는 배열이 있다는 전제하에
```javascript
products.forEach(item => {
	console.log(item.name);
})
```

- item.name 풀이
item은 products배열에 담긴 원소이고
그 원소가 가진 속성인 name을 가져오는 것



#### \# JS내에서 HTML영역에 element(태그들의 합)만들기 (createElement()함수 활용)
createElement : 자바 스크립트로 태그를 동적으로 생성
문법 :
```javascript
변수선언문 객체명 = document.createElement("태그명");
```
ex)
```javascript
const col = document.createElement("div")
```
-> JS상에서 col이라는 객체 생성과 동시에
JS상의 col객체와 동일시 되는 HTML에서 눈에 보이지 않는 \<div\> 태그를 생성함 (중요!!)
-> col객체의 속성에 데이터 값을 넣으면 그에 해당하는
HTML의 \<div\>태그에 동일한 값이 들어감



#### \# JS내에서 동적으로 만든 element이용
1) JS객체를 이용한  HTML상의 태그의 class지정
ex) col.className = "col-md-4 mb-4";
-> col(\<div\>태그인)에게 class이름을 "col-md-4 mb-4"라고 부여함

2) JS객체를 이용한  HTML상의 태그의 데이터 값 지정
```javascript
// 결합할게 없고 줄바꿈이 없어서 굳이 ` `(백틱)을 쓸 필요는 없음
col.innerHTML = ${item.name};
```
-> 눈에 안보이는 HTML상의 \<div\>태그 안에 \`${item.name}\` 값이 들어감

3) JS객체를 이용한 부모객체 안에 자식객체로 넣기
(JS)
3-1) 부모태그를 가져옴
```javascript
const container = document.getElementById("productContainer");
```

3-2) 부모객체 안에 자식객체로 넣기 (appendChild()함수이용)
container.appendChild(col)
-> HTML상에서 id가 productContainer인 태그 안에
col객체인 class이름이 col-md-4 mb-4인 \<div\>태그가 들어감

(HTML상에서) (눈에는 \<div class="col-md-4 mb-4"\>\</div\>이 안보이지만)
```html
<div class="row" id="productContainer">
	<div class="col-md-4 mb-4"></div>
</div>
```



#### \# append : 무리가 있는데 그 무리 제일 뒤쪽에 하나 추가하는 행위



#### \# node : 태그의 프로그래밍적 이름 (간단히 알아만 두기)
- 개념 :
\<div\>나 \<h1\>를 태그라고 부르지만,
자바스크립트 입장에서 이들을 조작 가능한 \*\*객체(Object)\*\*로 취급함
그래서 이를 \*\*노드(Node)\*\*라고 부르는 거임

- 특징
태그뿐만 아니라 그 안에 들어가는 글자(Text), 주석 등도
전부 넓은 의미의 노드에 포함됨.



#### \# create : 생성
메모리 상에 새로운 노드를 탄생시키는 것



#### \# 이벤트 (event)
브라우저에서 발생하는 사건들
ex) 키보드 누르기, 마우스 클릭, 스크롤, 페이지 전환 등

- Event Driven Programming
특정 이벤트에 따라서 실행 코드를 작성하는 기술을 의미

- Event 이름(Event Type)
ex) click, load, unload 등

- Event 속성
on + 이벤트 이름
ex) on + click

- 이벤트 핸들러 (Event Handler)
이벤트 속성에 할당이 되어 있는 함수
\[어떤 어떠한 이벤트가 발생하면… ~해라.\] 라는 식으로 해석



#### \# on 이벤트 핸들러 속성 (이벤트 속성)
(on+이벤트) 조합으로 사용하는 속성
ex)
```html
<div class="d-flex justify-content-start">
	<a href="/product/insert">
		<button id="insertBtn" onclick="register()" class="btn btn-primary mb-3">상품 등록</button>
	</a>
</div>
```
-> 속성 : onclick : 클릭을 할때
-> 속성값 : "register()" : register() 함수를 실행해라

\* 숫자도 쌍따옴표 붙어야 함 *



#### \# 파라미터 (Parameter)
- 개념 :
정확히는 Query Parameter (쿼리 파라미터)가 맞음
사용자가 서버에게 파라미터를 보내면서 이 파라미터(조건)에 맞는 데이터를 가져와!라고 함
ex) 아이디랑 비밀번호 입력창에 hong과 hello를 입력하면 다음페이지로 넘어가면서
파라미터값은 username=hong&password=hello 이 됨

- 시작점 : ?
- 파라미터간의 구분자 : &
-> 따라서 파라미터의 수는 구분자의 수 +1과 같다.

- 문법 :
```javascript
파라미터_이름=파라미터_값
name=value
```
ex)
```javascript
password=hello
```


#### \# 전송방식 (method)
- 명칭 :
정확히는 HTTP 요청 메서드(HTTP Request Method)
혹은 HTTP 메서드가 맞음
\* http : 프로토콜 (2매체가 통신을 하기 위한 통신 규약) *

- 개념 :
브라우저(Client)\*\*가 \*\*서버(Server)\*\*에게 데이터를 보낼 때의 규칙
웹 브라우저(사용자)가 웹 서버(URL 주소)에 사용자가 입력한 데이터(파라미터)를
GET 또는 POST라는 \*\*봉투(규격)\*\*에 담아서 보낼 때의 규칙

- 종류 :
1) get
- 보내는 곳 : http의 head 부분
단점 : 내용을 다 볼 수 있음 (보안 취약) -> username이랑 password가 주소창에 다 보임
ex) http://localhost:63342/login?username=hong&password=hello

2) post
- 보내는 곳 : http의 body 부분
장점 : 내용을 주소창에서 볼 수 없음 (보안 유리)
ex) http://localhost:63342/login



#### \# window 객체
JS에서의 최상위 객체 (Java의 object같은 느낌)
document, location, history, navigator, screen 등 모두를 담고있음

자바스크립트 규칙상 window 객체의 자식들은 window.를 떼고
속성(자식)만 불러도 브라우저가 알아서 알아들음
-> 따라서 window.location가 아니고 location이 맞음



#### \# location 객체
'주소창'이라는 정보를 통째로 담고 있는 객체(도구 상자)



#### \# href 속성
Setter(설정자)'라는 특별한 기능을 가진 속성
->Setter속성을 가진 객채들은 값을 넣는 행위 자체가 실행 버튼임

(중요!!!)
따라서 location.href가 함수가 아님에도
값을 처음 넣거나 값을 변경하면 실행이 됨
ex)
```javascript
function goDetail(id){
	//alert('상세 페이지 이동 :' + id);
	location.href = `ProductDetailNew.html?id=${id}`;
}
```
-> 여기서 location.href이 함수가 아님에도
`ProductDetailNew.html?id=${id}` 이곳으로 이동하게 됨



#### \# 파싱(Parsing)
브라우저나 프로그램이 어떤 글자 뭉치(데이터)를 읽어서 그 구조와 의미를 해석하는 과정
- 웹 브라우저에서의 파싱 (HTML 파싱)
한 줄씩 읽으면서 해석 (top-down방식)



#### \# DOMContentLoaded
HTML문서는 원래 top-down방식인데
순서를 비트는 구문
HTML문서가 다 읽혀지고나서 동작하라는 구문
정확히는 "HTML 문서의 모든 태그(DOM)를 다 읽어서 메모리에 올렸을 때"

만약 사용할 구문에 필요한 변수나 객체같은게 구문보다 아래에 있으면 원래는 오류가 나는데
사용할 구문에 DOMContentLoaded를 넣게되면 가장 나중에 동작하기에 오류가 나지 않음



#### \# addEventListener()함수
이벤트 리스너 등록 함수
특정 이벤트가 일어나면 특정 동작을 실행하는 함수

문법 :
대상.addEventListener("이벤트종류", 실행할함수, \[옵션\]);
옵션은 생략가능

ex)
```html
<script>
	document.addEventListener("DOMContentLoaded", function () {...});
</script>
```

- 풀이
document(HTML)의 모든 내용을 읽었을때(이벤트 발생) function을 실행해라



#### \# Dummy data
정식 데이터가 아니고 한시적으로 만든 데이터



#### \# window.location.search
window라는 최상위 객체의
location(주소창)의 search(파라미터영역)를 지칭하는 구문



#### \# URLSearchParams
쿼리 문자열(파라미터 목록)을 key-value 형태로 분리해주는 함수
-> 분리해서 몇개의 파라미터가 있는지 알려줌
-> 어떤 파라미터가 어떤 값으로 들어있는지는 안알려줌

생성 문법 :
```javascript
변수선언문 객체명 = new연산자 URLSearchParams(분석할문자열);
```
ex)
```javascript
const params = new URLSearchParams(window.location.search);
```
params이라는 객체에 window.location.search의 파라미터목록을 분리하는 함수의 값을 넣는다
-> 주소창의 파라미터영역을 가져와서 URLSearchParams함수로 파라미터목록을 분리하고
그 분리된 값을 params이라는 객체에 넣는다.

- 파라미터 목록 확인해보기
```javascript
console.log('파라미터 리스트');
console.log(params);
```
(결과)
size: 2

(풀이)
이 주소창 안에는 서로 다른 파라미터(정보 덩어리)가 2세트 들어있다



#### \# 웹페이지 속성 개념
웹페이지는 무조건 대소문자를 구별함
주소창에 적힌 것은 무조건!! 문자열(String)임



#### \# get() 함수
문법 :
```javascript
객체.get("가져올객체의속성)
```
ex)
```javascript
params.get("id")
```
params이라는 객체가 가진 속성 중에서 id라는 속성의 값을 가져와라
-> params.get("id")은 파라미터 중에서 id의 값을 가지게 됨 (문자열 데이터임)



#### \# Number()함수
숫자로 바꿔주는 함수 (정수든 실수든 상관없이 그냥 숫자)
문법 :
```javascript
Number("바꿀데이터")
```



#### \# find() 함수
배열(Array)객체에서 내가 원하는 조건에 딱 맞는 데이터 하나만 찾아내는 함수

- 동작 원리
배열의 첫 번째 칸부터 마지막 칸까지 순서대로 훑으면서,
내가 정한 조건이 참(true)인 원소를 발견해서 가져옴

- 문법 :
```javascript
변수선언문 객체명 = 배열.find(요소 => 조건식);
```
ex)
```javascript
const product = products.find(item => item.id === productId);
```
(풀이)
products배열에서 item원소를 살펴보는데 item.id === productId인 값이 있으면
그 값을 가져와서 product객체에 넣어라



#### \# URLSearchParams로 가져온 파라미터 목록의 내용 확인하기
- const productId = Number(params.get("id"));
params객체가 가진 파라미터 목록인 속성에서 id속성을 가져와서 숫자로 바꾸고
그 값을 productId라는 객체에 넣어라
-> 파라미터 목록에 어떤 속성이 있는지는 모르지만
-> 어떤 속성이 있는지 안다면 이렇게 속성값을 확인 할 수 있음
\* 상세페이지이기 때문에 사용자는 이미 상품을 골라서 상세페이지에 들어온 상태여서
id값이 파라미터 목록에 존재하는거임 *



#### \# 확인한 파라미터 목록에 있는 속성의 속성값 이용하기
- const product = products.find(item => item.id === productId);
products배열의 원소를 살펴보다가
만약 사용자가 선택한 그 상품이자 파라미터 목록에 들어있는 id와
동일한 id속성을 가진 배열안에 들어 있는 원소를 찾으면
그 원소를 가져와서 product객체에 넣어라

-> 그 후 if조건식으로 이에 맞는 상품페이지를 만들고 이 전체 스크립트를
```html
<script>
	document.addEventListener("DOMContentLoaded", function () {...});
</script>
```
이렇게 감싸면 오류가 발생하지 않음



#### \# 라이브러리(Library) vs 프레임워크(Framework)
필요할 때 가져다 쓰는 도구 모음 vs 정해진 틀(template)안에 코드를 넣어 사용하는 구조
개발자가 직접 코드의 흐름 제어 vs 프레임워크가 전체 흐름 제어
필요한 기능만 골라서 호출(Call)해서 사용 vs 정해진 규칙에 따라 코드를 끼워 넣음
독립적으로 사용 가능 vs 구조가 이미 만들어져 있음



#### \# jQuery의 상위 개념?이 JS임
- 개념
JS의 라이브러리(Library)
기존의 CSS, 특히 선택자하고 JS하고 같이 묶어서 코딩하는 것을
집대성해서 라이브러리 형태로 만들어 놓은것
\* 요즘은 당연히 사용 할 줄 알아야 함 *

- 부트스트랩과의 관계
부트스트랩의 전제가 jQuery의 존재라서
부트스트랩을 쓴다면 jQuery도 같이 라이브러리 로드 링크를 적어주는 것이 좋다

- 사용법
1) jQuery 라이브러리 로드 링크를 \<head\>에 입력
```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
```

2) jQuery에 맞는 문법 도구들을 사용하여 코드 입력
$ 기호는 jQuery를 부르는 기호
ex)
표준 자바스크립트 (Vanilla JS) :
```javascript
document.addEventListener("DOMContentLoaded", ...)
```
jQuery 방식 :
```javascript
$(function() { ... });
```




#### \# transition 속성
주어진 기간안에 속성값을 바꾸는 것
ex) transition 값이 0.3s라면 특정 값으로 0.3초후에 변화
(변화하는 과정을 0.3초간 보여줌)



#### \# Pseudo-classes
기존 선택자 뒤에 콜론(:)을 붙이고 가상 클래스 이름을 적습니다.

- 문법 :
(CSS)
```css
선택자:가상클래스 {
  속성: 속성값;
}
```

- 종류들
1) 반응형
:hover	요소에 마우스를 올렸을 때	버튼 색상 변경, 메뉴 펼치기
:active	요소를 클릭하고 있는 동안	버튼이 눌리는 효과
:focus	    요소에 포커스가 갔을 때 (입력창 등)	input 테두리 강조
:visited	사용자가 이미 방문한 링크일 때	읽은 글 표시

2) 구조적
:link - Unvisited links
:nth-child(n)	부모 안에서 n번째 자식일 때	표(table)의 짝수 줄 색칠하기
:first-child	첫 번째 자식 요소일 때	목록의 첫 항목 테두리 제거
:last-child	마지막 자식 요소일 때	목록의 마지막 구분선 제거



#### \# 클릭해서 변하는 토글 생성하기 (중요!!!!!)(jQuery 이용)
- $(function() { ... });
HTML)의 모든 내용을 읽고나서 function을 실행하라는 동작

- $("")
""안에 CSS에 선택자 넣는 것처럼 선택자를 심볼과 함께 넣으면 됨
ex) $("#grayImg")
-> id가 grayImg인 태그를 의미함! (중요!!)

- $("").click(function(){});
선택자가 ""인 태그가 click될때 function의 {}을 실행해라

- $(this)
this는 부모의 것과 같은 선택자
그 선택자인 태그를 의미함!
ex) $(this)

- toggleClass("");
""라는 이름의 Class를 추가해라
ex) $(this).toggleClass("gray");
부모 선택자인 태그안에 class="gray"를 토글형식으로 추가/삭제해라



#### \# 활성화 되는 것을 표현
```html
<style>
	/* 특정 항목이 활성화 되었을 때 테두리를 파랗게 표현하기 */
	.active{border: 2px solid blue;}
</style>
```

.active 클래스는 개발자들 끼리의 약속이여서 사실상 이름은 바꿔도 상관없음



#### \# 이미 활성화된 것을 비활성화 시키고 다시 선택한 것을 활성화 시키기(jQuery 이용)
- addClass("")
클래스 추가

- removeClass("")
클래스 삭제

(선생님이 만든 코드)
```javascript
$(".select-img").click(function (){
	$(".select-img").removeClass("active");
	$(this).addClass("active");
});
```
-> $(".select-img")인 모든 애들 삭제함 (이 파일에서는 3개의 파일을 다 확인해야함)

(내가 만든 코드)
```javascript
$(".select-img").click(function (){
	$(".active").removeClass("active");
	$(this).addClass("active");
});
```
-> $(".active")인 친구를 하나만 확인하면 되는거여서 더 최적화된 코드임



#### \# 콤보박스 만들기(jQuery 이용)
click(){}을 사용해도 되지만
change(){}를 사용하는게 좋음 (항목이 바뀌었다는 의미에서)
이런 함수를 이벤트라고 부름
click이벤트
change이벤트 : 값이 바뀌면 동작 실행
- 실습
```javascript
$("#categorySelect").change(function (){
	const selected = $(this).val();
	console.log(`선택 항목 : ${selected}`);
});
```

(풀이)
categorySelect라는 이름의 id선택자가 있는 태그가 변하면 기본값이 value="all" 이거임
categorySelect라는 이름의 id선택자가 있는 태그의 value값을 selected객체에 넣고
선택 항목 : ${selected}를 콘솔에서 보여줘라

\* change이벤트가 바뀌는 주체를 자동으로 인식하는 이유는 select태그의 값이
option value라는 것으로 정해져 있기 때문에 *



#### \# 콤보박스로 카테고리 별 제품들만 보여주기(jQuery 이용)
- show() 이벤트
해당 객체를 보여주는 이벤트

- hide() 이벤트
해당 객체를 숨겨주는 이벤트

- 속성 선택자를 사용해서 필터링해서 특정 값을 찾아내기
특정 클래스의 data-category의 값이 특정 값인 것들만 찾으면 됨 (중요함!!!)
선택자뒤에 대괄호를 넣으면 필터링이 가능함

1) 문법 :
```css
.선택자[필터링할내용]
```

2) 이용하기) 클래스가 combo-image인 것들 중에서 / data-category라는 속성이 있는데
/ 그 값이 특정값인 것을 찾기
ex)
```javascript
$(".combo-image[data-category='" + selected + "']").show();
```
.combo-image라는 이름의 클래스가 가진 data-category속성 값이
selected변수값과 동일한 태그를 의미함

\*\*\*\* (풀이과정) (중요함!!!!!) \*\*\*\*
전제 : $의 소괄호인 ()안에는 꼭! 따옴표가 들어가야할 필요는 없고 문자열 데이터만 들어가면 됨!

```javascript
$(".combo-image[data-category='" + selected + "']");
```

1\. $() 안에 있는 내용을 나누어 생각하기
1) 문자열로 변환됨 (양 끝 쌍따옴표 없어짐)
```
".combo-image[data-category='"
-> .combo-image[data-category='
```

2) +

3) selected변수가 가진 문자열 값인 all로 바뀜 -> all
```
selected
```

4) +

5) 문자열로 변환됨 (양 끝 쌍따옴표 없어짐)
```
"']"
-> ']
```

2\. 문자열로 변환된 각 내용들이 결합 연산자로 합쳐지게 됨
```
.combo-image[data-category=' + all + ']
-> .combo-image[data-category='all']
```


\* 중요 포인트 : 원래 처음에는 외따옴표가 서로 다른 쌍따옴표의 영역에 들어가 있기 때문에 쌍으로 연결 되지 않아서 사실상 외따옴표 역할을 하지 않는 그냥 문자의 역할을 했지만 전체 구문이 문자열로 바뀌고 결합연산자로 연결되면서 드디어 제 역할을 하는 외따옴표 쌍이 완성되었음!!!!!*

마지막 완성된 문장을 봐도 사실상 외따옴표가 필요하지는 않을 것 같지만 ('all'이나 all이나 같으니까)
만약 외따옴표가 없는 상태에서 변수가 가진 문자열 값이 공백을 포함하고 있는 inner peace같은 문자열 데이터면
```
.combo-image[data-category=inner peace]
```
이런식으로 나오게 되는데

이러면 에러가 발생할 수 있기 때문에 변수가 공백이 있는 문자열 값을 가지고 있어도 에러가 나지 않게 하려고 외따옴표를 굳이 붙여서
```
.combo-image[data-category='inner peace']
```
이렇게 만들어서 마지막으로 한번 더 문자열로 만들어주는 것이다.

\* 중요 포인트!!!! 외따옴표의 신분변화 (일반 의미없는 기호 -> 외따옴표 역할하는 특별한 기호) *

(전체 실습)
```javascript
$("#categorySelect").change(function () {
	const selected = $(this).val(); // 선택한 품목명
	console.log(`선택 항목 : ${selected}`);

	if (selected === "all") {
		$(".combo-image").show();
	} else {
		$(".combo-image").hide();
		$(".combo-image[data-category='" + selected + "']").show();
	}
});
```



#### \# jQuery의 선택자들 몇개
- 끝이 .jpg인 것들만 가져오기
문법 :
```javascript
[속성명$=속성값]
```
ex01)특정 속성에 특정 속성값을 가진 모든 것
```javascript
$("[href$='.jpg']")
```
ex02)특정 태그의 특정 속성에 특정 속성값을 가진 모든 것
```javascript
$("태그명[속성명$='속성값']")
$("a[href$='.jpg']")
```
-> a태그의 href속성의 속성값이 .jpg로 끝나는 것

- 시작이 "Tom"인 것들만 가져오기
문법 :
```javascript
[속성명$=속성값]
```
ex01)특정 속성에 특정 속성값을 가진 모든 것
```javascript
$("[title^='Tom']")
```
ex02)특정 태그의 특정 속성에 특정 속성값을 가진 모든 것
```javascript
$("태그명[속성명^='속성값']")
$("div[title^='Tom']")
```
-> div태그의 title속성의 속성값이 'Tom'으로 시작하는 것



#### \# 사진 크기 변할때 기준점 잡기 (transform-origin 속성 사용)
사진의 크기가 변해도 사진의 기준점을 정해서
그 기준점에서 움직이지 않고 그 기준점을 기준으로 사진의 크기가 변함

(CSS)
```css
#mainImage{
	width: 100%;
	height: 300px;
	max-width: 500px;
	transition: transform 0.3s ease;
	transform-origin: top left;
}

#mainImage:hover{
	transform: scale(1.1);
}
```



#### \# attr() 함수 (jQuery이용)
객체의 속성값을 가져오거나 변경하는 함수
1) 값을 가져올 때 (getter)
문법 :
```javascript
객체명.attr("속성명");
```
ex)
```javascript
$(this).attr("src");
```

2) 값을 변경할 때 (setter)
문법:
```javascript
객체명.attr("속성명", 변경할속성값);
```
ex)
```javascript
$("#mainImage").attr("src", newSrc);
```



#### \# 부모태그와 자식태그 필터링
문법 :
```javascript
$("부모선택자 자식선택자")
```
-> 부모선택자 중에서 자식선택자인 태그만 가져오기
ex)
```javascript
$("#rotateBox img")
```
-> id가 \#rotateBox인 태그중에서 img태그인 태그들 가져오기



#### \# last()함수
가장 마지막 순서의 태그 가져오기
```javascript
$("선택자").last()
```
->선택자인 태그중에서 가장 마지막 태그를 가져와라
ex)
```javascript
$("#rotateBox img").last();
```
-> id가 \#rotateBox인 태그중에서 img태그인 태그중 가장 마지막 태그를 가져와라



#### \# first()함수
가장 첫번째 순서의 태그 가져오기
```javascript
$("선택자").first()
```
->선택자인 태그중에서 가장 첫번째 태그를 가져와라
ex)
```javascript
$("#rotateBox img").first();
```
-> id가 \#rotateBox인 태그중에서 img태그인 태그중 가장 첫번째 태그를 가져와라



#### \# append()함수와 prepend()함수
- append()
제일 뒤에 넣기
ex)
```javascript
const first = $("#rotateBox img").first();
$("#rotateBox").append(first);
```

- prepend()
제일 앞에 넣기
ex)
```javascript
const last = $("#rotateBox img").last();
$("#rotateBox").prepend(last);
```



#### \# input의 type속성의 radio 속성값
한개의 그룹안에 있는 여러 개중에서 한개를 선택할때
한개의 그룹으로 지정하는 기준 : name속성값이 같으면 한개의 그룹임 (그룹핑)
\* 반드시 name속성값을 같게 해야 됨 *

\* 체크박스, 라디오, 콤보박스는 click보다는 change이벤트로 많이 코드를 만드는 경향이 있음 *

ex)
```javascript
$("input[name='imgStyle']").change(function (){

});
```
input태크 중에서 name속성이 imgStyle속성값인 것들이 바뀔때
(radio의 값들이 바뀔때)



#### \# method chaining
함수(동작)을 2개 이상 적을때
문법 :
```javascript
태그.함수().함수();
```
ex)
```javascript
myImage.removeClass().addClass(img-fluid);
```
myImage태그에 있는 class선택자들을 다 지우고 img-fluid인 class 선택자만 넣는다.



#### \# css()함수
HTML파일의 CSS부분 (\<style\>요소 안에 있는 내용)을 이용하는 함수
1) Getter 가져오기
속성값 가져오기
문법 :
```javascript
$("선택자").css("속성명");
```
ex)
```javascript
const width = $(".img-box").css("width");
```
CSS부분에 있는 .img-box 선택자의 속성인
width의 속성값을 가져오고 그 값을 width에 넣는다.

2) Setter 변경하기
속성값 변경하기
문법 :
```javascript
$("선택자").css("속성명", "값");
```
ex)
```javascript
$("#mainImage").css("width", w + "px");
```
CSS부분에 있는 \#mainImage 선택자의 속성인
width의 속성값을 가져오고 그 값을 w + "px"로 변경한다

3) 여러 개의 스타일 한꺼번에 바꾸기
여러 개의 속성값 바꾸기
문법 :
```javascript
$("선택자").css({"속성명": "속성값", "속성명": "속성값"});
```
ex)
```javascript
$("#mainImage").css({
    "width": "300px",
    "height": "200px",
    "border": "5px solid red",
    "opacity": "0.5"
});
```