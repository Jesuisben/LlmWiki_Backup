---
title: 2026-04-30 Dockerfile, Spring Boot 컨테이너, 로드 밸런싱
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [linux, backend, spring-boot, curriculum, study-log]
sources:
  - raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md
status: growing
confidence: high
---

# 2026-04-30 Dockerfile, Spring Boot 컨테이너, 로드 밸런싱

## 한 줄 요약

컨테이너를 이미지로 만드는 두 방식인 `commit`과 Dockerfile을 비교하고, Spring Boot 컨테이너 실행과 nginx 로드 밸런싱 설정까지 확장했다.

## 배운 내용

- 컨테이너 변경분을 이미지로 만드는 방법과 Dockerfile 스크립트로 이미지를 빌드하는 방법을 비교했다.
- `docker build -t ... -f Dockerfile ...`로 사용자 정의 이미지를 만들었다.
- 만든 이미지로 컨테이너를 실행하고 포트 매핑으로 브라우저에서 확인했다.
- Spring Boot 컨테이너를 만들고 MySQL 컨테이너 접속도 실습했다.
- `nginx.conf`에서 `upstream` 서버 그룹을 만들고 Apache/Nginx 쪽으로 요청을 분기하는 로드 밸런싱 개념을 배웠다.
- `/apache` 같은 경로에 따라 다른 서버 그룹으로 보내는 설정 흐름을 확인했다.

## 핵심 실습 흐름

```bash
cd ~/docker/dockerfile
docker build -t pohang-img -f ~/docker/dockerfile/Dockerfile01 .
docker image ls
docker container run --name pohang-ctr -d -p 8989:80 pohang-img
docker container stop pohang-ctr
docker container rm pohang-ctr
```

## 왜 중요한가

`docker run`만 알면 이미 만들어진 이미지를 실행할 수 있지만, 직접 서비스를 배포하려면 “우리 애플리케이션이 들어간 이미지”를 만들어야 한다. Dockerfile은 이미지 생성 과정을 코드처럼 남겨 반복 가능하게 만드는 도구다.

## 헷갈린 점 / 질문

- `commit`은 이미 실행·수정한 컨테이너를 이미지로 저장하는 방식이라 수동 작업 흔적이 남기 쉽다.
- Dockerfile은 이미지 생성 절차를 파일로 남겨 재현성이 좋다.
- 로드 밸런싱은 단순히 포트를 여는 것이 아니라, 앞단 서버가 뒤쪽 여러 서버로 요청을 나눠 보내는 구조다.

## 관련 페이지

- [[concepts/dockerfile-vs-compose|Dockerfile vs Docker Compose]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]

## 출처

- `raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md`
