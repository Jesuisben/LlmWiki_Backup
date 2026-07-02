---
title: Linux Apache/Nginx 웹서버
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [linux, backend]
sources:
  - raw/Study/5. Linux/2026.04.27(월)/2026.04.27(월).md
  - raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf
  - raw/Study/5. Linux/교육 자료/Linux/Linux 이론.pdf
status: growing
confidence: high
---

# Linux Apache/Nginx 웹서버

## 정의

Apache와 Nginx는 HTTP 요청을 받아 HTML, 이미지, CSS 같은 웹 문서를 응답하는 웹 서버다. Linux 수업에서는 정적 홈페이지 파일을 `/var/www/html/`에 배치해 VM IP로 접속하는 실습을 했다.

## 수업 흐름

1. `apt update` 후 Apache 또는 Nginx를 설치했다.
2. `systemctl enable/start/status`로 서비스를 자동 시작 설정·실행·상태 확인했다.
3. UFW에서 80/443/22 포트를 허용했다.
4. MobaXterm으로 `my_homepage.zip`을 옮기고 압축을 풀었다.
5. Apache 기본 `index.html`을 백업한 뒤 내 홈페이지 파일로 교체했다.
6. Nginx도 GitHub에서 받은 정적 파일을 `/var/www/html/`에 복사해 확인했다.

## 핵심 명령어

```bash
sudo apt update
sudo apt install -y apache2
sudo systemctl enable apache2
sudo systemctl start apache2
sudo systemctl status apache2
sudo ufw enable
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow ssh
mkdir myhomepage
unzip my_homepage.zip
sudo cp /var/www/html/index.html /var/www/html/index.bak
sudo cp -r ./* /var/www/html/
sudo systemctl stop apache2
sudo apt install -y nginx
sudo systemctl start nginx
sudo cp -r ./* /var/www/html/
```

## 왜 중요한가

Spring Boot 이전의 기본 웹 서버 구조를 이해하면, 이후 reverse proxy, load balancing, Docker의 Apache/nginx 컨테이너, Spring Boot 포트 충돌을 더 쉽게 이해할 수 있다.

## 자주 헷갈리는 점

- Apache 패키지 이름은 Ubuntu에서 `apache2`다.
- `/var/www/html/`은 웹 서버가 기본으로 보여주는 문서 디렉터리다.
- 80은 HTTP, 443은 HTTPS, 22는 SSH 포트다.
- UFW를 켠 뒤 SSH를 허용하지 않으면 MobaXterm 접속이 끊길 수 있다.
- VirtualBox NAT를 쓰면 포트 포워딩, Bridge를 쓰면 VM IP 접근을 구분해야 한다.

## 관련 페이지

- [[summaries/2026-04-27-linux-archive-java-alias|2026-04-27 Linux 압축, 다운로드, Java 실행 준비]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/docker-reverse-proxy-load-balancing|Docker reverse proxy와 로드 밸런싱]]
- [[entities/linux|Linux]]

## 출처

- `raw/Study/5. Linux/2026.04.27(월)/2026.04.27(월).md`
- `raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf` — p.177~194 Apache/Nginx 실습
- `raw/Study/5. Linux/교육 자료/Linux/Linux 이론.pdf` — systemctl, httpd, ufw 개념
