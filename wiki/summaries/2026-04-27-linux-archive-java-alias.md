---
title: 2026-04-27 Linux 압축, 다운로드, Java 실행 준비
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [linux, java, backend, curriculum, study-log]
sources:
  - raw/Study/5. Linux/2026.04.27(월)/2026.04.27(월).md
  - raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf
  - raw/Study/5. Linux/교육 자료/Linux/Linux 이론.pdf
  - raw/Study/5. Linux/교육 자료/Github 교안(실습).pdf
  - raw/Study/5. Linux/교육 자료/Linux/Linux 실습(Librarian).pdf
status: growing
confidence: high
---

# 2026-04-27 Linux 압축, 다운로드, Java 실행 준비

## 한 줄 요약

`wget`/`curl` 다운로드, `tar`/`zip` 압축, `rm -rf` 삭제, alias와 `.bashrc`, JDK/JDBC, GitHub 기초, Apache/Nginx 웹서버 구동까지 Linux 서버 준비 흐름을 폭넓게 다룬 날이다.

## 배운 내용

- `wget`과 `curl -L -o`로 GitHub의 `.tar.gz` 파일을 내려받았다.
- `tar -xzvf`로 `.tar.gz`를 압축 해제했다.
- Windows에서 MobaXterm drag-and-drop으로 파일을 옮길 때 root가 만든 디렉터리라면 `chown`으로 소유권을 바꿔야 했다.
- `zip -r`, `unzip`, `rm`, `rm -rf`로 압축과 삭제를 실습했다.
- `alias`는 세션 한정이고, 지속하려면 `.bashrc`에 추가해야 한다는 점을 배웠다.
- `openjdk-17-jdk`, MySQL JDBC driver, `javac -cp`, `java -cp`로 Linux에서 Java 실행을 준비했다.
- GitHub 교안 흐름으로 work tree, stage, repository, push/pull의 기본 구도를 봤다.
- Apache/Nginx 웹서버 설치와 `/var/www/html/` 문서 교체, UFW 방화벽, 포트 번호 80/443/22를 다뤘다.

## 핵심 실습 / 예제

```bash
mkdir -p ~/downloads/wgettest
cd ~/downloads/wgettest
wget https://github.com/vim/vim/archive/refs/tags/v9.1.0000.tar.gz
tar -xzvf v9.1.0000.tar.gz
curl -L -o vim.tar.gz https://github.com/vim/vim/archive/refs/tags/v9.1.0000.tar.gz
sudo chown -R broadcast:broadcast /home/broadcast/downloads/fromwindows/
zip -r morning_garden.zip .
rm -rf vim-9.1.0000/
alias head3='head -n 3 java.txt'
cat alias_test.sh >> .bashrc
sudo apt install -y openjdk-17-jdk
wget https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/8.4.0/mysql-connector-j-8.4.0.jar
sudo apt install -y apache2
sudo ufw allow 80/tcp
sudo apt install -y nginx
```

## 왜 중요한가

서버 배포는 “파일을 가져오고, 풀고, 필요한 프로그램을 설치하고, 포트를 열고, 서비스를 실행하는 일”의 반복이다. 이 날은 이후 Maven 패키징, Docker 설치, GitHub clone, 웹서버 구동의 기반을 만들었다.

## 헷갈린 점 / 질문

- `apt install`은 패키지 설치, `wget`/`curl`은 파일 다운로드다.
- `rm -rf`는 디렉터리도 강제로 지우므로 실습 경로를 반드시 확인해야 한다.
- alias는 현재 shell에만 살아 있고, 새 접속에서도 쓰려면 `.bashrc`에 넣어야 한다.
- Apache의 기본 DocumentRoot는 `/var/www/html/`이다.
- Git의 stage는 “커밋할 변경을 올려두는 중간 영역”이다.

## 관련 페이지

- [[concepts/linux-package-archive|Linux 패키지·다운로드·압축]]
- [[concepts/linux-web-server-apache-nginx|Linux Apache/Nginx 웹서버]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]]

## 출처

- `raw/Study/5. Linux/2026.04.27(월)/2026.04.27(월).md`
- `raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf` — p.153~170 다운로드/압축/alias/Java, p.177~194 Apache/Nginx
- `raw/Study/5. Linux/교육 자료/Linux/Linux 이론.pdf` — apt, systemctl, ufw, mount/file system 개념
- `raw/Study/5. Linux/교육 자료/Github 교안(실습).pdf` — Git work tree/stage/repository/push/pull 기본 구조
- `raw/Study/5. Linux/교육 자료/Linux/Linux 실습(Librarian).pdf`
