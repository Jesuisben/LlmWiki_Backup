---
title: 2026-04-27 Linux 압축, Java 실행, Git과 웹서버
created: 2026-07-06
updated: 2026-07-16
type: summary
tags: [linux, java, github, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md
status: growing
confidence: high
---

# 2026-04-27 Linux 압축, Java 실행, Git과 웹서버

## 한 줄 요약

다운로드·압축·소유권·alias로 server 파일을 준비한 뒤 JDK/JDBC와 Java 실행을 확인하고, Git remote 흐름과 Apache/Nginx·UFW를 이용한 정적 웹페이지 제공까지 확장했다.

## 왜 이 흐름으로 배웠는가

04-24까지는 로컬 VM의 파일과 권한을 다루었다. 실제 server 작업에서는 외부 artifact를 받아 풀고, 반복 명령을 설정하며, runtime을 설치해 program을 실행하고, source를 remote repository와 주고받고, 마지막에는 network port를 통해 결과를 제공해야 한다. 그래서 이날은 **파일 반입 → 압축·소유권 → 반복 작업 설정 → Java runtime → Git remote → host web server** 순서로 운영 작업의 폭을 넓혔다.

## 교시별 학습 전개

### 1교시: `wget`, `curl`, Windows drag-and-drop과 `tar`

동일한 Vim source archive를 세 방식으로 Linux에 가져왔다.

1. `wget`은 URL의 파일명을 유지해 download했다.
2. `curl -L -o`는 redirect를 따라가며 저장할 파일명을 직접 지정했다.
3. Windows에서 MobaXterm drag-and-drop으로 VM home에 파일을 복사했다.

각 방식 뒤 `ls`로 archive가 생겼는지 확인하고 `tar -xzvf`로 풀어 source directory와 내부 파일 목록을 확인했다. `wget`과 `curl`은 Java 자체를 설치하는 명령이 아니라 **원격 파일을 가져오는 도구**라는 경계를 잡았다.

Windows 반입 실습에서는 `sudo mkdir`로 만든 directory가 root 소유라 일반 사용자 drag-and-drop이 실패했다. `ls -al`로 root owner를 확인하고 `chown -R`로 일반 사용자에게 넘긴 뒤 복사가 가능해졌다. 전날 배운 ownership이 실제 file transfer 오류 해결로 이어진 사례다. ^[raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md]

### 2교시: zip archive 이동과 위험한 삭제

`zip` package를 설치하고 전날 만든 방송사 directory의 두 program folder를 각각 `zip -r`로 압축해 다른 directory로 이동했다. 중간에는 owner와 directory 접근 권한을 조정해야 했다.

download test artifact를 정리하면서 일반 파일은 `rm`, directory tree는 `rm -rf`로 삭제했다. `-r`은 하위 항목까지 재귀 처리하고 `-f`는 확인을 줄이므로, 경로를 잘못 쓰면 복구하기 어려운 명령이라는 주의가 필요하다.

### 2~3교시: session 한정 alias와 지속 설정

Java keyword 파일의 앞 3줄·뒤 5줄을 보여 주는 긴 명령을 alias로 만들고 실행했다. 현재 session에서는 동작했지만 MobaXterm을 끊고 다시 접속하자 사라졌다.

다음으로 alias들을 `alias_test.sh`에 적고 `source`로 현재 shell에 반영했다. 이것도 새 session에서는 자동 적용되지 않았기 때문에 `.bashrc`에 같은 내용을 직접 넣거나 script 내용을 append했다. 재접속 후 alias가 동작하면서 **script에 저장하는 것**과 **shell 시작 시 자동으로 읽히게 하는 것**의 차이를 확인했다.

### 3교시 후반: JDK·JDBC와 Java compile/run

Java 실습은 다음 순서로 진행했다.

1. package index를 update했다.
2. Spring Boot version을 고려해 OpenJDK 17을 설치했다.
3. `java -version`으로 runtime 정보를 확인했다.
4. MySQL JDBC driver JAR을 download했다.
5. 한 줄을 출력하는 `JavaTest.java`를 준비했다.
6. 현재 directory와 JDBC JAR을 classpath에 넣어 `javac`로 compile했다.
7. 같은 classpath로 `java`를 실행해 한국어 test message 출력을 확인했다.

JDBC import는 source에서 comment 상태였고, 실제 program은 DB 연결이 아니라 간단한 출력만 수행했다. 따라서 driver를 내려받고 classpath에 포함한 사실과 JDBC 연결 성공을 같은 결과로 쓰지 않는다.

### 4~5교시: Git의 local/remote 흐름

WorkTree → stage → local repository → remote repository의 이동을 설명하고, Windows의 Git Bash에서 여러 sample repository를 준비했다.

- author name/email을 global config로 설정했다.
- `git init`으로 local repository를 만들었다.
- GitHub remote를 `origin`이라는 이름으로 연결했다.
- `git add`로 stage하고 `git commit`으로 local history를 만들었다.
- `git push -u origin master`로 최초 upstream을 정해 remote에 올리고 GitHub 화면에서 확인했다.
- `git remote -v`와 remote 제거, 최초 push 뒤 단축 명령도 보조로 확인했다.

실제 계정명·email·repository URL은 Summary에 재노출하지 않는다. 이 구간은 Linux VM의 Git server 운영이 아니라 **Linux 과목 안에서 수행한 Git Bash/GitHub remote 입문**이며, 05-04~05-06 협업 수업의 선행이다.

### 6교시: Apache service, UFW, 정적 page 교체

Apache 실습은 package update·설치, 부팅 자동 시작, service start/status, UFW, reboot, browser 확인 순서였다.

- `systemctl status apache2`에서 active 상태를 확인했다.
- UFW를 활성화하고 SSH 22, HTTP 80, HTTPS 443의 inbound rule을 허용했다.
- reboot 뒤 SSH와 Apache service가 다시 active인지 확인했다.
- browser에서 guest IP로 Apache 기본 page를 확인했다.
- Windows에서 가져온 homepage archive를 풀고 `/var/www/html/`의 기본 `index.html`을 backup한 뒤 새 파일로 교체했다.
- Apache를 stop/start했을 때 접속 실패·성공이 바뀌는 것을 browser에서 확인하고 다음 실습을 위해 중지했다.

### 7교시: Nginx와 GitHub clone

Apache를 중지한 뒤 Nginx를 설치·시작·상태 확인했다. GitHub sample repository를 clone해 실제 `index.html`이 있는 directory로 이동하고 `/var/www/html/`에 복사한 뒤 guest IP로 browser 결과를 확인했다.

Apache와 Nginx가 같은 document root를 사용한 수업 구성이라도 둘을 동시에 80번 port에 띄우는 실습은 아니었다. service를 전환하면서 한 host의 HTTP server 역할을 비교했다.

### 8교시: Librarian 복습

마지막 교시는 Librarian 교안의 지정 page 실습으로 기록되어 있다. 날짜 노트에 세부 명령·결과가 없으므로 별도 성공 결과를 만들지 않는다.

## 대표 실습: 정적 homepage를 Apache로 제공

**입력**은 Windows에서 가져온 homepage archive, Apache package, guest IP와 UFW rule이었다. **처리**는 archive 해제 → Apache 설치·service 시작 → 80번 허용 → 기본 document backup → `/var/www/html/`에 새 파일 복사 → service 상태 확인 순서였다. **결과**로 browser에서 Apache 기본 page 대신 새 homepage가 보였고, service stop/start에 따라 접속 가능 여부가 달라지는 것을 확인했다.

## 대표 artifact와 확인 결과

- `wget`·`curl`로 받은 tar archive와 해제된 source directory
- Windows drag-and-drop 실패와 `chown` 후 성공
- 방송사 directory의 zip archive
- `alias_test.sh`와 `.bashrc`의 지속 alias
- OpenJDK 17, JDBC driver JAR, `JavaTest.class`, test 출력
- local Git repository와 GitHub remote push 결과
- Apache/Nginx service, UFW 22·80·443 rule, `/var/www/html/`의 교체 page

## 헷갈리기 쉬운 지점

1. **download와 install은 다르다.** `wget`·`curl`은 file transfer이고, `apt install`은 OS package 설치다.
2. **archive 생성·해제와 file 이동은 별도 작업이다.** `tar`/`zip` 결과를 `ls`로 확인한 뒤 `mv`한다.
3. **alias를 script에 적는 것만으로 새 shell에 자동 적용되지는 않는다.** `source`는 현재 shell, `.bashrc`는 새 Bash session 시작과 연결된다.
4. **JDK 설치·JDBC JAR 준비·DB 연결은 서로 다른 완료 단계다.** 이날 확인한 실행 결과는 단순 Java 출력이다.
5. **Git Bash 작업과 Linux VM server 작업을 같은 환경으로 합치지 않는다.** Git remote 흐름은 후속 협업 학습의 선행이다.
6. **Apache/Nginx의 설치·service 상태·firewall·document는 서로 다른 확인점이다.** browser 실패 시 port만 보지 말고 service와 file 위치도 확인한다.

## 이전·다음 수업 연결

- 이전: [[summaries/2026-04-24-linux-users-permissions|04-24]]의 owner·group·permission을 download directory와 archive 이동 오류에 적용했다.
- 다음: [[summaries/2026-04-28-maven-spring-boot-docker-intro|04-28]]에는 단일 Java class를 넘어 GitHub의 Spring Boot project를 Maven JAR로 package하고, host service에서 Docker container로 실행 단위를 바꾼다.
- 후속 활용: Apache/Nginx·UFW·Java 실행은 EC2 배포의 선행이고 Git push는 CI/CD trigger의 선행이다. 이날은 AWS cloud resource나 GitHub Actions workflow를 만들지 않았다.

## 관련 페이지

- [[concepts/linux-package-archive|Linux 패키지·다운로드·압축]]
- [[concepts/linux-web-server-apache-nginx|Linux Apache/Nginx 웹서버]]
- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[entities/java|Java]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[entities/linux|Linux]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md` — 실제 교시·download/archive·permission·alias·Java·Git·web server 흐름의 최우선 근거