---
title: 호스트 포트 포워딩 vs Docker 포트 매핑
created: 2026-07-13
updated: 2026-07-13
type: comparison
tags: [linux, docker, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md
  - raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
status: growing
confidence: high
---

# 호스트 포트 포워딩 vs Docker 포트 매핑

## 비교 목적

Linux 수업에서는 VM에서 80번 요청을 Spring Boot의 9000번 포트로 보내는 포트 포워딩을 다뤘고, Docker에서는 `-p 8888:80`, `-p 9000:9000`처럼 호스트와 컨테이너 포트를 연결했다. 둘 다 외부 요청의 목적지를 바꾸지만 적용되는 네트워크 층이 다르다.

## 한눈에 보기

| 항목 | 호스트 포트 포워딩 | Docker 포트 매핑 |
|---|---|---|
| 수업 예 | `iptables`로 host 80 → Spring Boot 9000 | `docker run -p 8888:80 httpd` |
| 대상 | Linux host에서 실행 중인 프로세스 | host와 격리된 container 프로세스 |
| 설정 위치 | VM/Linux의 방화벽·NAT 규칙 | Docker 실행 옵션 또는 Compose `ports` |
| 점검 대상 | 서비스 실행, host 포트, UFW/iptables | 컨테이너 실행, `ports`, container 내부 서비스 |

## 어떻게 이어지는가

Spring Boot jar를 VM에서 직접 실행할 때는 Linux host의 포트와 UFW/iptables를 확인한다. 같은 앱을 컨테이너화한 뒤에는 Docker가 host 포트와 container 포트를 연결한다. 이후 reverse proxy Nginx를 앞단에 둘 때도 Nginx의 listen/proxy 설정과 Docker 매핑은 별도로 읽어야 한다.

## 헷갈리기 쉬운 포인트

- `-p 8888:80`의 왼쪽은 브라우저가 접속하는 host 포트이고, 오른쪽은 컨테이너 내부 서비스 포트다.
- Docker network는 컨테이너끼리 통신하는 통로이고, 포트 매핑은 host 밖/안의 접속 경로다. 같은 기능이 아니다.
- UFW에서 host 포트를 막으면 Docker 컨테이너가 정상이어도 외부 접속이 실패할 수 있다.

## 관련 페이지

- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[concepts/docker-reverse-proxy-load-balancing|Docker reverse proxy와 로드 밸런싱]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md`
- `raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md`
- `raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md`
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md`
