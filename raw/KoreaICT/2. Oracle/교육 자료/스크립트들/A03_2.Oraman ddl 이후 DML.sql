-- 회원 데이터
insert into members
values('yusin', '김유신', 'abc123', '남자', '1990/12/25', '결혼', 220, '용산', null);

insert into members 
values('lee', '이순신', 'abc1234', '남자', '1990/12/25', '이혼', 220, '마포', 'yusin') ;

insert into members 
values('choi', '최영', 'abc1234', '남자', '1990/12/25', '결혼', 155, '강남', 'yusin') ;

insert into members 
values('kang', '강감찬', 'abc1234', '남자', '1990/12/25', '이혼', null, '서대문', 'yusin') ;

-- 컬럼 이름을 명시하여 추가하기
insert into members(id, name, password, gender, birth, marriage, salary, address, manager)
values('yoon', '윤봉길', 'abc1234', '남자', '1990/12/25', '미혼', 230, '용산', 'yusin') ;

insert into members(id, name, password, gender, birth, marriage, salary, address, manager)
values('kim9', '김구', 'abc1234', '남자', '1990/12/25', '결혼', 280, '강남', null) ;

insert into members(id, name, password, gender, birth, marriage, salary, address, manager)
values('general', '김좌진', 'abc1234', '남자', '1990/12/25', '이혼', 385, '마포', 'kim9') ;

insert into members(id, name, password, gender, birth, marriage, salary, address, manager)
values('an', '안중근', 'abc1234', '남자', '1990/12/25', '결혼', 360, '서대문', 'kim9') ;

-- 일부 컬럼만 명시하여 추가하기
-- 급여(salary)를 명시하지 않으면 기본 값이 추가됩니다.
insert into members(id, name, password, gender, birth, marriage, address, manager, salary)
values('nongae', '논개', 'abc1234', '여자', '1990/12/25', '미혼', '강남', 'soon', 100) ;

insert into members(id, name, password, gender, birth, marriage, address, manager, salary)
values('queen', '선덕여왕', 'abc1234', '여자', '1990/12/25', '결혼', '용산', 'soon', 100) ;

insert into members(id, name, password, gender, birth, marriage, salary, address)
values('soon', '유관순', 'abc1234', '여자', '1990/12/25', '미혼', 240, '마포') ;

-- 컬럼 이름을 임의의 순서대로 작성하기
insert into members(id, salary, manager, address, name, password, gender, birth, marriage)
values('shin', 215, 'kim9', '서대문', '신사임당', 'abc1234', '여자', '1990/12/25', '미혼') ;

insert into members(id, salary, manager, address, name, password, gender, birth, marriage)
values('hwang', 215, 'kim9', '용산', '황진이', 'abc1234', '여자', '1990/12/25', '결혼') ; 

insert into members(id, salary, manager, address, name, password, gender, birth, marriage)
values('myoung', 215, 'soon', '강남', '명성왕후', 'abc1234', '여자', '1990/12/25', '이혼') ; 

insert into members(id, salary, manager, address, name, password, gender, birth, marriage)
values('maria', 215, 'soon', '서대문', '조마리아', 'abc1234', '여자', '1990/12/25', '이혼') ; 

insert into members(id, salary, manager, address, name, password, gender, birth, marriage)
values('princess', 215, 'soon', '마포', '덕혜옹주', 'abc1234', '여자', '1990/12/25', '결혼') ;
---------------------------------------------------------------
-- 게시물 데이터
---------------------------------------------------------------
insert into boards(no, writer, password, subject, content, readhit, regdate)
values(BOARD_SEQ.nextval, 'an', 'abc123', '자바', '너무 어려워', default, '1980/12/25') ;

insert into boards(no, writer, password, subject, content, readhit, regdate)
values(board_seq.nextval, 'an', 'abc123', 'db', '그룹 바이', default, '1988/07/17') ;

insert into boards(no, writer, password, subject, content, readhit, regdate)
values(board_seq.nextval, 'an', 'abc123', 'jsp', '웹 프로그래밍', default, '1986/08/15') ;

insert into boards(no, writer, password, subject, content, readhit, regdate)
values(board_seq.nextval, 'queen', 'abc123', 'jdbc', '제이디비씨', default, '1990/01/22') ;

insert into boards(no, writer, password, subject, content, readhit, regdate)
values(board_seq.nextval, 'queen', 'abc123', 'sql', '에스큐엘', default, '1993/06/17') ;

insert into boards(no, writer, password, subject, content, readhit, regdate)
values(board_seq.nextval, 'maria', 'abc123', '자바', 'java', default, '1990/01/22') ;

insert into boards(no, writer, password, subject, content, readhit, regdate)
values(board_seq.nextval, 'maria', 'abc123', 'sql', '호호호', default, '2008/06/17') ;

insert into boards(no, writer, password, subject, content, readhit, regdate)
values(board_seq.nextval, null, 'abc123', '자바', 'java', default, '1990/01/22') ;

insert into boards(no, writer, password, subject, content, readhit, regdate)
values(board_seq.nextval, null, 'abc123', 'sql', '호호호', default, '2008/06/17') ;
---------------------------------------------------------------
-- 상품 데이터
---------------------------------------------------------------
INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (1,'아메리카노01','스타벅스','americano01.png',100,6000,'beverage','아메리카노는 에스프레소에 물을 추가한 음료로 강렬한 향과 맛을 가지고 있습니다. 에스프레소의 양과 물의 비율에 따라 진하거나 가벼운 맛을 즐길 수 있습니다.',3,TO_DATE('90/12/22','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (2,'아메리카노02','메가커피','americano02.png',100,5000,'beverage','아메리카노는 에스프레소에 물을 추가한 음료입니다.',4,TO_DATE('80/07/26','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (3,'아메리카노03','컴포즈커피','americano03.png',100,4000,'beverage','아메리카노는 에스프레소에 물을 추가한 음료입니다.',5,TO_DATE('23/06/02','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (4,'카푸치노01','빽다방','cappuccino01.png',100,6000,'beverage','카푸치노는 에스프레소와 스팀밀크로 만든 커피입니다.',3,TO_DATE('80/07/26','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (5,'카푸치노02','이디야','cappuccino02.png',100,5000,'beverage','카푸치노는 에스프레소와 스팀밀크로 만든 커피입니다.',4,TO_DATE('23/06/02','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (6,'카푸치노03','투썸플레이스','cappuccino03.png',100,4000,'beverage','카푸치노는 에스프레소와 스팀밀크로 만든 커피입니다.',5,TO_DATE('95/05/04','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (7,'커피01','스타벅스','coffee01.png',100,6000,'beverage','커피는 아라비카와 로부스타 원두로 만들어집니다.',6,TO_DATE('80/07/17','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (8,'커피02','메가커피','coffee02.jpg',100,5000,'beverage','커피는 아라비카와 로부스타 원두로 만들어집니다.',3,TO_DATE('90/12/22','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (9,'에스프레소01','컴포즈커피','eseupeuleso_01.png',100,4000,'beverage','에스프레소는 고농축 커피입니다.',4,TO_DATE('90/12/22','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (10,'에스프레소02','빽다방','eseupeuleso_02.png',100,3000,'beverage','에스프레소는 고농축 커피입니다.',5,TO_DATE('90/12/22','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (11,'쥬스01','이디야','juice01.png',100,3000,'beverage','과일이나 채소를 갈아서 만든 음료입니다.',5,TO_DATE('23/08/15','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (12,'쥬스02','투썸플레이스','juice02.png',100,6000,'beverage','과일이나 채소를 갈아서 만든 음료입니다.',6,TO_DATE('80/07/17','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (13,'우유01','스타벅스','milk01.jpg',100,4000,'beverage','우유는 다양한 요리에 사용됩니다.',4,TO_DATE('80/07/17','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (14,'우유02','메가커피','milk02.jpg',100,3000,'beverage','우유는 다양한 요리에 사용됩니다.',5,TO_DATE('90/12/22','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (15,'레드 와인 01','컴포즈커피','redwine01.png',100,6000,'beverage','레드 와인은 붉은 포도로 만들어집니다.',6,TO_DATE('90/12/22','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (16,'레드 와인 02','빽다방','redwine02.png',100,5000,'beverage','레드 와인은 붉은 포도로 만들어집니다.',3,TO_DATE('80/07/26','RR/MM/DD'));


INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (17,'바닐라 라떼 01','이디야','vanilla_latte_01.png',100,3000,'beverage','바닐라라떼는 에스프레소에 스팀밀크와 바닐라 시럽을 추가한 커피 음료입니다.',5,TO_DATE('95/05/04','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (18,'바닐라 라떼 02','투썸플레이스','vanilla_latte_02.png',100,6000,'beverage','바닐라라떼는 달콤하고 부드러운 커피 음료입니다.',6,TO_DATE('23/08/15','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (19,'바닐라 라떼 03','스타벅스','vanilla_latte_03.png',100,5000,'beverage','바닐라 시럽이 들어간 커피 음료입니다.',3,TO_DATE('80/07/17','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (20,'화이트 와인 01','메가커피','whitewine01.png',100,4000,'beverage','화이트 와인은 흰 포도로 만들어지는 와인입니다.',4,TO_DATE('90/12/22','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (21,'화이트 와인 02','컴포즈커피','whitewine02.png',100,3000,'beverage','화이트 와인은 가볍고 상쾌한 맛이 특징입니다.',5,TO_DATE('80/07/17','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (22,'브리오슈01','뚜레쥬르','brioche_01.png',100,3000,'bread','버터와 계란이 풍부한 프랑스식 빵입니다.',6,TO_DATE('95/05/04','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (23,'브리오슈02','성심당','brioche_02.png',100,6000,'bread','부드러운 식감의 프랑스 빵입니다.',3,TO_DATE('23/08/15','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (24,'브리오슈03','던킨도너츠','brioche_03.png',100,5000,'bread','버터 풍미가 강한 빵입니다.',4,TO_DATE('80/07/17','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (25,'브리오슈04','파리바게뜨','brioche_04.png',100,4000,'bread','달콤하고 부드러운 빵입니다.',5,TO_DATE('90/12/22','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (26,'브리오슈05','이성당','brioche_05.png',100,3000,'bread','풍부한 버터 향이 특징입니다.',6,TO_DATE('90/12/22','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (27,'치아바타01','삼송빵집','ciabatta_01.png',100,5000,'bread','이탈리아 전통 빵입니다.',3,TO_DATE('80/07/17','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (28,'치아바타02','태극당','ciabatta_02.png',100,4000,'bread','겉은 바삭하고 속은 부드러운 빵입니다.',4,TO_DATE('90/12/22','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (29,'치아바타03','뚜레쥬르','ciabatta_03.png',100,3000,'bread','이탈리아 스타일 빵입니다.',5,TO_DATE('90/12/22','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (30,'치아바타04','성심당','ciabatta_04.png',100,6000,'bread','겉은 바삭하고 속은 촉촉합니다.',6,TO_DATE('80/07/26','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (31,'치아바타05','던킨도너츠','ciabatta_05.png',100,5000,'bread','쫀득한 식감의 빵입니다.',3,TO_DATE('23/06/02','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (32,'치아바타06','파리바게뜨','ciabatta_06.png',100,4000,'bread','이탈리아식 빵입니다.',4,TO_DATE('95/05/04','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (33,'치아바타07','이성당','ciabatta_07.png',100,3000,'bread','담백한 맛이 특징입니다.',5,TO_DATE('23/08/15','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (34,'크로와상01','삼송빵집','croissant_01.png',100,4000,'bread','버터로 만든 프랑스 빵입니다.',4,TO_DATE('90/12/22','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (35,'크로와상02','태극당','croissant_02.png',100,3000,'bread','층층이 버터가 들어간 빵입니다.',5,TO_DATE('80/07/26','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (36,'크로와상03','뚜레쥬르','croissant_03.png',100,6000,'bread','바삭한 프랑스 빵입니다.',6,TO_DATE('23/06/02','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (37,'크로와상04','성심당','croissant_04.png',100,5000,'bread','버터향이 풍부한 빵입니다.',3,TO_DATE('95/05/04','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (38,'크로와상05','던킨도너츠','croissant_05.png',100,4000,'bread',NULL,4,TO_DATE('23/08/15','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (39,'크로와상06','파리바게뜨','croissant_06.png',100,3000,'bread',NULL,5,TO_DATE('80/07/17','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (40,'크로와상07','이성당','croissant_07.png',100,6000,'bread','프랑스 전통 빵입니다.',6,TO_DATE('90/12/22','RR/MM/DD'));

commit ;
select count(*) from products ;

-- 시퀀스 만들기
-- DROP SEQUENCE product_seq ;

DROP SEQUENCE ORAMAN.PRODUCT_SEQ ; 

CREATE SEQUENCE ORAMAN.PRODUCT_SEQ 
START WITH 41 
INCREMENT BY 1 
MINVALUE 0 
NOCYCLE NOCACHE NOORDER ;


INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (PRODUCT_SEQ.NEXTVAL,'크로와상08','삼송빵집','croissant_08.png',100,5000,'bread','겹겹이 버터가 들어간 빵입니다.',3,TO_DATE('80/07/17','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (PRODUCT_SEQ.NEXTVAL,'프렌치 바게트 01','태극당','french_baguette_01.png',100,6000,'bread','프랑스 대표 빵입니다.',6,TO_DATE('80/07/26','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (PRODUCT_SEQ.NEXTVAL,'프렌치 바게트 02','뚜레쥬르','french_baguette_02.png',100,5000,'bread','길고 바삭한 빵입니다.',3,TO_DATE('23/06/02','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (PRODUCT_SEQ.NEXTVAL,'프렌치 바게트 03','성심당','french_baguette_03.png',100,4000,'bread','프랑스 전통 빵입니다.',4,TO_DATE('95/05/04','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (PRODUCT_SEQ.NEXTVAL,'초콜릿 케익','빌리엔젤','chocolate_cake_01.png',100,6000,'cake','초콜릿으로 만든 달콤한 케이크입니다.',6,TO_DATE('23/08/15','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (PRODUCT_SEQ.NEXTVAL,'스폰지 케익 01','도레도레','sponge_cake_01.png',100,4000,'cake','부드럽고 가벼운 케이크입니다.',4,TO_DATE('23/06/02','RR/MM/DD'));

INSERT INTO ORAMAN.PRODUCTS (NUM,NAME,COMPANY,IMAGE,STOCK,PRICE,CATEGORY,CONTENT,POINT,INPUTDATE)
VALUES (PRODUCT_SEQ.NEXTVAL,'마카롱 01','라뒤레','macaron01.png',100,5000,'macaron','머랭으로 만든 프랑스 디저트입니다.',3,TO_DATE('90/12/22','RR/MM/DD'));
commit ;
---------------------------------------------------------------
-- 주문 데이터, 주문 상품 데이터
---------------------------------------------------------------
insert into orders(oid, mid, orderdate) values(order_seq.nextval, 'an', sysdate) ;
select max(oid) from orders ;

insert into orderdetails(odid, oid, pnum, qty) 
values(orderdetail_seq.nextval, 1, 1, 10) ;

insert into orderdetails values(orderdetail_seq.nextval, 1, 2, 5) ;
-------------------------------------------------------------------------
insert into orders(oid, mid, orderdate) values(order_seq.nextval, 'soon', sysdate) ;
select max(oid) from orders ;
insert into orderdetails(odid, oid, pnum, qty) values(orderdetail_seq.nextval, 2, 1, 10) ;
insert into orderdetails values(orderdetail_seq.nextval, 2, 3, 10) ;
-------------------------------------------------------------------------
insert into orders(oid, mid, orderdate) values(order_seq.nextval, 'an', sysdate) ;
select max(oid) from orders ;
insert into orderdetails(odid, oid, pnum, qty) values(orderdetail_seq.nextval, 3, 1, 5) ;
insert into orderdetails values(orderdetail_seq.nextval, 3, 4, 20) ;

commit ;

select * from members ;
select * from boards ORDER BY no DESC  ;
select * from products ORDER BY NUM DESC  ;
select * from orders ;
select * from orderdetails ;

