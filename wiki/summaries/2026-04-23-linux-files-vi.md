---
title: 2026-04-23 Linux 파일·디렉터리와 vi 편집기
created: 2026-07-06
updated: 2026-07-09
type: summary
tags: [linux, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/2026.04.23(목)/2026.04.23(목).md
status: growing
confidence: high
---

# 2026-04-23 Linux 파일·디렉터리와 vi 편집기

## 한 줄 요약

tree, mkdir, touch, cp, mv, find, vi, redirection으로 Linux 파일·디렉터리 조작과 편집 기본기를 익혔다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

서버에서는 GUI 탐색기보다 CLI로 파일을 만들고 옮기고 편집하는 일이 많다. 배포 설정 파일과 로그를 다루는 기반이다.

## 핵심 개념

- `tree / -L 1`로 최상위 디렉터리 구조를 확인했다.
- 실습용 디렉터리 구조를 만들고 파일 생성/복사/이동/검색을 반복했다.
- vi의 명령 모드/입력 모드/저장 종료 흐름을 배웠다.
- redirection으로 명령 결과를 파일에 쓰거나 이어붙이는 방식을 확인했다.

## 실습 / 예제

방송사/프로그램 이름 같은 디렉터리 구조를 만들고, 파일을 복사·이동·검색하면서 경로 감각을 익혔다.

## 헷갈린 점 / 질문

`>`는 덮어쓰기, `>>`는 이어쓰기다. vi는 입력 모드에서 바로 저장할 수 없고 ESC로 명령 모드로 돌아간 뒤 `:wq` 같은 명령을 써야 한다.

## 관련 페이지

- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]], [[entities/linux|Linux]], [[entities/docker|Docker]], [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.23(목)/2026.04.23(목).md`
