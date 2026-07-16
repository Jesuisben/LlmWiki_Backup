---
title: Docker exec/cp와 컨테이너 파일 다루기
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [linux, docker, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
status: growing
confidence: high
---

# Docker exec/cp와 컨테이너 파일 다루기

## 정의와 책임

`docker exec`는 **실행 중인 container의 namespace 안에서 새 명령 process를 실행**하고, `docker cp`는 host와 container filesystem 사이에 file/directory snapshot을 한 번 복사한다. 이 페이지는 실행 중 container의 file을 확인·변경·반출하는 일회 작업을 맡는다.

- container lifecycle은 [[concepts/docker-image-container|Docker 이미지와 컨테이너]]가 맡는다.
- 지속적으로 경로를 연결하는 bind mount·named volume은 [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]이 맡는다.

## 수업에서 왜 필요했는가

04-28에 Apache·Nginx·MySQL container를 여러 개 실행한 다음, 기본 page를 수업용 homepage로 바꾸고 DB 내부를 확인할 필요가 생겼다. container filesystem은 Linux host filesystem과 분리되어 있으므로 두 방식이 등장했다.

1. container 안에서 직접 명령·shell을 실행한다: `exec`
2. host에 준비한 file을 넣거나 container file을 꺼낸다: `cp`

04-29에는 이 차이를 `apache01-ctr`와 `nginx88`의 실제 path에서 양방향으로 다시 확인한 뒤, 지속 연결이 필요한 경우 mount로 넘어갔다.

## 04-28: 서로 다른 container 실습을 분리해서 보기

### `apache81`: 내부 shell과 직접 수정

실행 중 `apache81`에서 shell process를 시작했다. container에 Vim이 없어서 package source 설정을 조정하고 Vim을 설치한 뒤 Apache document root인 `/usr/local/apache2/htdocs/`의 `index.html`을 수정했다. shell을 종료한 뒤 해당 host port의 browser page에서 변경 결과를 확인했다.

이때 “container 안으로 들어간다”는 표현은 새 VM에 login한다는 뜻이 아니다. host의 Docker client가 실행 중 container에 `/bin/bash` process를 추가로 시작하고 terminal을 연결한 것이다.

### `apache82`: host file을 container로 복사

host의 clone directory에 있던 `index.html`과 image file을 `apache82`의 Apache document root로 각각 복사했다. copy 성공 출력과 browser page를 따로 확인했다. `apache81`의 직접 수정과 `apache82`의 file copy는 다른 container에서 수행된 실습이므로 하나의 연속 실행처럼 합치지 않는다. ^[raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md]

### MySQL·Nginx의 다른 목적

- `mysql85`: 먼저 log에서 `ready for connections`를 확인하고, `exec`로 container shell을 실행한 뒤 MySQL client prompt에 접속했다. container shell 진입과 DB login은 별도 단계다.
- `nginx83`: `/usr/share/nginx/html/`의 기본 page를 container 내부에서 직접 수정했다.
- `nginx84`: host의 HTML·image를 Nginx document root로 복사했다.

여러 container의 명령은 같은 `exec/cp` 책임을 설명하지만 artifact·path·확인 browser port가 다르다.

## 04-29: Apache에서 양방향 `cp` 확인

[[summaries/2026-04-29-docker-network-volume-image|04-29]]에는 실제 실습 file archive를 host의 `docker/` directory에 풀고 `apache01-ctr`를 실행했다.

### host → container

1. `exec`로 `/usr/local/apache2/htdocs` 목록과 기본 `index.html` 내용을 확인했다.
2. host의 `docker/host2container/index.html`을 같은 container path의 `index.html`로 복사했다.
3. `coffee01.png`도 같은 document root로 복사했다.
4. 각 copy 성공 출력을 확인하고 browser에서 작성한 문서와 image가 보이는지 확인했다.

### container → host

1. container의 `index.html`을 host의 같은 실습 directory에 `hello.html`이라는 다른 이름으로 복사했다.
2. container의 image를 host에 `world.png`라는 이름으로 복사했다.
3. host directory 목록에서 원본 file과 새 file이 함께 존재하는지 확인했다.

복사 방향은 `container:path` 표기가 source 쪽인지 destination 쪽인지로 구분한다. host→container와 container→host는 서로 반대인 별도 완료 조건이다. ^[raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md]

## 04-29 `nginx88`: 같은 원리를 다른 document root에 적용

Nginx 실습에서는 host의 `index03.html`을 `index.html` 이름으로 준비하고 image file과 함께 `nginx88`의 `/usr/share/nginx/html/`로 복사했다. copy 성공 뒤 browser에서 반영을 확인하고 container를 정리했다.

Apache path `/usr/local/apache2/htdocs/`와 Nginx path `/usr/share/nginx/html/`을 바꾸어 쓰면 명령 자체가 실행돼도 원하는 homepage가 바뀌지 않을 수 있다. container 이름뿐 아니라 image별 artifact path를 함께 확인해야 한다.

## `exec`의 동작과 선택 기준

| 목적 | 실행 방식 | 판단 기준 |
|---|---|---|
| file 하나 조회 | container에서 `ls`·`cat` 같은 단일 명령 실행 | interactive shell이 필요하지 않음 |
| 여러 명령을 연속 수행 | `-it`로 container shell process 실행 | package 설치·directory 이동·편집처럼 terminal 입력이 필요함 |
| DB 상태 확인 | 먼저 container log, 이후 필요하면 shell/client | container running과 DB readiness를 합치지 않음 |
| 정적 file 투입 | host에서 `docker cp` | image rebuild 없이 현재 container만 빠르게 바꿈 |

`exec` 대상 container는 running 상태여야 한다. stopped container를 다시 실행하는 책임은 `start`, 새 container를 만드는 책임은 `run`이다.

## `cp`, 내부 변경, image의 관계

`exec`로 만든 file과 `cp`로 넣은 file은 현재 container의 writable layer를 바꾼다. **원본 image는 자동으로 바뀌지 않는다.** container를 삭제하면 mount로 분리하지 않은 변경은 함께 사라질 수 있다.

04-29의 후반 실습에서는 다음 관계가 실제로 이어졌다.

1. `commit-ctr`에 HTML·image를 `cp`하고 내부에서 `jeju.txt`를 만들었다.
2. file 존재를 확인했다.
3. 변경된 container를 `jeju-img`로 commit했다.
4. 새 image로 `jeju-ctr`를 실행했다.
5. 새 container에서 `jeju.txt`와 browser page를 다시 확인했다.

이는 **container 내부 변경→새 image snapshot** 관계를 보여 준다. file copy 성공과 새 image 생성은 같은 완료 조건이 아니며, 재현 가능한 build recipe는 다음 날 Dockerfile의 책임이다.

## `docker cp`와 mount의 차이

| 방식 | 연결 성격 | host file을 나중에 수정하면 | 적합한 상황 |
|---|---|---|---|
| `docker cp` | 한 시점의 일회 복사 | container에 자동 반영되지 않음 | 확인용 file 투입·반출, 임시 homepage 교체 |
| bind mount | host path를 계속 연결 | 연결된 container path에 반영 | host에서 직접 관리하는 개발 file |
| named volume | Docker 관리 storage를 계속 연결 | container를 통해 관리하는 것이 기본 | DB·지속 data |

자세한 선택 비교는 [[comparisons/docker-cp-vs-bind-mount-vs-volume|docker cp vs bind mount vs volume]]에, 실제 Apache/Nginx mount 결과는 [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]에 둔다.

## 완료 조건을 분리하기

| 완료 조건 | 확인 artifact | 아직 보장하지 않는 것 |
|---|---|---|
| source file 존재 | host directory 목록 | 복사 성공 |
| 복사 성공 | `Successfully copied` 출력 | container 내부 내용·browser 응답 |
| container 내부 확인 | `exec`의 `ls`·`cat` 결과 | image 변경 |
| browser 반영 | 해당 container의 published port 응답 | 지속 저장 |
| 새 image 생성 | commit 결과와 image 목록 | 새 container의 file·browser 결과 |
| 새 container 재현 | 새 container의 `cat`·browser 확인 | Dockerfile 수준의 재현 절차 |

## 자주 헷갈리는 점

- **shell 접속과 DB 접속:** container shell prompt와 MySQL prompt는 실행 계층이 다르다.
- **file 복사와 path 연결:** `cp`는 synchronization이 아니다.
- **container file과 image file:** writable layer 변경은 base image에 역으로 반영되지 않는다.
- **Apache와 Nginx path:** image마다 document root가 다르다.
- **여러 container 실습 합성:** `apache81` 직접 수정, `apache82` copy, `nginx83` 직접 수정, `nginx84` copy는 각각 별도 실행이었다.

## 선행·후속 연결

- 선행: [[concepts/docker-image-container|Docker 이미지와 컨테이너]]의 running container와 이름·port를 알아야 정확한 target을 고를 수 있다.
- 직접 후속: [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]에서 일회 copy 대신 지속 path 연결을 배운다.
- image 후속: [[comparisons/docker-commit-vs-dockerfile|docker commit vs Dockerfile]]에서 현재 상태 snapshot과 재현 recipe를 구분한다.
- 범위 밖 후속: Compose의 service volume 선언과 CI image build는 이 페이지의 `exec/cp` 성공 결과가 아니다.

## 출처

- `raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md` — Apache·Nginx·MySQL container 내부 shell, 직접 수정, host→container copy의 실제 container/path 근거
- `raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md` — `apache01-ctr` 양방향 copy, `nginx88`, 변경 container→commit image의 최우선 근거
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md` — `exec`·`cp`·mount·image의 복습 책임 경계