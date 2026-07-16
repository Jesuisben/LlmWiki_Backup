---
title: Docker 네트워크와 볼륨
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [linux, docker, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
status: growing
confidence: high
---

# Docker 네트워크와 볼륨

## 정의와 이 페이지의 책임

Docker network는 container 사이 통신 경로를 만들고, mount는 container path에 container 밖 storage를 연결한다. 이 페이지는 **container 간 이름 기반 통신**과 **bind mount·named volume의 지속 연결**을 맡는다.

- host↔container 일회 file copy는 [[concepts/docker-cp-exec-container-files|Docker exec/cp와 컨테이너 파일 다루기]]의 책임이다.
- container 생성·running·port publish는 [[concepts/docker-image-container|Docker 이미지와 컨테이너]]의 책임이다.
- Compose의 YAML 선언 방식은 [[concepts/docker-compose-manifest|Docker Compose manifest]]의 후속 책임이다.

## 왜 필요했는가

container 하나의 web page를 보는 단계 다음에는 두 문제가 생겼다.

1. WordPress·Redmine 같은 application container가 MySQL·MariaDB container를 어떻게 찾는가?
2. container를 삭제해도 유지해야 하는 file·DB data를 어디에 둘 것인가?

04-28에는 WordPress–MySQL의 `network01`로 container 간 통신을 시작했다. 04-29에는 MariaDB–Redmine의 `network02`, Apache/Nginx bind mount, Docker named volume로 통신과 storage 책임을 분리했다. 05-01에는 같은 요소를 Compose manifest에 선언했지만, 그 선언 방식은 직접 CLI 실습과 구분한다.

## 04-28 `network01`: WordPress가 MySQL을 이름으로 찾기

### 입력

- 사용자 정의 bridge network `network01`
- MySQL container `mysql01`과 database 초기 설정
- WordPress container `wordpress01`과 DB host 설정
- browser가 WordPress에 들어갈 host port

### 처리

1. network를 만들고 network 목록에서 확인했다.
2. MySQL container를 `network01`에 연결해 실행했다.
3. WordPress container도 같은 network에 연결하고 DB host를 `mysql01`로 지정했다.
4. container 목록에서 둘의 `Up` 상태를 확인하고 network inspect에서 두 이름이 같은 network에 속했는지 확인했다.
5. browser에서 WordPress 설치·login 화면을 확인했다.
6. MySQL에 sample table/data를 만들고 commit했다.
7. WordPress container에 MySQL client를 설치해 `mysql01`이라는 이름으로 DB에 접속하고 sample rows를 조회했다.

### 결과와 한계

container name 기반 DB 접속과 data 조회까지 확인했다. container `Up`, network membership, WordPress browser 화면, DB query는 서로 다른 완료 조건이다. 수업 중 TLS certificate 불일치가 있어 보안 검증을 생략하는 우회 option을 사용했지만, 이를 일반 운영 권장 설정으로 확대하지 않는다. 실제 credential·email·one-time code는 재노출하지 않는다. ^[raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md]

## 04-29 `network02`: MariaDB와 Redmine

[[summaries/2026-04-29-docker-network-volume-image|04-29]]에는 network를 먼저 만들고 `mariadb02`, `redmine02`를 같은 `network02`에 연결했다.

- Redmine의 DB host 값은 MariaDB container name과 맞췄다.
- network, database name, user, credential 설정은 DB container와 application container 양쪽에서 일치해야 했다.
- browser는 host 8883→Redmine container 3000 publish를 통해 Redmine 화면에 접근했다.
- 전체 목록에서 두 container가 `Up`인지 확인했다.

여기서 `mariadb02` 이름 기반 연결은 **container→container 내부 통신**, host 8883 publish는 **browser→container 진입**이다. 같은 `network` 문제로 합치지 않는다.

## network 작업과 확인 방법

| 작업 | 책임 | 확인 |
|---|---|---|
| network create | 사용자 정의 bridge network 생성 | network 목록에 이름 존재 |
| run `--net=...` | container를 생성 시 network에 연결 | container가 해당 network membership을 가짐 |
| network connect | 기존 container를 추가 network에 연결 | inspect에서 membership 확인 |
| network inspect | driver·연결 container metadata 확인 | 이름·membership 확인이지 application readiness 증거는 아님 |
| container name 사용 | 같은 network의 DNS 이름으로 상대 service를 찾음 | 실제 client connection/query로 최종 확인 |

R05·R06의 대표 흐름은 생성 시 같은 network를 지정하고 inspect·실제 DB 접속으로 확인하는 방식이다. `connect` 명령 자체의 성공을 이 날짜에 실행했다고 만들지 않는다.

## 04-29 bind mount: host path를 직접 연결

### Apache `apache02-ctr`

host의 `~/bind_mount`를 Apache document root `/usr/local/apache2/htdocs`에 연결했다. 빈 host directory가 image의 기존 document root를 가리면서 browser에는 `Index of /`가 나타났다.

container inspect의 `Mounts`에서 다음 책임을 구분했다.

- `Type: bind`: host path 직접 연결
- `Source`: Linux host의 실제 directory
- `Destination`: container의 Apache document root

host mount directory에 HTML·image를 복사하고 HTML 이름을 `index.html`로 맞추자 별도 `docker cp` 없이 browser page가 바뀌었다.

### Nginx `nginx30-ctr`

host의 `~/bind_nginx`를 Nginx document root `/usr/share/nginx/html`에 연결했다. 빈 directory에서는 Apache의 listing과 달리 403이 발생했다. host 쪽에 실제 `index.html`과 image를 넣은 뒤 browser에서 정상 page를 확인했다.

같은 원인은 **빈 bind source가 image의 기존 document root를 가린 것**이고, Apache directory listing과 Nginx 403은 각 server의 기본 동작 차이다. 이 오류를 04-28의 `docker cp` 실습이나 다른 container에 귀속하지 않는다. ^[raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md]

## 04-29 named volume: Docker 관리 storage

`mount-vol`을 만든 뒤 `apache03-ctr`의 Apache document root에 연결했다.

1. volume create 결과로 volume 이름을 확인했다.
2. Apache container에 `mount-vol`을 연결했다.
3. volume inspect에서 name과 Docker 관리 `Mountpoint`를 확인했다.
4. container를 stop/remove한 뒤 volume을 별도로 remove했다.

수업의 직접 확인은 **volume artifact 생성·inspect·container 연결·별도 삭제**까지다. container를 삭제하고 새 container에 같은 volume을 다시 붙여 data가 유지되는 round-trip 결과는 R06에 명시적으로 기록되지 않았다. 일반 원리로 data를 container lifecycle과 분리한다고 설명할 수 있지만, 재생성 후 persistence를 실제 관찰한 것처럼 쓰지 않는다.

## bind mount와 named volume 선택 기준

| 기준 | bind mount | named volume |
|---|---|---|
| source | 사용자가 정한 host file/directory path | Docker가 이름과 저장 위치를 관리 |
| 관리 주체 | host 사용자 | Docker Engine |
| 수업 artifact | `~/bind_mount`, `~/bind_nginx` | `mount-vol` |
| 변경 방식 | host file을 직접 수정·복사 | container를 통해 다루는 방식을 권장 |
| 적합한 경우 | 개발 file·정적 page를 host에서 즉시 반영 | DB·지속 data처럼 host path 결합을 줄이고 싶은 경우 |
| 주의 | 빈 source가 image 기존 path를 가림, host path·권한 의존 | 실제 location을 직접 고치기보다 volume lifecycle로 관리 |

둘 다 container filesystem 밖 storage를 연결하지만 관리 책임이 다르다. `docker cp`는 어느 쪽도 아니며 한 번 복사할 뿐이다. 자세한 비교는 [[comparisons/docker-cp-vs-bind-mount-vs-volume|docker cp vs bind mount vs volume]]에 둔다.

## 05-01 Compose는 후속 manifest 활용

[[summaries/2026-05-01-docker-compose|05-01]]에는 network·volume·service 관계를 YAML로 선언했다.

- MySQL+Spring Boot: `spring-mysql-net`, MySQL named volume, service name 기반 datasource 연결
- MySQL+WordPress: `network01`, DB·WordPress volume, service 의존 관계

Compose가 network와 volume을 생성하고 container에 연결했지만, 이는 04-28~29 CLI 개념을 manifest로 반복한 후속 활용이다. `depends_on`은 시작 순서를 나타낼 뿐 DB readiness를 보장하지 않았고, 기본 `down` 뒤 image·volume이 남을 수 있음을 별도로 확인했다.

## 완료 조건을 분리하기

| 완료 조건 | 실제 증거 | 아직 보장하지 않는 것 |
|---|---|---|
| network 생성 | network 목록 | container 연결 |
| container network 연결 | network inspect membership | DB readiness |
| container running | 상태 `Up` | application 연결 성공 |
| DB readiness | DB log 또는 client 접속 | browser 응답 |
| 이름 기반 DB 통신 | 다른 container의 client query | host 공개 |
| port publish | host→container port 표시 | browser 정상 page |
| browser 응답 | WordPress·Redmine·Apache·Nginx page | DB data persistence |
| mount 연결 | inspect의 Source/Destination 또는 volume name | 기대 file 존재 |
| data persistence | container lifecycle 뒤 동일 data 재확인 | R06에서는 재생성 round-trip 미기록 |

## 계층 경계

- **Docker network:** 한 Docker Engine 안에서 container 간 통신과 이름 해석을 담당한다.
- **Docker port publishing:** host 요청을 container port로 전달한다.
- **VirtualBox bridge/NAT:** Windows host와 Ubuntu guest VM 사이의 network mode·port 경계다.
- **Linux iptables/UFW:** guest OS의 redirect·firewall 책임이다.
- **AWS VPC/Subnet/Security Group:** 후속 cloud network resource다.

이들을 모두 “network 설정”으로 묶으면 실패 위치를 찾을 수 없다. [[comparisons/host-port-forwarding-vs-docker-port-mapping|호스트 포트 포워딩 vs Docker 포트 매핑]]과 [[concepts/linux-process-service-port-firewall|Linux process·service·port·firewall 진단]]에서 host 경계를 함께 본다.

## 자주 헷갈리는 점

- container name은 같은 사용자 정의 network에서 상대 service를 찾는 이름이지 host browser 주소가 아니다.
- container `Up`은 DB query 준비나 web page 성공을 뜻하지 않는다.
- 빈 bind mount는 image의 기존 directory를 host 빈 directory로 가릴 수 있다.
- named volume이 지속 storage라는 원리와 실제 재생성 후 data 확인 결과를 구분해야 한다.
- Compose volume 선언은 storage 책임을 없애지 않는다. `down`과 volume 삭제는 별도다.
- DB credential은 network 연결 정보가 아니다. 값이 양쪽에서 맞아야 하지만 wiki에는 실제 값을 재노출하지 않는다.

## 선행·후속 연결

- 선행: [[concepts/docker-image-container|Docker 이미지와 컨테이너]]에서 container name·running·port publish를 구분한다.
- 같은 날: [[concepts/docker-cp-exec-container-files|Docker exec/cp와 컨테이너 파일 다루기]]의 일회 copy 한계를 확인한 뒤 mount로 이동했다.
- 후속: [[concepts/docker-compose-manifest|Docker Compose manifest]]가 service·network·volume 관계를 YAML에 선언한다.
- 범위 밖: R07 reverse proxy network, Docker registry, AWS VPC, CI/CD image 배포는 이 페이지의 직접 결과로 확장하지 않는다.

## 출처

- `raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md` — WordPress–MySQL `network01`, inspect, 이름 기반 DB query의 최우선 근거
- `raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md` — MariaDB–Redmine `network02`, Apache/Nginx bind mount, `mount-vol`의 최우선 근거
- `raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md` — network·volume의 Compose 후속 선언과 `down`/잔존 경계
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md` — network·port·cp·mount·volume의 복습 책임 경계