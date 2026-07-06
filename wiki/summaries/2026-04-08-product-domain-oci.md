---
title: 2026-04-08 상품 도메인과 OCI 소개
created: 2026-07-06
updated: 2026-07-06
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md
status: growing
confidence: high
---

# 2026-04-08 상품 도메인과 OCI 소개

## 한 줄 요약

상품 기능 구현을 시작하며 Category enum, Product Entity, 상품 이미지/설명/재고 구조를 만들고 OCI를 클라우드 후보로 소개받았다.

## 배운 내용

- 주제: 상품 도메인 시작
- 커리큘럼 위치: Java/Oracle/UI&UX 다음 단계에서 React 화면과 Spring Boot API를 실제 기능 단위로 연결하는 FrontEnd_BackEnd 과정이다.
- 이전 흐름: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]에서 HTML/CSS/JavaScript/Bootstrap/jQuery로 브라우저 화면을 만들었다.
- 다음 흐름: 이 날짜의 내용은 이후 Linux/AWS/CI/CD에서 Spring Boot 애플리케이션을 서버에 올리고 배포하는 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

회원 인증 다음 단계는 실제 쇼핑몰 기능의 중심인 상품이다. Category와 Product를 만들면서 Java enum, Entity 필드, DB 저장 구조가 화면 기능과 연결됐다.

## 핵심 개념

Category enum에는 ALL/BREAD/BEVERAGE/CAKE/MACARON 같은 상수와 한글 설명을 둔다. Product는 상품명, 가격, 카테고리, 재고, 이미지, 설명 등 화면과 DB가 공유해야 할 데이터를 담는다.

## 실습 / 예제

- 원본 노트의 코드는 대부분 Spring Boot `controller/service/repository/entity/dto/config`와 React `pages/types/api/routes` 파일을 실제로 수정하는 형태다.
- 실습을 복습할 때는 파일명 전체를 외우기보다 “요청 URL → Controller → Service → Repository/DB → DTO/응답 → React state/render” 순서로 따라가면 된다.
- 실습 데이터나 비밀번호 형태의 예시는 위키에 그대로 재노출하지 않고 역할 중심으로만 정리했다.

## 헷갈린 점 / 질문

enum은 단순 문자열보다 허용 가능한 값을 제한해 오타와 잘못된 카테고리를 줄인다. OCI는 Oracle Cloud Infrastructure로 AWS와 비슷한 클라우드 서비스라는 정도로 먼저 등장했다.

## 관련 페이지

- [[concepts/product-domain-flow|상품 도메인 기능 흐름]], [[comparisons/entity-vs-dto|Entity vs DTO]], [[entities/mysql|MySQL]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md`
