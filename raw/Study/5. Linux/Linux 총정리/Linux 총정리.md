---
title: Linux 총정리
created: 2026-07-03
updated: 2026-07-03
type: summary
tags: [linux, docker, ci-cd, study-log]
sources:
  - D:/Study_LLM_Wiki/raw/Study/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
  - D:/Study_LLM_Wiki/raw/Study/5. Linux/2026.04.23(목)/2026.04.23(목).md
  - D:/Study_LLM_Wiki/raw/Study/5. Linux/2026.04.24(금)/2026.04.24(금).md
  - D:/Study_LLM_Wiki/raw/Study/5. Linux/2026.04.27(월)/2026.04.27(월).md
  - D:/Study_LLM_Wiki/raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - D:/Study_LLM_Wiki/raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - D:/Study_LLM_Wiki/raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - D:/Study_LLM_Wiki/raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - D:/Study_LLM_Wiki/raw/Study/5. Linux/2026.05.04(월)/2026.05.04(월).md
  - D:/Study_LLM_Wiki/raw/Study/5. Linux/2026.05.06(수)/2026.05.06(수).md
  - D:/Study_LLM_Wiki/raw/Study/5. Linux/교육 자료/docker image를 docker hub에 업로드 하기.md
  - D:/Study_LLM_Wiki/raw/Study/5. Linux/교육 자료/도커 컴포즈 종합 실습.md
  - D:/Study_LLM_Wiki/raw/Study/5. Linux/교육 자료/리눅스 실습하기.md
status: growing
confidence: medium
---

Linux 총정리 (2026.04.22(수) ~ 2026.05.06(수))



#### \# 한 줄 요약

Linux 서버 기본 명령부터 Docker, Docker Compose, GitHub 협업까지 서버 배포의 바닥 흐름을 한 번에 묶은 총정리다.



#### \# 학습 흐름

2026-04-22에는 Ubuntu/SSH/CLI로 서버 접속을 시작했고, 04-23~04-24에는 파일·vi·사용자·권한을 익혔다. 04-27 이후에는 압축/다운로드/Java 실행, Maven/Spring Boot 실행, Docker 이미지·컨테이너·네트워크·볼륨·Dockerfile·Compose로 확장되었다. 마지막에는 GitHub/SourceTree/PR/충돌 해결이 배포 협업 흐름과 연결된다.



#### \# 핵심 개념

- Linux CLI: `pwd`, `cd`, `ls`, `mkdir`, `touch`, `cp`, `mv`, `find`, `vi`로 서버 파일 시스템을 다룬다.
- 권한: owner/group/others와 `rwx`, `sudo`, 사용자·그룹 관리를 통해 권한 오류를 해석한다.
- 서버 실행: Maven으로 Spring Boot jar를 만들고 Linux에서 포트·방화벽을 확인하며 실행한다.
- Docker: image/container, `exec`, `cp`, network, bind mount, volume, Dockerfile, Compose가 순차적으로 등장한다.
- 협업: branch, push, Pull Request, merge, pull, conflict 해결이 팀 개발의 기본 절차가 된다.



#### \# 실습 / 예제 흐름

VirtualBox Ubuntu 설치 후 MobaXterm/SSH로 접속하고, `/var/www/html` 같은 서버 경로를 다루며, Spring Boot jar를 직접 실행한다. 이후 MariaDB/Redmine/Spring Boot를 컨테이너로 띄우고 nginx upstream으로 로드밸런싱을 구성한 뒤 Compose manifest로 여러 컨테이너를 선언적으로 실행한다.



#### \# 자주 헷갈릴 점

- `cp`로 복사한 파일과 bind mount/volume으로 연결한 파일은 생명주기가 다르다.
- `docker commit`은 임시 스냅샷이고 Dockerfile은 재현 가능한 빌드 레시피다.
- Linux 권한 문제는 파일 권한, 소유자, 그룹, sudo 여부를 함께 봐야 한다.
- `git fetch`, `pull`, `clone`은 모두 원격과 관련 있지만 시점과 결과가 다르다.



#### \# 관련 위키 페이지

- [[entities/linux|Linux]]
- [[entities/docker|Docker]]
- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[concepts/docker-compose-manifest|Docker Compose manifest]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]]



#### \# 출처

- `D:/Study_LLM_Wiki/raw/Study/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md`
- `D:/Study_LLM_Wiki/raw/Study/5. Linux/2026.04.23(목)/2026.04.23(목).md`
- `D:/Study_LLM_Wiki/raw/Study/5. Linux/2026.04.24(금)/2026.04.24(금).md`
- `D:/Study_LLM_Wiki/raw/Study/5. Linux/2026.04.27(월)/2026.04.27(월).md`
- `D:/Study_LLM_Wiki/raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md`
- `D:/Study_LLM_Wiki/raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md`
- `D:/Study_LLM_Wiki/raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md`
- `D:/Study_LLM_Wiki/raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md`
- `D:/Study_LLM_Wiki/raw/Study/5. Linux/2026.05.04(월)/2026.05.04(월).md`
- `D:/Study_LLM_Wiki/raw/Study/5. Linux/2026.05.06(수)/2026.05.06(수).md`
- `D:/Study_LLM_Wiki/raw/Study/5. Linux/교육 자료/docker image를 docker hub에 업로드 하기.md`
- `D:/Study_LLM_Wiki/raw/Study/5. Linux/교육 자료/도커 컴포즈 종합 실습.md`
- `D:/Study_LLM_Wiki/raw/Study/5. Linux/교육 자료/리눅스 실습하기.md`
