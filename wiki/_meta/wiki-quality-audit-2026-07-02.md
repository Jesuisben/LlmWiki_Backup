---
title: 2026-07-02 LLM Wiki 품질 감사 리포트
created: 2026-07-02
updated: 2026-07-09
type: meta
tags: [study-log]
sources:
  - wiki/index.md
  - wiki/log.md
  - raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md
  - raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md
  - raw/KoreaICT/2. Oracle/Oracle 총정리/Oracle 총정리.md
  - raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md
  - raw/KoreaICT/6. AWS/교육 자료/AWS 기초 용어.pdf
  - raw/KoreaICT/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf
  - raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md
status: growing
confidence: high
---

# 2026-07-02 LLM Wiki 품질 감사 리포트

## 결론

이 리포트는 2026-07-09 기준으로 다시 정정되었다. 이전 기록에는 4·5과목 재ingest 직후의 기계적 lint 결과를 근거로 “모두 통과”, “0개”, “확인 완료”처럼 과하게 단정한 표현이 섞여 있었다.

이번 정정의 기준은 “파일 존재·frontmatter·링크만 맞는 상태”를 완료로 보지 않는 것이다. 4과목 FrontEnd_BackEnd와 5과목 Linux는 현재 raw MD 기준으로 날짜별 summary와 기능 흐름별 concept/entity/comparison을 다시 읽고, 실제 수업 흐름·실습·헷갈린 점이 복원되는지까지 재검증하는 대상으로 재분류했다. 아래 수치는 구조 점검 결과이지 내용 품질의 최종 완료 선언이 아니다.

## 현재 전체 수치

- `wiki/` Markdown 파일 수: 243개
- `wiki/index.md`의 `Total pages` 표기: 241개
- index 누락 페이지: 0개
- frontmatter 누락 페이지(`index.md`, `log.md` 제외): 0개
- frontmatter `sources: []` 페이지: 0개
- 대표 자리표시자 문구 잔존 파일(아카이브/작업 로그의 기록성 언급 제외): 0개
- 깨진 위키링크 후보: 0개
- 200줄 초과 긴 페이지: 3개 (`wiki/index.md`, `wiki/log.md`, `wiki/_meta/wiki-quality-audit-2026-07-02.md`)
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

### 자리표시자 문구 잔존 파일

- 없음

### 깨진 위키링크 후보

- 없음

### 긴 페이지 후보

- `wiki/index.md`
- `wiki/log.md`
- `wiki/_meta/wiki-quality-audit-2026-07-02.md`

> 2026-07-04 검증 기준으로 200줄 초과 지식 페이지는 없고, 운영 문서인 index/log와 누적 감사 리포트만 길다.

### needs-review / low confidence 후보

- 없음

### 고립 페이지 후보

- 없음

> FrontEnd_BackEnd 관련 summary, 환경 도구 entity, 운영 문서 `_meta` 고립 후보를 관련 concept/entity/meta 본문 링크 보강으로 해소했다.

## 아직 wiki에 거의 안 들어간 과목/기간 후보

사용자가 ingest는 직접 진행하기로 했으므로, 여기서는 잔여 후보만 유지한다.

- `raw/KoreaICT/6. AWS/2026.05.06(수) - 시작/` ~ `raw/KoreaICT/6. AWS/2026.05.08(금)/` — 2026-07-03 course-material-aware ingest 후, 같은 날 사용자가 지정한 날짜별 MD 3개가 실제 수업 메모를 포함함을 재확인해 기존 AWS wiki를 날짜 MD + 교육자료 PDF/실습 관리 대장 기준으로 보강·정정 완료. AWS 총정리류는 제외함.
- `raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/` ~ `raw/KoreaICT/7. Ci&CD/2026.05.13(수)/` — 2026-07-03 날짜별 MD 3개가 실제 수업 메모를 포함함을 확인하고, CI/CD 자동화·GitHub Actions·Spring Boot Docker/EC2 배포·Route 53/ALB/HTTPS 복습·Terraform·S3 파일 업로드를 wiki에 반영 완료.
- `raw/KoreaICT/8. Passwordless/2026.05.14(목)/` ~ `raw/KoreaICT/8. Passwordless/2026.05.21(목)/` — 2026-07-03 날짜별 ingest 완료. X1280 인증 흐름, QR/앱 승인, Spring Boot 연동, REST API/Postman, AAM/APE·FilingBox 보안 제품군 흐름을 wiki에 반영함.
- `raw/KoreaICT/10. Python/2026.06.19(금)/` ~ `raw/KoreaICT/10. Python/2026.06.30(화)/` — 2026-07-03 날짜별 ingest 완료. Python 설치·기초 문법·컬렉션·함수·모듈·표준 라이브러리·객체지향·예외 처리·파일/정규표현식·XML/JSON·Jupyter/Pandas 입문 흐름을 wiki에 반영함.
- `raw/KoreaICT/10. Python/2026.07.01(수)/` ~ `raw/KoreaICT/10. Python/2026.07.03(금)/` — Pandas DataFrame 조회·입출력, 결합·재구조화, `groupby` 집계·시각화 흐름을 기존 Python/Pandas/Jupyter 페이지에 반영 완료.

## 앞으로의 고품질 ingest 기준

- summary 페이지는 커리큘럼 위치, 이전/다음 흐름, 핵심 실습, 헷갈림 포인트, 관련 링크, 구체 raw 출처를 포함한다.
- concept 페이지는 일반론보다 수업 예제, 자주 헷갈리는 점, 이전/이후 개념 연결을 우선한다.
- entity 페이지는 기술의 첫 등장, 날짜별 학습 이력, 관련 기능 구현, 프로젝트/면접 설명 관점을 포함한다.
- comparison/query 페이지는 여러 수업에 걸쳐 반복되는 혼동을 표와 예제로 보존한다.

## 이번 최신화에서 처리 완료된 감사 리포트 잔여 후보

- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md` — 기존 Java concept/entity/comparison 보강에 반영 완료
- `raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md` — static/메모리/컬렉션/상속/추상화 관점으로 반영 완료

## 추가 정리: 1~4 과목 총정리 MD 복습 허브 생성

- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`, `raw/KoreaICT/2. Oracle/Oracle 총정리/Oracle 총정리.md`, `raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`, `raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md`를 균등 재점검했다.
- 날짜별 summary를 대체하지 않고 과목 단위 복습 허브로 쓰기 위해 다음 summary 4개를 추가했다.
  - [[summaries/2026-03-13-java-subject-review|Java 총정리]]
  - [[summaries/2026-03-20-oracle-subject-review|Oracle 총정리]]
  - [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]
  - [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]]
- `Java`, `Oracle Database`, `HTML`, `Spring Boot` entity에서 각 총정리 summary로 연결해 과목별 진입점을 보강했다.

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

- `raw/KoreaICT/3. UI&UX`의 2026-03-23~2026-03-27 사용자 정리 MD 5개를 `웹 서비스 Ui&UX.pdf`, `HTML&JS&CSS 이론(new).pdf`, `IT 관련 용어.pdf`, `library&framework.png`, 대표 HTML 소스코드와 대조해 summary 5개를 재작성했다.
- 기존 `html-css-basics`, `javascript-dom`, `bootstrap-basics`, `jquery-basics` concept에 교육자료·소스코드 대조 메모를 추가했다.
- `html`, `css`, `javascript`, `bootstrap`, `jquery` entity의 학습 이력과 출처를 UI&UX 교육자료 기준으로 보강했다.
- 반복 혼동으로 남을 가능성이 높은 `Library vs Framework`, `inline style vs internal CSS vs external CSS`, `GET vs POST` 비교 페이지를 추가했다.

## 추가 정리: Oracle course-material-aware 백필

- `raw/KoreaICT/2. Oracle`의 2026-03-13~2026-03-20 사용자 정리 MD 6개를 `오라클 교안.pdf`, `디비버(Dbeaver) 사용법.pdf`, `디비버(Dbeaver) 사용법(version 2.0).pdf`, A01~A07 SQL 스크립트와 대조해 summary 6개를 재작성했다.
- `oracle-database`, `dbeaver` entity의 날짜별 학습 이력과 실습 도구 맥락을 보강했다.
- 반복 혼동으로 남을 가능성이 높은 `ON DELETE SET NULL vs CASCADE`, `DDL vs DML vs DQL`, `Primary Key vs Foreign Key`, `Oracle Inner Join vs Outer Join` 비교 페이지를 추가했다.

## 추가 정리: Java course-material-aware 백필

- `raw/KoreaICT/1. Java`의 2026-02-26~2026-03-13 사용자 정리 MD 12개, `Java 총정리.md`, `클래스 숙제 완료.md`를 주 자료로 삼고 `Java 교안(이론_20260226).pdf`, `IntelliJ 교안.pdf`, `Github 교안(실습).pdf`, 관련 문제 이미지를 대조해 기존 Java 1차 wiki 정리본을 보강했다.
- 기존 Java summary 12개를 커리큘럼 위치, 이전/다음 흐름, 핵심 실습, 헷갈림 포인트, 구체 출처 중심으로 재작성했다.
- 기존 Java concept 13개와 Java/Git/GitHub/IntelliJ entity 4개, Java comparison 4개를 수업 예제와 교안 출처 중심으로 보강했다.
- 새 comparison은 만들지 않았다. 이미 있던 `기본 자료형 vs 참조 자료형`, `배열 vs 컬렉션`, `오버로딩 vs 오버라이딩`, `인터페이스 vs 추상 클래스`를 고도화하는 방식이 중복을 줄이는 데 적합했다.
## 추가 정리: AWS course-material-aware ingest

- `raw/KoreaICT/6. AWS`의 2026-05-06~2026-05-08 날짜 MD 3개와 `AWS 기초 용어.pdf`, `cloud.01.AWS 교안(이론_미니파일).pdf`, `cloud.02.AWS 교안(실습).pdf`, `cloud.03.AWS 교안(이론).pdf`, `실습 관리 대장(텍스트).md`를 주 출처로 삼아 AWS 과정을 정리했다. 이후 같은 날 날짜별 MD 3개가 실제 수업 메모를 포함함을 재확인해, 기존 AWS summary/concept/entity/comparison을 날짜별 MD 중심으로 보강·정정했다.
- summary 3개는 Cloud/VPC/EC2, VPC·EC2·Nginx·Spring Boot·RDS, Route 53/Load Balancer/HTTPS 흐름을 날짜별 학습 맥락으로 복원했다.
- concept 4개는 AWS 네트워킹, EC2 배포, RDS 연결, Route 53/ALB/HTTPS 배포 구조를 정리했다.
- entity 4개(`AWS`, `Amazon EC2`, `Amazon RDS`, `Amazon Route 53`)와 comparison 2개(`EC2 vs RDS`, `CLB vs ALB`)는 이후 CI/CD·Passwordless 배포 학습과 연결할 기반으로 유지·보강했다.
- 다음 잔여 후보는 `raw/KoreaICT/10. Python/2026.06.19(금)/` ~ `raw/KoreaICT/10. Python/2026.06.30(화)/`이다.

## 추가 정리: Ci&CD 날짜별 ingest

- `raw/KoreaICT/7. Ci&CD`의 2026-05-11~2026-05-13 날짜별 MD 3개와 CI&CD/AWS 교안을 확인해, GitHub Actions 기반 Spring Boot CI/CD, Route 53/ALB/HTTPS 앞단 복습, Terraform, S3 파일 업로드를 정리했다.
- 새 summary 3개는 날짜별 학습 맥락을 보존하고, 새 concept/entity 6개는 [[concepts/middle-project-cicd-deploy-flow|중간 프로젝트 CI/CD 배포 흐름]]과 AWS/Spring Boot 기존 페이지에 연결했다.
- 원본에 포함된 Docker token, AWS access key, RDS password, IP/endpoint 예시는 wiki에 재노출하지 않고 `{...}` 형태의 역할 설명으로 일반화했다.


## 추가 정리: Python 2026-06-19~2026-06-30 날짜별 ingest

- `raw/KoreaICT/10. Python`의 2026-06-19~2026-06-30 날짜별 MD 8개를 읽어 Pandas 이전 Python 기초/라이브러리/데이터 처리 흐름을 정리했다.
- 새 summary 8개는 Python 설치·기초 문법, 제어문/컬렉션, dict/comprehension/내장 함수, 함수/모듈/패키지, 표준 라이브러리/OOP, 예외/파일/정규표현식, XML/JSON/Jupyter, Pandas Series/DataFrame 입문 순서를 보존한다.
- 새 concept 5개를 생성해 기존 [[entities/python|Python]], [[entities/pandas|Pandas]], [[entities/jupyter-notebook|Jupyter Notebook]], [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]과 연결했다.
- 이로써 감사 리포트의 Python 2026-06-19~06-30 잔여 후보는 처리 완료 상태다.

## 추가 정리: Python 2026-07-03 Pandas groupby와 시각화

- `raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md`를 읽어 `groupby`, `agg`, 다중 색인 정리, 사용자 정의 집계 함수, `DataFrameGroupBy`, `transform`, `pd.cut`, matplotlib 그래프 흐름을 정리했다.
- 새 summary 1개는 2026-07-02의 `concat`/`merge`/`pivot` 다음 단계로 “범주별 요약과 시각화”를 연결한다.
- 새 concept `[[concepts/pandas-groupby-aggregation|Pandas groupby와 집계]]`는 `agg()`와 `transform()`의 차이, 다중 색인 정리, 연속형 변수 범주화를 초보자 관점에서 보존한다.
- 새 entity `[[entities/matplotlib|matplotlib]]`는 Pandas 분석 결과를 그래프로 확인하는 도구로 등록했다.

## 추가 정리: Java/Oracle subject-review hub 고도화

- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`와 날짜별 Java MD를 기준으로 `[[summaries/2026-03-13-java-subject-review|Java 총정리]]`를 단순 목차형 복습 허브에서 커리큘럼 흐름형 허브로 보강했다.
- Java 허브는 문법/변수/형변환/제어문/배열/클래스/생성자/상속/다형성/추상화/static-final을 하나의 학습 경로로 연결하고, `[[entities/java|Java]]` entity에 날짜별 학습 이력과 복습 경로를 보강했다.
- `raw/KoreaICT/2. Oracle/Oracle 총정리/Oracle 총정리.md`와 날짜별 Oracle MD를 기준으로 `[[summaries/2026-03-20-oracle-subject-review|Oracle 총정리]]`를 DBMS/SQL, DBeaver 접속, 트랜잭션, 제약조건, JOIN/서브쿼리, ERD/정규화 흐름으로 보강했다.
- Oracle 허브와 `[[entities/oracle-database|Oracle Database]]` entity에는 원본의 로컬 실습용 접속값을 재노출하지 않는 보안 메모를 남기고, 역할·절차 중심으로 설명을 일반화했다.
- 신규 페이지는 만들지 않았으므로 index `Total pages`는 235를 유지했다.

## 과거 기록 정정: FrontEnd_BackEnd 변경 MD 기준 구조 점검

- 이 섹션은 2026-07-06 당시 `raw/KoreaICT/4. FrontEnd_BackEnd` 변경 MD 19개를 기준으로 수행한 구조 점검 기록이다. 이후 사용자가 지적한 대로, 이 결과만으로 내용 품질이 충분히 고도화되었다고 보기는 어렵다.
- 점검 범위:
  - 날짜별 summary 18개와 `[[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]]`
  - `[[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]`, `[[concepts/product-domain-flow|상품 도메인 기능 흐름]]`, `[[concepts/shopping-cart-flow|장바구니 기능 흐름]]`, `[[concepts/order-flow|주문 기능 흐름]]`, `[[concepts/pagination-search|페이징과 검색]]`
  - 신규 durable page `[[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]`, `[[concepts/axios-interceptor-error-handling|Axios interceptor와 API 오류 처리]]`, `[[comparisons/jpql-vs-sql|JPQL vs SQL]]`
- 당시 구조 점검 결과: scoped frontmatter 누락 0개, `sources: []` 0개, `raw/KoreaICT/4. FrontEnd_BackEnd` 출처 누락 0개, 자리표시자/할 일 표식 0개, index 미등록 0개, scoped 깨진 위키링크 0개, `needs-review`/`confidence: low` 0개였다. 단, 이는 구조 lint 결과이며 날짜별 summary와 기능 흐름 설명의 충분성까지 보장하는 표현으로 해석하지 않는다.
- `wiki/index.md`에서 일부 설명이 다음 항목에 붙어 보이던 줄을 분리했다. 특히 `JWT, 세션, 쿠키 인증`, `Axios interceptor와 API 오류 처리`, `상품 도메인 기능 흐름`, `JPA 연관관계 매핑`, `Entity vs DTO`, `JPQL vs SQL` 항목의 한 줄 설명을 정리했다.
- 본문 링크 기준 고립 후보였던 `[[summaries/2026-04-17-cart-total-array-some|2026-04-17 장바구니 합계와 Array some]]`, `[[summaries/2026-04-20-order-list-scenario|2026-04-20 주문 목록과 테스트 시나리오]]`, `[[summaries/2026-05-20-filingbox-giga-mega|2026-05-20 FilingBox GIGA/MEGA와 WORM 스토리지]]`를 관련 concept 본문에서 자연스럽게 연결했다.
- 당시 전체 수치 기록은 `wiki/` Markdown 243개, `index.md` Total pages 241개였고, 전역 frontmatter 누락, 빈 sources, 대표 자리표시자 문구, 깨진 위키링크, 저신뢰 후보도 0개로 집계되었다. 단, 이 역시 구조 점검 수치이며 내용 고도화 완료 선언으로 보지 않는다.


## 추가 정리: 4·5과목 현재 MD 기준 재검증 정정 및 재ingest

- 이전 2026-07-09 기록의 “전면 재ingest/모두 통과” 표현은 과했다. 구조 lint만으로 내용 품질 완료를 선언하지 않도록 정정했다.
- 이번 패스에서는 `raw/KoreaICT/4. FrontEnd_BackEnd` 날짜별 MD 18개와 `FrontEnd_BackEnd 총정리.md`를 기준으로 summary 18개와 subject-review 허브를 재작성/보강했다.
- 4과목 관련 concept/entity/comparison에는 Spring Boot ↔ React ↔ JWT ↔ Product/Cart/Order/Pageable 기능 흐름 기준의 재검증 메모를 추가했다.
- `raw/KoreaICT/5. Linux` 날짜별 MD 10개와 `Linux 총정리.md`를 기준으로 summary 10개와 subject-review 허브를 재작성/보강했다.
- 5과목 관련 concept/entity/comparison에는 VM/SSH/CLI ↔ 권한/파일 ↔ Spring Boot jar 실행 ↔ Docker/Compose ↔ GitHub 협업 흐름 기준의 재검증 메모를 추가했다.
- 이 섹션의 검증 결과는 “내용까지 완전 무결”이 아니라, 이번 패스에서 새로 발견한 high-risk 후보를 수정하고 구조·출처·링크 검사를 반복한 결과를 의미한다.
