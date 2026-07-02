---
title: docker cp vs bind mount vs volume
created: 2026-07-02
updated: 2026-07-02
type: comparison
tags: [linux, backend]
sources:
  - raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
status: growing
confidence: high
---

# docker cp vs bind mount vs volume

## 비교 목적

Docker 수업에서는 컨테이너 파일을 바꾸는 방법으로 `docker cp`, bind mount, volume mount가 모두 등장했다. 셋은 모두 “컨테이너 안의 파일/데이터를 다룬다”는 점은 같지만 성격이 다르다.

## 한눈에 보기

| 항목 | `docker cp` | bind mount | volume mount |
|---|---|---|---|
| 핵심 | 파일을 한 번 복사 | 호스트 경로를 컨테이너 경로에 연결 | Docker가 관리하는 volume을 연결 |
| 연결 지속성 | 복사 순간만 | 컨테이너 실행 중 연결 | 컨테이너 삭제와 분리해 보존 가능 |
| 관리 주체 | 사용자 | 사용자/호스트 파일 시스템 | Docker |
| 수업 예시 | HTML/이미지를 Apache 컨테이너로 복사 | `~/bind_mount:/usr/local/apache2/htdocs` | `mount-vol:/usr/local/apache2/htdocs` |
| 적합한 상황 | 빠른 파일 교체 | 개발 중 파일 직접 반영 | DB/로그 등 보존 데이터 |

## 수업 예제

```bash
docker cp docker/host2container/index.html apache01-ctr:/usr/local/apache2/htdocs/index.html
docker cp apache01-ctr:/usr/local/apache2/htdocs/index.html ~/docker/host2container/hello.html
```

```bash
docker container run --name apache02-ctr -d -p 8090:80 -v ~/bind_mount:/usr/local/apache2/htdocs httpd
```

```bash
docker volume create mount-vol
docker container run --name apache03-ctr -d -p 8090:80 -v mount-vol:/usr/local/apache2/htdocs httpd
docker volume inspect mount-vol
```

## 언제 무엇을 쓰는가

- 컨테이너 안의 파일을 잠깐 교체하거나 꺼내오려면 `docker cp`.
- 로컬에서 파일을 계속 수정하면서 컨테이너에 바로 반영하려면 bind mount.
- 컨테이너가 삭제되어도 DB 데이터나 로그를 남기려면 volume mount.

## 헷갈리기 쉬운 포인트

- `docker cp`는 복사라서 이후 원본 변경이 자동 반영되지 않는다.
- bind mount는 빈 호스트 폴더를 컨테이너 웹 루트에 연결하면 컨테이너 안도 비어 보일 수 있다.
- volume의 실제 `Mountpoint`는 Docker 관리 영역이므로 직접 수정하기보다 컨테이너를 통해 다루는 편이 안전하다.
- Apache는 빈 디렉터리에서 `Index of /`가 보일 수 있지만, nginx는 파일이 없으면 403 Forbidden이 날 수 있다.

## 관련 페이지

- [[concepts/docker-cp-exec-container-files|Docker exec/cp와 컨테이너 파일 다루기]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[summaries/2026-04-29-docker-network-volume-image|2026-04-29 Docker 네트워크, 볼륨, 사용자 정의 이미지]]
- [[entities/docker|Docker]]

## 출처

- `raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md`
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf` — volume/bind mount 개념
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf` — host↔container 복사, bind mount, volume mount 실습
