---
title: Linux
created: 2026-07-02
updated: 2026-07-14
type: entity
tags: [linux]
sources:
  - raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
  - raw/KoreaICT/5. Linux/2026.04.23(목)/2026.04.23(목).md
  - raw/KoreaICT/5. Linux/2026.04.24(금)/2026.04.24(금).md
  - raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md
  - raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
  - raw/KoreaICT/5. Linux/교육 자료/Linux/Linux 이론.pdf
  - raw/KoreaICT/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf
status: growing
confidence: high
---

# Linux

## 무엇인가

Linux는 서버 운영체제로 널리 쓰이는 Unix 계열 운영체제다. 이 위키에서는 Spring/React로 만든 웹서비스를 실제 서버 환경에서 실행·배포하기 위해 배우는 운영체제 단계로 등장했다.

## 이 위키에서의 맥락

Java와 Spring Boot 수업에서는 코드를 작성하고 IDE에서 실행하는 개발자 관점이 중심이었다. Linux 과정부터는 서버에 접속하고, 파일을 배치하고, 권한을 관리하고, 포트를 열고, 빌드 산출물을 실행하는 운영 관점이 추가된다.

## 핵심 기능 / 특징

- SSH 원격 접속과 사용자 프롬프트.
- `/`를 기준으로 한 파일 시스템과 CLI 명령.
- 사용자·그룹·권한 기반 보안 모델.
- `apt`, `systemctl`, `ufw` 같은 서버 관리 명령.
- Maven/Spring Boot jar 실행과 Docker 실행 환경의 기반.

## 학습 이력

- [[summaries/2026-04-22-linux-install-ssh-cli|2026-04-22]]: Ubuntu VM, SSH, MobaXterm 접속.
- [[summaries/2026-04-23-linux-files-vi|2026-04-23]]: 파일·디렉터리·vi.
- [[summaries/2026-04-24-linux-users-permissions|2026-04-24]]: 사용자·그룹·권한.
- [[summaries/2026-04-27-linux-archive-java-alias|2026-04-27]]: 다운로드·압축·소유권·alias.
- [[summaries/2026-04-28-maven-spring-boot-docker-intro|2026-04-28]]: Spring Boot jar 실행과 Docker 입문.
- [[summaries/2026-05-06-linux-subject-review|Linux 총정리]]: VM/SSH·권한·서버 실행·Docker·GitHub 협업을 하나의 운영 학습 흐름으로 복습.

## 관련 개념

- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]
- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[concepts/linux-package-archive|Linux 패키지·다운로드·압축]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[entities/docker|Docker]]

## 최신 원본 대조

Linux를 VM/SSH로 접속해 파일·권한·방화벽·Spring Boot와 Docker를 실제 실행한 서버 기반 OS로 다시 명시했다. 2026-04-22~28의 흐름은 이후 Docker·AWS·CI/CD 운영 문제의 출발점이다.

## 출처

- `raw/KoreaICT/5. Linux` 날짜별 MD 및 `Linux 총정리.md`
