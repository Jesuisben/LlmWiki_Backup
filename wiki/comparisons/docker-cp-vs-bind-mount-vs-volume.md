---
title: docker cp vs bind mount vs volume
created: 2026-07-02
updated: 2026-07-09
type: comparison
tags: [linux, docker, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/KoreaICT/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf
  - raw/KoreaICT/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
status: growing
confidence: high
---

# docker cp vs bind mount vs volume

## 비교 목적

Docker 수업에서는 컨테이너 파일을 바꾸는 방법으로 `docker cp`, bind mount, volume mount가 모두 등장했다. 셋은 모두 파일/데이터와 관련되지만 사용 시점과 지속성이 다르다.

## 한눈에 보기

| 항목 | `docker cp` | bind mount | volume mount |
|---|---|---|---|
| 핵심 | 파일을 한 번 복사 | host 경로를 container 경로에 연결 | Docker가 관리하는 저장소 연결 |
| 연결 지속성 | 복사 순간만 | 실행 중 계속 연결 | 컨테이너 삭제와 분리해 보존 가능 |
| 관리 주체 | 사용자 | 사용자/host 파일 시스템 | Docker |
| 수업 예시 | HTML/이미지를 Apache 컨테이너로 복사 | `~/bind_mount:/usr/local/apache2/htdocs` | `mount-vol:/usr/local/apache2/htdocs` |
| 적합한 상황 | 빠른 파일 교체 | 개발 중 파일 직접 반영 | DB/로그 등 보존 데이터 |

## 언제 무엇을 쓰는가

- 단발성으로 파일 하나만 넣거나 꺼낼 때는 `docker cp`.
- host에서 수정한 정적 파일을 컨테이너에 바로 반영하고 싶으면 bind mount.
- DB 데이터처럼 컨테이너 생명주기와 분리해 보존할 데이터는 volume.

## 헷갈리기 쉬운 포인트

- `docker cp`는 연결이 아니라 복사다.
- bind mount는 host 경로가 사라지거나 권한이 틀리면 컨테이너에 바로 영향을 준다.
- volume은 Docker가 관리하므로 위치를 직접 다루기보다 `docker volume` 명령으로 관리한다.

## 관련 페이지

- [[concepts/docker-cp-exec-container-files|Docker exec/cp와 컨테이너 파일 다루기]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[concepts/docker-compose-manifest|Docker Compose manifest]]

## 5과목 현재 raw MD 기준 재검증 메모

- 2026-07-09에 `raw/KoreaICT/5. Linux` 날짜별 MD 10개와 `Linux 총정리.md`를 기준으로 다시 대조했다.
- 이 페이지는 단순 명령어 사전이 아니라 VM/SSH/CLI → 파일·권한 → Spring Boot jar 실행 → Docker network/volume/Dockerfile/Compose → GitHub branch/PR/conflict 흐름 속에서 읽어야 한다.
- 운영 관점에서는 코드보다 IP/포트/방화벽/권한/컨테이너 네트워크·볼륨이 문제 원인일 수 있음을 함께 기억한다.

## 출처

- `raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md`
