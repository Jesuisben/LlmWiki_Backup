Ci&CD 총정리 (2026.05.11(월) ~ 2026.05.13(수))

#### \# Ci&CD 수업의 전체 흐름
CI&CD 수업은 GitHub에 코드를 push한 뒤 Spring Boot 애플리케이션을 빌드하고, Docker Image를 Docker Hub에 올린 다음, AWS EC2에서 새 컨테이너로 실행하는 배포 자동화 흐름에서 시작했다.

그 다음 기존 AWS 수업에서 만든 도메인, Route 53, ACM 인증서, Application Load Balancer를 다시 연결해 HTTPS와 여러 EC2로의 부하 분산 흐름을 복습했다.

마지막으로 Terraform으로 VPC, Subnet, EC2처럼 클라우드 인프라를 코드로 선언하고, Spring Boot에서 Amazon S3 버킷에 이미지를 올리고 RDS MySQL에 상품 정보를 저장하는 흐름까지 확장했다.

즉 이 과목은 Linux·Docker·GitHub·AWS에서 따로 배운 배포 구성 요소를 자동화와 Infrastructure as Code(IaC) 관점으로 연결한 과정이다.


#### \# CI/CD란 무엇인가
- CI (Continuous Integration, 지속적 통합)
개발자가 변경한 코드를 자주 원격 저장소에 통합하고, 빌드·테스트 같은 검증을 자동으로 수행하는 과정이다.

- CD (Continuous Deployment, 지속적 배포)
검증된 결과물을 실제 실행 환경으로 전달하고, 새 버전을 배포하는 과정이다.

수업에서 정리한 전체 흐름은 다음과 같다.

개발자 -\> GitHub push -\> GitHub Actions 빌드 -\> Docker Image 생성 -\> Docker Hub push -\> EC2 Docker pull -\> Container 실행 -\> 서비스 배포

CI는 GitHub에 push된 소스를 빌드해 배포 가능한 결과물로 확인하는 구간이고, CD는 Docker Hub의 Image를 EC2에 가져와 실제 서비스로 실행하는 구간이다.

자동화를 시작시키는 기준점은 trigger(이벤트)다. 이번 실습에서는 `master` 브랜치로의 GitHub push가 trigger였다.

- CI/CD 도구 예시
  - GitHub Actions
  - Jenkins
  - GitLab CI/CD
  - CircleCI

- 배포 대상 예시
  - Linux 서버
  - Docker Container
  - AWS 같은 Cloud 환경


#### \# CI/CD를 시작하기 전 준비한 Spring Boot 프로젝트
Spring Initializr에서 Maven·Java 기반 Spring Boot 프로젝트를 생성하고 IntelliJ에서 열었다. 프로젝트는 Jar로 패키징하며, 웹 요청을 처리하는 Controller와 설정 파일을 먼저 준비했다.

`MainController`는 루트 URL 요청에 응답하는 가장 작은 서버 기능이다.

```java
package com.coffee.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MainController {

    @GetMapping("/")
    public String hello() {
        return "Hello GitHub Actions!";
    }
}
```

Spring Boot 서버 포트는 `application.properties`에서 설정했다.

```properties
server.port=9000
```

Maven의 `pom.xml`에는 Web과 Thymeleaf 의존성을 추가하고, 빌드 결과물 이름을 정할 수 있다.

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-web</artifactId>
</dependency>

<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-thymeleaf</artifactId>
</dependency>

<build>
  <finalName>cicd</finalName>
</build>
```

이 프로젝트를 Git 로컬 저장소로 만들고 GitHub 원격 저장소에 첫 push한 뒤, 이후 push마다 자동 빌드가 일어나도록 GitHub Actions workflow를 추가했다.


#### \# GitHub Actions CI workflow
GitHub Actions의 workflow 파일은 반드시 `.github/workflows/` 경로에 둔다. 파일명은 임의로 정할 수 있지만, 수업에서는 `ci.yml`을 사용했다.

```yaml
name: Spring Boot CI

on:
  push:
    branches:
      - master

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout source
        uses: actions/checkout@v4

      - name: Set up JDK 21
        uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'
          cache: maven

      - name: Build with Maven
        run: mvn clean package -DskipTests
```

workflow의 핵심 역할은 다음과 같다.

- `on.push.branches` : 어느 브랜치의 push를 실행 조건으로 삼을지 정한다.
- `actions/checkout` : GitHub runner에 현재 소스 코드를 가져온다.
- `actions/setup-java` : 빌드에 필요한 JDK 버전을 맞춘다.
- `mvn clean package -DskipTests` : 기존 빌드 산출물을 정리하고 Jar를 생성한다.

GitHub 저장소의 Actions 탭에서는 commit별 workflow 실행 이력과 build 단계의 성공·실패 로그를 확인할 수 있다. 자동화는 파일을 만들었다고 끝나는 것이 아니라, push 후 실행 결과를 확인해야 한다.


#### \# GitHub Secrets와 Docker Hub 인증
Docker Hub Access Token, EC2 접속 정보, Docker Image 이름처럼 소스 코드에 직접 넣으면 안 되는 값은 GitHub Secrets에 저장한다.

GitHub Secrets는 workflow 실행 시점에만 값을 전달하는 보안 저장소다. `.yml`, Java 코드, `application.properties`에 실제 토큰이나 개인 키를 적는 방식과 구분해야 한다.

수업에서 CD workflow에 연결한 대표적인 Secret 이름은 다음과 같다.

| Secret 이름 | 역할 |
| --- | --- |
| `DOCKER_USERNAME` | Docker Hub 계정 식별자 |
| `DOCKER_PASSWORD` | Docker Hub Access Token |
| `EC2_HOST` | 배포 대상 EC2의 Public 또는 Elastic IP |
| `EC2_KEY` | EC2 SSH Key Pair의 개인 키 내용 |
| `DOCKER_IMAGE` | Docker Hub에 push할 Image 이름 |
| `DOCKER_CONTAINER` | EC2에서 실행할 Container 이름 |

Docker Hub에 로그인하고 Image를 빌드·push하는 workflow 단계는 다음 형태다.

```yaml
- name: Login to DockerHub
  run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin

- name: Build Docker Image
  run: docker build -t "${{ secrets.DOCKER_IMAGE }}" -f SpringDockerFile .

- name: Push Docker Image
  run: docker push "${{ secrets.DOCKER_IMAGE }}"
```

`--password-stdin`은 비밀번호나 토큰을 명령행 인수에 직접 노출하지 않고 표준 입력으로 전달하기 위한 옵션이다. workflow에서 참조하는 Secret 이름과 GitHub 저장소 Settings에 등록한 Secret 이름은 정확히 일치해야 한다.


#### \# EC2에 Docker 배포 환경 준비하기
EC2에서 Docker Hub Image를 받아 컨테이너로 실행하려면 Docker Engine과 현재 사용자 권한을 준비해야 한다. Windows에서 만든 shell script를 Linux에서 실행할 때는 CRLF 줄바꿈 문제도 확인했다.

```shell
sudo cp docker_setup.sh.txt /root/docker_setup.sh
sudo su -
apt update
apt install dos2unix -y
dos2unix docker_setup.sh
chmod +x docker_setup.sh
./docker_setup.sh
```

Docker 서비스가 설치·실행 중인지 확인한다.

```shell
docker container --help
systemctl status docker
```

일반 사용자가 매번 `sudo` 없이 Docker 명령을 실행할 수 있도록 `docker` 그룹에 추가하고, 다시 로그인한 뒤 그룹과 버전을 확인한다.

```shell
exit
sudo usermod -aG docker $USER
groups $USER
docker version
```

`groups $USER` 출력에 `docker`가 포함되면 해당 사용자는 Docker 그룹에 속해 있다. 권한을 바꾼 직후에는 logout/login이 필요할 수 있다.

```text
ubuntu : ubuntu adm cdrom sudo dip lxd docker
```

컨테이너가 실제로 실행되었는지는 다음 명령으로 확인한다.

```shell
docker container ps -a
```

```text
CONTAINER ID   IMAGE                              COMMAND               STATUS              PORTS                    NAMES
<container-id> <docker-image>:latest              "java -jar app.jar"   Up About a minute   0.0.0.0:80->9000/tcp   <container-name>
```

외부 80 포트 요청을 컨테이너 내부 Spring Boot 9000 포트로 연결하면, 브라우저는 기본 HTTP 포트로 접속하고 애플리케이션은 설정한 포트에서 응답할 수 있다.


#### \# CI/CD 변경 반영 흐름
새 Controller, HTML template, 정적 이미지처럼 고객 요청에 따른 변경을 프로젝트에 추가한 뒤 GitHub에 다시 push하면 동일한 workflow가 다시 실행된다.

변경 반영의 핵심 순서는 다음과 같다.

소스 수정 -\> Git commit -\> Git push -\> GitHub Actions CI/CD 실행 -\> Docker Image 갱신 -\> EC2 Container 교체 -\> URL 접속 확인

화면이나 이미지만 바꿨더라도 배포 대상 컨테이너가 새 Image를 사용하도록 갱신되어야 한다. 따라서 Actions 실행 성공 여부뿐 아니라 배포 뒤 실제 URL에서 변경 사항이 보이는지 확인해야 한다.


#### \# 도메인, Route 53, ACM, HTTPS
CI/CD 다음 날에는 AWS에서 만든 애플리케이션을 IP 주소 대신 도메인으로 접속하고 HTTPS를 적용하는 흐름을 복습했다.

DNS(Domain Name System)는 사람이 읽기 쉬운 도메인 이름과 서버 또는 다른 네트워크 대상의 연결 정보를 관리한다.

도메인 연결의 기본 순서는 다음과 같다.

도메인 신청 -\> Route 53 Hosted Zone 생성 -\> NS 레코드 확인 -\> 도메인 등록 업체에 네임서버 연결 -\> ACM 인증서 요청 -\> CNAME 검증 레코드 생성 -\> 인증서 발급 확인

- Hosted Zone : 특정 도메인의 DNS 레코드를 관리하는 공간이다.
- NS 레코드 : 해당 도메인의 DNS를 담당하는 Name Server 정보다.
- SOA 레코드 : DNS 영역의 기본 메타데이터를 담는다.
- CNAME 레코드 : 다른 이름을 가리키는 DNS 레코드다. ACM 도메인 검증에도 사용한다.
- ACM (AWS Certificate Manager) : HTTPS에 필요한 SSL/TLS 인증서를 관리하는 AWS 서비스다.

ACM 인증서에는 기본 도메인뿐 아니라 `*.example.com` 같은 wildcard 이름을 추가할 수 있다. 인증서 상태가 `발급됨`이 되어야 HTTPS Listener에서 선택할 수 있다.


#### \# Application Load Balancer와 Target Group
Load Balancer는 요청을 여러 서버로 나누어 보내는 서비스다. 서버 한 대가 장애를 일으키거나 요청이 많아질 때 여러 EC2를 대상으로 처리량과 가용성을 높이는 데 사용한다.

수업에서는 두 EC2에 nginx 정적 페이지를 배치한 뒤 Target Group과 Application Load Balancer(ALB)를 만들었다.

```shell
sudo apt install -y nginx
git clone <정적_홈페이지_저장소_URL>
cd <EC2별_홈페이지_디렉터리>
sudo cp -r ./* /var/www/html/
sudo systemctl start nginx
```

- Target Group : 요청을 전달할 EC2 인스턴스 목록을 관리한다.
- ALB Security Group : 외부에서 ALB로 들어오는 HTTP·HTTPS 요청을 허용한다.
- ALB : Listener 규칙에 따라 요청을 Target Group의 정상 인스턴스로 전달한다.

구성 순서는 다음과 같다.

Target Group 생성 -\> ALB Security Group 생성 -\> ALB 생성 -\> HTTPS Listener에 ACM 인증서 연결 -\> Route 53 A 레코드 별칭 연결 -\> 도메인 접속 확인

ALB에는 서로 다른 Availability Zone의 Subnet을 연결하고, Target Group에 여러 EC2를 등록한다. Route 53에서는 루트 도메인과 `www` 같은 별도 이름의 A 레코드를 ALB 별칭 대상으로 만들 수 있다.

HTTPS를 사용하려면 Listener 프로토콜을 HTTPS로 선택하고 ACM에서 발급된 인증서를 연결해야 한다. 인증서가 없으면 HTTPS Listener 구성 단계가 진행되지 않는다.


#### \# AWS 실습 자원 삭제 순서
AWS 실습에서 만든 자원은 서로 연결되어 있어 생성 순서의 반대로 삭제해야 한다. 연결된 자원을 남기면 삭제가 실패하거나 불필요한 비용이 발생할 수 있다.

탄력적 IP -\> EC2 인스턴스 -\> Load Balancer -\> Target Group -\> RDS -\> EC2 Security Group -\> RDS Security Group -\> VPC -\> 인증서 -\> DNS 레코드 -\> Hosted Zone

실습 종료 후에는 특히 탄력적 IP, EC2, Load Balancer, RDS처럼 비용이 발생할 수 있는 리소스가 남아 있지 않은지 확인해야 한다.


#### \# Terraform과 Infrastructure as Code
Terraform은 서버, 네트워크, 보안 그룹, 스토리지 같은 인프라를 코드로 선언하고 명령으로 생성·변경·삭제하는 IaC 도구다.

콘솔 화면에서 같은 설정을 반복하는 대신 `.tf` 파일에 원하는 상태를 적어두면, Terraform이 현재 상태와 비교해 필요한 작업을 계획하고 적용한다.

- Provider : AWS처럼 Terraform이 제어할 클라우드 서비스 연결 정보다.
- Resource : EC2, VPC, Subnet처럼 실제로 만들고 관리할 인프라 자원이다.
- Module : 비슷한 구성이나 역할을 묶어 재사용하는 단위다.
- Variable : 환경별로 달라질 값을 분리하는 입력값이다.
- HCL (HashiCorp Configuration Language) : Terraform 설정 파일에서 사용하는 선언형 언어다.

```hcl
provider "aws" {
  region = "ap-northeast-2"
}

resource "aws_instance" "myserver" {
  ami           = "ami-<image-id>"
  instance_type = "t2.micro"

  tags = {
    Name = "WebServer"
  }
}
```

Terraform의 대표 명령은 다음과 같다.

```shell
terraform init
terraform plan -out='main.plan'
terraform apply 'main.plan'
terraform destroy
```

- `terraform init` : 현재 디렉터리를 Terraform 작업 디렉터리로 초기화하고 Provider를 내려받는다.
- `terraform plan` : 실제 적용 전에 생성·변경·삭제될 Resource를 미리 확인한다.
- `terraform apply` : 설정 파일과 plan을 바탕으로 실제 클라우드 Resource를 생성·변경한다.
- `terraform destroy` : Terraform이 관리하는 Resource를 삭제한다.

`destroy`는 되돌릴 수 없는 삭제 작업이므로, 출력되는 대상과 확인 문구를 읽고 신중히 실행해야 한다.

```text
Do you really want to destroy all resources?
Terraform will destroy all your managed infrastructure, as shown above.
There is no undo. Only 'yes' will be accepted to confirm.
```


#### \# Terraform의 AWS 인증과 인프라 구성
Terraform이 AWS API를 호출하려면 IAM 사용자와 Access Key 기반의 인증 정보가 필요하다. 이 정보는 코드에 직접 고정하지 않고 환경 변수나 안전한 Secret 관리 방식으로 전달해야 한다.

수업에서 Terraform으로 구성한 대표 자원은 다음과 같다.

| 리소스 | 역할 |
| --- | --- |
| VPC | 전체 가상 네트워크 |
| Public Subnet 2개 | 서로 다른 Availability Zone의 공개 네트워크 |
| Internet Gateway | VPC와 인터넷 연결 |
| Route Table | Subnet의 외부 통신 경로 |
| Security Group | SSH·HTTP·HTTPS 등 접근 규칙 |
| EC2 | 실제 Linux 서버 |
| Elastic IP | 서버에 연결할 고정 Public IP |

Terraform 실행 파일이 어느 명령 프롬프트 위치에서도 실행되도록 하려면 `terraform.exe`가 있는 디렉터리를 운영체제 Path 환경 변수에 등록한다.

작업 디렉터리에서 초기화한 뒤, AWS 자격 증명은 현재 shell 환경에 주입하고 plan을 먼저 확인하는 순서를 사용했다.

```shell
terraform init
set AWS_ACCESS_KEY_ID={MASKED}
set AWS_SECRET_ACCESS_KEY={MASKED}
terraform plan -out='main.plan'
terraform apply 'main.plan'
```

실습 중 인스턴스 유형처럼 Cloud 계정 제약이나 정책에 맞지 않는 설정으로 오류가 나면, HCL 설정을 수정하고 다시 plan과 apply를 실행해야 한다. 콘솔에서 임시로 바꾸는 방식보다 `.tf` 파일의 선언을 수정해야 다음 실행에도 같은 상태를 재현할 수 있다.


#### \# Amazon S3 파일 업로드와 RDS 연결
S3(Simple Storage Service)는 클라우드에서 파일과 객체를 저장하는 확장 가능한 스토리지 서비스다. 이번 실습에서는 Spring Boot 서버가 로컬 `images` 폴더 대신 S3 버킷에 상품 이미지를 업로드하도록 구성했다.

전체 데이터 흐름은 다음과 같다.

사용자 파일 선택 -\> UploadController -\> S3Service -\> S3 Bucket 객체 저장 -\> ProductService -\> ProductRepository -\> RDS MySQL 상품 행 저장 -\> 결과 페이지에서 이미지 URL 사용

Spring Boot가 RDS와 S3에 연결하려면 설정 값을 분리한다.

```properties
spring.datasource.url=jdbc:mysql://<RDS_ENDPOINT>:3306/<DATABASE_NAME>
spring.datasource.username=<DB_USERNAME>
spring.datasource.password=<DB_PASSWORD>

cloud.aws.credentials.access-key=<AWS_ACCESS_KEY>
cloud.aws.credentials.secret-key=<AWS_SECRET_KEY>
cloud.aws.s3.bucket=<S3_BUCKET_NAME>
```

S3 SDK 의존성도 Maven에 추가한다.

```xml
<!-- AWS S3 SDK -->
<dependency>
  <groupId>software.amazon.awssdk</groupId>
  <artifactId>s3</artifactId>
  <version>2.25.26</version>
</dependency>
```

역할을 나누면 다음과 같다.

- `S3Service` : 버킷에 이미지 파일을 저장하는 작업을 담당한다.
- `ProductService` : 상품과 이미지 업로드라는 비즈니스 흐름을 조합한다.
- `ProductRepository` : 상품 데이터를 CRUD 방식으로 RDS에 저장·조회한다.
- `UploadController` : 업로드 화면 이동, POST 업로드 요청, 이미지 목록 조회를 처리한다.
- `upload.html` : 파일을 선택하고 submit하는 입력 화면이다.
- `result.html` : 업로드 결과와 이미지 URL을 보여주는 화면이다.

버킷 접근 정책은 필요한 Action과 Resource만 허용하도록 작성해야 한다. 수업용 정책 형태는 다음과 같지만, 실제 서비스에서는 Public 접근과 쓰기 권한의 범위를 최소화해야 한다.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::<BUCKET_NAME>/*"
    }
  ]
}
```

업로드 후에는 S3 버킷의 객체 목록과 RDS MySQL의 `product` 테이블을 함께 확인해 파일 저장과 DB 행 저장이 모두 이뤄졌는지 검증한다.

```sql
use coffee;
show tables;
select * from product;
```


#### \# 수업 전체 연결 정리
Ci&CD에서 다룬 도구와 서비스는 하나의 웹서비스 운영 흐름으로 연결된다.

- GitHub는 애플리케이션 소스와 workflow를 관리한다.
- GitHub Actions는 push를 trigger로 Maven build, Docker Image build·push, EC2 배포를 자동화한다.
- Docker Hub는 배포 가능한 Image를 저장하고 EC2가 가져오는 중간 저장소다.
- EC2는 Docker Container로 Spring Boot 애플리케이션을 실행한다.
- Route 53과 ACM은 도메인 이름과 HTTPS 인증서를 관리한다.
- ALB와 Target Group은 여러 EC2로 요청을 분산한다.
- Terraform은 AWS 인프라 구성을 코드로 재현한다.
- S3는 이미지 같은 객체 파일을 저장하고, RDS는 상품 같은 관계형 데이터를 저장한다.

이 흐름을 이해하면 "코드를 작성했다"에서 끝나지 않고, 변경한 코드를 안전하게 빌드하고 배포하며 도메인으로 서비스하고, 필요한 인프라와 데이터를 함께 관리하는 과정까지 연결해서 볼 수 있다.
