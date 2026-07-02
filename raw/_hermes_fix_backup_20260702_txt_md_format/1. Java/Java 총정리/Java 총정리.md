Java 총정리 (2026.02.26(목) ~ 2026.03.13(금))
#### \# Java 구성
기본형 : 프로젝트 - 패키지 - 클래스, 인터페이스(다중 상속을 위한)


#### \# Java 특이사항
- Java는 띄어쓰기, 줄바꿈을 인식하지 못함

- 모든 문장의 끝에는 반드시 ;(세미콜론)이 붙는다. (가로줄의 끝)
But 중괄호에는 붙이지 않는다. (중괄호 = 바디, 클래스 바디, 메소드 바디)
But 배열생성시 초기화 기법에는 중괄호 후 세미콜론을 붙임

- main 메소드 (프로그램 출발선) (초록색 오른쪽 화살표 모양)
항상 클래스를 만들고 main을 만들고 시작해야한다.

- Java에서는 클래스 이름의 첫번째를 대문자로 하는게 관례임 (add X, Add O)

- 임의적으로 쓸 임시 변수를 보통은 사용할 변수 앞에 _를 붙인 변수로 정의해서 사용함
제어변수나 매개변수같은 변수


#### \# 유용한 단축키
- intelliJ 설정 : Ctrl + Alt + S

- 한줄복사 : Ctrl + D

- 자동 줄 맞춤 : Ctrl + Alt + L

- 같은 단어 복수로 입력되어있을때 한번에 전체 교체하는법
단어블록지정 후 (Ctrl + R)
Replace - 하나하나 바꾸기
Replace All - 전체 바꾸기

- 패키지명, 클래스명 변경 : Shift + F6

- 생성 단축키 : alt + insert키


#### \# 데이터 타입
문자형 (char)(1 ~ 2바이트)
문자열형 (String)(객체)
정수형 (int)(4바이트)
실수형 (double)(8바이트)
논리형 (boolean)(1바이트)


#### \# 안 배운 데이터 타입
정수형 - byte(1바이트), short(2바이트), long(8바이트)
실수형 - float(4바이트)


#### \# 변수 정의(선언)
문법 :
데이터타입 변수명;
ex)

```java
int age;
```
-> 정수형타입(int)의 변수명이 age인 변수 선언


#### \# 변수 대입(할당)
문법 :
변수명 = 변수값;
ex)

```java
age = 29;
```
-> age라는 변수에 대입 연산자(=)를 이용해서 29라는 변수값을 대입


#### \# 변수 선언 및 할당 동시 실행
문법 :
데이터타입 변수명 = 변수값;
ex)

```java
int age = 29;
```
-> 정수형타입(int)의 변수명이 age인 변수를 선언하고 29라는 변수값을 대입


#### \# 변수 덮어쓰기
이미 변수에 저장된 값을 다른 값으로 대체, 바꿔, 덮어 씀
x = 3 ; 이였던 것을
x = 4 ; 를 쓰면 덮어쓰기가 된거임

** 꼭!! 변수정의 후!! 변수대입 해야함 ** (중요함!!!!)


#### \# 주석
한 줄 주석 : //

여러 줄 주석 : /* */


#### \# 출력 메소드
- System.out.println(); - (sout) - 출력 후 줄바꿈(ln = line), +로 값들을 연결
ex)

```java
System.out.println("Hello world");
```

출력 :
Hello world


- System.out.print(); - 출력, 줄바꿈X, +로 값들을 연결

- System.out.printf(); - (souf) - 형식 지정 출력, 포멧 문자열 사용, 공백 출력O, 변수 필요O
서식(치환/형식) 지정자(Format Specifier)을 사용 - 이용 : 컴퓨터는 메모리에 0과 1로 저장된 덩어리가
어떤 데이터 타입인지 모르기에 직접 서식(치환/형식) 지정자를 이용해서 표시를 해줘야 함
문법 : %서식(치환/형식) 지정자

1) 서식(치환/형식) 지정자 :
%d(Decimal 정수) - int, long
%f(Floating-point 실수) - float, double
%s(String 문자열) - String
%c(Character 문자1개) - char

문법 :

```java
System.out.printf("출력내용 + 서식(치환/형식) 지정자", 변수명, 변수명);
//변수명은 ,(콤마)로 연결
ex)
int age = 29;
String name = "이현민";
System.out.printf("제 이름은 %s이고, 제 나이는 %d세 입니다.", name, age);
```

출력 :
제 이름은 이현민이고, 제 나이는 29세 입니다.


2) 소수점 몇자리까지 반올림해서 표시하기도 가능
문법 :
ex) 소수점 3자리까지 반올림해서 표현 : %.3f

(실습)
```java
double average = 74.6666666666666;
message = "평균 : %.3f"; //소수점 세번째까지 반올림해서 표현
System.out.printf(message, average);
```

(출력)
평균 : 74.667


3) 일정 크기 이상의 수 그대로 표현
Java에서는 일정 크기 이상의 수는 지수로 표현하는데
그대로 길게 표현하고 싶을때도 printf를 이용


#### \# 시퀀스
시퀀스 : 특수한 의미를 갖도록 약속된 '일련의 문자 조합
컴퓨터가 코드를 읽을 때 백슬래스(\)를 만나면 특수한 문자라고 인식하게 됨
\n : 줄바꿈
ex)

```java
int age = 29;
String name = "이현민";
System.out.printf("이름:%s\n나이:%d세", name, age);
```

출력:
이름:이현민
나이:29세


#### \# 변수명 (식별자) 명명 규칙
1. 첫 글자는 _, $, 영문 대문자 소문자 (한글 가능)
2. 글자수 제한 X
3. 공백 문자 및 특수 문자 사용 X
4. 숫자는 첫 글자에 X
5. 예약어, 키워드 사용 X


#### \# 연산자 우선 순위
단항>산술>이항>관계>비트>논리>조건>대입
단산이관비논조대


#### \# 연산자
- 산술 연산자 : +, -, *(곱하기), /(나누기), %(나누기 후 나머지)

- 증감 연산자 : ++, -- (1씩 증감)(숫자 앞 : 선 증감 / 숫자 뒤 : 후 증감)(단독으로 사용가능)
```java
int age = 1;
```
++age, age++은 age = age + 1 / age += 1과 같음

- 대입 연산자 : =

- 복합 대입 연산자 : +=, -=

- 관계 연산자 : <, <=, >, >=, ==, !=

- 논리 연산자 : not(!) - and(&&) - or(||)
우선 순위 : not(!) - and(&&) - or(||)
논리곱&논리합 표 알아둬야함 (표를 볼 줄 아는 정도) (진리표랑 같음)

- 조건 연산자(3항 연산자)(단순if문 축약느낌)
문법 :
(조건식)? (참일때의 값) : (거짓일때의 값);

```java
int a = 3, b = 5;
int result = a>=b ? a-b : b-a;
```
- 캐스팅(Casting)연산자(형변환 연산자) : 데이터의 타입을 다른 타입으로 "일시적"으로 변경함


#### \# (데이터를)읽기, (데이터에)쓰기
변수에 값을 넣기 (대입한다!)(할당한다!) (대입, 할당은 쓰기! 읽기X)

```java
x = 3 ; // x라는 변수에 3을 대입한다. (오른쪽을 왼쪽에 대입한다.) (쓰기)
y = 5 ; // y라는 변수에 3을 할당한다. (오른쪽을 왼쪽에 할당한다.) (쓰기)

sum = x + y ;
```
x + y 자체는 x값을 가져오고 y값을 가져오는 것 (읽기 2회)
sum에 가져온 x + y를 대입, 할당하는 행위 (쓰기)
-> =는 쓰기 행위임
\* 총 쓰기 3번, 읽기 2번 * (중요함!!!!!)


#### \# 변수 타입 재정의
변수의 타입을 정하면 절대로 바꿀 수 없음!!!!
\*변수 정의는 한번밖에 못한다!!*
!! int로 정의 한 것을 다시 int로 재정의 하는 것도 안됨 !!
!! int로 정의 한 것을 String으로 재정의 하는 것은 당연히 안됨 !!


#### \# 형변환 (Casting)
- 암시적 형변환 (묵시적 형변환) (변환대상을 포함한 더 큰 집합으로 변환할때 가능)
타입 변경 (ex 정수 -> 실수)
ex) double d = 100;

출력 -> 100.0
정수 100을 정의 및 대입하면 실수 데이터로 나옴 (정수데이터가 실수데이터로 형변환이 이루어짐)
(Java 가상 머신에 의해서)
(실수가 정수를 포함한 더 큰 집합이니까 가능)


(암시적 형변환 불가능 사례)

```java
int i = 3.14;
System.out.println("i : " + i);
```
-> 에러(incompatible type)
실수 데이터가 정수 데이터로 형변환이 이루어지는 일은 없음
(정수가 실수에 포함된 더 작은 집합이니까 불가능)

- 명시적 형변환 (변환대상을 포함하지 않는 더 작은 집합으로 변활할때 가능)(실수 -> 정수)
형변환연산자(캐스트 연산자, 캐스팅 연산자)(ex - (int))에 의한 형변환

```java
int i = (int)3.14;
System.out.println("i : " + i);
```

출력 -> i : 3


- 형변환 이용 예시
1.

```java
System.out.println(14/5); -> 출력 : 2
System.out.println((double)14/5); -> 출력 : 2.8
System.out.println((double)14/5); -> double 14 나누기 int 5
```
-> 14/5 -> 14.0/5(명시적 형변환) -> 14.0/5.0(정수의 실수화 - 암시적 형변환) -> 2.8
분자 or 분모가 실수이면 나머지도 실수로 변환됨 (암시적 형변환)

2.

```java
System.out.println(14/5); -> 출력 : 2
System.out.println((double)(14/5)); -> 출력 : 2.0
System.out.println((double)(14/5));
```
-> 14/5 -> 2 -> 2.0(명시적 형변환) -> 2.0


#### \# 정수 나누기
Java에서 정수 나누기 정수는 정수가 나온다.
(파이썬은 나누기 하면 실수가 나옴)


#### \# 문자 데이터의 형변환 (Java PDF P.29~30)
```java
// 아스키 코드 : A(65) a(97) 0(48)
char ch1 = 'c';
char ch2 = 'a';
boolean bool1 = ch1 > ch2; // 각각 99와 97으로 암시적 형변환
System.out.println("bool1 : " + bool1);
```

출력 : bool1 : true


문자끼리는 원해 크기 비교가 불가능해보이지만
사실 문자를 아스키 코드로 생각하고 크기를 비교할 수가 있음.
이런 과정에서 자연스럽게 문자가 숫자로 변환되면서 암시적 형변환이 이루어짐
(크기비교할때만! 그 크기 비교가 끝나면 다시 문자데이터로 취급)

- 크기비교 말고도 아예 계산으로 넣어지는 경우도 마찬가지
```java
int result = ch1 - ch2 + 5;
System.out.println("result : " + result);
```
(출력) -> result : 7

- 또 다른 문자 데이터 암시적 형변환
```java
char ch3 = 'D';
String str = ch3 >= 65 && ch3 < 97 ? "대문자" : "대문자아님";
(ch3는 문자 데이터인데 크기 비교를 위해 암시적 형변환으로 정수형 데이터가 됨)
System.out.println(("str : " + str));
```

출력 :  str : 대문자


// 자바의 char 타입은 정수형 데이터 타입이라고 볼 수 있습니다.

//(int안에 char영역이 있어서 int라고 볼 수도 있음)


#### \# 제어문
프로그램 수행 순서 제어
선택문(분기문) / 반복문


#### \# 선택문(분기문)
갈림길에서 선택(분기)한다
소괄호 / 중괄호 체크하기

- 단순 if (if)(경우의 수 1개일때 사용)
문법 :

```java
if(조건식){
	if 조건식이 참이 될때 실행될 구문
}
```

- 양자 택일 (if~else)(경우의 수 2개일때 사용)
문법 :

```java
if(조건식){
	if 조건식이 참일때 실행될 구문
}else{
	if 조건식이 거짓일때 실행될 구문
}
```

- 다중 택일 (if~else if~else) (경우의 수 2개 이상일때 사용)
문법 :

```java
if(조건식){
	if 조건식이 참일때 실행될 구문
}else if{
	if 조건식이 거짓이고 두번째 if조건식이 참일때 실행될 구문
}
```

else if라는 메소드가 따로 존재하는 것이 아니라
else라는 메소드 뒤에 if라는 메소드를 또 사용 한 것

- switch (switch case 구문)
문법 :

```java
switch (특정값){
	case 특정값 :
		조건인 특정값과 case의 특정값이 같을때 실행될 구문
}
```
\* if구문이랑 다른점

if 구문은 if 조건식에 맞는 그 구문을 실행하지만
switch 구문은 조건에 맞는 case 구문을 만나면 그 구문부터 밑에 있는 나머지 case 구문들을
모두 실행함.

- switch에 이용하는 다른 메소드
break; - switch 구문에서 조건에 맞는 case 구문을 만나 수행하고 그만두려면
break 메소드를 이용해야함

default; - case에 열거되지 않는 항목이 오면 이 구문이 실행됨
(if 구문의 else같은 느낌)

- switch 응용

(실습)
```java
//int month = 3 ;
//switch 구문을 사용하여 4계절 중 해당 계절 정보 출력하기
//switch 구문
public class Switch02 {
    static void main() {
        int month = 3;
        switch(month){
            case 3: case 4: case 5:
                System.out.println(month + "월은 봄입니다.");
                break;
            case 6: case 7: case 8:
                System.out.println(month + "월은 여름입니다.");
                break;
            case 9: case 10: case 11:
                System.out.println(month + "월은 가을입니다.");
                break;
            case 12: case 1: case 2:
                System.out.println(month + "월은 겨울입니다.");
                break;
            default:
                System.out.println("잘못된 입력입니다.");
        }
    }
}
```

(출력)
3월은 봄입니다.


#### \# 반복문
제어변수 : i
세미콜론 주의

- for 구문
반복 횟수가 명확할때 사용

문법 :

```java
for (초기식;조건식;증감식){
	반복 수행될 문장
}
```

초기식 : 최초 수행되는 수식(~부터)(오직! 한번만 실행)
-> int i = 1 (1부터)
조건식 : 비교/판단을 위한 근거가 되는 수식 (조건식이 성립(참)이 되면 실행)
-> i < 11 (11전까지)
증감식 : 제어 변수(i) 증가/감소를 위한 수식 (제어변수를 ~정도 증감해라
-> i = i + 1 / i += 1 / i++ (1씩 증가해라)

\* 초기식부터 조건식이 성립(참)될때까지 반복해서 실행함

(실습)
```java
//1부터 10까지의 총합
int total = 0;
for (int i = 1; i < 11; i++) {
	total += i;
}
System.out.println("총합01 : " + total);
```

(출력)
총합01 : 55


- while 구문
반복 횟수가 불명확할때 사용

문법 :

```java
초기식;
while(조건식){
	반복적으로 실행할 코드
	증감식;
}
```

ex)
```java
int total = 0;
int i = 1; //초기식
while(i<11){ //조건식
	total += i;
	i++; //i = i + 1, i += 1
}
System.out.println("총합01 + " + total);
```

- while 구문 응용 (무한 while구문)
반복 횟수가 불명확할때
반복 종료는 break;를 이용

```java
while(true){
	반복할 구문
}
```
계속해서 반복됨

- do while 구문
안배움


#### \# 보조 제어문
- break
제어문에서 종료할때 사용
문법 :

```java
break;
```
- continue
안배움


#### \# 입력함수
- 자바가 소스코드를 읽는 순서
```java
package -> import -> class -> method(main)
```
컴파일러의 작동: 자바는 코드를 읽기 전에 필요한 도구 리스트(import)를 먼저 체크함
그래서 실행코드(main)안에 체크한 도구 리스트에 맞는 특정 단어가 있을때
그냥 평범한 단어가 아니고 특별한 단어로 인식해서 특별한 기능을 수행하게 됨

import가 만약 main안에 있다면 자바에서 도구 리스트를 읽지 못해서
main안에 있는 원래는 특별한 기능을 가진 단어를 그냥 일반 단어로 인식하여
특별한 기능이 실행되지 않게 됨.

문법 :

```java
import java.util.Scanner; (package아래 class위에 입력해야 함)
Scanner scan = new Scanner(System.in);
	변수타입  변수명 = scan.nextint(); // 정수형 데이터 입력함수 (줄바꿈 됨)
ex) int input = scan.nextint();
	변수타입 변수명 = scan.next(); // 문자열형 데이터 입력함수 (공백에서 줄바꿈 됨)(공백 입력X)
ex)String name = scan.next();
	변수타입 변수명 = scan.nextLine(); // 문자열형 데이터 입력함수 (줄바꿈에서 줄바꿈 됨)(공백 입력O)
ex) String name = scan.nextLine();
```
\*scan.next();과 scan.nextLine();의 차이

```java
String name01 = scan.next(); //이 현민
```
-> 출력 : 이 -> (현민)은 찌꺼기가 남아서 다음 입력에 자동 입력됨

```java
String name02 = scan.nextLine(); // 이 현민 -> 출력 : 이 현민
```
- Scanner scan = new Scanner(System.in); 풀이
int, double, boolean은 기본 타입(Primitive)은 단순히 타입만 표현한다면
String, Scanner, random같은 참조 타입(Reference/Class)은
타입을 표현하면서 기능도 가지고 있음)

Scanner : String과 같은 클래스(타입)를 표현하는 단어 (타입을 표현하면서 기능도 있음)
-> 자바에서 제공하는 도구 상자(라이브러리)
scan : Scanner라는 기능을 가질 변수
new : 메모리에 새로운 객체를 만들으라는 명령어
Scanner() : 생성자 : 객체 생성시 초기화 하는 역할
System.in : 표준 입력 스트림 : 키보드 입력을 처리하는 자바의 기본통로
-> 키보드에서 데이터를 가져와라!

Scanner scan : 위의 방식으로 만들어진 단어를 scan이라는 이름으로 선언함
- import java.util.Scanner; 풀이
```java
import : 가져온다
```
java.util : 자바 도구 상자(라이브러리)에서
Scanner: Scanner라는 도구를

(실습)
```java
import java.util.Scanner;

Scanner scan = new Scanner(System.in);

System.out.print("이름 : ");
String name = scan.next();
System.out.print("나이 : ");
int age = scan.nextInt();
```

(출력)
이름 : 이현민
나이 : 29


#### \# 배열(array)
1부터가 아니고 0부터 시작해야한다

- 배열의 3요소
이름, 타입, 요소개수


#### \# 배열 - 01 new 연산자 기법 (배열 요소의 개수, 값이 명확하지 않을때) (요소 하나씩 추가)
- 배열생성
문법 :
타입[] 배열이름 = new 타입[요소개수];
ex) int[] arr = new int[3];

정수형 데이터를 가지는 변수명이 arr인 변수를 생성하고
이 변수는 3개의 정수형 데이터 타입 요소를 가진다
-> 빈방으로 놔둬도 되기때문에 배열 요소의 개수와 값이 명확하지 않을때
, 일단 방을 많이 만들고 배열 요소가 배열의 방의 개수보다 적으면
그냥 나머지는 빈방으로 놔둬도 됨.
\* 배열 요소가 없는 배열 순서를 출력하면 기본값으로 나옴 (int = 0 / String = null)

- 배열 요소 추가
문법 :
변수명[배열 방 번호 숫자] = 배열 요소;
ex)arr[1] = 1;

- 배열의 요소 개수
문법 :
변수명.length
ex) arr.length

(실습)
```java
int[] array = new int[3];
array[1] = 1;
System.out.println(array[1]);
System.out.println(array.length);
```

(출력)
1
3


(실습2)
```java
// bts 맴버들을 new 연산자를 사용하여 풀어 보세요.
String[] bts = new String[7];
bts[0] ="진";
bts[1] ="뷔";
bts[2] ="정국";
bts[3] ="rm";
bts[4] ="지민";
bts[5] ="슈가";
bts[6] ="제이홉";

System.out.println("배열 요소 출력하기");
for (int i = 0; i < bts.length; i++) {
	System.out.println(bts[i]);
}
```

(출력2)
배열 요소 출력하기
진
뷔
정국
rm
지민
슈가
제이홉


#### \# 배열 - 02 초기화 기법 (배열 요소의 개수, 값이 명확할때) (요소 한번에 추가)
\*유일하게? 중괄호( {} ) 옆에 세미콜론 (;)이 올 수 있는 양식

- 배열생성 및 추가 (new 연산자는 생성과 추가가 2단계로 나뉘어짐)
문법 :
타입[] 변수명 = 타입{요소, 요소, 요소};
ex)int[] arr = int {1, 2, 3};

- 배열의 요소 개수
문법 :
arr.length

(실습)
```java
// bts 맴버들을 초기화 기법으로 풀어 보세요.
// 요소의 값이 명확하고 변동사항이 없을때 사용하는 기법
String[] bts = {"진", "뷔", "정국", "rm", "지민", "슈가", "제이홉"};

System.out.println("배열 요소 출력하기");
for (int i = 0; i < bts.length; i++) {
	System.out.println(bts[i]);
}
```

(출력)
배열 요소 출력하기
진
뷔
정국
rm
지민
슈가
제이홉


(실습02 - 배열문제 + 입력함수, if제어문 이용)
```java
package ch03_array;

//입력함수 불러옴
import java.util.Scanner;

public class EvenOdd {
    static void main() {
		//입력함수 불러오기
        Scanner scan = new Scanner(System.in);

		//출력
        System.out.print("배열 요소 개수 입력 : ");
        int size = scan.nextInt(); //입력

		//배열 생성 (new 연산자 이용)
        int[] jumsu = new int[size];

        int odd = 0, even = 0; // 합산 변수들은 반복하기 전에 정의

		//jumsu.length대신 size입력해도 됨
        for (int i = 0; i < jumsu.length; i++) {
            System.out.print(i + "번째 정수 입력 : "); //출력
            jumsu[i] = scan.nextInt(); //배열에 요소 추가

            if (jumsu[i]%2==1){ //요소의 값이 홀수이면
                odd += jumsu[i];
            }else{ //아니면 (요소의 값이 짝수이면)
                even += jumsu[i];
            }
        }

        System.out.println("홀수의 총합 : " + odd);
        System.out.println("짝수의 총합 : " + even);
    }
}
```

(출력02 - 배열문제 + 입력함수, if제어문 이용)
배열 요소 개수 입력 : 4
0번째 정수 입력 : 5
1번째 정수 입력 : 3
2번째 정수 입력 : 4
3번째 정수 입력 : 8
홀수의 총합 : 8
짝수의 총합 : 12


#### \# 클래스
- 클래스 이름은 통상적으로 첫 글자는 대문자로 작성하는 경향이 있습니다. (ex - Scanner)
- 클래스를 구성하는 3요소 : 변수, 메소드, 생성자

1. 단계01 : 클래스 정의
클래스 : 기존 자료형을 이용하여 개발자가 새롭게 정의한 사용자 정의 타입(User-Defined Type)
무한히 생성가능, 추상적인 것 (틀, 템플릿)
타입이 들어가는 문법에 그대로 사용하는 경우가 많음
-> 내가 만든 String2개와 int1개를 가진 새로운 형태의 타입인 Product

1) 클래스 정의 및 맴버 생성
클래스 정의를 위해서는 업무파악이 필요
(어떤 내용이 들어가야 하는지 알아야 함)
ex) 시계라는 클래스를 정의하려면 시계의 내용인 디자인, 구동방식 등이 들어가야 함

문법 : 맴버 변수, 맴버 메소드 생성

(클래스)
- 맴버 변수
타입 이름;

- 맴버 메소드
반환타입 메소드명 (매개변수 리스트){
	실행될 구문;

```java
	return 반환할 값;
}
```
-> [반환타입]을 가진 [메소드]에 [매개변수리스트]가 투입될때
[실행될 구문]을 실행하고 반환할 값을 return한다.

```java
int plus5(int x){,,,} / int plus5(int x, int y){...}
매개변수리스트라고 한 이유가 매개변수가 2개 이상일 수도 있어서 ( ,(콤마)로 연결 )
```
1) 메소드 이름 정하기 1)plus5
2) 매개 변수의 갯수 및 타입 정하기 2)int x
3) 반환 타입 (결과 타입) 정하기 3)int /
ex)

(main클래스)
```java
int result = shin.plus5(3); // 메소드 호출
System.out.println("결과 : " + result);
```

(클래스)
```java
int plus5(int x){
	return x + 5;
}
//투입된 매개변수리스트로 인해 실행되어 나온 값을 반환타입을 가진 값으로 반환한다.
```

(출력)
결과 : 8


\* 맴버 메소드 풀이 * (중요함! 로직을 알아야함)
shin.plus5(3)
- shin이라는 객체가 속한 클래스의 맴버메소드인 plus5를 호출하고
매개변수는 3이야.
- int 3이라고 적으면 안됨!!!! 여기서 int 3은 int타입 3을 의미하는 것이 아니라
int 3이라는 변수를 선언한다는 의미로 사용되기 때문에

(클래스 맴버메소드의 매개변수리스트 내용과는 다름)
```java
int plus5(int x){
```
- plus5라는 메소드명을 가진 맴버 메소드는 int타입의 변수를 받을 건데
이건 이 메소드안에서 x라고 부를거야 (main클래스의 변수 선언과는 형태는 같지만 목적이 다름)
이 맴버 메소드로 인해서 반환하는 값이 있으면 나는 그 값의 타입을 int로 설정할거야.

```java
return x + 5;
```
- 아까 main클래스에서 호출해서 받은 int타입의 x값을
x + 5에 투입하고 이것을 다시 호출 받은 곳! 바로 그곳으로 반환(발송)할거야
- x+5는 8이니까 원래 호출한 shin.plus5(3)으로 다시 반환되니까
shin.plus5(3)의 값은 int타입을 가진 8이 되는거야

\* 호출 개념 *

```java
int result = shin.plus5(3);은
int result = int plus5(int x){return x + 5;} 이런 느낌인데 x에 3이 들어간 형태인데
```
				   메소드에서 return하는 값만 다시 보내주니까
				   사실상

```java
int result = x + 5인데 x가 3이고 x+5의 타입은 int인 느낌.
```
\* 맴버 변수 호출시*
shin.(객체.)을 누르면 (맴버변수인지 메소드인지 나타내는 약자)
맴버변수, 메소드 이름  반환타입이 나옴

shin. (f)price     			 int
		(m)plus5 (int x)     int

f(field)(필드) = 변수

m(method)(메소드)
변수는 소괄호가 없고 / 메소드는 소괄호가 있음

2. 단계02 : 객체 생성
- '생성자명'은 '클래스명'과 동일해야 함
- 객체 : 추상적 개념인 클래스를 통해 만들어진 구체적인 것
ex) 클래스 : 스포츠
객체 : 축구, 야구, 농구

클래스  : 붕어빵 틀
객체 : 만들어진 붕어빵

(main클래스)
문법 : 변수 선언 및 대입과 형태는 비슷함
클래스명 객체명 = new연산자 생성자명();

1) 객체 정의 후 할당
	클래스명 객체명
	객체명 = new연산자 생성자( 클래스명 () )

2) 객체 정의 및 할당
	클래스명 객체명 = new연산자 생성자명();
	\* 생성자 : 객체 생성시 오직 1번만 호출이 되는 특수 메소드

(main클래스)
(실습)
```java
public class ProductMain {
    static void main() {
        // 단계02 : 객체 생성
		// 1) 객체 정의 후 할당
		Product blackbean;
        blackbean = new Product(); // 짜파게티

		// 2) 객체 정의 및 할당
        Product shin = new Product(); // 신라면
	}
}
```
3. 단계03 : 맴버 변수에 값을 할당
.(점, dot) = 맴버 참조 연산자
-> 맴버에 참조를 하는 연산자 - 왼쪽에 있는 객체 안으로 들어가서
오른쪽에 있는 변수(멤버)를 찾아라! 라는 동작 실행

문법 :
객채명.맴버변수명 = 데이터 값

(main클래스)
(실습)
```java
shin.name = "신라면";
shin.price = 1000;
shin.inputdate = "2026/03/01";
```
4. 단계04 : 맴버 변수들의 값을 출력

```java
System.out.println("1번 상품 정보 출력");
System.out.println("이름 : " + shin.name);
System.out.println("단가 : " + shin.price);
System.out.println("입고 : " + shin.inputdate);
```

(출력)
1번 상품 정보 출력
이름 : 신라면
단가 : 1000
입고 : 2026/03/01


#### \# 클래스 안에서 매개변수 없는 메소드 만들기
매개변수가 필요없음
(변수가 필요없거나, 필요한 변수가 클래스 내부에 있어서 외부에서 가져올 필요가 없거나)

(클래스)
```java
// 상품명 : 신라면, 단가 : 1000원, 입고 : 2026/03/01
String showData(){
	String result = "상품명 : " + name + ", 단가 : " + price + "원, 입고 : " + "inputdate";
	return result ;
}
```

(main클래스)
```java
// 클래스에서 반환받은 메소드를 main클래스에 할당함
String str = shin.showData();
// 출력
System.out.println(str);
```

(출력)
상품명 : 신라면, 단가 : 1000원, 입고 : 2026/03/01


#### \# 반환안하고 알아서 클래스 내에서 출력해라
반환하지 않을때는 반환타입이 들어갈 자리에 void 입력

void - 응대하지 않는, 대답하지 않는
return(반환)하지 않아서 shin.Display()는 데이터로서의 '값'이 전혀 없음
'값'이 아니라 그저 동작하는 거임

return(반환)을 하지 않아서 (새로운 데이터를 저장하지 않아서)
쓰기 동작이 아니고 읽기 동작임

(클래스)
```java
void Display(){
	System.out.println("상품 : " + name);
	System.out.println("단가 : " + price);
	System.out.println("입고 : " + inputdate);
}
```

(main)
```java
shin.Display();
```
\* 변수, 메소드를 한번도 호출하지 않으면 회색으로 보임


#### \# 클래스를 보지 않아도 main클래스에 적힌 변수, 메소드의 타입을 아는 법 (당연한 유추)
int result = shin.plus5(su); - int임
String str = shin.showData(); - String임
shin.Display(); - 없음


#### \# 접근 지정자(제어자) (PDF p.81)
변수 왼쪽에 아무것도 안적혀있으면 default(기본)라고 부름

- 접근 지정자와 패키지와의 관계
종류											public		protected	  기본(default)		  private
동일 클래스								가능				가능				    가능		    	   가능
동일 패키지의 모든 클래스		가능				가능			 	    가능		   		 불가능
동일 패키지의 서브 클래스		가능				가능			 	    가능		   		 불가능
다른 패키지의 서브 클래스		가능				가능		  	   	  불가능	 	   	 불가능
다른 패키지의 일반 클래스		가능			  불가능	  		  불가능	 	   	 불가능
비고										전체 공개		일촌 공개  	   일촌 공개	   		 비공개


#### \# getter 메소드와 setter 메소드 (PDF p.82)
통장 잔액 조회(getter메소드)
통장 잔액 입금 출금할때 바뀜(setter메소드)

private 변수를 우회적으로 사용하기 위해서 사용하는 메소드들
Java에서는 보통 모든 변수들을 private으로 만듬

- getter 메소드
private 변수의 값을 읽어보기 위한 public 메소드
매개변수 X (클래스 내부에 private 변수가 있으니까)
반환O (private한 변수의 값을 public으로 바꿔서 반환해서 사용하려고)
문법 :

```java
public 반환타입(해당변수의) get변수의첫글자만대문자(){
	return 해당변수;
}

ex)
public int getPrice(){
	return price;
}
```
-> (main클래스)
객체명.getPrice()는 결국 private int price값과 동일한 값이니까
사용할 수 있게 됨
개념을 private int price를 사용한다고 생각하지말고

private int price의 '값'을 얻어와서 사용한다고 생각하면 됨
- setter 메소드
private 변수의 값을 설정하기(쓰기) 위한 public 메소드
매개변수 O
반환X -> viod

문법 :

```java
public void setPrice(int _price){
	price = _price;
}
```
풀이:
main클래스의 객체명.setPrice(매개변수 - _price값)로 인해
클래스의 int _price가 들어오고 그 값을 기존에 있던 private int price값에 재할당함

\*public void setPrice(int price){*이 안되는 이유!

```java
	price = price;
}
```
-> 항상 논리적으로 가까운 변수를 인식해서 메소드 안에 있는 "price = price"의 price 둘다

private price보다 매개변수 int price의 price를 인식해서
만약 매개변수 int price값이 2000이였다면 price = price의 값이 2000 = 2000이 된다.

-> 더 자주 쓰이는 관습적인 문법

```java
public void setPrice(int price){
	this.price = price;
}
```
이유 1) 이 변수가 그 변수다!라는 직관성
		2) 변수 이름을 짓는 고충 제거
		3) IDE와 궁합이 좋음(표시해줌)
		4) 표준처럼 굳어짐)

\*실질적으로 main에 사용하려면 반환을 해서 값을 받아야해서 getter를 해야함*

(클래스)
(실습)
```java
package ch04_class;

public class Product03 {
    // 클래스 정의
    // 맴버 변수 선언
    private String movement;
    private int power_reserve;

    //메소드 선언
    void Display(){
        System.out.println("무브먼트 : " + movement);
        System.out.println("파워리저브 : " + power_reserve);
    }
    public void setMovement (String _movement){
        movement = _movement;
    }
    public String getMovement (){
        return movement;
    }
    public void setPower_reserve (int _power_reserve){
        power_reserve = _power_reserve;
    }
    public int getPower_reserve (){
        return power_reserve;
    }
}
```

(main클래스)
```java
package ch04_class;

public class ProductMain03 {
    static void main() {
        // 객체 생성
        Product03 watch = new Product03();

        //객체 할당
        watch.setMovement("automatic");
        watch.setPower_reserve(38);

        //메소드 사용
        watch.Display();
    }
}
```

(출력)
무브먼트 : automatic
파워리저브 : 38


\*프로그램 흐름 이해하기 (중요함!)*

```java
void Display(){
	System.out.println("무브먼트 : " + movement);
	System.out.println("파워리저브 : " + power_reserve);
}
```
이 메소드가 main으로 넘어갈때 (main클래스)에서 watch.Display();일때
"System.out.println("무브먼트 : " + movement);

```java
System.out.println("파워리저브 : " + power_reserve);"이 메소드들이 그대로 넘어가서
```
main클래스에 있는 movement와 power_reserve변수를 사용해서 출력되는게 아니고

Display()메소드 안에 있는 메소드들의 결과 '값'을 호출하는 거여서
watch.Display()는 무브먼트 : automatic
							 파워리저브 : 38
이라는 값이라고 볼 수 있다.

따라서!!!!! main클래스에 movement변수와 power_reserve변수가 없어도 실행이 됨
이 말은?! getter 메소드를 사용해서 main클래스에
private인 movement변수와 power_reserve변수를 public으로 반환할 필요가 없긴하다.


#### \# 생성자
클래스 내에 기본 생성자가 있는데 눈에는 보이지 않음

정의 : 객체 생성시 오직 1번만 호출이 되는 특수한 메소드
목적 : 맴버 변수들의 초기화 (기본값을 넣는다)

- 생성자와 메소드의 차이점
생성자 : 오직 1번 호출 / 호출 시점이 객체 생성시
메소드 : 자유롭게 호출 / 호출 시점이 자유로움

+ 추가
생성자는 객체 생성될때 초기화를 시키고 / 메소드는 객체가 생성된 후 동작과 기능을 부여
생성자의 이름은 클래스 이름과 동일해야함
생성자는 반환 타입이 없고 / 메소드는 반드시 명시해야함 (void라도)
생성자는 new로 딱 한 번 실행되고 메소드는 원할때 언제든 호출 가능

기본 생성자를 (생성자가 속한 클래스 내부에) 줬지만 눈에 안보이니까 내가 컨트롤 할 수 없음
-> 개발자가 필요하면 따로 만들 수 있음
-> 개발자가 생성자를 만들면 눈에 보이지 않는 기본 생성자는 사라짐
혹은 개발자가 따로 만든 생성자를 기본 생성자라고 부르기도 함

문법 :

(클래스)
```java
생성자명(){

}
```
기본 생성자 :
```java
생성자명(){
}
```

(main클래스)
(실습)
```java
Product03 shin = new Product03();
```

(출력)
출력 메소드를 하지 않아도 저상태여도 출력이 됨
하지만 기본 생성자의 값이 아무것도 없어서 아무것도 출력하지 않음


\*그렇다면 기본 생성자는 의미 없는 것 아닌가?* (중요함!!)
이 기본 생성자마저 없으면 에러가 나면서 프로그램 자체가 돌아가지 않음
자바에서 기본 생성자는 마치 "프로그램을 돌리기 위한 최소한의 입장권" 같은 존재
이것 자체로 의미가 있음

(클래스)
(실습)
```java
// 기본 생성자를 수정하기
Product03(){
	System.out.println("하하하");
}
```

(main클래스)
```java
Product03 shin = new Product03(); // 출력메소드없어도 출력됨
System.out.println(shin);
```

(출력)
하하하
ch01_variable_operator.example@23fc625e


\* 객체의 기본값은 오브젝트의 상속을 받은 toString() 메소드임
(object 오브젝트는 상속의 계보 최고 위의 수퍼클래스)
(명시적 상속이 아니고 암시적 상속을 받음)
(명시적 상속은 extends를 이용하는 것)
ex) ch01_variable_operator.example@23fc625e

\* 클래스 내부에 맴버 변수들의 값도 기본값이 있음
String, 클래스, 배열 : null

```java
double : 0.0
```
int : 0
boolean : false


#### \# 생성자에 매개변수 추가 (main클래스와 클래스를 생성자로 연결)
main클래스의 생성자와 클래스의 생성자의 매개변수를 대칭시켜줘야함
메소드와 동일한 방식
\*사실상 생성자도 큰 범위에서는 메소드임

(main클래스)
(실습)
```java
Product03 shin = new Product03("신라면", 100, "2026/03/01");
```

(클래스)
```java
public Product03(String name, int price, String inputdate){
	// 객체 자신(this)이 소유한 name 변수에 매개 변수 name의 값을 할당하시오
	this.name = name ;
	this.price = price;
	this.inputdate = inputdate;
}
```
경로 : main클래스의 생성자의 매개변수 "신라면" -> 클래스의 생성자의 매개변수 String name -> 생성자 구문 안에서 (this.name이용해서 할당)
-> 클래스의 맴버 변수 String name

- this키워드 사용하는 이유
클래스 내부에 String name이 있을때 이 맴버 변수 String name을 생성자 내부에 가져오고 싶을때
그냥 바로 String name을 생성자 내부에 작성하면 새로운 String name이라는 변수를 선언한걸로 인식하기때문에
클래스 내부의 맴버 변수 String name을 가져올때는 this라는 키워드를 이용해서
this.name이라고 해야 클래스 내부의 맴버 변수 String name으로 인식함


#### \# 오버로딩
오버로딩이란 무엇인가 ? (=다중 정의)
한 개의 클래스 안에 이름은 같지만 매개변수(개수나 타입)가 다른 메소드나 생성자를 여러 개
만드는 것
이름 하나에 여러 기능을 얹는 것

목적 : 여러가지 이름의 메소드를 따로따로 만들면 만들기도 번거롭고 제3자가 봤을때 헷갈리니까
ex) 더하기는 add라는 메소드로 통일하자!

조건 : 메소드 이름 동일 / 매개변수의 개수 or 타입이 달라야 함

(main클래스)
(실습)
```java
Product03 shin = new Product03();
Product03 shin2 = new Product03("신라면", 100, "2026/03/01");
```

(클래스)
```java
public Product03(){
	System.out.println("하하하");
}

public Product03(String name, int price, String inputdate){
	this.name = name ;
	this.price = price;
	this.inputdate = inputdate;
	System.out.println(name + price + inputdate);
}
```

(출력)
하하하
신라면1002026/03/01


#### \# 맴버 변수의 기본값 설정
맴버 변수 생성하고 값을 할당

```java
private int price = 500 ;
```


#### \# 배열에 객체 이용 (new 연산자 기법)
(main클래스)
```java
int size = 2;
Product03[] itemlist = new Product03[size];

// 0번째 객체 생성 *객체 생성을 이렇게도 할 수 있구나 (new 생성자())
// 배열 객체 생성 문법 : 배열명[배열요소개수] = new연산자 클래스명(매개변수);
itemlist[0] = new Product03("소이조이", 2000, "2025/08/15");
itemlist[1] = new Product03("맥심커피", "2025/07/17");

for (int i = 0; i < itemlist.length; i++) {
	System.out.println((i+1) + "번째 상품 정보");
	itemlist[i].display();
}
```

(클래스)
```java
// 맴버 변수 생성
private String name ; // null
private int price = 500 ; // 0
private String inputdate ; // null

// 오버로딩
public Product03 (String name, String inputdate){
	this.name = name;
```
	this.price = price; // 기본값
	this.inputdate = inputdate;

```java
}

public Product03(String name, int price, String inputdate){
	this.name = name;
	this.price = price;
	this.inputdate = inputdate;
}

public void display() {
	System.out.println("상품명 : " + name);
	System.out.println("단가 : " + price);
	System.out.println("입고 : " + inputdate);
}
```

(출력)
1번째 상품 정보
상품명 : 소이조이
단가 : 2000
입고 : 2025/08/15
2번째 상품 정보
상품명 : 맥심커피
단가 : 500
입고 : 2025/07/17


#### \# 배열에 객체 이용 (초기화 기법)
(main클래스)
```java
// 배열 정의 (초기화 기법)
//초기화 기법의 객체 생성 문법 : new연산자 클래스명
Product03[] productArray = {
	new Product03("쭈쭈바", 1500, "2025/12/25"),
	new Product03("사과", 3000, "2025/06/06"),
	new Product03("오징어땅콩", "2025/07/17")
};

for (int i = 0; i < itemlist.length; i++) {
	System.out.println((i+1) + "번째 상품 정보");
	productArray[i].display();
}
```

(클래스)
```java
 public Product03 (String name, String inputdate){
	this.name = name;
```
	this.price = price; // 기본값
	this.inputdate = inputdate;

```java
}

public Product03(String name, int price, String inputdate){
	this.name = name;
	this.price = price;
	this.inputdate = inputdate;
}

public void display() {
	System.out.println("상품명 : " + name);
	System.out.println("단가 : " + price);
	System.out.println("입고 : " + inputdate);
}
```

(출력)
1번째 상품 정보
상품명 : 쭈쭈바
단가 : 1500
입고 : 2025/12/25
2번째 상품 정보
상품명 : 사과
단가 : 3000
입고 : 2025/06/06
3번째 상품 정보
상품명 : 오징어땅콩
단가 : 500
입고 : 2025/07/17


#### \# 상속
탄생 배경 : 계속해서 클래스를 만들지 말고 비슷한 것은 이미 만들어진 것에서
그 비슷한 특성을 물려받으면 중복할 일이 없지 않을까?

수퍼 클래스 - 부모 클래스 = 상위 클래스 = 상속을 해주는 클래스
서브클래스 - 자식 클래스 = 하위 클래스 = 상속을 받는 클래스
수퍼 클래스는 서브 클래스에 참조할 수 없음
서브 클래스는 수퍼 클래스에 참조할 수 있음

문법 :
접근지정자 class 서브클래스 extends 수퍼클래스{

```java
	//어떤 코드
}
```
Animal클래스 = 수퍼클래스
Dog클래스 = 서브클래스

(main클래스)
```java
Dog retriver = new Dog(); //객체 생성
```
retriver. //내용물을 보면 Dog클래스 안에 있는 맴버 변수말고도

			 // Animal클래스에서 상속받은 수퍼클래스의 맴버 변수도 있음
- display메소드를 만들때 모든 정보를 다 참조할 수 있는 서브 클래스에 만들면 됨
But 수퍼클래스에서 이용할 수 있는 정보를 가지고 display가능


#### \# 오버라이딩
부모에게 물려받은 메소드를 자식 클래스에 맞게 재정의하는 것
위에서 언급했던 자식 클래스에 추가 수정 가능여부

문법 :
```java
접근지정자  void 메소드(){
	super.메소드(); // 수퍼클래스의 메소드를 불러올때
}
```

(예시)
```java
public void display(){
	super.display();
}
```

(Animal수퍼클래스)
```java
public void display(){
	System.out.println("하이")
}
```

(Dog서브클래스)
```java
public class Dog extends Animal {
boolean guide; //안내경 여부

	@Override // 이 부분을 annotation이라고 부르고 고급? 주석이라고도 부름
					// 단순히 이 메소드는 오버라이딩되었다고 알리는 것.
					// 사실상 없어도 됨
	public void display() {
		// Dog클래스만의 메소드를 추가함(오버라이딩 함)
		System.out.println("안내견 여부 : " + guide);

		// super는 나의 수퍼 클래스 Animal을 의미합니다.
		// super(Animal)의 display를 호출해서 가져옴 (프린트 name과 age)
		super.display(); // Animal수퍼클래스의 display()메소드를 그대로 가져옴
								// 사실상 " System.out.println("하이") "이 추가 된 것
	}
}
```
\* 프로그램 논리 개념 (중요함!!!) *
수퍼클래스에

```java
public void bark(){

}
```
가 있고

서브클래스에 오버라이드할때
원래는

```java
public void bark(){
	super.bark();
}
```
인데

super.bark();를 제거해서 나온

```java
public void bark(){

}
```
는 그냥 서브클래스에 적은 bark()메소드와 오버라이드된 bark()메소드와 차이점이 없는데
이것을 과연 오버라이드라고 부를 수 있을까?

(답)
오버라이드임
왜냐하면 논리적으로 상속에 의해 수퍼클래스의 데이터들이 이미
서브클래스에 들어가 있는데
서브클래스에

```java
public void bark(){

}
```
이 메소드를 따로 적는다고해도 수퍼클래스의 메소드와 형태가 같아서
자동적으로 컴파이러가 오버라이드로 인식함
만약 이것을 서브클래스의 별도의 메소드라고 인식한다면
똑같은 형태의 메소드가 2개라는 의미인데
이러면 에러가 발생할 수밖에 없음.


#### \# 오브젝트 메소드 오버라이드 하기
가장 많이 쓰는 오브젝트의 메소드 : toString()
-> 반환타입이 String인 객체정보인 16진수의 해쉬코드 값을 문자열로 만들어서 출력해줌

\* 객체 출력시 오브젝트의 메소드인 toString()의 값이 나옴 *

(Animal클래스)
(불러오기)
```java
@Override
public String toString() {
	return super.toString(); // 16진수 값 : ch05_inheritance.Dog@85ede7b
}
```

(출력)
ch05_inheritance.Dog@85ede7b


(오버라이드 하기)
```java
@Override
public String toString() {
	String imsi = "이름 : " + name + ", 나이 : " + age + ", 먹이 : " + feed ;
	return imsi ;
}
```

(출력)
이름 : 김리트리버, 나이 : 2, 먹이 : 건식 사료


#### \# 메소드 은닉화
오버라이딩시 본의 아니게 부모 메소드 접근이 막히는 현상

예시:
원래 오브젝트의 메소드였던 toString을 서브클래스인 Animal클래스에서 오버라이드하고
그 후에 Animal클래스의 서브 클래스인 Dog클래스에서 toString메소드를 호출하려고할때 오브젝트의 toString메소드를 호출하지 못하고
논리적으로 더 가까운 Animal클래스에서 오버라이드된 toString이 호출되어버림

```java
				toString()
```
Object			O
Animal			O
Dog				X


#### \# 일반화
보편적인 공통분모를 수퍼클래스에 적는 것 (서브클래스들이 수퍼클래스에서 상속받을 수 있도록)
클래스 디자인 : 클래스에 내용을 추가해서 완성하는 것

(예시)
(수퍼클래스)
```java
(맴버 변수 생성)
public class Beverage03(){
	private String name; // 음료 이름
	private double price; // 단가
}
```
-> 모든 음료에는 이름이 있고 단가가 있으니까 공통분모인 이름, 단가를 맴버 변수로 수퍼클래스 Beverage03에 적어서 일반화 함
이렇게하면 서브클래스들에는 자동으로 name과 price 맴버 변수가 생성됨 (눈에 보이지는 않지만)


#### \# private 맴버 변수를 다른 클래스에서 사용하려면
서브클래스가 수퍼클래스의 변수에 접근
1. private은 getter / setter로 접근
2. private 대신 protected로 작성
3. 생성자를 통한 대입


#### \# 3. 생성자를 통한 대입 사용
서브 클래스의 생성자의 첫줄에는 super(); 라는 단어가 숨어있다.
super(); - 매개변수가 0개인 super클래스의 생성자
ex) Americano03클래스의 생성자 public Americano03(String name, double price, double waterAmount){...}의 첫줄에는 super();라는 단어가 숨어있다.
사용자가 super(매개변수); 형식으로 다시 작성하면, super();는 사라집니다. - 마치 클래스의 타입에 기본값을 다시 작성하면 사라지는 것 처럼

super();의 매개변수에 private때문에 사용하지 못하는 변수를 넣고 다시 수퍼클래스에 보내면 수퍼클래스 내에서는 private변수를 사용할 수 있으니까
이렇게 사용할 수 있음
그런데 수퍼클래스에 다시 보낼때 수퍼클래스에서 이 super(매개변수);를 받을 수 있게 1대1 대응이 가능한 생성자를 만들어야 함

(main클래스)
(실습)
```java
public class InheTest03 {
    static void main(String[] args) {
		// 1) Americano03클래스의 Americano03생성자로 값이 넘어감
        Americano03 americano = new Americano03("아메리카노", 4000.0, 200.0);
        Espresso03 espresso = new Espresso03();
        Latte03 latte = new Latte03();
    }
}
```

(Americano03서브클래스)
```java
public class Americano03 extends Beverage03 {
    private double waterAmount; // 투입하는 물의 양
    // 생성자 만들기 (메소드와 똑같음)
	// 2) main클래스의 Americano03생성자으로부터 값을 받아서
	// 현재 String name은 "아메리카노" / double price는 4000.0 / double waterAmount는 200.0 임
    public Americano03(String name, double price, double waterAmount){
        // 서브 클래스의 생성자의 첫줄에는 super(); 라는 단어가 숨어있다.
        // super(); - 매개변수가 0개인 super클래스의 생성자
        // 사용자가 super(매개변수); 형식으로 다시 작성하면, super();는 사라집니다.

		// 4) public Americano03의 매개변수에 name과 price 변수를 사용하기 위한 껍데기를 줘야하는데
		// super클래스에서 private이여서 가져와야해서 super클래스에 보낼 생성자를 사용
        super(name, price);

		// 3) double waterAmount라는 데이터를 쓰기 위한 정의된 껍데기가 필요해서
		// Americano03클래스의 waterAmount 맴버 변수 사용
        this.waterAmount = waterAmount;
    }
}
```

(Beverage03수퍼클래스)
```java
public class Beverage03 {
	// 음료 이름
    private String name;
	// 단가
    private double price;
	// 5) 4에서 보내준 super(name, price);의 생성자와 1대1 대응되는 생성자를 만듬
    public Beverage03(String name, double price){
		// 6)서브 클래스에 맴버 변수 껍데기를 보내기 위해 재정의
        this.name = name;
        this.price = price;
    }
}
// 7) 다시 역 순서로 데이터를 보냄
```


#### \# (# 3. 생성자를 통한 대입 사용) <- 이 방법을 사용해서 생긴 오류 잡기
이 방법을 사용하면 같은 수퍼클래스를 공유하고 있는 다른 서브 클래스의 생성자에는
똑같이 super(); -> ( Beverage03(){} )이 숨겨져 있는데
super();이 똑같이 있다가 갑자기

```java
public Beverage03(String name, double price){
	this.name = name;
	this.price = price;
}
```
위에처럼 매개변수가 있는 생성자를 하나라도 직접 만드는 순간,
자바가 사용자가 직접 관리하는 줄 알고 기본 생성자 조차 자동으로 만들어주지 않아서

Beverage03(){}이라는 값 자체가 Beverage03수퍼클래스에 없는거임
그래서 수퍼클래스에 super();와 대응할

```java
public Beverage03(){}
```
이것을 만들어주면 해결됨


#### \# 왜 Beverage03에 기본 생성자가 없나요?
자바의 규칙 때문임
클래스에 생성자를 하나도 안 쓰면, 자바가 자동으로 public Beverage03() {} (기본 생성자)을 만들어줌
하지만 사용자가 매개변수가 있는 생성자(public Beverage03(String name, double price))를 하나라도 직접 만드는 순간,
자바는 "아, 사용자가 직접 관리하나 보네?" 하고 기본 생성자를 자동으로 만들어주지 않습니다.
따라서 매개변수가 있는 생성자를 만들면 Beverage03(){}은 존재하지 않음
-> 따라서 서브클래스에 생성자에 눈에 보이지 않는 기본 생성자인 super(){}이 존재하지 않아서 에러가 발생함

해결 방법
1) Beverage03수퍼클래스에 기본 생성자를 명시적으로 생성하기

```java
public Beverage03(){}
```
-> 이렇게 하면 super() -> ( Beverage03(){} )의 값이 공백으로라도 "존재"는 하기에 에러가 발생하지는 않는다.

2) 서브클래스의 생성자 안에 있는 기본 생성자인 super()또한 수퍼클래스의 기본 생성자처럼
매개변수가 있는 생성자를 하나라도 직접 만드는 순간, 기본 생성자를 자동으로 만들어주지 않기때문에
임의로 super(name, price); 같은 생성자를 만들면 에러가 발생하지 않는다.


#### \# 참조 형변환
1) 승급(UpCasting)
두 클래스가 상속관계라는 전제 하에서
낮은 등급의 클래스가 높은 등급의 클래스 타입으로 한시적 형태가 바뀌는 동작

// 부모입장에서 자식들 관리를 편하게 하려고 사용하는 방법
// 암시적 형변환
문법 :
수퍼클래스 객체명 = new연산자 서브클래스();

```java
Americano04 beverage01 = new Americano04("아메리카노", 4000.0, 250.0);
```
-> Beverage04 beverage01 = new Americano04("아메리카노", 4000.0, 250.0);
이렇게 되면 beverage01객체는 한시적으로 Beverage04수퍼클래스의 객체가 되어서

Beverage04수퍼클래스의 맴버 변수와 맴버 메소드를 사용할 수 있게 된다. (반대로 Americano04클래스의 맴버 변수와 맴버 메소드를 사용할 수 없게 된다.)
But 어디까지나 한시적으로 바뀌는 것이지 근본은 beverage01가 Americano04클래스의 객체이다.

2) 강등(DownCasting)

```java
Americano04 cofeee = (Americano04)beverage01; // 명시적 형변환
//이해하기 위해서는
// int i = (int)3.14; 처럼 생각해서 클래스도 개발자가 만들어 낸 타입이라고 생각해서 그대로 대입
// 클래스명(타입) 새로운객체(변수) = (클래스명(타입))이전객체명(데이터값);
cofeee.sipAmericano(); // 이제 다시 cofeee가 Americano04의 객체가 되어서 Americano04의 메소드를 사용할 수 있음
```
문법 :
서브클래스 새로운객체명 = (서브클래스)승급된객체명;

(main클래스)
```java
Beverage04 beverage02 = new Espresso04("에스프레소", 5000.0, 2);
beverage02.showInfo();

// 새로운 객체 esspreeso
Espresso04 espreeso = (Espresso04)beverage02;
// 강등된 새로운 객체 esspreeso는 Espresso04서브클래스의 객체가 되어서
// Espresso04서브클래스의 맴버 변수와 맴버 메소드 사용가능
espreeso.drinkEspresso();
```


#### \# 승급 개념과 배열의 사용
```java
//클래스(타입처럼 써서) 배열 생성
Beverage04[] beverage = {
	new Espresso04("마이뿌레소", 2000.0, 1),
	new Latte04("바나나 라떼",7000.0,"바나나 우유")
};

for (int i = 0; i < beverage.length; i++) {
	System.out.println("--------------------------------------------");
	beverage[i].showInfo();
}
```

(출력)
--------------------------------------------
음료 이름 : 마이뿌레소
단가 : 2000.0원
--------------------------------------------
음료 이름 : 바나나 라떼
단가 : 7000.0원


\*beverage[i]자체가 객체임


#### \# 배열, 반복문 + 선택문 이용
// instanceof 연산자 : 승급된 객체 변수가 수많은 서브 클래스 중에서 어떤 클래스로
//        		   				   생성이 되었는 지를 판단하고자 할 때 사용합니다.
-> 처음에 생성된 곳!이 어디니?
-> 너 고향이 어디니?같은 느낌인가봄

문법 :
객체 instanceof 클래스
-> 결과값 : 논리타입
true, false

ex) beverage[i] instanceof Americano04
-> beverage[i]가 Americano04클래스에 들어 있는거 맞니?

(실습)
```java
for (int i = 0; i < beverage.length; i++) {
	System.out.println("--------------------------------------------");
	beverage[i].showInfo();

	// instanceof : 승급된 객체 변수가 수많은 서브 클래스 중에서 어떤 클래스로
	//              생성이 되었는 지를 판단하고자 할 때 사용합니다.
	if(beverage[i] instanceof Americano04){ // 아메리카노
		Americano04 ameri = (Americano04)beverage[i];
		ameri.sipAmericano();
	}else if(beverage[i] instanceof Espresso04){ // 에스프레소
		Espresso04 espre = (Espresso04)beverage[i];
		espre.drinkEspresso();
	}else if(beverage[i] instanceof Latte04){ // 라떼
		Latte04 latt = (Latte04)beverage[i];
		latt.enjoyLatte();
	}else{ // 차후에...
}
```

(출력)
--------------------------------------------
음료 이름 : 아메리카노
단가 : 4000.0원
아메리카노를 홀짝 홀짝 마십니다.
--------------------------------------------
음료 이름 : 마이뿌레소
단가 : 2000.0원
투입할 샷의 개수는1개입니다.
--------------------------------------------
음료 이름 : 바나나 라떼
단가 : 7000.0원
부드럽고 크리미한 바나나 라떼를 마십니다.


#### \# 향상된 for / 확장 for 구문
배열, 컬렉션에 저장된 요소들을 처음부터 끝까지 하나씩 순차적으로 꺼낼 때 사용하는 반복문
인덱스 관리 필요X -> 코드 간결, 실수 줄여줌
단순히 전체를 보거나 출력할때 사용
선입 선출(FIFO)의 방식으로 출력됨 - 배열[0] 순서부터 배열 [i]까지 출력됨

향상된 for / 확장 for 구문 문법 :

```java
for(타입 단수이름 : 복수이름){ // 타입 : 배열요소의 타입 / 복수이름 : 배열이름 / 단수이름 : 제어변수 i같은 느낌으로 생각하기
	반복할 구문 ;
}

ex)
for(Beverage04 items : beverage){
	반복할 구문;
}
```


#### \# 선입선출 / 후입선출
1) 선입선출(FIFO)
먼저 들어온 데이터가 먼저 나감 (자료구조 : Queue)
ex) 프린터 인쇄 대기열
거의 대부분의 자료구조가 여기에 해당됨

2) 후입선출(LIFO)
마지막에 들어온 데이터가 가장 먼저 나감 (자료구조 : Stack)
ex) 쌓여 있는 접시 꺼내기


#### \# 다른 패키지에 접근 (클래스 자체 내부에 다른 패키지의 클래스를 가져올 수 있다)
```java
import ch04_class.Product01;
// ch04_class라는 패키지의 Product01이라는 클래스를 가져오기
// 다른 패키지에서 가져올 데이터가 public이여야함

// 동일한 패키지가 아니면 import 구문을 사용해야 합니다.
// 반드시 public이어야 합니다.
// 클래스 내의 변수/메소드 또한 public이 아니면 접근이 불가능합니다.
```

(실습)
```java
import ch04_class.Product01;

public class MyProduct {
    static void main(String[] args) {
        Product01 apple = new Product01();
        apple.name = "사과";
        System.out.println("품목이름 : " + apple.name);
    }
}
```

(출력)
품목이름 : 사과


#### \# 추상 메소드
공통적인 특징(어느정도의 가이드라인)을 모으지만
구체적인 내용은 자식에게 맡기기 위해서 필요함
+ 서브 클래스들에게 강제성?을 부여하기 위해서

무언가 행동이나 기능을 해야한다고만 전달하고 구체적인 내용은 제시하지 않는 메소드
"너 뭔가 해야해!! 근데 그건 너가 정해!"라고 수퍼 클래스가 서브 클래스한테 말하는 메소드
결과 : 강제적인 표준규범을 만듬 (표준 규범이 없으면 서로다른 개발자들끼리 여러 이름의 메소드로 만들어서 유지보수가 힘듬)

\* 추상 메소드 : 서브 클래스에게 강제로 오버라이딩을 시키는 메소드 * (중요함!!)

문법 : (사실상 순서는 2 - 1 - 3)
1) 수퍼 클래스의 형식 변경
추상 메소드가 들어간 클래스는 그 자체가 반드시 추상 클래스여야 한다
클래스에 abstract 추가
ex)

```java
public abstract class Beverage05
```
2) 수퍼 클래스의 메소드 형식 변경
클래스의 일반 메소드 만드는 거에서 abstract추가, 중괄호 삭제 후 ;(세미콜론) 추가
접근지정자 abstract 타입 메소드명();
ex)

```java
public abstract void drink();
```
3) 서브 클래스에 (수퍼 클래스의 추상 메소드를 구체화하는) 메소드 추가
문법 : (일반 메소드 만들때와 동일)
```java
접근지정자 타입 메소드명(){
}
```
서브 클래스에 (수퍼 클래스의 추상 메소드를 구체화하는) 메소드를 추가하지 않으면 오류가 남
-> 이래서 "강제성"을 부여한다라고 표현함.


#### \# interface 인터페이스 (다중상속)
인터페이스 내의 모든 메소드는 추상 메소드임
따라서 따로 추상 메소드 형식으로 메소드를 만들지 않아도 자동으로 추상 메소드가 됨
-> 서브클래스는 강제적으로 오버라이딩을 해야 함 (중요함!!)

문법 :
1) (서브클래스)
서브클래스 extends 수퍼클래스 implements 인터페이스

```java
public class Americano05 extends Beverage05 implements WaterAdjustable
```
2) (인터페이스) 인터페이스의 메소드 형식
수퍼 클래스의 추상 메소드 만드는 형식에서 abstract을 뺀 형태
인터페이스의 메소드들은 모두 당연하게도 추상메소드여서 abstract을 빼도 추상 메소드로 인식해서!
-> 접근지정자 타입 메소드명();

But abstract을 생략하지 않고 다 적어도 됨
-> 접근지정자 abstract 타입 메소드명();

3) (서브클래스)
인터페이스의 추상 메소드를 구체화하는 메소드 오버라이딩하기
문법 : (일반 메소드 만들때와 동일)
```java
접근지정자 타입 메소드명(){
	사용할 구문
}
```


#### \# Static키워드를 이용한 static변수
원래 클래스의 맴버 변수를 main클래스에 호출하려면 반드시 main클래스에 객체가 있고
그 객체에 참조 연산자를 이용해서 호출 해야하는데
클래스에 Static 변수 생성시 main클래스에 객체 생성없이 클래스의 맴버 변수를 호출 할 수 있음
\* 굳이 객체까지 필요없을때 static 변수 사용 -> static변수는 클래스 변수라고도 불림.

문법 :

(클래스)
```java
접근지정자 static 타입 맴버변수명 = 맴버변수값;
```

(main클래스)
클래스명.맴버변수명

(클래스)
(실습)
```java
public static String STORE_NAME = "G-CAFE";
```

(main클래스)
```java
System.out.println("어서 오세요~~" + Beverage05.STORE_NAME + "입니다.");
```

(출력)
어서오세요~~G-CAFE입니다.


#### \# final키워드를 이용한 final변수(=상수)
final이 붙어 있으면 편집 불가능한 상수(constant)입니다.
final이 붙은 변수는 더이상 변수라고 부르지 않고 편집 불가능한 상수(constant)라고 부름

문법:
접근지정자 final 타입 맴버변수명 = 맴버변수값;

(클래스)
(실습)
```java
public static final String STORE_NAME = "G-CAFE"; // final 추가
```

(main클래스)
```java
Beverage05.STORE_NAME = "하하하";                 // final이 붙은 변수여서 편집 불가능하기에 에러가 발생함
System.out.println("어서 오세요~~" + Beverage05.STORE_NAME + "입니다.");
```


#### \# private이고 static인 변수 (중요?함!)
```java
private static int beverageCount = 0; // 주문한 커피 잔수

public static int getBeverageCount(){
	return beverageCount;
}
```
객체 없이 호출할 수는 있지만 함부로 접근하지 못하게 private으로 제한해두지만
이 변수를 사용하기 위해서 getter를 써줘서 후회적으로 사용할 수 있게 해줌.


#### \# static이 붙은 메소드
맴버 메소드가 아니라 static메소드라고 불림

- 호출법
1) 일반적 : 원래 맴버 메소드와 같이
문법 :
객체명.맴버메소드명()

2) 다른 방법 : static메소드여서 가능한 방법 (static변수 호출법과 형태가 같음!!)
문법 :
클래스명.static메소드명()

\* static이 붙은 맴버 변수, 맴버 메소드는 (중요!)
객체 생성없이 -> 클래스명.static변수명 / 클래스명.static메소드명 -> 으로 호출 가능!
