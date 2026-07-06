---
title: Docker reverse proxy와 로드 밸런싱
created: 2026-07-02
updated: 2026-07-06
type: concept
tags: [linux, docker, backend]
sources:
  - raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/Study/5. Linux/교육 자료/로드 밸런싱.png
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
status: growing
confidence: high
---

# Docker reverse proxy와 로드 밸런싱

## 정의

Reverse proxy는 사용자가 실제 backend 서버와 직접 통신하지 않고 앞단 proxy 서버와 통신하게 만드는 구조이고, load balancing은 요청을 여러 backend로 나누어 보내는 방식이다.

## 왜 중요한가

여러 컨테이너가 각각 서비스를 제공할 때 사용자가 모든 컨테이너 주소를 알 필요는 없다. 앞단 Nginx가 하나의 진입점이 되고, 뒤쪽 서버로 요청을 분산하면 부하와 장애 위험을 줄일 수 있다.

## 수업 구조

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

backend 컨테이너는 외부 포트를 직접 노출하지 않고 같은 Docker network 안에서만 통신하게 구성했다.

## nginx 설정 예시

```nginx
events {}

http {
    upstream backend {
        server apache01:80;
        server apache02:80;
        server apache03:80;
    }

    server {
        listen 80;
        location / {
            proxy_pass http://backend;
        }
    }
}
```

## 자주 헷갈리는 점

- reverse proxy는 “뒤쪽 서버를 대신해 앞에서 요청을 받는 서버”이고, load balancing은 그 요청을 나누어 보내는 전략이다.
- backend 컨테이너 이름은 같은 Docker network 안에서 DNS처럼 사용할 수 있다.
- AWS Load Balancer를 배우기 전에 Docker/Nginx로 같은 구조의 작은 버전을 먼저 경험한 셈이다.

## 관련 개념

- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[concepts/aws-route53-load-balancer-https|AWS Route 53, Load Balancer, HTTPS 흐름]]
- [[comparisons/clb-vs-alb|CLB vs ALB]]

## 출처

- `raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md`
- `raw/Study/5. Linux/교육 자료/로드 밸런싱.png`
