---
title: AWS S3 파일 업로드 흐름
created: 2026-07-03
updated: 2026-07-18
type: concept
tags: [aws, spring-boot, backend]
sources:
  - raw/KoreaICT/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md
  - raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md
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

사용자가 `upload.html`에서 파일을 제출하면 `UploadController`가 요청을 받고 `S3Service`가 AWS SDK로 bucket object 저장을 담당한다. `ProductService`와 `ProductRepository`는 상품 정보와 이미지 주소를 RDS에 저장하는 역할로 설명되었다. 날짜 원본에는 실제 Java method 본문과 RDS insert 결과가 없어 이 역할 설명을 완성된 end-to-end 코드 실행으로 확대하지 않는다.

## 핵심 구성 요소

| 구성 | 역할 |
|---|---|
| S3 bucket | 이미지 파일이 저장되는 클라우드 스토리지 공간 |
| IAM user/access key | Spring Boot 코드가 S3 API를 호출하기 위한 권한 정보 |
| AWS SDK S3 dependency | Java 코드에서 S3 API를 호출하게 해 주는 라이브러리 |
| `S3Service` | 실제 업로드 담당 서비스 |
| `UploadController` | 업로드 화면 이동, POST 처리, 목록 조회 담당 |
| RDS/MySQL | 파일 자체가 아니라 상품 행과 이미지 URL/key 저장 |

## Spring Boot 설정 책임

날짜 원본은 RDS datasource URL·username·password와 S3 access key·secret key·bucket 이름을 `application.properties`에 두는 수업용 설정을 기록한다. 위키에는 실제 endpoint·account·credential·bucket 이름을 옮기지 않는다. 이 설정은 연결에 필요한 입력일 뿐, 설정 작성만으로 DB나 S3 연결 성공이 증명되지는 않는다.

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
- DB에 이미지 binary 자체를 넣는 것이 아니라, 보통 S3 object URL/key를 저장한다. 수업의 검증도 bucket 객체 목록과 RDS `product` table을 함께 확인하는 방식이었다.
- bucket public access를 열면 실습은 쉽지만 보안상 위험하다. 실제 서비스는 IAM 권한, bucket policy, presigned URL, CloudFront 같은 선택지를 검토해야 한다.
- access key와 secret key는 password와 같은 민감값이다. GitHub, wiki, 코드 저장소에 그대로 남기지 않는다.

## 05-13 결과 경계

- 첫 image upload는 실패했다고 수업 메모에 명시되어 있지만 오류 응답·화면은 없다.
- bucket policy를 편집한 뒤 재시도 성공과 bucket object 확인이 수업 메모에 기록되어 있다. 이는 실행 관찰 서술이며 listing·API 응답·screenshot 같은 1차 결과는 미보존이다.
- MySQL Workbench 연결 설정과 `product` 조회 SQL은 있지만 query 결과 행은 없어 RDS 상품 저장 성공은 확정하지 않는다.

## 관련 개념

- [[summaries/2026-05-13-terraform-s3-file-upload|2026-05-13 Terraform과 S3 파일 업로드]]
- [[entities/amazon-s3|Amazon S3]]
- [[concepts/aws-rds-spring-boot|AWS RDS와 Spring Boot 연결]]
- [[concepts/spring-boot-cicd-docker-ec2-flow|Spring Boot CI/CD Docker-EC2 배포 흐름]]
- [[entities/spring-boot|Spring Boot]]

## 출처

- `raw/KoreaICT/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md`
- `raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md`
- `raw/KoreaICT/7. Ci&CD/교육 자료/cloud.02.AWS 교안(실습).pdf`
