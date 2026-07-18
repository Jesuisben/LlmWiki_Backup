---
title: 2026-04-30 Dockerfile, Spring Boot 컨테이너와 Nginx 로드 밸런싱
created: 2026-07-06
updated: 2026-07-18
type: summary
tags: [linux, docker, spring-boot, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/KoreaICT/5. Linux/교육 자료/로드 밸런싱.png
status: growing
confidence: high
---

# 2026-04-30 Dockerfile, Spring Boot 컨테이너와 Nginx 로드 밸런싱

## 한 줄 요약

Dockerfile의 build context와 instruction을 실제 image 생성으로 확인한 뒤, Spring Boot JAR와 MySQL을 container network로 연결하고, 별도 VM에서 Nginx reverse proxy가 Apache·Nginx backend 여섯 개로 browser 요청을 분배하는 흐름까지 구현했다.

## 왜 이 순서로 배웠는가

전날 `docker commit`으로 변경된 container를 image로 저장했지만, 그 image가 어떤 base와 파일 복사 절차로 만들어졌는지는 남지 않았다. 그래서 오전에는 Dockerfile로 **재현 가능한 image 생성 절차**를 배웠고, 오후에는 그 image가 실제 Spring Boot+DB service를 실행할 수 있는지 검증했다. 마지막에는 container 하나를 실행하는 데서 더 나아가 여러 web container 앞에 Nginx를 두고 요청을 나누었다.

`Dockerfile → Spring Boot+MySQL → reverse proxy/load balancing` 순서는 image recipe가 실제 다중 server 구성의 기초가 되는 과정을 보여 준다.

## 교시별 학습 전개

### 1교시 — Dockerfile과 build context

- Apache base image에서 시작해 HTML과 이미지를 document root로 복사하는 `Dockerfile01`을 확인했다.
- Dockerfile, HTML, PNG가 같은 build context에 준비돼 있는지 먼저 점검했다.
- `docker build`의 `-f`로 Dockerfile 경로를 지정하고 마지막 `.`으로 현재 directory를 build context로 전달했다.
- build log에서 Dockerfile과 context를 읽고 image를 export한 결과를 확인했다.
- 생성된 image로 container를 실행하고 browser에서 바뀐 홈페이지를 확인했다.
- Nginx base image를 사용한 별도 Dockerfile 실습으로 같은 절차를 혼자 반복했다. 원본의 두 번째 Dockerfile에는 image 복사 destination이 HTML 파일 경로와 겹치는 표기가 있으므로, 이 페이지에서는 성공한 결과를 임의로 보정해 만들지 않는다.

### 2~3교시 — 기록 공백

날짜 MD의 2·3교시는 제목만 있고 실질 내용이 없다. 다른 교시나 PDF 내용을 이 시간대의 직접 실행 결과로 소급하지 않는다.

### 4교시 — Spring Boot JAR image와 MySQL container 연결

실습은 다음 의존 순서를 따랐다.

1. `spring-mysql-net`을 만든다.
2. MySQL container를 같은 network에 실행하고 DB·application용 사용자를 준비한다.
3. Spring project에서 Linux profile과 image 경로 설정을 확인하고 Maven으로 `docker_spring_mysql.jar`를 만든다.
4. Dockerfile로 JAR를 포함한 `myspring-img`를 build한다.
5. Spring container를 같은 network에 실행하면서 DB URL의 host를 MySQL container 이름으로 지정한다.
6. MySQL prompt에서 `product` table과 sample row를 준비한다.
7. container 상태를 확인한 뒤 Spring log 명령과 browser 확인 URL을 기록한다. 실제 log·화면 결과는 원본에 보존되지 않았다.

#### Dockerfile instruction의 실제 역할

| instruction | 이날의 역할 |
|---|---|
| `FROM` | JDK가 포함된 Eclipse Temurin 17 image를 base로 선택 |
| `ARG` | build 시 복사할 `target/*.jar` 경로를 변수로 받음 |
| `COPY` | build context의 JAR를 image 안의 정해진 이름으로 복사 |
| `EXPOSE` | container가 사용할 9000 포트를 문서화 |
| `ENTRYPOINT` | container가 시작될 때 `java -jar`를 자동 실행 |
| `ENV` | 한글 encoding 보조 설정을 image에 추가 |

`EXPOSE 9000`만으로 host에서 접속되는 것은 아니다. 실제 browser 진입에는 container 실행 시 host 9000과 container 9000을 연결하는 port mapping도 필요했다.

#### application과 DB 설정의 연결

- Spring profile은 Linux용 설정을 선택하도록 전달했다.
- datasource URL은 `localhost`가 아니라 같은 Docker network의 `mysql-ctr`를 DB host로 사용했다.
- host의 image directory는 Spring container의 `/images`에 bind mount했다.
- MySQL에서 `coffee` DB, `product` table, sample rows를 준비하고 commit·select로 확인했다.
- credential은 수업 원본에 있지만 이 Summary에서는 역할만 남기고 실제 값을 재노출하지 않는다.

#### 확인 결과

- `docker container ps`에서 Spring과 MySQL이 `Up` 상태였고 Spring은 9000:9000 mapping이 표시됐다.
- Spring log에서 확인해야 할 application 시작 메시지와 DB 원인 예외 기준을 기록했지만 실제 log 출력은 보존되지 않았다.
- browser 확인 URL은 기록됐지만 host 9000 포트의 실제 product 화면 결과는 보존되지 않았다.
- 실습 뒤 두 container를 중지·삭제하고 목록이 비었는지 확인했다.

image build 성공, container `Up`, application log 정상, browser 응답은 서로 다른 확인 단계다. 이날은 앞의 두 단계와 DB row 결과만 보존됐으므로 log·browser 성공까지 확대하지 않는다.

### 5교시 — Nginx reverse proxy와 load balancing

먼저 Bluesky라는 별도 Ubuntu VM을 만들고 bridge network·OpenSSH·UFW를 설정한 뒤 Docker를 설치했다. 일반 사용자를 Docker group에 추가한 뒤 재로그인하여 권한을 반영했다.

그 다음 `proxy-net`에 backend를 준비했다.

- Apache: `apache01`·`apache02`·`apache03`
- Nginx: `nginx04`·`nginx05`·`nginx06`
- proxy: host의 `nginx.conf`를 mount한 `reverse-proxy`

backend container에는 host port를 각각 공개하지 않았다. 같은 `proxy-net`에서 reverse proxy가 container 이름과 80 포트로 접근하게 했다.

`nginx.conf`에는 Apache 세 대의 `backend_apache` upstream과 Nginx 세 대의 `backend_nginx` upstream을 만들었다. `/apache/`는 Apache group, `/nginx/`는 Nginx group, `/`는 기본 Apache group으로 `proxy_pass`했다. reverse proxy container만 host 80 포트에 공개했다.

#### 입력 → 처리 → 결과

- 입력: browser가 VM의 80 포트 또는 `/apache/`, `/nginx/` 경로로 요청한다.
- 처리: reverse proxy Nginx가 `location`과 `proxy_pass`로 upstream group을 선택한다.
- 결과: 새로고침할 때 서로 다른 backend의 구별 가능한 페이지가 번갈아 응답했다.

Apache 한 개와 Nginx 한 개를 중단한 뒤에도 새로고침 테스트를 계속한 기록은 load balancing과 일부 backend 중단 상황을 함께 관찰하려는 실습이었다. 다만 health check 정책이나 운영 수준 장애 조치까지 설정한 기록은 아니다.

### 6~8교시 — 후속 작성 표지만 존재

원본에는 `이어서 작성`만 있고 추가 구현·검증 결과는 없다. 오전·5교시의 결과를 이 시간대까지 확대하지 않는다.

## 그림 자료가 보조한 것

`로드 밸런싱.png`에는 user 다섯 명의 요청이 화살표를 거쳐 상담자 두 명에게 분배되는 비유만 표시된다. “상담자=요청을 처리하는 server/container”라는 직관을 보조할 뿐, 실제 `proxy-net`, upstream 이름, port, mount 구조의 증거는 날짜 MD의 Nginx 실습에서 가져왔다.

## 대표 실습: browser 요청이 backend까지 가는 경로

1. 동일 network에 backend container 여섯 개를 만든다.
2. 각 backend의 홈페이지를 서로 구별할 수 있게 바꾼다.
3. host에 upstream과 `location`이 있는 `nginx.conf`를 작성한다.
4. 설정 파일을 reverse proxy container에 mount하고 이 container만 host 80 포트에 공개한다.
5. browser 요청이 reverse proxy를 거쳐 선택된 upstream의 backend로 전달되는지 새로고침으로 확인한다.

이날 직접 구현한 것은 **Docker network 안의 Nginx reverse proxy**다. [[concepts/aws-route53-load-balancer-https|AWS Load Balancer]]의 Target Group·Listener·cloud health check를 만든 것은 아니다.

## 헷갈리기 쉬운 지점

- **Dockerfile과 build context:** Dockerfile이 어느 경로에 있느냐와 `COPY`가 읽을 수 있는 context 범위는 같은 개념이 아니다. 마지막 `.`을 빠뜨리면 context가 전달되지 않는다.
- **`FROM`과 `ENTRYPOINT`:** `FROM`은 image build의 시작점이고, `ENTRYPOINT`는 만들어진 container가 시작될 때 실행할 process다.
- **`EXPOSE`와 `-p`:** `EXPOSE`는 image의 의도된 port를 나타내고, 외부 접속 경로는 실행 시 port mapping이 만든다.
- **DB host의 `localhost`:** Spring container 안의 localhost는 Spring container 자신이다. 같은 network의 MySQL은 service/container 이름으로 찾는다.
- **reverse proxy와 load balancing:** proxy는 client 대신 backend에 요청을 전달하는 위치이고, upstream 여러 대에 분배하는 구성이 load balancing을 수행한다.
- **Nginx와 AWS Load Balancer:** 요청 분배라는 목적은 이어지지만 실행 주체와 설정 계층이 다르다.

## 이전·다음 연결과 과목 경계

- 이전: [[summaries/2026-04-29-docker-network-volume-image|04-29]]의 commit snapshot·network·mount를 Dockerfile과 실제 Spring Boot+DB image로 확장했다.
- 다음: [[summaries/2026-05-01-docker-compose|05-01]]에는 이날 여러 `run`·network·volume 설정을 YAML manifest 하나로 선언한다.
- 선행: Spring source와 Maven JAR는 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd]]에서 만든 애플리케이션을 Linux/Docker 실행환경으로 옮긴 것이다.
- 후속: AWS의 ALB와 CI/CD Docker 배포는 이 수동 실습을 cloud resource와 workflow automation으로 확장한다.

## 관련 페이지

- [[comparisons/docker-commit-vs-dockerfile|docker commit vs Dockerfile]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/docker-reverse-proxy-load-balancing|Docker reverse proxy와 로드 밸런싱]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[concepts/dockerfile-vs-compose|Dockerfile vs Docker Compose]]
- [[entities/maven|Maven]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md`
- `raw/KoreaICT/5. Linux/교육 자료/로드 밸런싱.png` — 상담자에게 요청을 나누는 비유만 보조

날짜 MD의 실제 교시와 설정을 우선했다. 이미지에는 기술 구성도가 없으므로 port·upstream·network 근거로 사용하지 않았다.
