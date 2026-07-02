---
title: Linux CLI와 파일 시스템
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [linux]
sources:
  - raw/Study/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
  - raw/Study/5. Linux/2026.04.23(목)/2026.04.23(목).md
  - raw/Study/5. Linux/교육 자료/Linux/Linux 이론.pdf
  - raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf
status: growing
confidence: high
---

# Linux CLI와 파일 시스템

## 정의

Linux CLI(Command Line Interface)는 명령어로 운영체제를 조작하는 방식이고, 파일 시스템은 `/` 루트에서 시작해 `/home`, `/etc`, `/var`, `/usr` 같은 디렉터리로 뻗어 나가는 계층 구조다.

## 왜 중요한가

Spring Boot나 Docker를 서버에서 실행할 때는 IDE나 Windows 탐색기보다 터미널에서 파일을 만들고, 권한을 보고, 설정을 수정하고, 로그를 확인하는 일이 많다. CLI와 파일 시스템은 Linux 배포 작업의 기본 언어다.

## 수업에서 등장한 흐름

1. VirtualBox Ubuntu VM에 SSH로 접속했다.
2. `사용자@호스트:현재경로$` prompt를 읽었다.
3. `/home/broadcast` 아래 방송사/프로그램 이름의 디렉터리 트리를 만들었다.
4. `echo`, `touch`, `cat`으로 파일을 만들고 확인했다.
5. `cp`, `mv`, `find`로 파일을 복사·이동·검색했다.
6. `vi`, `grep`, `more`, `diff`로 서버 안의 텍스트를 편집·검색·비교했다.

## 핵심 명령어

```bash
pwd
cd /home/broadcast
cd ..
ls -al
tree / -L 1
mkdir -p sbs/morning_wide
echo "This is a test" > kbs/1night_2days/hello.txt
echo "append" >> total.txt
touch mbc/infinite_challenge/everyone.txt
cat total.txt
cp source.txt target.txt
mv old.txt new.txt
find /home/broadcast -iname "WORLD.TXT"
grep -iwn "break" total.txt
more -n 10 total.txt
diff java.txt java.doc
vi total.txt
```

## 경로 감각

- 절대 경로: `/home/broadcast/kbs/1night_2days/hello.txt`처럼 `/`에서 시작한다.
- 상대 경로: `kbs/1night_2days/hello.txt`, `./kbs/...`, `../broadcast/...`처럼 현재 위치를 기준으로 해석한다.
- `~`는 현재 사용자의 home directory다.
- `.`은 현재 디렉터리, `..`은 상위 디렉터리다.

## 자주 헷갈리는 점

- `mkdir a/b`는 `a`가 없으면 실패하지만 `mkdir -p a/b`는 중간 디렉터리까지 만든다.
- `>`는 덮어쓰기, `>>`는 누적이다.
- `find`는 파일 이름뿐 아니라 타입·크기·수정 시간·실행 가능 여부로도 찾을 수 있다.
- `vi`는 입력 모드와 명령 모드가 나뉜다. 글 입력은 `i`, 저장 후 종료는 `Esc` → `:wq`다.
- `diff`의 `<`는 왼쪽 파일, `>`는 오른쪽 파일의 차이를 나타낸다.

## 이후 학습과 연결

- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]을 알아야 파일 수정/실행 오류를 해석할 수 있다.
- [[concepts/linux-web-server-apache-nginx|Linux Apache/Nginx 웹서버]]에서는 `/var/www/html/` 같은 서버 문서 경로를 다룬다.
- [[concepts/docker-cp-exec-container-files|Docker exec/cp와 컨테이너 파일 다루기]]도 결국 컨테이너 내부 Linux 파일 시스템을 다루는 것이다.

## 관련 수업

- [[summaries/2026-04-22-linux-install-ssh-cli|2026-04-22 Linux 설치, SSH 접속, 기본 CLI]]
- [[summaries/2026-04-23-linux-files-vi|2026-04-23 Linux 파일·디렉터리와 vi 편집기]]

## 출처

- `raw/Study/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md`
- `raw/Study/5. Linux/2026.04.23(목)/2026.04.23(목).md`
- `raw/Study/5. Linux/교육 자료/Linux/Linux 이론.pdf` — prompt, 절대/상대 경로, 파일 시스템
- `raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf` — p.92~127 파일/디렉터리/vi 실습
