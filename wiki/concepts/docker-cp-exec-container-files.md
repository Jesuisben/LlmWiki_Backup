---
title: Docker exec/cp와 컨테이너 파일 다루기
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [linux, backend]
sources:
  - raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
status: growing
confidence: high
---

# Docker exec/cp와 컨테이너 파일 다루기

## 정의

`docker exec`는 실행 중인 컨테이너 안에서 명령을 실행하거나 shell에 들어가는 명령이고, `docker cp`는 host와 container 사이에서 파일을 복사하는 명령이다.

## 수업에서 사용한 상황

- Apache/nginx 컨테이너 내부의 기본 `index.html` 위치를 확인했다.
- 컨테이너 안에 `vim`을 설치하고 직접 HTML을 수정했다.
- host에 있는 HTML/이미지 파일을 컨테이너 웹 루트로 복사했다.
- 컨테이너 안의 파일을 host로 다시 복사했다.
- MySQL 컨테이너에 들어가 DB 프롬프트에 접속했다.

## 핵심 명령어

```bash
docker exec apache01-ctr ls /usr/local/apache2/htdocs
docker exec apache01-ctr cat /usr/local/apache2/htdocs/index.html
docker exec -it apache81 /bin/bash
apt update
apt install -y vim
cd /usr/local/apache2/htdocs/
vi index.html
exit
docker cp docker/host2container/index.html apache01-ctr:/usr/local/apache2/htdocs/index.html
docker cp docker/host2container/coffee01.png apache01-ctr:/usr/local/apache2/htdocs/coffee01.png
docker cp apache01-ctr:/usr/local/apache2/htdocs/index.html ~/docker/host2container/hello.html
docker exec -it mysql85 /bin/bash
mysql -u root -p
```

## Apache와 Nginx의 웹 루트

| 이미지 | 기본 웹 루트 |
|---|---|
| `httpd` | `/usr/local/apache2/htdocs/` |
| `nginx` | `/usr/share/nginx/html/` |

## 왜 중요한가

컨테이너가 “작은 서버”처럼 동작한다는 감각을 잡게 해 준다. 다만 `exec`로 들어가 수동 수정한 내용은 재현성이 떨어질 수 있으므로, 나중에는 Dockerfile이나 mount로 관리하는 편이 좋다.

## 자주 헷갈리는 점

- `exec`는 실행 중인 컨테이너에 명령을 내린다. 정지된 컨테이너에는 바로 들어갈 수 없다.
- `docker cp`는 복사이므로 이후 원본 파일을 바꿔도 자동 반영되지 않는다.
- 컨테이너 내부에는 `vi` 같은 도구가 없을 수 있어 설치가 필요할 수 있다.
- `docker exec -it nginx04 /bin/`처럼 shell 경로를 잘못 쓰면 실패할 수 있다. 보통 `/bin/bash` 또는 `/bin/sh`를 확인한다.

## 관련 페이지

- [[summaries/2026-04-29-docker-network-volume-image|2026-04-29 Docker 네트워크, 볼륨, 사용자 정의 이미지]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[comparisons/docker-cp-vs-bind-mount-vs-volume|docker cp vs bind mount vs volume]]
- [[comparisons/docker-commit-vs-dockerfile|docker commit vs Dockerfile]]

## 출처

- `raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md`
- `raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md`
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf` — p.51~72 host/container 파일 복사와 mount 전 단계 실습
