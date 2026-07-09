Linux 총정리

#### \# 전체 흐름
Linux 과목은 VirtualBox와 Ubuntu 설치에서 시작해서 SSH/MobaXterm 접속, 파일/디렉토리 명령어, vi, 사용자·그룹·권한, 압축/다운로드, Spring Boot jar 실행, Docker 이미지·컨테이너·네트워크·볼륨, Dockerfile, Docker Compose, Git/GitHub 협업까지 이어진다.

#### \# 날짜별 핵심
- 2026.04.22(수)
  - 교육 자료 파일 설명
  - Linux 설치에 필요한 파일 설치 (Linux 실습(MobaXterm, VirtualBox, 실습) PDF 이용)
  - VirtualBox 이어서 설정
  - 네트워크 셋팅 - 브릿지 모드 (Linux 실습(MobaXterm, VirtualBox, 실습) PDF (P.65))
  - 해당 IP에 접속하기 위해서 접속 아이콘을 만들기 (MobaXterm을 이용)
- 2026.04.23(목)
  - 트리 형식으로 디렉토리 보기 (Linux 실습(MobaXterm, VirtualBox, 실습).pdf(P.93))
  - 해당 디렉토리 구조를 만들기 (Linux 실습(MobaXterm, VirtualBox, 실습).pdf(P.92))
  - 파일 생성하기 (Linux 실습(MobaXterm, VirtualBox, 실습).pdf(P.103~110))
  - 복사 및 이동 (Linux 실습(MobaXterm, VirtualBox, 실습).pdf(P.114~115))
  - 파일 찾기 (Linux 실습(MobaXterm, VirtualBox, 실습).pdf(P.116~117))
- 2026.04.24(금)
  - ls -l (Line Long)로 나온 코드들 풀이하기
  - 계층 구조 (Linux 이론.pdf(P.135~136))
  - 사용자 계정 관리 - 사용자와 그룹 (Linux 이론.pdf(P.135~136))
  - 사용자와 그룹 생성하기 (Linux 실습(MobaXterm, VirtualBox, 실습).pdf(P.127~))
  - skywalker 사용자 계정 생성하기
- 2026.04.27(월)
  - 리눅스에 Java 설치하는 방법
  - 파일 압축해제(tar 명령어) - wget 명령어 이용 (Linux 실습(MobaXterm, VirtualBox, 실습).pdf(P.153))
  - 파일 압축해제(tar 명령어) - curl 명령어 이용 (Linux 실습(MobaXterm, VirtualBox, 실습).pdf(P.154))
  - 파일 압축해제(tar 명령어) - 윈도우에 다운받기 (Linux 실습(MobaXterm, VirtualBox, 실습).pdf(P.154))
  - 파일 압축 및 이동 (Linux 실습(MobaXterm, VirtualBox, 실습).pdf(P.156))
- 2026.04.28(화)
  - 메이븐 설명 (SpringBoot 교안.pdf(P.22))
  - 웹 서버 설치/구도 - 스프링 부트와의 연동 (Linux 실습(MobaXterm, VirtualBox, 실습).pdf(P.189~194))
  - 도커의 개요 (Docker 교안(이론).pdf(P.23~24))
  - 도커 이미지 생성 (Docker 교안(이론).pdf(P.25))
  - Docker 설치 (Docker 교안(실습).pdf(P.120))
- 2026.04.29(수)
  - 레드 마인 및 MariaDB 컨테이너 생성 및 연동 (Docker 교안(실습).pdf(P.44~49))
  - 실전 활용 컨테이너 사용법 (Docker 교안(실습).pdf(P.51))
  - 실전 활용 컨테이너 사용법 (Docker 교안(실습).pdf(P.52~55))
  - 실전 활용 컨테이너 사용법 (Docker 교안(실습).pdf(P.56~57))
  - 실습 해보기 (Docker 교안(실습).pdf(P.62))
- 2026.04.30(목)
  - 컨테이너로 이미지(도커 이미지) 만들기 (Docker 교안(실습).pdf(P.78~81))
  - 내가 직접 혼자서 실습해보기 (Docker 교안(실습).pdf(P.82))
  - DockerFile 응용 (Docker 교안(실습).pdf(P.84~100))
  - Spring Boot 컨테이너 생성
  - docker exec -it -e LANG=en_US.UTF-8 -e LC_ALL=en_US.UTF-8 mysql-ctr mysql -u gomdori -p --default-character-set=utf8mb4
- 2026.05.01(금)
  - 도커 컴포즈 - 매니페스트 파일 (Docker 교안(이론).pdf(P.85~))
  - 도커 컴포즈 사용하기 (Docker 교안(실습).pdf(P.102))
  - 도커 데스크탑 설치(Docker 교안(이론).pdf(P.1~20))
  - 도커 데스크탑 이용해보기
  - 백엔드 시험
- 2026.05.04(월)
  - 깃 관련 설명 (Github 교안(실습).pdf(P.2~3))
  - Git Bash 이용하기 (Github 교안(실습).pdf(P.11~31))
  - 깃허브에서 파일 생성
  - 원격 저장소에서 로컬 저장소로 Pull하기
  - 커밋하지 않고 Push 시도하기
- 2026.05.06(수)
  - Github 협업 시나리오 - 팀원 (Github 교안(실습).pdf(P.78~93))
  - 인텔리제이 설정
  - 팀원 신규 브랜치 생성 및 커밋과 푸쉬하기 (Github 교안(실습).pdf(P.94~96))
  - Pull Request 실습 (Github 교안(실습).pdf(P.97~108))
  - Pull Request 실습 - 직접 해보기 (Github 교안(실습).pdf(P.109~120))

#### \# 자주 나온 명령어
- apt install git
- sudo apt install openssh-server
- sudo systemctl start ssh
- sudo systemctl status ssh
- sudo poweroff
- sudo ufw allow 22
- sudo apt install -y tree
- cd
- echo "Hello, World!"
- echo "I will be back" > kbs/1night_2days/world.txt
- touch mbc/infinite_challenge/everyone.txt
- touch mbc/infinite_challenge/thankyou.txt
- mkdir /home/broadcast/sbs/morning_wide
- mkdir -p /home/broadcast/sbs/morning_wide
- echo "sbs man in black box file" > sbs/man_in_blackbox/todolist.txt
- echo "some settings be effected" > sbs/man_in_blackbox/settings.txt
- sudo su -
- echo 'welcome~~my homepage' > index.html
- cat index.html (확인용)
- ls -al (확인용)
- cd / (root 디렉토리로 돌아가기)
- useradd -m -d /home/sunnyday -u 7000 -s /bin/bash sunnyday
- tail /etc/passwd | grep sunnyday
- tail /etc/group | grep sunnyday
- ls -al /home/sunnyday
- useradd -m -c shy_guy -e 2025-12-25 -d /home/rainbow7 -u 7500 -s /bin/bash -p $(openssl passwd -6 test1234) rainbow7
- cd ~/downloads/wgettest (이동)
- ls // 파일 없음
- wget https://github.com/vim/vim/archive/refs/tags/v9.1.0000.tar.gz
- tar -xzvf v9.1.0000.tar.gz
- ls
- cd vim-9.1.0000/
- cd ~/downloads/curltest (이동)
- curl -L -o vim.tar.gz https://github.com/vim/vim/archive/refs/tags/v9.1.0000.tar.gz
- sudo systemctl stop nginx # 구동중인 nginx 종료 하기
- sudo systemctl disable nginx # 재부팅시 구동이 안되도록 지정하기
- sudo systemctl stop apache2 # 구동중인 apache2 종료 하기
- sudo systemctl disable apache2 # 재부팅시 구동이 안되도록 지정하기
- cd git_sample_02/
- sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 9000
- sudo iptables -t nat -L -n | grep 9000
- sudo ufw allow 9000/tcp
- sudo apt install -y maven
- mvn -v
- docker network create network02
- docker network ls
- docker run --net=network02 --name=mariadb02 -dit -e MYSQL_ROOT_PASSWORD=My@Sql01 \
- docker run --net=network02 --name=redmine02 -dit -p=8883:3000 -e REDMINE_DB_MYSQL=mariadb02 \
- docker container ls -a
- docker container stop mariadb02 redmine02
- docker container rm mariadb02 redmine02
- docker image rm mariadb redmine
- mv dk04.docker_실습_파일.zip docker_test.zip
- mkdir docker
- cd ~/docker/dockerfile
- docker build -t pohang-img -f ~/docker/dockerfile/Dockerfile01 .
- docker image ls
- docker container ps -a
- docker container run --name pohang-ctr -d -p 8989:80 pohang-img
- ip a show enp0s3
- docker container stop commit-ctr pohang-ctr
- docker container rm commit-ctr pohang-ctr
- docker image rm pohang-img
- docker image 			nginx
- docker container run
- cd D:\docker\shopping_03_mini_database
- docker build -t myspring-img -f Dockerfile01 .
- docker compose -p hello -f ~/docker/compose01/compose_mysql_springboot.yml up -d
- docker container ps -a --format "table {{.Names}}\t{{.Status}}"
- mysql-ctr 	Up About a minute
- docker exec -it mysql-ctr /bin/bash
- mkdir GitTest
- cd GitTest
- mkdir bluerain
- cd bluerain
- git init
- ls -al로 확인해보기
- git status
- git config user.name "bluesky"
- git config user.email "bluesky@naver.com"

#### \# 헷갈리기 쉬운 구분
- `sudo`는 관리자 권한으로 명령을 실행할 때 사용한다. 설명 문장과 실제 명령어를 구분해서 봐야 한다.
- `chmod`는 권한 숫자/문자 변경, `chown`은 소유자/그룹 변경이다.
- Docker image는 실행 전 설계도이고, container는 image로 만든 실행 단위이다.
- `docker commit`은 실행 중인 컨테이너 상태를 이미지로 저장하는 방식이고, Dockerfile은 이미지 생성 절차를 파일로 남기는 방식이다.
- bind mount는 호스트 폴더를 직접 연결하고, volume은 Docker가 관리하는 저장 공간을 연결한다.
- `git clone`은 원격 저장소 전체를 처음 가져오는 것, `git pull`은 이미 연결된 저장소의 변경을 내려받아 합치는 것이다.

#### \# 복습 순서
1. Ubuntu VM 설치와 SSH 접속 흐름을 먼저 확인한다.
2. 파일/디렉토리/vi/권한 명령어를 직접 입력해 본다.
3. Maven으로 Spring Boot jar를 만들고 Linux에서 실행하는 흐름을 복습한다.
4. Docker image/container, port mapping, network, volume을 구분한다.
5. Dockerfile과 Docker Compose로 같은 실행 환경을 반복 가능하게 만드는 이유를 정리한다.
6. GitHub branch, PR, merge, pull, conflict 해결 순서로 협업 흐름을 복습한다.
