---
title: Docker reverse proxy와 로드 밸런싱
created: 2026-07-02
updated: 2026-07-18
type: concept
tags: [linux, docker, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/KoreaICT/5. Linux/교육 자료/로드 밸런싱.png
status: growing
confidence: high
---

# Docker reverse proxy와 로드 밸런싱

## 이 페이지의 책임

이 페이지는 2026-04-30 수업의 `proxy-net` 안에서 **browser 요청이 Nginx reverse proxy를 거쳐 Apache·Nginx backend container로 전달되는 과정**을 설명한다. 04-27 Linux host에 직접 설치한 Nginx, 04-28의 단일 web container, 후속 AWS ALB는 실행 위치와 관리 주체가 다르므로 같은 구성으로 합치지 않는다.

## 정의와 필요성

- **Reverse proxy**: client가 backend에 직접 접속하지 않고 앞단 proxy에 요청하면, proxy가 내부 backend를 선택해 요청을 전달한다.
- **Load balancing**: 여러 backend가 있을 때 요청을 한 곳에 몰지 않고 나누는 처리 방식이다.

수업에서는 backend 여섯 개를 host port에 각각 공개하지 않았다. 같은 Docker network 안에서 container 이름과 80번 port로 찾게 하고, 외부에는 `reverse-proxy`의 host 80번만 공개했다. 이 때문에 browser는 backend 이름을 몰라도 하나의 진입점으로 요청할 수 있었다.

## 실제 수업 artifact

| 역할 | 실제 artifact | 실행 위치·연결 |
|---|---|---|
| Docker network | `proxy-net` | proxy와 backend가 container 이름으로 통신하는 범위 |
| Apache backend | `apache01`, `apache02`, `apache03` | `httpd`, container port 80, host port 미공개 |
| Nginx backend | `nginx04`, `nginx05`, `nginx06` | `nginx`, container port 80, host port 미공개 |
| proxy 설정 | host의 `~/nginx.conf` | `reverse-proxy`의 `/etc/nginx/nginx.conf`로 bind mount |
| 외부 진입점 | `reverse-proxy` | host 80 → container 80 port mapping |

각 backend의 homepage를 서로 구별할 수 있게 바꾼 것은 새로고침 때 어느 container가 응답했는지 눈으로 확인하기 위한 준비였다. Apache는 host 파일을 `docker cp`로 넣었고, Nginx는 container 내부 기본 페이지를 수정했다.

## 원본의 `nginx.conf`

아래 설정은 R07의 연속된 실제 원문이다. `backend_apache`와 `backend_nginx`를 별도 upstream으로 만들고 URL path에 따라 전달 대상을 나눴다.

```nginx
# nginx.conf 파일 시작
events {}

http {
   # upstream : 서버 그룹 (로드밸런싱)
   # backend_apache라고 그룹 이름 설정
    upstream backend_apache {
        server apache01:80;
        server apache02:80;
        server apache03:80;
    }

    upstream backend_nginx {
        server nginx04:80;
        server nginx05:80;
        server nginx06:80;
    }

    server { # 외부 요청 받는 곳
      # 기본 포트를 80으로 지정
        listen 80;

        # Apache로 보내기
		# 만약 /apache라고 치면 해당 경로(그룹)로 이동하게 하기
        location /apache/ {
            proxy_pass http://backend_apache/;
        }

        # Nginx로 보내기
        location /nginx/ {
            proxy_pass http://backend_nginx/;
        }

        # 기본 (로드밸런싱 테스트)
        location / {
            proxy_pass http://backend_apache/;
        }
    }
}
# nginx.conf 파일 끝
```

`upstream`은 backend 묶음의 이름이고, `proxy_pass`는 현재 `location`의 요청을 그 묶음으로 전달한다. `/`와 `/apache/`는 Apache group, `/nginx/`는 Nginx group을 선택했다.

## 입력 → 처리 → 결과

1. **입력**: browser가 VM의 80번, `/apache/`, `/nginx/` 중 하나로 요청한다.
2. **진입**: host 80번에 공개된 `reverse-proxy` container가 요청을 받는다.
3. **처리**: Nginx가 `location`을 고르고 해당 `proxy_pass`의 upstream으로 전달한다.
4. **내부 통신**: `proxy-net`에서 backend container 이름과 80번 port로 연결한다.
5. **결과**: 선택된 backend의 구별 가능한 homepage가 proxy를 거쳐 browser에 응답한다.

원본은 기본 URL에서 Apache 세 개가, `/nginx/`에서는 Nginx 세 개가 새로고침에 따라 번갈아 보였다고 기록한다. Apache 한 개와 Nginx 한 개를 중단한 뒤 새로고침하는 단계도 적혀 있지만, health check 설정·재시도 정책·장애 조치 결과 로그까지 보존된 것은 아니다.

## 완료 조건을 한 번에 묶지 않기

| 확인 단계 | 수업에서 확인할 대상 | 판정 경계 |
|---|---|---|
| backend 실행 | Apache·Nginx container 여섯 개 | 생성 명령만으로 homepage 응답까지 자동 확정하지 않음 |
| network 연결 | 모든 container가 `proxy-net` 사용 | 같은 network와 host port 공개는 다른 문제 |
| 설정 artifact | host `nginx.conf` 작성·mount | 파일 존재·mount와 설정 문법 유효성은 별도 |
| proxy process | `reverse-proxy`가 host 80에 공개 | 원본에는 독립 `nginx -t`나 proxy log 결과가 없음 |
| backend 응답 | 각 homepage가 구별 가능 | proxy를 거치지 않은 내부 응답과 browser 진입을 구분 |
| browser 분배 | URL별 group 선택과 새로고침 결과 | round-robin 관찰은 운영 health check 완성을 뜻하지 않음 |

browser에서 여러 backend 응답을 관찰한 것은 설정·network·proxy process·backend 응답이 함께 작동했다는 통합 결과다. 그러나 독립 설정 검사나 운영 모니터링을 실행했다는 증거로 확대하지 않는다.

## 자주 헷갈리는 경계

- **04-27 host Nginx**는 Ubuntu host의 service와 document root를 직접 운영했다. 이 페이지의 Nginx는 Docker container 안의 proxy process다.
- **04-28 web container**는 host port로 개별 homepage를 공개했다. 이 실습의 backend는 proxy만 접근하도록 host port를 생략했다.
- **Docker network와 port mapping**은 다르다. `proxy-net`은 container 간 경로이고, `-p 80:80`은 browser가 proxy로 들어오는 host 경로다.
- **Nginx reverse proxy와 AWS ALB**는 요청 분배 목적이 닮았지만, Nginx config/container와 AWS Listener·Target Group·health check는 다른 실행 계층이다.
- `로드 밸런싱.png`는 user 다섯 명의 업무를 상담자 두 명에게 나누는 비유다. network·port·container 구성의 기술 증거로 사용하지 않는다.

## 선행·후속 연결

- 선행: [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]에서 배운 이름 기반 통신과 mount를 proxy 구성에 사용했다.
- 같은 날: [[summaries/2026-04-30-dockerfile-spring-load-balancing|04-30 Summary]]에서 Dockerfile·Spring Boot+MySQL 실습 뒤 reverse proxy로 확장됐다.
- 후속: [[concepts/docker-compose-manifest|Docker Compose manifest]]는 여러 container 관계를 YAML로 선언하지만 proxy 설정의 의미를 자동 설계하지 않는다.
- cloud 확장: [[concepts/aws-route53-load-balancer-https|AWS Route 53, Load Balancer, HTTPS 흐름]]은 별도 AWS resource와 운영 경계를 다룬다.
- 후속 수업: [[summaries/2026-05-12-route53-alb-https-review|05-12 Route 53·ALB·HTTPS]]에서 Docker Nginx 설정이 아니라 AWS Target Group·Listener·ALB로 요청 분배를 확장했다.

## 출처

- `raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md` — 실제 container·network·config·mount·browser 흐름
- `raw/KoreaICT/5. Linux/교육 자료/로드 밸런싱.png` — 상담자 업무 분배 비유만 보조