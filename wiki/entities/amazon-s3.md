---
title: Amazon S3
created: 2026-07-03
updated: 2026-07-18
type: entity
tags: [aws]
sources:
  - raw/KoreaICT/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md
  - raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md
  - raw/KoreaICT/7. Ci&CD/교육 자료/cloud.02.AWS 교안(실습).pdf
status: growing
confidence: high
---

# Amazon S3

## 무엇인가

Amazon S3(Simple Storage Service)는 AWS의 객체 스토리지 서비스다. 수업에서는 Spring Boot 상품 이미지 업로드 파일을 서버 로컬 폴더가 아니라 클라우드 bucket에 저장하기 위해 사용했다.

## 이 위키에서의 맥락

AWS 과정에서는 EC2가 애플리케이션 서버, RDS가 DB 서버 역할을 맡았다. Ci&CD 과정의 2026-05-13 수업에서는 여기에 파일 저장소로 S3가 추가되었다. 이로써 Spring Boot 서비스는 다음처럼 책임을 나눌 수 있다.

EC2는 Spring Boot/Docker container 실행, RDS는 상품·회원·주문 같은 구조화 데이터, S3는 이미지·첨부 파일 같은 object 저장을 맡는다. 이 책임 분리는 서비스별 역할 설명이며, 05-13에는 S3 upload 재시도 성공과 bucket object 확인이 수업 메모의 실행 관찰로 남아 있다. listing·API 응답·화면은 보존되지 않았다.

## 핵심 기능 / 특징

- Bucket이라는 저장 공간에 object를 저장한다.
- Object는 key와 URL을 통해 참조할 수 있다.
- IAM user/role과 bucket policy로 접근 권한을 제어한다.
- Spring Boot에서는 AWS SDK를 이용해 파일을 업로드할 수 있다.

## 학습 이력

- [[summaries/2026-05-13-terraform-s3-file-upload|2026-05-13]]: bucket·IAM·Spring Boot `S3Service`·`UploadController`·RDS 상품 데이터 역할을 연결했다. 첫 upload 실패와 policy 수정 뒤 재시도 성공·bucket object 확인은 관찰 서술로 기록됐고, S3 1차 결과와 RDS query 결과는 미보존이다.

## 프로젝트/면접 관점

S3는 “파일 저장을 애플리케이션 서버에서 분리하는 스토리지”라고 설명할 수 있다. 서버가 여러 대거나 Docker container가 재생성되는 구조에서는 로컬 폴더보다 S3 같은 외부 스토리지가 더 안정적이다. 단, public bucket 설정은 보안 위험이 있으므로 실제 서비스에서는 IAM 권한, bucket policy, presigned URL, CloudFront 연동을 함께 고려해야 한다.

## 관련 개념

- [[concepts/aws-s3-file-upload|AWS S3 파일 업로드 흐름]]
- [[entities/aws|AWS]]
- [[entities/amazon-rds|Amazon RDS]]
- [[entities/amazon-ec2|Amazon EC2]]
- [[concepts/aws-rds-spring-boot|AWS RDS와 Spring Boot 연결]]

## 출처

- `raw/KoreaICT/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md`
- `raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md`
- `raw/KoreaICT/7. Ci&CD/교육 자료/cloud.02.AWS 교안(실습).pdf`
