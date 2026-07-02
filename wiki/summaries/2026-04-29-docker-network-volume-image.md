---
title: 2026-04-29 Docker 네트워크, 볼륨, 사용자 정의 이미지
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [linux, backend, curriculum, study-log]
sources:
  - raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
  - raw/Study/5. Linux/교육 자료/docker image를 docker hub에 업로드 하기.md
status: growing
confidence: high
---

# 2026-04-29 Docker 네트워크, 볼륨, 사용자 정의 이미지

## 한 줄 요약

Docker 네트워크로 DB와 웹 애플리케이션 컨테이너를 연결하고, `docker cp`, bind mount, volume mount, `commit`, Docker Hub push/pull까지 컨테이너 운영의 핵심 흐름을 배운 날이다.

## 배운 내용

- MariaDB + Redmine, MySQL + WordPress처럼 둘 이상의 컨테이너를 같은 Docker network에 묶었다.
- `--net=network02`, `REDMINE_DB_MYSQL=mariadb02`처럼 컨테이너 이름으로 DB를 참조했다.
- `docker logs mysql85 | grep ready`로 DB 컨테이너 준비 상태를 확인했다.
- `docker exec -it`로 컨테이너 내부 shell 또는 MySQL client에 들어갔다.
- `docker cp`로 host에서 container로, container에서 host로 파일을 복사했다.
- bind mount는 호스트 디렉터리를 컨테이너 웹 루트에 직접 연결하고, volume mount는 Docker가 관리하는 볼륨을 연결하는 방식임을 비교했다.
- `docker commit`으로 수정된 컨테이너를 이미지로 저장하고, Docker Hub 형식으로 tag 후 push하는 흐름을 배웠다.

## 핵심 실습 / 예제

```bash
docker network create network02
docker run --net=network02 --name=mariadb02 -dit -e MYSQL_ROOT_PASSWORD=My@Sql01 -e MYSQL_DATABASE=coffee mariadb
docker run --net=network02 --name=redmine02 -dit -p=8883:3000 -e REDMINE_DB_MYSQL=mariadb02 -e REDMINE_DB_DATABASE=coffee -e REDMINE_DB_USERNAME=root -e REDMINE_DB_PASSWORD=My@Sql01 redmine
docker cp docker/host2container/index.html apache01-ctr:/usr/local/apache2/htdocs/index.html
docker container run --name apache02-ctr -d -p 8090:80 -v ~/bind_mount:/usr/local/apache2/htdocs httpd
docker volume create mount-vol
docker container run --name apache03-ctr -d -p 8090:80 -v mount-vol:/usr/local/apache2/htdocs httpd
docker commit commit-ctr jeju-img
docker tag jeju-img:latest rktngusals/jeju-img:latest
docker push rktngusals/jeju-img:latest
```

## 왜 중요한가

실제 웹서비스는 웹 서버만 단독으로 실행되지 않고 DB, 파일 저장소, 네트워크가 함께 필요하다. 이 날의 실습은 Docker를 “컨테이너 하나 실행”에서 “여러 컨테이너와 저장소를 운영하는 도구”로 확장했다.

## 헷갈린 점 / 질문

- `docker cp`는 일회성 복사이고 mount는 경로 연결이다.
- bind mount는 사용자가 관리하는 호스트 경로, volume은 Docker가 관리하는 저장소다.
- 같은 네트워크에 있는 컨테이너는 컨테이너 이름으로 서로 찾을 수 있다.
- Docker Hub에 push하려면 로컬 이미지 이름을 `계정명/이미지명:태그` 형식으로 tag해야 한다.
- private repository나 username 오류는 pull/push 권한 오류로 이어질 수 있다.

## 관련 페이지

- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[concepts/docker-cp-exec-container-files|Docker exec/cp와 컨테이너 파일 다루기]]
- [[comparisons/docker-cp-vs-bind-mount-vs-volume|docker cp vs bind mount vs volume]]
- [[comparisons/docker-commit-vs-dockerfile|docker commit vs Dockerfile]]
- [[entities/docker|Docker]]

## 출처

- `raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md`
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf` — p.71~75 volume/bind mount, p.85~91 Compose 배경
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf` — p.32~72 네트워크, WordPress/MySQL, docker cp, mount 실습
- `raw/Study/5. Linux/교육 자료/docker image를 docker hub에 업로드 하기.md`
