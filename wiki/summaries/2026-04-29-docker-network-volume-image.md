---
title: 2026-04-29 Docker 네트워크, 볼륨, 사용자 정의 이미지
created: 2026-07-02
updated: 2026-07-06
type: summary
tags: [linux, docker, backend, curriculum]
sources:
  - raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
status: growing
confidence: high
---

# 2026-04-29 Docker 네트워크, 볼륨, 사용자 정의 이미지

## 한 줄 요약

Docker 컨테이너 내부 파일을 다루고, DB+웹 컨테이너를 같은 네트워크에 연결하며, bind mount/volume/commit으로 상태를 관리한 날이다.

## 배운 내용

- `docker exec`로 컨테이너 내부 명령을 실행하고 shell에 들어갔다.
- `docker cp`로 host와 container 사이에서 HTML·이미지 파일을 복사했다.
- MySQL, WordPress, MariaDB, Redmine 컨테이너를 실행하면서 환경 변수와 네트워크를 사용했다.
- `docker network create`와 `--net`으로 컨테이너 이름 기반 통신을 구성했다.
- bind mount와 Docker volume의 차이를 실습했다.
- 수정된 컨테이너를 `docker commit`으로 새 이미지로 저장했다.

## 핵심 개념

- [[concepts/docker-cp-exec-container-files|Docker exec/cp와 컨테이너 파일 다루기]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[comparisons/docker-cp-vs-bind-mount-vs-volume|docker cp vs bind mount vs volume]]
- [[comparisons/docker-commit-vs-dockerfile|docker commit vs Dockerfile]]

## 실습 / 예제

```bash
docker exec -it apache81 /bin/bash
docker cp ./index.html apache81:/usr/local/apache2/htdocs/index.html

docker network create network01
docker run --name mysql01 --net=network01 -dit -e MYSQL_ROOT_PASSWORD={PASSWORD} -e MYSQL_DATABASE=coffee mysql
docker run --name wordpress01 --net=network01 -dit -p 8882:80 -e WORDPRESS_DB_HOST=mysql01 wordpress

docker run --name bind01 -d -p 8081:80 -v ~/bind_mount:/usr/local/apache2/htdocs httpd
docker volume create mount-vol
docker commit commit-ctr jeju-img
```

## 헷갈린 점 / 질문

- `docker cp`는 파일을 한 번 복사할 뿐이고, 이후 host 파일을 수정해도 컨테이너에 자동 반영되지 않는다.
- bind mount는 host 경로와 container 경로를 연결하므로 개발 중 파일 변경 반영에 유리하다.
- volume은 Docker가 관리하는 저장 공간이어서 컨테이너 삭제와 데이터를 분리해 생각할 수 있다.
- DB 비밀번호 같은 값은 수업 예제로 등장해도 wiki에는 실제 값 대신 `{PASSWORD}`로 일반화한다.

## 관련 페이지

- [[summaries/2026-04-30-dockerfile-spring-load-balancing|2026-04-30 Dockerfile, Spring Boot 컨테이너, 로드 밸런싱]]
- [[entities/docker|Docker]]

## 출처

- `raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md`
