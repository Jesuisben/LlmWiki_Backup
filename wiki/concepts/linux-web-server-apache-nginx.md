---
title: Linux Apache/Nginx 웹서버
created: 2026-07-02
updated: 2026-07-13
type: concept
tags: [linux, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
status: growing
confidence: high
---

# Linux Apache/Nginx 웹서버

## 정의

Apache와 Nginx는 HTTP 요청을 받아 정적 파일을 응답하거나, 뒤쪽 애플리케이션 서버로 요청을 전달하는 웹 서버다.

## 왜 중요한가

Spring Boot 서버를 직접 9000번 포트로 노출할 수도 있지만, 실제 배포에서는 Nginx가 80/443번 포트에서 요청을 받고 Spring Boot나 여러 컨테이너로 전달하는 구조가 자주 쓰인다.

## 핵심 설명

- Apache/httpd와 Nginx는 정적 HTML을 제공하는 웹서버로 실습했다.
- `/var/www/html/` 또는 컨테이너 내부 htdocs 경로에 `index.html`을 두고 브라우저로 확인했다.
- `systemctl stop nginx/apache2`로 기존 웹서버가 포트를 점유하지 않게 했다.
- Docker 실습에서는 Nginx를 reverse proxy와 load balancer로 사용했다.

## 예시

```bash
sudo systemctl stop nginx
sudo systemctl disable nginx
sudo systemctl stop apache2
sudo ufw allow 80
```

Docker 컨테이너 예시는 다음 흐름으로 이어진다.

```bash
docker run --name nginx01 -d -p 8080:80 nginx
docker exec -it nginx01 /bin/bash
```

## 자주 헷갈리는 점

- Apache/Nginx는 Spring Boot 자체가 아니다. 앞단에서 정적 파일을 주거나 reverse proxy 역할을 맡을 수 있다.
- 같은 포트를 두 프로세스가 동시에 사용할 수 없으므로 포트 충돌을 먼저 확인해야 한다.
- Docker 안의 Nginx와 Linux host에 설치한 Nginx는 서로 다른 실행 단위다.

## 관련 개념

- [[concepts/docker-reverse-proxy-load-balancing|Docker reverse proxy와 로드 밸런싱]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/aws-ec2-nginx-spring-deploy|AWS EC2에서 Nginx와 Spring Boot 배포]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md`
