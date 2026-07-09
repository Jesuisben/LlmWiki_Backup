-- 오라클 교안 : 215~293쪽 

-- dual 테이블 : 간단한 산술 연산 및 함수 테스트
select 5*3 from dual ;
select power(2, 10) from dual ;
select 'hello' from dual ;
select upper('hello'), lower('HELLO') from dual ;
SELECT mod(14, 5) FROM dual ;

-- 문자열 함수 예제
-- 자바의 String 클래스가 갖고 있는 메소드 공부
-- (1) 상품 이름을 대문자로 조회
SELECT NAME, UPPER(NAME) AS NAME_UPPER, upper(category), lower(category)
FROM PRODUCTS;

-- (2) 상품 이름 길이 확인
SELECT NAME, LENGTH(NAME) AS NAME_LENGTH
FROM PRODUCTS;

-- (3) 회사명 앞 3글자만 출력
SELECT COMPANY, SUBSTR(COMPANY, 1, 3) AS SHORT_COMPANY
FROM PRODUCTS;

-- (4) 상품명과 회사명 합치기
-- concat() 함수 : 문자열 결합해주는 함수
SELECT NAME || ' - ' || COMPANY AS PRODUCT_INFO
FROM PRODUCTS;

-- (5) 특정 문자 치환 (A → ★)
SELECT NAME, REPLACE(NAME, '아', '★') AS REPLACED_NAME
FROM PRODUCTS;

-- company 컬럼에 '가'라는 글자가 포함된 행
SELECT instr('컴포즈커피', '가'), instr('메가커피', '가') FROM dual ;
SELECT * FROM products WHERE instr(company, '가') > 0 ;

-- 패딩 : rpad, lpad
SELECT company, lpad(company, 10, '*'), rpad(company, 10, '*')
FROM products ;

SELECT trim('  aa ') FROM dual ;
SELECT rtrim('xxaaxx', 'x') FROM dual ;
SELECT ltrim('xxaaxx', 'x') FROM dual ;

-- company 컬럼에 '커피'라는 단어 모두 지워 주세요.
SELECT company, rtrim(company, '커피') FROM products ;

-- 숫자형 함수 예제
-- 자바의 Math 클래스 공부
-- abs() 함수 : 절대 값
SELECT -5, abs(-5) FROM dual ;


-- (1) 가격 + 10% 인상
SELECT NAME, PRICE, PRICE * 1.1 AS NEW_PRICE
FROM PRODUCTS;


SELECT round(1234.567), trunc(1234.567) FROM dual ;

SELECT round(1234.567, 2), trunc(1234.567, 2) FROM dual ;

SELECT ceil(1234.567), floor(1234.567) FROM dual;


-- (2) 포인트 반올림
SELECT NAME, POINT, ROUND(POINT) AS ROUND_POINT
FROM PRODUCTS;

-- (3) 가격 절삭
SELECT NAME, PRICE, TRUNC(PRICE, -1) AS TRUNC_PRICE
FROM PRODUCTS;

-- sqrt() : 루트
SELECT sqrt(5) FROM dual ;

SELECT price, sqrt(price), round(sqrt(price), 2)
FROM products ;

-- (4) 재고 + 가격 합계 계산
SELECT NAME, STOCK + PRICE AS TOTAL_VALUE
FROM PRODUCTS;

-- (5) 가격의 나머지 값
SELECT NAME, MOD(PRICE, 30) AS REMAINDER
FROM PRODUCTS;

-- 날짜 함수 예제
-- (1) 입력일 확인
SELECT NAME, INPUTDATE
FROM PRODUCTS;

-- (2) 오늘 날짜와 차이
SELECT NAME, INPUTDATE, SYSDATE - INPUTDATE AS DAYS_DIFF
FROM PRODUCTS;

-- (3) 7일 후 날짜
SELECT NAME, INPUTDATE, INPUTDATE + 7 AS AFTER_7_DAYS
FROM PRODUCTS;

-- (4) 월 단위 차이
SELECT NAME, MONTHS_BETWEEN(SYSDATE, INPUTDATE) AS MONTH_DIFF
FROM PRODUCTS;
-- (5) 다음 월 같은 날짜
SELECT NAME, ADD_MONTHS(INPUTDATE, 1) AS NEXT_MONTH
FROM PRODUCTS;



-- 오라클 교안 : 294~326쪽 
-- 집계 함수
-- 전체 상품 개수
-- 전체 상품 개수
SELECT COUNT(*) AS TOTAL_COUNT
FROM PRODUCTS;

-- 2. 가격이 있는 상품 개수 (NULL 제외)
-- 가격이 NULL이 아닌 상품 개수
SELECT COUNT(PRICE) AS PRICE_COUNT
FROM PRODUCTS;

SELECT count(*) - COUNT(PRICE) AS "단가널갯수"
FROM PRODUCTS;


--  COUNT(컬럼)은 NULL 제외라는 점이 핵심입니다.

-- 카테고리의 종류에는 어떠한 것이 있나요?
SELECT count(DISTINCT category) FROM products ;

-- 3. 최고 / 최저 가격
-- 최고가 / 최저가
SELECT MAX(PRICE) AS MAX_PRICE, MIN(PRICE) AS MIN_PRICE FROM PRODUCTS;

SELECT min(name), max(name) FROM members ;

-- 4. 평균 가격
-- 평균 가격
SELECT AVG(PRICE) AS AVG_PRICE FROM PRODUCTS;

--  NULL 값은 자동 제외됨

-- 5. 총 재고 수량
-- 전체 재고 합계
SELECT SUM(STOCK) AS TOTAL_STOCK FROM PRODUCTS;


-- 남녀 각각 몇명인가요?
SELECT gender, count(*)
FROM members
GROUP BY gender ;

-- 6. 카테고리별 상품 개수
-- 카테고리별 상품 개수
SELECT CATEGORY, COUNT(*) AS CNT
FROM PRODUCTS
GROUP BY CATEGORY;


-- 7. 카테고리별 평균 가격
-- 카테고리별 평균 가격
SELECT CATEGORY, AVG(PRICE) AS AVG_PRICE
FROM PRODUCTS
GROUP BY CATEGORY;

-- 8. 회사별 상품 개수
-- 회사별 상품 개수
SELECT COMPANY, COUNT(*) AS CNT
FROM PRODUCTS
GROUP BY COMPANY
ORDER BY company;

-- 9. 카테고리별 최고 가격 (정렬 포함)
-- 카테고리별 최고 가격 (높은 순)
SELECT CATEGORY, MAX(PRICE) AS MAX_PRICE
FROM PRODUCTS
GROUP BY CATEGORY
ORDER BY MAX_PRICE DESC;

-- 카테고리별 회사별 최고 가격(높은 순)
SELECT category, company, max(price) AS max_price
FROM products
GROUP BY category, company
ORDER BY category, company desc;

-- HAVING 절 사용하기
-- 회사별 상품 개수를 파악하되 3개이상인 회사 정보만 출력
SELECT COMPANY, COUNT(*) AS CNT
FROM PRODUCTS
GROUP BY COMPANY
ORDER BY company;


SELECT COMPANY, COUNT(*) AS CNT
FROM PRODUCTS
GROUP BY COMPANY
HAVING count(*) >= 3
ORDER BY company;

-- HAVING은 GROUP BY 이후 조건



-- 10. 평균 가격이 5000 이상인 카테고리
-- 평균 가격이 5000 이상인 카테고리
SELECT CATEGORY, AVG(PRICE) AS AVG_PRICE
FROM PRODUCTS
GROUP BY CATEGORY
HAVING AVG(PRICE) >= 5000;

--  HAVING은 GROUP BY 이후 조건

-- 11. NULL 처리 (NVL 활용)
-- NULL 가격을 0으로 처리 후 평균 계산
SELECT AVG(NVL(PRICE, 0)) AS AVG_PRICE
FROM PRODUCTS;
-- 12. 회사별 총 매출(가격 기준)
-- 회사별 총 가격 합계
SELECT COMPANY, SUM(PRICE) AS TOTAL_PRICE
FROM PRODUCTS
GROUP BY COMPANY;
-- 13. 카테고리별 상품 수 + 평균 가격 + 총 재고
-- 종합 집계
SELECT 
    CATEGORY,
    COUNT(*) AS CNT,
    AVG(PRICE) AS AVG_PRICE,
    SUM(STOCK) AS TOTAL_STOCK
FROM PRODUCTS
GROUP BY CATEGORY;
-- 14. 가장 비싼 상품 정보 (서브쿼리)
-- 최고가 상품 조회
SELECT *
FROM PRODUCTS
WHERE PRICE = (SELECT MAX(PRICE) FROM PRODUCTS);
-- 15. 가장 많이 등록된 회사 TOP 1
-- 상품을 가장 많이 등록한 회사
SELECT COMPANY, COUNT(*) AS CNT
FROM PRODUCTS
GROUP BY COMPANY
ORDER BY CNT DESC
FETCH FIRST 1 ROW ONLY;