---
title: Docker 이미지와 컨테이너
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [linux, backend]
sources:
  - raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md
status: growing
confidence: high
---

# Docker 이미지와 컨테이너

## 정의

Docker 이미지는 애플리케이션 실행 환경을 담은 템플릿이고, 컨테이너는 그 이미지로 만든 실제 실행 단위다. 수업에서는 이미지를 “밀키트/템플릿”, 컨테이너를 “그 밀키트로 실제 만든 요리/실행 인스턴스”처럼 이해했다.

## 왜 중요한가

개발 PC와 서버의 Java 버전, DB 설치 상태, 파일 위치가 다르면 “내 컴퓨터에서는 되는데 서버에서는 안 됨” 문제가 생긴다. Docker는 실행 환경을 이미지로 고정해 같은 방식으로 실행하게 만든다.

## 핵심 명령어

```bash
docker image ls
docker container ls -a
docker run --name apache01-ctr -d -p 8090:80 httpd
docker exec apache01-ctr ls /usr/local/apache2/htdocs
docker cp index.html apache01-ctr:/usr/local/apache2/htdocs/index.html
docker container stop apache01-ctr
docker container rm apache01-ctr
docker image rm httpd
```

## 수업에서 이어진 흐름

- 2026-04-28: Docker 개요, 이미지 생성, 컨테이너 실행, Apache/MariaDB/nginx 컨테이너 실습.
- 2026-04-29: Redmine + MariaDB 컨테이너 연동, 네트워크와 마운트.
- 2026-04-30: 컨테이너 변경분을 이미지로 만들기, Dockerfile로 이미지 빌드, Spring Boot 컨테이너.
- 2026-05-01: Docker Compose로 여러 컨테이너를 묶어 실행.

## 자주 헷갈리는 점

- 이미지는 실행 전 템플릿이고, 컨테이너는 생성/실행된 결과다.
- 컨테이너를 삭제해도 이미지가 바로 삭제되는 것은 아니다. 반대로 이미지를 삭제하려면 그 이미지를 쓰는 컨테이너 정리가 먼저 필요할 수 있다.
- 컨테이너 내부 파일 수정은 임시적일 수 있다. 유지하려면 bind mount, volume, 또는 새 이미지 생성이 필요하다.

## 관련 페이지

- [[entities/docker|Docker]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[concepts/dockerfile-vs-compose|Dockerfile vs Docker Compose]]
- [[summaries/2026-04-28-maven-spring-boot-docker-intro|2026-04-28 Maven, Spring Boot 서버 실행, Docker 입문]]

## 출처

- `raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md`
- `raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md`
- `raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md`
