---
title: 2026-04-28 Maven, Spring Boot 서버 실행, Docker 입문
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [linux, spring-boot, backend, curriculum, study-log]
sources:
  - raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md
status: growing
confidence: high
---

# 2026-04-28 Maven, Spring Boot 서버 실행, Docker 입문

## 한 줄 요약

Linux 서버에서 Maven으로 Spring Boot 프로젝트를 패키징하고 `java -jar`로 실행한 뒤, Docker 이미지·컨테이너 개념과 기본 컨테이너 실행을 시작했다.

## 배운 내용

- 기존 웹 서버 포트 충돌을 막기 위해 `systemctl stop/disable nginx`, `apache2`를 정리했다.
- GitHub에서 Spring Boot 예제 프로젝트를 clone하고 Maven을 설치했다.
- `mvn clean package -DskipTests`로 `.jar` 파일을 만들고, `target/`에서 결과물을 확인했다.
- 방화벽과 포트 리다이렉션을 설정해 브라우저에서 Spring Boot 실행 결과를 확인했다.
- Docker 이미지를 “밀키트/템플릿”, 컨테이너를 “이미지로 실제 실행한 인스턴스”에 비유해 배웠다.
- Docker 설치·설정 후 Apache, MariaDB, nginx 등 컨테이너를 실행·삭제·내부 수정했다.

## 핵심 실습 흐름

```bash
sudo apt install -y maven
mvn -v
mvn clean package -DskipTests
cd target
ls *.jar
sudo ufw allow 9000/tcp
```

Docker 쪽에서는 이미지 pull/run, 컨테이너 목록 확인, 컨테이너 내부 파일 수정, DB 컨테이너 실행을 실습했다.

## 왜 중요한가

지금까지는 IDE에서 Spring Boot를 실행했다면, 이 날부터는 Linux 서버에서 빌드 산출물 `.jar`를 직접 실행하는 배포 관점으로 이동한다. Docker는 이 실행 환경을 이미지로 고정하고 컨테이너로 반복 실행하기 위한 다음 단계다.

## 헷갈린 점 / 질문

- `mvn clean package`는 소스 코드를 배포 가능한 `.jar`로 빌드하는 명령이지 서버를 실행하는 명령이 아니다.
- `pom.xml`이 있는 프로젝트 루트에서 Maven 명령을 실행해야 한다.
- Docker 이미지와 컨테이너는 클래스와 객체처럼 생각하면 쉽다. 이미지는 실행 템플릿, 컨테이너는 실행 중이거나 생성된 실제 단위다.

## 관련 페이지

- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[entities/maven|Maven]]
- [[entities/docker|Docker]]

## 출처

- `raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md`
