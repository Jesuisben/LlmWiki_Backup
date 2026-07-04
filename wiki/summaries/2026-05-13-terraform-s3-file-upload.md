---
title: 2026-05-13 Terraform과 S3 파일 업로드
created: 2026-07-03
updated: 2026-07-03
type: summary
tags: [aws, ci-cd, spring-boot, backend, curriculum]
sources:
  - raw/Study/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md
  - raw/Study/7. Ci&CD/교육 자료/cloud.02.AWS 교안(실습).pdf
  - raw/Study/7. Ci&CD/교육 자료/cloud.03.AWS 교안(이론).pdf
status: growing
confidence: high
---

# 2026-05-13 Terraform과 S3 파일 업로드

## 한 줄 요약

Terraform으로 AWS 인프라를 코드화하는 관점을 배우고, Spring Boot에서 상품 이미지를 로컬 폴더가 아니라 Amazon S3 bucket에 업로드하는 구조를 실습한 날이다.

## 커리큘럼 위치

이 수업은 CI/CD와 AWS 배포의 “운영 자동화” 관점을 넓힌다. [[summaries/2026-05-11-cicd-github-actions-spring-boot|05-11]]이 애플리케이션 빌드/배포 자동화라면, 05-13의 Terraform은 VPC/Subnet/EC2 같은 인프라를 코드로 만들고 지우는 IaC 방향이다. 또한 S3 파일 업로드는 중간 프로젝트에서 상품 이미지나 첨부 파일을 서버 로컬 디스크가 아니라 클라우드 스토리지로 분리하는 흐름과 연결된다.

## 배운 내용

### 1. Terraform과 HCL

Terraform은 인프라를 문서/코드로 작성해 명령어로 생성·변경·삭제할 수 있게 하는 IaC(Infrastructure as Code) 도구다. 수업에서는 Windows에 Terraform을 설치하고 `Path` 환경 변수에 `D:\terraform`을 등록해 어디서나 `terraform -v`를 실행할 수 있게 했다.

Terraform 구성은 provider, resource, module, variable 같은 요소로 나뉘며, HCL(HashiCorp Configuration Language)이라는 선언적 문법을 사용한다.

```hcl
provider "aws" {
  region = "ap-northeast-2"
}

resource "aws_instance" "myserver" {
  ami           = "ami-..."
  instance_type = "t3.micro"
}
```

### 2. Terraform 기본 명령

- `terraform init`: 작업 디렉터리 초기화와 provider 다운로드.
- `terraform plan`: 어떤 리소스가 생성/변경/삭제될지 사전 확인.
- `terraform apply`: plan 또는 설정 파일을 바탕으로 실제 리소스 생성.
- `terraform destroy`: Terraform이 관리하는 리소스 삭제.

원본에는 IAM access key와 secret key 예시가 포함되어 있으나, 위키에는 실제 값을 보존하지 않는다. Terraform/AWS 자동화에서는 이런 자격 증명을 환경 변수나 안전한 secret 저장소로 분리해야 한다.

### 3. S3 bucket과 Spring Boot 파일 업로드

클라우드 환경에서는 상품 이미지를 `shop/images` 같은 서버 로컬 폴더에만 두기 어렵다. 서버가 바뀌거나 컨테이너가 재생성되면 로컬 파일이 사라지거나 서버별로 달라질 수 있기 때문이다. 그래서 이미지 저장소 역할로 [[entities/amazon-s3|Amazon S3]] bucket을 사용한다.

실습 흐름은 다음과 같다.

```text
사용자 upload.html
  ↓ multipart/form-data
UploadController
  ↓ 파일 저장 요청
S3Service
  ↓ AWS SDK
Amazon S3 bucket
  ↓ public/object URL
ProductService
  ↓ image_url 저장
RDS MySQL product table
```

### 4. Spring Boot 구성 요소

- `S3Service`: bucket에 이미지 파일을 업로드하는 서비스.
- `ProductService`: S3 업로드 결과 URL과 상품 정보를 함께 DB에 저장.
- `ProductRepository`: 상품 CRUD 담당.
- `UploadController`: 업로드 화면 이동, 이미지 업로드 POST, 이미지 목록 조회 담당.
- `upload.html`: 파일 선택과 제출 화면.
- `result.html`: 업로드 결과와 이미지 URL 확인 화면.

`pom.xml`에는 AWS SDK S3 의존성이 필요하다.

```xml
<dependency>
  <groupId>software.amazon.awssdk</groupId>
  <artifactId>s3</artifactId>
  <version>2.25.26</version>
</dependency>
```

## 실습 / 예제

1. Terraform 설치 후 `Path` 등록과 버전 확인.
2. IAM 사용자와 access key를 준비해 Terraform이 AWS API를 호출할 수 있게 함.
3. `main.tf`로 VPC/Subnet/IGW/Route Table/Security Group/EC2/EIP를 선언.
4. `terraform init`, `terraform plan`, `terraform apply`로 리소스 생성.
5. S3 bucket 생성과 IAM 사용자 권한 설정.
6. Spring Boot `application.properties`에 RDS/S3 설정 추가. 실제 값은 코드 저장소에 직접 넣지 않는 것이 안전하다.
7. S3 bucket policy를 조정해 업로드와 조회를 테스트.
8. MySQL Workbench에서 `product` table의 `image_url` 저장 결과 확인.

## 헷갈린 점 / 질문

- Terraform은 애플리케이션 배포 도구라기보다 인프라 생성/관리 도구다. GitHub Actions와 함께 쓰면 인프라와 애플리케이션 배포 자동화를 각각 코드화할 수 있다.
- S3 bucket을 public으로 열면 실습은 편하지만 보안 위험이 있다. 실제 서비스에서는 공개 범위, presigned URL, IAM 권한을 별도로 설계해야 한다.
- 이미지 파일 자체는 S3에 저장되고, DB에는 파일 URL이나 key를 저장하는 구조로 이해하는 것이 좋다.
- 원본에는 AWS access key, RDS password 같은 민감값 예시가 있으므로 wiki에는 구조만 남기고 값은 일반화한다.

## 관련 페이지

- [[concepts/aws-s3-file-upload|AWS S3 파일 업로드 흐름]]
- [[entities/amazon-s3|Amazon S3]]
- [[concepts/aws-rds-spring-boot|AWS RDS와 Spring Boot 연결]]
- [[concepts/spring-boot-cicd-docker-ec2-flow|Spring Boot CI/CD Docker-EC2 배포 흐름]]
- [[concepts/middle-project-cicd-deploy-flow|중간 프로젝트 CI/CD 배포 흐름]]
- [[entities/spring-boot|Spring Boot]]

## 출처

- `raw/Study/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md`
- `raw/Study/7. Ci&CD/교육 자료/cloud.02.AWS 교안(실습).pdf`
- `raw/Study/7. Ci&CD/교육 자료/cloud.03.AWS 교안(이론).pdf`
