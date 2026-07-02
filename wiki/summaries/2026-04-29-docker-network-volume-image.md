---
title: 2026-04-29 Docker 네트워크, 볼륨, 사용자 정의 이미지
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [linux, backend, curriculum, study-log]
sources:
  - raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md
status: growing
confidence: high
---

# 2026-04-29 Docker 네트워크, 볼륨, 사용자 정의 이미지

## 한 줄 요약

MariaDB와 Redmine 컨테이너를 같은 Docker 네트워크에 연결하고, bind mount/volume mount로 컨테이너 데이터와 호스트 파일을 연결하며, 컨테이너 변경분을 이미지로 만드는 흐름을 배웠다.

## 배운 내용

- `docker network create network02`로 컨테이너 간 통신용 네트워크를 만들었다.
- MariaDB 컨테이너를 먼저 만들고, Redmine 컨테이너가 DB 컨테이너 이름을 바라보게 연결했다.
- 컨테이너, 이미지, 네트워크를 확인하고 정리하는 명령을 사용했다.
- `docker exec`로 컨테이너 내부 명령을 실행했다.
- `docker cp`로 호스트와 컨테이너 사이 파일을 복사했다.
- bind mount와 volume mount의 차이를 배웠다.
- Apache/nginx 컨테이너의 웹 루트 파일을 바꿔 화면 변화를 확인했다.
- 컨테이너를 기반으로 사용자 정의 이미지를 만들고 Docker Hub 업로드 흐름을 소개받았다.

## 핵심 실습 흐름

```bash
docker network create network02
docker run --net=network02 --name=mariadb02 -dit -e MYSQL_ROOT_PASSWORD=My@Sql01 mariadb
docker run --net=network02 --name=redmine02 -dit -p=8883:3000 -e REDMINE_DB_MYSQL=mariadb02 redmine
docker container ls -a
docker container stop mariadb02 redmine02
docker container rm mariadb02 redmine02
```

## 왜 중요한가

실제 서비스는 웹 서버 하나만으로 끝나지 않고 DB, 캐시, 파일 저장소 등 여러 실행 단위가 연결된다. Docker 네트워크는 컨테이너끼리 이름으로 통신하게 해 주고, 볼륨/마운트는 컨테이너가 사라져도 필요한 데이터나 파일을 유지하는 방법이다.

## 헷갈린 점 / 질문

- 컨테이너끼리 통신하려면 네트워크가 먼저 있어야 한다. 원본에도 “네트워크가 있어야 컨테이너가 의미가 있어서 항상 네트워크 먼저 만들기”라고 강조되어 있다.
- 컨테이너 내부 파일을 직접 수정하면 컨테이너 삭제 시 사라질 수 있다. 유지가 필요하면 mount나 이미지화가 필요하다.
- image 삭제는 해당 image를 쓰는 container 정리 후 가능하다.

## 관련 페이지

- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[entities/docker|Docker]]

## 출처

- `raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md`
