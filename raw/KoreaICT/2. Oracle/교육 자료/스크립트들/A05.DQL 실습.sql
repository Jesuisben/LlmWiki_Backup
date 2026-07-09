-- 오라클 교안 : 134~195

-- DQL
-- select *|{[distinct] column 리스트|표현식, [alias],
-- from 테이블 1[, 테이블 2, …] 
-- [where condition] 
-- [group by column] 
-- [having column] 
-- [order by column];


-- PRODUCTS 테이블 문제 + 정답
-- 기본 조회
-- 1. 모든 상품을 조회하세요.
-- *는 all columns를 의미합니다.
SELECT * FROM products ;

-- 2. 상품 이름과 가격을 조회하세요.
-- 관심있는 컬럼만 콤마로 연결하여 조회
SELECT name, price FROM products ;
select name, price from products ;

-- 단가, 입고일자, 재고 목록
SELECT price, inputdate, stock FROM products ;

-- 3. 상품 이름, 회사, 재고를 조회하세요.
select name, company, stock from products ;

-- 4. 상품의 카테고리를 중복 없이 조회하세요.
-- distinct : 중복된 데이터는 1개만 표시
select distinct category from products ;

select category from products ;


-- 파생 컬럼과 별칭
-- 20. 상품 이름과 가격, 가격 + 1000을 조회하세요.
select name, price, price + 1000 from products ;

-- 21. 상품 이름과 연간 가격(가격 * 12)을 조회하세요.
-- as 키워드는 옵션입니다.
select name, price,  price * 12 as "annual price" from products ;

-- 22. '상품명 : ○○, 가격 : ○○원' 형식으로 출력하세요.
select '상품명 : ' || name || ', 가격 : ' || price || '원' as result
from products ;

------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------

-- 조건 검색(행의 제한)
select * from products where num = 1 ;

-- 5. 가격이 5000 이상인 상품을 조회하세요.
select * from products where price >= 5000 ;

-- 6. 재고가 100인 상품을 조회하세요.
select * from products where stock = 100 ;

-- 7. 카테고리가 'bread'인 상품을 조회하세요.
select * from products where category = 'bread' ;


-- and 연산자와 or 연산자
SELECT * FROM products WHERE price = 3000 AND point = 6 ;

-- 단가가 3000이거나, 포인트가 6인 항목 조회
SELECT * FROM products WHERE price = 3000 OR point = 6 ;

-- 8. 가격이 3500 이상이고 4500 이하인 상품을 조회하세요.
SELECT * FROM products WHERE price >= 3500 AND price <= 4500 ;

SELECT * FROM products WHERE price BETWEEN 3500 AND 4500 ;

-- 9. 가격이 4000 또는 6000인 상품을 조회하세요.
SELECT * FROM products WHERE price = 4000 or price = 6000 ;

-- in 절(clause) : or 연산자의 대체 표현
select * from products where price in (4000, 6000) ;

-- in 절을 사용하여 'cake' 또는 'beverage'인 항목들 조회
SELECT * FROM products WHERE category in ('cake', 'beverage') ;

-- 포인트가 5인 상품을 조회하세요.
select * from products where point = 5 ;

-- 포인트가 5가 아닌 상품을 조회하세요.
select * from products where point != 5 ;

select * from products where point <> 5 ;

-- null 데이터 


-- 15. 가격이 NULL인 상품을 조회하세요.
select * from products where price is null ;

SELECT * FROM boards WHERE writer IS NULL ;


-- 문자열 검색
-- wildcard 문자 : _(무조건 1글자), %(0개 이상의 문자열)
-- like 키워드에 wildcard 문자가 사용됩니다.
-- 상품 이름에 '라떼'가 포함된 상품을 조회하세요.
select * from products where name like '%라떼%' ;

-- '크로와상'으로 시작하는 상품을 조회하세요.
select * from products where name like '크로와상%' ;

-- '01'로 끝나는 상품을 조회하세요.
select * from products where name like '%01' ;

-- 상품명 2번째 글자가 '이'인 상품들 조회
SELECT * FROM products where name LIKE '_이%';

-- 부정어 사용하기
-- 카테고리가 'bread'가 아닌 항목
SELECT * FROM products WHERE CATEGORY NOT IN ('bread') ;
-- 게시물 작성자가 확실한 게시물
SELECT * FROM boards WHERE WRITER IS NOT NULL ;
-- 단가가 3500원 이상 5500원 이하에 포함되지 않는 상품
SELECT * FROM products WHERE price NOT BETWEEN 3500 AND 5500 ;
-- '크로와상'으로 시작하지 않는 상품들
SELECT * FROM products name NOT LIKE '크로와상%' ;


-- 정렬
-- 16. 가격이 낮은 순으로 상품을 조회하세요.
select * from products order by price asc ;

-- 17. 가격이 높은 순으로 상품을 조회하세요.
select * from products order by price desc ;

-- 18. 상품 이름을 기준으로 오름차순 정렬하세요.
select * from products order by name asc ;

-- 19. 카테고리별로 정렬하고, 같은 카테고리에서는 가격이 높은 순으로 정렬하세요.
SELECT DISTINCT category FROM products ORDER BY category ASC ;

select * from products order by category asc, price desc ;

-- boards 테이블 : 작성자에 대하여 내림차순으로 조회하되 최신 게시물부터 먼저 보여 주세요.
SELECT * FROM boards ORDER BY writer DESC, NO DESC ;

