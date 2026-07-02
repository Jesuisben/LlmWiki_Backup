---
title: 2026-04-24 Linux 사용자, 그룹, 권한
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [linux, curriculum, study-log]
sources:
  - raw/Study/5. Linux/2026.04.24(금)/2026.04.24(금).md
  - raw/Study/5. Linux/교육 자료/Linux/Linux 이론.pdf
  - raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf
  - raw/Study/5. Linux/교육 자료/AccessRights.png
  - raw/Study/5. Linux/교육 자료/OwnerShip.png
  - raw/Study/5. Linux/교육 자료/Linux/Linux 실습(Librarian).pdf
status: growing
confidence: high
---

# 2026-04-24 Linux 사용자, 그룹, 권한

## 한 줄 요약

`ls -l`의 권한 문자열을 해석하고, 사용자·그룹 생성과 `/etc/passwd`, `/etc/shadow`, `/etc/group`, `chmod`, `chown`, `chgrp`를 통해 Linux의 다중 사용자 권한 모델을 배웠다.

## 배운 내용

- 모든 파일에는 owner와 group이 있고, 권한은 owner/group/others 세 범주에 적용된다.
- `r`, `w`, `x`는 각각 읽기, 쓰기, 실행 권한이며 숫자로는 4, 2, 1에 대응한다.
- `AccessRights.png`는 `cat file.txt`, `echo "hello" > file.txt`, `./script.sh` 예시로 read/write/execute를 설명한다.
- `OwnerShip.png`는 owner를 집 주인, group을 가족/팀, others를 외부인으로 비유해 `ls -l`의 owner/group 필드를 설명한다.
- `/etc/skel`은 새 사용자 홈 디렉터리에 복사될 기본 템플릿이다.
- `useradd -m`, `passwd`, `useradd -D`, `groupadd`, `usermod -G`로 사용자·그룹을 만들고 확인했다.
- `chmod 644`, `chmod 444`, `chmod 777`, `chmod 700`, `chmod g-x`, `chmod -R a-w`로 권한을 변경했다.
- `chown`, `chgrp`로 파일/디렉터리의 소유자와 그룹을 바꿨다.
- 실행 권한이 없는 `.sh` 파일은 `./script.sh` 실행 시 `Permission denied`가 날 수 있고, `chmod 744` 등으로 실행 권한을 줘야 한다.

## 핵심 실습 / 예제

```bash
sudo su -
cd /etc/skel
echo 'welcome~~my homepage' > index.html
useradd -m skywalker
passwd skywalker
tail /etc/passwd | grep skyw
useradd -m -d /home/sunnyday -u 7000 -s /bin/bash sunnyday
groupadd -g 7777 journalist
usermod -G journalist sunnyday
chmod 644 kbs/1night_2days/hello.txt
chmod 555 /home/broadcast/mbc/infinite_challenge
sudo chown -R broadcast:broadcast ytn
sudo chgrp -R journalist kbs
chmod 744 print_tree.sh
./print_tree.sh
```

## 왜 중요한가

Spring Boot 배포나 Docker volume/mount 실습에서 “파일을 못 씀”, “실행 권한 없음”, “root가 만든 디렉터리에 일반 사용자가 접근 못 함” 같은 오류가 반복된다. Linux 권한 모델을 알아야 서버 운영 오류를 해석할 수 있다.

## 헷갈린 점 / 질문

- 첫 글자 `-`는 파일, `d`는 디렉터리다. 그 뒤 9글자가 owner/group/others의 권한이다.
- `chmod 644`는 owner `rw-`, group `r--`, others `r--`이다.
- `sudo mkdir ytn`처럼 root가 만든 디렉터리는 일반 사용자가 파일을 만들지 못할 수 있다.
- `chown user:group file`은 owner와 group을 함께 바꾸고, `chgrp group file`은 group만 바꾼다.
- `usermod -G`는 보조 그룹 지정이다. 기존 보조 그룹 보존이 필요하면 보통 `-aG`를 함께 쓴다.

## 관련 페이지

- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]
- [[concepts/docker-install-permission-setup|Docker 설치와 권한 설정]]

## 출처

- `raw/Study/5. Linux/2026.04.24(금)/2026.04.24(금).md`
- `raw/Study/5. Linux/교육 자료/Linux/Linux 이론.pdf` — p.34~43 사용자 계정 파일, p.119~124 권한/chmod/chown/chgrp
- `raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf` — p.133~150 사용자·그룹·권한 실습
- `raw/Study/5. Linux/교육 자료/AccessRights.png`
- `raw/Study/5. Linux/교육 자료/OwnerShip.png`
- `raw/Study/5. Linux/교육 자료/Linux/Linux 실습(Librarian).pdf`
