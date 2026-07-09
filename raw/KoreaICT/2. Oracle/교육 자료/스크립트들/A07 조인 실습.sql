-- 조인 실습
-- 오라클 교안 : 347~365쪽

-- 게시물 작성자의 이름과 글 제목 출력
-- 오라클 조인 : 콤마와 where 사용
SELECT members.name, boards.SUBJECT
FROM members, boards
WHERE MEMBERS.ID = BOARDS.WRITER ;

-- ANSI 조인 : join과 on 절 사용
SELECT members.name, boards.SUBJECT
FROM members JOIN boards
ON MEMBERS.ID = BOARDS.WRITER ;

-- 별칭 사용 : 긴 테이블 이름을 짧은 alias 사용하기
SELECT m.name, b.SUBJECT
FROM members m JOIN boards b
ON m.ID = b.WRITER ;

-- 추가적인 필터링은 and 연산자 사용
SELECT m.name, b.SUBJECT
FROM members m JOIN boards b
ON m.ID = b.WRITER
AND m.name IN('안중근', '조마리아') ;

-- 게시물을 남기지 않은 사람도 같이 볼래요.
SELECT m.name, b.SUBJECT
FROM members m LEFT OUTER JOIN BOARDS b
ON m.ID = b.WRITER ;

-- 작성자가 누구인지 모르는 데이터도 같이 볼래요.
SELECT m.name, b.SUBJECT
FROM members m full OUTER JOIN BOARDS b
ON m.ID = b.WRITER ;

-- 각 회원들의 게시물 작성 건수
SELECT m.id, m.Name, count(*)
FROM members m JOIN BOARDS b
ON m.id = b.writer
group by m.id, m.NAME ;


-- 각 회원들의 게시물 작성 건수(미작성자도 포함)
SELECT m.id, m.Name, count(writer) AS cnt
FROM members m LEFT OUTER JOIN BOARDS b
ON m.id = b.writer
group by m.id, m.NAME
ORDER BY cnt DESC, m.name ASC ;

-- 서브 쿼리
-- 최소 급여자의 이름과 급여를 출력
-- 최소 급여?
SELECT min(salary) FROM members ;

SELECT name, salary FROM members WHERE salary = 100 ;


SELECT name, salary
FROM members 
WHERE salary = (SELECT min(salary) FROM members) ;

-- 사원들의 평균 월급보다 많이 받는 사원들
SELECT name, salary
FROM members 
WHERE salary > (SELECT avg(salary) FROM members);

-- 관리자가 '김구'인 사원들
SELECT * FROM members 
WHERE manager = (SELECT id FROM members WHERE name = '김구');

-- '이순신'의 급여 보다 낮은 급여를 받는 사원들 정보
SELECT name, salary FROM members
WHERE salary < (SELECT salary FROM members WHERE name = '이순신' ) ;

-- 관리자가 '김구'인 사원들중에서 평균 급여보다 낮은 급여를 받는 사원들 정보
SELECT name, salary
FROM members
WHERE manager = (SELECT id FROM members WHERE name = '김구')
AND salary < (SELECT avg(salary) FROM members);

-- 다중행 서브 쿼리
-- in, any, all
-- 관리자 '김구' 또는 '유관순'인 사원들
SELECT name, manager
FROM MEMBERS
WHERE manager IN (SELECT id FROM members WHERE name IN('김구', '유관순'));

-- 게시물 작성자의 이름과 생일과 성별
SELECT DISTINCT writer FROM boards WHERE writer IS NOT null

SELECT name, birth, gender
FROM members
WHERE id IN (SELECT DISTINCT writer FROM boards WHERE writer IS NOT null);

-- '이혼'하지 않은 사원들 목록
SELECT name, marriage
FROM members
WHERE id not IN (SELECT id FROM members WHERE marriage in ('이혼'));

-- 성별로 최저 급여자의 이름과 급여와 성별
SELECT gender, min(salary) FROM members GROUP BY GENDER ;

SELECT name, salary, gender
FROM MEMBERS
WHERE (gender, salary) IN (SELECT gender, min(salary) FROM members GROUP BY GENDER) ;

-- 결혼 유형별 최저 급여자의 이름, 급여, 결혼 유형
-- 확인하기
SELECT DISTINCT marriage FROM members ;

SELECT marriage, min(salary) FROM members GROUP BY marriage ;

SELECT name, salary, marriage
FROM MEMBERS
WHERE (marriage, salary)
IN (SELECT marriage, min(salary) FROM members GROUP BY marriage);

-- 주소별 최대 급여자의 이름과 주소와 급여 컬럼
-- 확인하기
SELECT DISTINCT address FROM members ;

SELECT address, max(salary) FROM members GROUP BY address ;

SELECT name, address, salary
FROM members
WHERE (address, salary)
IN (SELECT address, max(salary) FROM members GROUP BY address);