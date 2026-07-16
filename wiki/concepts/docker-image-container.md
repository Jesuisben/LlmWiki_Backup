---
title: Docker 이미지와 컨테이너
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

# Docker 이미지와 컨테이너

## 정의와 이 페이지의 책임

Docker image는 container를 만들기 위한 실행환경 artifact이고, container는 그 image로 생성되어 실행·중지·삭제되는 process 단위다. 이 페이지는 **기성 image 준비와 container lifecycle·상태·port publishing**을 맡는다.

- container 내부 명령과 일회 파일 복사는 [[concepts/docker-cp-exec-container-files|Docker exec/cp와 컨테이너 파일 다루기]]가 맡는다.
- container 간 통신과 지속 저장은 [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]이 맡는다.
- `commit`과 Dockerfile의 선택은 [[comparisons/docker-commit-vs-dockerfile|docker commit vs Dockerfile]]이 맡는다.

## 수업에서 왜 필요했는가

[[summaries/2026-04-28-maven-spring-boot-docker-intro|04-28]]에는 Spring Boot source를 Maven JAR로 만들고 Linux host process로 직접 실행했다. 이 방식은 server마다 code·dependency·JDK·설정을 다시 준비해야 한다. 그래서 같은 실행환경을 image로 준비하고, 필요할 때 container instance로 반복 실행하는 Docker로 이동했다.

수업에서는 Java의 class/object 비유로 image/container를 설명했지만 완전히 같은 개념은 아니다. 핵심은 **하나의 image에서 여러 container를 만들 수 있고, image와 container의 생명주기가 분리된다**는 점이다.

## 04-28 기성 image 실습 순서

### 1. Apache `httpd`: 첫 pull과 lifecycle

1. local에 `httpd` image가 없는 상태에서 이름, detached 실행, host 8888→container 80 publish를 지정해 container를 실행했다.
2. Docker는 local image를 찾지 못해 registry에서 `httpd:latest` layer를 내려받았다.
3. 실행 중 목록에서 image, container name, `Up` 상태, published port를 확인했다.
4. VM 주소와 host port로 Apache 기본 page를 확인했다.
5. container를 stop한 뒤 전체 목록에서 `Exited` 상태를 확인했다.
6. container를 remove한 뒤 목록에서 사라진 것을 확인했다.

이 흐름의 입력은 기성 image 이름과 run option, 처리는 pull→create→start, 결과는 local image와 이름 있는 container다. browser 확인은 그 container의 web service와 port 경로가 실제 요청에 응답한 별도 결과다. ^[raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md]

### 2. Nginx: 같은 lifecycle 반복

`nginx85`를 host 8885→container 80으로 실행하고 상태·browser를 확인한 뒤 stop/remove했다. Apache와 Nginx의 image 이름이 각각 `httpd`, `nginx`라는 차이를 실제로 확인했다.

### 3. Apache·Nginx·MySQL 여러 개 실행

Apache 2개, Nginx 2개, MySQL 2개를 동시에 실행했다.

- 각 web container의 내부 HTTP port는 각자의 namespace에서 80으로 같을 수 있었다.
- 같은 host에서 publish하는 host port는 충돌하지 않게 서로 달랐다.
- MySQL container는 초기 설정을 environment variable로 전달했고, 실제 값은 이 페이지에 재노출하지 않는다.
- 실행 중 목록에서 6개가 `Up`인지 확인하고 web container는 각 host port의 browser page를 따로 확인했다.
- 마지막에는 6개를 stop→remove하고 목록이 비었는지 확인했다.

## lifecycle 명령을 결과 기준으로 구분하기

| 작업 | 대상·결과 | 수업에서의 판단 기준 |
|---|---|---|
| pull | registry image를 local image store에 준비 | local에 없던 image가 download됨 |
| create | image에서 새 container metadata·writable layer 생성 | container는 생기지만 실행 여부는 별도 |
| run | 필요한 경우 pull 후 새 container를 create하고 start | **매번 새 container**를 만드는 흐름 |
| start | 이미 존재하는 stopped container를 다시 실행 | 같은 container의 name·writable state를 이어 씀 |
| stop | running container의 주 process를 멈춤 | 전체 목록에서 `Exited` 확인 |
| restart | 같은 container를 stop 후 다시 start하는 lifecycle | 새 container나 새 image를 만들지 않음 |
| rm | container metadata·writable layer 삭제 | image는 별도로 남을 수 있음 |
| rmi/image rm | local image 삭제 | 그 image를 참조하는 container가 있으면 정리 순서에 제약이 생길 수 있음 |

R05에는 `run`, 상태 목록, `stop`, `rm`, image 정리가 직접 나타난다. `create`·`start`·`restart`는 Docker lifecycle의 책임을 구분하기 위한 명령이지만, 이 날짜의 대표 성공 흐름은 `run→stop→rm`이다. 원본에 없는 재시작 성공 결과를 만들지 않는다.

## container name·detached·상태

- `--name`은 사람이 lifecycle·network·exec/cp 대상을 안정적으로 찾게 하는 container 식별자다.
- `-d`는 container의 주 process를 background에서 실행하고 terminal을 돌려받는 option이다. 원본의 “demo” 설명은 `detached`로 바로잡아 이해한다.
- `docker container ls`는 running container를, `docker container ps -a`/`ls -a`는 stopped 상태까지 포함한 목록을 확인하는 데 사용했다.
- `Up`은 container의 주 process가 실행 중이라는 뜻이지 application readiness나 browser 성공을 자동 보장하지 않는다.

## port publishing과 완료 조건 분리

`host-port:container-port` publish는 host로 들어온 요청을 특정 container port로 전달한다. Docker network의 container 간 이름 기반 통신과는 다른 경로다.

| 완료 조건 | 실제 확인 | 다음 조건을 대신하지 않음 |
|---|---|---|
| image 존재 | pull 결과 또는 image 목록 | container 생성 |
| container 생성 | 전체 목록에 name 존재 | running |
| container running | status `Up` | DB readiness·web 응답 |
| port publish | 목록에 host→container port 표시 | browser 응답 |
| web browser 응답 | Apache/Nginx page 확인 | DB container readiness |
| DB readiness | MySQL log의 `ready for connections` | client login·query 성공 |

따라서 container가 `Up`이어도 web process가 아직 준비 중이거나 port가 잘못 publish되면 browser가 실패할 수 있다. 반대로 image가 local에 있다는 사실만으로 container가 존재한다고 볼 수 없다.

## 04-29 사용자 image는 후속 연결

[[summaries/2026-04-29-docker-network-volume-image|04-29]]에는 실행 중 Apache/Nginx container의 변경 상태를 `commit`해 `jeju-img`, `pohang-nginx-img` 같은 사용자 image를 만들고, 그 image로 새 container를 실행해 file과 browser 결과를 확인했다.

이것은 R05의 **기성 image를 pull/run하는 흐름**에서 “변경된 container도 새 image의 입력이 될 수 있다”로 확장된 것이다. Docker Hub tag·push·pull은 registry 생명주기이며 세션 7 후보 범위이므로 여기서 상세 절차를 복제하지 않는다.

## 직접 수업과 후속 image 경계

- R05: registry의 기성 `httpd`·`nginx`·MySQL·WordPress image를 pull/run했다.
- R06: 변경 container를 `commit`해 사용자 image를 만들었다.
- R07: Dockerfile로 Spring Boot·web image를 build했다. 이는 다음 세션 범위이며 R05의 기성 image 실습과 합치지 않는다.
- CI/CD: source push를 trigger로 image build/push/deploy를 자동화한다. Linux 수업의 수동 image lifecycle 성공을 CI image 성공으로 소급하지 않는다.

## 자주 헷갈리는 점

- **`run`과 `start`:** `run`은 새 container, `start`는 기존 stopped container다.
- **image 삭제와 container 삭제:** 서로 다른 자원이다. container를 지워도 image는 남을 수 있다.
- **container `Up`과 service 준비:** MySQL은 log readiness, web server는 browser 응답처럼 service별 확인이 더 필요하다.
- **host port와 container port:** 여러 web container가 내부 80을 써도 host port는 각각 달라야 했다.
- **container 내부 변경과 image 변경:** writable layer의 file을 고쳐도 원본 image가 자동 변경되지 않는다.
- **VM과 container:** container는 별도 guest OS 전체가 아니라 Docker Engine 위의 격리된 process 단위다. [[comparisons/virtual-machine-vs-docker-container|가상 머신(VM) vs Docker 컨테이너]]에서 계층을 비교한다.

## 관련 개념

- [[concepts/docker-install-permission-setup|Docker 설치와 권한 설정]]
- [[concepts/docker-cp-exec-container-files|Docker exec/cp와 컨테이너 파일 다루기]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[comparisons/host-port-forwarding-vs-docker-port-mapping|호스트 포트 포워딩 vs Docker 포트 매핑]]
- [[comparisons/docker-commit-vs-dockerfile|docker commit vs Dockerfile]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md` — 기성 image pull, Apache/Nginx/MySQL container lifecycle·상태·port·browser의 최우선 근거
- `raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md` — 변경 container→commit image→새 container의 후속 연결
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md` — image/container·port mapping의 복습 경계