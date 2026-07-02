---
title: Wiki Log Archive 2026-06
created: 2026-07-02
updated: 2026-07-02
type: meta
tags: [study-log]
sources:
  - wiki/log.md
status: stable
confidence: high
---
# Wiki Log Archive 2026-06

이 문서는 `wiki/log.md`가 길어져 분리한 2026-06 작업 로그 아카이브다. 원래 로그 항목의 내용을 보존한다.

## [2026-06-29] create | LLM 위키 기본 골격 생성

- 목적: 국비지원 웹서비스 풀스택 개발자 과정 학습 내용을 장기적으로 추적하고, 새 세션에서도 위키를 통해 맥락을 복원할 수 있게 하기 위함.
- 생성한 구조:
  - `raw/` — 사용자가 넣는 원본 자료 폴더. LLM은 읽기만 하고 수정하지 않음.
  - `raw/assets/` — 원본 자료에 딸린 이미지/첨부파일.
  - `wiki/` — LLM이 정리한 지식 베이스.
  - `wiki/summaries/` — 수업/자료 요약.
  - `wiki/concepts/` — 개념 정리.
  - `wiki/entities/` — 기술/도구/프레임워크 정리.
  - `wiki/comparisons/` — 비교 분석.
  - `wiki/queries/` — 보존 가치 있는 질문 답변.
  - `wiki/_meta/` — 운영 보조 문서와 점검 리포트.
- 생성한 파일:
  - `AGENTS.md` — 위키 운영 규칙과 사용자/목적/커리큘럼 맥락.
  - `wiki/index.md` — 전체 위키 목차 골격.
  - `wiki/log.md` — 작업 일지 골격.

## [2026-06-30] create | 집 노트북 Hermes/LLM Wiki 환경 복제 가이드

- 목적: 현재 컴퓨터의 Obsidian LLM Wiki와 Hermes Agent 설정, memory, skills, Desktop UI 설정을 집 노트북에서도 최대한 동일하게 복제할 수 있도록 절차를 문서화함.
- 생성한 파일:
  - `wiki/_meta/hermes-home-laptop-setup.md` — GitHub clone, AppData Hermes 설정 복사, `config.yaml`의 `cwd` 경로 수정, GitHub 인증, 확인 체크리스트를 정리한 가이드.
- 수정한 파일:
  - `wiki/index.md` — Meta 섹션에 새 가이드 문서를 등록하고 페이지 수/업데이트 날짜를 갱신함.

## [2026-06-30] update | 집 노트북 Hermes 인증 파일 제외 방식 반영

- 목적: 집 노트북에서 OpenAI OAuth를 새로 연결할 예정이므로, API 키/OAuth 토큰 파일을 복사하지 않는 더 안전한 이전 방식을 문서에 반영함.
- 수정한 파일:
  - `wiki/_meta/hermes-home-laptop-setup.md` — `.env`, `auth.json`은 복사하지 않고, `config.yaml`, `state.db`, `skills/`, `projects.db` 중심으로 옮기는 권장 절차와 체크리스트를 추가/수정함.

## [2026-06-30] ingest | raw 폴더 초기 자료 전체 정리

- 목적: `raw/`에 들어 있는 AI 지시문, LLM Wiki 운영 참고자료, Markdown 문법 자료를 `wiki/` 지식 레이어에 통합함.
- 읽은 원본:
  - `raw/ai-instructions/hermes-agent-llm-wiki-initial-setup.md`
  - `raw/ai-instructions/hermes-default-profile-instructions.md`
  - `raw/ai-instructions/karpathy-agent-guidelines.md`
  - `raw/ai-instructions/llm-wiki-command-cheatsheet.md`
  - `raw/markdown-grammar/markdown-grammar.md`
  - `raw/Study/1. Java/2026.02.26(목)/2026.02.26(목).md` — 파일이 비어 있어 별도 요약 페이지는 만들지 않음.
- 생성한 파일:
  - `wiki/_meta/llm-wiki-operating-model.md` — LLM Wiki의 raw/wiki/schema 구조와 이 Vault에서의 적용 방식 정리.
  - `wiki/_meta/llm-wiki-command-reference.md` — ingest/query/lint/update/compare/roadmap 등 LLM Wiki 작업 명령어 정리.
  - `wiki/_meta/hermes-default-profile-mode-system.md` — default 프로필 + safe/smart/danger 모드 운영 방식 정리.
  - `wiki/_meta/agent-coding-guidelines.md` — AI Agent 코딩 작업 원칙 요약.
  - `wiki/concepts/markdown-basic-syntax.md` — Markdown 기본 문법 정리.
- 수정한 파일:
  - `wiki/index.md` — 새 위키 페이지 5개를 등록하고 전체 페이지 수를 갱신함.

## [2026-06-30] update | 2026-02-26 OT raw 변경분 반영

- 목적: 이전 ingest 시 비어 있던 `raw/Study/1. Java/2026.02.26(목)/2026.02.26(목).md`에 내용이 추가되어, 교육 첫날 오리엔테이션 내용을 위키에 반영함.
- 생성한 파일:
  - `wiki/summaries/2026-02-26-orientation.md` — 교육 과정 정보, 출결/외출/휴가 규칙, 자습, Notepad++/Chrome/IntelliJ/Zoom 설치 준비 정리.
- 수정한 파일:
  - `wiki/index.md` — Summaries 섹션에 새 요약 페이지를 등록하고 전체 페이지 수를 갱신함.

## [2026-06-30] ingest | 2026-02-27 GitHub 초기 설정

- 목적: Java 프로젝트를 Git으로 관리하고 GitHub 원격 저장소 및 IntelliJ IDEA와 연결하는 초기 설정 흐름을 위키에 반영함.
- 읽은 원본:
  - `raw/Study/1. Java/2026.02.27(금)/깃허브 초기 설정.md`
  - `raw/Study/1. Java/2026.02.27(금)/2026.02.27(금).md` — 작업 중 Java 수업 본문이 추가되어, 아래 `2026-02-27 Java 기본 자료형과 연산자` 항목에서 별도 ingest함.
- 생성한 파일:
  - `wiki/summaries/2026-02-27-github-initial-setup.md` — Git 설치 경로, 프로젝트 폴더 이동, `git config`, GitHub 원격 저장소, IntelliJ 연동 흐름 정리.
  - `wiki/entities/git.md` — Git의 역할과 이 위키에서의 학습 맥락 정리.
  - `wiki/entities/github.md` — GitHub의 역할과 이 위키에서의 학습 맥락 정리.
- 수정한 파일:
  - `wiki/index.md` — 새 요약/엔티티 페이지 3개를 등록하고 전체 페이지 수를 갱신함.

## [2026-06-30] ingest | 2026-02-27 Java 기본 자료형과 연산자

- 목적: 2026-02-27 Java 수업 본문에 추가된 기본 자료형, 변수 선언, 산술/대입/복합 대입/증감 연산자, GitHub 원격 저장소 이슈 내용을 위키에 반영함.
- 읽은 원본:
  - `raw/Study/1. Java/2026.02.27(금)/2026.02.27(금).md`
  - `raw/Study/1. Java/2026.02.27(금)/깃허브 초기 설정.md`
- 생성한 파일:
  - `wiki/summaries/2026-02-27-java-basic-types-operators.md` — Java 자료형, 변수, 연산자 실습과 GitHub 관련 이슈를 수업 흐름대로 정리.
  - `wiki/concepts/java-basic-types.md` — `char`, `String`, `int`, `double`, `boolean`의 의미와 헷갈리는 점 정리.
  - `wiki/concepts/java-operators.md` — 산술/대입/복합 대입/증감 연산자의 의미와 실행 순서 정리.
  - `wiki/entities/java.md` — 이 위키에서 Java의 위치와 학습 이력 정리.
- 수정한 파일:
  - `wiki/index.md` — 새 요약/개념/엔티티 페이지 4개를 등록하고 전체 페이지 수를 갱신함.
  - `wiki/summaries/2026-02-27-github-initial-setup.md` — 같은 날짜 Java 수업 요약으로 연결되는 관련 링크를 추가함.

## [2026-06-30] note | Java raw MD 검토 재개 위치

- 목적: 다음 세션에서 사용자가 raw MD 변환 결과 검토를 이어갈 위치를 잊지 않도록 기록함.
- 현재 사용자가 확인한 위치:
  - `raw/Study/1. Java/2026.03.04(수)/2026.03.04(수).md` — 파일 중간 정도까지 검토함.
- 다음에 이어볼 위치:
  - `raw/Study/1. Java/2026.03.04(수)/2026.03.04(수).md`의 중간 이후부터 계속 검토.

## [2026-06-30] ingest | raw Study 수업 자료 대량 정리

- 목적: `raw/Study/`에 쌓여 있던 Java, Oracle, UI&UX 수업 자료 중 실내용이 있는 Markdown을 날짜순 위키 요약과 핵심 개념/엔티티 페이지로 통합함.
- 처리한 원본:
  - `raw/Study/1. Java/2026.03.03(화)/2026.03.03(화).md`
  - `raw/Study/1. Java/2026.03.04(수)/2026.03.04(수).md`
  - `raw/Study/1. Java/2026.03.05(목)/2026.03.05(목).md`
  - `raw/Study/1. Java/2026.03.06(금)/2026.03.06(금).md`
  - `raw/Study/1. Java/2026.03.09(월)/2026.03.09(월).md`
  - `raw/Study/1. Java/2026.03.10(화)/2026.03.10(화).md`
  - `raw/Study/1. Java/2026.03.11(수)/2026.03.11(수).md`
  - `raw/Study/1. Java/2026.03.12(목)/2026.03.12(목).md`
  - `raw/Study/1. Java/2026.03.13(금)/2026.03.13(금).md`
  - `raw/Study/2. Oracle/2026.03.13(금) - 시작/2026.03.13(금) - 시작.md`
  - `raw/Study/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
  - `raw/Study/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
  - `raw/Study/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
  - `raw/Study/2. Oracle/2026.03.19(목)/2026.03.19(목).md`
  - `raw/Study/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
  - `raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md`
  - `raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md`
  - `raw/Study/3. UI&UX/2026.03.25(수)/2026.03.25(수).md`
  - `raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md`
  - `raw/Study/3. UI&UX/2026.03.27(금)/2026.03.27(금).md`
- 제외/보류한 원본:
  - `raw/Study/0. 교육명/**`, `raw/Study/4. FrontEnd_BackEnd/**`, `raw/Study/5. Linux/**`, `raw/Study/6. AWS/**`, `raw/Study/7. Ci&CD/**`, `raw/Study/8. Passwordless/**`, `raw/Study/10. Python/**` 중 현재 30줄/174자 수준의 시간표 템플릿 파일은 실내용이 없어 요약 페이지를 만들지 않음.
- 생성한 파일:
  - `wiki/summaries/2026-03-03-java-logic-ternary.md`
  - `wiki/summaries/2026-03-04-java-control-flow.md`
  - `wiki/summaries/2026-03-05-java-for-while.md`
  - `wiki/summaries/2026-03-06-java-while-array.md`
  - `wiki/summaries/2026-03-09-java-class-object.md`
  - `wiki/summaries/2026-03-10-java-constructor-overloading-inheritance.md`
  - `wiki/summaries/2026-03-11-java-inheritance-polymorphism.md`
  - `wiki/summaries/2026-03-12-java-abstract-interface-static.md`
  - `wiki/summaries/2026-03-13-java-project-oracle-start.md`
  - `wiki/summaries/2026-03-16-oracle-dbms-sql-dbeaver.md`
  - `wiki/summaries/2026-03-17-oracle-ddl-dml-constraints-sequence.md`
  - `wiki/summaries/2026-03-18-oracle-constraints-validation.md`
  - `wiki/summaries/2026-03-19-oracle-functions-join-subquery.md`
  - `wiki/summaries/2026-03-20-database-modeling-normalization-view-index.md`
  - `wiki/summaries/2026-03-23-html-css-intro.md`
  - `wiki/summaries/2026-03-24-css-layout-javascript-intro.md`
  - `wiki/summaries/2026-03-25-bootstrap-form.md`
  - `wiki/summaries/2026-03-26-javascript-dom-product-pages.md`
  - `wiki/summaries/2026-03-27-jquery-ui-interaction.md`
  - `wiki/concepts/java-conditional-logic.md`
  - `wiki/concepts/java-loop.md`
  - `wiki/concepts/java-array.md`
  - `wiki/concepts/java-class-object.md`
  - `wiki/concepts/java-inheritance.md`
  - `wiki/concepts/java-abstract-interface.md`
  - `wiki/concepts/oracle-sql-basics.md`
  - `wiki/concepts/oracle-constraints-sequence.md`
  - `wiki/concepts/oracle-functions-join-subquery.md`
  - `wiki/concepts/database-modeling-normalization.md`
  - `wiki/concepts/html-css-basics.md`
  - `wiki/concepts/javascript-dom.md`
  - `wiki/concepts/bootstrap-basics.md`
  - `wiki/concepts/jquery-basics.md`
  - `wiki/entities/oracle-database.md`
  - `wiki/entities/dbeaver.md`
  - `wiki/entities/html.md`
  - `wiki/entities/css.md`
  - `wiki/entities/javascript.md`
  - `wiki/entities/bootstrap.md`
  - `wiki/entities/jquery.md`
- 수정한 파일:
  - `wiki/index.md` — 새 요약/개념/엔티티 페이지를 등록하고 전체 페이지 수를 54개로 갱신함.
  - `wiki/log.md` — 이번 ingest 기록을 추가함.
  - `wiki/entities/java.md` — 2026-03-03~2026-03-12 Java 학습 이력 링크를 추가함.
- 비고: 대량 정리이므로 각 페이지는 `status: growing` 초안으로 두었고, 원본의 `추가 공부`, `중요`, 질문 표시가 있는 부분은 추후 보강 대상으로 남김.
