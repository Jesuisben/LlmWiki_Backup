AWS 총정리 (2026.05.06(수) ~ 2026.05.08(금))

#### \# AWS 수업의 전체 흐름
AWS 수업은 Linux와 Docker에서 로컬 또는 가상 머신으로 서버를 실행하던 흐름을 클라우드로 옮기는 과정이었다.

먼저 AWS 서비스와 네트워크 주소 체계를 이해하고, VPC 안에 Public Subnet 2개와 EC2 2대를 구성했다.

그 다음 두 EC2의 통신과 nginx 정적 페이지를 확인하고, Spring Boot 애플리케이션과 RDS MySQL을 연결했다.

마지막으로 RDS MySQL을 EC2의 Spring Boot 프로젝트와 연결하고, 실습 자원을 의존 순서에 맞춰 삭제하는 과정까지 확인했다.


#### \# AWS에서 자주 사용하는 메뉴
- VPC (Virtual Private Cloud)
나만의 가상 네트워크 공간을 만드는 서비스

VPC 대시보드에서 주로 보는 것
- VPC
- 서브넷
- 라우팅 테이블
- 인터넷 게이트웨이
- DHCP 옵션 세트
- 보안 그룹

- EC2 (Elastic Compute Cloud)
클라우드에서 사용하는 가상 서버

VirtualBox에서 가상 머신을 만들었던 것처럼, AWS에서는 EC2 인스턴스를 만들어 Linux 서버를 사용함

EC2 메뉴에서 주로 보는 것
- 인스턴스
- 인스턴스 유형
- 보안 그룹
- 탄력적 IP
- 키 페어
- 로드밸런서
- 대상 그룹

- RDS (Relational Database Service)
AWS가 MySQL 같은 데이터베이스 생성·상태·백업 같은 관리 기능을 제공하는 서비스

Aurora and RDS 메뉴에서 데이터베이스를 생성하고, 연결 정보와 Endpoint를 확인함

#### \# AWS 관련 기초 용어
- OnDemand
IT 자원을 필요한 만큼 사용하고, 사용한 만큼 비용을 내는 종량제 방식

서버를 미리 사서 보관하는 방식이 아니라 필요할 때 EC2, RDS 같은 자원을 생성해서 사용함

- OnPremise
서버, 네트워크, 데이터베이스 같은 장비를 회사나 개인이 직접 보유하고 운영하는 방식

OnDemand가 필요한 만큼 빌려 쓰는 방식에 가깝다면, OnPremise는 직접 장비를 구매하고 운영하는 방식임

- Region (리전)
서울, 도쿄처럼 AWS 데이터 센터가 있는 큰 물리적 지역

하나의 리전 안에 여러 개의 VPC를 만들 수 있음

- AZ (Availability Zone, 가용 영역)
하나의 리전 안에 있는 실제 데이터 센터 구역

VPC는 리전 범위의 논리적인 네트워크이고, Subnet과 EC2는 특정 AZ에 배치함

- Subnet (서브넷)
VPC 안에서 용도에 따라 나눈 더 작은 네트워크 공간

외부 요청을 받는 서버는 Public Subnet에 두고, 데이터베이스처럼 외부에 직접 공개하지 않을 자원은 별도 Subnet에 배치하는 방식으로 확장할 수 있음


#### \# 네트워크와 IP 주소
- 옥텟 (Octet)
`192.168.1.10`처럼 IPv4 주소를 점으로 나눈 각 숫자 묶음

IPv4 주소는 8비트 단위의 옥텟 4개로 구성됨

- Network 주소와 Host 주소
Network 주소는 어느 네트워크에 속하는지 나타내고, Host 주소는 그 네트워크 안의 개별 장치를 구분함

- CIDR
IP 주소 뒤의 `/16`, `/24`처럼 네트워크 범위를 표현하는 표기법

`10.250.0.0/16`은 앞쪽 16비트를 네트워크 주소로 사용하고, `10.250.1.0/24`은 앞쪽 24비트를 네트워크 주소로 사용함

- VPC와 Subnet 예시
VPC : `10.250.0.0/16`

Public Subnet 2A : `10.250.1.0/24`

Public Subnet 2C : `10.250.11.0/24`

VPC가 큰 네트워크 범위이고, Subnet은 그 안에서 실제 EC2를 배치할 용도로 나눈 범위임


#### \# 보안 그룹 (Security Group)
EC2나 RDS 앞에 두는 방화벽 같은 접근 규칙

- InBound
외부에서 서버 안으로 들어오는 트래픽 규칙

- OutBound
서버에서 외부로 나가는 트래픽 규칙

주로 확인할 포트
- HTTP : 80
- HTTPS : 443
- SSH : 22
- Spring Boot 예제 서버 : 9000
- MySQL : 3306

접속이 안될 때는 보안 그룹의 인바운드/아웃바운드 규칙을 먼저 확인해야 함

ICMP 규칙을 추가하면 `ping` 테스트를 허용할 수 있음

실습에서 `0.0.0.0/0`은 모든 IPv4 주소를 허용한다는 뜻이다. 실제 서비스에서는 특히 SSH와 DB 포트의 접속 출발지 범위를 필요한 곳으로 제한해야 함


#### \# VPC 기본 구성 과정
VPC 생성
-\> 인터넷 게이트웨이 생성
-\> 인터넷 게이트웨이를 VPC에 연결
-\> VPC DNS 설정 확인
-\> Public Subnet 생성
-\> 라우팅 테이블 생성
-\> 라우팅 테이블에 인터넷 게이트웨이 경로 추가
-\> 라우팅 테이블과 Subnet 연결
-\> 보안 그룹 생성 및 인바운드 규칙 설정
-\> KeyPair 생성
-\> EC2 인스턴스 생성
-\> 탄력적 IP 연결
-\> MobaXterm으로 SSH 접속


#### \# VPC 생성
VPC는 내가 사용할 가상 네트워크의 가장 큰 틀

예시 설정
- 이름 : EDU-VPC
- IPv4 CIDR 블록 : `10.250.0.0/16`
- IPv6 CIDR 블록 : 없음
- 테넌시 : 기본값

VPC 생성 후에는 이름을 확인하기 쉽도록 `Name` 태그를 설정함


#### \# 인터넷 게이트웨이와 라우팅 테이블
- 인터넷 게이트웨이 (Internet Gateway)
VPC 안의 자원이 인터넷과 통신할 수 있도록 연결하는 통로

인터넷 게이트웨이를 만든 뒤에는 반드시 사용할 VPC에 연결하고 상태가 Attached인지 확인함

- 라우팅 테이블 (Route Table)
네트워크 요청이 어디로 나가야 하는지 정하는 길 안내 표

인터넷으로 나가야 하는 Public Subnet에는 다음처럼 기본 경로를 추가함

```text
Destination : 0.0.0.0/0
Target      : 생성한 Internet Gateway
```

`0.0.0.0/0`은 모든 IPv4 주소, 즉 외부 인터넷 전체를 의미함

라우팅 테이블을 만든 것만으로는 충분하지 않고, 실제 사용할 Subnet과 연결해야 적용됨


#### \# VPC DNS 설정
VPC 설정에서 DNS 호스트 이름을 활성화함

IP 주소만 외우는 것보다 문자열 주소를 이용하는 것이 편하고, 이후 RDS Endpoint 같은 주소를 사용할 때도 필요함


#### \# Subnet과 EC2 2대 구성
- Public Subnet 2A
  - 이름 : EDU-PUBLIC-SBN-2A
  - 가용 영역 : ap-northeast-2a
  - Subnet CIDR : `10.250.1.0/24`
  - EC2 이름 : EDU-PUBLIC-EC2-2A

- Public Subnet 2C
  - 이름 : EDU-PUBLIC-SBN-2C
  - 가용 영역 : ap-northeast-2c
  - Subnet CIDR : `10.250.11.0/24`
  - EC2 이름 : EDU-PUBLIC-EC2-2C

서브넷을 서로 다른 AZ에 만들면, 서로 다른 위치의 EC2를 대상으로 통신과 서비스 구성을 실습할 수 있음

VPC, 인터넷 게이트웨이, 라우팅 테이블은 여러 Subnet이 공유할 수 있지만, EC2와 탄력적 IP는 각각의 서버에 맞게 따로 연결함


#### \# 보안 그룹 만들기와 규칙 설정
EC2용 보안 그룹을 만들고 VPC를 선택함

예시 이름 : EDU-PUBLIC-SG-2A, EDU-PUBLIC-SG-2C

처음에는 필요한 규칙만 열어두고, 접속 문제를 확인하면서 인바운드 규칙을 추가함

예시 인바운드 규칙

```text
HTTP              80    0.0.0.0/0
HTTPS             443   0.0.0.0/0
SSH               22    0.0.0.0/0
사용자 지정 TCP    9000  0.0.0.0/0
```

EC2끼리 `ping`을 확인하려면 모든 ICMP IPv4 인바운드 규칙도 필요할 수 있음


#### \# KeyPair와 EC2 인스턴스
- KeyPair
EC2에 SSH로 접속하기 위한 키 파일

키 페어를 만들면 `.pem` 개인 키 파일이 내려받아짐

개인 키 파일은 다시 받을 수 없을 수 있으므로 안전하게 보관해야 함

- EC2 인스턴스
클라우드에서 실행하는 Linux 가상 서버

예시 설정
- AMI : Ubuntu
- VPC와 Subnet : 만든 VPC와 해당 Public Subnet 선택
- 퍼블릭 IP 자동 할당 : 활성화
- 보안 그룹 : 해당 EC2용 보안 그룹 선택

EC2는 VirtualBox에서 Linux VM을 만드는 과정과 비슷하지만, 인터넷에 연결된 클라우드 서버라는 차이가 있음


#### \# 탄력적 IP (Elastic IP)
EC2의 Public IP는 인스턴스를 중지하거나 다시 시작하는 과정에서 바뀔 수 있음

고정된 주소로 접속하려면 탄력적 IP를 할당하고 EC2 인스턴스에 연결함

탄력적 IP는 연결하지 않고 보관하면 비용이 발생할 수 있으므로, 실습이 끝나면 연결 해제와 릴리스까지 확인해야 함


#### \# MobaXterm으로 EC2 접속
MobaXterm에서 SSH 세션을 만들고 다음 정보를 넣음

- Remote host : EC2에 연결한 탄력적 IP
- Username : Ubuntu 이미지라면 `ubuntu`
- Advanced SSH settings : KeyPair의 `.pem` 파일 선택
- Session name : EC2 이름과 비슷하게 지정

이제 내 컴퓨터의 MobaXterm에서 AWS EC2 Linux 서버를 조작할 수 있음


#### \# EC2끼리 ping 테스트
Public2A와 Public2C가 서로 통신할 수 있는지 `ping`으로 확인함

```shell
ping -c 5 <상대_EC2_IP>
```

처음에 패킷 손실이 발생하면 ICMP 인바운드 규칙이 없는지 확인함

보안 그룹에 모든 ICMP IPv4 규칙을 추가한 뒤 다시 실행하면 응답 패킷과 packet loss를 확인할 수 있음

`ping`은 서버가 살아있는지와 네트워크 통신 가능 여부를 간단히 확인하는 용도임


#### \# EC2에 nginx 설치와 정적 페이지 확인
각 Public EC2에 nginx를 설치하고 웹 서버가 실행되는지 확인함

```shell
sudo apt install -y nginx
sudo systemctl start nginx
sudo systemctl status nginx
```

두 EC2의 Public IP 또는 탄력적 IP로 브라우저 접속해서 nginx 기본 화면이 보이면 웹 서버가 동작하는 것

서버별 화면을 구분하려면 Git 저장소에서 정적 홈페이지 파일을 받고 `/var/www/html/`에 복사함

```shell
git clone <홈페이지_저장소_URL>
cd <서버별_홈페이지_디렉터리>
sudo cp -r ./* /var/www/html/
sudo systemctl restart nginx
```

Public2A와 Public2C에 서로 다른 화면을 넣으면, 어느 서버에 접속했는지 브라우저에서 구분할 수 있음


#### \# Spring Boot를 EC2에서 실행하기
nginx를 중지하고, EC2에 JDK와 Maven을 설치한 뒤 Spring Boot 프로젝트를 빌드함

```shell
sudo systemctl stop nginx
sudo apt update
sudo apt install -y openjdk-17-jdk
sudo apt install -y maven
java -version
mvn -v
```

프로젝트를 받은 뒤 Maven으로 jar 파일을 만듦

```shell
git clone <Spring_Boot_프로젝트_URL>
cd <프로젝트_디렉터리>
mvn clean package -DskipTests
cd target/
```

80 포트 요청을 Spring Boot 예제 서버의 9000 포트로 보내도록 설정하고 jar를 실행함

```shell
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 9000
java -jar <생성된_jar_파일명>.jar
```

IntelliJ에서 Spring Boot 애플리케이션을 실행하던 것을, 이제는 EC2 Linux 서버에서 직접 실행하는 과정


#### \# EC2에서 HTML 파일 수정 후 다시 빌드하기
Public2C처럼 서버별 화면을 구분하고 싶다면 프로젝트의 HTML 템플릿을 수정함

```shell
sudo vi <프로젝트_경로>/src/main/resources/templates/<HTML_파일명>.html
```

수정 후에는 다시 Maven 빌드를 하고 jar를 실행해야 변경 사항이 반영됨

```shell
cd <프로젝트_디렉터리>
mvn clean package -DskipTests
cd target/
java -jar <생성된_jar_파일명>.jar
```

`mvn clean package`의 `clean`은 기존 `target` 디렉터리를 정리한 뒤 새로 빌드하는 과정


#### \# RDS와 Spring Boot 연동
RDS는 AWS에서 MySQL 같은 데이터베이스를 생성하고 관리하는 서비스

EC2에 직접 DB를 설치할 수도 있지만, RDS를 사용하면 DB 인스턴스 생성과 관리 기능을 AWS에서 제공받을 수 있음

RDS 생성 시 확인할 것
- 엔진 옵션 : MySQL
- 템플릿 : 프리 티어 여부 확인
- 가용성 및 내구성 : 실습에서는 단일 AZ 인스턴스 사용
- DB 인스턴스 식별자
- 마스터 사용자 이름과 암호
- 초기 데이터베이스 이름
- VPC와 보안 그룹

생성이 끝나려면 상태가 `사용 가능`으로 바뀌어야 함

- Endpoint
RDS에 접속할 때 사용하는 데이터베이스 주소

Spring Boot의 `application.properties`에서 기존 `localhost` 대신 RDS Endpoint를 사용함

```properties
spring.datasource.url=jdbc:mysql://<RDS_ENDPOINT>:3306/<DATABASE_NAME>
spring.datasource.username=<DB_USERNAME>
spring.datasource.password=<DB_PASSWORD>
```

암호, 실제 Endpoint, 개인 키 같은 값은 총정리나 Git 저장소에 그대로 남기지 않고 별도로 관리해야 함

- EC2와 RDS 연결
EC2와 RDS가 같은 VPC 안에서 통신하도록 만들고, RDS 보안 그룹에서 MySQL 포트 접근이 허용되는지 확인해야 함

Public2A와 Public2C 같은 여러 EC2가 하나의 RDS 데이터베이스를 함께 사용할 수 있음


#### \# EC2에서 MySQL 클라이언트로 RDS 접속
EC2에서 MySQL 클라이언트를 설치한 뒤 RDS Endpoint로 접속 테스트함

```shell
sudo apt update
sudo apt install mysql-client -y
mysql -h <RDS_ENDPOINT> -P 3306 -u <DB_USERNAME> -p
```

접속이 안 되면 다음을 확인함
- RDS 상태가 사용 가능인지
- Endpoint와 포트 번호가 맞는지
- 사용자 이름과 암호가 맞는지
- EC2와 RDS 보안 그룹에서 MySQL 접근을 허용했는지


#### \# RDS에서 테이블과 데이터 만들기
RDS에 접속한 뒤 Spring Boot 프로젝트에서 사용할 데이터베이스와 테이블을 확인함

```sql
SHOW DATABASES;
USE <DATABASE_NAME>;
SHOW TABLES;

CREATE TABLE products(
    id BIGINT PRIMARY KEY,
    name VARCHAR(100),
    price INT,
    description TEXT,
    image_url VARCHAR(255)
);
```

상품 데이터를 추가한 뒤 `SELECT`로 조회하면, Spring Boot가 사용할 데이터가 RDS에 들어간 것을 확인할 수 있음


#### \# RDS 연결 프로젝트 실행
RDS를 사용하는 Spring Boot 프로젝트를 받은 뒤 `application.properties`의 DB 연결 정보를 RDS 기준으로 바꿈

```shell
git clone <RDS_연동_프로젝트_URL>
cd <프로젝트_디렉터리>
vi src/main/resources/application.properties
mvn clean package -DskipTests
cd target/
java -jar <생성된_jar_파일명>.jar
```

로컬에서는 `localhost` DB를 보던 프로젝트가, EC2에서는 RDS MySQL을 바라보도록 바뀌는 과정


#### \# AWS 자원 삭제 순서
AWS 실습 자원은 남아 있으면 비용이 발생할 수 있으므로, 실습 종료 후 삭제 순서도 중요함

기본 흐름
탄력적 IP 연결 해제
-\> 탄력적 IP 릴리스
-\> EC2 인스턴스 종료
-\> RDS 데이터베이스 삭제
-\> 보안 그룹 정리
-\> 인터넷 게이트웨이 분리·삭제
-\> Subnet과 라우팅 테이블 정리
-\> VPC 삭제
-\> KeyPair 삭제

- 탄력적 IP
연결 해제 후 릴리스해야 더 이상 사용하지 않는 IP 주소 비용을 줄일 수 있음

- EC2
인스턴스를 종료한 뒤 상태가 종료됨인지 확인함

- RDS
삭제 과정에서 최종 스냅샷 여부와 삭제 확인 항목을 잘 확인함

- 보안 그룹
다른 자원이 아직 참조하고 있으면 삭제되지 않을 수 있으므로 EC2와 RDS를 먼저 정리함

- VPC
연결된 자원이 남아 있으면 삭제할 수 없으므로 인터넷 게이트웨이, 서브넷, 보안 그룹, EC2, RDS 같은 의존 자원을 먼저 확인함


#### \# AWS 전체 흐름 정리
1) Region 안에 VPC라는 내 가상 네트워크를 만든다.

2) VPC 안에 Public Subnet을 만들고, 인터넷 게이트웨이와 라우팅 테이블을 연결한다.

3) 보안 그룹에서 HTTP, HTTPS, SSH, Spring Boot 포트 같은 필요한 접속 규칙을 연다.

4) EC2 인스턴스를 만들고 KeyPair와 탄력적 IP를 연결한 뒤 MobaXterm으로 SSH 접속한다.

5) EC2끼리 ping으로 통신을 확인하고 nginx 또는 Spring Boot 애플리케이션을 설치·실행한다.

6) RDS MySQL을 만들고 EC2/Spring Boot가 Endpoint를 이용해 데이터베이스에 접속하도록 설정한다.

7) 실습이 끝나면 비용이 발생할 수 있는 탄력적 IP, EC2, RDS, 보안 그룹, VPC를 의존 순서에 맞춰 정리한다.


#### \# 헷갈리기 쉬운 점
- VPC는 네트워크 전체 틀이고, Subnet은 VPC 안에서 나눈 작은 네트워크 구역임

- Security Group은 EC2, RDS 같은 AWS 자원에 적용하는 접근 규칙임

- 인터넷 게이트웨이를 만들기만 해서는 인터넷 연결이 되지 않고, VPC 연결과 라우팅 테이블 설정까지 해야 함

- EC2의 Public IP와 Elastic IP는 다름. Public IP는 바뀔 수 있고, Elastic IP는 고정해서 연결하는 주소임

- EC2는 서버를 직접 관리하는 가상 머신이고, RDS는 AWS가 관리 기능을 제공하는 데이터베이스 서비스임

- AWS는 자원을 만든 것뿐 아니라 남겨두는 것도 비용과 연결될 수 있으므로, 실습 종료 후 삭제 확인이 중요함
