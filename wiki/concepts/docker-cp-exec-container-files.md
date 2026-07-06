---
title: Docker exec/cp와 컨테이너 파일 다루기
created: 2026-07-02
updated: 2026-07-06
type: concept
tags: [linux, docker, backend]
sources:
  - raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
status: growing
confidence: high
---

# Docker exec/cp와 컨테이너 파일 다루기

## 정의

`docker exec`는 실행 중인 컨테이너 안에서 명령을 실행하는 도구이고, `docker cp`는 host와 container 사이에서 파일을 복사하는 도구다.

## 왜 중요한가

컨테이너는 격리된 환경이라 host 파일 시스템과 내부 파일 시스템이 다르다. 웹 루트 파일 교체, DB 접속, 설정 확인을 하려면 컨테이너 내부 접근 방식과 파일 전달 방식을 알아야 한다.

## 핵심 설명

- `docker exec 컨테이너 명령`: 컨테이너 내부에서 한 번 명령 실행.
- `docker exec -it 컨테이너 /bin/bash`: 컨테이너 내부 shell 접속.
- `docker cp host경로 컨테이너:container경로`: host에서 container로 복사.
- `docker cp 컨테이너:container경로 host경로`: container에서 host로 복사.

## 예시

```bash
docker exec apache01 ls /usr/local/apache2/htdocs
docker exec apache01 cat /usr/local/apache2/htdocs/index.html
docker exec -it apache81 /bin/bash
apt update
apt install -y vim
cd /usr/local/apache2/htdocs
vi index.html
exit

docker cp ./index.html apache01:/usr/local/apache2/htdocs/index.html
docker cp apache01:/usr/local/apache2/htdocs/index.html ./index-from-container.html
```

## 자주 헷갈리는 점

- `docker cp`는 파일을 연결하는 것이 아니라 복사한다. 계속 동기화되지 않는다.
- 컨테이너 내부에 `vim` 같은 도구가 없을 수 있다. 이미지는 최소 구성인 경우가 많다.
- 컨테이너 내부에서 바꾼 내용은 이미지에 자동 반영되지 않는다. 이미지화하려면 `docker commit` 또는 Dockerfile이 필요하다.

## 관련 개념

- [[comparisons/docker-cp-vs-bind-mount-vs-volume|docker cp vs bind mount vs volume]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]

## 출처

- `raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md`
