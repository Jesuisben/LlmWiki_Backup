---
title: Docker 네트워크와 볼륨
created: 2026-07-02
updated: 2026-07-09
type: concept
tags: [linux, docker, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/KoreaICT/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf
  - raw/KoreaICT/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
status: growing
confidence: high
---

# Docker 네트워크와 볼륨

## 정의

Docker 네트워크는 컨테이너끼리 통신하게 해 주는 가상 네트워크이고, 볼륨/마운트는 컨테이너 밖의 저장 공간이나 파일을 컨테이너 안에 연결하는 방법이다.

## 왜 중요한가

Spring Boot와 MySQL, WordPress와 MySQL, Redmine과 MariaDB처럼 여러 컨테이너가 함께 동작하려면 컨테이너 사이 통신과 데이터 보존이 필요하다.

## 핵심 설명

- 사용자 정의 network에 붙은 컨테이너는 컨테이너 이름을 host처럼 사용할 수 있다.
- bind mount는 host 경로를 컨테이너 경로에 직접 연결한다.
- volume은 Docker가 관리하는 저장 공간을 컨테이너에 연결한다.
- DB 데이터는 컨테이너 삭제와 분리되어야 하므로 volume이 중요하다.

## 예시

```bash
docker network create network01
docker run --name mysql01 --net=network01 -dit \
  -e MYSQL_ROOT_PASSWORD={PASSWORD} \
  -e MYSQL_DATABASE=coffee mysql

docker run --name wordpress01 --net=network01 -dit -p 8882:80 \
  -e WORDPRESS_DB_HOST=mysql01 \
  -e WORDPRESS_DB_NAME=coffee wordpress

docker run --name bind01 -d -p 8081:80 \
  -v ~/bind_mount:/usr/local/apache2/htdocs httpd

docker volume create mount-vol
docker run --name volume01 -d -p 8082:80 \
  -v mount-vol:/usr/local/apache2/htdocs httpd
```

## 자주 헷갈리는 점

- port mapping은 host와 container 사이 접속이고, Docker network는 container와 container 사이 접속이다.
- bind mount는 host 폴더 위치가 중요하고, volume은 Docker가 위치를 관리한다.
- DB 비밀번호는 수업 예제에 있어도 wiki에서는 실제 값 대신 `{PASSWORD}` 같은 대체 표기로 일반화한다.

## 관련 개념

- [[comparisons/docker-cp-vs-bind-mount-vs-volume|docker cp vs bind mount vs volume]]
- [[concepts/docker-compose-manifest|Docker Compose manifest]]
- [[concepts/docker-reverse-proxy-load-balancing|Docker reverse proxy와 로드 밸런싱]]

## 5과목 현재 raw MD 기준 재검증 메모

- 2026-07-09에 `raw/KoreaICT/5. Linux` 날짜별 MD 10개와 `Linux 총정리.md`를 기준으로 다시 대조했다.
- 이 페이지는 단순 명령어 사전이 아니라 VM/SSH/CLI → 파일·권한 → Spring Boot jar 실행 → Docker network/volume/Dockerfile/Compose → GitHub branch/PR/conflict 흐름 속에서 읽어야 한다.
- 운영 관점에서는 코드보다 IP/포트/방화벽/권한/컨테이너 네트워크·볼륨이 문제 원인일 수 있음을 함께 기억한다.

## 출처

- `raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md`
