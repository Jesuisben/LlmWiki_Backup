---
title: Docker reverse proxy와 로드 밸런싱
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [linux, backend]
sources:
  - raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/Study/5. Linux/교육 자료/로드 밸런싱.png
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
status: growing
confidence: high
---

# Docker reverse proxy와 로드 밸런싱

## 정의

Reverse proxy는 사용자가 실제 backend 서버와 직접 통신하지 않고 앞단 proxy 서버와 통신하게 만드는 구조다. Load balancing은 앞단 서버가 뒤쪽 여러 서버/컨테이너로 요청을 나누어 보내는 방식이다.

## 수업 비유

`로드 밸런싱.png`는 대기자 명단의 여러 사용자 요청을 두 상담자가 나누어 처리하는 그림이다. 한 상담자에게만 몰리면 부하가 커지고, 한 명에게 문제가 생기면 전체 처리에 영향을 준다. 서버도 마찬가지로 여러 컨테이너에 요청을 분산하면 부하와 장애 위험을 줄일 수 있다.

## 수업 실습 구조

```text
사용자 브라우저
  ↓
reverse-proxy nginx 컨테이너: 80번 포트
  ↓
proxy-net Docker network
  ├─ apache01:80
  ├─ apache02:80
  ├─ apache03:80
  ├─ nginx04:80
  ├─ nginx05:80
  └─ nginx06:80
```

backend 컨테이너는 외부 포트를 직접 노출하지 않고 `--network proxy-net`에만 붙였다. 외부에는 reverse proxy 컨테이너의 80번 포트만 열었다.

## nginx 설정 핵심

```nginx
events {}

http {
    upstream backend_apache {
        server apache01:80;
        server apache02:80;
        server apache03:80;
    }

    upstream backend_nginx {
        server nginx04:80;
        server nginx05:80;
        server nginx06:80;
    }

    server {
        listen 80;

        location /apache/ {
            proxy_pass http://backend_apache/;
        }

        location /nginx/ {
            proxy_pass http://backend_nginx/;
        }

        location / {
            proxy_pass http://backend_apache/;
        }
    }
}
```

## 핵심 명령어

```bash
docker network create proxy-net
docker container run -d --name apache01 --network proxy-net httpd
docker container run -d --name apache02 --network proxy-net httpd
docker container run -d --name apache03 --network proxy-net httpd
docker container run -d --name nginx04 --network proxy-net nginx
docker container run -d --name nginx05 --network proxy-net nginx
docker container run -d --name nginx06 --network proxy-net nginx
sudo vi ~/nginx.conf
docker container run -d --name reverse-proxy --network proxy-net -p 80:80 -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf nginx
```

## 왜 중요한가

실무 배포에서는 사용자가 애플리케이션 서버 각각에 직접 접근하지 않고, nginx 같은 앞단 서버를 통해 접근하는 경우가 많다. 이 구조는 TLS 종료, 보안, 경로 분기, 부하 분산, 무중단 배포의 기초가 된다.

## 자주 헷갈리는 점

- reverse proxy는 앞단에서 요청을 받아 backend로 대신 보내는 서버다.
- load balancing은 여러 backend 후보 중 하나로 요청을 분배하는 동작이다.
- backend 컨테이너에 `-p`를 붙이지 않아도 같은 Docker network 안에서는 reverse proxy가 컨테이너 이름으로 접근할 수 있다.
- `upstream`은 backend 서버 그룹 이름이다.
- `proxy_pass http://backend_apache/;`의 마지막 `/` 유무는 경로 전달 방식에 영향을 줄 수 있다.

## 관련 페이지

- [[summaries/2026-04-30-dockerfile-spring-load-balancing|2026-04-30 Dockerfile, Spring Boot 컨테이너, 로드 밸런싱]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[concepts/linux-web-server-apache-nginx|Linux Apache/Nginx 웹서버]]
- [[entities/docker|Docker]]

## 출처

- `raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md`
- `raw/Study/5. Linux/교육 자료/로드 밸런싱.png`
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf`
