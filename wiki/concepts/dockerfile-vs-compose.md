---
title: Dockerfile vs Docker Compose
created: 2026-07-02
updated: 2026-07-06
type: comparison
tags: [linux, docker, backend]
sources:
  - raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/Study/5. Linux/Linux 총정리/Linux 총정리.md
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
status: growing
confidence: high
---

# Dockerfile vs Docker Compose

## 비교 목적

수업에서 Dockerfile과 Docker Compose가 연달아 등장했기 때문에 둘 다 “Docker 설정 파일”처럼 보일 수 있다. 하지만 하나는 이미지를 만들고, 다른 하나는 여러 컨테이너 실행 구성을 선언한다.

## 한눈에 보기

| 항목 | Dockerfile | Docker Compose |
|---|---|---|
| 핵심 질문 | 이미지를 어떻게 만들까? | 여러 컨테이너를 어떻게 함께 실행할까? |
| 결과 | Docker image | service/container/network/volume 실행 구성 |
| 파일 형식 | 보통 `Dockerfile` | 보통 `docker-compose.yml` |
| 주요 명령 | `docker build` | `docker compose up/down` |
| 주요 키워드 | `FROM`, `COPY`, `RUN`, `EXPOSE`, `ENTRYPOINT` | `services`, `ports`, `volumes`, `networks`, `environment` |
| 수업 예시 | Spring Boot jar를 담은 `myspring-img` | MySQL + Spring Boot 다중 컨테이너 구성 |

## 언제 무엇을 쓰는가

- 내 애플리케이션을 어떤 실행 환경으로 포장할지 정할 때는 Dockerfile을 쓴다.
- DB, backend, proxy처럼 여러 컨테이너를 한 번에 띄울 때는 Compose를 쓴다.
- 실제 프로젝트에서는 Dockerfile로 app image를 만들고, Compose에서 그 image와 DB/network/volume을 함께 실행할 수 있다.

## 헷갈리기 쉬운 포인트

- Compose가 Dockerfile을 완전히 대체하지 않는다.
- Dockerfile은 컨테이너 “하나의 이미지 레시피”, Compose는 서비스 묶음 “실행 설계도”에 가깝다.
- `docker compose up`이 build를 수행할 수는 있지만, 그때도 이미지 생성 규칙은 Dockerfile에 들어 있다.

## 관련 페이지

- [[concepts/docker-compose-manifest|Docker Compose manifest]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[comparisons/docker-commit-vs-dockerfile|docker commit vs Dockerfile]]

## 출처

- `raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md`
- `raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md`
