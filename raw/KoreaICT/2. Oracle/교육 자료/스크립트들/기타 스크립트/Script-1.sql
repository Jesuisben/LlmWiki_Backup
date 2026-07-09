-- 데이터 추가하기
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

-- 참조 무결성 제약 조건 (참조 무결성 테스트?) (오류나야 정상)
-- 존재하지 않는 학생
insert into subjects values(9044555, 'ABC01', 'B');
-- 존재하지 않는 학과 정보 추가하기
insert into students values(9021777, '김철수', '701223-1111111', '전산과');
-- 자식 테이블에 데이터가 존재하므로 삭제 불가능
delete from departments where department = '가정 의학';