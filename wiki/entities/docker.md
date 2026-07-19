---
title: Docker
created: 2026-07-02
updated: 2026-07-19
type: entity
tags: [linux, docker, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
  - raw/KoreaICT/5. Linux/교육 자료/docker image를 docker hub에 업로드 하기.md
  - raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md
  - raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md
status: growing
confidence: high
---

# Docker

## 무엇인가

Docker는 application 실행환경을 image로 만들고, Docker Engine이 그 image를 격리된 container process로 실행하도록 관리하는 platform이다. 이 위키에서는 Linux host에서 server를 직접 설치·실행한 다음, 실행환경을 **image·container·network·storage·recipe·manifest·registry**로 나누어 재현하는 도구로 등장했다.

## 이 위키에서의 첫 등장과 필요성

2026-04-28에 Maven JAR를 Linux host process로 직접 실행한 뒤 Docker 설치·권한 설정과 기성 web/DB image를 배웠다. host에 application과 의존성을 직접 반복 설치하는 대신, 실행 단위를 image로 준비하고 container로 생성·삭제할 수 있다는 점이 다음 수업의 network·mount·registry·Dockerfile·Compose로 확장됐다.

## 구성 요소와 책임 경계

| 구성 요소 | 책임 | 책임이 아닌 것 |
|---|---|---|
| Linux host | filesystem·user/group·service·port·Docker Engine 실행 기반 | container image의 application recipe 자체 |
| Docker Engine | image·container·network·volume 생성과 실행 | Dockerfile 작성, application 업무 성공 판정 |
| image | 새 container를 만들 실행환경 artifact | 현재 실행 중인 process |
| container | image에서 생성된 실행 process·writable layer | host OS 전체나 영구 저장소 |
| network | container 이름 기반 내부 통신 | host/browser의 port 공개 |
| bind mount·volume | container 밖의 file/data 연결 | image build 절차 기록 |
| Dockerfile | image를 만드는 instruction·build context | 여러 service의 runtime 관계 선언 |
| Compose | 여러 service·network·volume·environment·port 관계 선언 | DB readiness·CI/CD·운영 cluster 자동 해결 |
| registry | tag가 붙은 image를 환경 사이에 저장·전달 | source code·Git history 관리 |

Dockerfile과 Compose는 Docker Engine을 대신하지 않는다. 파일은 원하는 상태를 선언하고, 실제 image/container/network/volume을 만드는 주체는 Engine이다.

## 날짜별 기술 이력

### [[summaries/2026-04-28-maven-spring-boot-docker-intro|04-28 — 설치, image와 container]]

- setup script의 CRLF·실행 권한을 처리하고 Docker service와 일반 사용자 group/session 권한을 확인했다.
- Apache·Nginx·MySQL·WordPress 기성 image를 받고 container 이름·detached 실행·host:container port를 경험했다.
- WordPress와 MySQL을 사용자 정의 network에서 이름으로 연결했다.

설치됨, daemon service active, 일반 사용자 socket 접근, image 존재, container `Up`, browser/DB 응답은 서로 다른 완료 조건이다.

### [[summaries/2026-04-29-docker-network-volume-image|04-29 — network, file, storage, commit, registry]]

- MariaDB–Redmine을 같은 network에 연결하고 browser 진입 port와 container 간 DB host를 구분했다.
- `exec`·`cp`로 내부 상태와 일회 파일 복사를 확인한 뒤 bind mount와 named volume으로 지속 연결을 배웠다.
- 변경 container를 `commit`해 새 image로 만들고 새 container에서 file과 homepage를 확인했다.
- local image를 registry 형식으로 전달하는 실제 순서인 login→tag→push를 수행했고, 다른 환경에서는 namespace 누락 오류와 올바른 pull/run 명령을 기록했다. remote 성공 출력은 보존되지 않았다.

registry 절차는 [[concepts/docker-registry-tag-push-pull|Docker registry tag·push·pull]]가 맡고, image/container의 기본 구분은 [[concepts/docker-image-container|Docker 이미지와 컨테이너]]가 맡는다.

### [[summaries/2026-04-30-dockerfile-spring-load-balancing|04-30 — Dockerfile, application image, reverse proxy]]

- Apache/Nginx homepage를 Dockerfile과 build context로 image에 넣고 build→container→browser 순서로 확인했다.
- Maven JAR를 `FROM`·`ARG`·`COPY`·`EXPOSE`·`ENTRYPOINT`가 있는 Dockerfile로 image화했다.
- MySQL과 Spring container를 같은 network에 연결해 두 container의 `Up` 상태와 DB row를 확인했다. Spring log·browser는 확인 기준과 명령/URL만 있고 실제 성공 출력은 보존되지 않았다.
- `proxy-net`에서 Nginx reverse proxy가 Apache·Nginx backend group으로 요청을 분배했다.

image build 성공은 container `Up`이나 application·DB·browser 성공과 같지 않다. reverse proxy 흐름은 [[concepts/docker-reverse-proxy-load-balancing|Docker reverse proxy와 로드 밸런싱]]에서 host Nginx·단일 web container·AWS ALB와 분리한다.

### [[summaries/2026-05-01-docker-compose|05-01 — Compose와 다중 service]]

- MySQL+Spring Boot와 MySQL+WordPress의 service·network·volume·environment·port·`depends_on` 관계를 YAML로 선언했다.
- 첫 Compose 실습은 자원 생성, container `Up`, DB 작업 결과를 확인했다. browser·`down`·잔존 자원은 명령과 확인 절차만 기록됐고 결과는 미보존이다.
- 제공 WordPress manifest의 들여쓰기와 요구사항 값 불일치를 수정했다.

Compose `up`, DB readiness, application/browser 성공, `down`, volume/image 삭제는 각각 별도 완료 조건이다.

## 대표 artifact와 입력 → 처리 → 결과

| artifact | 입력 | Docker가 처리한 것 | 확인 결과 |
|---|---|---|---|
| 기성 web/DB image | image 이름·실행 옵션 | pull·container 생성·port/network 연결 | 상태와 browser/DB를 별도 확인 |
| bind mount·named volume | host path 또는 volume 이름 | container path에 외부 storage 연결 | inspect·browser·삭제 범위를 확인 |
| commit image | 변경된 running container | writable 상태를 새 image로 snapshot | 새 container의 file·homepage 확인 |
| registry image | local image와 registry tag | login 뒤 layer push, 다른 환경 pull/run | push digest는 확인, 다른 환경의 최종 browser 결과는 원본에 독립 보존되지 않음 |
| Dockerfile image | base·copy할 artifact·start instruction·context | instruction layer를 실행해 image build | image 목록→container→browser/application 순으로 확인 |
| reverse proxy | network·backend·mounted config | proxy container가 upstream으로 request 전달 | URL·새로고침별 backend 응답 관찰 |
| Compose project | image와 service 관계 YAML | project network·volume·container 생성/정리 | `Up`·DB 결과와 browser·`down` 절차의 근거 수준 구분 |

## 확인 상태를 과장하지 않는 법

1. **설치됨**: Docker package/Engine이 준비됐다는 뜻이다.
2. **image build/pull됨**: container를 만들 artifact가 있다는 뜻이다.
3. **container `Up`**: process가 실행 중이라는 뜻이지 DB readiness나 업무 성공을 보장하지 않는다.
4. **network 연결됨**: container 간 경로가 있다는 뜻이지 host/browser port가 열린 것은 아니다.
5. **DB readiness**: 실제 prompt·query·application 연결을 별도로 확인해야 한다.
6. **proxy/browser 응답**: request가 proxy와 backend를 왕복했다는 통합 결과다.
7. **registry push/pull**: image 전달 상태이며 source 배포나 application 기능 검증과 다르다.
8. **Compose `up/down`**: project 자원 생명주기이며 volume/image 삭제 범위는 별도다.

## 직접 수업과 후속 활용 경계

### Linux 과목에서 직접 수행

- Linux VM의 Docker 설치·service·group/session 권한
- image/container lifecycle, port, network, `exec`·`cp`, bind mount·volume
- `commit`, 수동 registry tag·login·push·pull/run
- Dockerfile image build, Spring Boot+MySQL container, Nginx reverse proxy
- Compose로 두 종류의 다중 service 관계를 선언하고 첫 실습의 `Up`·DB 결과를 확인; browser·정리 결과는 미보존

### 후속 과목에서 확장

- AWS EC2는 cloud VM과 network/security resource 위에서 container를 실행하는 별도 환경이다.
- CI/CD는 GitHub push를 trigger로 test/build, registry push, server 갱신을 자동화한다. Linux 수업의 수동 push가 곧 workflow 성공을 뜻하지 않는다.
- Passwordless·중간 프로젝트에서 Docker/Compose를 사용해도 해당 제품 구성과 application 통합 결과는 후속 수업에 귀속한다.
- 단계 9 두 가이드는 backend/frontend·database와 Passwordless server를 container로 배치하는 명령·Dockerfile·workflow snippet을 제시한다. 이 raw 폴더에는 실제 image, digest, container state, log가 없으므로 build·push·run·application 성공은 확정하지 않는다.

## 프로젝트·면접에서 설명할 관점

“Docker를 썼다”보다 **어떤 artifact와 완료 조건을 관리했는지** 설명해야 한다. 예를 들면 “Maven JAR를 Dockerfile로 image화하고 MySQL과 network로 연결했으며, container `Up`뿐 아니라 DB row와 browser 응답을 따로 확인했다. 이후 Compose로 service 관계를 선언했지만 `depends_on`을 readiness로 간주하지 않았다”처럼 말할 수 있다.

## 관련 개념

- [[concepts/docker-install-permission-setup|Docker 설치와 권한 설정]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[concepts/docker-cp-exec-container-files|Docker exec/cp와 컨테이너 파일 다루기]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[concepts/docker-registry-tag-push-pull|Docker registry tag·push·pull]]
- [[concepts/docker-reverse-proxy-load-balancing|Docker reverse proxy와 로드 밸런싱]]
- [[concepts/docker-compose-manifest|Docker Compose manifest]]
- [[concepts/dockerfile-vs-compose|Dockerfile vs Docker Compose]]
- [[comparisons/docker-commit-vs-dockerfile|docker commit vs Dockerfile]]
- [[comparisons/virtual-machine-vs-docker-container|가상 머신(VM) vs Docker 컨테이너]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md`
- `raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md`
- `raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md`
- `raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md`
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md`
- `raw/KoreaICT/5. Linux/교육 자료/docker image를 docker hub에 업로드 하기.md` — 수동 registry 절차와 credential 저장 경고의 보조자료
- `raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md` — application image·CI/CD·server container 후속 설계
- `raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md` — 인증 server container·TLS 후속 설계