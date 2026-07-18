---
title: Spring Boot CI/CD Docker-EC2 배포 흐름
created: 2026-07-03
updated: 2026-07-18
type: concept
tags: [spring-boot, ci-cd, aws, backend]
sources:
  - raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md
  - raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md
  - raw/KoreaICT/7. Ci&CD/교육 자료/CI&CD(SpringBoot_실습).pdf
status: growing
confidence: high
---

# Spring Boot CI/CD Docker-EC2 배포 흐름

## 정의

Spring Boot CI/CD Docker-EC2 배포 흐름은 Spring Boot 애플리케이션을 jar로 빌드하고 Docker image로 패키징한 뒤, Docker Hub를 거쳐 AWS EC2에서 컨테이너로 실행하는 자동 배포 구조다.

## 왜 중요한가

이전에는 EC2에 직접 접속해 JDK/Maven을 설치하고 `mvn clean package`, `java -jar`를 수동으로 실행했다. CI/CD를 붙이면 push 한 번으로 같은 빌드·이미지 생성·배포 절차를 반복할 수 있어 중간 프로젝트 같은 팀 작업에서 실수를 줄일 수 있다.

## 전체 흐름

Spring Boot code를 push하면 GitHub Actions가 Maven build와 Docker image build/push를 맡고, 별도 CD workflow가 EC2 container 갱신을 맡는다. 이 책임 흐름은 날짜 원본의 설정과 절차를 재구성한 것이며, 원본에서 직접 확인 가능한 최종 실행 결과는 `docker container ps -a`의 `Up` 상태와 host 80 → container 9000 port mapping이다.

## 단계별 설명

### 1. Spring Boot 프로젝트 준비

- `MainController`에서 `/` 요청에 문자열을 반환한다.
- `application.properties`에서 `server.port=9000`을 설정한다.
- `pom.xml`에 Web/Thymeleaf 의존성을 추가하고 `<finalName>cicd</finalName>`으로 jar 이름을 고정한다.

### 2. CI: GitHub Actions에서 Maven build

기본 `ci.yml`에서 GitHub Actions runner가 JDK 21을 준비하고 `mvn clean package -DskipTests`를 실행하도록 정의한다. 여기서 실패하면 Docker image를 만들기 전에 문제를 발견할 수 있지만, 05-11 원본에는 실제 Maven 종료 log나 jar artifact 목록이 남아 있지 않다.

### 3. Docker image build/push

수업에서는 `ci.yml`에 Docker Hub login, `SpringDockerFile` 기반 image build, Docker Hub push 단계를 추가했다. Docker Hub token은 [[concepts/github-actions-secrets-deploy|GitHub Secrets]]로 분리한다.

### 4. CD: EC2에서 컨테이너 실행

EC2에는 Docker가 설치되어 있어야 한다. 별도 `cd.yml`이 EC2 배포를 연결하며, 날짜 원본에 workflow 전문은 없으므로 위키에서는 새 image pull과 기존 container 갱신이라는 역할만 기록한다. 실습에서는 `0.0.0.0:80->9000/tcp` 형태로 외부 80번 요청을 Spring Boot 9000번 컨테이너 포트로 연결했다.

## 명령·설정과 직접 결과

| 구간 | 원본 증거 | 완료 경계 |
|---|---|---|
| Maven CI | workflow와 build 명령 | job·artifact 결과 미보존 |
| Docker registry | login·build·push workflow | push 결과 미보존 |
| EC2 Docker 준비 | group·version 출력 | Docker 사용 준비 확인 |
| container | `ps -a` 출력 | 실행 중 상태와 port mapping 확인 |
| browser | 확인 URL | 응답·변경 화면 미보존 |

## 검증 포인트

- GitHub Actions run이 성공했는가?
- Docker Hub에 새 image tag가 올라갔는가?
- EC2에서 `docker container ps -a`에 새 container가 떠 있는가?
- Security Group이 80/9000 등 필요한 포트를 허용하는가?
- 브라우저에서 `/`, `/first`, `/second` 같은 URL이 실제로 응답하는가?

## 자주 헷갈리는 점

- Maven build 산출물(jar)과 Docker image는 다르다. jar는 애플리케이션 파일이고, Docker image는 실행 환경까지 묶은 템플릿이다.
- Docker Hub는 배포 서버가 아니라 image registry다. EC2가 Docker Hub에서 image를 pull해서 실행한다.
- EC2 접속 key, Docker token, image 이름, container 이름은 workflow 코드에 직접 쓰지 말고 Secrets로 관리한다.
- Load Balancer/Route 53/HTTPS 앞단과 이 컨테이너 배포 흐름은 서로 연결되지만 책임이 다르다. 컨테이너가 떠 있어야 ALB health check와 도메인 접속도 의미가 있다.

## 관련 개념

- [[summaries/2026-05-11-cicd-github-actions-spring-boot|2026-05-11 CI/CD, GitHub Actions, Spring Boot 자동 배포]]
- [[concepts/ci-cd-automation|CI/CD 자동화]]
- [[concepts/github-actions-workflow|GitHub Actions workflow]]
- [[concepts/github-actions-secrets-deploy|GitHub Actions Secrets 기반 배포]]
- [[concepts/aws-ec2-nginx-spring-deploy|AWS EC2에서 Nginx와 Spring Boot 배포]]
- [[concepts/middle-project-cicd-deploy-flow|중간 프로젝트 CI/CD 배포 흐름]]
- [[entities/docker|Docker]]
- [[entities/amazon-ec2|Amazon EC2]]

## 출처

- `raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md`
- `raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md`
- `raw/KoreaICT/7. Ci&CD/교육 자료/CI&CD(SpringBoot_실습).pdf`
