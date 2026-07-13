Passwordless 총정리 (2026.05.14(목) ~ 2026.05.21(목))

#### \# Passwordless 수업의 전체 흐름
Passwordless 수업은 비밀번호를 직접 입력하는 인증 방식이 피싱·키로거·악성코드에 취약하다는 문제에서 시작했다.

먼저 피싱, 랜섬웨어, 원격 코드 실행(RCE), DDoS 같은 공격과 제로트러스트 관점을 살펴보고, 입력 기반 credential을 줄이는 ITU-T X.1280 Passwordless 인증의 개념을 배웠다.

그 다음 Passwordless X1280 서비스를 Members 사이트에 등록하고, Docker 기반 인증 서버를 설치해 Auth Server, User Connection Server, Push Request Server를 구성했다.

이후 MariaDB·Java/Spring 샘플 애플리케이션·Tomcat을 연결해 계정 등록, 모바일 앱 승인, Passwordless 로그인과 해제 흐름을 실습했다.

마지막으로 인증·인가·IDP·SSO·상호인증을 구분하고 AAM/APE 통합 서버, FilingBox GIGA/MEGA의 WORM 스토리지, Postman REST API 호출까지 확장했다.

즉 이 과목은 로그인 화면 하나를 만드는 방법보다, 사용자·인증 서버·모바일 인증기·애플리케이션 서버·저장소를 함께 보호하는 보안 서비스 흐름을 다룬 과정이다.


#### \# Passwordless가 필요한 보안 배경
수업에서 다룬 대표 공격은 다음과 같다.

- 피싱(Phishing)
이메일이나 메시지로 사용자를 속여 ID·비밀번호 입력을 빼앗고 내부 시스템에 침투하는 공격이다.

- 랜섬웨어(Ransomware)
악성코드로 PC·서버의 데이터를 암호화하거나 유출한 뒤 금전을 요구하는 공격이다. 피싱으로 이미 침투한 뒤 실행되는 경우가 많다.

- 원격 코드 실행(RCE, Remote Code Execution)
서버·클라우드·애플리케이션의 취약점을 악용해 권한을 올리거나 관리자 권한을 탈취하는 공격이다. 사용자가 로그인하는 절차를 우회하는 백도어와 연결될 수 있다.

- DDoS
대량 트래픽으로 서비스 접속을 마비시키는 공격이다. 서버 자체보다 네트워크 설계가 병목이 되어 장애가 나는 경우도 있다.

기존 인증은 사용자가 비밀번호, OTP 같은 정보를 입력해 자신을 증명하는 Input-Based User Credential 방식에 의존한다. 하지만 입력 행위가 존재하면 피싱 페이지, 키로거, 중간자 공격이 그 입력을 노릴 수 있다.

제로트러스트(Zero Trust)는 내부 사용자를 포함해 이미 공격자가 침투했을 수 있다고 가정하고, 신뢰 대신 지속적인 검증을 적용하는 보안 관점이다. Passwordless는 이 관점에서 사용자 입력 비밀값을 줄이고 인증기·서버 상태를 검증하려는 접근이다.


#### \# Passwordless X1280의 핵심 개념
Passwordless X1280은 ITU-T X.1280 번호가 부여된 Passwordless 인증 기술로 수업에서 소개되었다.

기존 ID/비밀번호 로그인은 사용자가 비밀번호를 입력해 서버에 전달한다. 반면 X1280 흐름에서는 사용자가 ID를 입력한 뒤, 서버가 인증번호 또는 승인 요청을 사용자 모바일 인증기에 제시하고 사용자가 앱에서 승인한다.

사용자 입력 -\> 서버 검증이라는 일방향 흐름 대신, 서비스 요청과 모바일 인증기의 확인을 연결해 사용자 인증과 서버 인증을 함께 확인하는 것이 핵심이다.

- 기존 OTP와의 차이
기존 OTP는 생성된 일회용 번호를 사용자가 다시 웹 화면에 입력하는 방식이다. Passwordless X1280은 사용자가 번호를 다시 입력하는 단계를 줄이고 앱에서 승인한다.

- FIDO·Passkey와의 맥락
수업에서는 FIDO·Passkey를 단말기의 생체인증 센서를 사용하는 대역내 인증 방식으로 비교했다. X1280은 모바일 인증기를 별도로 활용해 생체인증 센서를 추가하기 어려운 장치도 지원하려는 대역외 인증 방식으로 설명되었다.

- 인증기 확인
요청이 어느 서비스에서 왔는지, 사용자가 가진 인증기인지, 추가 생체인증이 필요한지를 앱 승인 과정에서 확인한다.

- AI Agent와의 연결
AI Agent가 인증이 필요한 작업을 수행할 때 최종 승인권을 사용자에게 남겨두는 방식으로 Passwordless 인증을 연결할 수 있다.


#### \# 인증, 인가, IDP, SSO, 상호인증
인증(Authentication)과 인가(Authorization)는 구분해야 한다.

- 인증
사용자가 정말 그 사용자와 같은지 확인하는 과정이다. 비밀번호·PIN처럼 아는 것, OTP 앱·보안카드처럼 가진 것, 지문·얼굴처럼 나 자신이라는 세 가지 요소를 조합한 MFA(Multi-Factor Authentication)로 강화할 수 있다.

- 인가
인증된 사용자가 어느 기능·데이터까지 접근하거나 수정할 수 있는지 판단하는 과정이다. 로그인했다고 모든 상품 가격을 수정하거나 데이터를 삭제할 권한이 생기는 것은 아니다.

- IDP(Identity Provider)
여러 웹사이트·앱에서 쓸 수 있는 디지털 신원을 발급하고 관리하는 시스템이다.

- SSO(Single Sign-On)
한 번 로그인해 얻은 인증 티켓 또는 토큰을 이용해 연결된 여러 서비스의 재로그인 부담을 줄이는 방식이다.

- 상호인증(Mutual Authentication)
서비스가 사용자만 확인하는 단방향 인증과 달리, 사용자도 접속하려는 서비스가 신뢰할 수 있는 대상인지 확인하는 방식이다. 피싱·파밍 사이트에 정보를 넘기지 않도록 돕는 Passwordless의 중요한 맥락이다.


#### \# X1280 서비스 적용 순서
Passwordless X1280 서비스 적용은 다음 세 단계로 정리할 수 있다.

서비스 등록 -\> X1280 인증 서버 설치 -\> 웹 애플리케이션 적용

1\. 서비스 등록 단계
Members 사이트에서 애플리케이션 정보와 서비스 도메인을 등록한다. 일반 모드에서는 DNS TXT 레코드로 도메인 검증을 수행하고, 테스트 모드에서는 검증 절차가 간소화된다.

서비스 승인 뒤 내려받는 `setting.ap` 파일은 Auth Server 관리자 페이지에 업로드하는 라이선스·설정 파일이다.

2\. X1280 서버 설치 단계
Docker를 설치하고 X1280 통합 컨테이너를 실행한다. 이 컨테이너는 다음 서버를 함께 설치한다.

- Auth Server: 서비스 설정과 인증 관리
- User Connection Server: 사용자 연결 처리
- Push Request Server: 모바일 앱으로 승인 요청 전달

3\. 웹 애플리케이션 적용 단계
애플리케이션은 UI 제공 방식 또는 RESTful API 제공 방식으로 X1280 인증 기능을 연결할 수 있다. 관리자 페이지의 서비스 서버 설정에서 API 사용 종류를 선택하고, 애플리케이션에는 서버 ID·서버 키·인증 서버 URL 같은 연결 정보를 설정한다.


#### \# WEB 서버와 WAS 서버
- WEB 서버
HTML, CSS, 이미지처럼 정적 파일을 주로 제공한다.

- WAS(Web Application Server)
JSP, Java Class, API처럼 요청에 따라 결과가 바뀌는 동적 처리를 담당한다.

Passwordless 연동에서는 웹 화면이 로그인·등록 UI를 제공하고, WAS 또는 Spring 애플리케이션이 인증 서버 REST API와 통신하며 서비스 계정의 상태를 처리한다.


#### \# Docker로 Passwordless X1280 서버 설치
Rocky Linux에서 Docker Engine을 준비하고, X1280 컨테이너가 사용할 Docker network를 만든다.

```shell
dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
dnf -y install docker-ce docker-ce-cli containerd.io
systemctl start docker
systemctl enable docker

docker network create some-network
docker network ls
```

X1280 통합 이미지는 인증 서버, 사용자 연결 서버, Push Request 서버와 필요한 volume·port를 한 컨테이너 구성으로 실행한다.

```shell
docker run -d --name server \
--network some-network \
--restart always \
-e DOMAIN={Passwordless 서버 도메인 또는 IP} \
-e USE_SSL=false \
-v auth-settings:/opt/x1280/tomcat/conf/passwordless \
-v auth-logs:/opt/x1280/tomcat/logs \
-v user-connection-logs:/opt/x1280/connector/logs \
-v push-request-logs:/opt/x1280/pushConnector/logs \
-v config:/etc/opt/x1280 \
-v database:/var/lib/mysql \
-p 8005:8005 \
-p 8080:8080 \
-p 8180:8180 \
-p 8143:8143 \
-p 8443:8443 \
-p 11040:11040 \
-p 12010:12010 \
-p 15010:15010 \
dualauth/passwordless-x1280-single:latest
```

컨테이너의 port mapping과 Host 서버 방화벽은 별개다. 외부에서 접근해야 하는 port는 Docker Host의 `firewalld`에도 허용해야 한다.

```shell
dnf install -y firewalld
systemctl enable --now firewalld

firewall-cmd --zone=public --permanent --add-port=8143/tcp
firewall-cmd --zone=public --permanent --add-port=11040/tcp
firewall-cmd --zone=public --permanent --add-port=15010/tcp
firewall-cmd --reload
firewall-cmd --list-all
```

실행 뒤에는 image, network, volume과 각 서버 프로세스를 확인한다.

```shell
docker image ls
docker network ls
docker volume ls

docker exec -it server /bin/bash
ps -ef | grep tomcat
ps -ef | grep connect
ps -ef | grep push
```

설치 상태를 처음부터 다시 만들 때는 컨테이너·이미지·연결된 volume·network를 순서대로 정리해야 한다. 이 과정은 인증 서버 데이터까지 제거할 수 있으므로, 실습 초기화와 운영 데이터 삭제를 구분해야 한다.


#### \# SSL과 Auth Server 관리자 설정
HTTP 대신 HTTPS로 운영하려면 Passwordless 서버 도메인용 인증서와 Tomcat keystore를 준비하고 컨테이너가 읽을 수 있는 경로에 배치한다. `USE_SSL=false`는 인증서를 적용하지 않는 실습 구성에만 사용한다.

Auth Server 관리자 페이지에서는 다음을 수행한다.

1\. Members 사이트에서 내려받은 `setting.ap` 파일 업로드
2\. 서비스 서버 정보 등록
3\. 서버 ID와 서버 키 발급·보관
4\. UI 제공 또는 REST API 제공 방식 선택

서버 키는 웹 애플리케이션이 인증 서버를 호출할 때 쓰는 연결 정보이므로 소스 코드·공개 저장소에 직접 적지 않고 환경별 설정 또는 비밀값 관리 도구로 분리해야 한다.


#### \# Spring 웹 애플리케이션과 Passwordless 연동
로컬 개발 환경에서는 MariaDB, JDK, Spring Tools for Eclipse(STS), Passwordless Java REST API 샘플 프로젝트를 준비했다.

샘플 애플리케이션은 MariaDB에 사용자 정보를 저장하고, `config.properties`에서 X1280 서버 연결 정보를 읽는다. 실제 값은 환경마다 다르므로 아래처럼 placeholder로 관리해야 한다.

```properties
passwordless.corpId={서버 아이디}
passwordless.serverId={서버 아이디}
passwordless.serverKey={서버 키}
passwordless.simpleAutopasswordUrl=http://{인증 서버 주소}:8080
passwordless.restCheckUrl=http://{인증 서버 주소}:11040
passwordless.pushConnectorUrl=ws://{인증 서버 주소}:15010
```

연동 후 학습한 사용자 흐름은 다음과 같다.

계정 생성 -\> Passwordless 등록 -\> 모바일 앱에 서비스 등록 -\> Passwordless 로그인 승인 -\> 로그아웃 -\> Passwordless 해제 -\> 비밀번호 로그인 확인

수업 샘플에서는 Passwordless 로그인 뒤 기존 비밀번호가 임의 값으로 변경될 수 있으므로, 다시 일반 비밀번호 로그인으로 돌아가려면 Passwordless 등록 해제가 필요하다는 동작을 확인했다.


#### \# MariaDB와 애플리케이션 서버 배포
Passwordless 샘플은 사용자 정보를 저장할 MariaDB 데이터베이스와 `userinfo` 테이블을 사용했다. 데이터베이스 계정·비밀번호 같은 실제 credential은 예제 파일이나 Git 저장소에 노출하지 않고 별도 설정으로 관리해야 한다.

```sql
CREATE DATABASE passwordless;

USE passwordless;

CREATE TABLE userinfo (
    `id` varchar(1000) NOT NULL,
    `pw` varchar(1000) NOT NULL,
    `regdate` datetime NULL DEFAULT NOW(),
    PRIMARY KEY (`id`)
);
```

서버 배포에서는 Rocky Linux에 MariaDB, OpenJDK, Tomcat을 설치하고, Maven으로 만든 WAR 파일을 Tomcat `webapps`에 배치했다.

```shell
/usr/local/tomcat/bin/shutdown.sh
rm -rf /usr/local/tomcat/webapps/ROOT
rm -f /usr/local/tomcat/webapps/ROOT.war
cp ./ROOT_rest.war /usr/local/tomcat/webapps/ROOT.war
/usr/local/tomcat/bin/startup.sh
```

배포 뒤에는 Tomcat의 설정 파일을 수정하는 것만으로 끝내지 않고, 서버 재시작과 브라우저에서 Passwordless 등록·로그인·해제 흐름을 다시 확인해야 한다.


#### \# AAM과 APE 통합 인증 관리
Passwordless 수업 후반에는 AAM(Autopassword Access Manager)과 APE(Autopassword Enterprise)를 이용한 인증 관리 환경도 실습했다.

- AAM
사용자·정책·인증 서버 설정과 클라이언트 접근을 관리하는 역할로 다뤘다.

- APE
AAM과 연동해 사용자·인증기 정보를 관리하고, 관리자 웹에서 라이선스·연동 서비스·정책을 설정하는 역할로 다뤘다.

실습의 큰 흐름은 다음과 같다.

VM 준비 -\> AAM/APE/DMZ 통합 설치 -\> 라이선스 키 적용 -\> APE 기본 설정 -\> AAM 인증 서버 설정 -\> 부서·사용자 생성 -\> 모바일 Enterprise 앱 계정 등록 -\> Windows Client 로그인

AAM과 APE의 Corp ID, Manager Token, Secret key 같은 연동 값은 서로 일치해야 한다. 한쪽 설정만 바꾸면 사용자 정보·정책·인증 요청의 연동이 실패할 수 있으므로, 관리자 화면에서 값을 비교하고 수정한 뒤 저장한다.


#### \# FilingBox, NAS, WORM으로 보는 저장소 보호
인증만 강해도 랜섬웨어로부터 데이터가 자동으로 안전해지는 것은 아니다. 수업에서는 NAS와 WORM 저장소를 통해 데이터 보호 계층을 함께 살펴봤다.

- NAS(Network Attached Storage)
네트워크를 통해 여러 장치가 접근할 수 있는 저장소다.

- WORM(Write Once Read Many)
데이터를 한 번 기록한 뒤에는 읽기만 가능하도록 하는 보존 방식이다. 원본 보존과 변경 방지에 사용한다.

- FilingBox GIGA
가상 머신으로 서버를 구성하고, 관리자·그룹·사용자·공유 폴더를 만들며 폴더별 저장 모드를 설정했다.

- FilingBox MEGA
장치 관리와 Windows Client 연결을 중심으로 살펴봤다.

실습에서 구분한 폴더/드라이브 모드는 다음과 같다.

| 모드 | 의미 | 사용 맥락 |
| --- | --- | --- |
| RO | Read Only, 읽기 전용 | 원본·규정 자료의 열람 |
| RW | Read Write, 읽기·쓰기 | 일반 협업 폴더 |
| AO | Append Only, 추가 전용 | 기존 기록을 바꾸지 않고 새 기록만 추가 |
| WORM | Write Once Read Many | 변경 방지가 필요한 보존 데이터 |

이 흐름은 Passwordless가 계정 탈취를 줄이는 인증 계층이라면, FilingBox는 탈취·랜섬웨어 이후에도 데이터를 변경하기 어렵게 만드는 저장소 보호 계층이라는 점을 보여준다.


#### \# REST API와 Postman 확인
마지막 실습에서는 Postman으로 X1280 인증 서버 REST API를 호출했다. 먼저 Postman collection을 import하고, 서버 키·인증 서버 주소·사용자 ID 같은 환경별 값을 Variables에 설정한다.

사용자 등록 여부 확인(isAP) 호출은 인증 서버가 해당 사용자에게 Passwordless 인증기가 등록됐는지 확인하는 예시다. 응답은 JSON 구조로 확인한다.

```json
{
  "result": true,
  "msg": "OK.",
  "code": "000.0",
  "data": {
    "exist": false
  }
}
```

`result`는 API 호출의 처리 결과, `code`와 `msg`는 상태 설명, `data.exist`는 사용자 인증기 등록 여부를 나타내는 값으로 읽을 수 있다. 실제 서비스에서는 HTTP 상태 코드, API 문서, 오류 응답과 함께 해석해야 한다.


#### \# 전체 인증·보호 흐름 다시 보기
Passwordless 수업의 구성 요소는 다음 흐름으로 연결된다.

사용자 로그인 요청 -\> 웹 애플리케이션 -\> X1280 Auth Server -\> User Connection/Push Request Server -\> 모바일 인증기 승인 -\> 인증 결과 반환 -\> 애플리케이션 접근 허용

여기에 운영 관점의 구성 요소가 더해진다.

- Docker·VM·방화벽: 인증 서버 실행 환경과 네트워크 접근 제어
- MariaDB·Tomcat·Spring: 사용자 데이터와 웹 애플리케이션 실행
- AAM·APE·SSO·IDP: 사용자·정책·연동 서비스의 인증 관리
- NAS·WORM·FilingBox: 랜섬웨어 이후까지 고려한 데이터 보존
- Postman REST API: UI 밖에서 인증 서버 동작을 검증하는 도구

Passwordless는 비밀번호 입력을 없애는 화면 기능만이 아니라, 피싱 저항성·상호인증·인증기 승인·서버 설정·비밀값 관리·데이터 보호를 함께 설계해야 하는 보안 아키텍처의 한 부분이다.
