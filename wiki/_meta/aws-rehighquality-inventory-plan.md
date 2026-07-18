---
title: AWS 내용 재고도화 전수 재고와 실용형 실행 계획
created: 2026-07-18
updated: 2026-07-18
type: meta
tags: [aws, linux, ci-cd, curriculum, study-log]
sources:
  - AGENTS.md
  - wiki/index.md
  - wiki/log.md
  - wiki/_meta/wiki-content-rehighquality-work-plan.md
  - wiki/_meta/linux-rehighquality-inventory-plan.md
  - raw/KoreaICT/6. AWS/AWS 총정리/AWS 총정리.md
status: stable
confidence: high
---

# AWS 내용 재고도화 전수 재고와 실용형 실행 계획

## 문서 상태와 범위

이 문서는 내용 재고도화 단계 6 `AWS`의 전수 재고·raw↔wiki 대응 기준선이자 실용형 2개 세션 실행 계획이다. Linux처럼 유형을 과도하게 분할하지 않고, 세션 1에서 재고와 핵심 Summary·Concept·Entity를 함께 고도화했다.

- 현재 상태: **세션 1~2 완료 — 단계 6 AWS 최종 완료**
- AWS 전체 상태: **완료**. Comparison·Query 판단과 직접 12페이지 전체 고정점을 통과했다.
- 다음 실행 단위: 단계 7 CI/CD. 이 문서에서는 후속 과목 본문을 시작하지 않는다.
- 단계 7 CI/CD: 05-11~13 원본과 12개 후속 페이지는 과목 경계 확인에만 사용했다.
- `raw/KoreaICT/6. AWS`: 읽기 전용

## 작업 전 기준선

- 직전 완료 단계: 단계 5 Linux 전체 고정점
- 시작 `raw/KoreaICT/6. AWS` scoped status: 0건
- 시작 `raw/KoreaICT/6. AWS` scoped diff: 0건
- 시작 시 AWS 핵심 페이지 일부에는 직전 Linux 후속 경계 교정이 누적돼 있었다. 그 변경을 보존하고 이번 세션에서 실제 raw와 다시 대조했다.
- 전체 저장소의 기존 변경은 이번 AWS 작업과 분리하며 복구·commit·push하지 않는다.

## raw 전수 재고 요약

- 실제 파일: **9개**, 총 **23,952,751 bytes**
- Markdown: **5개**
  - 날짜별 수업 MD 3개
  - AWS 총정리 MD 1개
  - 문서형 교육자료 MD 1개
- PDF: **4개**
- 이미지: **0개**
- 날짜별·총정리 MD: **1,427줄**
- 문서형 교육자료 MD: **27줄**
- 전체 MD: **1,454줄**
- 0바이트 파일: **0개**
- 과목 내부 byte-identical 중복: **0개**
- 다른 과목과의 byte-identical 중복: **1개**. P04는 `raw/KoreaICT/7. Ci&CD/교육 자료/cloud.03.AWS 교안(이론).pdf`와 동일하다.
- 독립 source/config/script/archive: **0개**. 명령·출력·SQL·properties는 날짜 MD 안에 있다.

## raw 식별자와 실제 전체 경로

날짜별·총정리 Markdown은 `R`, PDF·문서형 교육자료는 `P`, 이미지는 `I`로 나눈다. 현재 이미지는 없어 `I` 식별자는 없다.

### 날짜별 Markdown과 총정리

| ID | 실제 전체 경로 | 실제 수업일·역할 | 실제 자원·설정·오류·완료 조건 |
|---|---|---|---|
| R01 | `raw/KoreaICT/6. AWS/2026.05.06(수) - 시작/2026.05.06(수) - 시작.md` | 2026-05-06, AWS 첫날 | 1~6교시는 비어 있고 7~8교시에 AWS 메뉴·Security Group·Subnet·IPv4/CIDR을 읽었다. Route 53·RDS·ACM은 메뉴 이름이며 VPC·EC2 생성 결과가 아니다. |
| R02 | `raw/KoreaICT/6. AWS/2026.05.07(목)/2026.05.07(목).md` | 2026-05-07, VPC·EC2 실습 | On-Demand/On-Premise, Region/AZ, VPC·IGW·DNS·두 Subnet·Route Table·Security Group·Key Pair·EC2·EIP·MobaXterm SSH, 해제 순서. 5~8교시 반복 실습은 지시만 있고 반복별 최종 출력은 없다. |
| R03 | `raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md` | 2026-05-08, EC2 server·RDS 실습 | 두 EC2 `ping` 실패→ICMP Inbound 추가→양방향 0% loss는 출력으로 확인. Nginx·Spring Boot·RDS MySQL/client/SQL/JDBC·삭제는 명령·설정·완료 조건이 있으나 browser·build·query·application·최종 삭제 결과는 미보존. |
| R04 | `raw/KoreaICT/6. AWS/AWS 총정리/AWS 총정리.md` | 2026-05-06~08 복습 허브 | 날짜 흐름과 VPC/EC2/RDS/비용·정리 관계를 종합한다. 날짜별 실제 결과를 대체하지 않는다. |

### PDF·문서형 교육자료

| ID | 실제 전체 경로 | 형식 | 역할·경계 |
|---|---|---|---|
| P01 | `raw/KoreaICT/6. AWS/교육 자료/AWS 기초 용어.pdf` | PDF, 4쪽 | On-Demand/On-Premise 등 용어 보조. 수업일·리소스 성공 결과 근거로 쓰지 않는다. |
| P02 | `raw/KoreaICT/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf` | PDF, 11쪽 | AWS 메뉴와 VPC 기본 구성의 짧은 이론 보조자료 |
| P03 | `raw/KoreaICT/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf` | PDF, 312쪽 | VPC·EC2·RDS 콘솔 화면 절차 보조. 날짜 MD에 없는 실행 결과를 만들지 않는다. |
| P04 | `raw/KoreaICT/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf` | PDF, 249쪽 | network/cloud 이론 보조. CI/CD 과목의 동일 PDF와 byte-identical이다. |
| P05 | `raw/KoreaICT/6. AWS/교육 자료/실습 관리 대장(텍스트).md` | Markdown, 27줄 | VPC·Subnet·EC2·EIP와 CLB/ALB 예정 이름 표. 예정 표는 생성·응답 성공 증거가 아니며 CLB/ALB 실행은 05-12 CI/CD 원본으로 판정한다. |

## 직접 source 지식 페이지 재계산

frontmatter `sources`에 `raw/KoreaICT/6. AWS/`를 직접 가진 지식 페이지는 **12개**다. Meta 페이지는 제외한다.

- `summary 4`
- `concept 4`
- `entity 3`
- `comparison 1`
- `query 0`
- 디렉터리와 frontmatter `type` 불일치: 0개

### raw↔Summary 대응

| wiki 경로 | 주 raw·최초/확장일 | 분류·세션 1 결과 | 책임·완료 경계 |
|---|---|---|---|
| `wiki/summaries/2026-05-06-aws-cloud-vpc-ec2.md` | R01, 05-06 | 부분 보강 완료 | 메뉴·Subnet·SG·IPv4/CIDR 사전 학습만 보존. Region/AZ·On-Demand·리소스 생성은 R02로 이동해 소급 금지. |
| `wiki/summaries/2026-05-07-aws-ec2-nginx-rds.md` | R02, 05-07 | 부분 보강 완료 | VPC→IGW/DNS→Subnet/Route→SG/Key Pair→EC2/EIP/SSH와 정리 절차. Nginx·Spring·RDS는 R03. |
| `wiki/summaries/2026-05-08-aws-rds-resource-cleanup.md` | R03·R04, 05-08 | 전면 오류 교정 완료 | ping 성공 출력과 Nginx·Spring·RDS·JDBC·삭제의 절차/결과 미보존을 표로 분리. Route 53/ACM/ALB는 후속. |
| `wiki/summaries/2026-05-08-aws-subject-review.md` | R01~R04, 05-06~08 | 부분 보강 완료 | 날짜별 Summary를 대체하지 않는 복습 허브. 직접 성공 결과와 명령·완료 조건을 분리. |

### raw↔Concept 대응

| wiki 경로 | 주 raw·최초/확장일 | 분류·세션 1 결과 | 중심 책임·경계 |
|---|---|---|---|
| `wiki/concepts/aws-cloud-vpc-networking.md` | R01~R03, 05-06→08 | 부분 보강 완료 | VPC/Subnet/IGW/Route/SG/EIP 계층과 ICMP 오류 해결. Linux UFW·iptables 및 Docker network와 혼합 금지. |
| `wiki/concepts/aws-ec2-nginx-spring-deploy.md` | R03, 05-08; CI/CD 05-12 후속 | 전면 오류 교정 완료 | EC2 안의 Nginx·JDK/Maven·JAR·80→9000 절차와 미보존 결과. Target Group·ALB는 후속 source로 분리. |
| `wiki/concepts/aws-rds-spring-boot.md` | R03·R04, 05-08 | 전면 오류 교정 완료 | RDS 생성→SG/3306→MySQL client/SQL→datasource/JAR 단계. 실제 endpoint·계정·암호와 성공 출력 비노출. |
| `wiki/concepts/aws-resource-lifecycle-cost-management.md` | R02~R04, 05-07→08 | 부분 보강 완료 | EIP·EC2·RDS·SG·network 의존성 정리 순서와 최종 상태 미보존을 분리. |

### raw↔Entity 대응

| wiki 경로 | 주 raw·최초/확장일 | 분류·세션 1 결과 | 중심 책임·경계 |
|---|---|---|---|
| `wiki/entities/aws.md` | R01~R04, 05-06→08 | 부분 보강 완료 | AWS 3일 직접 이력과 05-12~13 CI/CD 후속 이력을 분리하는 platform 허브 |
| `wiki/entities/amazon-ec2.md` | R01~R03, 05-06→08 | 부분 보강 완료 | Ubuntu instance·SG·Key Pair·EIP·SSH·server 역할. Actions·ALB 대상은 CI/CD 후속. |
| `wiki/entities/amazon-rds.md` | R03, 05-08 | 부분 보강 완료 | MySQL 관리형 DB·endpoint·SG/3306·JDBC 역할과 결과 미보존. S3 역할 분리는 05-13 후속. |

### Comparison·Query 대응

| wiki 경로·후보 | 주 raw | 현재 분류 | 다음 세션 판단 |
|---|---|---|---|
| `wiki/comparisons/ec2-vs-rds.md` | R02~R04 | 전면 고도화 완료 | EC2 process 실행과 RDS data 계층, endpoint·3306·Security Group, 비용·삭제, 명령과 미보존 결과를 실제 선택 상황으로 교정했다. Multi-AZ·Read Replica는 직접 실습이 아닌 일반 기능으로 분리했다. |
| Query 신규 후보 | R02~R04 | **0개 유지 확정** | 독립 사용자 질문 기록이 없고 VPC·EC2 배포·RDS·lifecycle Concept와 `ec2-vs-rds`가 실제 혼동·troubleshooting·선택 기준을 모두 흡수한다. 별도 Query는 중복 탐색 경로가 되므로 만들지 않았다. |

## Linux 선행·AWS 직접·CI/CD 후속 경계

| 구간 | 직접 책임 | AWS와의 연결 |
|---|---|---|
| Linux 선행 | VirtualBox Ubuntu, SSH, UFW, Nginx, Maven JAR, `java -jar`, Linux `iptables` | EC2 안에서 재사용되는 OS·process·port 작업이다. VPC·Subnet·IGW·Route Table·SG·EIP·RDS 책임이 아니다. |
| AWS 05-06~08 직접 | VPC/Subnet/IGW/Route/SG, EC2/EIP/Key Pair/SSH, ICMP, Nginx·Spring 수동 절차, RDS/JDBC 절차, 비용·정리 | 출력으로 확인된 결과는 05-08 ICMP 전후가 핵심이다. 명령·설정만 있는 단계를 성공으로 확대하지 않는다. |
| CI/CD 05-11~13 후속 | GitHub Actions, Docker image 자동 배포, Route 53, ACM, Target Group, ALB, HTTPS, Terraform, S3 | AWS 서비스이지만 과목·수업일·성공 결과는 단계 7에 귀속한다. P05 예정 표나 05-06 메뉴를 직접 성공 근거로 쓰지 않는다. |

핵심 후속 경계 페이지는 `2026-05-11-cicd-github-actions-spring-boot`, `2026-05-12-route53-alb-https-review`, `2026-05-13-terraform-s3-file-upload`, `aws-route53-load-balancer-https`, `ci-cd-automation`, `github-actions-workflow`, `spring-boot-cicd-docker-ec2-flow`, `terraform-infrastructure-as-code`, `aws-s3-file-upload`, `amazon-route-53`, `amazon-s3`, `clb-vs-alb`다. 이 세션에서는 경계만 확인하고 단계 7 본문을 재고도화하지 않았다.

## code fence 재고와 처리

세션 시작의 직접 12페이지에는 fence **12개**가 있었다.

- `text 7`
- `bash 2`
- `shell 1`
- `properties 2`

대상 11개에 있던 diagram·명령·properties fence는 서로 떨어진 원문을 합치거나 placeholder로 일반화한 예제여서 실제 수업의 한 연속 실행처럼 보일 위험이 있었다. 핵심 흐름은 표·prose로 충분해 모두 제거했다. `ec2-vs-rds`에는 처음부터 fence가 없었다.

- 세션 1 최종 직접 페이지 fence: **0개**
- 원문 연속 대조 대상: **0개**
- PDF/image 수동 fence 예외: **0개**
- `bash` fence: **0개**
- 명령·출력·설명 혼합 또는 분리 unit 잔여: **0개**

## 민감정보와 식별자 경계

- R02~R03에는 실제 Public IP, private topology, Key Pair/resource 이름, repository URL, RDS endpoint, DB 계정·비밀번호가 있다.
- 세션 1 wiki 변경분에는 그 값을 옮기지 않고 resource 역할·port·완료 조건만 남겼다.
- `0.0.0.0/0`, 22·80·443·9000·3306, `/16`·`/24`는 protocol/학습 규칙 설명이며 실제 개인 식별값으로 취급하지 않는다.
- P05의 CLB/ALB 이름은 예정 표일 뿐 생성 결과가 아니므로 직접 성공 주장에 쓰지 않았다.

## 실용형 실행 계획

AWS는 총 **2개 세션**으로 완료한다.

| 세션 | 범위 | 대상 |
|---:|---|---|
| 1 | 재고 + 핵심 지식 고도화 | R01~R04·P01~P05 전수 재고, 직접 페이지 12개 재계산, Summary 4·Concept 4·Entity 3 고도화 |
| 2 | Comparison/Query + 과목 전체 고정점 | `ec2-vs-rds`, Query 0개 유지 판단, 직접 12페이지·후속 경계·index/log/meta·raw/Git 전체 검증, 단계 6 최종 완료 기록 |

## 세션 1 완료 결과

- raw 9개를 R01~R04·P01~P05에 빠짐없이 1회씩 대응했다.
- 직접 source 지식 페이지 12개를 `summary 4 / concept 4 / entity 3 / comparison 1 / query 0`으로 재계산했다.
- 지정 Summary 4·Concept 4·Entity 3을 실제 내용 공백과 과확정이 있는 부분만 고도화했다.
- 05-06 메뉴·이론, 05-07 VPC·EC2·EIP, 05-08 ICMP·Nginx·Spring·RDS를 날짜별로 분리했다.
- ping 출력 성공과 Nginx·Spring·RDS·JDBC·삭제의 명령/설정/완료 조건을 분리했다.
- Linux 선행 책임과 CI/CD 05-11~13 후속 책임을 AWS 직접 3일 결과와 분리했다.
- 새 지식 페이지·Comparison·Query는 만들지 않았다. 새 페이지는 이 Meta 1개뿐이다.
- 단계 6 AWS 전체는 미완료이며 상위 계획의 최종 완료 행을 갱신하지 않았다.

## 세션 2 최종 판단과 완료 고정점

- Comparison: `ec2-vs-rds`를 R02~R04 직접 흐름으로 고도화했다. EC2·RDS의 역할/관리 경계, EC2→RDS endpoint·3306 연결, 비용·삭제 조건, 실제 명령과 미보존 결과를 분리했고 실제 resource 이름·IP 대역·DB 이름을 일반화했다.
- Query: **신규 0개 유지**를 확정했다. 독립 사용자 질문이 없고 4개 Concept와 Comparison이 네트워크·배포·DB 연결·자원 정리의 반복 혼동을 이미 흡수한다.
- 직접 source 지식 페이지: `summary 4 / concept 4 / entity 3 / comparison 1 / query 0`, 총 12개를 재계산했다. R01~R04 source union 4/4, P01~P05 inventory 5/5, 미분류 0개다.
- 과목 경계: Linux 선행 8개와 CI/CD 05-11~13 후속 12개를 다시 읽어 Linux process/port, AWS network/compute/database, CI/CD automation·Route 53/ACM/ALB·Terraform/S3 책임을 분리했다. 단계 7 본문은 수정하지 않았다.
- 구조: 직접 12페이지의 frontmatter·type·status·confidence·허용 tag·source 실경로·깨진 링크·고립·index 등록 누락/중복·actionable placeholder·빈 sources·200줄 초과 오류는 모두 0개다. `needs-review`·`confidence: low`도 0개다.
- fence: 직접 12페이지는 최종 fence 0개, 원문 연속 대조·수동 예외·미처리 단위 0개, `bash` 0개다.
- 보안: 직접 12페이지에서 실제 account·email·Public/Private IP·RDS endpoint·Key Pair/resource 이름·DB 이름·password·token·credential·AWS identifier 노출 지표 0개를 확인했다. protocol 상수 `0.0.0.0/0`, port, `/16`·`/24`는 설명값으로 유지했다.
- page count: `wiki/**/*.md` 277개에서 `index.md`·`log.md`를 제외한 실제 page 수 275개이며 index `Total pages: 275`와 일치한다.
- raw: 9개·23,952,751 bytes, MD 1,454줄, 0바이트 0개, 과목 내부 중복 0개를 재확인했다. 시작·종료 scoped status/diff는 0건이고 정렬된 9개 SHA-256 manifest digest는 `b185d92d5866e27d1593681db97bbe8709059debdc3eef56527b5b220d51e2af`로 동일하다.
- Git: AWS 직접 12페이지와 기록 문서의 scoped `git diff --check`를 통과했다. commit·push는 수행하지 않았다.

## 관련 페이지

- [[_meta/wiki-content-rehighquality-work-plan|LLM Wiki 내용 재고도화 작업 계획]]
- [[_meta/linux-rehighquality-inventory-plan|Linux 내용 재고도화 전수 재고와 실행 분할 계획]]
- [[summaries/2026-05-08-aws-subject-review|AWS 총정리]]
- [[entities/aws|AWS]]
- [[concepts/aws-cloud-vpc-networking|AWS Cloud와 VPC 네트워킹]]
- [[concepts/aws-resource-lifecycle-cost-management|AWS 자원 생명주기와 비용 관리]]
