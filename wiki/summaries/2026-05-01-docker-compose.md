---
title: 2026-05-01 Docker Compose와 다중 컨테이너 실행
created: 2026-07-02
updated: 2026-07-06
type: summary
tags: [linux, docker, backend, curriculum]
sources:
  - raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/Study/5. Linux/교육 자료/도커 컴포즈 종합 실습.md
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
status: growing
confidence: high
---

# 2026-05-01 Docker Compose와 다중 컨테이너 실행

## 한 줄 요약

여러 `docker run` 명령을 하나의 `docker-compose.yml` manifest로 정리해 MySQL+Spring Boot 같은 다중 컨테이너 구성을 실행한 날이다.

## 배운 내용

- Docker Compose가 여러 service, network, volume, environment, port mapping을 한 파일에 선언하는 도구임을 배웠다.
- `docker compose up -d`, `docker compose down`, `docker compose logs`로 실행·중지·로그 확인을 했다.
- YAML 들여쓰기와 `services`, `networks`, `volumes`, `environment`, `depends_on`의 역할을 구분했다.
- MySQL과 Spring Boot 컨테이너를 같은 네트워크에 두고 DB host를 service 이름으로 지정하는 흐름을 익혔다.
- Compose 파일은 운영 절차를 문서화하므로 팀원이나 서버가 바뀌어도 같은 구성을 재현하기 쉽다는 점을 배웠다.

## 핵심 개념

- [[concepts/docker-compose-manifest|Docker Compose manifest]]
- [[concepts/dockerfile-vs-compose|Dockerfile vs Docker Compose]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[entities/docker|Docker]]

## 실습 / 예제

```yaml
services:
  db:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: {PASSWORD}
      MYSQL_DATABASE: appdb
    volumes:
      - db-data:/var/lib/mysql
  app:
    image: myspring-img
    ports:
      - "9000:9000"
    depends_on:
      - db

volumes:
  db-data:
```

```bash
docker compose up -d
docker compose ps
docker compose logs
docker compose down
```

## 헷갈린 점 / 질문

- Compose는 이미지를 만드는 Dockerfile과 다르다. Compose는 이미 있는 이미지 또는 Dockerfile 빌드 결과를 “어떻게 함께 실행할지” 적는다.
- YAML은 들여쓰기가 문법이므로 탭/스페이스와 계층을 조심해야 한다.
- `depends_on`은 시작 순서를 돕지만 DB가 완전히 준비될 때까지 애플리케이션 재시도 로직을 대신해 주지는 않는다.

## 관련 페이지

- [[summaries/2026-05-04-git-github-sourcetree|2026-05-04 GitHub, Git Bash, SourceTree 협업 입문]]
- [[concepts/spring-boot-cicd-docker-ec2-flow|Spring Boot CI/CD Docker-EC2 배포 흐름]]

## 출처

- `raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md`
- `raw/Study/5. Linux/교육 자료/도커 컴포즈 종합 실습.md`
