---
title: Docker 설치와 권한 설정
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [linux, docker, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
  - raw/KoreaICT/5. Linux/교육 자료/도커 컴포즈 종합 실습.md
status: growing
confidence: high
---

# Docker 설치와 권한 설정

## 정의

이 페이지는 Ubuntu host에 Docker Engine을 설치하고, daemon service와 Unix socket 접근 권한을 확인해 일반 사용자가 Docker client 명령을 실행할 수 있게 만드는 흐름을 맡는다. image/container 생명주기는 [[concepts/docker-image-container|Docker 이미지와 컨테이너]], container 내부 작업은 [[concepts/docker-cp-exec-container-files|Docker exec/cp와 컨테이너 파일 다루기]]의 책임이다.

## 수업에서 왜 필요했는가

[[summaries/2026-04-28-maven-spring-boot-docker-intro|2026-04-28]]에는 Spring Boot를 host의 JAR process로 실행한 뒤, code·dependency·JDK·설정을 매 server에 반복 준비하지 않기 위해 Docker로 전환했다. Docker 실습을 시작하려면 먼저 세 가지가 필요했다.

1. Docker 프로그램과 daemon이 설치되어야 한다.
2. daemon service가 실제로 실행 중이어야 한다.
3. 현재 사용자가 Docker socket을 사용할 권한을 가져야 한다.

05-01에는 새 Gomdori VM에서 OpenSSH·UFW를 준비한 뒤 같은 setup 절차를 다시 수행했다. 이는 Docker 설치 절차의 반복 확인이지, 04-28의 성공 결과를 대신하는 독립 Docker 수업일은 아니다. P09도 이 두 번째 실습의 checklist를 보조할 뿐 실행 성공을 새로 만들지 않는다.

## 04-28 설치 흐름과 artifact

| 순서 | 입력·처리 | 확인 결과와 책임 |
|---:|---|---|
| 1 | Windows에서 받은 `docker_setup.sh.txt`를 일반 사용자 home에 두고 `/root/docker_setup.sh`로 복사 | 설치용 shell artifact가 root 영역에 준비됨. 파일 복사는 설치 완료가 아님 |
| 2 | `sudo su -`로 root session에 들어가 package index를 갱신 | script에 개별 `sudo`가 없고 `/root` 파일을 다뤄 root 권한을 사용함 |
| 3 | `dos2unix`를 설치하고 setup script에 적용 | Windows CRLF 때문에 Linux shell이 script를 잘못 읽을 수 있는 형식을 교정함 |
| 4 | `chmod +x`로 실행 bit를 부여한 뒤 script 실행 | 실행 권한과 실제 script 실행은 별도 단계임 |
| 5 | Docker container help 확인 | Docker CLI가 설치되어 명령을 해석하는지 확인함 |
| 6 | `systemctl status docker`에서 `active (running)` 확인 | Linux의 systemd가 Docker daemon service를 실행 중인지 확인함 |
| 7 | root session을 나와 일반 사용자를 `docker` group에 추가하고 group membership 확인 | 사용자 계정 정보가 바뀌었지만 현재 login shell의 supplementary group은 아직 예전 값일 수 있음 |
| 8 | 일반 사용자로 `docker version` 실행 | client와 server 정보가 함께 나오면 socket을 통해 daemon에 접근한 것까지 확인됨 |

R05에서 CRLF·`dos2unix`·실행 권한은 실제로 기록된 문제와 처리다. 일반적인 설치에서 항상 같은 오류가 난다고 확대하지 않는다. ^[raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md]

## Linux host와 Docker Engine의 책임 분리

| 계층 | 책임 | 이 계층에서 확인할 것 |
|---|---|---|
| Linux filesystem·권한 | setup script 위치, CRLF 교정, 실행 bit, `/root` 접근 | 파일 존재, 형식, `chmod`, root/sudo 사용 위치 |
| systemd | Docker daemon service 시작과 상태 관리 | `active (running)` 여부 |
| Docker Engine daemon | image·container·network·volume 실제 관리 | server 정보 응답과 후속 Docker 명령 결과 |
| Docker client | 사용자의 명령을 socket을 통해 daemon에 요청 | client 설치와 daemon 연결을 구분 |
| Linux group·login session | 일반 사용자의 Docker socket 접근 권한 | account의 group membership과 현재 shell 반영 여부 |

Docker group은 사실상 Docker daemon을 제어할 수 있는 강한 권한이다. 단순히 `docker` 실행 파일에 execute bit를 주는 문제와 같지 않다. Linux file·user·group의 선행 개념은 [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]에서 이어진다.

## 왜 group 추가 뒤 바로 반영되지 않는가

`usermod -aG`는 계정의 supplementary group 정보를 바꾸지만, 이미 열린 login session의 process들은 시작할 때 받은 group 목록을 그대로 유지할 수 있다. 그래서 계정 조회에서는 Docker group이 보여도 현재 shell의 `docker version`은 socket permission error를 낼 수 있다.

수업에서는 logout 후 새 session으로 다시 접속해 확인했다. 판단 순서는 다음과 같다.

1. account가 Docker group에 등록됐는지 확인한다.
2. 현재 shell에서 일반 사용자 Docker 명령을 실행한다.
3. permission error가 나면 logout/login으로 새 login session을 만든다.
4. 다시 `docker version`을 실행해 client 정보뿐 아니라 server 정보도 응답하는지 확인한다.

`sudo docker ...`가 한 번 성공했다는 사실은 일반 사용자 권한 반영의 증거가 아니다. root가 socket을 사용한 결과일 뿐이다.

## 완료 조건을 한 번에 합치지 않기

| 완료 조건 | 통과 증거 | 아직 보장하지 않는 것 |
|---|---|---|
| script 준비 | root 영역에 파일 존재 | 실행 가능·Docker 설치 |
| script 실행 가능 | CRLF 교정과 execute bit | script 성공 종료 |
| Docker 설치 | CLI help가 응답 | daemon active·일반 사용자 접근 |
| service 실행 | Docker service가 active | 특정 image 존재·container 실행 |
| 계정 권한 설정 | account가 Docker group에 속함 | 현재 shell 반영 |
| 일반 사용자 권한 반영 | 재login 후 `docker version`의 client/server 응답 | web container·browser 응답 |

따라서 “Docker가 설치됐다”, “service가 active다”, “일반 사용자가 daemon에 접근한다”, “container가 실행된다”는 서로 다른 완료 조건이다. 실행 중 container와 browser 응답은 설치 페이지가 아니라 image/container 페이지에서 확인한다.

## 자주 헷갈리는 점과 선택 기준

- **`sudo` 한 명령과 root session:** 파일 하나를 다룰 때는 명령별 `sudo`가 범위를 좁힌다. 수업에서는 `/root`의 setup script 전체가 개별 `sudo` 없이 작성돼 root session을 사용했다. 이를 모든 Docker 작업을 root로 해야 한다는 규칙으로 일반화하지 않는다.
- **`chmod +x`와 Docker 권한:** 전자는 setup script 파일 실행 권한, 후자는 Docker socket 접근 권한이다.
- **CLI 설치와 daemon 상태:** help가 보인다고 service가 active라고 단정하지 않는다.
- **group 등록과 현재 session:** account DB 변경과 이미 열린 shell의 group 목록은 반영 시점이 다르다.
- **P09의 OpenSSH/UFW:** 새 VM에 접속하기 위한 Linux host 준비다. Docker daemon 자체의 network·container 성공 조건이 아니다.

## 선행·후속 경계

- 선행: [[concepts/linux-package-archive|Linux 패키지·다운로드·압축]]과 [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]에서 package, root/sudo, script execute, group을 배웠다.
- 직접 후속: [[concepts/docker-image-container|Docker 이미지와 컨테이너]]에서 기성 image를 pull/run하고 container 상태와 browser 응답을 확인한다.
- 05-01 후속: [[summaries/2026-05-01-docker-compose|Docker Compose 수업]]의 새 VM setup은 설치 절차를 반복한 뒤 Compose manifest 실습으로 넘어간다.
- 범위 밖 후속: Dockerfile image, Compose service 선언, Docker registry, AWS EC2, CI/CD 배포는 설치·socket 권한과 다른 책임이다. 이 페이지는 그 실행 성공을 주장하지 않는다.

## 관련 개념

- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[concepts/linux-process-service-port-firewall|Linux process·service·port·firewall 진단]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[entities/docker|Docker]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md` — 설치 시작 맥락, setup script·CRLF·권한·service·group·재login의 최우선 근거
- `raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md` — 새 VM에서 setup 절차를 반복한 후 Compose로 넘어간 실제 순서
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md` — Linux 권한과 Docker daemon의 복습 연결
- `raw/KoreaICT/5. Linux/교육 자료/도커 컴포즈 종합 실습.md` — 05-01 setup checklist 보조자료이며 독립 성공 결과로 사용하지 않음