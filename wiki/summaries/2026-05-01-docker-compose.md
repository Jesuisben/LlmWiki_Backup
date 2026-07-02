---
title: 2026-05-01 Docker Compose와 다중 컨테이너 실행
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [linux, backend, curriculum, study-log]
sources:
  - raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
  - raw/Study/5. Linux/교육 자료/도커 컴포즈 종합 실습.md
status: growing
confidence: high
---

# 2026-05-01 Docker Compose와 다중 컨테이너 실행

## 한 줄 요약

Docker Compose manifest로 MySQL+Spring Boot, MySQL+WordPress 같은 다중 컨테이너 구성을 한 번에 만들고, Docker Desktop/WSL2 설치와 Compose YAML 오류 수정까지 경험한 날이다.

## 배운 내용

- Compose manifest는 어떤 컨테이너를 만들고, 어떤 이미지·포트·볼륨·네트워크·환경 변수를 쓸지 적는 YAML 설정 파일이다.
- Dockerfile은 단일 이미지 생성, Compose는 여러 서비스/컨테이너 구성 실행에 초점이 있다.
- `services`, `networks`, `volumes`, `depends_on`, `environment`, `ports`, `restart`의 역할을 봤다.
- `docker compose -p hello -f ... up -d`로 프로젝트명과 파일을 지정해 실행했다.
- Compose `down`은 컨테이너와 네트워크를 중지/삭제하지만 이미지와 볼륨은 별도 삭제가 필요할 수 있다.
- Docker Desktop 설치 과정에서 WSL2 활성화, Linux용 Windows 하위 시스템, 가상 머신 플랫폼, WSL 커널 업데이트를 확인했다.
- `도커 컴포즈 종합 실습.md`와 사용자 메모에서 WordPress+MySQL compose 파일의 잘못된 네트워크/들여쓰기/환경값을 직접 수정한 경험이 남아 있다.
- 같은 날 후반에는 백엔드 시험 문항이 있어 Spring MVC/JPA/Repository/Service/REST 개념 복습도 섞였다. 이 부분은 Linux보다는 Spring Boot 백엔드 복습 자료로 연결된다.

## 핵심 실습 / 예제

```yaml
services:
  mysql-svc:
    container_name: mysql-ctr
    image: mysql:8.0
    networks:
      - spring-mysql-net
    volumes:
      - mysql-spring-vol:/var/lib/mysql
    restart: always
    command: --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
    environment:
      MYSQL_ROOT_PASSWORD: My@Sql01
      MYSQL_DATABASE: coffee
      MYSQL_USER: spring
      MYSQL_PASSWORD: Spring@1234

  spring-svc:
    container_name: spring-ctr
    depends_on:
      - mysql-svc
    image: myspring-img:latest
    networks:
      - spring-mysql-net
    ports:
      - "9000:9000"
    environment:
      SPRING_PROFILES_ACTIVE: docker
      SPRING_DATASOURCE_URL: jdbc:mysql://mysql-svc:3306/coffee
      SPRING_DATASOURCE_USERNAME: spring
      SPRING_DATASOURCE_PASSWORD: Spring@1234

networks:
  spring-mysql-net:

volumes:
  mysql-spring-vol:
```

```bash
docker compose -p hello -f ~/docker/compose01/compose_mysql_springboot.yml up -d
docker container ps -a --format "table {{.Names}}	{{.Status}}"
docker exec -it mysql-ctr /bin/
docker compose -p hello -f ~/docker/compose01/compose_mysql_springboot.yml down
```

## 왜 중요한가

Spring Boot + DB처럼 여러 컨테이너가 함께 필요한 서비스는 `docker run`만으로 재현하기 어렵다. Compose는 실행 구성을 파일로 보존해 팀원·서버·수업 실습 사이에서 같은 환경을 반복 실행하게 해 준다.

## 헷갈린 점 / 질문

- YAML은 tab 대신 space 들여쓰기를 써야 한다.
- `depends_on`은 시작 순서 힌트이지 DB가 완전히 준비될 때까지 애플리케이션을 보장하는 것은 아니다.
- 서비스 이름(`mysql-svc`)과 컨테이너 이름(`mysql-ctr`)의 역할을 구분해야 한다. Compose 내부 네트워크에서는 보통 service 이름을 호스트명처럼 쓴다.
- `down` 후에도 volume이 남으면 DB 데이터가 남을 수 있다.
- WordPress+MySQL compose 실습에서는 자료의 값/들여쓰기 오류를 사용자가 수정한 별도 파일이 있었다.

## 관련 페이지

- [[concepts/docker-compose-manifest|Docker Compose manifest]]
- [[concepts/dockerfile-vs-compose|Dockerfile vs Docker Compose]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[entities/docker|Docker]]

## 출처

- `raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md`
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf` — p.85~91 Compose, up/down, Dockerfile과 Compose 비교
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf` — p.100~121 MySQL+Spring Boot Compose
- `raw/Study/5. Linux/교육 자료/도커 컴포즈 종합 실습.md`
