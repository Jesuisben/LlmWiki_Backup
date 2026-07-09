---
title: Wiki Log Archive 2026-07-02 Part 1
created: 2026-07-02
updated: 2026-07-02
type: meta
tags: [study-log]
sources:
  - wiki/log.md
status: stable
confidence: high
---
# Wiki Log Archive 2026-07-02 Part 1

이 문서는 2026-07-02 작업 로그가 길어져 분리한 Part 1 아카이브다. 원래 로그 항목의 내용을 보존한다.

## [2026-07-02] audit/update | LLM Wiki 품질 감사와 핵심 페이지 1차 고도화

- 목적: 기존 `wiki/`가 Karpathy식 LLM Wiki의 목적에 맞게 고품질 지식 레이어로 작동하는지 점검하고, 앞으로의 ingest 기준을 높이기 위함.
- 생성한 파일:
  - `wiki/_meta/wiki-quality-audit-2026-07-02.md` — 얕은 페이지, 빈 출처, 반복 placeholder 문구, 비교/질문 페이지 후보, 재ingest 후보, 고품질 ingest 기준을 정리한 감사 리포트.
- 수정한 파일:
  - `AGENTS.md` — `6.0 고품질 ingest 기준`을 추가해 앞으로 summary/concept/entity/comparison/query 페이지 작성 기준을 강화함.
  - `wiki/index.md` — 감사 리포트를 Meta 섹션에 등록하고 `다다` 오타를 수정함.
  - `wiki/concepts/oracle-functions-join-subquery.md` — Oracle 함수, `GROUP BY`/`HAVING`, JOIN, 서브쿼리, 단일행/다중행 서브쿼리를 원본 예제 중심으로 고도화함.
  - `wiki/concepts/java-class-object.md` — 클래스/객체, 멤버 변수, 메서드, 생성자, `this`, 오버로딩, 객체 배열을 원본 수업 흐름 중심으로 고도화함.
  - `wiki/concepts/spring-data-jpa-repository.md` — `Specification`, `Pageable`, `Page`, Controller/Service/Repository 흐름과 검색 테스트 시나리오를 원본 예제 중심으로 고도화함.
- 비고: 이번 작업은 템플릿을 바꾸는 것이 아니라, 기존 템플릿 안에서 내용 품질 기준을 높이고 핵심 concept 페이지 3개를 품질 기준 예시로 재작성한 것이다.

## [2026-07-02] create | 핵심 혼동 비교 페이지 4개 생성

- 목적: 기존 concept 고도화 중 실제로 자주 헷갈릴 만한 차이를 `wiki/comparisons/`에 보존해, 이후 질문/복습 시 바로 참조할 수 있게 하기 위함.
- 생성한 파일:
  - `wiki/comparisons/where-vs-having.md` — `WHERE`와 `HAVING`의 적용 시점과 사용 기준 비교.
  - `wiki/comparisons/single-row-vs-multi-row-subquery.md` — 단일행/다중행/다중컬럼 서브쿼리 구분과 연산자 선택 기준 비교.
  - `wiki/comparisons/controller-service-repository.md` — Spring Boot의 Controller, Service, Repository 역할 차이 비교.
  - `wiki/comparisons/entity-vs-dto.md` — Entity와 DTO의 목적, 사용 위치, 헷갈리는 점 비교.
- 수정한 파일:
  - `wiki/index.md` — Comparisons 섹션에 새 비교 페이지 4개를 등록하고 전체 페이지 수를 갱신함.

## [2026-07-02] update/create | Java 객체지향과 Oracle DB 핵심 concept 2차 고도화

- 목적: 품질 감사에서 우선순위가 높게 나온 얕은 concept 페이지들을 원본 수업 예제 중심으로 재작성하고, 반복 placeholder 문구와 빈 출처 문제를 줄이기 위함.
- 수정한 파일:
  - `wiki/concepts/java-inheritance.md` — `extends`, 일반화, `private` 접근, `super`, 업캐스팅/다운캐스팅, `instanceof`, `toString()` 오버라이딩을 음료 예제 중심으로 고도화함.
  - `wiki/concepts/java-abstract-interface.md` — 추상 메서드, 추상 클래스, 인터페이스, `implements`, 다중 인터페이스, `static/final`을 카페 예제 중심으로 고도화함.
  - `wiki/concepts/oracle-sql-basics.md` — DBMS, DBeaver 연결, SQL 분류, 테이블/행/열, `CREATE TABLE`, `INSERT`, `SELECT`, `COMMIT`/`ROLLBACK`을 원본 수업 흐름 중심으로 고도화함.
  - `wiki/concepts/oracle-constraints-sequence.md` — 시퀀스, PK/FK/CHECK, 참조 무결성, `ON DELETE` 옵션, 데이터 사전을 원본 오류/테스트 예제 중심으로 고도화함.
  - `wiki/concepts/database-modeling-normalization.md` — ERD, 이상 현상, 함수 종속성, 정규화, 참조 무결성, View, Index를 원본 수업 흐름 중심으로 고도화함.
- 생성한 파일:
  - `wiki/comparisons/interface-vs-abstract-class.md` — Java 추상 클래스와 인터페이스의 목적, 문법, 사용 기준 비교.
- 수정한 파일:
  - `wiki/index.md` — 새 비교 페이지를 Comparisons 섹션에 등록하고 전체 페이지 수를 갱신함.

## [2026-07-02] update | Java 제어문·배열과 UI&UX 핵심 concept 3차 고도화

- 목적: 품질 감사의 다음 우선순위였던 Java 배열/반복문/조건 판단 및 HTML/CSS/JavaScript/Bootstrap/jQuery concept 페이지를 원본 수업 노트의 실제 예제와 헷갈림 중심으로 재작성함.
- 다시 읽은 원본:
  - `raw/KoreaICT/1. Java/2026.03.03(화)/2026.03.03(화).md`
  - `raw/KoreaICT/1. Java/2026.03.04(수)/2026.03.04(수).md`
  - `raw/KoreaICT/1. Java/2026.03.05(목)/2026.03.05(목).md`
  - `raw/KoreaICT/1. Java/2026.03.06(금)/2026.03.06(금).md`
  - `raw/KoreaICT/1. Java/2026.03.12(목)/2026.03.12(목).md`
  - `raw/KoreaICT/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md`
  - `raw/KoreaICT/3. UI&UX/2026.03.24(화)/2026.03.24(화).md`
  - `raw/KoreaICT/3. UI&UX/2026.03.25(수)/2026.03.25(수).md`
  - `raw/KoreaICT/3. UI&UX/2026.03.26(목)/2026.03.26(목).md`
  - `raw/KoreaICT/3. UI&UX/2026.03.27(금)/2026.03.27(금).md`
- 수정한 파일:
  - `wiki/concepts/java-conditional-logic.md` — 비교/논리 연산자, 삼항 연산자, `if/else`, `switch`, `break` 흐름을 계절·학점·홀짝 예제 중심으로 고도화함.
  - `wiki/concepts/java-loop.md` — `for`, `while`, 무한 반복, `break`, 배열 반복, 향상된 for를 합계·입력·객체 배열 예제 중심으로 고도화함.
  - `wiki/concepts/java-array.md` — 배열 인덱스, `new` 방식, 초기화 기법, `length`, 입력값 배열 처리, 객체 배열 연결을 원본 예제 중심으로 고도화함.
  - `wiki/concepts/html-css-basics.md` — HTML 태그/속성/엔티티/표/이미지와 CSS 선택자/박스 모델/position/display를 UI&UX 수업 흐름으로 고도화함.
  - `wiki/concepts/bootstrap-basics.md` — CDN, 반응형, grid, form/button, Bootstrap class 사용을 장바구니·상품 등록 화면 예제 중심으로 고도화함.
  - `wiki/concepts/javascript-dom.md` — `document`, `innerHTML`, `undefined`, `===`, 객체/배열, `forEach`, `createElement`, 이벤트, URL 파라미터를 상품 페이지 예제로 고도화함.
  - `wiki/concepts/jquery-basics.md` — `$()` 선택자, ready, `click`/`change`, `toggleClass`, `addClass`/`removeClass`, `show`/`hide`, `attr`, method chaining을 이미지 UI 실습 중심으로 고도화함.
  - `wiki/index.md` — 고도화된 7개 concept의 한 줄 설명을 실제 학습 맥락 중심으로 갱신함.

## [2026-07-02] update/create | 잔여 핵심 entities와 FrontEnd_BackEnd concept 고도화

- 목적: 품질 감사 이후 남아 있던 `entities/` 핵심 페이지와 FrontEnd_BackEnd 프로젝트 흐름 concept 초안을 원본 수업 흐름, 실제 기능 구현, 헷갈림 포인트 중심으로 고도화함.
- 수정한 entity 페이지: `oracle-database`, `dbeaver`, `html`, `css`, `javascript`, `bootstrap`, `jquery`, `spring-boot`, `react`, `typescript`, `jwt`.
- 수정한 concept 페이지: `fullstack-project-flow`, `spring-boot-rest-api`, `react-typescript-basics`, `jwt-session-cookie-auth`, `dto-entity-service-controller`, `shopping-cart-flow`, `order-flow`, `pagination-search`.
- 생성/보강한 comparison 페이지: `session-vs-cookie-vs-jwt`, `react-router-vs-spring-api-url`, `primitive-vs-reference-types`.
- 수정한 파일: `wiki/index.md`, `wiki/log.md`.
- 비고: `raw/`는 읽기 전용으로 유지했고, 각 페이지의 `sources`를 구체 raw 경로로 정리함.

## [2026-07-02] update/create | Python Pandas 요약·개념·엔티티 고도화

- 목적: Python/Pandas 쪽 잔여 얕은 페이지와 2026-07-02 신규 raw를 고품질 ingest 기준에 맞게 보강함.
- 다시 읽은 원본:
  - `raw/KoreaICT/10. Python/2026.07.01(수)/2026.07.01(수).md`
  - `raw/KoreaICT/10. Python/2026.07.02(목)/2026.07.02(목).md`
- 생성한 파일:
  - `wiki/summaries/2026-07-02-python-pandas-reshape-merge.md` — `concat`, `merge`, `pivot`, SQL JOIN과의 연결을 중심으로 2026-07-02 Pandas 수업을 요약함.
- 수정한 파일:
  - `wiki/summaries/2026-07-01-python-pandas-dataframe.md` — 기존 Spring/React placeholder 내용을 제거하고 DataFrame 조회, `loc`/`iloc`, CSV 입출력, Series 통계, 그래프 흐름으로 재작성함.
  - `wiki/concepts/pandas-dataframe-basics.md` — DataFrame/Series, `loc`/`iloc`, 조건 수정, `reindex`, `drop`, CSV, `concat`/`merge`/`pivot`까지 원본 수업 예제 중심으로 고도화함.
  - `wiki/entities/python.md` — 이 위키에서 Python이 데이터 처리 과정으로 등장한 맥락과 날짜별 학습 이력을 정리함.
  - `wiki/entities/pandas.md` — Pandas의 DataFrame/Series, 입출력, 통계, 결합·재구조화 역할을 수업 흐름 중심으로 정리함.
  - `wiki/entities/jupyter-notebook.md` — Jupyter Notebook을 Pandas 셀 실행·표/그래프 확인 학습 환경으로 정리함.
  - `wiki/index.md` — 새 2026-07-02 요약 페이지를 등록하고 Python/Pandas 관련 한 줄 설명과 전체 페이지 수를 갱신함.

## [2026-07-02] ingest/update | Linux, Docker, GitHub 협업 raw 고도화

- 목적: 품질 감사에서 남은 재ingest 후보였던 Linux 과정 원본을 고품질 기준에 맞춰 날짜별 요약, 핵심 개념, 엔티티 페이지로 통합함.
- 다시 읽은 원본:
  - `raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md`
  - `raw/KoreaICT/5. Linux/2026.04.23(목)/2026.04.23(목).md`
  - `raw/KoreaICT/5. Linux/2026.04.24(금)/2026.04.24(금).md`
  - `raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md`
  - `raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md`
  - `raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md`
  - `raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md`
  - `raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md`
  - `raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md`
  - `raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md`
- 생성한 summary 페이지:
  - `wiki/summaries/2026-04-22-linux-install-ssh-cli.md`
  - `wiki/summaries/2026-04-23-linux-files-vi.md`
  - `wiki/summaries/2026-04-24-linux-users-permissions.md`
  - `wiki/summaries/2026-04-27-linux-archive-java-alias.md`
  - `wiki/summaries/2026-04-28-maven-spring-boot-docker-intro.md`
  - `wiki/summaries/2026-04-29-docker-network-volume-image.md`
  - `wiki/summaries/2026-04-30-dockerfile-spring-load-balancing.md`
  - `wiki/summaries/2026-05-01-docker-compose.md`
  - `wiki/summaries/2026-05-04-git-github-sourcetree.md`
  - `wiki/summaries/2026-05-06-github-branch-pr-conflict.md`
- 생성한 concept 페이지:
  - `wiki/concepts/linux-cli-files.md`
  - `wiki/concepts/linux-users-permissions.md`
  - `wiki/concepts/linux-package-archive.md`
  - `wiki/concepts/linux-spring-boot-server-deploy.md`
  - `wiki/concepts/docker-image-container.md`
  - `wiki/concepts/docker-network-volume.md`
  - `wiki/concepts/dockerfile-vs-compose.md`
  - `wiki/concepts/git-github-collaboration.md`
- 생성한 entity 페이지:
  - `wiki/entities/linux.md`
  - `wiki/entities/docker.md`
  - `wiki/entities/maven.md`
  - `wiki/entities/source-tree.md`
- 수정한 파일:
  - `wiki/index.md` — 새 summary/concept/entity 22개를 등록하고 전체 페이지 수를 123개로 갱신함.
  - `wiki/log.md` — 이번 Linux/Docker/GitHub 협업 고도화 기록을 추가함.
  - `wiki/_meta/wiki-quality-audit-2026-07-02.md` — 재ingest 후보 목록을 Linux/Python 처리 완료와 Java 총정리/숙제 남은 후보로 최신화함.
- 비고: `raw/`는 읽기 전용으로 유지했고, Java 총정리/숙제 raw는 다음 고도화 후보로 남겨 둠.
