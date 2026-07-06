---
title: Docker 이미지와 컨테이너
created: 2026-07-02
updated: 2026-07-06
type: concept
tags: [linux, docker, backend]
sources:
  - raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/Study/5. Linux/Linux 총정리/Linux 총정리.md
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf
status: growing
confidence: high
---

# Docker 이미지와 컨테이너

## 정의

Docker 이미지는 애플리케이션 실행 환경을 담은 읽기 전용 템플릿이고, 컨테이너는 그 이미지로 실제 실행한 격리된 프로세스 단위다.

## 왜 중요한가

서버마다 Java, DB, 웹서버 설치 상태가 다르면 배포가 흔들린다. Docker는 “실행 환경을 이미지로 고정하고 컨테이너로 실행”하게 해 개발 PC와 서버의 차이를 줄인다.

## 핵심 설명

- image: `httpd`, `nginx`, `mysql`, `wordpress`, `redmine`, 직접 만든 `myspring-img` 같은 실행 템플릿.
- container: image에서 생성되어 실행·중지·삭제되는 실제 단위.
- `docker run`: 이미지가 없으면 pull하고 컨테이너를 생성/실행한다.
- `-p 호스트포트:컨테이너포트`: 외부 접속 포트 연결.
- `-d`: 백그라운드 실행.
- `--name`: 컨테이너 이름 지정.

## 예시

```bash
docker run --name apache01 -d -p 8080:80 httpd
docker ps
docker ps -a
docker stop apache01
docker start apache01
docker rm apache01
docker images
docker rmi httpd
```

## 자주 헷갈리는 점

- 이미지는 삭제해도 실행 중인 컨테이너가 있으면 막힐 수 있다. 컨테이너와 이미지는 생명주기가 다르다.
- 컨테이너 내부에서 수정한 파일은 컨테이너 삭제 시 사라질 수 있다. 필요한 데이터는 volume/mount를 써야 한다.
- `docker run`은 “항상 새 컨테이너 생성”에 가깝고, 기존 컨테이너는 `start`/`stop`으로 다룬다.

## 관련 개념

- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[concepts/docker-compose-manifest|Docker Compose manifest]]
- [[comparisons/docker-commit-vs-dockerfile|docker commit vs Dockerfile]]

## 출처

- `raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md`
