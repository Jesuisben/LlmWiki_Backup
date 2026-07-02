---
title: Dockerfile vs Docker Compose
created: 2026-07-02
updated: 2026-07-02
type: comparison
tags: [linux, backend]
sources:
  - raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
status: growing
confidence: high
---

# Dockerfile vs Docker Compose

## 비교 목적

수업에서 Dockerfile과 Docker Compose가 연달아 등장했기 때문에 둘 다 “Docker 설정 파일”처럼 보일 수 있다. 하지만 역할은 다르다.

## 한눈에 보기

| 항목 | Dockerfile | Docker Compose |
|---|---|---|
| 핵심 질문 | 이미지를 어떻게 만들까? | 여러 컨테이너를 어떻게 함께 실행할까? |
| 결과 | Docker image | service/container/network/volume 실행 구성 |
| 파일 형식 | `Dockerfile` 텍스트 | YAML, 보통 `docker-compose.yml` 또는 `.yml` |
| 주요 명령 | `docker build` | `docker compose up`, `docker compose down` |
| 주요 키워드 | `FROM`, `COPY`, `RUN`, `EXPOSE`, `ENTRYPOINT` | `services`, `image`, `ports`, `volumes`, `networks`, `environment` |
| 수업 예시 | `pohang-img`, `myspring-img` 이미지 빌드 | MySQL + Spring Boot, MySQL + WordPress 구성 실행 |

## 수업 예제

Dockerfile 쪽은 다음 흐름이었다.

```bash
docker build -t pohang-img -f ~/docker/dockerfile/Dockerfile01 .
docker container run --name pohang-ctr -d -p 8989:80 pohang-img
```

Compose 쪽은 다음 흐름이었다.

```bash
docker compose -p hello -f ~/docker/compose01/compose_mysql_springboot.yml up -d
docker compose -p hello -f ~/docker/compose01/compose_mysql_springboot.yml down
```

## 언제 무엇을 쓰는가

- 우리 애플리케이션 실행 환경을 이미지로 만들고 싶으면 Dockerfile을 쓴다.
- 이미 만들어진 여러 이미지/서비스를 한 번에 띄우고 연결하고 싶으면 Docker Compose를 쓴다.
- Spring Boot + MySQL처럼 백엔드와 DB가 함께 필요한 로컬/실습 환경은 Compose가 특히 편하다.
- Compose가 Dockerfile을 대신하는 것은 아니다. Compose 안에서 Dockerfile build를 지시할 수도 있다.

## 헷갈리기 쉬운 포인트

- Dockerfile은 단일 이미지의 레시피, Compose는 여러 컨테이너 실행의 설계도에 가깝다.
- Dockerfile은 build 시점에 읽히고, Compose 파일은 실행 구성 생성 시점에 읽힌다.
- `docker compose down`은 컨테이너/네트워크를 정리하지만 이미지/볼륨은 별도 관리가 필요할 수 있다.

## 관련 페이지

- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[concepts/docker-compose-manifest|Docker Compose manifest]]
- [[comparisons/docker-commit-vs-dockerfile|docker commit vs Dockerfile]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[summaries/2026-04-30-dockerfile-spring-load-balancing|2026-04-30 Dockerfile, Spring Boot 컨테이너, 로드 밸런싱]]
- [[summaries/2026-05-01-docker-compose|2026-05-01 Docker Compose와 다중 컨테이너 실행]]

## 출처

- `raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md`
- `raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md`
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf` — p.85~91 Compose와 Dockerfile 비교
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf` — Dockerfile, Compose 실습
