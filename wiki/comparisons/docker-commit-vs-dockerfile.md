---
title: docker commit vs Dockerfile
created: 2026-07-02
updated: 2026-07-18
type: comparison
tags: [linux, docker, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
  - raw/KoreaICT/5. Linux/교육 자료/docker image를 docker hub에 업로드 하기.md
  - raw/KoreaICT/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
status: stable
confidence: high
---

# docker commit vs Dockerfile

## 비교 목적

04-29에는 실행 중인 web container의 변경 상태를 `docker commit`으로 image에 저장했고, 04-30에는 Dockerfile의 명시적 instruction으로 image를 build했다. 둘 다 image를 만들지만 **현재 상태를 캡처하는가, 생성 절차를 재실행 가능하게 남기는가**가 핵심 차이다.

## 한눈에 보기

| 비교 축 | `docker commit` | Dockerfile |
|---|---|---|
| 입력 | 변경된 container writable state | base image·build context·instruction 파일 |
| 결과 | 현재 상태의 새 image | 선언된 절차로 build한 새 image |
| 변경 이유 추적 | container 안에서 한 수동 작업은 별도 기록이 없으면 알기 어려움 | `FROM`·`COPY`·`RUN` 등으로 검토 가능 |
| 반복 재현 | 같은 수동 변경을 다시 해야 할 수 있음 | 같은 context와 instruction으로 다시 build 가능 |
| 수업 artifact | `commit-ctr`→`jeju-img`, Nginx 변경 container→사용자 image | `Dockerfile01/02`→`pohang-img`, `myspring-img` |
| 적합한 선택 | 빠른 실험 snapshot·상태 보존 | 팀 공유·반복 build·배포 기반 |

## 실제 선택 상황

### 상황 1: 방금 수정한 컨테이너 상태를 빠르게 보존

04-29에는 Apache container에 HTML·image를 복사하고 내부에 text file을 만든 뒤 `commit`했다. 새 image로 다른 container를 실행해 text file과 browser 결과를 다시 확인했다. **container 변경 → file 확인 → commit digest → image 목록 → 새 container → file/browser 확인**이 실제 완료 흐름이었다.

### 상황 2: 다른 사람이 같은 image를 다시 만들 수 있게 절차 보존

04-30에는 `FROM`과 `COPY`를 적은 Dockerfile, build context의 HTML·image, build 명령으로 web image를 만들었다. 이후 Spring Boot JAR image로 확장했다. 수동 shell history를 재현하는 대신 instruction 파일을 검토·수정·Git 관리할 수 있으므로 Dockerfile이 적합하다.

### 상황 3: registry와 CI/CD로 전달

수업의 `commit` image도 tag·login·push 대상이 되어 Docker Hub로 전달됐다. 따라서 registry push 가능 여부가 두 방식을 가르는 기준은 아니다. 다만 후속 CI/CD처럼 source에서 image를 반복 생성해야 할 때는 Dockerfile이 build 입력으로 적합하다.

## 둘을 함께 쓰는 관계

`commit`은 탐색 중 얻은 유효 상태를 임시 image로 보존하는 데 쓸 수 있고, 확인된 변경을 Dockerfile instruction으로 옮겨 재현 가능한 build로 정리할 수 있다. 두 image 모두 container 실행과 registry tag·push가 가능하지만, image가 만들어진 **과정의 투명성**은 다르다.

## 실제 오류·완료 조건

- `commit` 실습은 image digest와 image 목록만으로 끝내지 않고 새 container에서 file과 browser를 확인했다.
- Dockerfile 실습은 build 완료, image 존재, container 생성, browser 확인을 별도로 점검했다.
- Docker Hub 전송에서는 registry namespace가 빠진 image 이름으로 다른 환경에서 실행하자 pull access 오류가 났고, namespace를 포함해 pull/run해야 했다. 이는 commit vs Dockerfile 문제가 아니라 registry naming 문제다.
- P08은 tag·login·push·pull 절차를 보조하지만 실제 account·email·repository URL·credential은 이 페이지에 옮기지 않는다.

## 흔한 오해와 확인되지 않은 범위

- `docker commit`이 원본 image를 수정하는 것은 아니다. 새 image를 만든다.
- Dockerfile이 있다는 사실만으로 build·container·application 성공이 보장되지 않는다.
- `commit` image도 registry에 push할 수 있다. “commit은 공유 불가”는 틀리다.
- 수업은 image history 비교, layer 최적화, reproducible build의 byte-identical 결과, image signing까지 확인하지 않았다.
- 운영 배포에서는 Dockerfile 중심이 유리하지만, Linux 수업의 수동 push를 GitHub Actions 자동화 완료로 보지 않는다.

## 관련 페이지

- [[summaries/2026-04-29-docker-network-volume-image|2026-04-29 Docker network·volume·image]]
- [[summaries/2026-04-30-dockerfile-spring-load-balancing|2026-04-30 Dockerfile·Spring·로드 밸런싱]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[concepts/docker-registry-tag-push-pull|Docker registry tag·push·pull]]
- [[concepts/dockerfile-vs-compose|Dockerfile vs Docker Compose]]
- [[entities/docker|Docker]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md` — 변경 container→commit image→새 container의 file/browser 확인
- `raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md` — Dockerfile instruction→build→image→container의 최우선 근거
- `raw/KoreaICT/5. Linux/교육 자료/docker image를 docker hub에 업로드 하기.md` — commit image의 registry 전달·namespace 오류 보조
- Docker 실습 PDF와 Linux 총정리 — 날짜 MD의 두 image 생성 방식과 복습 경계 보조