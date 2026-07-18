---
title: CLB vs ALB
created: 2026-07-03
updated: 2026-07-18
type: comparison
tags: [aws, backend]
sources:
  - raw/KoreaICT/7. Ci&CD/2026.05.12(화)/2026.05.12(화).md
  - raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md
  - raw/KoreaICT/7. Ci&CD/교육 자료/cloud.03.AWS 교안(이론).pdf
status: stable
confidence: medium
---

# CLB vs ALB

## 비교 목적

CLB(Classic Load Balancer)와 ALB(Application Load Balancer)를 같은 완료 상태로 오해하지 않도록, 수업에서 직접 남은 증거와 일반 기능을 분리한다. 05-12 원본에서 CLB는 관리 표의 예정 항목뿐이고, 실제 구성 절차는 ALB·Target Group·Listener·ACM·Alias 쪽에 집중되어 있다.

## 한눈에 보기

| 항목 | CLB | ALB | 근거 수준 |
|---|---|---|---|
| 정식 이름 | Classic Load Balancer | Application Load Balancer | 일반 개념 |
| 05-12 원본에 남은 범위 | 관리 표의 예정 이름·설명 | Target Group·Security Group·ALB·HTTPS Listener·ACM·Alias 구성 절차 | 직접 수업 |
| 대상 관리 관점 | 기존 세대의 load balancing 모델 | Target Group에 EC2를 등록하고 Listener가 전달 | ALB 쪽만 직접 절차 |
| HTTP/HTTPS 처리 | 생성·응답 결과 없음 | HTTP/HTTPS Listener와 인증서 연결 절차 | 직접 수업 |
| routing·상태 확인 | 직접 다루지 않음 | path/host routing과 Health Check는 일반 기능이지만 05-12의 설정값·결과는 없음 | 일반 기능 |
| 최종 결과 | 생성·응답 모두 미보존 | target health·DNS 조회·HTTP/HTTPS 응답·browser 화면 미보존 | 결과 경계 |

## 언제 무엇을 쓰는가

- CLB는 AWS의 이전 세대 load balancer와 ALB 구조를 비교하는 기준으로만 사용한다. 이번 수업에서는 CLB 생성·검증을 했다고 판단할 증거가 없다.
- ALB는 HTTP/HTTPS 서비스에서 Listener·Target Group·ACM 인증서를 연결하는 구조를 학습할 때 사용한다. 이번 원본은 console 구성 절차를 보존하지만 정상 target이나 실제 응답을 증명하지 않는다.
- Route 53은 load balancer 종류가 아니라 DNS 서비스다. 05-12의 서비스 접속용 A/Alias는 ALB를 대상으로 하는 절차이며, DNS 조회 또는 browser 결과는 남지 않았다.

## 헷갈리기 쉬운 포인트

- **절차와 결과:** 생성 화면의 입력 순서나 확인 URL은 성공 결과가 아니다. target health, ALB 상태, DNS 조회, HTTP/HTTPS 응답을 각각 확인해야 한다.
- **Target Group과 ALB:** Target Group은 요청 대상 묶음이고, ALB는 Listener로 받은 요청을 그 묶음에 전달한다. 둘은 대체 관계가 아니다.
- **ACM과 ALB:** 인증서 요청·DNS 검증과 ALB 443 Listener 연결은 서로 다른 단계다. 원본에는 절차만 있고 발급·응답 화면은 없다.
- **일반 기능과 직접 수업:** ALB의 path/host routing과 Health Check는 일반 기능이다. 05-12에서 해당 규칙을 구성하거나 정상 결과를 확인했다고 확대하지 않는다.

## 관련 페이지

- [[summaries/2026-05-12-route53-alb-https-review|2026-05-12 Route 53, ALB, HTTPS 복습과 도메인 배포]]
- [[concepts/aws-route53-load-balancer-https|AWS Route 53, Load Balancer, HTTPS 흐름]]
- [[concepts/docker-reverse-proxy-load-balancing|Docker reverse proxy와 로드 밸런싱]]
- [[entities/amazon-route-53|Amazon Route 53]]
- [[entities/aws|AWS]]

## 출처

- `raw/KoreaICT/7. Ci&CD/2026.05.12(화)/2026.05.12(화).md`
- `raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md`
- `raw/KoreaICT/7. Ci&CD/교육 자료/cloud.03.AWS 교안(이론).pdf`
