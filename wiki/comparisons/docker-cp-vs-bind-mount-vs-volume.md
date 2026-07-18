---
title: docker cp vs bind mount vs volume
created: 2026-07-02
updated: 2026-07-18
type: comparison
tags: [linux, docker, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
  - raw/KoreaICT/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf
  - raw/KoreaICT/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
status: stable
confidence: high
---

# docker cp vs bind mount vs volume

## 비교 목적

04-29에는 host와 container 사이의 일회 file 복사, host path의 지속 연결, Docker 관리 storage 연결을 같은 web document root에 차례로 적용했다. 셋은 모두 file/data를 다루지만 **복사인가 연결인가**, **source를 누가 관리하는가**, **어떤 생명주기와 결합되는가**가 다르다.

## 한눈에 보기

| 비교 축 | `docker cp` | bind mount | named volume |
|---|---|---|---|
| 동작 | 한 시점의 file/directory 복사 | 지정 host path를 container path에 연결 | Docker가 관리하는 volume을 container path에 연결 |
| 지속 연결 | 없음 | 있음 | 있음 |
| source 관리 | 복사 전후 양쪽 file을 사용자가 관리 | host filesystem의 실제 path | Docker Engine의 volume lifecycle |
| 수업 artifact | Apache/Nginx HTML·image의 양방향 복사 | `~/bind_mount`, `~/bind_nginx` | `mount-vol` |
| 적합한 선택 | 단발성 반입·반출·검사 | 개발 file·정적 page 즉시 반영 | DB·지속 data처럼 host path 결합을 줄일 때 |
| 대표 위험 | 이후 원본 변경이 자동 반영되지 않음 | 빈 source가 image 기본 directory를 가림·host 권한 의존 | 실제 위치를 직접 다루기보다 volume 이름·연결·삭제를 관리해야 함 |

## 실제 선택 상황

### 상황 1: HTML·image를 한 번 넣거나 꺼내기

`docker cp`를 선택한다. host→Apache/Nginx document root 복사 뒤 transferred output과 browser를 확인했고, container→host 방향으로도 이름을 바꾸어 복사했다. **복사 성공 output → container 내부 file 확인 → browser/host file 확인**이 완료 조건이다.

### 상황 2: host에서 정적 page를 수정하자마자 반영

bind mount를 선택한다. Apache와 Nginx document root에 빈 host directory를 연결하자 image의 기본 file이 가려져 Apache는 directory listing, Nginx는 403을 보였다. host directory에 `index.html`과 image를 넣은 뒤 browser 결과가 바뀌었다.

### 상황 3: container와 분리된 Docker 관리 storage

named volume을 선택한다. `mount-vol`을 만들고 Apache document root에 연결한 뒤 inspect에서 Docker 관리 Mountpoint를 확인하고, container와 volume을 별도로 삭제했다. 다만 R06에는 container 재생성 후 동일 data를 다시 확인한 round-trip이 없다.

### 상황 4: 여러 service의 DB data 선언

05-01에는 named volume을 Compose manifest에 선언해 MySQL data path에 연결했다. 이는 volume 개념을 YAML로 반복한 것이며, `down`과 volume 삭제는 별도 완료 상태다.

## 함께 쓰는 관계

셋은 상호 배타적이지 않다. 초기 file을 `docker cp`로 검사하고, 개발 중에는 bind mount로 즉시 반영하며, DB·지속 data는 named volume에 둘 수 있다. 같은 container path에 여러 방식을 무계획하게 겹치면 무엇이 보이는지 혼란스러우므로 각 path의 source와 lifecycle을 명시한다.

## 실제 오류·완료 조건

| 단계 | 확인 | 아직 보장하지 않는 것 |
|---|---|---|
| `docker cp` output | byte transfer 성공 | web service가 새 file을 제공함 |
| container 내부 file | `cat`·목록 확인 | browser routing·cache 정상 |
| bind inspect | Source·Destination·Type 확인 | source에 기대 file 존재 |
| browser 응답 | Apache page 또는 Nginx page | container 재생성 뒤 data 보존 |
| volume create/inspect | volume 이름·Mountpoint | application data 기록 |
| container 삭제 | container 제거 | volume 자동 삭제 |

## 흔한 오해와 확인되지 않은 범위

- `docker cp`는 동기화가 아니다. 복사 뒤 host 원본 변경은 자동 반영되지 않는다.
- bind mount의 빈 source가 image file을 삭제한 것은 아니다. mount가 기존 path를 가린다.
- named volume의 일반적 지속성 원리와 이 수업에서 재생성 후 data를 확인한 결과를 구분한다.
- Compose `down`이 image·volume까지 모두 지운다고 단정하지 않는다.
- Linux 직접 수업은 한 host의 Docker storage다. AWS EBS/EFS/S3나 CI/CD artifact storage는 후속 과목의 다른 책임이다.

## 관련 페이지

- [[summaries/2026-04-29-docker-network-volume-image|2026-04-29 Docker network·volume·image]]
- [[summaries/2026-05-01-docker-compose|2026-05-01 Docker Compose]]
- [[concepts/docker-cp-exec-container-files|Docker exec/cp와 컨테이너 파일 다루기]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[concepts/docker-compose-manifest|Docker Compose manifest]]
- [[entities/docker|Docker]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md` — 양방향 `docker cp`, Apache/Nginx bind 결과, `mount-vol` lifecycle의 최우선 근거
- `raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md` — Compose volume 선언과 `down`·잔존 자원 경계
- Docker 이론·실습 PDF와 Linux 총정리 — 관리 주체·사용 상황·복습 관계의 보조 근거