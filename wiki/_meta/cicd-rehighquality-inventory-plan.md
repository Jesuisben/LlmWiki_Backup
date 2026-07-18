---
title: CI/CD 내용 재고도화 전수 재고와 실용형 실행 계획
created: 2026-07-18
updated: 2026-07-18
type: meta
tags: [ci-cd, aws, linux, github, curriculum, study-log]
sources:
  - AGENTS.md
  - wiki/index.md
  - wiki/log.md
  - wiki/_meta/wiki-content-rehighquality-work-plan.md
  - wiki/_meta/aws-rehighquality-inventory-plan.md
  - raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md
  - raw/KoreaICT/7. Ci&CD/2026.05.12(화)/2026.05.12(화).md
  - raw/KoreaICT/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md
  - raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md
status: stable
confidence: high
---

# CI/CD 내용 재고도화 전수 재고와 실용형 실행 계획

## 문서 상태와 범위

이 문서는 내용 재고도화 단계 7 `Ci&CD`의 전수 재고·raw↔wiki 대응 기준선이자 실용형 2개 세션 완료 기록이다. 세션 1에서 전수 재고와 핵심 Summary·Concept·Entity를 교정하고, 세션 2에서 Comparison·Query 최종 판단과 직접 19페이지 전체 고정점을 완료했다.

- 현재 상태: **세션 1~2 완료 — 단계 7 CI/CD 최종 완료**
- 세션 1: raw 전수 재고, 직접 source 지식 페이지 재계산, Summary 3·Concept 9·Entity 6 고도화
- 세션 2: 기존 Comparison 최종 고도화, 신규 Comparison·Query 0개 확정, 직접 19페이지 전체 고정점
- 단계 8 Passwordless 본문: 시작하지 않음
- `raw/KoreaICT/7. Ci&CD`: 읽기 전용

## 작업 전 기준선

- 직전 완료 단계: 단계 6 AWS 전체 고정점
- 시작 `raw/KoreaICT/7. Ci&CD` scoped status: 0건
- 시작 `raw/KoreaICT/7. Ci&CD` scoped diff: 0건
- 시작 정렬 SHA-256 manifest digest: `c1facebda686016a17322d4d65c09c40ab880b968d032189a5fac2c92ceceff1`
- 저장소 전체에는 이전 Linux/AWS 고도화와 Python raw 사용자 변경이 이미 존재했다. 이번 CI/CD 작업은 이를 복구·commit·push하지 않고 대상 범위만 수정했다.

## raw 전수 재고 요약

- 실제 파일: **8개**, 총 **23,226,472 bytes**
- Markdown: **4개**
  - 날짜별 수업 MD 3개
  - CI/CD 총정리 MD 1개
- PDF·교육자료: **4개**
- 독립 source/config/script: **0개**
  - Java·properties·XML·YAML·shell·HCL·JSON·SQL은 날짜 MD·총정리 안에 포함되어 있다.
- 이미지·기타 artifact: **0개**
- Markdown 전체: **1,466줄**
- 0바이트 파일: **0개**
- 과목 내부 byte-identical 중복: **0개**
- 다른 과목과의 byte-identical 중복: **1개**
  - P04는 `raw/KoreaICT/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf`와 동일하다.

## raw 식별자와 실제 전체 경로

### 날짜별 Markdown과 총정리
| ID | 실제 전체 경로 | bytes | 줄 | 역할·결과 경계 |
|---|---|---:|---:|---|
| R01 | `D:\Study_LLM_Wiki\raw\KoreaICT\7. Ci&CD\2026.05.11(월) - 시작\2026.05.11(월) - 시작.md` | 13,487 | 438 | CI/CD 이론→Spring Boot/Maven→GitHub Actions→Docker Hub/Secrets→EC2 CD. `groups`·Docker version·실행 중 container/port 출력은 보존되지만 Actions build·image push·browser 응답은 미보존이다. |
| R02 | `D:\Study_LLM_Wiki\raw\KoreaICT\7. Ci&CD\2026.05.12(화)\2026.05.12(화).md` | 6,923 | 230 | Route 53 hosted zone·NS, ACM DNS 검증, Nginx 두 EC2, Target Group·ALB·HTTPS Listener·Alias 절차. 확인 URL은 있으나 DNS/인증서/target health/browser 결과와 삭제 완료는 미보존이다. |
| R03 | `D:\Study_LLM_Wiki\raw\KoreaICT\7. Ci&CD\2026.05.13(수)\2026.05.13(수).md` | 12,593 | 372 | Terraform 설치·HCL·IAM·plan/apply/destroy와 S3/RDS 업로드. Terraform version 출력은 보존되고 apply 오류·수정 절차는 있으나 최종 성공은 없다. S3 첫 실패→policy 수정→재시도 성공·bucket object 확인은 수업 메모의 관찰 서술이며 listing·응답·화면은 없고 RDS query 결과도 없다. |
| R04 | `D:\Study_LLM_Wiki\raw\KoreaICT\7. Ci&CD\Ci&CD 총정리\Ci&CD 총정리.md` | 19,082 | 426 | 05-11~13 복습 허브. 날짜별 직접 결과를 대체하지 않으며, 일부 placeholder configuration·정규화된 예시는 source 성공 증거로 쓰지 않는다. |

### PDF·교육자료
| ID | 실제 전체 경로 | bytes | PDF page count | 역할·경계 |
|---|---|---:|---:|---|
| P01 | `D:\Study_LLM_Wiki\raw\KoreaICT\7. Ci&CD\교육 자료\CI&CD(SpringBoot_실습).pdf` | 2,019,860 | 66 | Spring Boot·GitHub Actions·Docker/EC2 CI/CD 화면 절차 보조. 날짜 원본에 없는 job·browser 성공 결과를 만들지 않는다. |
| P02 | `D:\Study_LLM_Wiki\raw\KoreaICT\7. Ci&CD\교육 자료\CI&CD(SpringBoot_이론).pdf` | 3,136,230 | 40 | Automation·CI/CD·Secret 등 개념 보조. 실제 수업일 실행 결과 근거가 아니다. |
| P03 | `D:\Study_LLM_Wiki\raw\KoreaICT\7. Ci&CD\교육 자료\cloud.02.AWS 교안(실습).pdf` | 10,392,256 | 280 | Route 53/ACM/ALB·Terraform·S3/RDS console 절차 보조. 날짜 MD의 결과 경계를 우선한다. |
| P04 | `D:\Study_LLM_Wiki\raw\KoreaICT\7. Ci&CD\교육 자료\cloud.03.AWS 교안(이론).pdf` | 7,626,041 | 249 | Cloud·load balancing·Terraform 이론 보조. AWS 과목 P04와 byte-identical이며 중복 사본을 별도 실행 증거로 세지 않는다. |

## 날짜별 수업 책임과 미보존 결과 경계

| 날짜 | 직접 범위 | 보존된 출력·관찰 서술 | 명령·설정·확인 절차만 보존 |
|---|---|---|---|
| 05-11 | GitHub Actions/Maven CI, Docker image/registry, EC2 container CD | Docker group·version, container `Up`, host 80→container 9000 mapping | Actions job, Maven artifact, image push, SSH CD log, browser 변경 응답 |
| 05-12 | Route 53/NS, ACM/CNAME, Target Group, ALB, HTTPS Listener, Alias | 별도 실행 출력 없음 | DNS 전파, 인증서 발급 상태, Nginx 응답, target health, ALB 상태, HTTP/HTTPS 응답, 자원 삭제 |
| 05-13 | Terraform/IaC, S3 object upload, RDS 상품 데이터 역할 분리 | Terraform version 출력; S3 실패·재시도 성공·bucket object 확인의 관찰 서술 | init log, 최종 plan/apply 성공, destroy 완료, S3 listing·응답·화면, RDS query 결과 |

## 직접 source 지식 페이지 재계산

frontmatter `sources`에 `raw/KoreaICT/7. Ci&CD/`를 직접 가진 지식 페이지는 **19개**다. Meta 페이지는 제외했다.

- `summary 3`
- `concept 9`
- `entity 6`
- `comparison 1`
- `query 0`
- 디렉터리와 frontmatter `type` 불일치: 0개

### raw↔Summary 대응
| wiki 경로 | 주 raw | 세션 1 분류·처리 | 책임·결과 경계 |
|---|---|---|---|
| `wiki/summaries/2026-05-11-cicd-github-actions-spring-boot.md` | R01·R04·P01·P02 | 부분 보강 완료 | workflow 정의, Docker/EC2 설정과 보존된 container 결과를 분리하고 합성 diagram/YAML을 제거했다. |
| `wiki/summaries/2026-05-12-route53-alb-https-review.md` | R02·R04·P03·P04 | 부분 보강 완료 | console 구성 절차와 DNS/ACM/target/browser 결과 미보존을 분리하고 합성 diagram을 제거했다. |
| `wiki/summaries/2026-05-13-terraform-s3-file-upload.md` | R03·R04·P03·P04 | 전면 오류 교정 완료 | Terraform apply 오류·미보존 성공, S3 재시도 성공, RDS query 미보존을 분리하고 합성 HCL/data-flow fence를 제거했다. |

### raw↔Concept 대응
| wiki 경로 | 주 raw | 세션 1 분류·처리 | 중심 책임·경계 |
|---|---|---|---|
| `wiki/concepts/ci-cd-automation.md` | R01·R04·P02 | 부분 보강 완료 | CI/image/CD/service 완료 상태를 나누고 container만 직접 보존 결과로 고정했다. |
| `wiki/concepts/github-actions-workflow.md` | R01·R04·P01 | 부분 보강 완료 | workflow 구조와 Actions job 결과를 분리하고 비연속 축약 YAML을 제거했다. |
| `wiki/concepts/github-actions-secrets-deploy.md` | R01·R04·P01, 단계 9 후속 | 부분 보강 완료 | Secret 역할과 배포 성공을 분리하고 합성 YAML을 제거했다. 단계 9 값·설계는 후속 경계로 유지했다. |
| `wiki/concepts/spring-boot-cicd-docker-ec2-flow.md` | R01·R04·P01 | 부분 보강 완료 | Maven·registry·EC2·browser 상태를 분리하고 합성 diagram을 제거했다. |
| `wiki/concepts/aws-route53-load-balancer-https.md` | R02·R04 | 전면 오류 교정 완료 | DNS→ALB→EC2와 RDS data 계층을 분리하고 실제 resource 이름·합성 diagram·성공 과확정을 제거했다. |
| `wiki/concepts/terraform-infrastructure-as-code.md` | R03·R04·P03·P04 | 전면 오류 교정 완료 | syntax example과 실제 `main.tf`를 분리하고 version/apply 오류/destroy prompt·미보존 결과를 복원했다. |
| `wiki/concepts/aws-s3-file-upload.md` | R03·R04·P03 | 전면 오류 교정 완료 | S3 성공과 RDS 미확정을 분리하고 합성 data-flow/properties fence를 제거했다. |
| `wiki/concepts/aws-ec2-nginx-spring-deploy.md` | AWS 05-08, R02 후속 | 최소 경계 교정 완료 | Linux/AWS 수동 서버와 CI/CD ALB 절차를 분리하고 target/browser 결과 미보존을 명시했다. |
| `wiki/concepts/middle-project-cicd-deploy-flow.md` | R01·P01, 단계 9 후속 | 최소 경계 교정 완료 | 05-11 단일 Spring 실습과 React/JWT/S3 프로젝트 설계를 분리하고 합성 workflow를 제거했다. |

### raw↔Entity 대응
| wiki 경로 | 주 raw | 세션 1 분류·처리 | 중심 책임·경계 |
|---|---|---|---|
| `wiki/entities/amazon-route-53.md` | R02·R04 | 부분 보강 완료 | NS/CNAME/Alias 절차와 실제 DNS/browser 결과 미보존을 분리했다. |
| `wiki/entities/amazon-s3.md` | R03·R04·P03 | 부분 보강 완료 | EC2/RDS/S3 책임과 S3 직접 성공·RDS 미확정을 구분하고 합성 diagram을 제거했다. |
| `wiki/entities/amazon-ec2.md` | AWS 직접 raw, R01·R02 후속 | 최소 경계 교정 완료 | container 직접 출력과 ALB target/browser 미보존을 구분했다. |
| `wiki/entities/amazon-rds.md` | AWS 05-08, R03 후속 | 최소 경계 교정 완료 | S3 object 성공과 RDS query 미보존을 분리했다. |
| `wiki/entities/aws.md` | AWS 직접 raw, R02·R03 후속 | 최소 경계 교정 완료 | AWS 직접 3일과 CI/CD 05-12~13의 절차·결과를 분리했다. |
| `wiki/entities/github.md` | Java/Linux 직접 raw, R01 후속 | 최소 경계 교정 완료 | remote/PR와 Actions/Secrets 책임, workflow 정의와 job 결과를 분리했다. |

### Comparison·Query 대응과 다음 세션 후보

| wiki 경로·후보 | 주 raw | 최종 판단 | 근거 |
|---|---|---|---|
| `wiki/comparisons/clb-vs-alb.md` | R02·R04·P04 | **유지·최종 고도화** | CLB 예정 항목과 ALB 구성 절차, 일반 path/host routing·Health Check, 미보존 target/DNS/HTTP 결과를 근거 수준별로 분리해 독립 비교 책임을 확정했다. |
| `Route 53 vs ALB` Comparison 후보 | R02·R04 | **신규 생성 안 함** | DNS name resolution과 HTTP/HTTPS 처리 차이는 중요하지만 `aws-route53-load-balancer-https`와 05-12 Summary가 역할·장애 확인 위치를 이미 직접 소유한다. 원본 반복 혼동이 한 수업 흐름을 넘지 않아 새 탐색 경로는 중복이다. |
| `S3 vs RDS` Comparison 후보 | R03·R04 | **신규 생성 안 함** | object와 row, bucket object 성공과 RDS query 미보존 경계는 `aws-s3-file-upload`와 S3/RDS Entity가 이미 소유한다. 별도 비교는 같은 05-13 설명을 반복한다. |
| `CI/CD 자동화 vs Terraform IaC` Comparison 후보 | R01·R03·R04 | **신규 생성 안 함** | application build/image/deploy와 infrastructure lifecycle 차이는 `ci-cd-automation`·`terraform-infrastructure-as-code`의 정의·중요성·상호 링크로 충분히 검색된다. |
| 기존 페이지 흡수 후보 | R01~R04 | **모두 신규 생성 안 함** | `CI vs CD`, `plan vs apply vs destroy`, `ci.yml vs cd.yml`, Maven JAR/Docker image, Docker Hub/EC2, CNAME/Alias, Target Group/ALB, ACM/ALB는 각 Concept·Entity·기존 Comparison의 책임으로 흡수한다. 특히 `cd.yml` 전문과 여러 실행 결과가 없어 새 비교가 근거를 늘리지 못한다. |
| “Actions가 성공해도 서비스가 안 보이는 이유” Query 후보 | R01·R02 | **신규 생성 안 함** | Actions run→registry image→EC2 container/port→Security Group→Target Group health→ALB Listener/ACM→Route 53 진단 순서는 유용하지만 실제 장애 질문·해결 이력이 완전히 보존되지 않았다. 임의 Query 생성 금지 기준에 따라 0개를 유지한다. |
| 기타 Query | R01~R04 | **0개 유지 확정** | 독립 사용자 질문이 없고 기존 Concept·Summary가 보존된 혼동과 완료 조건을 흡수한다. |

## 과목 경계

| 구간 | 직접 책임 | CI/CD와의 연결 |
|---|---|---|
| Linux 선행 | Git/GitHub 협업, Maven/JAR, Docker 설치·권한·image/container, process/service/port | CI/CD runner·EC2에서 재사용되는 실행 기반이다. Actions·AWS managed resource의 책임이 아니다. |
| AWS 05-06~08 직접 | VPC/Subnet/IGW/Route/SG, EC2/EIP/SSH, ICMP, Nginx·Spring·RDS 수동 절차, 비용·정리 | CI/CD가 배포할 cloud 기반이지만 05-12~13 결과를 AWS 직접 날짜에 소급하지 않는다. |
| CI/CD 05-11~13 직접 | Actions/Maven·Docker image·EC2 CD, Route 53/ACM/Target Group/ALB/HTTPS, Terraform/S3 | 이번 단계의 직접 범위다. 명령·설정과 실제 출력·결과를 분리한다. |
| Passwordless 후속 | X1280·AAM/APE·FilingBox·REST API 인증 흐름 | 도메인·HTTPS·server 운영이 배경이지만 인증 제품 학습을 CI/CD 결과로 섞지 않는다. |
| 중간 프로젝트 후속 | React/Nginx proxy, JWT/DB/S3 Secrets, 프로젝트 배포 설계 | 05-11 단일 Spring 실습의 확장이며 단계 9에서 별도 고도화한다. |

## code fence 재고와 처리

세션 시작의 직접 19페이지에는 fence **18개**가 있었다.

- 원본 Markdown의 정규화된 연속 단위와 일치: **3개**
- 비연속 축약·합성 diagram/config/workflow: **15개**
- `bash` fence: **0개**

세션 1에서 Summary·Concept·Entity의 비연속 fence 15개를 prose·table로 바꾸고, 원본 연속 단위인 YAML 1개와 XML 2개만 유지했다.

- 세션 1 종료 직접 페이지 fence: **3개**
- 원문 연속 대조: **3/3 일치**
- 수동/PDF 예외: **0개**
- `bash` fence: **0개**
- 명령·설명 혼합 또는 불필요하게 분리된 code unit: **0개**

Comparison은 민감 resource 이름과 성공 과확정만 최소 교정했으며 원래 fence가 없다. 비교 구조의 최종 고도화 판단은 세션 2에 남겼다.

## 민감정보와 식별자 경계

- R01~R03에는 실제 account·email·repository URL·Public/Private IP·domain·endpoint·Key Pair/resource 이름·password·token·credential·AWS identifier가 있다.
- 세션 1의 wiki 변경분에는 해당 값을 옮기지 않고 역할·port·완료 조건만 남겼다.
- `master`, Java/JDK version, protocol port, `/16`·`/24`, `0.0.0.0/0`, `0.0.0.0:80->9000/tcp` 같은 학습 규칙은 개인 식별값과 구분한다.
- 원본에 있는 실제 resource 이름은 wiki에서 generic role로 바꾸고, 원본을 다시 출력하지 않는다.

## 실용형 실행 계획

CI/CD는 총 **2개 세션**으로 완료한다.

| 세션 | 범위 | 대상 |
|---:|---|---|
| 1 | 재고 + 핵심 지식 고도화 | R01~R04·P01~P04 전수 재고, 직접 페이지 19개 재계산, Summary 3·Concept 9·Entity 6 고도화 |
| 2 | Comparison/Query + 과목 전체 고정점 | `clb-vs-alb`, 후보 4건 최종 판단, 직접 19페이지·과목 경계·index/log/meta·raw/Git 전체 검증, 단계 7 최종 완료 기록 |

## 세션 1 완료 결과

- raw 8개를 R01~R04·P01~P04에 빠짐없이 1회씩 대응했다.
- 직접 source 지식 페이지 19개를 `summary 3 / concept 9 / entity 6 / comparison 1 / query 0`으로 재계산했다.
- Summary 3·Concept 9·Entity 6을 내용 공백·날짜 귀속·성공 과확정·source 불일치·합성 fence가 있는 범위만 고도화했다. 종료 후 독립 감사로 확인한 본문 출처 목록 13건과 AWS→Passwordless 무출처 확장, ALB 일반 기능의 직접 근거 혼합도 추가 교정했다.
- 05-11 CI/CD container 출력, 05-12 전부 절차/미보존 결과, 05-13 Terraform version 출력·apply 오류·S3 재시도 성공 관찰 서술·RDS query 미보존을 분리했다.
- Linux 선행, AWS 05-06~08 직접, CI/CD 직접, Passwordless·중간 프로젝트 후속 책임을 분리했다.
- 새 지식 페이지·Comparison·Query는 만들지 않았다. 새 페이지는 이 Meta 1개뿐이다.
- 단계 7 전체는 미완료이며 상위 계획의 단계 7 완료 행을 추가하지 않았다.

## 세션 2 최종 판단과 완료 고정점

- Comparison: `clb-vs-alb`를 유지하고 최종 고도화했다. CLB는 관리 표의 예정 항목만, ALB는 Target Group·Listener·ACM·Alias 구성 절차만 직접 근거로 두었으며 path/host routing·Health Check는 일반 기능으로 분리했다. target health·DNS 조회·HTTP/HTTPS 응답·browser 화면은 미보존 상태다.
- 신규 Comparison: Route 53/ALB, S3/RDS, CI/CD/Terraform과 기존 페이지 흡수 후보는 모두 새 페이지를 만들지 않았다. 기존 Summary·Concept·Entity·Comparison이 검색 책임을 소유하고, 원본의 반복 혼동·독립 실행 증거가 새 페이지를 정당화할 만큼 추가되지 않는다.
- Query: 실제 장애 질문·해결 이력이 완전히 보존되지 않아 신규 **0개 유지**를 확정했다. 단계별 진단 순서를 임의 사용자 질문으로 만들지 않았다.
- 직접 source 지식 페이지: frontmatter 기준 `summary 3 / concept 9 / entity 6 / comparison 1 / query 0`, 총 19개다. R01~R04·P01~P04 source union 8/8, 미분류 0개이며 별도 CI/CD 총정리 Summary는 `ci-cd-automation` 허브와 날짜 Summary 3개가 책임을 충족해 만들지 않았다.
- 날짜 결과: 05-11은 Docker group/version과 실행 중 container·80→9000 mapping 출력, 05-12는 독립 실행 결과 0개, 05-13은 Terraform version 출력과 apply 오류·S3 첫 실패→policy 수정→재시도 성공·bucket object 확인의 관찰 서술을 유지했다. 나머지 Actions/JAR/image/SSH/browser, DNS/ACM/target/ALB/삭제, 최종 apply/destroy·plan/state/lock, S3 listing·응답·화면, RDS query 결과는 미보존이다.
- 과목 경계: Linux 선행, AWS 05-06~08 직접, CI/CD 05-11~13 직접, Passwordless·중간 프로젝트 후속을 분리했다. AWS·CI/CD source만 가진 페이지에 Passwordless/X1280 결과를 확장하지 않았으며 단계 8 본문은 수정하지 않았다.
- 구조·보안: 직접 19페이지의 frontmatter·source 실경로·본문 출처 동기화·허용 tag·wikilink·index·고립·actionable placeholder·빈 sources·200줄 초과·needs-review/low-confidence 오류 0개다. 실제 page 수와 index `Total pages`는 276/276이다.
- fence: YAML 1개·XML 2개, 총 3개를 raw 연속 단위와 대조해 3/3 일치했고 `bash`는 0개다. 원본에 독립 Java/YAML/HCL/shell/HTML/image/JAR/plan/log/screenshot artifact가 없다는 경계를 유지했다.
- raw/Git: 시작과 종료의 `raw/KoreaICT/7. Ci&CD` scoped status/diff는 0건이며 정렬된 8개 SHA-256 manifest digest `c1facebda686016a17322d4d65c09c40ab880b968d032189a5fac2c92ceceff1`가 동일하다. CI/CD 변경 범위의 `git diff --check`를 통과했고 commit·push는 수행하지 않았다.
- 비동기 독립 감사 반영: S3 성공을 출력·화면이 있는 1차 결과처럼 읽힐 수 있던 Summary·Concept·Entity·inventory를 `수업 메모의 실행 관찰 서술`로 낮추고, `-DskipTests`가 테스트 통과가 아니라 테스트 생략 package 절차임을 명시했다. Comparison 감사의 S3/RDS·CI/CD/Terraform 신설 권고는 기존 페이지가 검색 책임을 흡수하고 반복 혼동 근거가 부족하다는 생성 기준에 따라 채택하지 않았다. `clb-vs-alb` 흡수 권고는 P04 일반 이론을 출처에 추가하고 직접 범위를 축소하며 `confidence: medium`으로 낮춘 현재 독립 역할이 남는다고 판단해 유지했다.
- 단계 상태: 단계 7 CI/CD를 최종 완료로 확정했다. 다음 작업 단위는 단계 8 Passwordless 실용형 첫 세션이며 이 세션에서는 시작하지 않았다.

## 관련 페이지

- [[_meta/wiki-content-rehighquality-work-plan|LLM Wiki 내용 재고도화 작업 계획]]
- [[_meta/aws-rehighquality-inventory-plan|AWS 내용 재고도화 전수 재고와 실용형 실행 계획]]
- [[summaries/2026-05-11-cicd-github-actions-spring-boot|2026-05-11 CI/CD, GitHub Actions, Spring Boot 자동 배포]]
- [[summaries/2026-05-12-route53-alb-https-review|2026-05-12 Route 53, ALB, HTTPS 복습과 도메인 배포]]
- [[summaries/2026-05-13-terraform-s3-file-upload|2026-05-13 Terraform과 S3 파일 업로드]]
- [[concepts/ci-cd-automation|CI/CD 자동화]]
- [[concepts/github-actions-workflow|GitHub Actions workflow]]
- [[concepts/terraform-infrastructure-as-code|Terraform과 Infrastructure as Code]]
- [[concepts/aws-s3-file-upload|AWS S3 파일 업로드 흐름]]
