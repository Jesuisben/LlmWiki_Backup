---
title: 2026-04-28 Maven, Spring Boot 서버 실행, Docker 입문
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [linux, backend, spring-boot, curriculum, study-log]
sources:
  - raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
status: growing
confidence: high
---

# 2026-04-28 Maven, Spring Boot 서버 실행, Docker 입문

## 한 줄 요약

Linux에서 Spring Boot 프로젝트를 Maven으로 패키징해 `.jar`로 실행하고, Docker의 이미지/컨테이너 개념과 설치·초기 컨테이너 실행을 배운 날이다.

## 배운 내용

- 기존 nginx/apache2를 중지해 포트 충돌을 줄이고 Spring Boot 서버 실행을 준비했다.
- GitHub에서 Spring Boot 예제 프로젝트를 clone하고 `application.properties`의 `server.port=9000`을 확인했다.
- `iptables`로 80번 요청을 9000번으로 redirect하는 포트 리디렉션 개념을 봤다.
- `ufw allow 9000/tcp`로 Spring Boot 포트를 열었다.
- `mvn clean package -DskipTests`로 `.jar`를 만들고 `java -jar`로 실행했다.
- Docker 이론 교안의 이미지/컨테이너 개념을 “클래스/객체”, “밀키트/실행 결과” 비유로 이해했다.
- `docker_setup.sh.txt`를 `/root/docker_setup.sh`로 복사하고, Windows CRLF 문제를 `dos2unix`로 해결했다.
- `usermod -aG docker $USER` 후 재로그인해야 일반 사용자가 Docker 명령을 쓸 수 있음을 배웠다.
- `httpd`, `nginx`, `mysql` 이미지를 이용해 컨테이너 실행·중지·삭제를 실습했다.

## 핵심 실습 / 예제

```bash
sudo systemctl stop nginx
sudo systemctl disable nginx
sudo apt install -y maven
mvn clean package -DskipTests
cd target
java -jar shopping-0.0.1-SNAPSHOT.jar
sudo cp docker_setup.sh.txt /root/docker_setup.sh
sudo su -
apt install dos2unix -y
dos2unix docker_setup.sh
chmod +x docker_setup.sh
./docker_setup.sh
exit
sudo usermod -aG docker $USER
docker version
docker container run --name apache01 -d -p 8888:80 httpd
docker container stop apache01
docker container rm apache01
```

## 왜 중요한가

Linux에서 직접 `.jar`를 실행하는 방식은 수동 배포의 기본이고, Docker는 이 실행 환경을 이미지로 고정하는 다음 단계다. 즉 이 날은 “서버에서 직접 실행”에서 “컨테이너로 실행”으로 넘어가는 전환점이다.

## 헷갈린 점 / 질문

- Maven은 서버가 아니라 빌드 도구다. `mvn package`는 jar 생성, `java -jar`는 실행이다.
- Docker 설치 스크립트는 Windows에서 만든 파일이라 CRLF 문제로 바로 실행되지 않을 수 있다.
- Docker 그룹에 추가해도 현재 세션에는 바로 반영되지 않을 수 있어 logout/login이 필요하다.
- `-p 8888:80`은 호스트 8888번 포트를 컨테이너 80번 포트에 연결한다.

## 관련 페이지

- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/docker-install-permission-setup|Docker 설치와 권한 설정]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[entities/maven|Maven]]
- [[entities/docker|Docker]]

## 출처

- `raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md`
- `raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf` — Spring Boot 서버 실행, Maven, 웹서버 관련 실습
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf` — Docker 이미지/컨테이너 개념, 주요 이미지
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf` — Docker 설치, Apache/nginx/MySQL 컨테이너 실행
