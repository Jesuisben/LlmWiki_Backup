---
title: 2026-07-02 LLM Wiki 품질 감사 리포트
created: 2026-07-02
updated: 2026-07-03
type: meta
tags: [study-log]
sources:
  - wiki/index.md
  - wiki/log.md
  - raw/Study/1. Java/Java 총정리/Java 총정리.md
  - raw/Study/1. Java/숙제/클래스 숙제 완료.md
  - raw/Study/6. AWS/교육 자료/AWS 기초 용어.pdf
  - raw/Study/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf
status: growing
confidence: high
---

# 2026-07-02 LLM Wiki 품질 감사 리포트

## 결론

이 리포트는 2026-07-02 기준으로 최신화되었다. 초기 감사에서 지적했던 “대량 ingest로 만든 얕은 초안” 문제는 핵심 페이지 고도화와 비교 페이지 추가를 거치며 줄어들었다.

이번 마감 작업에서는 감사 리포트에 남아 있던 Java 잔여 후보 2개를 처리했다.

- `raw/Study/1. Java/Java 총정리/Java 총정리.md`
- `raw/Study/1. Java/숙제/클래스 숙제 완료.md`

처리 방식은 새 요약 페이지를 추가하는 대신, 기존 Java 핵심 concept/entity 페이지를 보강하고 비교/개념 페이지를 추가하는 방향으로 잡았다.

## 현재 전체 수치

- `wiki/` Markdown 파일 수: 191개
- `wiki/index.md`의 `Total pages` 표기: 189개
- index 누락 페이지: 0개
- frontmatter 누락 페이지(`index.md`, `log.md` 제외): 0개
- frontmatter `sources: []` 페이지: 0개
- 대표 placeholder 문구 잔존 파일(아카이브/작업 로그의 기록성 언급 제외): 0개
- 깨진 위키링크 후보: 0개
- 200줄 초과 긴 페이지: 2개 (`wiki/index.md`, `wiki/log.md`)
- `status: needs-review` 또는 `confidence: low` 페이지: 0개
- 고립 페이지 후보(본문 링크 기준, index/log 제외): 0개

> 주의: 고립 페이지는 `index.md` 등록 여부가 아니라 다른 본문 페이지에서 링크되는지를 기준으로 한 보수적 후보다. 운영 문서나 최신 신규 페이지는 일시적으로 고립 후보가 될 수 있다.

## 이번 Java 잔여 후보 처리 내역

### 보강한 기존 페이지

- [[concepts/java-class-object|Java 클래스와 객체]] — 클래스 숙제의 필드/메서드/생성자, stack/heap 관점 추가
- [[concepts/java-inheritance|Java 상속]] — 상속 목적, 부모 생성자 호출, `final` 메서드 관점 추가
- [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]] — 일반/final/추상 메서드 비교, 인터페이스 기능 규격 관점 추가
- [[concepts/java-array|Java 배열]] — 배열에서 컬렉션으로 이어지는 흐름 추가
- [[entities/java|Java]] — Java 전체 학습 이력과 총정리/숙제의 복습 관점으로 재작성
- [[comparisons/primitive-vs-reference-types|기본 자료형 vs 참조 자료형]] — stack/heap, `String`, 배열, 객체 참조 관점으로 재작성

### 새로 추가한 페이지

- [[concepts/java-memory-static-final|Java 메모리, static, final]] — static/method area, stack, heap, `static`, `final` 정리
- [[comparisons/array-vs-collection|배열 vs 컬렉션]] — 배열과 List/Set/Map의 사용 기준 비교
- [[comparisons/overloading-vs-overriding|오버로딩 vs 오버라이딩]] — 다중 정의와 재정의의 차이 정리

## 현재 lint 결과

### index 누락

- 없음

### frontmatter 누락

- 없음

### frontmatter `sources: []` 페이지

- 없음

### placeholder 문구 잔존 파일

- 없음

### 깨진 위키링크 후보

- 없음

### 긴 페이지 후보

- `wiki/index.md`
- `wiki/log.md`

> 2026-07-03 검증 기준으로 200줄 초과 지식 페이지는 없고, 운영 문서인 index/log만 길다.

### needs-review / low confidence 후보

- 없음

### 고립 페이지 후보

- 없음

> FrontEnd_BackEnd 관련 summary, 환경 도구 entity, 운영 문서 `_meta` 고립 후보를 관련 concept/entity/meta 본문 링크 보강으로 해소했다.

## 아직 wiki에 거의 안 들어간 과목/기간 후보

사용자가 ingest는 직접 진행하기로 했으므로, 여기서는 잔여 후보만 유지한다.

- `raw/Study/6. AWS/2026.05.06(수) - 시작/` ~ `raw/Study/6. AWS/2026.05.08(금)/` — 2026-07-03 course-material-aware ingest 후, 같은 날 사용자가 지정한 날짜별 MD 3개가 실제 수업 메모를 포함함을 재확인해 기존 AWS wiki를 날짜 MD + 교육자료 PDF/실습 관리 대장 기준으로 보강·정정 완료. AWS 총정리류는 제외함.
- `raw/Study/7. Ci&CD/2026.05.11(월) - 시작/` ~ `raw/Study/7. Ci&CD/2026.05.13(수)/` — 다음 잔여 후보. 사용자 날짜 MD가 템플릿인지 원본 재확인 필요.
- `raw/Study/8. Passwordless/2026.05.14(목)/` ~ `raw/Study/8. Passwordless/2026.05.21(목)/` — 사용자가 별도 ingest 예정.
- `raw/Study/10. Python/2026.06.19(금)/` ~ `raw/Study/10. Python/2026.06.30(화)/` — 사용자가 별도 ingest 예정. 일부는 시간표 템플릿 가능성이 있어 원본 재확인 필요.

## 앞으로의 고품질 ingest 기준

- summary 페이지는 커리큘럼 위치, 이전/다음 흐름, 핵심 실습, 헷갈림 포인트, 관련 링크, 구체 raw 출처를 포함한다.
- concept 페이지는 일반론보다 수업 예제, 자주 헷갈리는 점, 이전/이후 개념 연결을 우선한다.
- entity 페이지는 기술의 첫 등장, 날짜별 학습 이력, 관련 기능 구현, 프로젝트/면접 설명 관점을 포함한다.
- comparison/query 페이지는 여러 수업에 걸쳐 반복되는 혼동을 표와 예제로 보존한다.

## 이번 최신화에서 처리 완료된 감사 리포트 잔여 후보

- `raw/Study/1. Java/Java 총정리/Java 총정리.md` — 기존 Java concept/entity/comparison 보강에 반영 완료
- `raw/Study/1. Java/숙제/클래스 숙제 완료.md` — static/메모리/컬렉션/상속/추상화 관점으로 반영 완료

## 추가 정리: 깨진 위키링크 후보 제거

- `wiki/concepts/markdown-basic-syntax.md`의 Obsidian 링크 문법 예시를 HTML entity 기반 코드 표기로 바꿔 실제 위키링크로 인식되지 않게 했다.
- `wiki/summaries/2026-07-01-python-pandas-dataframe.md`의 Pandas 이중 대괄호 예시를 HTML entity 기반 코드 표기로 바꿔 리스트 인덱싱 예시가 위키링크로 오인되지 않게 했다.

## 추가 정리: FrontEnd_BackEnd 고립 페이지 연결 보강

- `wiki/concepts/fullstack-project-flow.md`, `spring-boot-rest-api.md`, `react-typescript-basics.md`, `jwt-session-cookie-auth.md`, `shopping-cart-flow.md`, `order-flow.md`, `pagination-search.md`의 수업 예시를 실제 summary 위키링크로 보강했다.
- `wiki/entities/spring-boot.md`, `react.md`, `typescript.md`의 학습 맥락을 실제 날짜별 summary와 연결했다.
- 그 결과 고립 페이지 후보는 20개에서 2개로 줄었다. 남은 2개는 운영 문서 성격의 `_meta` 페이지다.

## 추가 정리: `sources: []` 페이지 제거

- `wiki/_meta/hermes-home-laptop-setup.md`의 frontmatter에 `AGENTS.md`, `wiki/index.md`, `wiki/log.md`, `wiki/_meta/hermes-default-profile-mode-system.md`를 출처로 명시했다.
- 그 결과 frontmatter `sources: []` 페이지는 1개에서 0개로 줄었다.

## 추가 정리: 남은 `_meta` 고립 페이지 연결

- `wiki/_meta/llm-wiki-operating-model.md`의 관련 페이지에 `wiki/_meta/agent-coding-guidelines.md`와 이 감사 리포트를 연결했다.
- 그 결과 고립 페이지 후보는 2개에서 0개로 줄었다.

## 추가 정리: UI&UX course-material-aware 백필

- `raw/Study/3. UI&UX`의 2026-03-23~2026-03-27 사용자 정리 MD 5개를 `웹 서비스 Ui&UX.pdf`, `HTML&JS&CSS 이론(new).pdf`, `IT 관련 용어.pdf`, `library&framework.png`, 대표 HTML 소스코드와 대조해 summary 5개를 재작성했다.
- 기존 `html-css-basics`, `javascript-dom`, `bootstrap-basics`, `jquery-basics` concept에 교육자료·소스코드 대조 메모를 추가했다.
- `html`, `css`, `javascript`, `bootstrap`, `jquery` entity의 학습 이력과 출처를 UI&UX 교육자료 기준으로 보강했다.
- 반복 혼동으로 남을 가능성이 높은 `Library vs Framework`, `inline style vs internal CSS vs external CSS`, `GET vs POST` 비교 페이지를 추가했다.

## 추가 정리: Oracle course-material-aware 백필

- `raw/Study/2. Oracle`의 2026-03-13~2026-03-20 사용자 정리 MD 6개를 `오라클 교안.pdf`, `디비버(Dbeaver) 사용법.pdf`, `디비버(Dbeaver) 사용법(version 2.0).pdf`, A01~A07 SQL 스크립트와 대조해 summary 6개를 재작성했다.
- `oracle-database`, `dbeaver` entity의 날짜별 학습 이력과 실습 도구 맥락을 보강했다.
- 반복 혼동으로 남을 가능성이 높은 `ON DELETE SET NULL vs CASCADE`, `DDL vs DML vs DQL`, `Primary Key vs Foreign Key`, `Oracle Inner Join vs Outer Join` 비교 페이지를 추가했다.

## 추가 정리: Java course-material-aware 백필

- `raw/Study/1. Java`의 2026-02-26~2026-03-13 사용자 정리 MD 12개, `Java 총정리.md`, `클래스 숙제 완료.md`를 주 자료로 삼고 `Java 교안(이론_20260226).pdf`, `IntelliJ 교안.pdf`, `Github 교안(실습).pdf`, 관련 문제 이미지를 대조해 기존 Java 1차 wiki 정리본을 보강했다.
- 기존 Java summary 12개를 커리큘럼 위치, 이전/다음 흐름, 핵심 실습, 헷갈림 포인트, 구체 출처 중심으로 재작성했다.
- 기존 Java concept 13개와 Java/Git/GitHub/IntelliJ entity 4개, Java comparison 4개를 수업 예제와 교안 출처 중심으로 보강했다.
- 새 comparison은 만들지 않았다. 이미 있던 `기본 자료형 vs 참조 자료형`, `배열 vs 컬렉션`, `오버로딩 vs 오버라이딩`, `인터페이스 vs 추상 클래스`를 고도화하는 방식이 중복을 줄이는 데 적합했다.
## 추가 정리: AWS course-material-aware ingest

- `raw/Study/6. AWS`의 2026-05-06~2026-05-08 날짜 MD 3개와 `AWS 기초 용어.pdf`, `cloud.01.AWS 교안(이론_미니파일).pdf`, `cloud.02.AWS 교안(실습).pdf`, `cloud.03.AWS 교안(이론).pdf`, `실습 관리 대장(텍스트).md`를 주 출처로 삼아 AWS 과정을 정리했다. 이후 같은 날 날짜별 MD 3개가 실제 수업 메모를 포함함을 재확인해, 기존 AWS summary/concept/entity/comparison을 날짜별 MD 중심으로 보강·정정했다.
- summary 3개는 Cloud/VPC/EC2, VPC·EC2·Nginx·Spring Boot·RDS, Route 53/Load Balancer/HTTPS 흐름을 날짜별 학습 맥락으로 복원했다.
- concept 4개는 AWS 네트워킹, EC2 배포, RDS 연결, Route 53/ALB/HTTPS 배포 구조를 정리했다.
- entity 4개(`AWS`, `Amazon EC2`, `Amazon RDS`, `Amazon Route 53`)와 comparison 2개(`EC2 vs RDS`, `CLB vs ALB`)는 이후 CI/CD·Passwordless 배포 학습과 연결할 기반으로 유지·보강했다.
- 다음 잔여 후보는 `raw/Study/7. Ci&CD/2026.05.11(월) - 시작/` ~ `raw/Study/7. Ci&CD/2026.05.13(수)/`이다.
