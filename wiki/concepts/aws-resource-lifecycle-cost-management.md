---
title: AWS 자원 생명주기와 비용 관리
created: 2026-07-13
updated: 2026-07-18
type: concept
tags: [aws, backend]
sources:
  - raw/KoreaICT/6. AWS/2026.05.07(목)/2026.05.07(목).md
  - raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md
  - raw/KoreaICT/6. AWS/AWS 총정리/AWS 총정리.md
status: growing
confidence: high
---

# AWS 자원 생명주기와 비용 관리

## 정의

AWS 자원 생명주기 관리는 필요한 VPC·EC2·RDS·Elastic IP·Security Group을 생성해 연결하고, 실습이나 서비스가 끝나면 의존 관계를 확인하며 정리해 불필요한 비용과 잔존 접근 경로를 줄이는 작업이다.

## 왜 중요한가

AWS 수업의 On-Demand는 필요한 만큼 쓰고 비용을 지불하는 방식이었다. 따라서 “리소스를 만들 수 있다”만으로 끝나지 않고, 연결하지 않은 Elastic IP, 실행 중인 EC2, 남은 RDS, 사용하지 않는 보안 그룹과 VPC를 확인하는 운영 책임까지 함께 배웠다.

## 수업에서의 정리 원칙

1. **먼저 사용 중인 연결을 끊는다.** Elastic IP는 연결 해제 후 release하는 절차로 기록됐다.
2. **비용이 직접 발생하거나 상위 자원을 참조하는 실행 자원부터 정리한다.** EC2와 RDS의 종료·삭제 상태까지 확인해야 한다.
3. **의존 관계를 제거한다.** RDS/EC2가 참조하는 Security Group, Internet Gateway, Subnet, Route Table을 확인한다.
4. **마지막에 네트워크 틀을 정리한다.** 연결된 자원이 없을 때 VPC를 삭제한다.
5. **보안·데이터 옵션을 확인한다.** RDS 삭제 전 최종 스냅샷 같은 확인 항목을 무심코 넘기지 않는다.

수업의 정리 흐름은 `EIP 연결 해제·release → EC2 종료 → RDS 삭제 → Security Group·IGW·Subnet·Route Table → VPC → Key Pair`로 요약된다. 05-07 원본의 직접 목록은 EIP·EC2·Security Group·VPC·Key Pair이고, 05-08에는 RDS와 자동 생성 Security Group 정리가 추가됐다.

실제 콘솔의 정확한 삭제 가능 순서는 남아 있는 참조 자원에 따라 달라진다. 핵심은 생성 순서를 외우는 것이 아니라, **삭제가 거절되면 아직 무엇이 그 자원을 참조하는지 추적하는 것**이다.

## 실제 결과와 절차의 구분

- 05-07의 5~8교시는 “구성 및 삭제 과정을 두 번 혼자 실습”하라는 지시가 반복되지만 반복별 완료 화면은 없다.
- 05-08은 RDS를 포함한 삭제 순서와 체크박스·Security Group 규칙 정리 절차를 남겼지만 최종 자원 목록은 없다.
- 따라서 이 페이지는 안전한 정리 **순서와 확인점**을 보존하며, 모든 자원의 삭제 완료를 수업 결과로 단정하지 않는다.

## 자주 헷갈리는 점

- EC2를 중지·종료해도 Elastic IP를 release하지 않으면 비용 또는 잔존 자원 문제가 남을 수 있다.
- Security Group은 EC2/RDS가 사용 중이면 바로 삭제되지 않을 수 있다.
- RDS는 단순 서버 종료와 달리 삭제 확인·백업/스냅샷 선택을 함께 검토해야 한다.
- 실습의 `0.0.0.0/0` 허용은 학습 편의 설정이다. 정리 단계에서는 불필요한 공개 접근 규칙도 함께 검토한다.

## 관련 개념

- [[summaries/2026-05-07-aws-ec2-nginx-rds|2026-05-07 AWS VPC, EC2, EIP와 자원 관리]]
- [[summaries/2026-05-08-aws-rds-resource-cleanup|2026-05-08 AWS RDS MySQL 연결과 자원 정리]]
- [[summaries/2026-05-08-aws-subject-review|AWS 총정리]]
- [[entities/aws|AWS]]
- [[entities/amazon-ec2|Amazon EC2]]
- [[entities/amazon-rds|Amazon RDS]]
- [[comparisons/ec2-vs-rds|EC2 vs RDS]]

## 출처

- `raw/KoreaICT/6. AWS/2026.05.07(목)/2026.05.07(목).md`
- `raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md`
- `raw/KoreaICT/6. AWS/AWS 총정리/AWS 총정리.md`
