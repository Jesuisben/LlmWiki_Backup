---
title: Linux CLI와 파일 시스템
created: 2026-07-02
updated: 2026-07-13
type: concept
tags: [linux, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
  - raw/KoreaICT/5. Linux/2026.04.23(목)/2026.04.23(목).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
status: growing
confidence: high
---

# Linux CLI와 파일 시스템

## 정의

Linux CLI(Command Line Interface)는 마우스 대신 명령어로 서버를 조작하는 환경이고, 파일 시스템은 `/`를 뿌리로 하는 디렉터리/파일 계층 구조다.

## 왜 중요한가

서버에는 IntelliJ나 Explorer 같은 GUI가 없거나 제한적인 경우가 많다. Spring Boot jar, Dockerfile, nginx 설정, 로그 파일을 확인하려면 CLI에서 경로를 이동하고 파일을 읽고 수정할 수 있어야 한다.

## 핵심 설명

- `/`: Linux 파일 시스템의 최상위 경로.
- `~`: 현재 사용자의 홈 디렉터리.
- 절대경로: `/home/broadcast/...`처럼 `/`에서 시작.
- 상대경로: 현재 위치를 기준으로 이동.
- `pwd`: 현재 위치 확인.
- `cd`: 디렉터리 이동.
- `ls -al`: 숨김 파일 포함 상세 목록.
- `cat`, `head`, `tail`: 파일 내용 확인.
- `mkdir`, `touch`, `cp`, `mv`, `rm`: 생성·복사·이동·삭제.
- `find`: 조건에 맞는 파일 검색.
- `vi`: 서버 안에서 파일을 직접 수정하는 편집기.

## 예시

```bash
pwd
cd /home/broadcast
mkdir -p kbs/1night_2days
echo "This is a test" > kbs/1night_2days/hello.txt
cat kbs/1night_2days/hello.txt
ls -al
find . -name "*.txt"
vi index.html
```

## 자주 헷갈리는 점

- `>`는 화면 출력 방향을 파일로 바꾸므로 기존 파일을 덮어쓸 수 있다.
- `rm -rf`는 되돌리기 어렵다. 서버에서 삭제 명령은 항상 경로를 다시 확인해야 한다.
- `vi`는 입력 모드와 명령 모드가 나뉘므로 그냥 타이핑한다고 항상 입력되는 것은 아니다.
- Windows 경로 감각과 달리 Linux는 `/` 기준의 계층 구조와 대소문자 구분을 엄격히 따른다.

## 관련 개념

- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[concepts/linux-package-archive|Linux 패키지·다운로드·압축]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]

## 최신 원본 대조

2026-04-22~23의 VM/SSH 뒤 파일 실습을 기준으로, `tree / -L 1`, `mkdir -p`, `cp`·`mv`·`find`, `vi`, `>`/`>>`가 배포 파일·설정 파일을 CLI에서 다루는 순서임을 명시했다. 특히 `>`는 덮어쓰기, `>>`는 누적이라는 차이를 실제 파일 실습과 연결한다.

## 출처

- `raw/KoreaICT/5. Linux/2026.04.23(목)/2026.04.23(목).md`
