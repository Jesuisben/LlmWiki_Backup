-- 데이터 추가하기
-- 고객 데이터 추가
insert into members values('shin', '신동진', '마포 공덕');
insert into members values('yoo', '유남균', '용산 용문');
-- 상품 데이터 추가
insert into products values('P01', '청바지');
insert into products values('P02', 'T셔츠');
insert into products values('P03', '블라우스');
insert into products values('P04', '선글라스');
-- 주문 데이터 추가
insert into orders values(1001, '2022/03/01', 'shin');
insert into orders values(1002, '2022/07/17', 'yoo');
insert into orders values(1003, '2022/08/15', 'shin');
-- 주문 상세 데이터 추가
insert into orderdetails values(1001, 'P01', 10);
insert into orderdetails values(1001, 'P02', 20);
insert into orderdetails values(1002, 'P01', 30);
insert into orderdetails values(1002, 'P03', 40);
insert into orderdetails values(1003, 'P03', 50);
insert into orderdetails values(1003, 'P04', 60);
commit ;

-- 참조 무결성 제약 조건 (참조 무결성 테스트?) (오류나야 정상)
-- 송장 번호 1003을 주문 취소할 수 있나요?
delete from orders where oid = 1003 ;
-- 자식 테이블에 관련 데이터가 들어 있어서 삭제가 불가능합니다.
-- ORA-02292: integrity constraint
(GOMDORI.FK_ORDERS_TO_ORDERDETAILS) violated - child record found
-- 자식 테이블 데이터를 삭제 후 부모 테이블 데이터를 삭제하면 됩니다.
delete from orderdetails where oid = 1003 ;
delete from orders where oid = 1003 ;