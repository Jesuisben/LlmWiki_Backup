---
title: Docker 네트워크와 볼륨
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [linux, backend]
sources:
  - raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md
status: growing
confidence: high
---

# Docker 네트워크와 볼륨

## 정의

Docker 네트워크는 컨테이너끼리 통신하게 해 주는 가상 네트워크이고, 볼륨/마운트는 컨테이너 밖의 저장 공간이나 파일을 컨테이너 안에 연결하는 방법이다.

## 수업 예제

MariaDB와 Redmine 컨테이너를 연결할 때는 네트워크를 먼저 만들었다.

```bash
docker network create network02
docker network ls
docker run --net=network02 --name=mariadb02 -dit -e MYSQL_ROOT_PASSWORD=My@Sql01 mariadb
docker run --net=network02 --name=redmine02 -dit -p=8883:3000 -e REDMINE_DB_MYSQL=mariadb02 redmine
```

Apache/nginx 실습에서는 호스트 파일을 컨테이너 웹 루트에 복사하거나, bind mount/volume mount로 파일 저장 위치를 연결했다.

## 왜 중요한가

웹 애플리케이션은 보통 백엔드 컨테이너와 DB 컨테이너가 함께 동작한다. 네트워크가 없으면 컨테이너 이름으로 서로 찾기 어렵고, 볼륨이 없으면 컨테이너 삭제와 함께 데이터가 사라질 수 있다.

## bind mount vs volume mount

| 구분 | bind mount | volume mount |
|---|---|---|
| 기준 위치 | 호스트의 특정 경로 | Docker가 관리하는 볼륨 |
| 장점 | 로컬 파일을 바로 연결하기 쉬움 | Docker가 관리해 이식성과 관리성이 좋음 |
| 수업 맥락 | Apache/nginx 웹 루트 파일 교체 | 컨테이너 데이터 유지 |

## 자주 헷갈리는 점

- “컨테이너가 실행 중”이라는 것과 “컨테이너끼리 통신 가능”은 다르다. 같은 네트워크에 있어야 이름 기반 연결이 쉬워진다.
- DB 컨테이너는 데이터 유지가 중요하므로, 컨테이너 삭제와 데이터 삭제를 분리해서 생각해야 한다.
- `docker cp`는 복사이고 mount는 연결이다. 복사는 한 번 옮기는 것이고, mount는 실행 중 경로를 이어 붙이는 것에 가깝다.

## 관련 페이지

- [[summaries/2026-04-29-docker-network-volume-image|2026-04-29 Docker 네트워크, 볼륨, 사용자 정의 이미지]]
- [[summaries/2026-05-01-docker-compose|2026-05-01 Docker Compose와 다중 컨테이너 실행]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]

## 출처

- `raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md`
- `raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md`
