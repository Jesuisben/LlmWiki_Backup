---
title: 2026-05-07 AWS VPC, EC2, EIP와 자원 관리
created: 2026-07-03
updated: 2026-07-18
type: summary
tags: [aws, linux, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/6. AWS/2026.05.07(목)/2026.05.07(목).md
status: growing
confidence: high
---

# 2026-05-07 AWS VPC, EC2, EIP와 자원 관리

## 한 줄 요약

On-Demand 비용 관점에서 VPC와 두 public subnet, EC2·Elastic IP·SSH 접속을 실제로 구성하고, 실습 자원을 의존 순서로 해제하는 방법까지 반복한 날이다.

## 배운 내용

- On-Demand는 필요한 IT 자원을 쓰고 비용을 지불하는 방식이고, On-Premise는 장비를 직접 보유·운영하는 방식으로 비교했다.
- `/16` VPC 안에 서로 다른 두 AZ의 `/24` public subnet을 만들었다. 실제 수업 resource 이름과 IP 대역은 위키에 재노출하지 않는다.
- Internet Gateway를 VPC에 연결하고, Route Table의 `0.0.0.0/0` 경로를 IGW로 보내며, 각 subnet을 Route Table에 연결했다.
- Security Group에 HTTP 80, HTTPS 443, SSH 22, Spring Boot용 TCP 9000 규칙을 넣고 Key Pair를 만들었다.
- Ubuntu AMI 기반 EC2 두 대를 각각의 subnet에 만들고 Elastic IP를 연결해 MobaXterm SSH 세션을 구성했다.
- VPC/IGW/Route Table은 subnet끼리 공유하지만 EC2·Security Group·EIP·Key Pair는 서버별로 연결한다는 관계를 확인했다.
- EIP 연결 해제·release → EC2 종료 → Security Group → VPC → Key Pair 순의 해제 절차를 배웠다. 5~8교시에는 같은 구성·삭제 과정을 두 번 혼자 실습하라는 지시가 반복되지만, 반복별 성공 출력은 남아 있지 않다.

## 핵심 실습 / 예제

| 단계 | 만든·연결한 자원 | 확인 기준 |
|---:|---|---|
| 1 | VPC와 Internet Gateway | IGW 상태가 VPC에 `Attached` |
| 2 | DNS hostnames, 서로 다른 두 AZ의 Subnet | AZ와 CIDR이 계획과 일치 |
| 3 | Route Table과 `0.0.0.0/0 → IGW` | 두 Subnet이 Route Table에 연결 |
| 4 | EC2용 Security Group | 22·80·443·9000 Inbound 규칙 |
| 5 | Key Pair, Ubuntu EC2 두 대 | VPC·Subnet·Private IP·SG 선택 확인 |
| 6 | 각 EC2의 Elastic IP와 MobaXterm 세션 | EIP가 인스턴스에 연결되고 SSH 세션 생성 |
| 7 | EIP·EC2·SG·VPC·Key Pair 정리 | 절차는 기록됐지만 반복별 최종 상태 출력은 미보존 |

Nginx·Spring Boot·RDS 연동은 다음 날 [[summaries/2026-05-08-aws-rds-resource-cleanup|2026-05-08 AWS RDS MySQL 연결과 자원 정리]]에서 실제로 수행했다.

## 왜 중요한가

이 날은 Linux에서 다룬 SSH·서버 운영을 Cloud 네트워크 위로 옮긴 기반 실습이다. 다음 날 서버·DB를 올리기 전에, 어느 AZ/Subnet에 EC2가 있고 어떤 route·Security Group·EIP를 통해 접속하는지 먼저 구성했다.

## 헷갈린 점 / 질문

- `/16`은 VPC의 큰 주소 범위이고 `/24`는 그 안에서 EC2를 둘 subnet 범위다.
- Public Subnet은 이름만으로 public이 되지 않으며 Route Table의 `0.0.0.0/0 → IGW` 경로가 필요하다.
- Public IP는 달라질 수 있고 Elastic IP는 EC2에 연결해 고정적으로 쓰는 공인 주소다.
- 연결하지 않은 EIP와 남은 EC2는 비용과 연결될 수 있으므로 실습 후 release/종료 상태를 확인한다.

## 관련 페이지

- [[summaries/2026-05-06-aws-cloud-vpc-ec2|2026-05-06 AWS Cloud, VPC, EC2 입문]]
- [[concepts/aws-cloud-vpc-networking|AWS Cloud와 VPC 네트워킹]]
- [[concepts/aws-resource-lifecycle-cost-management|AWS 자원 생명주기와 비용 관리]]
- [[entities/amazon-ec2|Amazon EC2]]
- [[comparisons/virtual-machine-vs-docker-container|가상 머신(VM) vs Docker 컨테이너]]
- [[summaries/2026-05-08-aws-rds-resource-cleanup|2026-05-08 AWS RDS MySQL 연결과 자원 정리]]

## 출처

- `raw/KoreaICT/6. AWS/2026.05.07(목)/2026.05.07(목).md` — VPC/IGW/Route Table/SG/Key Pair/EC2/EIP/SSH와 해제 실습
