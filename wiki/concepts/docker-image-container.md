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
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
status: growing
confidence: high
---

# Docker 이미지와 컨테이너

## 정의

Docker 이미지는 애플리케이션 실행 환경을 담은 템플릿이고, 컨테이너는 그 이미지로 만든 실제 실행 단위다. 수업에서는 이미지를 “밀키트/설계도”, 컨테이너를 “실제로 돌아가는 인스턴스”로 이해했다.

## 왜 중요한가

개발 PC와 서버의 Java 버전, DB 설치 상태, 파일 위치가 다르면 “내 컴퓨터에서는 되는데 서버에서는 안 됨” 문제가 생긴다. Docker는 실행 환경을 이미지로 고정해 어느 서버에서도 비슷한 방식으로 실행하게 한다.

## 수업에서 이어진 흐름

- 2026-04-28: Docker 개요, 설치, Apache/nginx/MySQL 컨테이너 실행·중지·삭제.
- 2026-04-29: WordPress+MySQL, Redmine+MariaDB, `docker exec`, `docker cp`, network, mount.
- 2026-04-30: `docker commit`, Dockerfile, Spring Boot 컨테이너, reverse proxy.
- 2026-05-01: Docker Compose로 다중 컨테이너 실행.

## 핵심 명령어

```bash
docker image ls
docker images
docker container ls
docker container ps -a
docker container run --name apache01 -d -p 8888:80 httpd
docker container run --name nginx85 -d -p 8885:80 nginx
docker container run --name=mysql85 -dit -e MYSQL_ROOT_PASSWORD=root mysql
docker logs mysql85 | grep ready
docker exec -it apache81 /bin/bash
docker cp index.html apache82:/usr/local/apache2/htdocs/index.html
docker container stop apache01
docker container rm apache01
docker image rm httpd
```

## 이미지 이름과 태그

Docker 교안은 `nginx`, `mysql`, `python`, `openjdk`, `httpd` 같은 대표 이미지를 소개한다. `mysql:8.0`처럼 `:` 뒤의 값은 tag이며, 특정 버전 또는 `latest`를 가리킨다.

## 자주 헷갈리는 점

- 이미지는 실행 전 템플릿이고, 컨테이너는 생성/실행된 결과다.
- `docker run`은 로컬에 이미지가 없으면 Docker Hub에서 pull한 뒤 컨테이너를 만든다.
- 컨테이너를 삭제해도 이미지가 바로 삭제되는 것은 아니다.
- 컨테이너 내부 파일 수정은 컨테이너 삭제와 함께 사라질 수 있다. 유지하려면 bind mount, volume, commit, Dockerfile이 필요하다.
- `-d`는 detached/background, `-i`는 표준 입력 유지, `-t`는 가상 터미널 할당이다.

## 관련 페이지

- [[entities/docker|Docker]]
- [[concepts/docker-install-permission-setup|Docker 설치와 권한 설정]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[concepts/docker-cp-exec-container-files|Docker exec/cp와 컨테이너 파일 다루기]]
- [[comparisons/docker-commit-vs-dockerfile|docker commit vs Dockerfile]]
- [[concepts/dockerfile-vs-compose|Dockerfile vs Docker Compose]]

## 출처

- `raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md`
- `raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md`
- `raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md`
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf` — 이미지/컨테이너, 대표 이미지
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf` — 컨테이너 실행/상태/삭제, docker cp/exec
