---
title: Terraform과 Infrastructure as Code
created: 2026-07-03
updated: 2026-07-18
type: concept
tags: [aws, ci-cd]
sources:
  - raw/KoreaICT/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md
  - raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md
  - raw/KoreaICT/7. Ci&CD/교육 자료/cloud.02.AWS 교안(실습).pdf
  - raw/KoreaICT/7. Ci&CD/교육 자료/cloud.03.AWS 교안(이론).pdf
status: growing
confidence: high
---

# Terraform과 Infrastructure as Code

## 정의

Terraform은 VPC, Subnet, Security Group, EC2 같은 인프라를 클릭 작업이 아니라 `.tf` 코드로 선언하고 `init`, `plan`, `apply`, `destroy` 명령으로 관리하는 Infrastructure as Code 도구다.

## 왜 중요한가

CI/CD가 애플리케이션 빌드와 배포를 자동화한다면, Terraform은 그 애플리케이션이 올라갈 인프라 생성을 자동화한다. 두 흐름을 함께 이해하면 “서버를 만들고, 앱을 배포하고, 변경을 반복하는 과정”을 코드로 재현할 수 있다.

## 핵심 설명

Terraform은 HCL(HashiCorp Configuration Language)을 사용한다. 수업에서는 Windows에 Terraform을 설치하고 `Path` 환경 변수에 등록한 뒤, `main.tf`로 VPC, 서로 다른 가용 영역의 Public Subnet, Internet Gateway, Route Table, Security Group, EC2, Elastic IP 같은 AWS 리소스를 선언하는 흐름을 다뤘다.

원본의 짧은 HCL block은 provider와 resource 문법 예시다. 실제 실습은 별도로 받은 `main.tf`를 사용했으므로 예시 block을 적용된 전체 infrastructure code로 확대하지 않는다.

## 기본 명령

| 명령 | 의미 |
|---|---|
| `terraform init` | 작업 디렉터리 초기화, provider 다운로드 |
| `terraform plan` | 생성/변경/삭제될 리소스를 미리 확인 |
| `terraform apply` | 선언한 인프라를 실제 클라우드에 적용 |
| `terraform destroy` | Terraform이 관리하는 리소스 삭제 |

## 05-13 실행 증거

- `terraform -v` 출력은 설치 직후와 Path 등록 뒤 각각 보존되어 Windows 어디서나 CLI가 실행되는 상태를 확인할 수 있다.
- `terraform init`은 명령과 생성될 `.terraform`·lock file 설명이 있지만 실제 init log는 없다.
- 첫 apply는 account 제약과 instance type 문제로 오류가 났다고 기록되어 있다. 설정을 수정해 다시 plan/apply하는 절차는 있으나 최종 apply 성공 출력은 없다.
- `terraform destroy`는 확인 prompt 일부만 남아 있고 삭제 완료 출력은 없다.

## 자주 헷갈리는 점

- Terraform은 Spring Boot 코드를 배포하는 도구가 아니라 AWS 리소스를 만드는 도구다.
- `plan`은 실제 생성 전 미리보기이고, `apply`가 실제 변경이다.
- `destroy`는 리소스를 삭제하므로 비용 정리에는 유용하지만 운영 환경에서는 매우 위험하다.
- AWS access key와 secret key는 원본에 있더라도 코드/wiki에 남기지 않는다. 수업에서는 shell 환경 변수로 주입했지만, 실제 프로젝트에서는 더 안전한 Secret 관리 방식을 선택해야 한다.

## 관련 개념

- [[summaries/2026-05-13-terraform-s3-file-upload|2026-05-13 Terraform과 S3 파일 업로드]]
- [[concepts/ci-cd-automation|CI/CD 자동화]]
- [[concepts/aws-cloud-vpc-networking|AWS Cloud와 VPC 네트워킹]]
- [[entities/aws|AWS]]

## 출처

- `raw/KoreaICT/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md`
- `raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md`
- `raw/KoreaICT/7. Ci&CD/교육 자료/cloud.02.AWS 교안(실습).pdf`
- `raw/KoreaICT/7. Ci&CD/교육 자료/cloud.03.AWS 교안(이론).pdf`
