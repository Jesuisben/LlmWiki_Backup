---
title: 2026-05-08 AWS RDS MySQL 연결과 자원 정리
created: 2026-07-03
updated: 2026-07-18
type: summary
tags: [aws, linux, spring-boot, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md
  - raw/KoreaICT/6. AWS/AWS 총정리/AWS 총정리.md
status: growing
confidence: high
---

# 2026-05-08 AWS RDS MySQL 연결과 자원 정리

## 한 줄 요약

두 EC2의 `ping` 실패를 Security Group의 ICMP 규칙으로 해결한 뒤, Nginx·Spring Boot·RDS MySQL 연결 절차를 수행하고 결과가 보존된 단계와 명령만 남은 단계를 구분해 배운 날이다.

## 배운 내용

- 두 EC2 사이 `ping`은 처음 실패했고, 두 Security Group에 모든 ICMP IPv4 인바운드 규칙을 추가한 뒤 성공했다.
- 두 EC2에 Nginx를 설치하고 Git 저장소의 서로 다른 정적 페이지를 `/var/www/html/`에 배치하는 명령을 기록했다. 브라우저 확인 칸은 비어 있어 화면 성공은 확정하지 않는다.
- Nginx를 중지한 뒤 JDK 17·Maven 설치, Spring Boot 빌드와 jar 실행 명령을 기록했다. 패키지·프로세스·브라우저 결과는 원본에 보존되지 않았다.
- 실습에서는 `iptables`로 외부 80번 요청을 Spring Boot 9000번 포트로 redirect했다.
- RDS MySQL 생성 설정, EC2 연결 설정, `mysql-client` 접속 명령, 수업용 상품 테이블과 샘플 데이터 SQL을 기록했다. 상태가 `사용 가능`이어야 한다는 완료 조건은 있지만 실제 상태·조회 출력은 없다.
- `application.properties`의 DB 호스트를 `localhost`에서 RDS endpoint로 바꾸는 수정 절차와 “두 EC2가 하나의 DB를 공유한다”는 수업 결론이 있다. 변경 뒤 애플리케이션 응답은 미보존이다.
- 도메인 등록은 다음 단계 준비로만 언급됐고, Route 53/ACM/ALB 실습은 이 날짜 원본에 없다. 해당 실제 실습은 [[summaries/2026-05-12-route53-alb-https-review|2026-05-12 CI/CD Route 53, ALB, HTTPS]]에서 다룬다.

## 핵심 실습 / 예제

| 실습 단계 | 원본에 남은 증거 | 판정 |
|---|---|---|
| EC2 상호 `ping` | ICMP 추가 전 `100% packet loss`, 추가 후 양방향 `0% packet loss` 출력 | 성공 확인 |
| Nginx 설치·홈페이지 교체 | 설치·service·복사·restart 명령, 빈 웹 확인 칸 | 절차만 확인 |
| Spring Boot | JDK/Maven 설치·빌드·80→9000 redirect·jar 실행 명령, 빈 웹 확인 칸 | 절차만 확인 |
| RDS | 생성 설정·endpoint 확인 절차·EC2 연결·MySQL 접속/DDL/DML 명령 | 실행 결과 미보존 |
| Spring JDBC | datasource 세 항목 수정 지시·재빌드/jar 명령 | 애플리케이션 결과 미보존 |
| 자원 정리 | EIP→EC2→RDS→SG→VPC 순서 | 삭제 완료 상태 미보존 |

## 헷갈린 점 / 질문

- `ping`은 HTTP/SSH와 다른 ICMP 트래픽이므로 22·80·443을 열어도 실패할 수 있다.
- Nginx 정적 페이지 실습과 Spring Boot jar 실행은 순차적으로 수행한 서로 다른 서버 역할 확인이다.
- RDS endpoint는 EC2의 Public IP가 아니며, 같은 VPC여도 DB Security Group의 3306 규칙이 필요하다.
- `application.properties`에 실제 DB 비밀번호를 남기지 않는다. 원본의 접속값은 위키에서 재노출하지 않는다.
- 삭제는 EIP·EC2·RDS처럼 먼저 참조되는 자원을 정리한 뒤 Security Group·VPC로 진행해야 한다.
- Route 53·ACM·Target Group·ALB·HTTPS는 이 날의 빈 “도메인 등록 예정” 구간으로 완료된 것이 아니다. 실제 후속은 05-12 CI/CD 수업이다.

## 관련 페이지

- [[concepts/aws-ec2-nginx-spring-deploy|AWS EC2에서 Nginx와 Spring Boot 배포]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/aws-rds-spring-boot|AWS RDS와 Spring Boot 연결]]
- [[concepts/aws-resource-lifecycle-cost-management|AWS 자원 생명주기와 비용 관리]]
- [[comparisons/ec2-vs-rds|EC2 vs RDS]]
- [[entities/amazon-ec2|Amazon EC2]]
- [[entities/amazon-rds|Amazon RDS]]

## 출처

- `raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md`
- `raw/KoreaICT/6. AWS/AWS 총정리/AWS 총정리.md`
