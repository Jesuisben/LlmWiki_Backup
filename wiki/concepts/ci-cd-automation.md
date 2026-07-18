---
title: CI/CD 자동화
created: 2026-07-03
updated: 2026-07-18
type: concept
tags: [ci-cd, backend, curriculum]
sources:
  - raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md
  - raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md
  - raw/KoreaICT/7. Ci&CD/교육 자료/CI&CD(SpringBoot_이론).pdf
status: growing
confidence: high
---

# CI/CD 자동화

## 정의

CI/CD는 코드 변경이 들어왔을 때 빌드·검증·패키징·배포 절차를 자동화해, 개발자가 매번 같은 명령을 수동으로 반복하지 않게 만드는 개발/운영 흐름이다.

## 왜 중요한가

수동 배포는 “빌드 파일을 잘못 복사함”, “서버 명령을 빼먹음”, “환경값을 코드에 노출함”, “팀원마다 배포 방식이 다름” 같은 문제가 생기기 쉽다. CI/CD는 이런 절차를 workflow로 고정해 반복 가능하게 만든다.

## 수업에서의 핵심 흐름

수업의 책임 흐름은 `git push` → GitHub Actions checkout/JDK/Maven → Docker image build·registry push → EC2 container 갱신 → 서비스 확인이다. 이는 자동화 단계를 설명하는 모델이며, 날짜 원본에서 각 단계의 성공 증거가 모두 보존된 것은 아니다.

- **CI(Continuous Integration, 지속적 통합)**: push된 코드를 가져와 JDK를 맞추고 Maven build로 통합 가능한 상태인지 확인한다. 수업의 기본 `ci.yml`은 이 역할을 직접 보여 준다.
- **CD(Continuous Delivery/Deployment, 지속적 전달/배포)**: Docker Hub registry의 image를 EC2가 pull하고 새 container로 실행해 실제 서버에 반영한다. 수업의 Docker build/push 확장과 별도 `cd.yml`은 CI 결과물을 배포 단계로 연결한다.
- **Trigger**: workflow를 시작하는 사건이다. 수업에서는 GitHub `push`가 대표 trigger였다.

## 예시

Spring Boot 실습에서는 `push`를 trigger로 JDK 21과 Maven build를 정의한 뒤 Docker Hub login·image build/push와 EC2 배포 workflow를 연결했다. 직접 보존된 실행 증거는 EC2의 Docker version/group 출력과 `docker container ps -a`의 실행 중 container·port mapping이다. Actions build log, registry push log, browser 응답은 남아 있지 않다.

## 자동화 단계별 완료 조건

| 단계 | 확인해야 하는 결과 | 05-11 원본 상태 |
|---|---|---|
| CI build | Actions job·Maven 종료 상태와 artifact | 확인 절차만 있고 성공 log 미보존 |
| image 전달 | registry의 새 image/tag 또는 push log | workflow 정의만 보존 |
| EC2 배포 | 새 container의 image·상태·port | `Up` container 출력 보존 |
| 서비스 | 실제 URL/API 응답과 변경 내용 | URL만 기록, 응답 미보존 |

## 자주 헷갈리는 점

- CI/CD는 도구 이름이 아니라 흐름이다. GitHub Actions, Jenkins, GitLab CI/CD, CircleCI는 이 흐름을 구현하는 도구다.
- CI 성공은 “빌드가 됐다”는 뜻이지 “서비스가 사용 가능하다”는 뜻은 아니다. 배포 후 URL/API/컨테이너 상태를 확인해야 한다.
- CD를 자동으로 운영 서버까지 반영할지, 승인 후 반영할지는 팀 정책에 따라 다르다.
- Secret 값은 workflow 파일에 직접 쓰지 않고 [[concepts/github-actions-secrets-deploy|GitHub Actions Secrets 기반 배포]]로 분리한다.

## 관련 개념

- [[summaries/2026-05-11-cicd-github-actions-spring-boot|2026-05-11 CI/CD, GitHub Actions, Spring Boot 자동 배포]]
- [[concepts/github-actions-workflow|GitHub Actions workflow]]
- [[concepts/spring-boot-cicd-docker-ec2-flow|Spring Boot CI/CD Docker-EC2 배포 흐름]]
- [[concepts/middle-project-cicd-deploy-flow|중간 프로젝트 CI/CD 배포 흐름]]
- [[entities/github|GitHub]]

## 출처

- `raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md`
- `raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md`
- `raw/KoreaICT/7. Ci&CD/교육 자료/CI&CD(SpringBoot_이론).pdf`
