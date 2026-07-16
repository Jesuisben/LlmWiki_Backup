---
title: Docker Compose manifest
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [linux, docker, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md
status: growing
confidence: high
---

# Docker Compose manifest

## 이 페이지의 책임

이 페이지는 2026-05-01 수업에서 **MySQL+Spring Boot와 MySQL+WordPress의 service 관계를 YAML로 선언하고 올리고 내린 과정**을 설명한다. Dockerfile image build, DB readiness, CI/CD, 운영 cluster orchestration은 Compose manifest가 자동 해결한 것으로 확대하지 않는다.

## 정의와 필요성

Docker Compose manifest는 여러 container와 network·volume·environment·port 관계를 YAML 한 파일에 선언한 문서다. 04-30에는 network 생성, DB 실행, Spring image build, application 실행을 각각 수행했다. 05-01에는 반복할 관계를 파일로 남기고 `up`과 `down`으로 같은 project 단위를 관리했다.

## YAML 항목의 실제 책임

| 항목 | 수업에서 맡은 역할 | 오해하지 않을 것 |
|---|---|---|
| `services` | MySQL·Spring 또는 MySQL·WordPress 실행 단위 정의 | service 이름은 image나 container 이름과 동일 개념이 아님 |
| `image` | 미리 준비된 image 선택 | Dockerfile을 자동 작성하거나 항상 build하지 않음 |
| `container_name` | 실제 container 표시 이름 지정 | service discovery의 기본 식별 책임과 구분 |
| `networks` | 같은 project network에 service 연결 | host/browser 공개 port와 별도 |
| `volumes` | DB·WordPress 데이터를 container 밖에 연결 | `down`만으로 기본 삭제되지 않음 |
| `environment` | DB 생성 정보와 application 연결 설정 전달 | secret 관리가 해결된 것은 아님 |
| `ports` | host port와 container port 연결 | container 간 이름 기반 통신과 별도 |
| `depends_on` | service 시작 순서 의존 표현 | DB가 query 가능한 readiness까지 보장하지 않음 |
| `restart` | container 재시작 정책 선언 | application 정상 동작이나 무한 복구 보장 아님 |

## 실습 1: MySQL + Spring Boot

### 실제 manifest 관계

| 구분 | MySQL service | Spring Boot service |
|---|---|---|
| service 이름 | `mysql-svc` | `spring-svc` |
| container 이름 | `mysql-ctr` | `spring-ctr` |
| image | `mysql:8.0` | 전날 Dockerfile로 만든 `myspring-img:latest` |
| network | `spring-mysql-net` | `spring-mysql-net` |
| volume | `mysql-spring-vol` → MySQL data 경로 | manifest에는 image volume이 없고 나중에 파일을 별도 복사 |
| port | host 3306 → MySQL 3306 | host 9000 → Spring 9000 |
| environment | DB·application 사용자와 DB 생성 설정 | active profile·datasource URL·DB 사용자 설정 |
| 의존 | 없음 | `mysql-svc`에 `depends_on` |

Spring datasource host는 `localhost`나 `mysql-ctr`가 아니라 service 이름 `mysql-svc`로 기록됐다. 반면 상태 목록에는 `container_name`으로 지정한 `mysql-ctr`, `spring-ctr`가 보였다. service 이름은 Compose 내부 관계·DNS를 읽는 기준이고, container 이름은 실제 실행 객체를 식별하는 이름이다.

### 입력 → 처리 → 결과

1. **입력**: 미리 build한 Spring image와 MySQL image, 두 service의 network·volume·environment·port 관계를 적은 manifest.
2. **처리**: project 이름을 지정한 `up -d`가 MySQL image를 받고 project network·volume과 두 container를 생성했다.
3. **상태 확인**: 생성 출력과 container 상태 목록에서 두 container가 `Up`인지 확인했다.
4. **DB 확인**: MySQL prompt에서 DB를 선택해 product row를 입력·commit·조회했다.
5. **application 확인**: image가 보이지 않을 때 Spring container에 image directory를 복사한 뒤 browser 9000 응답을 확인했다.
6. **정리**: 같은 manifest로 `down`해 container·network를 내리고 image·volume 잔존을 구분했다.

원본에는 이 날짜의 `docker compose logs` 실행이 없다. container `Up`, DB row 조회, browser 응답을 각각 확인했지만, log 검증은 04-30 실습에서 수행한 것으로 날짜를 섞지 않는다.

## 실습 2: MySQL + WordPress

새 VM에서 Docker 설치·권한 반영을 다시 거친 뒤 Compose를 반복했다. 이 setup checklist는 Compose 자체 기능이 아니라 manifest를 실행할 host 준비 단계다.

| 구분 | MySQL service | WordPress service |
|---|---|---|
| service/container 이름 | `mysql01` / `mysql01` | `wordpress01` / `wordpress01` |
| image | `mysql:8.0` | `wordpress` |
| network | `network01` | `network01` |
| volume | `volume_mysql` → MySQL data 경로 | `volume_wordpress` → WordPress document root |
| port | host 3306 → MySQL 3306 | host 8085 → WordPress 80 |
| environment | DB 생성·접속 설정 | DB host·DB 이름·사용자 설정 |
| 의존 | 없음 | `mysql01`에 `depends_on` |

제공 manifest는 들여쓰기뿐 아니라 요구사항과 다른 network·설정값이 있어 두 종류의 수정본을 만들었다고 기록돼 있다. 요구사항 표의 WordPress network에는 `networks01`이라는 불일치도 있었고, 최종 수정본은 MySQL과 같은 `network01`을 사용했다. **YAML 문법 오류 수정**과 **실행 요구사항 값 수정**은 서로 다른 범위다.

`up -d` 뒤 browser 8085에서 WordPress를 확인했고 `down`으로 container·network를 내렸다. 다만 원본의 별도 volume 삭제 명령은 manifest의 실제 volume 이름과 다른 이름을 사용하므로, 그 명령으로 해당 project volume이 삭제됐다고 확정하지 않는다.

## 완료 조건을 한 번에 묶지 않기

| 완료 조건 | 확인 기준 | 아직 같지 않은 것 |
|---|---|---|
| manifest parse | YAML 계층·이름 참조가 유효 | container 실행 성공 |
| image 준비 | 참조 image가 local/registry에 존재 | application 시작 |
| Compose `up` | network·volume·container 생성 출력 | DB readiness·업무 기능 성공 |
| container 상태 | MySQL·application이 `Up` | DB login·query 성공 |
| DB readiness | prompt 접속·row 입력·조회 | browser 화면 성공 |
| application 성공 | browser에서 Spring/WordPress 응답 | 운영 배포·health check 완성 |
| Compose `down` | container·network 중지·삭제 | image·volume 삭제 |
| data/image 정리 | 별도 정확한 이름·옵션으로 삭제 | `down`만 실행한 상태 |

`depends_on`은 시작 순서를 표현했지만 health check를 구성하지 않았으므로 DB readiness를 보장하지 않는다. `up`이 성공했다는 출력만으로 application 전체 성공을 판단하지 않고 DB와 browser를 따로 확인한 이유다.

## 자주 헷갈리는 경계

- **Dockerfile과 Compose:** Dockerfile은 image recipe이고 Compose는 image를 service 관계로 실행하는 manifest다. 첫 실습도 image가 없으면 먼저 Dockerfile로 build했다.
- **Compose와 Docker Engine:** Compose가 선언을 해석해도 실제 image/container/network/volume을 만드는 주체는 Docker Engine이다.
- **Compose와 CI/CD:** manifest가 있어도 source test, image build·push, 운영 server 갱신은 자동화되지 않는다.
- **Compose와 운영 orchestration:** 이날은 한 host의 다중 container 실습이다. cluster scheduling, rolling deployment, 고가용성을 구현한 것이 아니다.
- **Docker Desktop:** GUI에 container/image가 보이는 것과 DB/application 왕복이 성공한 것은 다르다.
- **민감 설정:** 수업 manifest에는 실제 credential 값이 있었지만 이 페이지에는 재노출하지 않는다. YAML에 값을 적는 것 자체가 안전한 secret 관리라는 뜻도 아니다.

## 선행·후속 연결

- 선행: [[summaries/2026-04-30-dockerfile-spring-load-balancing|04-30]]의 Dockerfile image·network·수동 container 실행을 manifest로 옮겼다.
- storage: [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]의 network·named volume이 Compose project 자원으로 다시 등장했다.
- 비교: [[concepts/dockerfile-vs-compose|Dockerfile vs Docker Compose]]에서 image 생성과 다중 service 실행 책임을 나눈다.
- 후속: [[concepts/ci-cd-automation|CI/CD 자동화]]와 Passwordless·프로젝트 Compose 활용은 별도 수업·적용 범위다.

## 출처

- `raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md` — 두 manifest의 실제 service·오류 수정·실행·DB·browser·정리 흐름

Docker 실습·이론 PDF와 Compose 종합 실습 메모는 날짜 MD에 전사된 항목과 host setup을 확인하는 보조자료로만 검토했다. 독립 수업일이나 날짜 MD에 없는 성공 결과를 만들지 않았다.