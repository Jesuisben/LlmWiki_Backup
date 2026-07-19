---
title: 중간 프로젝트 공부 내용 재고도화 전수 재고와 실용형 실행 계획
created: 2026-07-19
updated: 2026-07-19
type: meta
tags: [project, ci-cd, aws, auth, spring-boot, react, curriculum, study-log]
sources:
  - AGENTS.md
  - wiki/index.md
  - wiki/log.md
  - wiki/_meta/wiki-content-rehighquality-work-plan.md
  - wiki/_meta/passwordless-rehighquality-inventory-plan.md
  - wiki/_meta/cicd-rehighquality-inventory-plan.md
  - raw/KoreaICT/9. 중간 프로젝트 공부/CICD/Github_Secrets 예시.md
  - raw/KoreaICT/9. 중간 프로젝트 공부/CICD/JWT(RS256)생성 방법.md
  - raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md
  - raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md
status: growing
confidence: high
---

# 중간 프로젝트 공부 내용 재고도화 전수 재고와 실용형 실행 계획

## 문서 상태와 범위

이 문서는 내용 재고도화 단계 9 `중간 프로젝트 공부`의 실제 raw 재고, 직접 source 지식 페이지, raw↔wiki 책임 경계와 실용형 두 세션 실행 기준선이다.

- 현재 상태: **세션 2 전체 고정점 완료 — 단계 9 최종 완료**
- 세션 1: raw 전수 재고, 직접 source 페이지 재계산, Summary·Concept·Entity 우선 고도화
- 세션 2: 기존 Comparison 최종 감사, 신규 Comparison·Query 판단, 직접 페이지 전체 고정점, 단계 9 완료 여부 확정
- 전체 검증 통과 뒤 상위 `wiki-content-rehighquality-work-plan.md`에 단계 9 완료 행을 추가했다.
- `raw/KoreaICT/9. 중간 프로젝트 공부`: 읽기 전용

## 작업 전 Git·raw 기준선

- branch: `master...origin/master`
- 저장소 전체 시작 상태: 이전 Passwordless·Python 작업을 포함한 modified 10개가 이미 존재했다.
- 단계 9 raw scoped status: 0건
- 단계 9 raw scoped diff: 0건
- 시작 정렬 SHA-256 manifest digest: `1d77c60dbfa22cf5f9173b897b1e0ddb0906b98ff9b543a1ba476d7b13d2a50f`
- 이번 세션은 기존 변경을 복구·commit·push하지 않았다.

## raw 전수 재고 요약

- 실제 파일: **4개**, 총 **170,194 bytes**
- Markdown: **4개**, 총 **4,481줄**
- PDF: **0개** — text 추출 대상 없음
- JSON: **0개** — request/saved response 구조 검사 대상 없음
- 이미지: **0개**
- archive: **0개**
- 독립 source: **0개**
- 독립 config: **0개**
- 독립 script: **0개**
- 0바이트: **0개**
- 파일별 SHA-256 계산 결과 과목 내부 byte-identical 중복: **0개**

Java·TypeScript·YAML·XML·Dockerfile·Nginx·shell·SQL·JSON 문법은 대형 Markdown 가이드 안의 연속 snippet이다. 별도 project source/config/script, build artifact, image, JAR, frontend build, key file, workflow run log, screenshot으로 과확정하지 않는다.

## raw 식별자와 파일별 역할

| ID | 실제 경로 | bytes | 줄 | 역할 |
|---|---|---:|---:|---|
| R01 | `raw/KoreaICT/9. 중간 프로젝트 공부/CICD/Github_Secrets 예시.md` | 1,174 | 19 | registry·server·DB·JWT·object storage 설정의 역할 목록. 실제 값·등록 결과가 아님 |
| R02 | `raw/KoreaICT/9. 중간 프로젝트 공부/CICD/JWT(RS256)생성 방법.md` | 255 | 7 | RSA key pair 생성·문자열 준비 명령 절차. 생성된 key artifact·검증 결과 없음 |
| R03 | `raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md` | 78,136 | 2,228 | backend→AWS/Docker→Actions→frontend/Nginx→file/S3→DNS/ALB의 설계·snippet과 짧은 성공·연결 관찰 서술 |
| R04 | `raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md` | 90,629 | 2,227 | 인증 server→서비스 등록→Spring REST 계층→React polling UI→배포 점검 설계, 일부 인프라 출력·초기 실패 관찰 |

## 교육자료·설계·artifact·실행 결과 분류

| 층 | 이 raw 폴더의 상태 | 판단 |
|---|---|---|
| 교육·선행자료 | 별도 PDF·collection 없음 | Linux·AWS·CI/CD·Passwordless 선행 과목의 직접 raw가 배경 지식이며 단계 9 결과는 아님 |
| 설계 가이드 | R03·R04 | 전체 적용 순서와 작성용 snippet을 소유 |
| 설정·key 목록 | R01·R02 | 필요한 역할·생성 절차를 소유 |
| 독립 project artifact | 0개 | Markdown snippet을 실제 repository file로 세지 않음 |
| embedded 부분 출력·관찰 | R03·R04 | 일부 shell·인증서·container 파일·거부 HTTP 응답, 짧은 성공·연결 서술, MIME 실패 관찰 |
| 독립 end-to-end 결과 artifact | 0개 | workflow run·image digest·재현 가능한 배포/API/browser/DB 결과가 없음 |

문서 안의 “확인”, “성공”, “연결”은 조건·지시, 짧은 관찰 주장, 구체 출력으로 나눠 읽는다. 부분 출력과 실패 관찰은 보존하되 독립 project artifact와 end-to-end 성공으로 확장하지 않는다.

## 직접 source 지식 페이지 재계산

세션 시작 시 frontmatter `sources`가 단계 9 raw를 가리킨 지식 페이지는 **9개**였다.

- summary 1
- concept 6
- entity 1
- comparison 1
- query 0

세션 1에서 기존 기술 Entity 6개에 단계 9 학습 이력과 직접 source를 추가했다. 현재 직접 지식 페이지는 **15개**다.

- summary **1**
- concept **6**
- entity **7**
- comparison **1**
- query **0**
- raw source union **4/4**
- 미분류 raw **0개**
- type·directory 불일치 **0개**

### Summary

- `wiki/summaries/2026-05-middle-project-cicd-passwordless-guide.md`

### Concept

- `wiki/concepts/middle-project-cicd-deploy-flow.md`
- `wiki/concepts/github-actions-secrets-deploy.md`
- `wiki/concepts/jwt-rs256-key-flow.md`
- `wiki/concepts/passwordless-x1280-auth-flow.md`
- `wiki/concepts/passwordless-qr-app-approval.md`
- `wiki/concepts/spring-boot-passwordless-integration.md`

### Entity

- `wiki/entities/github.md`
- `wiki/entities/docker.md`
- `wiki/entities/aws.md`
- `wiki/entities/spring-boot.md`
- `wiki/entities/react.md`
- `wiki/entities/jwt.md`
- `wiki/entities/passwordless-x1280.md`

### Comparison·Query

- `wiki/comparisons/passwordless-vs-password-login.md`
- Query 0개

## raw↔wiki 대응표

| raw | 직접 Summary | 직접 Concept | 직접 Entity | Comparison·Query |
|---|---|---|---|---|
| R01 | 중간 프로젝트 가이드 Summary | Secrets 기반 배포 | GitHub | 없음 |
| R02 | 중간 프로젝트 가이드 Summary | JWT RS256 key flow | JWT | 없음 |
| R03 | 중간 프로젝트 가이드 Summary | 배포 흐름·Secrets·RS256 | GitHub·Docker·AWS·Spring Boot·React·JWT | 없음 |
| R04 | 중간 프로젝트 가이드 Summary | X1280 흐름·QR/앱·Spring 연동 | Docker·AWS·Spring Boot·React·Passwordless 제품 | Passwordless vs password login |

## 직접 결과와 미보존 결과 경계

| 영역 | 문서에 직접 보존됨 | 미보존·완료로 단정 금지 |
|---|---|---|
| GitHub Actions | backend/frontend CI·CD workflow snippet, Secret 역할, test 생략 package 설정 | 실제 workflow file·run·test success·artifact |
| Docker | Dockerfile·설치·container 교체 명령 | image build/push digest, container state·log |
| AWS·DB | cloud 절차, VM DB container·SSH tunnel 상세, 일부 인증서 출력·연결 서술 | 관리형 DB와 VM container 중 최종 topology, resource export·target health·DNS/HTTPS 재현 결과 |
| Spring Boot | properties·JWT·file·Passwordless REST 계층 snippet, MIME 실패 관찰 | 독립 Java source, 수정 후 API, DB, session/JWT 결과 |
| React/Nginx | API/proxy·file UI·Passwordless polling snippet | 외부 callback, 독립 source/build, browser·network·timeout 결과 |
| RS256 | key 생성·주입·서명/검증 설계 | key artifact, 실제 token·검증 log |
| Passwordless | server 준비·서비스 등록·REST/UI 작성 절차와 일부 shell·파일·거부 응답 | 실제 등록·승인·해제 성공과 project login |

가이드 내부에는 DB URL 주입과 application 소비 불일치, object 삭제 snippet과 설명 충돌, Passwordless Secret 등록 목록과 container 전달 항목 불일치가 있다. R04의 CSS snippet 한 단위는 TypeScript 언어로 표시돼 있지만 raw는 수정하지 않았고 wiki fence로 복사하지 않았다. raw만으로 최종 구현을 확정하지 않는다.

## 날짜·과목·단계 경계

- FrontEnd_BackEnd 04-06~07은 password login·JWT/Bearer/SecurityContext의 직접 기준선이다.
- Linux는 Docker·Nginx·process/service/port와 GitHub 협업 기반이다.
- AWS 05-06~08은 VPC·EC2·RDS와 자원 생명주기의 직접 수업이다.
- CI/CD 05-11~13은 Actions·Docker image·EC2 CD, DNS/HTTPS/ALB, Terraform/S3 직접 수업이다.
- Passwordless 05-14~21은 인증 제품·server·sample·REST contract 직접 수업이다.
- 단계 9는 이 선행 내용을 중간 프로젝트에 적용하기 위한 Markdown 가이드·snippet 묶음이다.
- 단계 8의 직접 결과를 단계 9 실행 결과로 소급하지 않고, 단계 9 설계를 Passwordless 날짜 수업의 실행 결과로 되돌려 쓰지 않는다.

## 세션 1 생성·수정 결과

- 신규 Meta: 이 inventory 1개
- Summary: 1개 전면 고도화
- Concept: 6개 전수 대조·고도화
- Entity: 기존 7개에 단계 9 학습 이력·실제 역할·미보존 결과를 누적
- Comparison: 구조 최종 판단을 세션 2로 유지; 안전상 추가 수정 없음
- Query: 신규 생성 없음
- 합성 text fence 1개를 prose·표로 전환해 직접 지식 페이지 fence는 0개가 됨
- 후속 병렬 감사 반영: DB topology·환경변수 소비 불일치, test 생략, 부분 출력/관찰, object 삭제 모순, polling/callback·timeout, challenge/session 결속, 공개 endpoint와 local 상태 drift를 추가 교정함

## Comparison·Query 후보 최종 판단

| 후보 | 최종 판정 | 근거와 책임 페이지 |
|---|---|---|
| 기존 `passwordless-vs-password-login` | **유지·고도화** | 04-06~07 비밀번호/JWT 기준선과 05월 Passwordless·단계 9 적용 설계를 비교하는 독립 검색 책임이 있다. 단계 9 polling, callback 부재, 승인 결과→JWT 사이의 사용자·challenge/session·만료 결속과 runtime 미확정 범위를 추가했다. |
| HS256 vs RS256 | **기존 페이지에 흡수** | 대칭키 기준선과 비대칭키 차이는 `jwt-rs256-key-flow`와 `jwt` Entity가 key 소유·서명/검증·Secret 주입·runtime 미확정까지 이미 소유한다. 단계 9에는 실제 key·token·검증 결과가 없어 별도 Comparison의 두 선택 상황을 확장할 근거가 부족하다. |
| workflow 정의 vs 실행 결과 | **기존 페이지에 흡수** | `middle-project-cicd-deploy-flow`의 source/config→CI→registry→CD→application/data/cloud edge 완료 사다리와 통합 Summary의 증거 수준 표가 반복 검색 책임을 소유한다. 별도 페이지는 같은 축을 중복한다. |
| polling vs callback | **신규 기각** | R04는 React polling snippet만 제공하고 외부 server→Spring callback 구현·결과가 없다. 존재하지 않는 callback을 대칭적인 프로젝트 구현 결과처럼 합성하지 않고 QR/앱 Concept와 기존 로그인 Comparison에서 부재·경계만 보존한다. |
| local file vs object storage | **기존 페이지에 흡수** | `aws-s3-file-upload`가 local server storage와 object storage의 지속성·분리 책임을 이미 비교하고, 단계 9 통합 Summary가 object 삭제 설명 충돌과 실행 미확정을 소유한다. 신규 Comparison의 독립 책임이 부족하다. |
| 실제 장애 기록 기반 Query | **신규 기각** | raw에는 MIME 처리 실패와 거부 응답 같은 실패 관찰은 있으나 원인 확정→수정→재검증 성공 이력이 없다. 가상 해결 기록을 만들지 않고 `spring-boot-passwordless-integration` 진단 checklist와 증거 표에 흡수한다. |

최종 신규 수는 Comparison **0개**, Query **0개**다. 기존 Comparison 1개를 유지·고도화하므로 직접 지식 페이지 구성과 raw source union은 변하지 않는다.

## 세션 1 검증 결과

- 직접 지식 페이지: 15개 전수 분류, raw source union 4/4, 미분류 0
- 필수 frontmatter·source 실경로·본문 출처 동기화·허용 tag: 오류 0
- type·directory·index 등록·wikilink·고립·actionable placeholder·빈 sources: 오류 0
- 직접 지식 페이지 200줄 초과·`needs-review`·`confidence: low`: 0
- 이 inventory Meta는 raw·direct-page 전수 matrix를 한 문서에 보존하기 위한 207줄 구조적 예외이며 지식 페이지 분할 후보에서 제외
- code fence: 0개, 합성·비연속·`bash` 0
- 독립 artifact 과확정, 선행/후속 결과 소급, 실제 식별값 재노출: 0
- actual page count 279 = index `Total pages` 279
- affected tracked scope `git diff --check`: exit 0
- 신규 inventory trailing whitespace: 0, 검사 exit 0
- 종료 단계 9 raw scoped status/diff: 0건
- 종료 정렬 SHA-256 manifest digest: `1d77c60dbfa22cf5f9173b897b1e0ddb0906b98ff9b543a1ba476d7b13d2a50f` — 시작값과 동일
- 저장소 전체에는 별도 Python raw·Passwordless 작업 변경이 남아 있으며 이번 세션은 이를 복구·commit·push하지 않음
- 단계 9 전체 상태: **세션 1 완료 — Comparison·Query 최종 판단과 전체 고정점은 세션 2에서 수행**

## 세션 2 최종 검증 결과

- Comparison·Query: 기존 Comparison 1개를 유지·고도화하고, 신규 후보 4개와 장애 Query를 기존 Concept·Summary에 흡수하거나 근거 부족으로 기각했다. 신규 Comparison·Query는 0개다.
- 직접 지식 페이지: Summary 1·Concept 6·Entity 7·Comparison 1·Query 0, 합계 15개다. 디렉터리 기준과 frontmatter type 기준이 일치한다.
- raw 대응: source union 4/4, 미분류 raw 0개, 직접 source 실경로·frontmatter sources와 본문 출처 동기화 오류 0개다.
- 구조: 필수 frontmatter·허용 tag·type·directory·index 등록·wikilink·고립·actionable placeholder·빈 sources·`needs-review`·`confidence: low` 오류 0개다.
- 장문: 직접 지식 페이지 200줄 초과 0개다. 이 inventory는 raw·direct-page matrix와 두 세션 판정을 한 문서에 보존하는 Meta이므로 200줄 초과 구조적 예외로 유지한다.
- fence: 직접 15페이지의 code fence는 전체 0개이며 합성·비연속·언어 오류·`bash` 0개다. R04의 CSS snippet 언어 표기 문제는 raw 결함으로만 보존했고 wiki fence로 복사하지 않았다.
- 증거 경계: embedded snippet·부분 출력·관찰 서술·실패 관찰·조건/지시·독립 end-to-end 결과, 관리형 DB 계획·VM DB container 상세 절차, test 생략·test 성공, polling·callback, 외부 승인·JWT/session/인가를 분리했다.
- 인증 검토: timeout·polling 중단·오류/대기 구분, 사용자·hash/random·challenge/session·만료 결속, 공개 endpoint·rate limit·enumeration·local/external 상태 drift 공백을 유지했다.
- 민감정보: 변경된 wiki 추가행에서 credential assignment·private key 본문·access key·email·IP·URL·JWT literal 노출 지표 0개다. 실제 값은 출력하지 않았다.
- page count: actual 279 = index `Total pages` 279이며 신규 페이지가 없어 index 설명·수치는 변경하지 않았다.
- Git: 대상 tracked scope `git diff --check` 통과. line-ending 변환 안내는 있었으나 whitespace 오류는 없다.
- raw: 실제 파일 4개·170,194 bytes·Markdown 4,481줄, 0바이트·중복 0개다. 시작·종료 scoped status/diff는 0건이다.
- 정렬 SHA-256 manifest digest: `1d77c60dbfa22cf5f9173b897b1e0ddb0906b98ff9b543a1ba476d7b13d2a50f`로 세션 1 최종값과 동일하다.
- 단계 9 전체 상태: **최종 완료**. 단계 10 Python은 시작하지 않았고 Git commit·push도 수행하지 않았다.

## 관련 페이지

- [[_meta/wiki-content-rehighquality-work-plan|LLM Wiki 내용 재고도화 작업 계획]]
- [[_meta/cicd-rehighquality-inventory-plan|CI/CD 내용 재고도화 전수 재고와 실용형 실행 계획]]
- [[_meta/passwordless-rehighquality-inventory-plan|Passwordless 내용 재고도화 전수 재고와 실용형 실행 계획]]
- [[summaries/2026-05-middle-project-cicd-passwordless-guide|중간 프로젝트 CI/CD·배포·Passwordless 가이드]]
