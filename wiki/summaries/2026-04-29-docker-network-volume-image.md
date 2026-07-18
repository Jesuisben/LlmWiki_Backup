---
title: 2026-04-29 Docker 네트워크, 마운트, 사용자 정의 이미지와 registry
created: 2026-07-06
updated: 2026-07-18
type: summary
tags: [linux, docker, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md
status: growing
confidence: high
---

# 2026-04-29 Docker 네트워크, 마운트, 사용자 정의 이미지와 registry

## 한 줄 요약

MariaDB–Redmine 통신에서 시작해 host↔container 파일 복사, bind mount와 named volume, `docker commit`, Docker Hub tag·push·pull까지 이어 가며 컨테이너의 **통신·파일·데이터·이미지 배포 생명주기**를 각각 실습한 날이다.

## 왜 이 순서로 배웠는가

전날에는 WordPress와 MySQL을 같은 사용자 정의 network에 연결하면서 image와 container의 기본 생명주기를 배웠다. 이날은 “컨테이너끼리는 어떻게 찾는가”, “수정한 파일과 DB 데이터는 삭제 뒤에도 남는가”, “내가 바꾼 실행환경을 다른 컴퓨터로 어떻게 옮기는가”라는 운영 문제를 순서대로 해결했다.

1. network로 DB와 애플리케이션을 연결했다.
2. `docker exec`와 `docker cp`로 실행 중인 컨테이너의 내부 상태를 확인·변경했다.
3. 일회 복사와 달리 계속 연결되는 bind mount·named volume을 비교했다.
4. 변경된 컨테이너를 image로 저장하고 registry를 통해 다른 환경으로 전달했다.

이 흐름은 다음 날의 재현 가능한 Dockerfile과 05-01 Compose로 이어진다. `commit`으로 “현재 상태”를 옮긴 경험이 있어야 Dockerfile이 “변경 절차”를 기록하는 이유가 분명해진다.

## 교시별 학습 전개

### 1교시 — MariaDB와 Redmine을 같은 network에 연결

- `network02`를 먼저 만들고 `mariadb02`, `redmine02` 순서로 컨테이너를 실행했다.
- Redmine의 DB host에는 IP 대신 같은 network의 컨테이너 이름 `mariadb02`를 사용했다.
- DB 이름·사용자·비밀번호 설정은 MariaDB를 만들 때 전달한 값과 Redmine 쪽 연결 값이 서로 맞아야 했다. 실제 credential은 이 Summary에 재노출하지 않는다.
- 브라우저에서 host의 8883 포트로 Redmine 화면을 확인하고, `docker container ls -a`에서 두 컨테이너가 실행 중인지 확인했다.
- 실습 뒤에는 컨테이너를 중지·삭제하고 image를 정리했다. network 생성, container 실행, browser 확인, 자원 정리가 한 실습의 완결 단위였다. ^[raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md]

### 2~3교시 — `exec`와 `cp`로 컨테이너 파일 다루기

- 압축 실습 파일을 Linux home에 옮기고 `docker/` 아래에 풀었다.
- Apache container의 document root를 `docker exec`으로 조회하고 기본 `index.html`을 확인했다.
- host의 HTML·이미지를 container로 복사하자 브라우저의 홈페이지가 바뀌었다.
- 반대로 container의 파일을 host에 다른 이름으로 복사해 양방향 이동을 확인했다.
- 이어서 `nginx88`의 `/usr/share/nginx/html/`에도 HTML과 이미지를 복사하고 browser 결과를 확인했다.

여기서 `docker cp`는 **복사 시점의 파일 하나를 옮기는 작업**이다. 이후 host 파일을 고쳐도 container에 자동 반영되는 연결이 아니다.

### 3~4교시 — bind mount로 host와 container 경로 연결

- Apache의 document root에 빈 host directory를 bind mount했을 때 기존 기본 페이지가 가려지고 `Index of /`가 보였다.
- `docker container inspect`의 `Mounts`에서 `Type: bind`, host `Source`, container `Destination`을 확인했다.
- host의 mount directory에 HTML과 이미지를 넣고 이름을 `index.html`로 맞추자 container에 별도 `cp`하지 않아도 browser 결과가 바뀌었다.
- Nginx bind mount에서는 빈 directory 때문에 403이 발생했고, host 쪽에 실제 `index.html`을 넣은 뒤 정상 페이지를 확인했다. Apache의 directory listing과 Nginx의 기본 동작 차이가 같은 “빈 mount”에서 다른 결과를 만들었다.

입력은 host directory의 파일 변경이고, 처리는 bind mount의 동일 경로 연결이며, 결과는 container document root와 browser 응답의 즉시 변경이다.

### 5교시 — named volume과 데이터 지속성

- Docker가 관리하는 `mount-vol`을 만든 뒤 Apache document root에 연결했다.
- `docker volume inspect`에서 실제 mount point와 volume 이름을 확인했다.
- Docker 관리 영역을 host에서 직접 고치기보다 container를 통해 다루는 방식을 권장한다고 정리했다.
- 자원 정리는 container를 먼저 중지·삭제한 뒤 volume을 삭제하는 순서로 진행했다.

bind mount는 host의 명시적 경로를 사용자가 관리하고, named volume은 Docker 관리 영역을 사용한다. 둘 다 container filesystem 밖에 데이터를 두지만 관리 주체와 위치가 다르다.

### 5~6교시 — `docker commit`으로 사용자 정의 image 생성

- Apache container에 HTML·이미지를 복사하고 container 내부에서 `jeju.txt`를 만들었다.
- 수정된 `commit-ctr`를 `jeju-img`로 commit했다.
- 새 image로 `jeju-ctr`를 실행한 뒤 `jeju.txt`와 browser 화면이 그대로 있는지 확인했다.
- 같은 과정을 Nginx container에도 반복해 `pohang-nginx-img`를 만들고, 그 image로 새 container를 띄워 내부 파일과 browser 결과를 확인했다.

이 실습의 입력은 실행 중 container의 변경 상태, 처리는 `docker commit`, 결과는 동일 파일을 가진 새 image와 새 container다. image가 단순 이름표가 아니라 새로운 container를 재생성할 수 있는 배포 단위임을 확인했다.

### 7교시 — Docker Hub registry로 image 전달

- local image를 Docker Hub 형식의 `계정/image:tag`로 tag했다.
- 로그인 뒤 push 결과에서 layer upload와 digest를 확인했다.
- 다른 환경에서 local 이름만으로 실행했을 때는 image를 찾지 못하고 접근 오류가 발생했다.
- registry namespace를 포함한 올바른 pull/run 명령을 기록했다. 다만 해당 명령의 성공 출력이나 새 container의 상태·browser 결과는 원본에 남아 있지 않다.

실제 수업 순서는 **local image 준비 → registry 인증 → registry용 tag → push → 다른 환경의 pull/run 명령 기록**이다. 계정명·repository URL·비밀번호·PAT와 같은 실제 식별자·credential은 일반화했다. 로그인 출력에 credential이 평문 설정 파일에 저장될 수 있다는 경고도 있었으므로, 성공 메시지만 보고 보안 저장이 해결됐다고 생각하면 안 된다.

### 8교시 — AWS 계정 생성 예고

마지막에는 AWS 회원가입 링크를 열었다. 이는 다음 과목을 위한 계정 준비이며, 이날 Linux 수업에서 VPC·EC2·Security Group·배포를 구현한 것이 아니다. AWS의 직접 학습과 실행 결과는 [[summaries/2026-05-06-aws-cloud-vpc-ec2|05-06 AWS 입문]] 이후에 귀속한다.

## 대표 실습: 수정한 홈페이지를 다른 환경에서 다시 실행하기

1. 웹 server container를 실행한다.
2. host 파일을 `docker cp`로 document root에 넣고, container 내부에 확인용 text를 만든다.
3. browser와 `cat`으로 변경 상태를 확인한다.
4. 변경된 container를 image로 commit한다.
5. 새 image로 다른 container를 실행해 HTML·이미지·text가 포함됐는지 다시 확인한다.
6. image를 registry용으로 tag하고 push한다.
7. 다른 환경에서는 registry namespace를 포함한 pull/run 명령으로 원격 image를 참조한다. 해당 명령의 성공 출력과 같은 웹 결과는 원본에 보존되지 않았다.

한 번의 파일 복사에서 끝나지 않고 **container 변경 → image 고정 → local 새 container 검증 → registry push digest 확인**까지 이어진 것이 핵심이다. 다른 환경에서는 namespace 누락 오류와 올바른 명령만 확인할 수 있으므로 remote 재생성 성공으로 확대하지 않는다.

## 헷갈리기 쉬운 지점

- **Docker network와 port mapping은 다르다.** network는 container 간 이름 기반 통신에 쓰였고, `-p`는 host/browser가 container service로 들어오는 경로였다.
- **`docker cp`와 mount는 다르다.** `cp`는 일회 복사이고, bind mount·volume은 container 밖 저장공간을 계속 연결한다.
- **빈 bind directory는 원래 image의 document root 내용을 가릴 수 있다.** 그래서 Apache에서는 directory listing, Nginx에서는 403처럼 예상과 다른 첫 화면이 나왔다.
- **container를 삭제하면 내부 writable layer는 사라질 수 있다.** 지속 데이터는 bind mount나 volume으로 분리해야 한다.
- **`docker commit`은 재현 절차가 아니다.** 현재 상태의 snapshot은 만들 수 있지만 어떤 작업으로 그 상태가 됐는지는 다음 날 Dockerfile처럼 명시적으로 남겨야 한다.
- **Docker Hub와 GitHub는 역할이 다르다.** 이날 Hub에는 container image를 올렸고, 05-04 이후 GitHub에는 source와 Git commit을 공유했다.

## 이전·다음 연결과 과목 경계

- 이전: [[summaries/2026-04-28-maven-spring-boot-docker-intro|04-28]]의 image/container와 WordPress–MySQL network 입문을 multi-container 연결·저장·배포로 확장했다.
- 다음: [[summaries/2026-04-30-dockerfile-spring-load-balancing|04-30]]에는 snapshot 대신 Dockerfile로 image를 만들고 Spring Boot+MySQL과 Nginx reverse proxy를 구성한다.
- 후속: Docker Hub image는 [[concepts/ci-cd-automation|CI/CD 자동화]]에서 자동 build·push·배포 단위로 다시 쓰이지만, 이날은 사람이 tag·login·push·pull한 수동 실습이다.
- AWS: 계정 가입 안내만 있었으며 [[entities/amazon-ec2|Amazon EC2]]에서 container를 실행한 날이 아니다.

## 관련 페이지

- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[concepts/docker-cp-exec-container-files|Docker exec/cp와 컨테이너 파일 다루기]]
- [[comparisons/docker-cp-vs-bind-mount-vs-volume|docker cp vs bind mount vs volume]]
- [[comparisons/docker-commit-vs-dockerfile|docker commit vs Dockerfile]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[entities/docker|Docker]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md`

날짜 MD의 교시·실습 순서를 최우선 근거로 사용했다. Docker Hub 보조자료의 계정·주소·credential은 이 페이지에 재노출하지 않았고, AWS 가입은 후속 과목 준비로만 분리했다.
