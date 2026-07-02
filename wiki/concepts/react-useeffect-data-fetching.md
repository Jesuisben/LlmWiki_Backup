---
title: React useEffect와 데이터 요청
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [react, typescript, frontend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf
status: growing
confidence: high
---
# React useEffect와 데이터 요청

## 정의

`useEffect`는 React 컴포넌트가 렌더링된 뒤 실행할 부수 효과(side effect)를 선언하는 Hook이다. API 요청, DOM 관련 처리, 구독 설정처럼 렌더링 자체 밖에서 일어나는 작업에 사용한다.

## 왜 중요한가

상품 상세 페이지는 URL의 상품 ID를 보고 서버에서 상품 데이터를 가져와야 한다. 이 요청은 화면 JSX를 계산하는 과정 자체가 아니라, 컴포넌트가 나타난 뒤 실행되는 부수 효과이므로 `useEffect`와 잘 맞는다.

## 핵심 설명

React 교안 p.87은 `useEffect(<function>, <dependency>)` 형태와 dependency가 props/state와 연결된다는 점을 설명한다.

```typescript
useEffect(() => {
  loadProduct(productId);
}, [productId]);
```

- dependency 배열이 비어 있으면 보통 처음 mount될 때 한 번 실행된다.
- 특정 값이 들어 있으면 그 값이 바뀔 때 다시 실행된다.
- API 요청 결과는 state에 저장해 화면을 다시 렌더링한다.

## 수업 예시

- [[summaries/2026-04-13-product-detail-useeffect-service|2026-04-13]] — 상품 상세 조회에서 `useEffect`와 `ProductService`/`ProductController` 흐름을 연결했다.

## 자주 헷갈리는 점

- dependency 배열을 잘못 쓰면 API 요청이 너무 많이 실행되거나, 반대로 최신 ID로 다시 요청하지 않을 수 있다.
- `useEffect` 안의 비동기 요청은 실패/로딩/빈 데이터 상태를 함께 고려해야 한다.
- React의 `ProductService` 파일과 Spring의 `ProductService` 클래스는 이름이 같아도 위치와 책임이 다르다.

## 관련 개념

- [[concepts/react-typescript-basics]]
- [[concepts/product-domain-flow]]
- [[concepts/spring-boot-rest-api]]
- [[comparisons/react-router-vs-spring-api-url]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf`
