---
title: Dockerfile vs Docker Compose
created: 2026-07-02
updated: 2026-07-18
type: comparison
tags: [linux, docker, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
  - raw/KoreaICT/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
  - raw/KoreaICT/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf
status: stable
confidence: high
---

# Dockerfile vs Docker Compose

## 비교 목적

04-30에는 Dockerfile로 Apache·Nginx와 Spring Boot JAR의 **image 생성 절차**를 적었고, 05-01에는 Compose manifest로 MySQL+Spring Boot·MySQL+WordPress의 **여러 service 실행 관계**를 적었다. 둘 다 Docker 설정 파일이지만 답하는 질문과 생성 artifact가 다르다.

## 한눈에 보기

| 비교 축 | Dockerfile | Docker Compose |
|---|---|---|
| 핵심 질문 | image를 어떤 순서로 만들까? | 여러 service를 어떤 관계로 실행할까? |
| 직접 결과 | build된 image | container·network·volume의 project 실행 상태 |
| 대표 선언 | `FROM`, `COPY`, `RUN`, `ENTRYPOINT` | `services`, `image`, `ports`, `networks`, `volumes`, `environment`, `depends_on` |
| 수업 artifact | `Dockerfile01/02`, `pohang-img`, `myspring-img` | `compose_mysql_springboot.yml`, MySQL·Spring/WordPress service |
| 대표 확인 | build 완료→image 목록→container `Up`; Spring log·browser는 확인 절차만 기록 | 첫 manifest의 `up` 생성→container `Up`→DB 결과; browser·`down`은 절차만 기록 |
| 직접 수업일 | 2026-04-30 | 2026-05-01 |

## 실제 선택 상황

### 상황 1: Spring Boot JAR를 실행 가능한 image로 포장

Dockerfile을 선택한다. 04-30에는 Maven으로 만든 JAR와 실행 명령을 image에 넣어 `myspring-img`를 build했다. **입력 JAR·Dockerfile → image build → image 목록·container `Up`**까지 실제 결과가 보존됐다. log·browser는 확인 기준과 명령/URL만 있으므로 성공으로 확정하지 않는다.

### 상황 2: Spring Boot와 MySQL을 같은 구성으로 함께 실행

Compose를 선택한다. 05-01 manifest는 이미 준비한 `myspring-img`와 MySQL image, service 이름, network, volume, environment, port, `depends_on`을 연결했다. **manifest → project network·volume·container 생성 → container `Up` → DB row**까지 결과가 보존됐고, browser와 `down`은 확인 절차만 기록됐다.

### 상황 3: MySQL+WordPress 묶음을 다른 VM에서 반복

host의 OpenSSH·UFW·Docker 설치와 일반 사용자 Docker 권한을 먼저 준비한 뒤 Compose를 사용했다. host 준비는 Compose 기능이 아니며, YAML 들여쓰기 수정과 요구사항 값 수정도 서로 다른 작업이었다.

## 둘을 함께 쓰는 관계

Dockerfile로 application image를 만들고 Compose의 `image` 또는 `build` 항목에서 그 image를 service로 실행할 수 있다. 실제 MySQL+Spring 실습도 “image가 없으면 Dockerfile로 먼저 build → Compose로 DB·application 관계 실행” 순서였다. 따라서 둘은 대체재가 아니라 **build 책임과 runtime 조합 책임**을 나눈다.

## 실제 오류·완료 조건

| 단계 | 확인된 결과 | 아직 보장하지 않는 것 |
|---|---|---|
| Dockerfile build | build 완료와 image 목록 | container 실행·application readiness |
| container 실행 | container 존재·`Up` | DB 연결·browser 응답 |
| Compose `up` | network·volume·container 생성 | DB query 가능 상태 |
| DB 확인 | prompt 접속·row 조회 | browser 응답 |
| browser 확인 | Spring/WordPress 확인 URL 기록, 관찰 결과 미보존 | application 성공·운영 배포·health check |
| Compose `down` | 명령 기록, 실행 결과 미보존 | container·network 중지·삭제와 image·volume 삭제 |

## 흔한 오해와 확인되지 않은 범위

- Compose가 Dockerfile을 대체하지 않는다. Compose가 image를 참조해도 image 생성 규칙은 별도다.
- `depends_on`은 시작 순서 표현이지 DB readiness 보장이 아니다.
- Compose `up` 성공과 application 성공은 같은 상태가 아니다.
- 05-01 수업은 한 host의 다중 container 구성이다. cluster scheduling·rolling deployment·운영 secret 관리까지 확인하지 않았다.
- 후속 CI/CD에서는 Dockerfile build와 registry push·server 갱신을 자동화하지만, Linux 수업의 수동 build/Compose 결과를 workflow 성공으로 소급하지 않는다.

## 관련 페이지

- [[summaries/2026-04-30-dockerfile-spring-load-balancing|2026-04-30 Dockerfile·Spring·로드 밸런싱]]
- [[summaries/2026-05-01-docker-compose|2026-05-01 Docker Compose]]
- [[concepts/docker-compose-manifest|Docker Compose manifest]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[comparisons/docker-commit-vs-dockerfile|docker commit vs Dockerfile]]
- [[entities/docker|Docker]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md` — Dockerfile build·image·container·Spring Boot 실습의 최우선 근거
- `raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md` — 두 Compose manifest의 service 관계·오류 수정·DB·browser·정리 흐름
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md` — build와 runtime 조합의 복습 경계
- Docker 실습·이론 PDF — 날짜 MD에 전사된 개념·화면 절차의 보조자료