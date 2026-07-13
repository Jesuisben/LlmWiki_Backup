---
title: 2026-05-07 AWS VPC, EC2, EIP와 자원 관리
created: 2026-07-03
updated: 2026-07-13
type: summary
tags: [aws, linux, spring-boot, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/6. AWS/2026.05.07(목)/2026.05.07(목).md
  - raw/KoreaICT/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf
  - raw/KoreaICT/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf
  - raw/KoreaICT/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf
  - raw/KoreaICT/6. AWS/교육 자료/실습 관리 대장(텍스트).md
status: growing
confidence: high
---

# 2026-05-07 AWS VPC, EC2, EIP와 자원 관리

## 한 줄 요약

On-Demand 비용 관점에서 VPC와 두 public subnet, EC2·Elastic IP·SSH 접속을 실제로 구성하고, 실습 자원을 의존 순서로 해제하는 방법까지 반복한 날이다.

## 배운 내용

- On-Demand는 필요한 IT 자원을 쓰고 비용을 지불하는 방식이고, On-Premise는 장비를 직접 보유·운영하는 방식으로 비교했다.
- `EDU-VPC 10.250.0.0/16` 안에 `EDU-PUBLIC-SBN-2A 10.250.1.0/24`, `EDU-PUBLIC-SBN-2C 10.250.11.0/24`를 만들었다.
- Internet Gateway를 VPC에 연결하고, Route Table의 `0.0.0.0/0` 경로를 IGW로 보내며, 각 subnet을 Route Table에 연결했다.
- Security Group에 HTTP 80, HTTPS 443, SSH 22, Spring Boot용 TCP 9000 규칙을 넣고 Key Pair를 만들었다.
- Ubuntu AMI 기반 EC2 두 대를 각각의 subnet에 만들고 Elastic IP를 연결해 MobaXterm SSH 세션을 구성했다.
- VPC/IGW/Route Table은 subnet끼리 공유하지만 EC2·Security Group·EIP·Key Pair는 서버별로 연결한다는 관계를 확인했다.
- EIP 연결 해제·release → EC2 종료 → Security Group → VPC → Key Pair 순으로 해제하는 실습을 두 번 반복했다.

## 핵심 실습 / 예제

VPC/EC2 구성 순서는 다음처럼 정리된다.

```text
VPC 생성
→ Internet Gateway 생성/연결
→ VPC DNS hostnames 활성화
→ Subnet 생성
→ Route Table 생성 및 0.0.0.0/0 → IGW 라우팅 추가
→ Route Table과 Subnet 연결
→ Security Group 생성 및 Inbound 규칙 추가
→ Key Pair 생성
→ EC2 인스턴스 생성
→ Elastic IP 연결
→ MobaXterm SSH 접속
```

생성 흐름은 다음과 같다.

```text
VPC → IGW 연결 → DNS hostnames 활성화 → Public Subnet 2개
→ Route Table/0.0.0.0/0→IGW → Security Group → Key Pair
→ EC2 2대 → Elastic IP 연결 → MobaXterm SSH
```

Nginx·Spring Boot·RDS 연동은 다음 날 [[summaries/2026-05-08-aws-rds-resource-cleanup|2026-05-08 AWS RDS MySQL 연결과 자원 정리]]에서 실제로 수행했다.

## 왜 중요한가

이 날은 Linux에서 다룬 SSH·서버 운영을 Cloud 네트워크 위로 옮긴 기반 실습이다. 다음 날 서버·DB를 올리기 전에, 어느 AZ/Subnet에 EC2가 있고 어떤 route·Security Group·EIP를 통해 접속하는지 먼저 구성했다.

## 헷갈린 점 / 질문

- `/16`은 VPC의 큰 주소 범위이고 `/24`는 그 안에서 EC2를 둘 subnet 범위다.
- Public Subnet은 이름만으로 public이 되지 않으며 Route Table의 `0.0.0.0/0 → IGW` 경로가 필요하다.
- Public IP는 달라질 수 있고 Elastic IP는 EC2에 연결해 고정적으로 쓰는 공인 주소다.
- 연결하지 않은 EIP와 남은 EC2는 비용과 연결될 수 있으므로 실습 후 release/종료 상태를 확인한다.

## 관련 페이지

- [[concepts/aws-cloud-vpc-networking|AWS Cloud와 VPC 네트워킹]]
- [[concepts/aws-cloud-vpc-networking|AWS Cloud와 VPC 네트워킹]]
- [[concepts/aws-resource-lifecycle-cost-management|AWS 자원 생명주기와 비용 관리]]
- [[entities/amazon-ec2|Amazon EC2]]

## 출처

- `raw/KoreaICT/6. AWS/2026.05.07(목)/2026.05.07(목).md` — VPC/IGW/Route Table/SG/Key Pair/EC2/EIP/SSH와 해제 실습
