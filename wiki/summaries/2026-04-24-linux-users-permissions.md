---
title: 2026-04-24 Linux 사용자, 그룹, 권한
created: 2026-07-06
updated: 2026-07-09
type: summary
tags: [linux, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/2026.04.24(금)/2026.04.24(금).md
status: growing
confidence: high
---

# 2026-04-24 Linux 사용자, 그룹, 권한

## 한 줄 요약

`ls -l` 권한 문자열, owner/group/others, `/etc/passwd`, `/etc/shadow`, `/etc/group`, user/group 생성과 권한 변경을 실습했다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

서버 오류 중 상당수는 코드 문제가 아니라 사용자·그룹·권한 문제다. 파일을 누가 읽고 실행할 수 있는지 해석해야 배포 문제를 해결할 수 있다.

## 핵심 개념

- `-rw-rw-r--` 같은 권한 문자열을 파일 종류와 소유자/그룹/기타 권한으로 나누어 읽었다.
- 사용자 생성 시 같은 이름의 그룹이 자동 생성되는 흐름을 확인했다.
- `/etc/passwd`, `/etc/shadow`, `/etc/group`의 역할을 배웠다.
- 요구사항에 맞는 사용자/그룹 생성, 홈 디렉터리, shell, 기본 환경 설정을 실습했다.

## 실습 / 예제

skywalker 같은 계정을 만들고 관리자 계정에서 정보를 조회하며 사용자·그룹·권한이 실제 파일에 어떻게 표시되는지 확인했다.

## 헷갈린 점 / 질문

소유자(owner)와 그룹(group)은 이름이 같을 수 있지만 같은 개념은 아니다. 권한 문자열도 user/group/others 세 묶음으로 읽어야 한다.

## 관련 페이지

- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]], [[entities/linux|Linux]], [[entities/docker|Docker]], [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.24(금)/2026.04.24(금).md`
