---
title: 2026-05-06 AWS Cloud, VPC, EC2 입문
created: 2026-07-03
updated: 2026-07-03
type: summary
tags: [aws, linux, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/6. AWS/2026.05.06(수) - 시작/2026.05.06(수) - 시작.md
  - raw/KoreaICT/6. AWS/교육 자료/AWS 기초 용어.pdf
  - raw/KoreaICT/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf
  - raw/KoreaICT/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf
  - raw/KoreaICT/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf
  - raw/KoreaICT/6. AWS/교육 자료/실습 관리 대장(텍스트).md
status: growing
confidence: high
---

# 2026-05-06 AWS Cloud, VPC, EC2 입문

## 한 줄 요약

Linux/Docker까지 배운 서버 실행 지식을 AWS Cloud로 옮기기 위해, AWS 메뉴 구조와 VPC·Subnet·CIDR·Security Group·EC2의 기본 의미를 잡기 시작한 날이다.

## 배운 내용

- AWS에서 자주 쓰는 메뉴를 VPC, EC2, Route 53, RDS, Certificate Manager 중심으로 훑었다.
- Cloud는 서버·네트워크·DB 같은 IT 자원을 필요한 만큼 빌려 쓰는 On-Demand 방식이고, On-Premise는 직접 설비를 보유·운영하는 방식으로 대비된다.
- Region은 서울/도쿄 같은 큰 물리 지역이고, 하나의 Region 안에 여러 VPC를 만들 수 있다.
- VPC는 사용자가 정의하는 가상의 Private Cloud 네트워크이고, 실습에서는 `EDU-VPC 10.250.0.0/16`을 기준으로 삼았다.
- AZ(Availability Zone)는 Region 안의 독립된 데이터센터 묶음이고, 실습에서는 2A와 2C를 주로 사용했다.
- Subnet은 VPC를 AZ와 CIDR 범위 기준으로 나눈 구역이다. 실습 구조는 2A의 `10.250.1.0/24`, 2C의 `10.250.11.0/24` public subnet으로 이어진다.
- Security Group은 EC2 앞의 방화벽처럼 동작하며, Inbound는 들어오는 규칙, Outbound는 나가는 규칙이다.
- EC2는 VirtualBox에서 VM을 만들던 경험과 연결해 이해한 AWS 가상 서버다. AMI, Key Pair, Public/Private IP, Elastic IP가 함께 등장한다.
- IP 주소는 4개의 옥텟(octet)으로 구성되고, CIDR의 `/24`, `/16`은 앞에서 몇 비트를 네트워크 주소로 고정하는지를 나타낸다.

## 핵심 개념

```text
Region
└─ VPC 10.250.0.0/16
   ├─ AZ ap-northeast-2a
   │  └─ Subnet 10.250.1.0/24
   └─ AZ ap-northeast-2c
      └─ Subnet 10.250.11.0/24
```

수업에서 쓴 수식은 “큰 AWS 공간이 점점 작은 네트워크 단위로 나뉜다”는 흐름을 표현한다.

- `Region = Σ VPC_i`: 한 Region 안에는 여러 VPC가 있을 수 있다.
- `VPC = Σ AZ_i`: VPC는 Region 범위의 논리 네트워크라 여러 AZ를 포함해 설계할 수 있다.
- `AZ = Σ Subnet_i`: 각 AZ 안에는 용도별 여러 Subnet이 존재할 수 있다.

## 실습 / 예제

05월 06일은 실제 리소스 생성 전, 다음 날 실습할 구조를 읽고 이해하는 단계였다.

```text
EDU-VPC 10.250.0.0/16
├─ EDU-PUBLIC-SBN-2A 10.250.1.0/24
│  └─ EDU-PUBLIC-EC2-2A / Private IP 10.250.1.240
├─ EDU-PUBLIC-SBN-2C 10.250.11.0/24
│  └─ EDU-PUBLIC-EC2-2C / Private IP 10.250.11.240
├─ EDU-IGW
└─ EDU-PUBLIC-RT → 0.0.0.0/0 대상 Internet Gateway
```

`실습 관리 대장(텍스트).md`는 위 이름과 CIDR, 포트 규칙을 표로 보존하고 있어 이후 실습 복원 기준이 된다.

## 왜 중요한가

이전 [[entities/linux|Linux]]와 [[entities/docker|Docker]] 수업은 “서버 안에서 명령을 실행하고 프로세스를 띄우는 법”에 가까웠다. AWS에서는 서버 자체보다 먼저 “그 서버가 어떤 네트워크 범위, 어떤 가용 영역, 어떤 방화벽 규칙 안에 놓이는가”를 이해해야 한다. 이 관점이 없으면 EC2에 Spring Boot가 정상 실행되어도 외부 접속이 되지 않는 문제를 해석하기 어렵다.

## 헷갈린 점 / 질문

- VPC는 서버가 아니라 서버들이 들어갈 네트워크 공간이다.
- Subnet은 VPC의 일부이며, 특정 AZ와 CIDR 범위에 묶인다.
- Public Subnet은 이름만 public인 것이 아니라 Internet Gateway와 Route Table 경로가 있어야 public하게 동작한다.
- Security Group의 Inbound를 열지 않으면 SSH, HTTP, HTTPS가 막힌다.
- EC2 Public IP는 재시작/재생성 흐름에서 바뀔 수 있으므로 고정 주소가 필요하면 Elastic IP를 연결한다.
- `/24`는 “24개 주소”가 아니라 앞 24비트를 네트워크 주소로 고정한다는 뜻이다.

## 관련 페이지

- [[concepts/aws-cloud-vpc-networking|AWS Cloud와 VPC 네트워킹]]
- [[entities/aws|AWS]]
- [[entities/amazon-ec2|Amazon EC2]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]

## 출처

- `raw/KoreaICT/6. AWS/2026.05.06(수) - 시작/2026.05.06(수) - 시작.md` — AWS 메뉴, Security Group, Subnet, IP/CIDR 메모
- `raw/KoreaICT/6. AWS/교육 자료/AWS 기초 용어.pdf` — On-Demand, On-Premise, AWS 기초 용어
- `raw/KoreaICT/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf` — VPC/EC2/Route 53/RDS/ACM 메뉴와 기본 구조
- `raw/KoreaICT/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf` — VPC, IGW, Route Table, Security Group, EC2 생성 흐름
- `raw/KoreaICT/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf` — IP, CIDR, Subnet, Security Group 이론
- `raw/KoreaICT/6. AWS/교육 자료/실습 관리 대장(텍스트).md` — 실습 리소스 이름과 CIDR/IP/포트 표
