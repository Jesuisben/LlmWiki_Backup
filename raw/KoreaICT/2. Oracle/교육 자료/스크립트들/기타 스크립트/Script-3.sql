-- View
-- 오라클 교안 : 446~475
SELECT * FROM members ;

-- 곰돌이 한테 보여줄 뷰
CREATE OR REPLACE VIEW view01
AS 
SELECT name, password, gender
FROM MEMBERS
WHERE gender = '남자' ;

SELECT * FROM view01 ;

-- 곰돌이에게 뷰를 조회할 수 있는 권한 부여
GRANT SELECT ON view01 TO gomdori ;

-- 조금 복잡한 구문
CREATE OR REPLACE VIEW view02
as
SELECT m.name, m.gender, b.subject, b.content
from members m INNER JOIN boards b
ON m.id = b.writer ;

-- 곰돌이에게 뷰를 조회할 수 있는 권한 부여2
GRANT SELECT ON view02 TO gomdori ;

-- 뷰 목록 확인
-- 모든 사전들은 객체를 대문자로 관리합니다.
SELECT view_name, text FROM user_views WHERE view_name = 'VIEW01' ;

-- 곰돌이에게서 뷰 권한 박탈
REVOKE SELECT ON view01 FROM gomdori ;

REVOKE SELECT ON view02 FROM gomdori ;


DROP VIEW view01 ;

DROP VIEW view02 ;






