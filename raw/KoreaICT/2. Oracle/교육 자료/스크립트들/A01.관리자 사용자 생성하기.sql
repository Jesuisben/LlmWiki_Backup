-- 1. 접속 아이콘 생성(오라클 교재 43~51쪽)
-- 관리자 아이콘 생성
-- 관리자 계정 : sys/oracle

-- 신입 사원 계정 만들기
-- 	id : oraman
-- 	password : oracle
-- 신입 사원 아이콘 생성

-- 2. 포워드 엔지니어링(모델링 교재 29~33쪽)
-- 준비물 : 드라이버(ojdbc6.jar)
-- erd 파일을 데이터 베이스에 반영하기 

-- 호스트 :
-- 	데이터 베이스가 있는 컴퓨터 
-- 	localhost (127.0.0.1)
-- 포트 :
-- 	접속을 위한 포트(숫자 값), listener.ora 파일에 명시 되어 있음
-- 	1521
-- SID : 
-- 	데이터 베이스 식별 아이디
-- 	select instance_name from v$instance ; 명령어로 확인 가능
-- 	xe

-- 관리자 세션
-- 빼기 2개는 주석입니다.
-- 관리자가 소유한 테이블 목록 보기
select * from tab ;

-- 사용자 계정 생성
-- 계정 생성하고 잠금을 풀어 줍니다.
create user oraman identified by oracle account unlock ;

-- 기본 테이블 저장소를 users로 변경합니다.
-- 할당량(quota)을 무제한(unlimited) 제공해 줍니다.
alter user oraman default tablespace users quota unlimited on users ;

-- oraman에게 접속 권한(connect)과 resource 권한을 부여합니다.
grant connect, resource to oraman ;

drop user oraman cascade ;

-- 데이터 베이스 식별 아이디
select instance_name from v$instance ; 

-- 당신은 데이터 베이스관리자입니다.
-- 신규 사원인 마당(아이디 : madang, 비밀 번호 : madang) 사원을 생성하세요.
-- 테이블 생성이 가능하도록 권한을 부여 하세요.

create user madang identified by madang account unlock ;

alter user madang default tablespace users quota unlimited on users ;

alter user madang account unlock ;

grant connect, resource to madang ; 

-- 신규 사용자 곰돌이
CREATE USER gomdori IDENTIFIED BY oracle account unlock ;

ALTER USER gomdori DEFAULT TABLESPACE users quota unlimited ON users ;

GRANT CONNECT, resource TO gomdori ;

-- 신규 사용자 블루스카이
CREATE USER bluesky IDENTIFIED BY oracle account unlock ;

ALTER USER bluesky DEFAULT TABLESPACE users quota unlimited ON users ;

GRANT CONNECT, resource TO bluesky ;

SELECT tablespace_name FROM dba_tablespaces ;


-- 오라맨 사용자에게 view 생성 권한 주기
GRANT CREATE VIEW TO oraman ;










