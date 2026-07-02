---
title: 2026-05-01 Docker Compose와 다중 컨테이너 실행
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [linux, backend, curriculum, study-log]
sources:
  - raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md
status: growing
confidence: high
---

# 2026-05-01 Docker Compose와 다중 컨테이너 실행

## 한 줄 요약

Docker Compose를 사용해 MySQL과 Spring Boot 같은 여러 컨테이너의 이미지, 포트, 네트워크, 볼륨 설정을 하나의 manifest 파일로 실행하는 방식을 배웠다.

## 배운 내용

- Compose 파일은 “무엇을 어떻게 구성할지” 적어 둔 manifest 문서다.
- `docker-compose up`은 정의된 컨테이너와 주변 환경을 만들고 실행한다.
- `docker-compose down`은 서비스와 네트워크를 중지·삭제한다.
- Dockerfile은 단일 이미지 생성 절차, Docker Compose는 여러 컨테이너 조합 실행 절차에 가깝다.
- MySQL 서비스와 Spring Boot 서비스를 함께 띄우는 구성 흐름을 실습했다.
- `docker compose -p hello -f ... up -d`처럼 프로젝트명과 파일을 지정해 실행했다.
- `docker cp`, `docker exec`, MySQL 접속으로 컨테이너 내부와 데이터를 확인했다.
- Docker Desktop 설치와 UI 활용도 함께 다뤘다.

## 핵심 실습 흐름

```bash
docker compose -p hello -f ~/docker/compose01/compose_mysql_springboot.yml up -d
docker container ps -a --format "table {{.Names}}	{{.Status}}"
docker exec -it mysql-ctr /bin/bash
mysql -u spring -p
docker-compose down
```

## 왜 중요한가

Spring Boot + DB처럼 여러 실행 단위가 필요한 서비스는 `docker run`을 여러 번 손으로 치면 순서와 설정을 잊기 쉽다. Compose는 서비스 구성을 파일로 보존해 팀원과 같은 환경을 반복 실행하게 해 준다.

## 헷갈린 점 / 질문

- Dockerfile은 “이미지를 어떻게 만들지”, Compose는 “여러 컨테이너를 어떻게 묶어 실행할지”에 가깝다.
- Compose 파일은 단독 실행 프로그램이 아니라 Docker 엔진이 읽는 설정 파일이다.
- 권한 오류(`Permission denied`)가 보이면 Docker 그룹 권한이나 재로그인이 필요할 수 있다.

## 관련 페이지

- [[concepts/dockerfile-vs-compose|Dockerfile vs Docker Compose]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[entities/docker|Docker]]

## 출처

- `raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md`
