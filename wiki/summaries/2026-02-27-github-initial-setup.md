---
title: 2026-02-27 GitHub 초기 설정
created: 2026-07-02
updated: 2026-07-03
type: summary
tags: [java, curriculum, study-log]
sources:
  - raw/Study/1. Java/2026.02.27(금)/깃허브 초기 설정.md
  - raw/Study/1. Java/교육 자료/Github 교안(실습).pdf
  - raw/Study/1. Java/교육 자료/IntelliJ 교안.pdf
status: stable
confidence: high
---

# 2026-02-27 GitHub 초기 설정

## 한 줄 요약

Java 프로젝트 `MyJava`를 Git 저장소로 만들고 GitHub 원격 저장소와 IntelliJ 연동 흐름을 준비했다.

## 커리큘럼 위치

- Java 문법 학습과 동시에 소스 코드 이력 관리 습관을 만들기 시작한 날이다.
- 이후 Linux/Docker 단계의 [[concepts/git-github-collaboration|GitHub 협업 흐름]]과 연결된다.

## 배운 내용

- Git 설치 경로와 Git Bash/cmd에서의 `git.exe` 사용 맥락을 확인했다.
- `git config --global user.name`, `user.email`, `safe.directory`를 설정했다.
- `D:/java_project/MyJava` 위치에서 `git init`으로 로컬 저장소를 만들었다.
- GitHub의 원격 저장소 URL을 IntelliJ 프로젝트와 연결할 준비를 했다.
- IntelliJ 교안에서는 `Clone Repository`, Git/GitHub 플러그인·설정 흐름도 함께 다룬다.

## 핵심 실습 / 예제

- 사용자명/이메일 등록
- 안전 디렉터리 등록
- `git init`
- GitHub 원격 저장소: `MyJava`
- IntelliJ에서 Git과 GitHub 연동

## 헷갈린 점 / 질문

- `git init`은 내 폴더를 Git이 추적할 수 있게 만드는 작업이고, GitHub에 올라가는 것은 별도의 remote/push 작업이다.
- `git config --global`은 현재 프로젝트만이 아니라 사용자 환경 전체에 적용된다.
- `safe.directory`는 Git이 “이 경로는 신뢰할 수 있다”고 인식하도록 하는 설정이다.

## 관련 페이지

- [[entities/git|Git]]
- [[entities/github|GitHub]]
- [[entities/intellij-idea|IntelliJ IDEA]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]]

## 출처

- `raw/Study/1. Java/2026.02.27(금)/깃허브 초기 설정.md`
- `raw/Study/1. Java/교육 자료/Github 교안(실습).pdf`
- `raw/Study/1. Java/교육 자료/IntelliJ 교안.pdf`
