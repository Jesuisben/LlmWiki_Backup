---
title: AWS Cloud와 VPC 네트워킹
created: 2026-07-03
updated: 2026-07-03
type: concept
tags: [aws, backend]
sources:
  - raw/KoreaICT/6. AWS/2026.05.06(수) - 시작/2026.05.06(수) - 시작.md
  - raw/KoreaICT/6. AWS/2026.05.07(목)/2026.05.07(목).md
  - raw/KoreaICT/6. AWS/교육 자료/AWS 기초 용어.pdf
  - raw/KoreaICT/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf
  - raw/KoreaICT/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf
  - raw/KoreaICT/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf
  - raw/KoreaICT/6. AWS/교육 자료/실습 관리 대장(텍스트).md
status: growing
confidence: high
---

# AWS Cloud와 VPC 네트워킹

## 정의

AWS Cloud와 VPC 네트워킹은 AWS 안에 사용자가 통제하는 사설 네트워크 공간을 만들고, 그 안에 Subnet, Route Table, Internet Gateway, Security Group, EC2를 배치해 외부 접속과 내부 통신을 설계하는 과정이다.

## 수업에서의 등장 맥락

Linux와 Docker 수업에서는 “서버 안에서 무엇을 실행할지”가 중심이었다. AWS 수업에서는 “그 서버가 어느 Region/AZ/VPC/Subnet에 놓이고, 어떤 route와 security rule을 통해 외부와 통신하는지”가 중심이 됐다. 2026-05-06에는 메뉴·용어·IP/CIDR을 먼저 정리했고, 2026-05-07에는 `EDU-VPC`와 두 public subnet을 실제로 만들었다.

## 핵심 구성요소

| 구성요소 | 수업 기준 역할 | 예시 |
|---|---|---|
| Region | AWS 서비스가 위치한 큰 지역 | 서울 리전 |
| AZ | Region 안의 독립 데이터센터 묶음 | ap-northeast-2a, ap-northeast-2c |
| VPC | AWS 안의 사설 네트워크 | `EDU-VPC 10.250.0.0/16` |
| Subnet | VPC를 IP 범위와 AZ별로 나눈 구역 | `10.250.1.0/24`, `10.250.11.0/24` |
| Internet Gateway | VPC와 인터넷을 연결하는 출입구 | `EDU-IGW` |
| Route Table | 목적지별 다음 경로를 정하는 표 | `0.0.0.0/0 → IGW` |
| Security Group | EC2 단위 stateful 방화벽 | 22, 80, 443, 9000, ICMP 허용 |
| Elastic IP | EC2에 붙이는 고정 공인 IP | Public-2A-EIP, Public-2C-EIP |

## 예시 구조

```text
EDU-VPC 10.250.0.0/16
├─ EDU-PUBLIC-SBN-2A 10.250.1.0/24
│  └─ EDU-PUBLIC-EC2-2A 10.250.1.240
├─ EDU-PUBLIC-SBN-2C 10.250.11.0/24
│  └─ EDU-PUBLIC-EC2-2C 10.250.11.240
├─ EDU-IGW
└─ EDU-PUBLIC-RT
   └─ 0.0.0.0/0 → EDU-IGW
```

## CIDR 이해

`10.250.0.0/16`에서 `/16`은 앞 16비트가 네트워크 주소라는 뜻이다. `10.250.1.0/24`에서 `/24`는 앞 24비트를 네트워크 주소로 쓰므로, 그 subnet 안에서 host 주소를 더 촘촘하게 나눈다. 수업에서는 `/16` VPC 안에 `/24` subnet들을 만들어 “큰 주소 공간을 용도/AZ별 구역으로 자르는” 흐름을 익혔다.

## 왜 중요한가

배포 장애는 코드 문제가 아니라 네트워크 설정 문제에서 자주 나온다. Spring Boot가 정상 실행 중이어도 Security Group에서 80/443/9000이 닫혀 있거나, Route Table이 Internet Gateway를 보지 않거나, RDS 3306 접근이 막혀 있으면 외부 접속 또는 DB 연결이 실패한다.

## 자주 헷갈리는 점

- VPC CIDR(`/16`)은 전체 주소 공간이고, Subnet CIDR(`/24`)은 그 일부다.
- Public Subnet은 이름만 public인 것이 아니라 `0.0.0.0/0 → Internet Gateway` route가 있어야 한다.
- Security Group은 EC2 또는 Load Balancer에 붙는 stateful 방화벽이고, Inbound/Outbound 규칙을 따로 본다.
- `ping`은 HTTP/SSH와 다른 ICMP 트래픽이다. 22/80/443을 열어도 ICMP를 허용하지 않으면 ping은 실패할 수 있다.
- SSH 접속은 22번, HTTP는 80번, HTTPS는 443번, Spring Boot 실습은 9000번, MySQL은 3306번 포트가 주로 등장했다.

## 관련 개념

- [[summaries/2026-05-06-aws-cloud-vpc-ec2|2026-05-06 AWS Cloud, VPC, EC2 입문]]
- [[summaries/2026-05-07-aws-ec2-nginx-rds|2026-05-07 AWS EC2, Nginx, Spring Boot, RDS 연결]]
- [[entities/aws|AWS]]
- [[entities/amazon-ec2|Amazon EC2]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]

## 출처

- `raw/KoreaICT/6. AWS/2026.05.06(수) - 시작/2026.05.06(수) - 시작.md`
- `raw/KoreaICT/6. AWS/2026.05.07(목)/2026.05.07(목).md`
- `raw/KoreaICT/6. AWS/교육 자료/AWS 기초 용어.pdf`
- `raw/KoreaICT/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf`
- `raw/KoreaICT/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf`
- `raw/KoreaICT/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf`
- `raw/KoreaICT/6. AWS/교육 자료/실습 관리 대장(텍스트).md`
