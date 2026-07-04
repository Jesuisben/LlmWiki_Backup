---
title: Terraform과 Infrastructure as Code
created: 2026-07-03
updated: 2026-07-03
type: concept
tags: [aws, ci-cd]
sources:
  - raw/Study/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md
  - raw/Study/7. Ci&CD/교육 자료/cloud.02.AWS 교안(실습).pdf
  - raw/Study/7. Ci&CD/교육 자료/cloud.03.AWS 교안(이론).pdf
status: seed
confidence: high
---

# Terraform과 Infrastructure as Code

## 정의

Terraform은 VPC, Subnet, Security Group, EC2 같은 인프라를 클릭 작업이 아니라 `.tf` 코드로 선언하고 `init`, `plan`, `apply`, `destroy` 명령으로 관리하는 Infrastructure as Code 도구다.

## 왜 중요한가

CI/CD가 애플리케이션 빌드와 배포를 자동화한다면, Terraform은 그 애플리케이션이 올라갈 인프라 생성을 자동화한다. 두 흐름을 함께 이해하면 “서버를 만들고, 앱을 배포하고, 변경을 반복하는 과정”을 코드로 재현할 수 있다.

## 핵심 설명

Terraform은 HCL(HashiCorp Configuration Language)을 사용한다. 수업에서는 Windows에 Terraform을 설치하고 `Path` 환경 변수에 등록한 뒤, `main.tf`로 AWS 리소스를 선언하는 흐름을 다뤘다.

```hcl
provider "aws" {
  region = "ap-northeast-2"
}

resource "aws_instance" "myserver" {
  ami           = "ami-..."
  instance_type = "t3.micro"
}
```

## 기본 명령

| 명령 | 의미 |
|---|---|
| `terraform init` | 작업 디렉터리 초기화, provider 다운로드 |
| `terraform plan` | 생성/변경/삭제될 리소스를 미리 확인 |
| `terraform apply` | 선언한 인프라를 실제 클라우드에 적용 |
| `terraform destroy` | Terraform이 관리하는 리소스 삭제 |

## 자주 헷갈리는 점

- Terraform은 Spring Boot 코드를 배포하는 도구가 아니라 AWS 리소스를 만드는 도구다.
- `plan`은 실제 생성 전 미리보기이고, `apply`가 실제 변경이다.
- `destroy`는 리소스를 삭제하므로 비용 정리에는 유용하지만 운영 환경에서는 매우 위험하다.
- AWS access key와 secret key는 원본에 있더라도 코드/wiki에 남기지 않는다.

## 관련 개념

- [[summaries/2026-05-13-terraform-s3-file-upload|2026-05-13 Terraform과 S3 파일 업로드]]
- [[concepts/ci-cd-automation|CI/CD 자동화]]
- [[concepts/aws-cloud-vpc-networking|AWS Cloud와 VPC 네트워킹]]
- [[entities/aws|AWS]]

## 출처

- `raw/Study/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md`
- `raw/Study/7. Ci&CD/교육 자료/cloud.02.AWS 교안(실습).pdf`
- `raw/Study/7. Ci&CD/교육 자료/cloud.03.AWS 교안(이론).pdf`
