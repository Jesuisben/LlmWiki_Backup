Oracle 총정리 (2026.03.16(월) ~ 2026.03.20(금))

#### \# SQL 기본 개념
- SQL언어
표준 언어: 오라클(Oracle), MySQL, PostgreSQL 등 데이터베이스의 종류는 다양하지만,
대부분의 시스템이 이 SQL이라는 표준 언어를 따릅니다. (마치 사투리는 조금씩 달라도 표준어는 통하는 것과 비슷합니다.)

- 용어 정리
가로줄 : 행 (Row (로우))
세로줄 : 렬 (Column (컬럼))

- Schemas (스키마)
유저가 만든 객체들이 있는 곳

- 객체
데이터베이스에서 데이터를 관리하고 뽑아내기 위해 스키마 안에 만들어두는 모든 도구들
ex) 테이블, 뷰, 인덱스, 시퀀스 등

- 파일 왼쪽 * 표시
저장을 하지 않았다는 의미

- 데이터 타입
varchar2 - 가변길이 문자열
char - 고정길이 문자열 (ex 주민등록번호)
숫자 (정수, 실수) - number
날짜 - date

- 테이블 생성시 주의사항
테이블 이름은 일반적으로 복수형을 사용함 (예약어와 구분하려고)
최소 하나 이상의 컬럼이 있어야 생성이 됨

- 문자열 표현
외따옴표( '  ' )를 사용

- SQL에서의 \*표시
All이라는 뜻을 가진 Wildcard 문자

- 개념들
integrity 무결성
violated 반칙

- SQL 진행 순서
from - where - group by - having - select - order by

- SQL 문 분류
1) 연산자 : 값을 계산하거나 비교하여 결과를 내는 도구
ex) +, -, >, <, =, <>, between

2) 키워드, 예악어 : SQL 언어 자체에서 미리 정의된 특별한 의미를 가진 단어
ex) select, from, where 등

3) 함수 : 함수는 보통 뒤에 괄호()가 붙고 그 안에 인자를 넣는 형태
ex) sum(), avg(), concat()



#### \# 단축키
- Edit Connection : F4

- 해당 쿼리 실행 : Ctrl + Enter

- 전체 쿼리 실행 : Alt + X

- 새로운 객체 생성 (테이블, 컬럼, 시퀀스 등) : Alt + Insert

- 찾기 / 바꾸기 : Ctrl + F

- View Xxx (Xxx : Table, Column) : F4

- 새로고침 : F5

- 가장 첫번째 위치로 이동 : Ctrl + Home



#### \# 주석
한 줄 주석 : --



#### \# 우리가 하는 작업은 데이터 모델링



#### \# DBMS (DataBase Management System) : 데이터베이스 관리 시스템
줄여서 \~\~DB라고 부름 ex) 오라클 DB(대용량 데이터에 이용)



#### \# SQL구문 (Oracle PDF P.34)
SQL : Structured Query Language (구조화된 질의 언어)
데이터를 정의, 조작, 제어, 조회하기 위해 사용하는 표준 프로그래밍 언어

- DQL (Data Query Language) : 데이터 질의 언어 (데이터 검색)
주요 명령어 : SELECT (조회)
예시 : 데이터 조회
일상 예시 : 매출 장부 확인 - (핵심 : 데이터를 바꾸지 않고 궁금한 정보만 확인하는 일) - 데이터 읽기

- DML (Data Manipulation Language) : 데이터 조작 언어 (내용물 관리)
주요 명령어 : INSERT, UPDATE, DELETE
실행 주체 : 행(row)단위
예시 : 회원가입, 상품등록
일상 예시 : 주문 받고 커피 만들기

INSERT (삽입) : 오늘 팔기 시작한 '신상 원두' 정보를 메뉴 리스트에 적어 넣는 것
UPDATE (수정) : 원두 가격이 올라서 메뉴판의 '아메리카노 가격'만 지우고 다시 적는 것
DELETE (삭제) : 재고가 떨어진 특정 메뉴를 리스트에서 지우는 것
(핵심 : 메뉴판 틀!은 그대로 두고, 그 안의 "글자(데이터)"만 넣었다 뺐다 하는 일) - 실제 데이터 (알맹이)

- DDL (Data Definition Language) : 데이터 정의 언어 (뼈대 만들기)
주요 명령어 : CREATE, ALTER, DROP
실행 주체 : 객체(object)단위 (테이블, 유저, 시퀀스)
예시 : 구조나 틀 생성, 변경, 삭제
일상 예시 : 카페 인테리어와 메뉴판 만들기

CREATE (생성): 카페 건물을 짓고, '커피 메뉴'라는 이름의 메뉴판(테이블)을 벽에 거는 것. (테이블, 유저, 시퀀스)
ALTER (수정): 메뉴판에 '사이즈 선택' 칸을 새로 추가하거나, 테이블 위치를 바꾸는 것.
DROP (삭제): 장사가 안되어 메뉴판 자체를 떼어버리거나 가게를 철거하는 것.
핵심: 알맹이(커피)가 아니라 '가게 구조나 메뉴판 양식' 자체를 건드리는 일입니다. - 테이블 구조 (껍데기)
틀 안에 있는 데이터를 편집하는 DML과는 다르게 DDL은 틀 자체를 편집함 - 틀 안의 데이터를 편집하지는 않음

// DCL은 몰라도 됨
DCL (Data Control Language) : 데이터 제어 언어 (권한 부여)
주요 명령어 : GRANT, REVOKE
실행 주체 : 사용자(user)단위
예시 :
일상 예시 : 알바생에게는 '포스기 조회' 권한만 주고, 매니저에게는 '가격 수정' 권한까지 주는 것.

TCL (Transaction Control Language) : 트랜잭션(작업 단위) 제어
주요 명령어 : COMMIT(저장) <-> ROLLBACK(취소)
예시 : DML을 통해 조작된 결과를 확정 or 취소하는 등 작업 단위(트랜잭션)을 제어함
일상 예시 : 손님이 카드로 결제했는데 기계 오류가 났을 때, 결제를 완전히 \*\*저장(Commit)\*\*하거나 아예 \*\*취소(Rollback)\*\*해서 돈이 꼬이지 않게 하는 것.
핵심 : 가게 운영의 \*\*'규칙과 안전'\*\*을 관리하는 일입니다. - 작업 확정



#### \# T (Transaction) (트랜잭션)
- 데이터베이스에서 더 이상 쪼갤 수 없는 하나의 완벽한 작업 단위

- 여러 개의 SQL 명령어가 모여서 "이건 무조건 한꺼번에 성공하거나,
아니면 아예 하나도 안 한 걸로 쳐야 해!"라고 묶어놓은 세트
(세트! 인거에 주의)

- 트랜잭션의 존재 이유(계좌 이체 사례)
A가 B에게 10,000원을 송금한다고 가정해 봅시다. 이 작업은 내부적으로 두 단계(여러 개의 SQL명령어)로 나뉩니다.

STEP 1: A의 계좌에서 10,000원을 뺀다. (UPDATE)
STEP 2: B의 계좌에 10,000원을 더한다. (UPDATE)

만약 STEP 1은 성공했는데, 갑자기 은행 서버가 꺼져서 STEP 2가 실패하면
A의 돈은 사라졌는데 B는 받지 못한 대참사가 발생

이런 비극을 막기 위해 STEP 1과 2를 하나의 '트랜잭션'으로 묶음.

\* 둘 다 성공하면? → 확정(COMMIT)
\* 하나라도 실패하면? → 없던 일로 하기(ROLLBACK)



#### \# Dbeaver 기본 세팅 이해
1\. 관리자 서버 세팅
1) SYSDBA권한을 가진 커넥션 생성 ( 이름 : 로컬DB(관리자) )
데이터베이스 - 새 데이터베이스 연결 - Oracle(데이터베이스 종류 선택) - 다음
-> Host(localhost), DataBase(xe), Username(sys), Role(SYSDBA),
Password(oracle), save password(체크), Client(XE) - Test Connection버튼 - driver다운로드 - Connected 나오면 괜찮은거임
-> 아이콘 생성됨

// 용어 정리
Host : 컴퓨터 / localhost : 내 컴퓨터
DataBase(xe) : 데이터 베이스 이름이 xe(xe버전이다)임
Username이랑 Password는 Oracle관리자 계정
Role(SYSDBA) : 맡은 역할이 SYSDBA : System DataBase Administration (시스템 데이터베이스 관리자)
save password(체크) : 자동로그인 (멀티유저 있으면 체크해제)
Client(XE) :
Test Connection : 정상적으로 세팅이 된건지 확인하기

만약에 안되면 Edit DRiver에서 Default Database(xe), Default User(sys)로 바꾸고 확인

2) 생성된 아이콘 이름, 설명 바꾸기
생성된 아이콘 우클릭(Oracle모양 아이콘) - Edit Connection (F4번 단축키) - General
-> Connection name : 로컬DB(관리자), Description : 관리자를 위한 데이터베이스 접속 아이콘입니다.
-> 확인누르기


3) 사용자 생성하기
- A01 스크립트 가져오기 - Active datasource(N/A) 클릭 - 로컬DB(관리자) 선택 후 Select
(스크립트 사용 주체를 설정하는 것)
\* 스크립트 도구상자와 SQL 편집기 사이에 우클릭해서 행 번호 표시 켜기! *
\* 윈도우 - 환경설정 - 연결 - 연결 유형 - Auto-commit by default 체크해제 *

- 스크립트 내의 명령어들 실행
```sql
-- 사용자 계정 생성
-- 계정 생성하고 잠금을 풀어 줍니다.
create user oraman identified by oracle account unlock ;
```
oraman : 아이디
oracle account : 비밀번호
unlock : 생성성

```sql
-- 기본 테이블 저장소를 users로 변경합니다.
-- 할당량(quota)을 무제한(unlimited) 제공해 줍니다.
alter user oraman default tablespace users quota unlimited on users ;
```

(유저에게 할당량을 무제한으로 줌)
```sql
-- oraman에게 접속 권한(connect)과 resource 권한을 부여합니다.
grant connect, resource to oraman ;
```
(아이디 비번이 있더라도 관리자가 권한을 주지 않으면 접속을 못함)
(접속 권한), (oraman에게 준다)    -> oraman에게 접속권한을 grant(수여한다)하다
(resource : 일반 사용자가 할 수 있는 모든 권한)

- 새로운 데이터 베이스 연결
데이터베이스 - 새 데이터베이스 연결
Host(localhost), DataBase(xe), Username(oraman), Role(Normal),
Password(oracle), save password(체크), Client(XE) - Test Connection버튼 - 완료
- xe클릭 후 F4버튼 누르기(이름, 설명 바꾸기) - Connection name : 로컬DB(오라맨), Description : hello - 확인
\* Username(oraman) / Role(Normal) : oraman이라는 유저가 (Normal)일반 사용자라는 뜻 *
\* 아이디(oraman)와 비밀번호(oracle)를 스크립트에서 입력한 명령어대로 사용해야 함 *



#### \# 테이블 생성
로컬DB(오라맨) - Schemas - ORAMAN - Tables - 우클릭 - Create New Table (단축키 : Alt + Insert)
- Name : MEMBERS, Tablespace : USERS, Comment : 회원을 위한 테이블입니다.

- SQL 명령어
```sql
CREATE TABLE ORAMAN.MEMBERS (

)
TABLESPACE USERS;
COMMENT ON TABLE ORAMAN.MEMBERS IS '회원을 위한 테이블입니다.';
```



#### \# Null 여부
컬럼 생성시 not Null = null이 안된다 = 반드시 입력되야 하는 사항이다.



#### \# Primary Key
절대로 중복되면 안되고 반드시 입력되야 하는 사항
ex) 회원가입할때 ID같은 정보
이름 양식 : 테이블명_컬럼명_pk



#### \# VARCHAR2()
소괄호 안에 있는 숫자는 글자 수(최대길이) (영문/숫자 기준으로 최대 20자가 들어갈 수 있다.)
일반적으로 이름은 9바이트면 충분 (한글은 한 글자당 3바이트 차지)



#### \# NUMBER(  ,  )
number(10, 2)을 만들때 Type : number / Precision : 10 / Scale : 2
Precision : 소수점 이하 자릿수를 포함한 수의 전체 길이
Scale : 소수점 이하 자릿수

정수자리(Precision-Scale)와 소수점 자리(Scale)가 들어갈 방을 각각 나누고 시작함

ex) number(4, 2) 일 경우
33.22 -> 33.22로 저장
9.9 -> 09.90으로 저장

- 주의사항
Scale 초과 (소수점 이하 자릿수 초과) : 반올림 되고 에러가 일어나지 않음
ex) number(4, 2) -> 33.311 -> 33.31

Precision 초과 (정수 자릿수 초과) : 에러 발생 (칸이 모자르다!)
ex) number(4, 2) -> 정수자리는 2개 -> 333.31 -> 에러 발생
333.3 -> 에러 발생 (소수점 자리 비어져도 처음부터 정수자리를 나누고 시작해서 의미 없음)



#### \# 테이블의 tap들
Properties(테이블의 구조)
Data(테이블의 데이터)
엔티티 관계도



#### \# 테이블의 컬럼에 데이터 값 넣기 (DML 명령어)
- 컬럼 명시형
```sql
INSERT INTO 테이블 명 (컬럼명) VALUES(데이터값);
```
컬럼의 순서에 맞는 데이터 값을 대응 시켜야 함
테이블에서 정한 컬럼의 순서가 달라져도 데이터 값과 순서가 대응만 되면 상관없음
특정 컬럼(예: 비고란)에 값을 넣고 싶지 않을 때 해당 컬럼을 빼고 작성할 수 있습니다.
특정 컬럼을 빼고 작성할 시 기본값으로 추가 됨 / 혹은 default를 넣어도 기본값이 추가 됨
(컬럼 생성시 기본값 입력시 그 기본값, 기본값 입력하지 않았을 시 Null)


- 컬럼 생략형
```sql
INSERT INTO 테이블명 VALUES (데이터값);
```

테이블을 만들 때 정한 모든! 컬럼에 대해 순서!대로 값을 다 넣어야 함
특정 컬럼만 제외해서 값을 안넣는 행위 불가 (물론! NULL이라는 값?을 넣으면 가능)
만약 컬럼이 5개인데 값을 4개만 넣으면 에러 발생 -> 유지보수 어려움



#### \# count 함수
숫자를 세는 기능
문법 :
```sql
SELECT COUNT(컬럼명) FROM 테이블명;
```



#### \# Commit
영구 저장
반대 개념 : rollback(롤백)



#### \# 시퀀스
중복되지 않는 순차적인 번호를 자동으로 생성해 주는 독립적인 객체(Object)
하나의 시퀀스가 하나의 테이블에 종속되는 관계는 아님
-> 따라서 테이블이 사라져도 시퀀스는 남아있음

\* 시퀀스는 \*\*'함수'가 아니라 '데이터를 보관하고 있는 객체 *

- 시퀀스 생성
커넥션 - 스키마 - oraman - 시퀀스 폴더 - 생성
시퀀스 이름 양식 : 테이블명_seq
문법 : 데이터값 넣는 곳에 적기
시퀀스명.NEXTVAL
```sql
ex) INSERT INTO BOARDS (ID, NAME, AGE) VALUES (BOARDS_seq.NEXTVAL, '현민', 29) ;
```
\* 시퀀스명.CURRVAL도 있는데 안배움 \*

Value : 시작값 (0)
Increment : 증가값 (1)
Min Value : 최소값 (1)
Max Value : 최종값 (1000000)
Cache : 미리 뽑은 값 -> 오늘 20개 뽑고 5개쓰면 ~ 남은 15개는 남는게 아니고 휘발됨
-> 시작 값인 Value부터 Max Value까지 Increment만큼씩 증가하는데 최소값은 Min Value야

Cycle : Value부터 시작해서 Increment만큼 변해서 Max Value까지 간 후에!
Min Value로 돌아가게 하는 설정

- 사이클(Cycle) 기능 때문에 생기는 현상
번호가 Max Value까지 다 차서 다시 처음으로 돌아올 때,
Value(시작값)로 돌아가는 게 아니라 Min Value로 돌아가서 다시 시작합니다.
-> 숫자가 100부터 시작했어도 Max Value인 1000000까지 간 후 다음 숫자는 100이 아니라
Min Value인 1로 돌아감

- Cycle 주의사항 (중요함!!)
만약 기본 키(Primary Key)인 컬럼의 경우
Cycle 기능을 체크 해제 해야함 -> Max Value까지 간 후 다시 숫자가 돌아가면 중복된 데이터가
들어가서 에러가 날 확률이 존재함!



#### \# max함수
해당 컬럼의 가장 높은 수의 값을 가진 행렬을 가지고 오기
문법 :
max(컬럼명)
ex) select max(oid) from orders ;



#### \# 데이터 사전
오라클 데이터 베이스도 유저가 어떤 테이블, 어떤 시퀀스를 가지고 있는지 알아야 함
한마디로 데이터 베이스 관리 장부를 데이터 사전이라고 부름
문법:
user_객체명s
ex) 테이블 : user_tables
시퀀스 : user_sequences



#### \# 참조관계 (Dbeaver 교안 P.94)
0) 충족 요건 (참조 무결성 제약 조건)
main(부모) 테이블은 자식 테이블에서 사용중인 데이터는 삭제가 불가능합니다.
sub(자식) 테이블은 부모 테이블이 가지고 있는 값 또는 null값을 가질 수 있습니다.

1) 메인테이블과 서브테이블은 참조관계임
기본 키(pk)와 외래 키(fk)라는 연결 고리가 설정되어 있어야 함.

2) 
- 메인테이블(master테이블)에 속한
참조 "되는" 컬럼(primary key(pk) - "기본 키")(foreign key에게 "참조됨")
- 서브테이블(detail테이블)에 속한
참조 "하는" 컬럼(foreign key(fk) - "외래 키")(primary key를 "참조함")

2) 무결성이 깨졌다. (무결성을 지키기 위해 참조 무결성 제약 조건을 걸어놓음)
메인테이블에 없는 primary key(인 컬럼)을 서브테이블에 foreign key로 참조하면 무결성이 깨짐.
(기본 키와 외래 키라는 연결 고리에 문제가 생김)



#### \# 관계형 데이터베이스(RDB - 우리가 사용하는건 오라클RDB)
연결 고리가 있다 - 참조 관계이다 - 관계를 맺고 있다.
위의 관계를 가진 데이터베이스를 관계형 데이터 베이스라고 함



#### \# OOP (Object-Oriented Programming)
우리가 공부한 OOP는 Java - 객체를 사용해서 클래스들간의 관계를 이용하니까



#### \# 참조 무결성 제약 조건 (On Delete 옵션)(Dbeaver 교안 P.96)
On Delete 옵션 : pk데이터가 지워졌을때 하는 동작

1) On Delete set null 옵션
ex) 쇼핑몰에서 회원이 탈퇴하더라도, 게시물의 정보를 삭제하지 않고, 남겨 두는 경향이 있습니다. (Dbeaver 교안 P.98)
On Delete set null 옵션 사용 : pk데이터가 지워졌을때 fk값을 null값으로 바꾸기

2) On Delete cascade 옵션
ex) 쇼핑몰에서 고객이 특정 주문을 최소한다고 가정할 때, 주문 상세 정보는 동시에 삭제가 되어야 합니다. (Dbeaver 교안 P.105)
on Delete cascade 옵션 : pk데이터가 지워졌을때 fk값도 같이 삭제하기
(cascade = 연쇄반응)



#### \# Foreign Keys 생성하기
서브테이블 더블클릭 - Properties - Foreign Keys 클릭 후 생성하기
Table : ORAMAN.BOARDS - 오라맨의 BOARDS라는 테이블이다.
Schema : ORAMAN - ORAMAN이라는 스키마.
Reference table(참조할 테이블)에서 메인테이블 선택 후
Unique Key : MEMBERS_id_pk (Primary Key) - 참조할 pk의 유니크 키 입력
Custom Name에 서브테이블명_서브테이블의fk할컬럼명_fk 작성하기 -> boards서브테이블의 writer컬럼을 fk로 만들겠다.
Column에서 writer 선택
On Delete에서 Set Null 선택

ex)
```sql
ALTER TABLE ORAMAN.BOARDS ADD CONSTRAINT BOARDS_MEMBERS_FK FOREIGN KEY (WRITER) REFERENCES ORAMAN.MEMBERS(ID) ON DELETE SET NULL;
```
수정해라 / ORAMAN유저의 BOARDS테이블에 / 제약 조건을 넣어라 / WRITER라는 컬럼을 FOREIGN KEY로 BOARDS_MEMBERS_FK라는 이름으로
참조한다 / ORAMAN.MEMBERS테이블의 ID컬럼을 / ON DELETE 세팅(PK가 삭제되는 경우 행동)은 SET NULL(FK를 NULL값으로 바꾸기)이다.



#### \# 오류코드 해석
integrity constraint (ORAMAN.BOARDS_MEMBERS_FK) violated - 무결성 제약조건을 지키지 않았다.
parent key not found - 당신이 서브 테이블(BOARDS)에 넣으려고 하는 그 ID가, 메인 테이블(MEMBERS)의 PK(부모 키) 목록에 존재하지 않습니다."



#### \# 테이블 생성시 제약 조건 설정 (Dbeaver교안 P.97)
제약 조건은 5개 있음(Oracle교안 P.389) -> "제약 조건"을 "구조"라고 봐서 DDL의 ALTER를 이용하여 바꿈
1\. not null : 컬럼에 null 값을 허용하지 않으므로, 반드시 입력해야 하는 컬럼을 의미합니다

2\. unique : 중복된 데이터의 입력을 허용하지 않는 조건으로, 널 값은 고려 대상이 아닙니다.
내부적으로 인덱스(index)가 생성이 됩니다.

3\. primary key : not null 조건과 unique 조건이 합쳐진 것입니다.
내부적으로 검색 기능의 향상을 위하여 인덱스(index)가 생성이 됩니다.

4\. foreign key : 부모 테이블의 기본 키를 참조하는 서브 테이블의 컬럼에 부여되는 키를 의미합니다.

5\. check : 저장 가능한 값의 범위 또는 조건을 지정하여 설정 값만 허용하기 위한 제약 조건입니다.
예를 들어 '급여 컬럼은 항상 0 이상입니다.', '성별 컬럼은 \[남] 또는 \[여]의 값 중에 하나가 입력이 될 수 있습니다.'
ex) Dbeaver교안 P.57
1) password 코멘트
비밀번호 (members_password_ck)
length(password)>=3 and length(password)<=50

2) 성별 코멘트
성별(members_gender_ck)
```java
gender in('남자', '여자', null)
```

3) 결혼 코멘트
결혼 여부('결혼', '이혼', '미혼' 중 택일), 필수 입력 유도
members_marriage_ck, marriage in('결혼', '이혼', '미혼')

4) 급여
급여(members_salary_ck, salary >= 100)



#### \# 제약 조건 만들기 (Dbeaver 교안 P.108)
제약 조건에 위배 되는 것이 테이블에 있으면 제약 조건 생성 자체가 안됨
따라서 제약 조건을 만들기 전에 테이블부터 확인해야 함

문법 :
테이블명_컬럼명_ck

Constraints -> 생성 -> 이름 : MEMBERS_password_CHECK -> Type : CHECK
-> Expression(표현식) : length(password) >= 3 and length(password) <= 50

- 결과값
```sql
ALTER TABLE ORAMAN.MEMBERS
ADD CONSTRAINT MEMBERS_PASSWORD_CHECK CHECK (length(password) >= 3 and length(password) <= 50) ENABLE;
```
\* not null은 not null이라고 표현 안되고 CHECK라고 표현되는데 이유는 모르겠지만
암튼 Constraints 목록 중에서 Condition을 보고 not null인지 다른 CHECK인지 확인하면 됨\*



#### \# 메인테이블을 삭제할때 (중요함!!)
1) 참조관계 자체를 일단 끊어주면 메인테이블이든 서브테이블이든 그냥 개별로 삭제하면 되는데
2) 참조관계로 연결되어있으면 서브테이블부터 삭제를 하고나서 메인테이브를 삭제해야 한다.



#### \# 폼 유효성 검사 (Validation Check)
사용자가 웹사이트의 입력창(폼)에 데이터를 입력했을 때, 그 데이터가 서버로 전송되기 전에 정해진 규칙에 맞는지 확인하는 과정
목적 : 유효성 검사가 없다면 잘못된 데이터가 데이터베이스(DB)에 쌓여 프로그램이 멈추거나 보안 사고가 발생할 수 있습니다.



#### \# 오류코드 설명
SQL Error \[2290] \[23000]: ORA-02290: check constraint (ORAMAN.MEMBERS_PASSWORD_CK) violated

constraint(제약 조건)의 이름을 설정하지 않으면 오라클에서 SYS_C+숫자 형식으로 임의로 설정해줌
나중에 분석하기 좋게 제약 조건의 이름을 명확하게 설정하자!



#### \# 트랜잭션 개요 (Oracle 교안 P.120~123)
개념 : 데이터를 처리하는 (업무를 처리하는) 논리적인 처리 단위
목적 : 일관성 유지(무결성 보장), 안정적 데이터 복구
특징 : ALL-OR-NOTHING 방식 - 논리적 연관 작업 그룹화가능
(commit을 하면 rollback을 못하고 / rollback을 하면 commit을 못함)

- 트랜잭션 시작과 종료
시작 : 최초 DML 문장이 실행됨과 동시에 트랜잭션 시작
종료 : commit(영구 저장) 명령어 또는 rollback(이전 작업 취소) 명령어를 사용하면 종료

\** DML 문장은 마지막에 반드시 commit이나 rollback을 해야 함 ** (중요함!)
\** DDL 문장은 automatic commit이여서 자동으로 commit돼서 마지막에 commit이나 rollback을 안해도 됨 ** (중요함!)



#### \# 트랜잭션 제어어 (Oracle 교안 P.124)
가볍게 알기
- 저장점 : 롤백해서 돌아가는 곳
형식 :
저장점 만들기 - savepoint 레이블_이름 ;
저장점으로 이동 - rollback to 레이블_이름 ;



#### \# 데이터 디자인 중에서 중요한 것
넣으려는 데이터 값이 제약 조건에 위배되지 않는지!
제약 조건을 바꿀 때 이미 들어가 있는 데이터 값에 위배되지 않는지!



#### \# DQL (Data Query Language) (A05스크립트!!에 작성함)
- select 명령어 사용
```sql
select *|{[distinct] column 리스트|표현식, [alias] from 테이블 1[, 테이블 2, …
] [where condition] [group by column] [having column] [order by column];
```
대괄호 안에 있는건 선택사항 -> select랑 from은 필수임


- 단순 컬럼 조회 (2개 이상의 컬럼은 콤마로 연결)
문법 :
```sql
select 컬럼명, 컬럼명 from 테이블명 ;
```
ex)
```sql
SELECT name, price FROM products ;
```
조회해라/name과 price 컬럼들을/products테이블에서

- distinct
중복된 데이터는 1개만 표시
```sql
select distinct category from products ;
```

// 파생 컬럼 (알리아스 Alias)(별칭, 가명)
실제로는 존재하지 않는 컬럼
select로 조회할때만 일회성으로 보여주는 컬럼
문법 :
1) 컬럼명 자체를 바꾸기 (산술연산 이용)
ex) select name, price, price + 1000 from products ;

2) as 사용
컬럼명 as 파생컬럼명
ex) select name, price * 12 as annual_price from products ;

- 주의사항
알리아스에 공백을 넣으면 에러가 발생하지만
굳이 공백을 넣고 싶으면 쌍따옴표를 이용해 알리아스를 생성하면 됨
ex) select name, price * 12 "annual price" from products ;

// 문자열 결합 ( || 연결 연산자 이용) (Java의 + 결합 연산자)
ex) select '상품명 : ' || name || ', 가격 : ' || price || '원' as result from products ;
-> 상품명 : 아메리카노01, 가격 : 6000원

// 행의 제한 (필터링) (조건 검색) \[where condition] - condition에 연산자들 넣기
ex) select * from products where num = 1 ; -> SQL에서 = 는 같다라는 의미 (할당X)
조회해라 / 모두 / products테이블에서 / num이 1인
-> products테이블에서 num컬럼(Column)의 값이 1인 행(Row)들만 필터링하여,
해당 행의 모든( * ) 컬럼(Column) 데이터를 조회하라
사용법 : 상품 페이지 적용에 사용

// and 연산자 (2개 이상 필터링 동시 충족)
문법 :
조건 and 조건
ex) SELECT * FROM products WHERE price = 3000 AND point = 6 ;
조회하라 / 모든 컬럼을 / products테이블에서 / price컬럼의 값이 3000이고,
point컬럼의 값이 6인 행들만

- 범위표현
```sql
SELECT * FROM products WHERE price >= 3500 AND price <= 4500 ;
```
(3500이상이고 4500이하)

-> between절 사용하여 대체 표현 (and 연산자의 범위표현 같은 결과)
문법 : 컬럼명 between 조건 and 조건 (이상, 이하 개념) (초과, 미만 X) (문자열사용 가능)
ex) SELECT * FROM products WHERE price BETWEEN 3500 AND 4500 ;

// or 연산자 (복수 조건 중 한개만 충족시)
ex) SELECT * FROM products WHERE price = 4000 or price = 6000 ;
조회하라 / 모든 컬럼을 / products테이블에서 / price컬럼의 값이 4000이거나, 6000인 행들만

-> in절 사용하여 대체 표현
문법 : 컬럼명 in (조건, 조건)
ex) select * from products where price in (4000, 6000) ;
조회하라 / 모든 컬럼을 / products테이블에서 / price컬럼의 값이 4000이거나. 6000인 행들만

// <> 연산자 (Java의 !=와 같은 의미)
같지 않다라는 의미
ex) select * from products where point <> 5 ;
조회하라 / 모든 컬럼을 / product테이블에서 / point컬럼의 값이 5가 아닌 행들만
\* !=연산자는 예전에는 SQL에서 사용하지 못했지만 최근에는 편의를 위해 가능해짐 *

// is 연산자
null 값을 조건에 넣기 위해 사용
문법 : 컬럼명 is null
ex) select * from products where price is null ;
조회하라 / 모든 컬럼을 / products테이블에서 / price컬럼의 값이 null인 행들만
\* null값은 비교 판단할 수 업는 미지의 값이기에 관계 연산자를 사용하지 못한다 *

// like 연산자 (중요함!!)
문자열의 일부분만 일치하는 데이터를 찾을 때 사용하는 비교 연산자
wildcard문자와 함께 사용 / 문자열 좌 우에 붙여서 사용
언더라인, 퍼센트 같이 사용 가능
1) _ (언더라인) : 무조건 1글자 (중복 사용 가능)
2) % (퍼센트) : 0개 이상의 문자열 (0개 이상 : 아무글자가 없어도 만족)
문법 :
- _ (언더라인) : 컬럼명 like '_문자열' / 컬럼명 like '문자열_'
- % (퍼센트) : 컬럼명 like '%문자열' / 컬럼명 like '문자열%'
ex)
이름이 두 글자이면서, 두번째 글자가 \[순]인 회원 : select * from members where name like '\_순' ;
이름의 첫 번째 글자가 \[선]인 회원 : select name from members where name like '선%' ;
이름 중에 \[연]이라는 글자가 있는 회원 : select name from members where name like '%연%' ;
이름의 2 번째 글자가 \[순] 인 회원 : select * from members where name like '\_순%' ;
이름의 끝자리가 \[후]인 회원 : select * from members where name like '%후' ;

사용법 : 연관검색어?

// not 연산자
부정어 만들때 사용
문법 :
1) 일반적
not 연산자
ex) 카테고리가 'bread'가 아닌 항목
```sql
SELECT * FROM products WHERE CATEGORY NOT IN ('bread') ;
```


2) is 연산자
is not null
ex) 게시물 작성자가 확실한 게시물
```sql
SELECT * FROM boards WHERE WRITER IS NOT NULL ;
```

\* 간단한건 !=나 <>사용해도 됨 *

// 행의 정렬 (order by 키워드 전 알아야 함)
- 오름차순 : 작은 수부터 큰 수까지 (우리가 아는 순서대로?)
숫자 : 1 / 2 / 3
문자 : A / B / C
날짜 : 2009-01-23 / 2009-02-22 / 2009-04-15 (최초날짜부터)
null : 가장 마지막에 추출됨

- 내림차순 : 큰 수부터 작은 수까지
숫자 : 3 / 2 / 1
문자 : C / B / A
날짜 : 2009-04-15 / 2009-02-22 / 2009-01-23 (최근날짜부터)
null : 가장 먼저 추출됨

// order by 키워드 (order도 키워드, by도 키워드)
정렬하는 키워드
1) asc (Ascending) : 오름차순
2) desc (Descending) : 내림차순
문법 :
```sql
order by 컬럼 (asc) ; - asc는 안써도 됨, 기본값이여서
order by 컬럼 desc ;
```
 ex) 카테고리별로 정렬하고, 같은 카테고리에서는 가격이 높은 순으로 정렬하세요.
```sql
select * from products order by category asc, price desc ;
```

\* 카테고리에 어떤 것들이 있는지 조회하기 \*
```sql
SELECT DISTINCT category FROM products ORDER BY category ASC ;
```
distinct사용 : category종류만 보는 것이기에 중복된 것 제외

// 실제 사용법
1) 모든 상품 목록 조회
```sql
SELECT * FROM products ;
```

2) 상품에 대한 상세 보기 / 상품 주문 페이지
```sql
select * from products where num = 1 ;
```

3) 데이터 필터링할때 (하한값얼마 상한값얼마에서 찾기)
```sql
select * from products where price in (4000, 6000) ;
```

// dual 테이블 (Oracle 교안 P.217) (A06스크립트)
정의 : SYS 관리자가 소유하고 있는 1행 1열의 (가상) 테이블
특징 : 모든 USER가 사용가능
용도 : 간단한 계산기의 용도 / 특정 함수의 검증
문법 :
```sql
select 계산식 from dual ;
```
ex)
- 단순 계산
```sql
select 5*3 from dual ; -> 5*3이라는 컬럼(열)에 1이라는 행(row)에 값이 15로 나옴
```

-  power함수 계산 (제곱 계산)
문법 : power(밑, 지수)
```sql
select power(2, 10) from dual ; -> 2의 10제곱 계산
```

- 그냥 문자열은 그대로 조회됨
```sql
select 'hello' from dual ; -> 그대로 hello 조회
```

- upper / lower 함수
문자열 변환 함수
1) upper : 대문자로 변환
2) lower : 소문자로 변환
문법 : upper('소문자') / lower('대문자')
ex) select upper('hello'), lower('HELLO') from dual ;
-> HELLO와 hello 조회

- mod 함수
나누기의 나머지 계산
문법 : mod(나눌값, 나누는값)
ex) select mod(14, 5) from dual ;
-> 4 조회

// length 함수
문자열의 길이 표현
문법 : length(컬럼명)
ex)
```sql
select length(name) as name_length from products ;
```
조회해라 / name컬럼의 데이터의 문자열 길이를 /
name_length라는 알리아스로 / products테이블에서

// substr 함수
문자열 특정 부분 추출하는 함수
인덱스가 Java와 다르게 1로 시작 -> Oracle은 1베이스이다.
문법 :
substr(추출될문자열인컬럼명, 추출시작위치, 추출할문자갯수)
ex) 방식이 Java의 오버로딩 방식과 유사함
```sql
select substr(password, 1, 3) from employees ; -> 1부터 3 인덱스의 문자열 조회
select substr(password, -2, 2) from employees ;
```
-> -2부터 -1 인덱스의 문자열 조회 -> (abcd) => c와 d 조회
\* 추출할 문자 갯수를 생략할시 문자열 끝까지 추출함 \*

// concat 함수
문자열 결합 함수
간편하게 ||을 사용해도 됨
문법 : concat('문자열', '문자열') - 2개의 인자(요소)밖에 사용못함
따라서 3개이상부터는 중첩시켜야 함께
ex) select concat(name, ' - ') from products ;
중첩 : concat(concat(name, ' - '), company)

// replace 함수
특정 문자 치환 함수
문법 :
replace(컬럼명, 치환될문자열, 치환할문자열)
ex)
```sql
select replace(name, '아', '★') from products ;
```

// instr 함수
문자열 내에서 검색하고자 하는 문자열의 위치를 정수값으로 변환해주는 함수
검색하고자 하는 문자열이 문자열 내에 없을 시 0으로 조회됨
문법 :
instr(특정문자열, 검색하고자하는문자열)
instr(컬럼명, 검색하고자하는문자열)
ex)
SELECT instr('컴포즈커피', '가'), instr('메가커피', '가') FROM dual ; -> 0과 2
SELECT * FROM products WHERE instr(company, '가') > 0 ;
-> company 컬럼에 '가'라는 글자가 포함된 행

// padding 함수
lpad (left pad) : 왼쪽 정렬
rpad (right pad) : 오른쪽 정렬
문법 :
lpad (컬럼명, 전체길이, 채울문자)
-> 전체길이를 정하고 컬럼의 데이터를 가져와서 "왼쪽부터" 빈 공간에 채울문자로 채움
rpad (컬럼명, 전체길이, 채울문자)
-> 전체길이를 정하고 컬럼의 데이터를 가져와서 "오른쪽부터" 빈 공간에 채울문자로 채움
ex)
```sql
SELECT company, lpad(company, 10, '*'), rpad(company, 10, '*') FROM products ;
```

// trim 함수
문자열에서 특정 문자열을 지우는 함수
문법 :
trim(문자열) : 공백 지우기
trim(문자열, 지울문자) / trim(컬럼명, 지울문자)
ltrim이나 rtrim으로 응용 가능
ex)
```sql
SELECT trim('  aa ') FROM dual ;
SELECT rtrim('xxaaxx', 'x') FROM dual ;
SELECT ltrim('xxaaxx', 'x') FROM dual ;

SELECT rtrim(company, '커피') FROM products ;
```
-> company 컬럼에 '커피'라는 단어 모두 지워 주세요.

// abs 함수 (Java의 Math 클래스 같이 공부하기)
절대값으로 변환해주는 함수
문법 :
abs(절대값으로_바꿀_수)
ex)
```sql
select abs(-5) from dual ;
```

// 반올림 함수 (round, trunc)
- round() - 포인트 반올림
정수값으로 반올림
- trunc() - 가격 절삭
나머지 값 버림
문법 :
round(실수, 몇번째소수점까지반올림해서표현할지)
trunc(실수, 몇번째소수점까지표현할지)
ex)
```sql
SELECT round(1234.567), trunc(1234.567) FROM dual ;
```
-> 1235 / 1234
```sql
SELECT round(1234.567, 2), trunc(1234.567, 2) FROM dual ;
```
-> 1234.57 / 1234.56

// 올림 함수 (ceil, floor)
ceil (ceiling) : 소수점 이하가 뭐든 무조건 정수 숫자 하나 올리고 소수점 버림
floor : 소수점 이하가 뭐든 무조건 소수점 버림
ex)
```sql
SELECT ceil(1234.567), floor(1234.567) FROM dual;
```
1235와 1234

// sqrt 함수
루트 표현 함수
문법 :
sqrt(루트할_숫자)
ex)
SELECT sqrt(5) FROM dual ; -> 2.23606797749978969640917366873127623544

\* 함수의 중첩 \*
SELECT price, sqrt(price), round(sqrt(price), 2) FROM products ;

// sysdate 함수
현재 날짜 함수 (단위 : day 일)

ex) 오늘 날짜와 입고 날짜의 차이
```sql
select sysdate - inputdate from products ;
```

7일 후 날짜
```sql
select inputdate + 7 from products ;
```

// add_months 함수
개월 더하는 함수
문법 :
add_months(날짜컬럼, 더할개월수)
ex) 다음 월 같은 날짜
```sql
select add_months(inputdate, 1) from products ;
```



#### \# 단일행(single row) 함수
각각의 행에 하나씩 적용이 되는 함수
ex) upper, lower 등
- 그룹(집계) 함수를 제외하고 대부분은 단일행 함수임
- 단일행 함수는 투입 : 1개, 산출 : 1개 / 그룹 함수는 투입 : 여러개, 산출 : 1개
ex) upper에 투입한 값이 1개고 산출도 1개임
sum은 투입한 갑이 여러개이고 산출은 sum값 1개임



#### \# 그룹(집계) 함수 (Oracle 교안 P.296) (대략 5개 정도 있음)
전체를 대상으로 하나의 통계적인 수치 데이터를 추출해 내는 함수

1\. avg 함수 : 평균, 널 값은 무시 / 숫자 가능 / 문자 및 날짜 불가능
문법 :
avg(컬럼명)
ex) stock : 10, 20, 30, null -> 60나누기 3 -> null값을 무시함.
평균 가격
```sql
SELECT AVG(PRICE) AS AVG_PRICE FROM PRODUCTS;
```

2\. count 함수 : 숫자 카운팅 함수 (몇개인지)
문법 :
1) count(\*) : null 값을 포함하여 전체 행수를 표현합니다 -> stock -> 4개
2) count(표현식) : null 값을 제외한 개수를 표현합니다.  -> stock -> 3개
ex) SELECT COUNT(COMPANY) FROM PRODUCTS; -> 47개 (회사종류 - 중복포함)
3) count(distinct 표현식) : 중복된 데이터는 하나로 개수를 표현합니다. -> stock -> 3개
ex) SELECT COUNT(DISTINCT COMPANY) FROM PRODUCTS; -> 16개 (회사종류 - 중복제외)

응용 : null값인 price컬럼의 데이터 갯수 (null값 포함한 수 - null값 제외한 수)
ex)
```sql
SELECT count(*) - COUNT(PRICE) AS "단가 널 갯수" FROM PRODUCTS;
```
-> 쌍따옴표는 파생컬럼의 이름에 공백을 넣을때 사용함

3\. max : 최대 값, 널 값은 무시 / 숫자 가능 / 문자 및 날짜 가능
문법 :
max(컬럼명)
ex)
```sql
SELECT MAX(PRICE) AS MAX_PRICE FROM PRODUCTS;
```
응용 : 문자열을 숫자로 생각해서 가나다 순 이름 찾기
```sql
SELECT max(name) FROM members ;
```

4\. min : 최소 값, 널 값은 무시 / 숫자 가능 / 문자 및 날짜 가능
문법 :
min(컬럼명)
ex)
```sql
SELECT MIN(PRICE) AS MIN_PRICE FROM PRODUCTS;
```
응용 : 문자열을 숫자로 생각해서 가나다 순 이름 찾기
```sql
SELECT min(name) FROM members ;
```

5\. sum : 합계, 널 값은 무시 / 숫자 가능 / 문자 및 날짜 불가능
문법 :
sum(컬럼명)
ex)
전체 재고 합계
```sql
SELECT SUM(STOCK) AS TOTAL_STOCK FROM PRODUCTS;
```
\* avg함수는 사실 sum 함수와 count 함수의 결합으로 가능
-> SELECT SUM(STOCK) / count(stock) AS avg_STOCK FROM PRODUCTS;


#### \# group by 함수 (Oracle 교안 P.309)
특정 컬럼 기준 데이터 그룹화 -> (중요함!)행에 개별 데이터가 아닌 범주화된 데이터들이 나옴!!!!
그룹화할컬럼은 범주형 데이터여야 함 (연속형 데이터는 안됨) -> 그래야 행에 표현 가능
\* 행에 컬럼(열)같은 특별한 조건을 추가하는 느낌? \*

\*\* group by를 사용할때 select 절에 올 수 있는 2가지 경우 **
1) 그룹 함수
2) GROUP BY 절에 명시하여 그룹화한 컬럼
-> 그룹화된 행(요약본)과 그룹화되지 않은 행(개별 데이터)은
	출력되는 행의 개수(데이터의 입자감)가 서로 달라 하나의 표에 담을 수 없기 때문

문법 :
```sql
select 일반컬럼명, 그룹함수(컬럼명)
from 테이블명
group by 그룹화할컬럼명
```

ex) 남녀 각각 몇명인가요?
```sql
SELECT gender, count(*)
FROM members
GROUP BY gender ;
```
-> gender컬럼에 여자, 남자나오고 count(*)에 각 인원 수 나옴

카테고리별 평균 가격
```sql
SELECT CATEGORY, AVG(PRICE) AS AVG_PRICE
FROM PRODUCTS
GROUP BY CATEGORY;
```

카테고리별 최고 가격 (높은 순)
```sql
SELECT CATEGORY, MAX(PRICE) AS MAX_PRICE
FROM PRODUCTS
GROUP BY CATEGORY
ORDER BY MAX_PRICE DESC;
```

카테고리별 회사별 최고 가격(높은 순) / 2개 이상의 그룹화 + 정렬
```sql
SELECT category, company, max(price) AS max_price
FROM products
GROUP BY category, company
ORDER BY category, company desc;
```
\* 2개 이상의 그룹화를 할 시 순서에 따라서 그룹화의 계층 구조가 다르게 보임 \*


#### \# group by 함수 + having 절
having절은 group by 함수에다가 필터링(조건)을 추가해줌
(where 절 같은 것)

\* having 절에는 단일행 함수는 못쓰고 오직 그룹 함수만 쓸 수 있음 *
-> having은 그룹화한 데이터만 처리 가능
\* 반대로 where 절에는 그룹 함수는 못쓰고 오직 단일행 함수만 쓸 수 있음 *
-> where은 개별 데이터만 처리 가능

having 절에는 avg / count / max / min / sum만 사용 가능
\* having 절은 group by 함수에 종속되어 있음 *
문법 :
```sql
group by 그룹화할컬럼명 having 조건식
```

ex) 회사별 상품 개수를 파악하되 3개이상인 회사 정보만 출력
```sql
SELECT COMPANY, COUNT(*) AS CNT
FROM PRODUCTS
GROUP BY COMPANY
HAVING count(*) >= 3
ORDER BY company;
```

- where과 having을 나눈 이유
언뜻 where과 having은 둘다 필터링(조건설정)을 한다는 의미에서 같아보이고
나누는게 의미 없어보임
이유:
1) 계산의 효율성
SQL이 진행되는 순서가 from - where - group by - having - select - order by 인걸 보면
1차적으로 (where)개별 데이터들을 걸러주고 (group by)걸러진 데이터를 그룹화 해주고
2차적으로 (having)그룹화한 데이터를 걸러주면 컴퓨터(DB)가 처리해야 할 데이터 양이
확 줄어들게 됨

2) 데이터의 성격 (집계 데이터의 존재 유무)
where단계에서는 아직 데이터들이 그룹화하지 않고 개별 데이터로 존재하기에 처리할 수 없음
따라서 그룹화한 데이터를 처리하려면 where(개별 데이터 필터링)이 끝나고 나서
진행 순서에 따라 group by로 그룹화가 되고나서 그룹화한 결과값을
having으로 처리할 수밖에 없음



#### \# Ansi 조인

Oracle 조인과 다른 문법적으로 다른 정석적인 SQL 문법
ANSI 조인 : join과 on 절 사용
```sql
SELECT members.name, boards.SUBJECT
FROM members JOIN boards
ON MEMBERS.ID = BOARDS.WRITER ;
```



#### \# Join (조인) (Oracle 교안 P.348)
서로 다른 두 개 이상의 테이블을 \*\*공통된 컬럼(연결 고리)\*\*을 기준으로 합쳐서,
마치 하나의 테이블처럼 데이터를 조회하는 기술
기본값 : 이너 조인

- 서로 다른 테이블들이 참조 관계일 필요는 없음
조인의 핵심은 \*\*"두 테이블의 컬럼 값이 서로 매칭되는가"\*\*이지,
"두 테이블이 미리 부모-자식 관계로 묶여 있는가"가 아니기 때문

\* 테이블명에 알리아스(별칭) 사용 시 as를 사용하면 안됨 - 컬럼은 as 혹은 생략 가능

- 소유격 연산자 ( . )
Join이 된 SQL구문에서 특정 테이블의 특정 컬럼임을 표시하기 위해
소유격 연산자 (멤버 참조 연산자)를 사용해서 표현함
(마치 Java에서 객체.맴버변수 하는 느낌)
문법 :
테이블명.컬럼
ex) members.name

// 테이블에 알리아스(별칭) 사용 시 테이블의 컬럼들도 모두 테이블의 별칭과 대응되게 바꿔줘야 함
-> from members m 이라고 별칭 사용시 -> select member.name을 m.name이라고 해야 함

- 연산 방식에 따른 분류
1\. Equi Join
동일한 의미의 컬럼을 기준으로 = 연산으로 조인하는 것을 말합니다.
문법 :
```sql
select 메인테이블명.컬럼, 서브테이블명.컬럼
from 메인테이블명, 서브테이블명
Where 메인테이블명.기본키 = 서브테이블명.외래키
```
ex)
```sql
SELECT members.name, boards.subject
FROM members, boards
WHERE MEMBERS.ID = BOARDS.WRITER ;
```
-> 이너 조인임과 동시에 Equi 조인임

- 별칭 사용 : 긴 테이블 이름을 짧은 alias 사용하기
```sql
SELECT m.name, b.SUBJECT
FROM members m JOIN boards b
ON m.ID = b.WRITER ;
```

- 추가적인 필터링은 and 연산자 사용
```sql
SELECT m.name, b.SUBJECT
FROM members m JOIN boards b
ON m.ID = b.WRITER
AND m.name IN('안중근', '조마리아') ;
```


2\. Non-Equi Join
동일 컬럼이 없이 non-Equal 연산자로 조인하는 것을 말합니다
- 내부 처리 방식
1) Inner Join (A와 B의 교집합)
조인 조건을 만족하는 행만 표시합니다.
방향성 - 없음
문법 :
```sql
select 컬럼리스트
from 메인테이블 (별칭) (inner) join 서브테이블 (별칭)
on 메인테이블의컬럼 = 서브테이블의컬럼 ;
```

ex1) 게시물을 남긴 사람들만 볼래요.
id와 writer가 일치하는 행들 중에서 name컬럼과 subject컬럼에 있는 행들을 조회
```sql
SELECT m.name, b.SUBJECT
FROM members m JOIN boards b
ON m.ID = b.WRITER ;
```

ex2) 각 회원들의 게시물 작성 건수 (조인 + group by)
```sql
SELECT m.id, m.Name, count(*)
FROM members m JOIN BOARDS b
ON m.id = b.writer
group by m.id, m.NAME ;
```


2) Outer Join (A or B or A와 B의 합집합)
조인 조건에 만족하지 않는 행도 추출됩니다.
방향성 - 있음 (단방향)
방향성에 따라 조회되는 값이 달라짐
방향성에 따라 3가지로 나눔


2-1) left outer join (래프트 아우터 조인)
방향성 : 왼쪽 -> 오른쪽
왼쪽 테이블 + 테이블들의 교집합
문법 :
```sql
select 컬럼리스트
from 메인테이블 (별칭) left outer join 서브테이블 (별칭)
on 메인테이블의컬럼 = 서브테이블의컬럼 ;
```

ex1) 게시물을 남기지 않은 사람도 같이 볼래요.
```sql
SELECT m.name, b.SUBJECT
FROM members m LEFT OUTER JOIN BOARDS b
ON m.ID = b.WRITER ;
```

ex2) 각 회원들의 게시물 작성 건수(미작성자도 포함) (조인 + group by)
```sql
SELECT m.id, m.Name, count(writer)
FROM members m LEFT OUTER JOIN BOARDS b
ON m.id = b.writer
group by m.id, m.NAME ;
```


2-2) right outer join (라이트 아우터 조인)
방향성 : 오른쪽 -> 왼쪽
오른쪽 테이블 + 테이블들의 교집합
문법 :
```sql
select 컬럼리스트
from 메인테이블 (별칭) right outer join 서브테이블 (별칭)
on 메인테이블의컬럼 = 서브테이블의컬럼 ;
```

ex) 작성자가 누구인지 모르는 데이터도 같이 볼래요.
```sql
SELECT m.name, b.SUBJECT
FROM members m full OUTER JOIN BOARDS b
ON m.ID = b.WRITER ;
```


2-3) full outer join (풀 아우터 조인)
방향성 : 왼쪽 <-> 오른쪽
왼쪽, 오른쪽 테이블의 합집합
문법 :
```sql
select 컬럼리스트
from 메인테이블 (별칭) full outer join 서브테이블 (별칭)
on 메인테이블의컬럼 = 서브테이블의컬럼 ;
```

ex) 작성자가 누구인지 모르는 데이터도 같이 볼래요.
```sql
SELECT m.name, b.SUBJECT
FROM members m full OUTER JOIN BOARDS b
ON m.ID = b.WRITER ;
```

- Self Join (안배움)
- Cross Join (안배움)



#### \# 다차원 조인 : 3개 이상 조인 하는 것
pk, fk 개념과 참조 무결성 제약조건, 제약조건의 개념을 잘 알고 있어야 함.



#### \# 서브 쿼리
쿼리 안에 쿼리를 넣는 것
- 개념
메인 쿼리 : SELECT name, salary FROM members WHERE salary = (             ) - 나중에 실행됨
서브 쿼리 : SELECT min(salary) FROM members - 먼저 실행됨

- 목적 (최적화) (영어 문장에서 that절을 쓰는 느낌인듯)
아이오(I/O - input, output)를 줄이려고
/ 원래였으면 아이오가 2번 발생하는데 이렇게 줄이면 1번 발생함

+(중요함!!!) 원래 SELECT name FROM members WHERE salary = MIN(salary);
이렇게 하고 싶은데 이러면 where에 그룹함수 min()이 들어가서 오류가 나서
select에는 min()을 사용할 수 있으니 서브쿼리를 이용하는 것


ex)
최소 급여자의 이름과 급여를 출력
1) 최소 급여 계산 (계산값 = 100)
```sql
SELECT min(salary) FROM members ;
```

2) 계산값을 넣어서 최소 급여자 찾기
```sql
SELECT name, salary FROM members WHERE salary = 100 ;
```

위의 두 문장을 한 번에 해결하기
```sql
SELECT name, salary
FROM members
WHERE salary = (SELECT min(salary) FROM members) ;
```

- 사원들의 평균 월급보다 많이 받는 사원들
```sql
SELECT name, salary
FROM members
WHERE salary > (SELECT avg(salary) FROM members) ;
```

- 관리자가 '김구'인 사원들
```sql
SELECT * FROM members
WHERE manager = (SELECT id FROM members WHERE name = '김구');
```
-> 그냥 manager = '김구'라고 해도 되는데
-> 굳이 where name = '김구'인 id를 manager와 같다라고 표현하고 싶어서 서브쿼리 표현
-> '김구'가 동명이인이 있을 수도 있어서 unique key인 id를 이용한 것

- '이순신'의 급여 보다 낮은 급여를 받는 사원들 정보
```sql
SELECT name, salary FROM members
WHERE salary < (SELECT salary FROM members WHERE name = '이순신' ) ;
```



#### \# 단일행 서브쿼리 : (=, <>, >, >=, <, <=) 사용 - (Java에서 비교 연산자도 1대1 비교였음)
위의 서브쿼리들은 단일행 서브쿼리들임
비교 대상자들이 1대1 비교 (ex - 한 사람 한 사람씩 비교함)

- 메인 쿼리가 1개 있고 서브 쿼리가 2개 있는 경우
관리자가 '김구'인 사원들중에서 평균 급여보다 낮은 급여를 받는 사원들 정보

```sql
SELECT name, salary
FROM members
WHERE 관리자가 '김구'인 사원들 and 평균 급여보다 낮은 급여를 받는 사원들
```

SQL)
```sql
SELECT name, salary
FROM members
WHERE manager = (SELECT id FROM members WHERE name = '김구')
AND salary < (SELECT avg(salary) FROM members);
```



#### \# 다중행 서브쿼리 : (= 대신 -> in, any, all) 사용
- 기본 원리 예시
(잘못된 예)
```sql
SELECT name, manager
FROM MEMBERS
WHERE manager = (SELECT id FROM members WHERE name IN('김구', '유관순');
```
-> 대응 되는 것이 1대 2관계여서 (=)을 쓰면 안됨!! (중요함!!!)

(정상적인 예)
```sql
SELECT name, manager
FROM MEMBERS
WHERE manager IN (SELECT id FROM members WHERE name IN('김구', '유관순'));
```
-> 이렇게 일대다 관계일때는 in을 사용함

```sql
SELECT name, manager
FROM MEMBERS
WHERE manager IN ('kim9', 'soon');
```
-> 이렇게 안쓰는 이유는 manager는 중복될 수 있는 값인데 ID는 중복하지 않는 값으로
설정해놓아서 굳이 굳이 서브 쿼리를 써서 ID로 찾으려고 하는 것


// 다른 예시들
게시물 작성자의 이름과 생일과 성별
```sql
SELECT name, birth, gender
FROM members WHERE id IN (SELECT DISTINCT writer FROM boards WHERE writer IS NOT null);
```
-> members가 메인테이블이고 boards가 서브테이블일때 보통 PK와 FK를 많이 이용함

- '이혼'하지 않은 사원들 목록
```sql
SELECT name, marriage
FROM members
WHERE id not IN (SELECT id FROM members WHERE marriage in ('이혼'));
```



#### \# 다중컬럼(열) 서브쿼리
- 성별로 최저 급여자의 이름과 급여와 성별
```sql
SELECT gender, min(salary) FROM members GROUP BY GENDER ;

SELECT name, salary, gender
FROM MEMBERS
WHERE (gender, salary) IN (SELECT gender, min(salary) FROM members GROUP BY GENDER) ;
```
-> 연산자 우선 순위때문에 소괄호 사용
/ 각각 대응하기 위해서 where뒤에 2개의 컬럼 + 서브쿼리안에 컬럼도 2개

- 결혼 유형별 최저 급여자의 이름, 급여, 결혼 유형
확인하기
```sql
SELECT DISTINCT marriage FROM members ;
```

서브쿼리 만들기
```sql
SELECT marriage, min(salary) FROM members GROUP BY marriage ;

SELECT name, salary, marriage
FROM MEMBERS
WHERE (marriage, salary)
IN (SELECT marriage, min(salary) FROM members GROUP BY marriage) ;
```

- 주소별 최대 급여자의 이름과 주소와 급여 컬럼
확인하기
```sql
SELECT DISTINCT address FROM members ;
```

서브쿼리 만들기
```sql
SELECT address, max(salary) FROM members GROUP BY address ;

SELECT name, address, salary
FROM members
WHERE (address, salary)
IN (SELECT address, max(salary) FROM members GROUP BY address);
```



#### \# ERD(Entity-Relationship Diagram)
개체-관계 모델을 시각적으로 표현한 도표
데이터베이스를 설계할 때 어떤 데이터들이 필요하고,
그 데이터들이 서로 어떤 연관성을 가지는지 한눈에 파악하기 위해 그리는 일종의 설계도

- 핵심요소 : 엔티티(Entity 개체), 속성(Attribute), 관계(Relationship)

- Dbeaver 엔티티 관계도
로컬DB(오라맨) 커넥션 - 스키마 - ORAMAN 더블클릭 후 엔티티 관계도

- 일대다 관계
검은색 동그라미 : "다"쪽에 붙어있음 (까마귀 발 모양)
채워진 다이아몬드 : 참조관계 - ON DELETE CASCADE
비어있는 다이아몬드 : 참조관계 - ON DELETE SET NULL



#### \# 데이터 모델링 (Dbeaver 교안 P.2)
사용자의 요구 사항을 분석한 다음 이를 문서화하는 일련의 과정
-> 데이터 사용에 대하여 구조화/조직화하는 단계
-> 업무 분석/설계 단계에서 적절한 표기법(ERD)으로 표현하는 방법
-> 실제(Entity)와 관계(Relation)에 의하여 문서를 표현하는 방식
현실세계 -> 문서 -> 설계 -> 구현 -> DataBase화



#### \# 이상 현상 (Dbeaver 교안 P.30)
데이터 집합에서 예상하지 못한, 비정상적인 패턴이나 동작을 나타내는 현상
ex) 데이터의 오류, 이상치, 누락, 부정확성 등
이상치 : 상식선에서 정상적인 범위를 벗어난 경우


1) 삽입 이상 (Insert) : 데이터 삽입시 필요 없는 속성까지 입력해야 하는 현상
ex) 어떤 테이블에 '통계학'이라는 학과를 추가하고 싶은데
테이블에 컬럼에는 '학과'만 있는 것이 아니라서
'통계학'이라는 데이터를 가진 행을 추가하려면 억지로 다른 컬럼에도 데이터를 입력해야 함
-> null값으로 억지로 다른 컬럼에 값을 넣으면 null이 너무 많아지기도하고
기본키, not null 문제가 있고
내가 데이터가 없는 것인지, 모르는것인지에 대한 혼동도 올 수 있음


2) 갱신 이상 (Update) : 데이터 갱신시 필요하지 않는 데이터까지 갱신해야 하는 상황
일반적으로 동일한 데이터에 대해 2건 이상의 업데이트가 일어나는 경우에 많이 발생
ex) 만약 테이블 안에 데이터에 이름이 '신동진'이고 전화번호가 010-1234-5678이고
과목이라는 컬럼에 5개의 값이 있다고 할때
행이 과목이라는 컬럼의 값 5개를 제외하고는 이름과 전화번호가
5개로 중복된 상태로 있다고 가정한다면
신동진이라는 사람의 전화번호가 갱신되어 바꿔야할때 5개의 행 전부를 일일히 찾아서
업데이트 해줘야 함


3) 삭제 이상 (Delete) : 데이터 삭제시 보존이 되어야 하는 데이터까지 삭제가 되는 현상
ex) 만약 한 학과에 '이가희'라는 학생만 존재한다고 할때 그 학생이 자퇴를 해서
그 학생의 데이터를 지우고 싶은데 이 학과에 이 학생만 존재해서 행 데이터 상으로는
이 학생의 데이터를 지우면 학과 데이터도 같이 삭제가 되는 일이 생김



#### \# 정규화 개념 (Dbeaver 교안 P.24)
- 정의 : 테이블에 입력/수정/삭제시 "이상 현상"을 최소화하기 위하여
좀 더 작은 단위의 테이블로 분해하는 과정
(데이터 구조화/체계적으로 재배치/분해하는 방법)

- 목적 :
데이터의 일관성 보장 / 중복된 데이터 최소화로 안정성 확보
이상 현상 방지 / 높은 응집력과 낮은 결합도 / 저장 공간 최소화 / 재활용성 높임

- 필요 충분 조건 :
데이터 분해시 데이터의 손실 없어야 함 (무손실 분해)
분해된 테이블들은 "조인 연산"을 통하여 원래 테이블의 모든 내용을 표현할 수 있어야 함



#### \# 함수의 종속성
왼쪽 속성 값에 의해 오른쪽 속성의 값이 결정될때 '함수적으로 종속한다'라고 함
이러한 성질을 '함수 종속성'
기준 값 X를 결정자(Determinant)
종속 되는 값 Y를 종속자(Dependent)
x는 기본키 / y는 외래키 - 반드시 그런건 아니지만 예를 들자면!!
ex) 주민번호를 알면 성별을 알 수 있다. / 생년월일을 알면 나이를 알 수 있다.

- Dbeaver 교안 P.28보고 직접 해보기
학생번호 -> 이름 : 학생번호에 따라 이름이 다름
학생번호 -> 주소 : 학생번호에 따라 주소가 다름
학생번호 -> 학과 : 학생번호에 따라 학과가 다름
학과 -> 사무실 : 과에 따라 사무실이 다름
강좌이름 -> 강의실 : 강좌이름에 따라 강의실이 다름

기본키 : 학생번호
외래키 : 이름, 주소, 학과

- 이행적 함수 종속
릴레이션 A → B 이고, B → C이면 A → C인 관계가 성립하는 관계
ex) '아이디'를 알면 고객의 '등급'을 알 수 있고, '등급'을 알면 고객의 '할인율'을 알 수 있다.
따라서 '아이디'를 알면 고객의 '할인율'을 알 수 있다.



#### \# 정규화(Dbeaver 교안 P.31~35)
0\. 정규화 전 이상 현상 파악하기 (Dbeaver 교안 P.31)
ex)
삽입 이상 : 신설학과 '통계학' 입력시 학생 이름도 반드시 입력해야 함
갱신 이상 : 동일한 학생인데 데이터 갱신시 일부 데이터만 변경되는 문제
삭제 이상 : 특정 학생 삭제시 학과까지 삭제가 되는 문제

1\. 제 1정규형 : 모든 속성은 원자 값 / 단일 값을 가져야 함 (Dbeaver 교안 P.33)
중복되는 행을 별도로 분리
ex)

|  공통정보   | 학생정보 |      학생정보      | 학생정보  | 학생정보 | 수강과목<br>정보 | 수강과목<br>정보 |
| :-----: | :--: | :------------: | :---: | :--: | :--------: | :--------: |
|   학번    |  이름  |     주민등록번호     |  학과   |  대학  |    과목코드    |     성적     |
| 9021756 | 신동진  | 701223-1111111 | 기계 공학 |  공대  |   ABC01    |     B      |
| 9021756 | 신동진  | 701223-1111111 | 기계 공학 |  공대  |   ABC02    |     A      |
| 9323789 | 유남균  | 801125-1026222 | 컴퓨터공학 |  공대  |   COM01    |     C      |
| 9323789 | 유남균  | 801125-1026222 | 컴퓨터공학 |  공대  |   COM02    |     B      |
| 9431156 | 이가희  | 190717-2026456 | 가정 의학 |  의대  |   MED38    |     A      |

1) 함수 종속성
학번 -> 이름
학번 -> 주민등록번호
학번 -> 학과
학번 -> 대학

학과 -> 대학

학번, 과목코드 -> 성적

\* (중요!!)학번->대학 인 이유 : 종속하는 쪽은 복수여도 상관없는데 종속되는 쪽은 복수이면 안됨
어찌되었든 학번을 복수여도 그 값에 종속되는 하나의 값인 대학이 나오기에 함수 종속성임

2) 이상 현상 분석
학생의 \[성적]을 알려면 반드시 \[학번]과 \[과목 코드] 정보를 알고 있어야 하는 문제가 있습니다.
따라서, 기본 키는 {학번, 과목 코드}가 되어야 합니다.
\* 복합 primary key : 2개의 컬럼이 있어야 비로소 1개의 primary key 역할을 할때
But 이러면 이름, 주민등록번호, 학과은 학번만 알아도 가능하고 과목코드는 상관없음
성적은 학번과 과목코드를 2개다 알아야 가능
따라서
학생 테이블 : 기본키 : 학번 / 나머지 컬럼 : 이름, 주민등록번호, 학과, 대학
수강 과목 : 기본키 : 학번, 과목코드 / 나머지 컬럼 : 성적
으로 나누면 됨

2\. 제 2정규형 : 기본 키가 아닌 모든 속성들은 기본 키에 완전히 종속 되어야 함 (Dbeaver 교안 P.34)
1) 학생 테이블

| 학번      | 이름  | 주민등록번호         | 학과     | 대학  |
| ------- | --- | -------------- | ------ | --- |
| 9021756 | 신동진 | 701223-1111111 | 기계 공학  | 공대  |
| 9323789 | 유남균 | 801125-1026222 | 컴퓨터 공학 | 공대  |
| 9431156 | 이가희 | 190717-2026456 | 가정 공학  | 공대  |

1-1) 함수 종속성
학번 -> 학과
학번 -> 대학

학과 -> 대학

1-2) 이행적 함수 종속
학번 -> 학과 -> 대학


2) 수강 과목 테이블

| 학번      | 과목코드  | 성적  |
| ------- | ----- | --- |
| 9021756 | ABC01 | B   |
| 9021756 | ABC02 | A   |
| 9323789 | COM01 | C   |
| 9323789 | COM02 | B   |
| 9431156 | MED38 | A   |

2-1) 함수 종속성
학번, 과목코드 -> 성적

3) 이상 현상 분석
3-1) 수강 과목 테이블 : 기본키가 {학번, 과목 코드} -> 성적은 기본 키에 함수적 종속성을 완전히 충족
-> 문제 없음
3-2) 학생 테이블 :
대학 컬럼은 학번컬럼과 학과컬럼에 동시에 완전 종속됨 - 이행적 함수 종속
\[학번 -> 학과 -> 대학]을 제거 해야 함
따라서
학생 테이블 : 기본키 : 학번 / 나머지 컬럼 : 이름, 주민등록번호, 학과
학과 테이블 : 기본키 : 학과 / 나머지 컬럼 : 대학
으로 나누면 됨

4\. 제 3정규형 : 이행적 함수 종속 제거 (Dbeaver 교안 P.35)
1) 학생 테이블

| 학번      | 이름  | 주민등록번호         | 학과     |
| ------- | --- | -------------- | ------ |
| 9021756 | 신동진 | 701223-1111111 | 기계 공학  |
| 9323789 | 유남균 | 801125-1026222 | 컴퓨터 공학 |
| 9431156 | 이가희 | 190717-2026456 | 가정 공학  |

1-1) 함수 종속성
학번 -> 이름
학번 -> 주민등록번호
학번 -> 학과


2) 수강 과목 테이블

| 학번      | 과목코드  | 성적  |
| ------- | ----- | --- |
| 9021756 | ABC01 | B   |
| 9021756 | ABC02 | A   |
| 9323789 | COM01 | C   |
| 9323789 | COM02 | B   |
| 9431156 | MED38 | A   |

2-1) 함수 종속성
학번, 과목코드 -> 성적

3) 학과 테이블

| 학과     | 대학  |
| ------ | --- |
| 기계 공학  | 공대  |
| 컴퓨터 공학 | 공대  |
| 가정 의학  | 의대  |

3-1) 함수 종속성
학번 -> 대학


4) 이상 현상 분석
모든 테이블의 모든 속성들이 기본 키에 완전히 함수적으로 종속 되고 있음.



#### \# 새로운 user만들기 (A01 스크립트)
- 하단부에 추가
```sql
-- 신규 사용자 곰돌이
CREATE USER gomdori IDENTIFIED BY oracle account unlock ;

ALTER USER gomdori DEFAULT TABLESPACE users quota unlimited ON users ;

GRANT CONNECT, resource TO gomdori ;

-- 신규 사용자 블루스카이
CREATE USER bluesky IDENTIFIED BY oracle account unlock ;

ALTER USER bluesky DEFAULT TABLESPACE users quota unlimited ON users ;

GRANT CONNECT, resource TO bluesky ;
```

- 새로운 데이터 베이스 연결
곰돌이 : 로컬DB(곰돌이)



#### \# 정규화 SQL로 하기 (Dbeaver 교안 P.36)
- ERD를 보고 따라 만들기
노란색 열쇠 모양 : PK
F모양 : FK

1) 참조 무결성 제약 조건 설정
FK설정
STUDENTS_DEPARTMENT_FK - ON DELETE : NO ACTION
(학생이 존재하면 학과는 없어지지 말아야 할 것 같아서)
```sql
ALTER TABLE GOMDORI.STUDENTS
ADD CONSTRAINT STUDENTS_DEPARTMENTS_FK FOREIGN KEY (DEPARTMENT)
REFERENCES GOMDORI.DEPARTMENTS(DEPARTMENT);
```


SUBJECTS_STUDENTS_FK - ON DELETE : NO ACTION
(학생이 없어져도 과목 내역은 남게 하려고)
```sql
ALTER TABLE GOMDORI.SUBJECTS
ADD CONSTRAINT SUBJECTS_STUDENTS_FK FOREIGN KEY (HAKBUN)
REFERENCES GOMDORI.STUDENTS(HAKBUN);
```

2) 데이터 추가하기
```sql
-- 학과 데이터 추가
insert into departments values('기계 공학', '공대');
insert into departments values('컴퓨터 공학', '공대');
insert into departments values('가정 의학', '의대');

-- 학생 데이터 추가
insert into students values(9021756, '신동진', '701223-1111111', '기계 공학');
insert into students values(9323789, '유남균', '801125-1026222', '컴퓨터 공학');
insert into students values(9431156, '이가희', '190717-2026456', '가정 의학');

-- 과목 성적 데이터 추가
insert into subjects values(9021756, 'ABC02', 'A');
insert into subjects values(9323789, 'COM01', 'C');
insert into subjects values(9323789, 'COM02', 'B');
insert into subjects values(9431156, 'MED38', 'A');
commit ;
```


3) 참조 무결성 테스트 (오류나야 정상)
```sql
-- 존재하지 않는 학생
insert into subjects values(9044555, 'ABC01', 'B');
-- 존재하지 않는 학과 정보 추가하기
insert into students values(9021777, '김철수', '701223-1111111', '전산과');
-- 자식 테이블에 데이터가 존재하므로 삭제 불가능
delete from departments where department = '가정 의학';
```



#### \# 정규화 예시 02 따라만들기 (Dbeaver 교안 P. 43) (On delete 옵션을 뭘로 선택할지 다시 한 번 고민하기)
```sql
CREATE TABLE BLUESKY.MEMBERS (
	ID VARCHAR2(30) NOT NULL,
	NAME VARCHAR2(30) NULL,
	ADDRESS VARCHAR2(255) NULL,
	CONSTRAINT MEMBERS_ID_PK PRIMARY KEY (ID)
)
TABLESPACE USERS;
COMMENT ON TABLE BLUESKY.MEMBERS IS '학생을 위한 테이블입니다';
COMMENT ON COLUMN BLUESKY.MEMBERS.ID IS '아이디';
COMMENT ON COLUMN BLUESKY.MEMBERS.NAME IS '이름';
COMMENT ON COLUMN BLUESKY.MEMBERS.ADDRESS IS '주소';

CREATE TABLE BLUESKY.ORDERS (
	"OID" NUMBER(38,0) NOT NULL,
	ORDERDATE DATE NULL,
	ID VARCHAR2(30) NULL,
	CONSTRAINT ORDERS_OID_PK PRIMARY KEY ("OID")
)
TABLESPACE USERS;
COMMENT ON TABLE BLUESKY.ORDERS IS '주문을 위한 테이블입니다';
COMMENT ON COLUMN BLUESKY.ORDERS."OID" IS '송장 번호';
COMMENT ON COLUMN BLUESKY.ORDERS.ORDERDATE IS '주문 일자';
COMMENT ON COLUMN BLUESKY.ORDERS.ID IS '회원 아이디';

CREATE TABLE BLUESKY.PRODUCTS (
	PNUM VARCHAR2(30) NOT NULL,
	DESCRIPTION VARCHAR2(255) NULL,
	CONSTRAINT PRODUCTS_PNUM_PK PRIMARY KEY (PNUM)
)
TABLESPACE USERS;
COMMENT ON TABLE BLUESKY.PRODUCTS IS '상품을 위한 테이블입니다';
COMMENT ON COLUMN BLUESKY.PRODUCTS.PNUM IS '제품 번호';
COMMENT ON COLUMN BLUESKY.PRODUCTS.DESCRIPTION IS '제품 설명';

CREATE TABLE BLUESKY.ORDERDETAILS (
	"OID" NUMBER(38,0) NULL,
	PNUM VARCHAR2(30) NULL,
	QTY NUMBER(38,0) NULL
)
TABLESPACE USERS;
COMMENT ON TABLE BLUESKY.ORDERDETAILS IS '상품 상세를 위한 테이블입니다';
COMMENT ON COLUMN BLUESKY.ORDERDETAILS."OID" IS '송장 번호';
COMMENT ON COLUMN BLUESKY.ORDERDETAILS.PNUM IS '상품 번호';
COMMENT ON COLUMN BLUESKY.ORDERDETAILS.QTY IS '주문 수량';

ALTER TABLE BLUESKY.ORDERS
ADD CONSTRAINT ORDERS_MEMBERS_FK FOREIGN KEY (ID)
REFERENCES BLUESKY.MEMBERS(ID) ON DELETE SET NULL;

ALTER TABLE BLUESKY.ORDERDETAILS
ADD CONSTRAINT ORDERDETAILS_ORDERS_FK FOREIGN KEY ("OID")
REFERENCES BLUESKY.ORDERS("OID") ON DELETE CASCADE;

ALTER TABLE BLUESKY.ORDERDETAILS
ADD CONSTRAINT ORDERDETAILS_PRODUCTS_FK FOREIGN KEY (PNUM)
REFERENCES BLUESKY.PRODUCTS(PNUM) ON DELETE SET NULL;
```



#### \# View (Oracle 교안 P. 446)
원래 user가 가진 테이블같은 객체 등은 user 본인 혹은 관리자만 볼 수 있음
정의 : 물리적인 테이블에 근거하여 해당 테이블의 "일부"를 보여 주는
논리에 근거한 가상의 테이블

- 절차:
A : 테이블 일부를 보여주는 유저 / B : 테이블 일부를 보는 유저
관리자 스크립트에서 A에게 view 생성 권한 주기 -> A스크립트에서 view 생성
-> A스크립트에서 B에게 view를 볼 권한 주기 -> B스크립트에서 view 조회 가능!

- view 생성, 권한 주기 및 실제 조회
1) 관리자 스크립트에서 A에게 view 생성 권한 주기
(A01 스크립트)
```sql
-- 오라맨 사용자에게 view 생성 권한 주기
GRANT CREATE VIEW TO oraman ;
```
-> 만약 복수의 사용자에게 view 생성 권한을 주려면 콤마로 연결 해주면 됨


2) A스크립트에서 view 생성
(새로운 스크립트 - active datasource는 로컬DB(오라맨))
```sql
-- 오라맨의 테이블의 일부를 곰돌이 한테 보여줄 뷰 생성
CREATE VIEW view01
AS
SELECT name, password, gender
FROM MEMBERS
WHERE gender = '남자' ;
```
-> 로컬DB(오라맨) 커넥션 - 스키마 - ORAMAN - Views에 보면 VIEW01이 생성된게 보임

2-1) View의 생성 및 삭제
테이블과 같이 create로 생성하고 drop으로 삭제 가능
But, CREATE OR REPLACE VIEW view01 사용가능
create or replace : 없으면 만들고 이미 있으면 대체해라


3) A스크립트에서 B에게 view를 볼 권한 주기
(oraman 스크립트)
곰돌이에게 뷰를 조회할 수 있는 권한 부여
grant : 수여하다, 부여하다 / on : ~에 대하여 / to : ~에게
```sql
GRANT SELECT ON view01 TO gomdori ;
```
수여하다 / select권한을 / view01에 대하여 / gomdori에게


4) B스크립트에서 view 조회 가능!
(gomdori 스크립트)
곰돌이 세션
```sql
-- 오라맨의 회원 테이블 조회
SELECT * FROM oraman.members ; -> 에러발생
SELECT * FROM oraman.view01 ; -> 조회 가능
```
-> view의 제한성때문에 members테이블의 일부이자 select 권한을 가진 view01만 조회 가능

- view 권한 박탈
DCL 구문 (data control language) : 데이터 제어어 (사용자(user)단위)
grant 권한 부여
revoke 권한 박탈

(oraman스크립트)
```sql
-- 곰돌이에게서 뷰 권한 박탈
REVOKE SELECT ON view01 FROM gomdori ;
```
박탈한다 / select권한을 / view01에 대한 / gomdori로부터

But 뷰 목록은 살아 있어서 user한테 select권한을 주면 다시 볼 수 있음
\* REVOKE SELECT ON view01 FROM gomdori ; 여기에서 view들을 콤마로 여러개 나열은 못함 *

- view 삭제
```sql
DROP VIEW view01 ;
```

- 또 다른 view 사용법
(oraman스크립트)
```sql
-- 조금 복잡한 구문
CREATE OR REPLACE VIEW view02
as
SELECT m.name, m.gender, b.subject, b.content
from members m INNER JOIN boards b
ON m.id = b.writer ;
```



#### \# 데이터 사전
테이블 : user_tables
뷰 : user_views



#### \# 뷰 목록 확인
-> SELECT * FROM user_views ;
view_name(이름) 컬럼 / TEXT(내용) 컬럼이 핵심
ex)
```sql
SELECT view_name, text FROM user_views ;
SELECT view_name, text FROM user_views WHERE view_name = 'view01' ;
```
-> 에러가 나지는 않지만 아무것도 조회 못함
모든 사전들은 객체를 대문자로 관리하기에 -> VIEW01로 조회 해야 함
-> SELECT view_name, text FROM user_views WHERE view_name = 'VIEW01' ;



#### \# 인덱스
책의 목차같은 것?
인덱스 생성 시점 :
primary key를 생성할때 (pk)
unique 생성할때 (uk)

커넥션 - 스키마 - ORAMAN 안에 있는 것들이 다 객체
DBMS (database management system) (줄여서 DB)
RDB(관계형 데이터베이스)