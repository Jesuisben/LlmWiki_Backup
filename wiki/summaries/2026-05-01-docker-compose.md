---
title: 2026-05-01 Docker Compose와 다중 service 실행
created: 2026-07-06
updated: 2026-07-16
type: summary
tags: [linux, docker, spring-boot, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md
status: growing
confidence: high
---

# 2026-05-01 Docker Compose와 다중 service 실행

## 한 줄 요약

전날 수동으로 만들었던 MySQL·Spring Boot의 image·network·volume·environment·port 관계를 Compose YAML에 선언하고 `up` 한 번으로 생성한 뒤, 상태·DB·browser 결과와 `down` 이후 남는 자원을 확인했다.

## 왜 이 순서로 배웠는가

04-30에는 network 생성, MySQL 실행, Spring JAR build, image build, Spring container 실행을 각각 명령으로 수행했다. 구성 요소가 늘어날수록 이름·network·volume·환경 변수·실행 순서를 빠뜨리기 쉬워진다. Compose는 이 관계를 manifest로 저장해 같은 묶음을 반복해서 올리고 내리기 위해 배웠다.

오전의 MySQL+Spring Boot 실습으로 실제 application 구성을 선언한 뒤, Docker Desktop에서 같은 image/container를 GUI로 확인했다. 오후에는 backend 시험을 별도 범위로 치르고, 마지막에 새 VM에서 MySQL+WordPress Compose를 다시 구성하면서 잘못된 YAML 들여쓰기와 설정값을 수정했다.

## 교시별 학습 전개

### 1교시 — Compose manifest와 MySQL+Spring Boot

#### manifest가 대신한 수동 작업

기존에는 `docker container run`을 service마다 실행하고 network와 volume도 따로 만들었다. 이날 manifest에는 다음을 한 파일에 선언했다.

| YAML 항목 | 이날의 책임 |
|---|---|
| `services` | `mysql-svc`, `spring-svc`라는 실행 단위 정의 |
| `image` | MySQL 8.0과 전날 만든 Spring Boot image 선택 |
| `networks` | 두 service를 `spring-mysql-net`에 연결 |
| `volumes` | MySQL 데이터를 `mysql-spring-vol`에 보존 |
| `environment` | DB 생성·사용자와 Spring profile·datasource 설정 전달 |
| `ports` | host 3306·9000과 service port 연결 |
| `depends_on` | Spring service가 MySQL service 뒤에 시작하도록 의존 관계 표시 |

YAML은 tab 대신 space 들여쓰기를 사용했고, service 이름과 `container_name`을 구분했다. Spring datasource URL의 host에는 `mysql-svc`라는 service 이름을 사용했다.

#### 실행과 확인

1. 전날 만든 `myspring-img`가 있는지 확인하고, 없으면 Dockerfile로 build한다.
2. `compose_mysql_springboot.yml`을 작성한다.
3. project 이름과 manifest 경로를 지정해 `docker compose ... up -d`를 실행한다.
4. 출력에서 MySQL image pull, network·volume 생성, MySQL·Spring container 생성을 확인한다.
5. `docker container ps -a` 형식 출력에서 두 container가 `Up`인지 확인한다.
6. MySQL container에서 `coffee` DB에 product sample row를 넣고 commit·select한다.
7. image가 보이지 않으면 Spring container에 image directory를 복사한 뒤 browser 9000 포트에서 화면을 확인한다.
8. 같은 manifest로 `down`해 container와 network를 내린다.

`down` 뒤에도 image와 volume은 자동 삭제되지 않는다고 확인했다. 따라서 “서비스를 내림”과 “데이터·image까지 제거함”은 다른 작업이다. 실제 volume 삭제는 별도로 수행했다.

#### 확인 범위의 한계

원본에는 `up` 출력과 `docker container ps -a`, DB 입력·조회, browser 확인이 있다. 이 날짜에 `docker compose logs`를 실행한 기록은 없다. Spring log 확인은 04-30의 `docker logs -f spring-ctr` 실습에 속하므로 이날 실행한 것처럼 합치지 않는다.

### 2교시 — 기록 공백

원본에는 `이어서 작성`만 있다. 1교시 실습의 추가 결과를 임의로 만들지 않는다.

### 3~5교시 — Docker Desktop 설치와 GUI 확인

- Windows version 확인, WSL2와 Virtual Machine Platform 활성화, kernel update, Docker Desktop 설치·재부팅 순서를 정리했다.
- 권한 문제로 설치되지 않을 때 Docker 관련 process와 ProgramData의 잔여 directory를 확인하는 troubleshooting 메모가 있다.
- Docker Desktop terminal에서 Apache container를 실행했다.
- GUI의 Containers·Images 영역에 생성 결과가 보이는지 확인하고 stop·delete·image delete를 수행했다.

Docker Desktop은 Docker 개념을 대신하는 별도 orchestration 도구가 아니라, 같은 container/image 상태를 Windows GUI와 terminal에서 확인하는 실행환경으로 다뤘다.

### 6교시 — backend 시험 경계

이 시간에는 Servlet/JSP, Spring MVC, dependency injection, JPA annotation, Service/Repository, REST Controller 등을 묻는 20문항 backend 시험을 치렀다. Docker Compose 실습의 일부가 아니며, [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 수업]]을 평가한 별도 학습 활동이다.

따라서 이날 Summary에는 “시험을 치렀다”는 경계만 보존하고, 시험 문항을 Compose의 기능이나 Docker 실행 결과로 해석하지 않는다.

### 7교시 — 새 VM에서 MySQL+WordPress Compose 반복 실습

- Gomdori VM을 만들고 bridge network·OpenSSH·UFW·MobaXterm session을 준비했다.
- Docker setup script의 CRLF를 `dos2unix`로 고치고 실행 권한을 부여했다.
- 일반 사용자를 Docker group에 넣고 permission denied가 나면 logout/login 후 `docker version`을 다시 확인했다.
- MySQL과 WordPress를 `network01`, DB·WordPress용 named volume, environment, `depends_on`, port로 연결하는 YAML을 사용했다.
- 제공 manifest의 들여쓰기와 실제 요구사항이 맞지 않아 수정본을 만들었다는 기록을 보존했다.
- `up -d` 뒤 browser 8085 포트에서 WordPress를 확인하고, `down` 뒤 image·volume을 별도 삭제했다.

이 두 번째 실습은 Compose가 Spring Boot 전용이 아니라 DB와 다른 web application의 다중 service 관계에도 같은 방식으로 적용된다는 점을 보여 준다.

### 8교시 — 다음 Git/GitHub 수업 예고

마지막에는 다음 주에 GitHub 협업을 배우고 추가 계정을 준비할 수 있다는 메모만 있다. branch·PR·conflict의 직접 학습은 [[summaries/2026-05-04-git-github-sourcetree|05-04]]와 [[summaries/2026-05-06-github-branch-pr-conflict|05-06]]에 귀속한다.

## 대표 실습: YAML 한 파일에서 application 묶음 복원

### 입력

- 미리 build한 Spring Boot image
- MySQL image
- service·network·volume·environment·port 관계가 적힌 YAML

### 처리

Compose가 project prefix를 붙인 network와 volume을 만들고, MySQL과 Spring container를 순서에 맞춰 시작했다. Spring은 service 이름으로 DB를 찾고, MySQL volume은 container 밖에 데이터를 두었다.

### 결과

- `up` 출력에서 image·network·volume·container 생성 확인
- 상태 목록에서 두 container의 `Up` 확인
- MySQL에서 product row 입력·조회
- browser에서 Spring 화면 확인
- `down` 후 container·network 제거, image·volume 잔존 확인

이 흐름은 단순히 container 두 개가 “보인다”는 GUI 확인보다, 선언한 관계가 실제 DB와 browser 왕복으로 이어지는지를 확인한 실습이다.

## 헷갈리기 쉬운 지점

- **Dockerfile과 Compose:** Dockerfile은 image를 만드는 recipe이고 Compose는 준비된 image들을 service 관계로 실행하는 manifest다. Compose의 `build`가 image build를 호출할 수 있어도 두 책임이 같아지는 것은 아니다.
- **`depends_on`과 readiness:** 시작 순서를 표현하지만 DB가 query를 받을 준비까지 끝났음을 보장하는 health check는 이날 구성하지 않았다.
- **service 이름과 container 이름:** Compose 내부 DNS와 `depends_on`은 service 이름을 기준으로 이해해야 한다. 화면에 보이는 container 이름과 항상 같은 개념은 아니다.
- **`down`과 데이터 삭제:** 기본 `down` 후 volume·image가 남을 수 있다. 데이터 지속성과 자원 정리 범위를 옵션별로 확인해야 한다.
- **YAML 들여쓰기:** 잘못된 들여쓰기나 서로 맞지 않는 network 이름은 manifest가 실행되지 않거나 service 연결을 깨뜨릴 수 있다.
- **Docker Desktop의 GUI:** container가 보이는 것과 application·DB 연결이 정상이라는 것은 다르다. 상태, DB, browser를 각각 확인해야 한다.
- **Compose와 운영 orchestration:** 이날은 한 host의 로컬 다중 container 구성이다. CI/CD pipeline, rolling deployment, cluster scheduling까지 자동 해결한 것은 아니다.

## 이전·다음 연결과 과목 경계

- 이전: [[summaries/2026-04-30-dockerfile-spring-load-balancing|04-30]]의 수동 network·MySQL·Spring image/container 구성을 YAML로 옮겼다.
- 다음: [[summaries/2026-05-04-git-github-sourcetree|05-04]]에는 실행환경 관리에서 source 변경 이력과 remote 협업 관리로 전환한다.
- 후속 Docker: Passwordless의 Docker server와 프로젝트 로컬 통합환경에서도 Compose가 활용되지만, 이날 결과를 후속 service의 직접 구현으로 확대하지 않는다.
- 후속 CI/CD: Compose 파일이 있다고 build·test·registry push·production deploy가 자동화되는 것은 아니다. 그 책임은 [[concepts/ci-cd-automation|CI/CD 자동화]]에서 별도로 배운다.

## 관련 페이지

- [[concepts/docker-compose-manifest|Docker Compose manifest]]
- [[concepts/dockerfile-vs-compose|Dockerfile vs Docker Compose]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[comparisons/docker-cp-vs-bind-mount-vs-volume|docker cp vs bind mount vs volume]]
- [[entities/docker|Docker]]
- [[concepts/docker-install-permission-setup|Docker 설치와 권한 설정]]

## 출처

- `raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md`

날짜 MD에 MySQL+Spring Boot와 MySQL+WordPress manifest·실행 결과가 충분히 전사되어 있어 보조 교안을 page source로 강제하지 않았다. 실제 credential·계정·IP는 재노출하지 않았다.
