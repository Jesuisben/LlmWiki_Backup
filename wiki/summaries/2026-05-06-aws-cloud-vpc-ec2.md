---
title: 2026-05-06 AWS Cloud, VPC, EC2 입문
created: 2026-07-03
updated: 2026-07-18
type: summary
tags: [aws, linux, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/6. AWS/2026.05.06(수) - 시작/2026.05.06(수) - 시작.md
status: growing
confidence: high
---

# 2026-05-06 AWS Cloud, VPC, EC2 입문

## 한 줄 요약

Linux/Docker까지 배운 서버 실행 지식을 AWS Cloud로 옮기기 위해, AWS 메뉴 구조와 VPC·Subnet·CIDR·Security Group·EC2의 기본 의미를 잡기 시작한 날이다.

## 배운 내용

- AWS에서 자주 쓰는 메뉴를 VPC, EC2, Route 53, RDS, Certificate Manager 중심으로 훑었다. 이 날 Route 53·RDS·ACM은 메뉴 이름만 확인했다.
- VPC 메뉴에서 Subnet·Route Table·Internet Gateway·Security Group이 어디에 있는지 확인했다.
- EC2 메뉴에서 Instance·Security Group·Elastic IP·Key Pair와 Load Balancer·Target Group 항목을 확인했다. 리소스 생성 결과는 아니다.
- Subnet을 작업에 따라 네트워크를 나눈 공간으로 설명하고, IPv4의 octet·network/host 부분을 정리했다.
- Security Group은 EC2 앞의 방화벽처럼 동작하며, Inbound는 들어오는 규칙, Outbound는 나가는 규칙이다.
- IP 주소는 4개의 옥텟(octet)으로 구성되고, CIDR의 `/24`, `/16`은 앞에서 몇 비트를 네트워크 주소로 고정하는지를 나타낸다.

## 핵심 개념

| 범위 | 수업에서 잡은 의미 | 다음 날 실습과의 연결 |
|---|---|---|
| Region | 서울·도쿄처럼 AWS 자원이 놓이는 큰 지역 | 한 Region 안에서 VPC를 구성한다. |
| VPC | Region 범위의 논리적 사설 네트워크 | 05-07에 `/16` VPC를 실제 생성한다. |
| AZ | Region 안의 물리적 가용 영역 | 05-07에 서로 다른 두 AZ를 선택한다. |
| Subnet | 특정 AZ에 놓이는 VPC의 주소 구역 | 각 AZ에 `/24` public subnet을 만든다. |

Region·AZ와 On-Demand/On-Premise의 직접 설명, VPC·EC2 생성 절차는 05-07 원본에서 처음 구체화된다. 05-06 페이지는 다음 날 내용을 소급하지 않고 메뉴·네트워크 기초에만 머문다.

## 실습 / 예제

05월 06일 원본의 1~6교시는 비어 있고 7~8교시에 AWS 메뉴, Security Group, Subnet, IPv4/CIDR, 다음 날 다룰 VPC 구성 요소를 읽었다. 따라서 이 날의 완료 상태는 **메뉴·이론 사전 학습**이며 VPC·EC2 생성 결과는 아니다.

원본이 예고한 다음 날 구조는 `/16` VPC 안에 서로 다른 두 AZ의 `/24` subnet을 두고, EC2·Security Group·Elastic IP를 연결하는 형태다. 실제 생성·SSH·삭제 반복은 [[summaries/2026-05-07-aws-ec2-nginx-rds|2026-05-07]]에 귀속한다.

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
- [[summaries/2026-05-06-linux-subject-review|Linux 총정리]]
- [[summaries/2026-05-07-aws-ec2-nginx-rds|2026-05-07 AWS VPC, EC2, EIP와 자원 관리]]

## 출처

- `raw/KoreaICT/6. AWS/2026.05.06(수) - 시작/2026.05.06(수) - 시작.md` — 7~8교시 AWS 메뉴, Security Group, Subnet, IPv4/CIDR과 다음 날 예고. 문서 안의 PDF 쪽수 표기는 교안 위치를 가리키지만, 이 페이지는 날짜 MD에 전사된 범위만 사용했다.
