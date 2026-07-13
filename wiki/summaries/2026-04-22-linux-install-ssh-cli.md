---
title: 2026-04-22 Linux 설치, SSH 접속, 기본 CLI
created: 2026-07-06
updated: 2026-07-13
type: summary
tags: [linux, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
status: growing
confidence: high
---

# 2026-04-22 Linux 설치, SSH 접속, 기본 CLI

## 한 줄 요약

VirtualBox에 Ubuntu VM을 설치하고 브리지 네트워크, SSH/MobaXterm 접속, apt, prompt, 파일 시스템 구조로 Linux 서버 학습을 시작했다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

Spring/React 프로젝트를 실제 서버에 올리려면 IDE 밖의 운영체제에 접속하고 명령어로 설치·실행·파일 관리를 할 수 있어야 한다.

## 핵심 개념

- Ubuntu ISO, VirtualBox, MobaXterm의 역할을 구분했다.
- VM 네트워크를 브리지 모드로 설정하고 IP 기반 접속 아이콘을 만들었다.
- `apt`로 패키지를 설치하는 개념을 배웠다.
- Linux prompt 구조, 관리자 prompt, `/` 기준 디렉터리 구조를 처음 확인했다.

## 실습 / 예제

VirtualBox VM 생성 → 네트워크 설정 → MobaXterm SSH 접속 → 기본 명령어/디렉터리 구조 확인 순서로 실습했다.

## 헷갈린 점 / 질문

VM은 별도 컴퓨터처럼 동작하는 가상 머신이고, MobaXterm은 그 VM에 접속하는 클라이언트다. 둘을 같은 프로그램으로 보면 이후 포트/IP 문제에서 헷갈린다.

## 관련 페이지

- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]], [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]], [[entities/linux|Linux]], [[entities/docker|Docker]], [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md`
