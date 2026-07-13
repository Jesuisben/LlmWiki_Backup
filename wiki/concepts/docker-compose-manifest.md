---
title: Docker Compose manifest
created: 2026-07-02
updated: 2026-07-13
type: concept
tags: [linux, docker, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/KoreaICT/5. Linux/교육 자료/도커 컴포즈 종합 실습.md
  - raw/KoreaICT/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf
  - raw/KoreaICT/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
status: growing
confidence: high
---

# Docker Compose manifest

## 정의

Docker Compose manifest는 여러 컨테이너와 그 주변 실행 환경을 하나의 YAML 파일에 선언한 문서다.

## 왜 중요한가

MySQL + Spring Boot, WordPress + MySQL처럼 여러 컨테이너가 필요한 구성을 `docker run` 여러 줄로 매번 입력하면 실수하기 쉽다. Compose는 실행 구성을 파일로 남겨 반복 가능하게 한다.

## 주요 항목

| 항목 | 의미 |
|---|---|
| `services` | 실행할 컨테이너/서비스 목록 |
| `image` | 사용할 이미지 |
| `build` | Dockerfile로 이미지를 빌드할 위치 |
| `container_name` | 컨테이너 이름 |
| `ports` | host port와 container port 연결 |
| `volumes` | bind mount 또는 Docker volume 연결 |
| `networks` | 연결할 Docker network |
| `environment` | 환경 변수 |
| `depends_on` | 서비스 시작 순서 의존 |
| `restart` | 재시작 정책 |

## 예시

```yaml
services:
  mysql:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: {PASSWORD}
      MYSQL_DATABASE: appdb
    volumes:
      - mysql-data:/var/lib/mysql
    networks:
      - app-net

  spring:
    image: myspring-img
    ports:
      - "9000:9000"
    depends_on:
      - mysql
    networks:
      - app-net

networks:
  app-net:

volumes:
  mysql-data:
```

```bash
docker compose up -d
docker compose ps
docker compose logs
docker compose down
```

## 자주 헷갈리는 점

- YAML은 들여쓰기가 문법이다. `services` 아래 service 이름과 각 설정의 계층을 정확히 맞춰야 한다.
- `depends_on`은 컨테이너 시작 순서이지 DB 준비 완료 보장은 아니다.
- Compose 파일 안의 비밀번호는 실무에서 `.env`나 secret 관리로 분리해야 한다.

## 관련 개념

- [[concepts/dockerfile-vs-compose|Dockerfile vs Docker Compose]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[concepts/spring-boot-cicd-docker-ec2-flow|Spring Boot CI/CD Docker-EC2 배포 흐름]]

## 최신 원본 대조

2026-05-01의 Spring image+MySQL Compose 실행을 기준으로 보강했다. `up -d`는 service뿐 아니라 project network와 volume을 만들며, `down`과 volume 삭제 옵션은 DB 데이터 보존에 다른 영향을 준다.

## 출처

- `raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md`
- `raw/KoreaICT/5. Linux/교육 자료/도커 컴포즈 종합 실습.md`
