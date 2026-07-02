---
title: Docker 네트워크와 볼륨
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [linux, backend]
sources:
  - raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
status: growing
confidence: high
---

# Docker 네트워크와 볼륨

## 정의

Docker 네트워크는 컨테이너끼리 통신하게 해 주는 가상 네트워크이고, 볼륨/마운트는 컨테이너 밖의 저장 공간이나 파일을 컨테이너 안에 연결하는 방법이다.

## 네트워크 실습

WordPress + MySQL, Redmine + MariaDB 실습에서는 네트워크를 먼저 만들고 두 컨테이너를 같은 네트워크에 붙였다.

```bash
docker network create network01
docker container run --net=network01 --name=mysql01 -dit -e MYSQL_ROOT_PASSWORD=My@Sql01 -e MYSQL_DATABASE=coffee mysql --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
docker container run --name=wordpress01 -dit --net=network01 -p=8882:80 -e WORDPRESS_DB_HOST=mysql01 -e WORDPRESS_DB_NAME=coffee -e WORDPRESS_DB_USER=root -e WORDPRESS_DB_PASSWORD=My@Sql01 wordpress
docker network inspect network01 --format '{{range .Containers}}{{.Name}}{{"
"}}{{end}}'
```

같은 네트워크에서는 `mysql01`, `mariadb02` 같은 컨테이너 이름이 DB host처럼 쓰였다.

## mount 실습

```bash
docker container run --name apache02-ctr -d -p 8090:80 -v ~/bind_mount:/usr/local/apache2/htdocs httpd
docker container inspect apache02-ctr | grep -E "Source|Destination|bind"
docker volume create mount-vol
docker container run --name apache03-ctr -d -p 8090:80 -v mount-vol:/usr/local/apache2/htdocs httpd
docker volume inspect mount-vol
```

## bind mount vs volume mount

| 구분 | bind mount | volume mount |
|---|---|---|
| 기준 위치 | 호스트의 특정 경로 | Docker가 관리하는 볼륨 |
| 관리 주체 | 사용자 | Docker |
| 수업 예시 | `~/bind_mount:/usr/local/apache2/htdocs` | `mount-vol:/usr/local/apache2/htdocs` |
| 장점 | 개발 중 파일을 직접 바꿔 반영하기 쉬움 | Docker가 관리해 컨테이너 삭제와 데이터를 분리하기 좋음 |
| 주의 | 빈 호스트 폴더를 웹 루트에 연결하면 컨테이너 내부도 비어 보일 수 있음 | 실제 경로는 Docker 관리 영역이라 직접 수정 비권장 |

## 왜 중요한가

웹 애플리케이션은 보통 backend 컨테이너와 DB 컨테이너가 함께 동작한다. 네트워크가 없으면 이름 기반 연결이 어렵고, 볼륨이 없으면 컨테이너 삭제와 함께 데이터가 사라질 수 있다.

## 자주 헷갈리는 점

- “컨테이너가 실행 중”과 “컨테이너끼리 통신 가능”은 다르다.
- DB 컨테이너는 데이터 유지가 중요하므로 volume을 고려해야 한다.
- `docker cp`는 복사이고, mount는 연결이다.
- nginx는 빈 bind mount 디렉터리를 웹 루트로 쓰면 403 Forbidden이 날 수 있다.

## 관련 페이지

- [[summaries/2026-04-29-docker-network-volume-image|2026-04-29 Docker 네트워크, 볼륨, 사용자 정의 이미지]]
- [[summaries/2026-05-01-docker-compose|2026-05-01 Docker Compose와 다중 컨테이너 실행]]
- [[comparisons/docker-cp-vs-bind-mount-vs-volume|docker cp vs bind mount vs volume]]
- [[concepts/docker-compose-manifest|Docker Compose manifest]]

## 출처

- `raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md`
- `raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md`
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf` — p.71~75 volume/bind mount
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf` — WordPress/MySQL, Redmine/MariaDB, bind/volume mount 실습
