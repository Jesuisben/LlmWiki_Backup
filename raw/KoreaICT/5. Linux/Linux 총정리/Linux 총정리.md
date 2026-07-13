Linux 총정리 (2026.04.22(수) ~ 2026.05.06(수))

#### \# Linux 과목의 전체 흐름
Linux 과목은 Ubuntu 가상 머신을 만들고 SSH로 접속하는 것에서 시작했다. 이후 파일·디렉토리·vi 편집기, 사용자·그룹·권한, 다운로드·압축·Java 실행 환경을 다루고, Apache/Nginx와 Spring Boot 서버 실행으로 서버 운영의 기초를 연결했다.

그 다음에는 Docker image와 container, network, bind mount/volume, Dockerfile, Docker Compose를 이용해 애플리케이션 실행 환경을 재현하는 방법을 배웠다. 마지막에는 Git/GitHub의 branch, Pull Request, merge, conflict 해결을 통해 여러 사람이 같은 프로젝트를 관리하는 협업 흐름으로 마무리했다.


#### \# Linux와 서버 환경
- Linux는 서버에서 많이 사용하는 운영체제(OS)다.
- Windows에서 VirtualBox로 Ubuntu 가상 머신(VM)을 만들고, MobaXterm으로 원격 접속하는 흐름을 실습했다.
- VM은 한 대의 실제 컴퓨터 안에서 별도의 컴퓨터처럼 동작하는 가상 환경이다.
- SSH(Secure Shell)는 네트워크를 통해 다른 컴퓨터의 터미널에 안전하게 접속하는 프로토콜이다.
- 브리지(Bridged) 네트워크를 사용하면 VM도 같은 네트워크에서 별도 IP 주소를 받아 다른 컴퓨터에서 접속할 수 있다.

문법 : SSH 서버 설치·시작·상태 확인
```shell
sudo apt install openssh-server
sudo systemctl start ssh
sudo systemctl status ssh
```

- `apt`는 Ubuntu/Debian 계열에서 프로그램을 설치·업데이트·삭제하는 패키지 관리 도구다.
- `sudo`는 현재 명령을 관리자 권한으로 실행한다.
- `systemctl`은 systemd 서비스의 시작·중지·상태 확인을 담당한다.
- SSH의 기본 포트는 22번이므로 UFW 방화벽에서도 해당 포트를 허용해야 외부 접속이 가능하다.

```shell
sudo ufw allow 22
```

- `ip a`로 네트워크 인터페이스와 IP 주소를 확인할 수 있다.
- 작업을 끝낼 때는 서버를 갑자기 종료하지 말고 정상 종료 명령을 사용한다.

```shell
sudo poweroff
```


#### \# Linux Prompt 구조
터미널의 Prompt는 현재 명령을 입력할 준비가 되었다는 표시다.

```text
사용자명@호스트명:현재경로$
```

- 일반 사용자는 보통 `$`로 표시된다.
- root 관리자 계정은 보통 `#`로 표시된다.
- `~`는 현재 사용자의 홈 디렉토리(home directory)를 의미한다.
- Prompt를 읽으면 누구로 로그인했는지, 어느 서버인지, 어느 경로에서 작업하는지 파악할 수 있다.


#### \# 파일 시스템과 디렉토리 구조
Linux 파일 시스템은 `/`(root directory)에서 시작하는 하나의 트리 구조다.

- `/` : 최상위 root 디렉토리
- `/home` : 일반 사용자 홈 디렉토리
- `/etc` : 시스템 설정 파일
- `/var` : 로그, 웹 서버 데이터처럼 변하는 데이터
- `/usr` : 프로그램과 라이브러리
- `/bin`, `/sbin` : 기본 실행 명령어
- `/tmp` : 임시 파일

- 디렉토리는 파일을 담는 폴더 역할을 한다.
- 파일 경로는 절대 경로(absolute path)와 상대 경로(relative path)로 나뉜다.

절대 경로 : `/`부터 시작하는 전체 위치
```shell
cd /home/broadcast/kbs
```

상대 경로 : 현재 위치를 기준으로 이동하는 경로
```shell
cd kbs
cd ..
cd ~
```

- `.`은 현재 디렉토리다.
- `..`은 상위 디렉토리다.
- `~`는 로그인한 사용자의 홈 디렉토리다.
- 경로를 먼저 이해해야 `cp`, `mv`, `rm` 같은 명령어가 어느 파일을 대상으로 하는지 안전하게 판단할 수 있다.


#### \# 파일과 디렉토리 확인
현재 위치와 목록을 확인하는 명령어부터 익힌다.

```shell
pwd
ls
ls -al
tree
```

- `pwd` : 현재 작업 경로를 출력한다.
- `ls` : 현재 경로의 파일과 디렉토리 목록을 본다.
- `ls -al` : 숨김 파일까지 긴 형식(long format)으로 본다.
- `tree` : 디렉토리 구조를 트리 형태로 출력한다.

`tree`가 설치되어 있지 않다면 다음처럼 설치한다.

```shell
sudo apt install -y tree
```

`ls -l` 결과의 대표적인 형태는 다음과 같다.

```text
-rw-r--r-- 1 broadcast broadcast 80 Apr 23 03:40 java.txt
```

앞의 권한 문자열은 파일 종류와 권한을 뜻한다.

```text
- rw- r-- r--
│ │   │   └─ others 권한
│ │   └──── group 권한
│ └──────── owner 권한
└────────── 파일 종류
```

- 첫 글자 `-`는 일반 파일, `d`는 디렉토리다.
- `r`은 읽기(read), `w`는 쓰기(write), `x`는 실행(execute) 권한이다.


#### \# 파일과 디렉토리 만들기
- `mkdir`은 디렉토리를 만든다.
- `mkdir -p`는 중간 디렉토리가 없어도 부모 경로까지 함께 만든다.
- `touch`는 빈 파일을 만들거나 파일의 수정 시간을 갱신한다.

```shell
mkdir GitTest
mkdir -p /home/broadcast/sbs/morning_wide
touch mbc/infinite_challenge/everyone.txt
```

파일에 내용을 쓰는 대표적인 방법은 `echo`와 redirection이다.

```shell
echo "Hello, World!"
echo "I will be back" > kbs/1night_2days/world.txt
```

- `>`는 출력 결과를 파일에 새로 쓴다. 기존 내용이 있으면 덮어쓴다.
- `>>`는 기존 파일의 끝에 내용을 추가한다.
- redirection은 명령의 화면 출력 방향을 파일로 바꾸는 기능이다.

```shell
echo "첫 번째 줄" > memo.txt
echo "두 번째 줄" >> memo.txt
cat memo.txt
```

- `cat`은 파일 내용을 출력한다.
- 중요한 파일에 `>`를 사용할 때는 기존 내용을 지울 수 있으므로 경로와 목적을 다시 확인한다.


#### \# 복사, 이동, 삭제, 검색
```shell
cp source.txt backup.txt
cp -r source_dir backup_dir
mv oldname.txt newname.txt
rm file.txt
rm -r directory
find /home -name "*.txt"
```

- `cp`는 파일 또는 디렉토리를 복사한다.
- `cp -r`은 디렉토리 내부까지 재귀적으로 복사한다.
- `mv`는 파일을 이동하거나 이름을 바꾼다.
- `rm`은 파일을 삭제한다.
- `rm -r`은 디렉토리와 내부를 삭제한다.
- `find`는 조건에 맞는 파일·디렉토리를 찾는다.

\* `rm -rf`는 경로를 잘못 입력하면 많은 파일을 되돌리기 어렵게 삭제할 수 있으므로, 먼저 `pwd`, `ls`, 대상 경로를 확인한 후 사용해야 한다. \*


#### \# vi 편집기
`vi`는 터미널에서 파일을 작성·수정하는 편집기다. GUI가 없는 서버에서도 설정 파일을 고칠 수 있어 중요하다.

```shell
vi memo.txt
```

vi의 핵심은 명령 모드(command mode)와 입력 모드(insert mode)를 구분하는 것이다.

- `i` : 현재 위치에서 입력 모드로 전환
- `a` : 현재 문자 뒤에서 입력 모드로 전환
- `Esc` : 명령 모드로 복귀
- `:w` : 저장
- `:q` : 종료
- `:wq` : 저장 후 종료
- `:q!` : 저장하지 않고 강제 종료
- `/문자열` : 문자열 검색

- vi에서 입력한 뒤 바로 종료되지 않는 이유는 입력 모드와 명령 모드가 나뉘어 있기 때문이다.
- 설정 파일을 수정할 때는 저장 전후에 `cat`, `grep`, 서비스 상태 확인으로 결과를 검증하는 습관이 필요하다.


#### \# 사용자와 그룹
Linux는 여러 사용자가 하나의 서버를 공유할 수 있으므로 사용자(user), 그룹(group), 소유자(owner), 권한(permission)을 구분한다.

- 사용자 : 서버에 로그인하거나 프로세스를 실행하는 주체
- 그룹 : 여러 사용자에게 공통 권한을 부여하기 위한 묶음
- owner : 파일 또는 디렉토리를 소유한 사용자
- group : 해당 파일에 연결된 그룹
- root : 시스템 전체를 관리할 수 있는 최고 관리자 계정

계정 정보는 대표적으로 다음 파일에서 확인한다.

```text
/etc/passwd : 사용자 기본 정보
/etc/shadow : 암호화된 비밀번호 정보와 계정 보안 정보
/etc/group : 그룹 정보
```

사용자를 생성할 때는 홈 디렉토리, UID, 기본 shell 등의 옵션을 정할 수 있다.

```shell
useradd -m -d /home/sunnyday -u 7000 -s /bin/bash sunnyday
tail /etc/passwd | grep sunnyday
tail /etc/group | grep sunnyday
```

- `-m` : 홈 디렉토리를 함께 만든다.
- `-d` : 홈 디렉토리 경로를 지정한다.
- `-u` : UID를 지정한다.
- `-s` : 로그인 shell을 지정한다.
- `grep`은 출력에서 특정 문자열이 포함된 행만 찾는다.

그룹을 생성하거나 삭제할 때는 `groupadd`, `groupdel`을 사용한다. 사용자의 기본 그룹과 보조 그룹을 구분해 업무 단위 권한을 설계해야 한다.


#### \# 권한과 소유권
권한은 owner, group, others 세 주체에 대해 각각 읽기·쓰기·실행을 부여한다.

```text
r = read    = 4
w = write   = 2
x = execute = 1
```

권한을 숫자로 표현할 때는 각 권한 값을 더한다.

```text
7 = rwx
6 = rw-
5 = r-x
4 = r--
```

```shell
chmod 755 script.sh
chmod u+x script.sh
chmod g-w report.txt
```

- `chmod 755`는 owner에게 `rwx`, group과 others에게 `r-x`를 부여한다.
- 기호 모드에서는 `u`(owner), `g`(group), `o`(others), `a`(all)를 사용한다.

소유자와 그룹을 바꾸는 명령어는 다음과 같다.

```shell
chown user file.txt
chown user:group file.txt
chgrp group file.txt
```

- `chmod`는 권한을 변경한다.
- `chown`은 owner 또는 owner와 group을 변경한다.
- `chgrp`은 group만 변경한다.
- 세 명령어의 역할을 섞어 외우지 않는 것이 중요하다.

프로세스 상태를 확인하고 종료할 때는 `ps`, `grep`, `kill`을 사용한다. 서버를 중지하기 전에는 어떤 사용자의 어떤 프로세스인지 먼저 확인해야 한다.


#### \# 다운로드, 압축, alias
서버에서는 설치 파일이나 소스 파일을 다운로드하고 압축을 풀어 사용하는 일이 많다.

```shell
wget https://github.com/vim/vim/archive/refs/tags/v9.1.0000.tar.gz
tar -xzvf v9.1.0000.tar.gz
```

```shell
curl -L -o vim.tar.gz https://github.com/vim/vim/archive/refs/tags/v9.1.0000.tar.gz
tar -xzvf vim.tar.gz
```

- `wget`은 URL에서 파일을 내려받는다.
- `curl -L`은 redirect를 따라가며, `-o`로 결과 파일명을 정할 수 있다.
- `tar -x`는 압축 해제, `-z`는 gzip 처리, `-v`는 처리 과정을 출력, `-f`는 파일명을 지정한다.
- `zip`, `unzip`도 파일 묶음 압축·해제에 사용한다.

alias는 긴 명령어에 짧은 별칭을 붙이는 기능이다.

```shell
alias ll='ls -al'
alias
unalias ll
```

- 현재 shell에서 만든 alias는 접속을 종료하면 사라질 수 있다.
- 자주 쓰는 alias는 shell 설정 파일이나 별도 `.sh` 파일에 정리해 다시 읽어오도록 관리할 수 있다.


#### \# Linux에서 Java 실행 준비
Linux 서버에서 Java 프로그램이나 Spring Boot를 실행하려면 JDK가 필요하다.

```shell
sudo apt install default-jdk
java -version
javac -version
```

- JDK(Java Development Kit)는 Java 컴파일러와 실행 환경을 포함한다.
- `java`는 컴파일된 프로그램을 실행하고, `javac`는 `.java` 파일을 컴파일한다.
- Windows IDE에서만 실행하던 Java 프로그램을 Linux에서도 실행해 보면서 개발 환경과 운영 환경의 연결을 확인했다.


#### \# 웹 서버: Apache와 Nginx
웹 서버는 브라우저의 HTTP 요청을 받아 정적 파일을 제공하거나, 애플리케이션 서버 앞에서 요청을 전달하는 역할을 한다.

- Apache HTTP Server와 Nginx는 대표적인 웹 서버다.
- 정적 HTML/CSS/이미지는 웹 서버의 document root에 배치해 제공할 수 있다.
- Spring Boot는 내장 서버로 직접 실행할 수 있고, Nginx를 앞단에 두면 80/443 포트 요청을 Spring Boot 포트로 전달할 수 있다.

서비스를 중지하고 자동 시작을 해제하는 예시는 다음과 같다.

```shell
sudo systemctl stop nginx
sudo systemctl disable nginx
sudo systemctl stop apache2
sudo systemctl disable apache2
```

방화벽은 서비스가 사용하는 포트를 명시적으로 허용해야 한다.

```shell
sudo ufw allow 80/tcp
sudo ufw allow 9000/tcp
```

- 80번 포트는 일반 HTTP의 대표 포트다.
- Spring Boot 애플리케이션 포트는 `application.properties`의 `server.port`로 정할 수 있다.
- 포트가 열려 있어도 서비스가 실행 중인지, 바인딩 주소가 맞는지, 방화벽 규칙이 맞는지를 함께 확인해야 한다.


#### \# Maven과 Spring Boot 서버 실행
Maven은 Java/Spring Boot 프로젝트의 의존성 관리와 빌드를 담당한다.

```shell
sudo apt install -y maven
mvn -v
```

일반적인 Spring Boot 배포 흐름은 다음과 같다.

```shell
mvn package
java -jar target/application.jar
```

- `mvn package`는 소스 코드와 의존성을 빌드해 실행 가능한 jar 파일을 만든다.
- `java -jar`는 만들어진 jar를 Linux 서버에서 실행한다.
- 로컬 개발 환경에서 동작하던 프로그램을 서버에서 실행하려면 JDK, 포트, DB 연결, 방화벽, 로그 위치를 함께 점검해야 한다.

Nginx 또는 iptables를 이용하면 80번 포트 요청을 Spring Boot의 다른 포트로 연결할 수 있다.

```shell
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 9000
sudo iptables -t nat -L -n | grep 9000
```


#### \# Docker의 기본 개념
Docker는 애플리케이션과 실행에 필요한 환경을 image로 만들고, 어디서나 비슷하게 실행하도록 돕는 컨테이너 도구다.

- image : 실행 환경을 담은 읽기 전용 설계도
- container : image를 실제로 실행한 인스턴스
- Docker Hub : image를 올리고 내려받는 registry
- port mapping : 호스트 포트와 컨테이너 포트를 연결하는 설정
- environment variable : 컨테이너 실행 시 전달하는 설정값

Docker를 설치한 후에는 daemon과 권한을 확인해야 한다. 일반 사용자가 `docker` 명령을 사용하도록 그룹을 설정한 경우에는 로그아웃 후 다시 로그인해야 적용될 수 있다.

기본적인 image와 container 확인 명령어는 다음과 같다.

```shell
docker image ls
docker container ps
docker container ps -a
docker network ls
docker volume ls
```

컨테이너 생성·시작·중지·삭제 흐름은 다음과 같다.

```shell
docker container run --name web-ctr -d -p 8989:80 nginx
docker container stop web-ctr
docker container rm web-ctr
docker image rm nginx
```

- `-d`는 background(detached) 실행이다.
- `-p 8989:80`은 호스트 8989 포트를 컨테이너 80 포트에 연결한다.
- 실행 중인 컨테이너를 삭제하려면 먼저 중지해야 하는 경우가 많다.


#### \# 컨테이너 내부 작업과 파일 복사
컨테이너 안에서 shell을 실행하거나 파일을 확인할 수 있다.

```shell
docker exec -it web-ctr /bin/bash
docker cp index.html web-ctr:/usr/share/nginx/html/index.html
docker cp web-ctr:/usr/share/nginx/html/index.html ./index.html
```

- `docker exec`은 실행 중인 컨테이너 내부에서 명령을 실행한다.
- `-it`는 터미널 입력을 연결해 shell을 직접 사용할 때 쓴다.
- `docker cp`는 host와 container 사이에 파일을 한 번 복사한다.
- 컨테이너 내부에서 수정한 파일은 컨테이너를 삭제하면 사라질 수 있으므로, 지속적으로 보존할 데이터에는 mount 또는 volume을 사용한다.


#### \# Docker network와 DB 컨테이너 연동
여러 컨테이너가 함께 동작할 때는 사용자 정의 network를 만들고 컨테이너 이름으로 서로 통신하도록 구성할 수 있다.

```shell
docker network create network02
docker network ls
```

- 같은 Docker network에 연결된 컨테이너는 컨테이너 이름을 host처럼 사용해 통신할 수 있다.
- MariaDB/MySQL 같은 DB 컨테이너와 Redmine 같은 웹 애플리케이션 컨테이너를 같은 network에 배치해 연동하는 실습을 했다.
- DB root password, 앱 DB 계정, API key처럼 비밀값이 필요한 설정은 명령어·소스 코드에 고정하지 말고 환경 변수, secret 관리 도구, 별도 설정으로 분리해야 한다.

예시 구조 :

```text
브라우저
  ↓
웹 애플리케이션 컨테이너
  ↓ Docker network
MariaDB/MySQL 컨테이너
```


#### \# bind mount와 volume
컨테이너의 데이터 보존 방법은 크게 bind mount와 volume으로 나뉜다.

- bind mount : 호스트의 특정 경로를 컨테이너 경로에 직접 연결한다.
- volume : Docker가 관리하는 저장 공간을 컨테이너에 연결한다.
- `docker cp` : 파일을 한 번 복사할 뿐이며 지속적인 연결 방식은 아니다.

```shell
docker volume create web-data
docker container run -d --name web-ctr -v web-data:/usr/share/nginx/html nginx
```

- DB 데이터처럼 컨테이너가 삭제되어도 보존해야 하는 데이터에는 volume이 적합하다.
- 개발 중 호스트의 소스 파일을 즉시 컨테이너에서 반영하고 싶을 때는 bind mount가 편리하다.
- 어떤 방식이든 host 경로, container 경로, 권한, 삭제 시 데이터가 남는지 여부를 구분해서 이해해야 한다.


#### \# 컨테이너로 image 만들기와 Docker Hub
실행 중인 컨테이너 상태를 image로 저장할 수 있다.

```shell
docker commit web-ctr my-web-image:1.0
docker image ls
```

- `docker commit`은 실습 중 변경된 컨테이너 상태를 빠르게 image로 남길 때 사용할 수 있다.
- 그러나 사람이 어떤 변경을 했는지 재현하기 어렵기 때문에, 반복 가능한 배포에는 Dockerfile을 사용하는 편이 좋다.
- 사용자 정의 image는 Docker Hub 같은 registry에 push해 다른 서버에서도 pull하여 실행할 수 있다.


#### \# Dockerfile
Dockerfile은 image를 만드는 절차를 코드로 적은 파일이다. 같은 Dockerfile을 사용하면 누가 빌드해도 비슷한 실행 환경을 만들 수 있다.

```dockerfile
FROM httpd
COPY index.html /usr/local/apache2/htdocs/index.html
```

```shell
docker build -t pohang-img -f Dockerfile .
docker container run --name pohang-ctr -d -p 8989:80 pohang-img
```

- `FROM`은 기반 image를 정한다.
- `COPY`는 build context의 파일을 image 안으로 복사한다.
- `RUN`은 image를 만드는 과정에서 실행할 명령이다.
- `CMD` 또는 `ENTRYPOINT`는 컨테이너 시작 시 실행할 기본 명령을 정한다.
- `docker build`의 마지막 `.`은 build context다. Dockerfile에서 `COPY`할 수 있는 파일 범위를 뜻한다.

Spring Boot도 jar 파일을 image에 복사하고 `java -jar`로 실행하는 Dockerfile로 컨테이너화할 수 있다.


#### \# Nginx reverse proxy와 로드 밸런싱
Nginx는 브라우저 요청을 여러 Spring Boot 컨테이너로 전달하는 reverse proxy 역할을 할 수 있다.

```nginx
upstream app_servers {
    server app01:9000;
    server app02:9000;
}

server {
    listen 80;

    location / {
        proxy_pass http://app_servers;
    }
}
```

- `upstream`에는 요청을 나눠 받을 backend 서버를 정의한다.
- `proxy_pass`는 들어온 요청을 backend로 전달한다.
- 로드 밸런싱은 한 서버에 요청이 몰리지 않게 여러 서버로 분산하는 방식이다.
- 브라우저를 새로고침했을 때 서로 다른 컨테이너가 번갈아 응답하도록 확인하며 request 흐름을 이해했다.


#### \# Docker Compose
Docker Compose는 여러 컨테이너의 image, port, environment, network, volume을 YAML manifest 한 파일에 선언하는 도구다.

```yaml
services:
  db:
    image: mysql
    volumes:
      - db-data:/var/lib/mysql

  app:
    image: my-spring-app
    depends_on:
      - db
    ports:
      - "9000:9000"

volumes:
  db-data:
```

- `services`에는 실행할 컨테이너 단위를 적는다.
- `depends_on`은 서비스 시작 순서의 의존 관계를 표현한다.
- `volumes`는 Docker volume 정의다.
- Compose는 DB와 Spring Boot처럼 서로 연결된 여러 컨테이너를 반복 가능하게 실행하는 데 유용하다.

```shell
docker compose -p hello -f compose_mysql_springboot.yml up -d
docker compose -p hello -f compose_mysql_springboot.yml down
```

- `up -d`는 manifest에 정의된 서비스와 network, volume을 background로 생성·시작한다.
- `down`은 서비스와 network를 중지·삭제한다. volume 삭제 옵션을 함께 주는 경우 데이터 보존 여부를 먼저 확인해야 한다.


#### \# Git과 GitHub
Git은 파일의 변경 이력을 local repository에 기록하는 분산 버전 관리 시스템이다. GitHub는 Git repository를 원격으로 공유하고 협업하는 서비스다.

- working directory : 현재 작업 중인 파일 공간
- staging area : 다음 commit에 포함할 변경을 고르는 공간
- local repository : 내 컴퓨터의 commit 이력
- remote repository : GitHub 같은 원격 저장소
- commit : 의미 있는 변경 묶음의 저장 기록

새 프로젝트를 Git으로 관리하는 기본 흐름은 다음과 같다.

```shell
mkdir GitTest
cd GitTest
git init
git config user.name "developer"
git config user.email "developer@example.com"
git status
git add .
git commit -m "first commit"
```

- `git init`은 현재 폴더를 Git repository로 만든다.
- `git status`는 변경·staging 상태를 확인하는 가장 중요한 점검 명령이다.
- `git add`는 commit할 변경을 staging area에 올린다.
- `git commit`은 staging된 변경을 local repository에 기록한다.

원격 저장소와 연결한 뒤에는 push와 pull로 변경을 주고받는다.

```shell
git remote add origin 원격저장소주소
git push -u origin main
git pull origin main
git clone 원격저장소주소
```

- `git push`는 local commit을 원격 저장소에 올린다.
- `git pull`은 이미 연결된 원격 저장소의 변경을 내려받고 현재 branch에 반영한다.
- `git clone`은 원격 저장소 전체를 처음 local로 복제한다.
- commit하지 않은 변경은 push할 수 없다는 점을 실습으로 확인했다.


#### \# branch와 Pull Request 협업
여러 사람이 같은 프로젝트를 수정할 때는 각자 branch에서 작업하고 Pull Request(PR)로 변경을 검토·병합한다.

```shell
git branch feature-login
git switch feature-login
git add .
git commit -m "로그인 기능 추가"
git push -u origin feature-login
```

협업 흐름 :

```text
main branch에서 최신 내용 확인
  ↓
작업자별 feature branch 생성
  ↓
코드 수정 → add → commit → push
  ↓
GitHub에서 Pull Request 생성
  ↓
검토 후 main branch에 merge
  ↓
각 작업자가 main branch를 pull하여 최신화
```

- Pull Request는 단순히 merge 버튼을 누르는 기능이 아니라, 변경 내용을 비교·검토하고 팀 합의를 남기는 협업 단위다.
- 두 사람이 같은 파일의 같은 부분을 다르게 수정하면 conflict가 발생할 수 있다.
- conflict가 발생하면 어느 변경을 유지할지 직접 결정하고, conflict marker를 제거한 뒤 다시 add·commit·push한다.
- SourceTree는 Git 명령을 GUI로 보여 주는 도구지만, 내부 개념은 Git Bash 명령과 같다.


#### \# 자주 헷갈리는 구분
- `sudo` : 관리자 권한으로 명령을 실행하는 접두어다. root 계정으로 계속 작업하는 것과는 다르다.
- 절대 경로 : `/`부터 시작한다. 상대 경로 : 현재 경로를 기준으로 한다.
- `>` : 파일 내용을 새로 쓴다. `>>` : 기존 내용 뒤에 추가한다.
- `chmod` : 권한 변경, `chown` : 소유자 변경, `chgrp` : 그룹 변경이다.
- image : 실행 전 설계도, container : image로 실행한 실제 단위다.
- `docker cp` : 일회성 복사, bind mount : 호스트 경로 직접 연결, volume : Docker 관리 저장 공간이다.
- `docker commit` : 실행 중 컨테이너 상태를 image로 저장, Dockerfile : image 생성 절차를 파일로 관리한다.
- Dockerfile : image 하나를 만드는 recipe, Docker Compose : 여러 서비스를 함께 실행하는 manifest다.
- `git clone` : 원격 저장소를 처음 복제, `git pull` : 이미 연결된 저장소의 최신 변경을 가져와 반영한다.
- `git fetch` : 원격 변경을 내려받기만 하고 현재 branch에 자동 병합하지 않는다.


#### \# 복습 순서
1) Ubuntu VM 설치, 브리지 네트워크, SSH/MobaXterm 접속 흐름을 먼저 직접 해본다.
2) `pwd`, `cd`, `ls`, `mkdir`, `touch`, `cp`, `mv`, `rm`, `find`, redirection, vi를 작은 디렉토리에서 반복한다.
3) `ls -l`의 owner/group/others 권한을 읽고, `chmod`·`chown`·`chgrp`의 역할을 구분한다.
4) `wget`/`curl`, `tar`, alias, JDK 설치로 서버에 필요한 프로그램과 파일을 준비하는 흐름을 복습한다.
5) Maven으로 jar를 만들고 Linux에서 Spring Boot를 실행하며 포트·방화벽·웹 서버 관계를 확인한다.
6) Docker image/container, port mapping, network, mount를 분리해서 실습한다.
7) Dockerfile과 Docker Compose로 같은 서버 환경을 반복 가능하게 만드는 이유를 정리한다.
8) Git에서 status → add → commit → push → pull의 기본 흐름을 익힌 뒤 branch → PR → merge → conflict 해결 순서로 협업을 복습한다.
