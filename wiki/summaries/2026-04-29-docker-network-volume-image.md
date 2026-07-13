---
title: 2026-04-29 Docker 네트워크, 볼륨, 사용자 정의 이미지
created: 2026-07-06
updated: 2026-07-13
type: summary
tags: [linux, docker, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md
status: growing
confidence: high
---

# 2026-04-29 Docker 네트워크, 볼륨, 사용자 정의 이미지

## 한 줄 요약

MariaDB와 Redmine 컨테이너를 Docker network로 연결하고, bind mount/volume mount, docker commit, 사용자 정의 이미지 흐름을 실습했다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

실제 서비스는 컨테이너 하나로 끝나지 않는다. DB와 앱 컨테이너가 통신해야 하고, 컨테이너가 삭제되어도 데이터나 파일은 보존되어야 한다.

## 핵심 개념

- 가상 네트워크 생성 후 MariaDB 컨테이너와 Redmine 컨테이너를 같은 네트워크에 연결했다.
- 컨테이너 내부 파일 수정, `docker exec`, `docker cp` 흐름을 확인했다.
- bind mount와 Docker volume mount의 차이를 배웠다.
- 컨테이너 상태를 이미지로 만드는 `docker commit`과 사용자 정의 이미지 생성을 실습했다.

## 실습 / 예제

network 생성 → DB 컨테이너 실행 → 앱 컨테이너 실행 → network/volume 확인 → 컨테이너 정리 순서로 다중 컨테이너 운영 감각을 익혔다.

## 헷갈린 점 / 질문

컨테이너 내부 수정은 컨테이너 삭제 시 사라질 수 있다. 지속성이 필요하면 bind mount나 volume을 사용해야 한다.

## 관련 페이지

- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]], [[concepts/docker-cp-exec-container-files|Docker exec/cp와 컨테이너 파일 다루기]], [[comparisons/docker-cp-vs-bind-mount-vs-volume|docker cp vs bind mount vs volume]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md`
