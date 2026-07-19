---
title: 중간 프로젝트 CI/CD 배포 흐름
created: 2026-07-03
updated: 2026-07-19
type: concept
tags: [project, ci-cd, aws, spring-boot, react]
sources:
  - raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md
  - raw/KoreaICT/7. Ci&CD/교육 자료/CI&CD(SpringBoot_실습).pdf
  - raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md
  - raw/KoreaICT/9. 중간 프로젝트 공부/CICD/Github_Secrets 예시.md
status: growing
confidence: medium
---

# 중간 프로젝트 CI/CD 배포 흐름

## 정의

중간 프로젝트 CI/CD 배포 흐름은 GitHub 저장소의 변경을 기준으로 빌드, Docker image 생성/전송, 서버 반영, 서비스 확인을 자동화하는 절차다. 2026-05-11 수업의 Spring Boot 단일 프로젝트 CI/CD 실습이 중간 프로젝트 배포 가이드의 기반이 된다.

## 왜 중요한가

수동 배포는 파일 누락, 서버 명령 실수, 환경 변수 노출 위험이 크다. CI/CD를 쓰면 같은 절차를 반복 가능하게 만들고, 팀 프로젝트에서 “내 PC에서는 됨” 문제를 줄일 수 있다.

## 핵심 설명

- **코드 저장소**: GitHub가 변경 이력과 workflow 실행의 출발점이다.
- **백엔드 준비**: Spring Boot의 일부 설정을 배포 환경에서 주입하도록 설명하고 Dockerfile로 image 빌드 단위를 준비한다. 다만 가이드의 DB URL 직접값과 CD가 주입하는 DB URL 환경변수 사이에 실제 소비 표현이 맞지 않아, 모든 DB 설정이 주입된다고 확정할 수 없다. React는 정적 파일 또는 프론트엔드 산출물로 준비된다. ^[raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md]
- **Registry 단계**: Spring Boot Docker image는 Docker Hub 같은 registry에 push할 수 있다.
- **Secrets 단계**: Docker Hub 인증, backend/frontend image, EC2 host/key, DB 연결, JWT 키, S3 접근 항목은 역할별 GitHub Secrets로 분리하고 workflow 파일에는 실제 값을 쓰지 않는다. ^[raw/KoreaICT/9. 중간 프로젝트 공부/CICD/Github_Secrets 예시.md]
- **CI와 CD의 분리**: CI는 빌드한 Docker image를 Docker Hub에 push하고, CD는 EC2에서 새 image를 받아 기존 container를 갱신한다. ^[raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md]
- **프론트·확장 단계**: React의 `/api` 요청을 Nginx proxy로 백엔드에 연결하고, 파일 저장소는 S3로 전환하며, 이후 도메인 하나로 서비스 접점을 확장한다. ^[raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md]
- **확인 단계**: Actions job, application build, image push, 원격 container, API/browser, DB/object storage, DNS/HTTPS를 같은 성공 상태로 묶지 않고 각각 확인한다.

## 가이드가 제시한 배포 완료 사다리

| 단계 | 문서에 보존된 것 | 프로젝트 완료 증거 |
|---|---|---|
| source/config | properties·Java/XML·Dockerfile·TypeScript·Nginx·YAML snippet | 실제 repository file과 local test |
| CI | backend/frontend workflow template와 test 생략 package 설정 | 별도 test report, job log, build artifact, image digest |
| Registry | image 이름과 push 절차 | registry에서 확인한 version/tag/digest |
| CD | server 접속과 container 교체 절차 | 원격 log, 새 container·port 상태 |
| Application | API·browser 확인 위치 | 실제 HTTP status/body와 화면 관찰 |
| Data/File | DB 연결·multipart·S3 전환 설계 | query row, object, application response |
| Cloud edge | DNS·certificate·Target Group·ALB 절차 | 발급 상태, healthy target, DNS/HTTPS 응답 |

현재 단계 9 raw는 표의 두 번째 열에 해당하는 설계 문서와 embedded snippet을 제공한다. 세 번째 열의 완료 증거는 독립 artifact로 보존하지 않는다. 일부 짧은 성공·연결 관찰 서술은 있지만 log·응답·listing을 동반한 end-to-end 증거와 구분한다.

## DB 토폴로지와 설정 불일치

선행 AWS 수업은 관리형 DB를 다뤘지만, 단계 9 가이드의 상세 절차는 VM 내부 DB container와 SSH tunnel 접속을 사용한다. 문서 초반의 관리형 DB 계획과 세부 절차가 섞여 있어 중간 프로젝트가 최종 채택한 토폴로지는 raw만으로 확정할 수 없다.

또한 application 설정의 DB URL은 직접값으로 적혀 있는 반면 CD workflow는 별도 DB URL 환경변수를 주입한다. 제시된 설정에서 그 환경변수를 소비하는 연결이 보이지 않으므로, Secret을 등록·전달했다는 사실과 application이 실제로 읽었다는 사실을 분리해야 한다.

## 수업 직접 범위와 프로젝트 후속 범위

05-11 직접 수업은 Spring Boot 단일 실습의 `master` push·Maven·Docker Hub·EC2 container 흐름을 다뤘다. React build, Nginx `/api` proxy, 프로젝트 DB/JWT/S3 Secret 조합은 `raw/KoreaICT/9. 중간 프로젝트 공부/`의 후속 설계다. 두 범위를 한 workflow가 그날 실행된 것처럼 합성하지 않는다.

Linux의 Docker·Nginx와 AWS의 VPC·EC2·RDS는 선행 기반이고, CI/CD 05-11~13은 자동화·DNS/HTTPS·S3를 직접 학습한 구간이다. 단계 9는 이 지식을 중간 프로젝트 요구사항으로 조립한 **가이드 범위**다. 선행 과목의 제한된 성공 결과를 단계 9 배포 성공으로 복사하지 않는다.

## 자주 헷갈리는 점

- workflow YAML에는 Secret **값**이 아니라 `${{ secrets.NAME }}` 같은 참조만 남긴다.
- EC2 접속 정보와 RDS 접속 정보는 역할이 다르다.
- 배포 성공은 Actions 성공 표시만 보지 말고 실제 서비스 URL/API 응답까지 확인해야 한다.
- 05-11 수업의 실습용 Docker token, EC2 IP, key 값은 학습 원본에 있어도 wiki와 저장소에는 재노출하지 않는다.
- `Dockerfile`·workflow·Nginx snippet이 문서에 있다는 사실은 해당 파일이 실제 프로젝트에 존재한다는 뜻이 아니다.
- container `Up`, target health, browser 응답, DB row, S3 object는 각각 독립 완료 상태다.
- 가이드의 file service에는 object 삭제 호출이 있으나 뒤 설명은 object storage 삭제가 되지 않는다고 적어 서로 충돌한다. 실제 source와 실행 결과가 없으므로 어느 쪽이 최종 구현인지 확정하지 않는다.
- 교육용 절차의 광범위한 port 공개·공개 registry/object·장기 credential·container 환경변수 주입은 운영 기본값으로 복사하지 않는다. 최소 network scope, private object, 단기 credential·workload role, key rotation을 별도로 설계한다.

## 관련 개념

- [[concepts/github-actions-secrets-deploy|GitHub Actions Secrets 기반 배포]]
- [[concepts/ci-cd-automation|CI/CD 자동화]]
- [[concepts/github-actions-workflow|GitHub Actions workflow]]
- [[concepts/spring-boot-cicd-docker-ec2-flow|Spring Boot CI/CD Docker-EC2 배포 흐름]]
- [[concepts/aws-s3-file-upload|AWS S3 파일 업로드 흐름]]
- [[concepts/aws-ec2-nginx-spring-deploy|AWS EC2에서 Nginx와 Spring Boot 배포]]
- [[entities/github|GitHub]]

## 출처

- `raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md`
- `raw/KoreaICT/7. Ci&CD/교육 자료/CI&CD(SpringBoot_실습).pdf`
- `raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md`
- `raw/KoreaICT/9. 중간 프로젝트 공부/CICD/Github_Secrets 예시.md`
