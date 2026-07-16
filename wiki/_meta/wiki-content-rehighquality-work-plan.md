---
title: LLM Wiki 내용 재고도화 작업 계획
created: 2026-07-15
updated: 2026-07-15
type: meta
tags: [curriculum, study-log]
sources:
  - AGENTS.md
  - wiki/index.md
  - wiki/log.md
  - wiki/_meta/wiki-quality-audit-2026-07-02.md
status: growing
confidence: high
---

# LLM Wiki 내용 재고도화 작업 계획

## 목적

현재 wiki의 출처·frontmatter·index·위키링크 정합성은 유지하면서, 각 페이지를 사용자가 직접 다시 읽어 공부할 수 있고 Agent도 과거 학습 맥락을 정확히 복원할 수 있는 내용 중심 지식 베이스로 재고도화한다.

이 작업은 페이지 수를 늘리거나 구조 lint를 반복하는 작업이 아니다. 기존 페이지를 현재 `raw/KoreaICT/` 원본과 다시 대조하여 실제 수업 흐름, 구체 실습, 코드·명령·데이터 흐름, 헷갈리는 이유, 이전·다음 학습 연결을 복원하는 작업이다.

## 현재 기준선

- 구조 정합성은 `wiki/_meta/wiki-quality-audit-2026-07-02.md`의 최신 수치를 기준으로 한다.
- 구조 lint 통과는 내용 품질 완료의 근거가 아니다.
- 짧은 페이지가 곧 나쁜 페이지인 것은 아니지만, frontmatter·출처·링크만 갖춘 얕은 요약은 재고도화 완료로 보지 않는다.
- 사용자가 읽었을 때 수업 내용을 다시 이해하기 어렵다면 Agent 검색용으로도 충분히 고도화된 페이지가 아니다.
- `wiki/queries/`는 실제 보존 가치가 있는 사용자 질문이나 여러 페이지를 종합한 답변이 있을 때만 만든다. 빈 공간을 채우기 위해 질문을 만들어내지 않는다.

## 세션 운영 원칙

1. **한 단계는 과목 1개다.** 과목 하나의 감사 → 수정 → 검증을 새 세션 하나에서 완결한다.
2. 한 세션에서는 계획에 적힌 과목 하나만 처리한다. 다음 과목을 자동으로 시작하지 않는다.
3. 새 세션 첫 줄은 `smart 모드로 진행한다.`로 시작한다. 현재 프로젝트 내부의 `wiki/` 수정과 검증은 자율 수행하되, `raw/`는 읽기 전용으로 유지한다.
4. 세션 시작 시 `AGENTS.md`, `wiki/index.md`, 최근 `wiki/log.md`, 이 계획 문서, 대상 과목의 기존 wiki 페이지와 현재 raw MD를 읽는다.
5. 수정 전에 대상 과목의 페이지 목록과 raw 출처 대응표를 만든다. 기존 페이지를 우선 고도화하고, 중복 페이지를 만들지 않는다.
6. 과목 내부에서 summary → concept → entity → comparison → query 후보 순으로 검토하되, 실제 수정은 상호 연결이 깨지지 않도록 함께 수행한다.
7. 세션이 정상 완료되면 이 문서의 완료 기록과 `wiki/log.md`를 갱신한다. 새 페이지 또는 index 설명 변경이 있으면 `wiki/index.md`도 갱신한다.
8. 완료 보고 마지막에는 **바로 다음 미완료 단계 하나만** 시작하는 새 세션 복붙 프롬프트를 반드시 제공한다.
9. 검증 실패나 토큰 부족으로 과목이 끝나지 않았으면 다음 과목으로 넘기지 않는다. 같은 과목의 미완료 범위·실패 게이트·재개 지점을 담은 이어서 작업 프롬프트를 제공한다.
10. Git commit·push는 사용자가 별도로 요청하지 않는 한 수행하지 않는다.

## 과목별 실행 순서

커리큘럼의 선행·후행 연결을 보존하기 위해 아래 순서를 고정한다.

1. **Java** — 문법 → 제어문 → 배열 → 클래스/객체 → 생성자 → 상속/다형성 → 추상화 → `static/final`
2. **Oracle** — DBMS/SQL → DDL/DML/트랜잭션 → 제약조건/시퀀스 → 함수/JOIN/서브쿼리 → 모델링/정규화
3. **UI&UX** — HTML/CSS → JavaScript/DOM → Bootstrap/Form → 상품 페이지 → jQuery 상호작용
4. **FrontEnd_BackEnd** — 환경 구성 → Spring/React 연결 → Member/JWT → Product → Cart → Order → Pageable/검색
5. **Linux** — VM/SSH/CLI → 파일/권한 → 서버 실행 → Docker/Compose → GitHub 협업
6. **AWS** — Cloud/VPC → EC2/네트워크 → Nginx/Spring Boot → RDS → 자원 생명주기·비용
7. **Ci&CD** — GitHub Actions/Maven CI → Docker image → EC2 CD → Route 53/ACM/ALB → Terraform/S3
8. **Passwordless** — 인증 배경 → X1280 → Docker 연동 서버 → Spring 샘플 → AAM/APE → FilingBox/WORM → REST API
9. **중간 프로젝트 공부** — CI/CD·배포·Passwordless 적용을 실제 프로젝트 설계와 연결하되, 수업 직접 구현과 확장 설계를 구분
10. **Python** — 기본 문법 → 컬렉션/함수/OOP → 파일/정규표현식/XML/JSON → Pandas → API/크롤링/지도 → 텍스트 마이닝
11. **전체 통합 품질 검증** — 모든 과목 완료 뒤에만 수행한다. 중복·모순·교차 과목 연결·전체 내용 품질을 확인하고 잔여 오류를 고정점으로 보정한다.

## 페이지 유형별 내용 완료 기준

### Summary

- 해당 날짜/단원의 raw 원본 전체 흐름을 실제로 대조한다.
- 그날 무엇을 배웠는지뿐 아니라 왜 그 순서로 배웠는지 설명한다.
- 이전 수업과 다음 수업의 구체 연결을 적는다.
- 원본에 코드·SQL·명령·설정·데이터 흐름이 있으면 대표 실습을 최소 1개 이상 구체적으로 복원한다.
- 단순 주제 나열 대신 입력 → 처리 → 결과 또는 실행 순서를 설명한다.
- `헷갈린 점 / 질문`에는 실제 혼동 원인과 구분 기준을 적는다. 억지 질문은 만들지 않는다.
- 원본 자체가 빈 시간표나 개요라 구체화할 근거가 없으면 그 사실을 명시하고 인접 자료와 섞어 추정하지 않는다.

### Concept

- 사전식 정의보다 이 수업에서 언제·왜 등장했는지를 중심에 둔다.
- 초보자가 이해할 수 있는 단계적 설명과 정확한 개발 용어를 함께 쓴다.
- 실제 수업 코드·SQL·명령·프로젝트 상황 중 최소 하나를 예시로 든다.
- 잘못 이해하기 쉬운 방식과 올바른 판단 기준을 함께 설명한다.
- 선행 개념, 후속 수업, 관련 summary를 자연스럽게 연결한다.

### Entity

- 기술의 정의만 적지 않고 이 위키에서의 첫 등장과 날짜별 학습 이력을 정리한다.
- 어떤 실습·기능·프로젝트에서 역할이 커졌는지 설명한다.
- 관련 concept/comparison/summary를 연결한다.
- 사용자가 프로젝트나 면접에서 설명할 수 있는 관점을 실제 학습 근거에 맞춰 적는다.

### Comparison

- 표의 항목을 실제 선택 기준이 드러나도록 구성한다.
- `언제 무엇을 쓰는가`에 최소 2개의 구체 상황을 둔다.
- 단순 차이뿐 아니라 함께 사용할 수 있는 관계와 흔한 오해를 설명한다.
- 관련 수업 예제 또는 코드/쿼리/요청 흐름에 연결한다.

### Query

- 실제 사용자 질문, 반복 혼동, 여러 페이지를 종합한 답변만 보존한다.
- 질문을 임의로 만들어 페이지 수를 늘리지 않는다.
- 짧은 답과 자세한 설명, 참고한 wiki/raw, 다음 복습 경로를 포함한다.

## 금지되는 얕은 고도화 패턴

- frontmatter·sources·링크만 보강하고 내용 고도화 완료라고 보고하기
- `현재 raw 기준으로 재검증했다`는 메모만 추가하기
- index 항목 수·페이지 수·줄 수만 품질 근거로 사용하기
- raw 제목이나 키워드를 문장으로 바꿔 나열하기
- 구체 예제 대신 `관련 페이지를 참고한다`, `추후 보강한다`로 끝내기
- 원본에 없는 코드·실습 결과·사용자의 혼동을 만들어내기
- `confidence: high`를 출처가 존재한다는 이유만으로 유지하기
- 기존 사용자/Agent 변경을 확인하지 않고 과목 전체를 일괄 덮어쓰기

## 과목별 세션 절차

### 1. 시작 상태 확인

- `AGENTS.md`, `wiki/index.md`, `wiki/log.md`, 이 계획 문서를 읽는다.
- `git status --short --branch`와 대상 wiki diff를 읽어 기존 변경을 구분한다.
- 완료 기록에서 바로 다음 미완료 과목인지 확인한다.
- 대상 `raw/KoreaICT/<과목>/`의 현재 MD와 교육자료 범위를 확인한다.

### 2. 내용 품질 감사

- frontmatter sources와 실제 raw 경로를 대응시킨다.
- 대상 과목과 직접 관련된 summary/concept/entity/comparison/query 페이지를 전수 목록화한다.
- 각 페이지를 `유지`, `부분 보강`, `전면 재작성`, `통합 후보`, `신규 필요`, `근거 부족`으로 분류한다.
- summary의 날짜별 흐름, concept의 수업 예제, entity의 학습 이력, comparison의 선택 기준 누락을 검사한다.
- 감사 결과만 보고하고 세션을 끝내지 말고 같은 세션에서 수정으로 이어간다.

### 3. 수정

- 현재 raw를 근거로 기존 페이지를 우선 고도화한다.
- 페이지 간 중복 설명은 각 페이지 역할에 맞게 정리하고 위키링크로 연결한다.
- 중요한 주장·예제는 구체 raw 출처 또는 provenance marker로 추적 가능하게 한다.
- 원본의 민감값·개인 경로·운영 endpoint는 재노출하지 않고 역할 중심으로 일반화한다.
- 새 페이지가 필요하면 `wiki/index.md`에 등록하고 Total pages를 실제 수치로 갱신한다.

### 4. 검증

다음 항목을 모두 실제로 검사한다.

- 대상 과목 관련 페이지 전수 처리 여부와 미분류 페이지 0개
- summary별 이전/다음 흐름, 구체 실습, 헷갈림 내용
- concept별 수업 근거 예시, 중요성, 선행/후속 연결
- entity별 첫 등장·학습 이력·구현 역할
- comparison별 표·선택 상황·흔한 오해·관련 수업
- frontmatter, sources 실제 존재, 허용 태그, 깨진/모호한 위키링크
- 신규/변경 페이지의 index 등록과 한 줄 설명
- placeholder·근거 없는 단정·일괄 재검증 메모 잔존
- 현재 작업이 만든 고립 페이지
- `raw/`를 Agent 도구가 수정하지 않았는지 구분
- 대상 `wiki/` 범위의 scoped `git diff --check`
- 시작·중간·끝의 대표 고위험 페이지를 raw와 직접 재대조

새로운 실제 오류나 내용 공백이 발견되면 수정 후 위 전체 검증을 다시 실행한다. 미분류 후보나 실패 게이트가 남아 있으면 완료로 기록하지 않는다.

### 5. 기록과 인계

- 이 문서의 과목별 완료 기록에 한 행을 append한다.
- `wiki/log.md`에 실제 수정 범위·내용 검증·남은 제한을 기록한다.
- 새 페이지가 있거나 설명이 바뀌었으면 `wiki/index.md`를 갱신한다.
- 완료 보고에는 변경 파일, 핵심 고도화, 실제 검증 결과, raw 비수정, 다음 과목 자동 미실행을 포함한다.
- 보고 마지막에 다음 단계용 복붙 프롬프트를 제공한다.

## 완료 판정 게이트

한 과목은 아래 조건을 모두 만족해야 완료다.

1. 관련 기존 페이지와 현재 raw 출처의 대응을 전수 확인했다.
2. 얕은 페이지를 실제 수업 맥락·실습·혼동·연결 중심으로 보강했다.
3. 새 페이지는 반복 학습 가치가 있는 경우에만 만들었다.
4. 구조 lint뿐 아니라 대표 raw 대조와 페이지 유형별 내용 검증을 수행했다.
5. 검증 실패·미분류 후보·근거 없는 `confidence: high`가 남지 않았다.
6. index/log/이 계획의 완료 기록을 현재 상태와 일치시켰다.
7. `raw/`는 Agent 도구가 수정하지 않았다.
8. 다음 과목을 자동 실행하지 않았다.
9. 다음 세션용 복붙 프롬프트를 완료 보고 마지막에 제공했다.

## 과목별 완료 기록 (append-only)

| 완료일 | 단계 | 대상 과목 | 주요 변경 | 내용 검증 | 구조 검증 | 상태 / 다음 단계 |
|---|---:|---|---|---|---|---|
| 2026-07-15 | 1 | Java | 기존 34개 전수 수정·고도화, 숙제 summary와 캡슐화 concept 2개 신설, 비근거 인터페이스·날짜 귀속·원천 불일치 교정 | 직접 감사와 병렬 3계통 감사를 교차 검토하고 시작·중간·끝·총정리·숙제 재대조 | frontmatter·source·태그·링크·index·고립·diff 검증 통과 | 완료 / 다음은 2. Oracle |
| 2026-07-15 | 2 | Oracle | 기존 28개 전수 고도화, 신규/query 0개, 함수 종속성 PK/FK 오해·합성 SQL·Oracle 직접/JPA 후속 경계 교정 | raw 24/24 대응, SQL 56/56 원문 검증, 시작·중간·끝·총정리 고위험 직접 대조 | 전체 261페이지의 frontmatter·source·태그·링크·index와 scoped diff 검증 통과 | 완료 / 다음은 3. UI&UX |
| 2026-07-15 | 2 보강 | Oracle 비동기 감사 반영 | 병렬 summary·concept·entity/comparison 감사 3계통을 완료본과 재대조해 기존 28개를 추가 보정하고 `oracle-data-dictionary-schema-objects` concept 1개 신설 | raw 24/24, Oracle 지식 페이지 29개, SQL 61/61, 03-16 후반·03-18 source 불일치·03-19 RTRIM·03-20 1NF~3NF/View·03-30 MySQL 경계 고정점 통과 | 전체 262페이지·source 904건·위키링크 2,028건, frontmatter·source·태그·링크·index·diff 오류 0 | 최종 완료 / 다음은 3. UI&UX |
| 2026-07-15 | 3 | UI&UX | 기존 21개 전수 부분 보강, 신규/query 0개, `<alt>`·POST 보안·축약/합성 코드·직접 구현/후속 React·Spring 경계 교정 | raw 96/96 재고·대응표 21행, HTML/CSS/JavaScript fence 37/37 원문 연속 코드 대조, summary/concept/entity/comparison 내용 게이트 통과 | 전체 262페이지·source 908건·위키링크 2,031건, frontmatter·source·태그·링크·index·diff 오류 0, UI&UX raw status/diff 0 | 완료 / 다음은 4. FrontEnd_BackEnd |
| 2026-07-15 | 3 보강 | UI&UX 비동기 감사 반영 | 병렬 summary·concept·entity/comparison 감사 3계통을 완료본과 재대조해 기존 21개를 추가 보정하고 `html-form-controls-submission`, `ui-vs-ux`, `custom-css-vs-bootstrap` 3개 신설 | raw 96/96, UI&UX 지식 페이지 24개, HTML/CSS/JavaScript fence 39/39, 날짜 노트/교육 artifact 버전 차이와 직접 UI&UX/후속 React·Spring 경계 고정점 통과 | 전체 265페이지·source 974건·위키링크 1,801건, frontmatter·source·태그·링크·index·diff 오류 0, UI&UX raw status/diff 0 | 최종 완료 / 다음은 4. FrontEnd_BackEnd |
| 2026-07-16 | 4 | FrontEnd_BackEnd | 세션 2~15에서 기존 지식 페이지를 고도화하고 Query 2개를 신설한 뒤 세션 16에서 59개 전체 고정점 QA, JPQL/SQL fence 2개 원문 교정, 신규 Query·Comparison 역링크 보강 | R01~R19 19/19·22,838행, P01~P10 10/10 텍스트 추출, I01~I05 5/5 실제 artifact 대응; JWT/인가·Cart/Order·검색 실행 미확정·후속 과목 경계 재검증 | 59개 frontmatter·source·태그·링크·index·고립·placeholder 오류 0, code fence 2/2 원문 일치, Total pages 269 유지 | 최종 완료 / 단계 5 Linux는 시작하지 않음 |

## 단계 1 Java 완료 상세

### raw 출처 식별자

- `R01` `raw/KoreaICT/1. Java/2026.02.26(목) - 시작/2026.02.26(목) - 시작.md`
- `R02` `raw/KoreaICT/1. Java/2026.02.27(금)/2026.02.27(금).md`
- `R03` `raw/KoreaICT/1. Java/2026.02.27(금)/깃허브 초기 설정.md`
- `R04`~`R12` `raw/KoreaICT/1. Java/2026.03.03(화)`부터 `2026.03.13(금)`까지의 날짜별 MD
- `R13` `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
- `R14` `raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md`
- `E01` Java 이론 교안, `E02` IntelliJ 교안, `E03` GitHub 실습 교안
- `I01` 2026-02-27 문제 이미지 3개, `I02` 2026-03-03 연산자 문제/답 이미지

`R04`~`R12`의 날짜 대응은 순서대로 03-03, 03-04, 03-05, 03-06, 03-09, 03-10, 03-11, 03-12, 03-13이다.

### 기존 페이지 ↔ raw 대응 및 분류

| 유형 | wiki 페이지 | 주 대응 출처 | 분류 | 감사·처리 결과 |
|---|---|---|---|---|
| summary | `2026-02-26-orientation` | R01, E01, E02 | 부분 보강 | 변수 읽기/쓰기·문자/문자열·Git 지원 트랙까지 첫날 후반 흐름을 복원함 |
| summary | `2026-02-27-java-basic-types-operators` | R02, I01, E01 | 부분 보강 | 전위/후위 증감의 실제 값 변화와 복합 대입 읽기/쓰기를 보강함 |
| summary | `2026-02-27-github-initial-setup` | R01~R03, E02, E03 | 전면 재작성 | init→stage→commit→remote→push→clone과 위험 명령 경계를 복원함 |
| summary | `2026-03-03-java-logic-ternary` | R04, I02, E01 | 전면 재작성 | 누락됐던 형변환 시점·정수 나눗셈·char 비교와 원본 오기를 교정함 |
| summary | `2026-03-04-java-control-flow` | R05, E01 | 전면 재작성 | 조건문뿐 아니라 `printf`·학점/경품/평균 종합 실행 흐름까지 복원함 |
| summary | `2026-03-05-java-for-while` | R06, E01 | 부분 보강 | 초기화→조건→누적→증감과 실제 합계 결과를 복원함 |
| summary | `2026-03-06-java-while-array` | R07, E01 | 부분 보강 | 정답 입력 순서, 음수 종료/평균, 배열 계산 결과를 복원함 |
| summary | `2026-03-09-java-class-object` | R08, R14, E01 | 전면 재작성 | 업무 파악→객체→메서드 매개변수/반환→`void`→캡슐화 흐름을 복원함 |
| summary | `2026-03-10-java-constructor-overloading-inheritance` | R09, R13, R14, E01 | 전면 재작성 | 03-11 음료 귀속 오류를 03-10 `Animal` 계층으로 교정하고 원천 코드 불일치를 명시함 |
| summary | `2026-03-11-java-inheritance-polymorphism` | R10, R13, E01 | 부분 보강 | 자식 생성→`super`→부모 배열→`instanceof`→다운캐스팅 실행 흐름을 보강함 |
| summary | `2026-03-12-java-abstract-interface-static` | R11, R13, R14, E01 | 부분 보강 | 실제 `Beverage05`와 물·샷·우유 인터페이스/메서드로 교정·구체화함 |
| summary | `2026-03-13-java-project-oracle-start` | R12, Oracle 시작 MD | 전면 재작성·근거 부족 | 근거 없는 프로젝트 해석을 제거하고 팀 프로젝트/코드리뷰·Oracle/DBeaver 전환만 보존함 |
| summary | `2026-03-13-java-subject-review` | R01~R13 | 유지 | 문법→객체지향→Oracle 연결과 대표 실습 앵커가 충분함 |
| summary | `java-homework-research-review` | R14 | 신규 필요 | 직접 수업 복습과 메모리·컬렉션·제네릭 사전조사를 분리하고 답안 검증 경계를 보존함 |
| concept | `java-basic-types` | R01, R02, R13, E01 | 부분 보강 | 형변환 시점 예시와 선행·후속·후속 과목 경계를 추가함 |
| concept | `java-operators` | R02, R04, R13, I02, E01 | 부분 보강 | 증감·형변환·삼항 실제 코드와 `<>`·`&` 원본 오기 경계를 추가함 |
| concept | `java-conditional-logic` | R04, R05, R13, E01 | 부분 보강 | 실제 학점·switch 결과와 선행/후속 범위를 추가함 |
| concept | `java-loop` | R06, R07, R11, R13, E01 | 부분 보강 | Scanner 무한 반복·평균 0분모·향상 for/FIFO 오해와 직접 학습 범위를 보강함 |
| concept | `java-array` | R07, R09, R11, R13, E01 | 부분 보강 | 입력 크기 배열·기본값/null·`length`·음수 홀짝·원본 문법 오류를 보강함 |
| concept | `java-class-object` | R08, R13, R14, E01 | 전면 재작성 | 객체/참조·반환/void·필드/지역 변수·getter/setter 검증 지점을 복원함 |
| concept | `java-method-constructor-overloading` | R08, R09, R13, E01 | 전면 재작성 | 메서드 호출 데이터 흐름과 생성자·오버로딩 오해를 실제 코드로 재구성함 |
| concept | `java-object-array-memory` | R09, R10, R13, R14 | 부분 보강 | 실제 상품명·음료 타입 배열과 후속 프로젝트 경계를 명시함 |
| concept | `java-inheritance` | R09, R10, R13, E01 | 부분 보강 | `Americano03`→`super`→`Beverage03` 초기화와 기본 생성자 오류를 복원함 |
| concept | `java-polymorphism-casting` | R10, R13, E01 | 부분 보강 | 실제 `Beverage04[]`, `instanceof`, 다운캐스팅 예시와 범위를 추가함 |
| concept | `java-abstract-interface` | R11, R13, R14, E01 | 전면 재작성 | 비근거 `Cookable` 제거, 실제 기능 인터페이스와 현대 Java 경계로 교정함 |
| concept | `java-interface-capability-design` | R11, R13 | 통합 후보→유지 보강 | 실제 `SpecialCoffee05` 다중 기능과 capability 설계 역할을 강화해 독립 가치를 확보함 |
| concept | `java-memory-static-final` | R11, R13, R14, E01 | 전면 재작성 | 실제 `STORE_NAME`·`beverageCount++`와 숙제 메모리 모델의 정확성 경계를 분리함 |
| concept | `java-access-modifier-encapsulation` | R08, R10, R13, R14 | 신규 필요 | 세 수업/숙제에 반복된 접근 범위·getter/setter·상속 캡슐화를 독립 페이지로 보존함 |
| entity | `java` | R01~R14, E01 | 부분 보강 | 첫 등장·날짜별 이력에 프로젝트/면접 설명 관점을 추가함 |
| entity | `git` | R03, E03, Linux 후속 raw | 부분 보강 | Java 첫 `git init`과 후속 협업 역할을 분리하고 본문 출처를 복원함 |
| entity | `github` | R03, E03, Linux·CI/CD 후속 raw | 부분 보강 | 원격 저장소→PR 협업→Actions 자동화 이력을 단계별로 구분함 |
| entity | `intellij-idea` | R01, R03, E02, E03, Spring 후속 교안 | 부분 보강 | Java 직접 작업 환경과 Spring 후속 확장, IDE 설명 관점을 분리함 |
| comparison | `primitive-vs-reference-types` | R01, R02, R09, R13, R14, E01 | 부분 보강 | 계산·상품 객체·객체 배열 선택 상황과 지역 변수 기본값 예외를 추가함 |
| comparison | `array-vs-collection` | R07, R11, R13, R14 | 부분 보강 | 3개 선택 상황과 직접 실행/숙제 조사/후속 Spring 범위를 분리함 |
| comparison | `overloading-vs-overriding` | R09, R10, R13, E01 | 부분 보강 | 상품 생성자와 `toString()` 재정의의 구체 상황·동시 사용 관계를 추가함 |
| comparison | `interface-vs-abstract-class` | R11, R13, R14, E01 | 부분 보강 | 실제 음료 공통 상태와 물·샷·우유 기능 조합으로 선택 기준을 구체화함 |

### 통합·신규·query 판단

- 기존 34개 감사 분류는 유지 1개, 부분 보강 22개, 전면 재작성 10개, 통합 후보 1개다. 통합 후보 `java-interface-capability-design`은 실제 `SpecialCoffee05` 기반 capability 설명을 강화해 독립 페이지로 유지했다.
- 반복 학습 가치가 명확한 `java-access-modifier-encapsulation` concept과 날짜 없는 숙제를 직접 수업/사전조사로 분리한 `java-homework-research-review` summary를 신설했다.
- Java 관련 실제 사용자 질문 기록을 확인했지만 별도 query로 보존해야 할 신규 질문은 없었다. 숙제의 조사 질문은 이미 concept/comparison에 흡수되어 임의 query를 만들지 않았다.
- 유일한 근거 부족 페이지는 03-13 프로젝트 전환 summary다. 원본에 프로젝트 코드가 없다는 한계를 본문에 명시했으므로 근거 없는 보완 없이 완료 범위에 포함했다.

## 단계 2 Oracle 감사·수정 상세

### raw 출처 식별자

- `R01` `raw/KoreaICT/2. Oracle/2026.03.13(금) - 시작/2026.03.13(금) - 시작.md`
- `R02` `raw/KoreaICT/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
- `R03` `raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `R04` `raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
- `R05` `raw/KoreaICT/2. Oracle/2026.03.19(목)/2026.03.19(목).md`
- `R06` `raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
- `R07` `raw/KoreaICT/2. Oracle/Oracle 총정리/Oracle 총정리.md`
- `E01` `raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf`
- `E02` `raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf`
- `E03` `raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법(version 2.0).pdf`
- `S01` `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A01.관리자 사용자 생성하기.sql`
- `S02` `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A02.오라맨 스크립트.sql`
- `S03` `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A03 Oraman ddl.sql`
- `S04` `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A03.Oraman ddl(선생님이 만든 버젼).sql`
- `S05` `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A03_2.Oraman ddl 이후 DML.sql`
- `S06` `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A04.DDL 실습.sql`
- `S07` `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A05.DQL 실습.sql`
- `S08` `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A06.함수 실습.sql`
- `S09` `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A07 조인 실습.sql`
- `X01` `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/기타 스크립트/Script.sql` — 0바이트 빈 파일로 내용 주장 근거가 없음
- `X02` `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/기타 스크립트/Script-1.sql` — 학생·학과·성적 데이터와 FK 위반 실습
- `X03` `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/기타 스크립트/Script-2.sql` — 회원·상품·주문·주문상세와 자식 행 삭제 제한 실습
- `X04` `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/기타 스크립트/Script-3.sql` — View 생성·JOIN View·권한 부여/박탈
- `X05` `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/기타 스크립트/Script-4.sql` — 다른 schema에서 Oracle View 조회

`R02`~`R06`은 순서대로 03-16, 03-17, 03-18, 03-19, 03-20이다. `S03`은 DBeaver가 생성한 상세 저장 옵션과 객체 comment를 보존한 export이고, 실제 PK/FK/`ON DELETE` 판단은 날짜 원문과 `S04` 교사 작성 DDL을 우선했다. `X01`은 빈 파일임을 확인해 어떤 wiki 주장에도 사용하지 않았다. 별도 Oracle 숙제 파일은 현재 raw 24개 재고에 없다.

### 기존 페이지 ↔ raw 대응 및 분류

| 유형 | wiki 페이지 | 주 대응 출처 | 분류 | 감사·처리 결과 |
|---|---|---|---|---|
| summary | `2026-03-13-java-project-oracle-start` | R01, Java 03-13 | 부분 보강 | Java 프로젝트 종료→Oracle/DBeaver 설치 전환을 복원하고 객체-테이블 매핑은 후속 범위로 구분함 |
| summary | `2026-03-16-oracle-dbms-sql-dbeaver` | R02, E01, E02, S01, S02 | 전면 재작성 | DBMS/클라이언트, 관리자/일반 사용자, schema→테이블 순서를 복원하고 실습 비밀번호 재노출을 제거함 |
| summary | `2026-03-17-oracle-ddl-dml-constraints-sequence` | R03, E01, E02, S02~S05 | 부분 보강 | 번호 생성→데이터 사전→DDL 복구→PK/FK/삭제 규칙의 수업 순서와 `MAX`/`NEXTVAL` 차이를 보강함 |
| summary | `2026-03-18-oracle-constraints-validation` | R04, E01, E03, S06, S07 | 부분 보강 | 위반 입력→트랜잭션→DDL→DQL 흐름, 폼 검증/DB 제약조건 경계, 삭제된 초안/실제 트랜잭션 구간을 구분함 |
| summary | `2026-03-19-oracle-functions-join-subquery` | R05, E01, S08, S09 | 부분 보강 | 값 가공→집계→JOIN→서브쿼리의 난도 흐름과 outer join의 `COUNT(writer)` 이유를 보강함 |
| summary | `2026-03-20-database-modeling-normalization-view-index` | R06, E01, E02, X02~X05 | 전면 재작성 | 함수 종속성을 PK/FK와 혼동한 원본 메모를 교정하고 설계→DDL/FK→View/Index 경계를 복원함 |
| summary | `2026-03-20-oracle-subject-review` | R01~R07, E01~E03, S01~S09, X02~X05 | 부분 보강 | 실제 INSERT/JOIN 앵커와 Oracle 직접 수업/후속 Spring·JPA 경계를 추가한 과목 허브로 강화함 |
| concept | `oracle-sql-basics` | R02, R04, E01, S07 | 부분 보강 | 환경 생성→입력→조건 조회 맥락과 Java 선행·함수/JOIN/서브쿼리·JPA 후속 연결을 추가함 |
| concept | `oracle-constraints-sequence` | R03, R04, E01, S02, S04 | 통합 후보→유지 보강 | 식별값 발급과 DB 검증이 한 INSERT에서 만나는 overview 역할을 명확히 하고 세부 페이지로 연결함 |
| concept | `oracle-functions-join-subquery` | R05, S08, S09 | 통합 후보→유지 보강 | 중복 사전이 아니라 03-19 함수→집계→JOIN→서브쿼리 탐색 지도로 역할을 고정함 |
| concept | `oracle-ddl-dml-transaction` | R02~R04, E01, E03, S06 | 부분 보강 | 실제 상품 INSERT→조회→ROLLBACK→재조회와 DBeaver Auto Commit/Oracle 트랜잭션을 구분함 |
| concept | `oracle-sequence` | R02~R04, S02, S04, S05 | 부분 보강 | 날짜별 등장, 독립 schema 객체, `user_sequences`, `MAX(id)` 오해와 `NOCYCLE` 이유를 추가함 |
| concept | `oracle-data-dictionary-schema-objects` | R03, R06, R07, S02, X04 | 신규 필요 | `USER_TABLES`·`USER_SEQUENCES`·`USER_VIEWS`가 여러 날짜에 반복되어 DDL 결과와 사용자 소유 schema 객체를 검증하는 독립 concept으로 보존함 |
| concept | `oracle-referential-integrity` | R03, R04, R06, E02, S04, X02, X03 | 부분 보강 | 회원-게시글·주문-상세·학생-학과 관계와 JOIN/FK, DB/JPA cascade 경계를 구분함 |
| concept | `oracle-sql-functions` | R05, E01, S08 | 부분 보강 | 행 가공→그룹 집계 맥락, `COUNT(*)`/`COUNT(expr)`, 일반 컬럼/GROUP BY 오류 기준을 보강함 |
| concept | `oracle-join` | R05, E01, S09 | 부분 보강 | 정규화된 정보 복원, JOIN/FK 차이, outer join count와 선행·후속 연결을 보강함 |
| concept | `oracle-subquery` | R05, S09 | 부분 보강 | 최소·평균 급여와 여러 관리자 조건으로 결과 개수·연산자·JOIN 선택 기준을 구체화함 |
| concept | `database-modeling-normalization` | R06, E02, X02, X03 | 전면 재작성 | 이상 현상→함수 종속성→분해→FK DDL→JOIN 복원과 Oracle 직접/프로젝트 확장 경계를 재구성함 |
| concept | `database-normalization-functional-dependency` | R06, E02, X02 | 전면 재작성 | `X→Y`를 PK/FK로 치환한 오해를 교정하고 학생·학과·성적 결정 관계를 구현 단계와 분리함 |
| concept | `database-view-index` | R06, E01, X04, X05 | 부분 보강 | View 실제 권한 흐름, 비밀번호 컬럼 노출 경계, Index의 직접 학습 범위와 비근거 성능 수치 금지를 명시함 |
| entity | `oracle-database` | R01~R07, 관련 E/S/X | 부분 보강 | 첫 등장·날짜별 이력에 구현 역할, 면접 설명 관점, Oracle 직접/후속 JPA 경계를 추가함 |
| entity | `dbeaver` | R01~R06, E02, E03 | 부분 보강 | 설치→연결→DDL export→트랜잭션→ERD 이력과 DBMS/클라이언트 오류 진단 관점을 추가함 |
| comparison | `on-delete-set-null-vs-cascade` | R03, R06, E02, S04, X02, X03 | 부분 보강 | 게시글 보존/주문상세 삭제의 2개 선택 상황, nullable FK, No Action, JPA 경계를 추가함 |
| comparison | `ddl-vs-dml-vs-dql` | R02, R04, E01, S06, S07 | 전면 재작성 | EMAIL DDL·급여 UPDATE·BETWEEN SELECT의 원문 SQL과 주문 저장/조회 선택 상황을 추가함 |
| comparison | `primary-key-vs-foreign-key` | R03, R06, E02, S04, X02, X03 | 전면 재작성 | 회원 식별·게시글/주문상세 참조 상황과 PK/FK·JOIN·함수 종속성 오해를 구분함 |
| comparison | `oracle-inner-vs-outer-join` | R05, E01, S09 | 전면 재작성 | 게시글 0개 회원 보존 여부, 실제 집계 SQL, `COUNT(*)` 오해를 선택 상황으로 재구성함 |
| comparison | `single-row-vs-multi-row-subquery` | R05, S09 | 부분 보강 | 평균 1개와 관리자 여러 명의 실제 예제로 결과 개수·연산자 선택과 오류 해결 기준을 보강함 |
| comparison | `where-vs-having` | R04, R05, S08 | 부분 보강 | 상품 행/회사 그룹의 2개 선택 상황과 `WHERE→GROUP BY→HAVING` 실행 단계를 구분함 |
| comparison | `jpql-vs-sql` | R03, FrontEnd_BackEnd 04-20·04-22 | 부분 보강 | Oracle `SELECT * FROM orders`와 실제 `Order` JPQL을 나란히 두고 직접 수업/후속 JPA 경계를 명시함 |

### 통합·신규·query 판단

- 기존 28개 감사 분류는 부분 보강 19개, 전면 재작성 7개, 통합 후보 2개이며 미분류·근거 부족은 0개다.
- 통합 후보 `oracle-constraints-sequence`는 번호 발급과 무결성 검증의 공동 overview, `oracle-functions-join-subquery`는 03-19 탐색 지도라는 고유 역할을 강화해 독립 페이지로 유지했다.
- 최초 직접 감사에서는 기존 페이지로 충분하다고 판단했지만, 후속 병렬 3계통 감사에서 `USER_TABLES`, `USER_SEQUENCES`, `USER_VIEWS`가 03-17·03-20·총정리에 반복되는 공통 검증 축임을 재확인했다. 이에 `oracle-data-dictionary-schema-objects` concept 1개를 신설하고 기존 시퀀스·View·Oracle entity에 연결했다.
- Hermes 세션 기록에서 Oracle·서브쿼리·HAVING·정규화·시퀀스·DBeaver·트랜잭션 관련 실제 사용자 질문을 검색했지만, 이번 작업 지시 외에 독립 query로 보존할 반복 질문은 발견하지 못했다. 임의의 사용자 혼동을 만들지 않아 query는 신설하지 않았다.

## 단계 3 UI&UX 감사·수정 상세

### raw 전체 파일 재고

- 실제 파일 수: 96개
- 확장자: Markdown 8, PDF 5, HTML 59, CSS 1, JavaScript 1, PNG 11, JPG 9, GIF 2
- 아래 경로는 2026-07-15의 `raw/KoreaICT/3. UI&UX` 실제 파일 전수 재귀 목록이다. `FrontEnd&BackEnd.pdf`는 UI&UX 폴더 안 교육자료로 경계만 확인했으며 단계 4 과목 고도화를 시작하지 않았다.

- `U001` `raw/KoreaICT/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md`
- `U002` `raw/KoreaICT/3. UI&UX/2026.03.24(화)/2026.03.24(화).md`
- `U003` `raw/KoreaICT/3. UI&UX/2026.03.25(수)/2026.03.25(수).md`
- `U004` `raw/KoreaICT/3. UI&UX/2026.03.26(목)/2026.03.26(목).md`
- `U005` `raw/KoreaICT/3. UI&UX/2026.03.27(금)/2026.03.27(금).md`
- `U006` `raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
- `U007` `raw/KoreaICT/3. UI&UX/UI&UX 총정리/속성들.md`
- `U008` `raw/KoreaICT/3. UI&UX/UI&UX 총정리/태그들.md`
- `U009` `raw/KoreaICT/3. UI&UX/교육 자료/FrontEnd&BackEnd.pdf`
- `U010` `raw/KoreaICT/3. UI&UX/교육 자료/HTML&JS&CSS 이론(new).pdf`
- `U011` `raw/KoreaICT/3. UI&UX/교육 자료/images/americano01.png`
- `U012` `raw/KoreaICT/3. UI&UX/교육 자료/images/basil.jpg`
- `U013` `raw/KoreaICT/3. UI&UX/교육 자료/images/bg_choco.jpg`
- `U014` `raw/KoreaICT/3. UI&UX/교육 자료/images/brioche_02.png`
- `U015` `raw/KoreaICT/3. UI&UX/교육 자료/images/cappuccino02.png`
- `U016` `raw/KoreaICT/3. UI&UX/교육 자료/images/chamomile.jpg`
- `U017` `raw/KoreaICT/3. UI&UX/교육 자료/images/ciabatta_02.png`
- `U018` `raw/KoreaICT/3. UI&UX/교육 자료/images/croissant_02.png`
- `U019` `raw/KoreaICT/3. UI&UX/교육 자료/images/french_baguette_01.png`
- `U020` `raw/KoreaICT/3. UI&UX/교육 자료/images/herbtea2.gif`
- `U021` `raw/KoreaICT/3. UI&UX/교육 자료/images/herbtea3.jpg`
- `U022` `raw/KoreaICT/3. UI&UX/교육 자료/images/lemonbalm.jpg`
- `U023` `raw/KoreaICT/3. UI&UX/교육 자료/images/milk.jpg`
- `U024` `raw/KoreaICT/3. UI&UX/교육 자료/images/milk_c.jpg`
- `U025` `raw/KoreaICT/3. UI&UX/교육 자료/images/mybu.gif`
- `U026` `raw/KoreaICT/3. UI&UX/교육 자료/IT 관련 용어.pdf`
- `U027` `raw/KoreaICT/3. UI&UX/교육 자료/IT 관련 용어2.pdf`
- `U028` `raw/KoreaICT/3. UI&UX/교육 자료/jQueryImageTest/jQueryImageTest.html`
- `U029` `raw/KoreaICT/3. UI&UX/교육 자료/jQueryImageTest/whitewine02.png`
- `U030` `raw/KoreaICT/3. UI&UX/교육 자료/jQueryImageTest/wine01.png`
- `U031` `raw/KoreaICT/3. UI&UX/교육 자료/library&framework.png`
- `U032` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/aaatemplate.html`
- `U033` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/apple.jpg`
- `U034` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/arrayEx.html`
- `U035` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/basicFunc.html`
- `U036` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/boxModelTest.html`
- `U037` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/end.html`
- `U038` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/fanta02.png`
- `U039` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/first.html`
- `U040` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/firstExam.html`
- `U041` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/fisrtExam.html`
- `U042` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/fourth.html`
- `U043` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/gaipForm.html`
- `U044` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/gaipForm2.html`
- `U045` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/gotopage1.html`
- `U046` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/imageMap.html`
- `U047` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/kinds2.html`
- `U048` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/Koala.jpg`
- `U049` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/listExam.html`
- `U050` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/listModelEx.html`
- `U051` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/locationEx.html`
- `U052` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/mathEx.html`
- `U053` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/MyElementEx01.html`
- `U054` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/MyElementEx02.html`
- `U055` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/myfont.html`
- `U056` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/myFuncExam.html`
- `U057` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/mytext.html`
- `U058` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/NumberEx.html`
- `U059` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/operatorEx.html`
- `U060` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/outerFile.css`
- `U061` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/positionEx01.html`
- `U062` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/positionEx02.html`
- `U063` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/positionEx03.html`
- `U064` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/positionEx04.html`
- `U065` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/register1.html`
- `U066` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/register2.html`
- `U067` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/script.js`
- `U068` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/second.html`
- `U069` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/spanEx.html`
- `U070` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/start.html`
- `U071` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/StringEx.html`
- `U072` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/styleExam.html`
- `U073` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/tableExam.html`
- `U074` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/templatejsp.html`
- `U075` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/third.html`
- `U076` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/undefinedEx.html`
- `U077` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/회원가입화면.png`
- `U078` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/CartList.html`
- `U079` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/FruitList.html`
- `U080` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/FruitOne.html`
- `U081` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/LoginPage.html`
- `U082` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/OrderList.html`
- `U083` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/ProductDetail.html`
- `U084` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/ProductInsertForm.html`
- `U085` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/ProductList.html`
- `U086` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/SignupPage.html`
- `U087` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/CartList.html`
- `U088` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/FruitList.html`
- `U089` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/FruitOne.html`
- `U090` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/LoginPage.html`
- `U091` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/OrderList.html`
- `U092` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductDetail.html`
- `U093` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductInsertForm.html`
- `U094` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductList.html`
- `U095` `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/SignupPage.html`
- `U096` `raw/KoreaICT/3. UI&UX/교육 자료/웹 서비스 Ui&UX.pdf`

### 기존 페이지 ↔ raw 대응 및 분류

| 유형 | wiki 페이지 | 주 대응 출처 | 분류 | 감사·처리 결과 |
|---|---|---|---|---|
| summary | `2026-03-23-html-css-intro` | U001, U006~U008, U010, U026, U073 | 부분 보강 | 실제 `tableExam`의 table/image 코드와 정적 UI/후속 서버 경계를 복원함 |
| summary | `2026-03-24-css-layout-javascript-intro` | U002, U006~U008, U010, U036, U061~U064 | 전면 재작성 | box/list/span 레이아웃, non-Bootstrap CartList, JavaScript 입문과 실제 혼동을 날짜 흐름으로 다시 구성함 |
| summary | `2026-03-25-bootstrap-form` | U003, U006~U008, U078, U084, U087, U093, U096 | 부분 보강 | non-Bootstrap form→Bootstrap form 순서와 직접 구현/후속 서버 저장 경계를 추가함 |
| summary | `2026-03-26-javascript-dom-product-pages` | U004, U006~U008, U083~U085, U092~U094 | 전면 재작성 | ProductList·상태형 ProductDetail·날짜 노트 ProductDetailNew를 분리하고 query string→`Number`→`find`를 다시 구성함 |
| summary | `2026-03-27-jquery-ui-interaction` | U005, U006~U008, U028~U030 | 전면 재작성 | 실제 selector/class명과 7개 이미지 상호작용, `first/last`·`prepend/append` 노드 이동 흐름으로 다시 구성함 |
| summary | `2026-03-27-uiux-subject-review` | U001~U008, U010~U031, U032~U096 | 전면 재작성 | 대표 artifact·원본/교육파일 차이표와 직접 구현/후속 확장 경계를 가진 복습 허브로 다시 구성함 |
| concept | `html-css-basics` | U001~U003, U006~U008, U010, U036, U060~U073, U078~U095 | 부분 보강 | 실제 class cascade·select 예제와 `alt` 속성 정정을 추가함 |
| concept | `javascript-dom` | U002, U004, U006, U010, U034~U076, U083~U085, U092~U094 | 부분 보강 | 첫 DOM 출력과 상품 배열·URL 문자열→숫자 변환·더미 데이터 경계를 보강함 |
| concept | `bootstrap-basics` | U003~U005, U006, U087~U096 | 부분 보강 | CDN 제약, non-Bootstrap 선행 구조, Bootstrap/후속 React 범위를 구분함 |
| concept | `jquery-basics` | U005, U006, U028~U031 | 유지 | 기존 원문 재현도가 높아 구조를 유지하고 category 필터·기존 DOM 노드 이동의 실제 교육 코드만 경미 보강함 |
| concept | `html-form-controls-submission` | U002, U003, U087, U093 | 신규 필요 | form control의 `name/value`, submit event, `FormData`, 서버 검증 경계를 후속 React/Spring과 연결함 |
| entity | `html` | U001~U008, U032~U095 | 부분 보강 | 첫 등장·날짜별 역할에 화면 구조와 프로젝트/면접 설명 관점을 추가함 |
| entity | `css` | U001~U008, U010, U028, U032~U076 | 부분 보강 | cascade·position·상태 class 학습 이력과 프로젝트 경계를 추가함 |
| entity | `javascript` | U002, U004~U006, U010, U028, U034~U076, U083~U094 | 부분 보강 | DOM→배열 card→query string 흐름과 언어/DOM/library 구분을 보강함 |
| entity | `bootstrap` | U003~U006, U028, U087~U096 | 부분 보강 | non-Bootstrap→class 적용 이력과 UI framework 설명 관점을 추가함 |
| entity | `jquery` | U005, U006, U028~U031 | 부분 보강 | 첫 등장과 이미지 UI 기능별 역할, 레거시/React 경계를 추가함 |
| comparison | `html-tag-vs-attribute` | U001, U003, U007, U008, U073, U093 | 부분 보강 | 실제 basil image·form 입력의 두 선택 상황과 `<alt>` 오해를 교정함 |
| comparison | `id-vs-class` | U001, U004, U005, U006, U028, U073, U085, U094 | 부분 보강 | 단일 container/반복 image group의 두 선택 상황과 동시 사용 관계를 추가함 |
| comparison | `javascript-dom-vs-jquery` | U004, U005, U028, U094 | 부분 보강 | 실제 버튼 숨김·이미지 class 토글 코드와 wrapper 관계를 명시함 |
| comparison | `inline-style-vs-internal-css-vs-external-css` | U001, U002, U007, U036, U060, U073 | 부분 보강 | 단일 확인·문서 공통·CDN 공유의 세 선택 상황과 공존 관계를 추가함 |
| comparison | `get-vs-post` | U003, U004, U084, U085, U093, U094 | 부분 보강 | 상세 조회와 후속 등록의 두 상황, POST/HTTPS 보안 오해를 교정함 |
| comparison | `library-vs-framework` | U003, U005, U006, U028, U031 | 부분 보강 | 교육 이미지의 예시 차이를 보존하고 jQuery+Bootstrap 동시 사용 관계를 추가함 |
| comparison | `ui-vs-ux` | U001, U026, U027, U092 | 신규 필요 | 과목 첫 정의와 form·loading/error/success 화면으로 인터페이스와 전체 경험을 비교함 |
| comparison | `custom-css-vs-bootstrap` | U002, U003, U078, U084, U087, U093 | 신규 필요 | 대응하는 non-Bootstrap/Bootstrap 화면 9쌍의 선택 상황·공존 관계·오해를 정리함 |

### 통합·신규·query 판단

- 기존 직접 관련 21개는 summary 6, concept 4, entity 5, comparison 6이다. 비동기 감사 재대조 결과 유지 1개, 부분 보강 16개, 전면 재작성 4개로 확정했으며 통합 후보·근거 부족·미분류는 0개다.
- 기존 페이지에 억지로 흡수하면 탐색 역할이 흐려지는 form 제출, UI/UX 차이, 직접 CSS/Bootstrap 비교를 신규 3개로 만들었다. 최종 UI&UX 대상은 24개이며 `wiki/index.md`의 `Total pages: 265`와 일치한다.
- 세션 기록과 원본의 질문/혼동을 검토했지만 실제 사용자 질문으로 별도 보존할 query는 없었다. `<alt>`, POST 보안, id/class, DOM/jQuery 혼동은 기존 concept/comparison에 흡수했다.
- 코드 fence는 날짜별 MD와 교육 HTML/CSS/JavaScript 파일을 우선 근거로 사용했다. PDF는 수업 흐름·용어·화면 요구사항의 보조 근거이며, 추출되지 않은 실행 결과를 만들지 않았다.
- `U009`는 UI&UX 교육자료 디렉터리 재고에는 포함하지만 단계 4 `FrontEnd_BackEnd`의 날짜별 raw·기존 wiki 대응·수정에는 사용하지 않았다.

## 새 세션 복붙 프롬프트 생성 규칙

- 첫 줄은 반드시 `smart 모드로 진행한다.`이다.
- 현재 단계 번호와 과목을 명시한다.
- `D:\Study_LLM_Wiki`의 `AGENTS.md`, `wiki/index.md`, 최근 `wiki/log.md`, 이 계획 문서를 먼저 읽게 한다.
- 해당 과목 하나만 감사 → 수정 → 검증까지 완료하게 한다.
- `raw/` 읽기 전용, 기존 변경 보호, 다음 과목 자동 실행 금지를 명시한다.
- 구조 lint가 아니라 내용 완료 기준을 요약한다.
- 완료 기록·index/log 업데이트와 다음 세션 프롬프트 제공을 요구한다.
- 단계가 미완료면 다음 과목 프롬프트가 아니라 같은 단계 재개 프롬프트를 만들게 한다.

## 첫 실행 단계

- 단계: 1
- 과목: `1. Java`
- 범위: Java 날짜별 summary, Java 총정리 허브, Java concept/entity/comparison 및 직접 연결된 Git/GitHub/IntelliJ 페이지
- 주의: Java 수업 직접 근거와 이후 Spring/프로젝트 연결을 구분한다. 교육자료와 숙제는 출처로 활용하되, raw 원본은 수정하지 않는다.
- 완료 뒤 다음 단계: `2. Oracle`

## 관련 페이지

- [[_meta/wiki-quality-audit-2026-07-02|2026-07-02 LLM Wiki 품질 감사 리포트]]
- [[_meta/llm-wiki-operating-model|LLM Wiki 운영 모델]]
- [[_meta/llm-wiki-command-reference|LLM Wiki 명령어 참고]]
- [[_meta/txt-to-md-conversion-work-plan|TXT→MD 남은 과목 변환 작업 인계]]
