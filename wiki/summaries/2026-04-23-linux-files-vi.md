---
title: 2026-04-23 Linux 파일·디렉터리와 vi 편집기
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [linux, curriculum, study-log]
sources:
  - raw/Study/5. Linux/2026.04.23(목)/2026.04.23(목).md
  - raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf
  - raw/Study/5. Linux/교육 자료/Linux/Linux 이론.pdf
  - raw/Study/5. Linux/교육 자료/Linux/Linux 실습(Librarian).pdf
status: growing
confidence: high
---

# 2026-04-23 Linux 파일·디렉터리와 vi 편집기

## 한 줄 요약

`tree`, `mkdir`, `touch`, `echo`, `cat`, `cp`, `mv`, `find`, `vi`, redirection, `grep`, `more`, `diff`로 Linux 파일 시스템을 실제로 만들고 수정하고 비교한 날이다.

## 배운 내용

- `tree / -L 1`로 `/` 아래 최상위 디렉터리 구조를 확인했다.
- `broadcast` 홈 아래에 `kbs`, `mbc`, `sbs`와 방송 프로그램 이름의 하위 디렉터리 구조를 만들었다.
- `echo "..." > file.txt`로 파일을 만들고, `cat`으로 내용을 확인했다.
- `touch`로 빈 파일을 만들고, `ls -l`, `ls -al`, `ls -lR`로 목록을 확인했다.
- `mkdir -p`로 존재하지 않는 상위 디렉터리까지 한 번에 만들었다.
- `cp`, `mv`로 복사·이동·이름 변경을 실습했다.
- `find`에 `-name`, `-iname`, `-type`, `-size`, `-mtime`, `-executable`을 붙여 파일을 찾았다.
- `vi`의 명령 모드, 입력 모드, 실행 모드를 구분하고 `:wq`, `:q!`, `dd`, `yy`, `p`, `u`, `:%s/old/new/g`를 실습했다.
- `>`, `>>`, `head`, `tail`, `grep`, `more`, `diff`로 파일 내용 흐름을 다뤘다.

## 핵심 실습 / 예제

```bash
sudo apt install -y tree
tree / -L 1
mkdir -p /home/broadcast/sbs/morning_wide
echo "This is a test" > kbs/1night_2days/hello.txt
cat kbs/1night_2days/hello.txt
cp sbs/man_in_blackbox/* kbs/morning_garden/
mv sbs/man_in_blackbox/todolist.txt sbs/man_in_blackbox/abandon.txt
find /home/broadcast -iname "WORLD.TXT"
vi total.txt
grep -iwn "break" total.txt
diff java.txt java.doc
```

## 왜 중요한가

서버에서는 GUI 탐색기보다 CLI로 파일을 만들고, 설정을 고치고, 로그나 차이를 확인하는 일이 많다. 이 날의 명령어들은 이후 Apache/Nginx 설정, Dockerfile 작성, Git 충돌 확인의 기초가 된다.

## 헷갈린 점 / 질문

- `>`는 덮어쓰기, `>>`는 뒤에 누적이다.
- `mv`는 이동뿐 아니라 같은 디렉터리 안에서 이름 변경에도 쓰인다.
- `find /home/broadcast -name "k*.txt"`처럼 와일드카드를 쓸 때는 검색 대상과 패턴의 차이를 구분해야 한다.
- `vi`에서 글자를 입력하려면 먼저 `i`, `a`, `o` 등으로 입력 모드에 들어가야 한다.
- `grep -w`는 단어 단위 검색이라 `break`와 `breaking`을 구분할 수 있다.

## 관련 페이지

- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]
- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[concepts/linux-package-archive|Linux 패키지·다운로드·압축]]

## 출처

- `raw/Study/5. Linux/2026.04.23(목)/2026.04.23(목).md`
- `raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf` — p.92~127 파일/디렉터리, vi, redirection, find 실습
- `raw/Study/5. Linux/교육 자료/Linux/Linux 이론.pdf` — vi, 파일 시스템, shell 개념
- `raw/Study/5. Linux/교육 자료/Linux/Linux 실습(Librarian).pdf`
