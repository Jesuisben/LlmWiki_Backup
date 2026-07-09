---
title: AWS S3 파일 업로드 흐름
created: 2026-07-03
updated: 2026-07-03
type: concept
tags: [aws, spring-boot, backend]
sources:
  - raw/KoreaICT/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md
  - raw/KoreaICT/7. Ci&CD/교육 자료/cloud.02.AWS 교안(실습).pdf
status: growing
confidence: high
---

# AWS S3 파일 업로드 흐름

## 정의

AWS S3 파일 업로드 흐름은 사용자가 업로드한 이미지나 파일을 Spring Boot 서버 로컬 폴더에 저장하지 않고, Amazon S3 bucket에 저장한 뒤 DB에는 파일 URL 또는 object key를 저장하는 구조다.

## 왜 중요한가

로컬 개발에서는 `shop/images` 같은 폴더에 이미지를 둘 수 있다. 하지만 클라우드/컨테이너 배포에서는 서버가 여러 대가 되거나 컨테이너가 재생성될 수 있어 로컬 파일 저장이 불안정하다. S3를 사용하면 파일 저장소를 애플리케이션 서버와 분리할 수 있다.

## 수업에서의 흐름

```text
사용자
  ↓ 파일 선택/제출
upload.html
  ↓ POST upload
UploadController
  ↓
S3Service
  ↓ AWS SDK for Java
Amazon S3 bucket
  ↓ image URL/key 반환
ProductService
  ↓
RDS MySQL product table에 상품 정보 + image_url 저장
```

## 핵심 구성 요소

| 구성 | 역할 |
|---|---|
| S3 bucket | 이미지 파일이 저장되는 클라우드 스토리지 공간 |
| IAM user/access key | Spring Boot 코드가 S3 API를 호출하기 위한 권한 정보 |
| AWS SDK S3 dependency | Java 코드에서 S3 API를 호출하게 해 주는 라이브러리 |
| `S3Service` | 실제 업로드 담당 서비스 |
| `UploadController` | 업로드 화면 이동, POST 처리, 목록 조회 담당 |
| RDS/MySQL | 파일 자체가 아니라 상품 정보와 이미지 URL/key 저장 |

## Spring Boot 설정 예시

실제 값은 코드 저장소에 직접 쓰지 않는 것이 안전하다. 수업 원본에는 학습용 예시가 있었지만, 위키에서는 placeholder로 일반화한다.

```properties
spring.datasource.url=jdbc:mysql://<RDS_ENDPOINT>:3306/<DB_NAME>
spring.datasource.username=<DB_USER>
spring.datasource.password=<DB_PASSWORD>

cloud.aws.credentials.access-key=<AWS_ACCESS_KEY_ID>
cloud.aws.credentials.secret-key=<AWS_SECRET_ACCESS_KEY>
cloud.aws.s3.bucket=<S3_BUCKET_NAME>
```

AWS SDK 의존성 예시는 다음과 같다.

```xml
<dependency>
  <groupId>software.amazon.awssdk</groupId>
  <artifactId>s3</artifactId>
  <version>2.25.26</version>
</dependency>
```

## 자주 헷갈리는 점

- S3 bucket과 RDS는 역할이 다르다. S3는 파일 저장소, RDS는 구조화된 데이터 저장소다.
- DB에 이미지 binary 자체를 넣는 것이 아니라, 보통 S3 object URL/key를 저장한다.
- bucket public access를 열면 실습은 쉽지만 보안상 위험하다. 실제 서비스는 IAM 권한, bucket policy, presigned URL, CloudFront 같은 선택지를 검토해야 한다.
- access key와 secret key는 password와 같은 민감값이다. GitHub, wiki, 코드 저장소에 그대로 남기지 않는다.

## 관련 개념

- [[summaries/2026-05-13-terraform-s3-file-upload|2026-05-13 Terraform과 S3 파일 업로드]]
- [[entities/amazon-s3|Amazon S3]]
- [[concepts/aws-rds-spring-boot|AWS RDS와 Spring Boot 연결]]
- [[concepts/spring-boot-cicd-docker-ec2-flow|Spring Boot CI/CD Docker-EC2 배포 흐름]]
- [[entities/spring-boot|Spring Boot]]

## 출처

- `raw/KoreaICT/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md`
- `raw/KoreaICT/7. Ci&CD/교육 자료/cloud.02.AWS 교안(실습).pdf`
