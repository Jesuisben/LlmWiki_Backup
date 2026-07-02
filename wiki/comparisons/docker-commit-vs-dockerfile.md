---
title: docker commit vs Dockerfile
created: 2026-07-02
updated: 2026-07-02
type: comparison
tags: [linux, backend]
sources:
  - raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
  - raw/Study/5. Linux/교육 자료/docker image를 docker hub에 업로드 하기.md
status: growing
confidence: high
---

# docker commit vs Dockerfile

## 비교 목적

수업에서는 컨테이너를 이미지로 만드는 방법으로 `docker commit`과 Dockerfile 두 가지가 등장했다. 둘 다 이미지를 만들지만 재현성과 관리 방식이 다르다.

## 한눈에 보기

| 항목 | `docker commit` | Dockerfile |
|---|---|---|
| 출발점 | 실행 중이거나 수정된 컨테이너 | 파일로 작성한 이미지 생성 절차 |
| 장점 | 빠르게 현재 상태를 이미지로 저장 | 재현 가능하고 이력 관리에 좋음 |
| 단점 | 어떤 명령으로 만들었는지 남기기 어려움 | 처음에는 문법을 익혀야 함 |
| 수업 예시 | `commit-ctr` → `jeju-img` | `Dockerfile01` → `pohang-img`, `myspring-img` |
| 실무 감각 | 임시 실험/스냅샷 | 표준적인 이미지 빌드 방식 |

## 수업 예제

```bash
docker container run --name commit-ctr -d -p 8090:80 httpd
docker cp ~/docker/commit/index04.html commit-ctr:/usr/local/apache2/htdocs/index.html
docker exec -it commit-ctr /bin/bash
echo "This is jeju test" > /usr/local/apache2/htdocs/jeju.txt
exit
docker commit commit-ctr jeju-img
```

```dockerfile
FROM httpd
COPY index05.html /usr/local/apache2/htdocs/index.html
COPY image18_02.png /usr/local/apache2/htdocs
```

```bash
docker build -t pohang-img -f ~/docker/dockerfile/Dockerfile01 .
```

## 언제 무엇을 쓰는가

- 수업 중 빠르게 “지금 수정한 컨테이너 상태”를 이미지로 남기려면 `commit`을 쓸 수 있다.
- 팀원과 공유하거나 CI/CD에서 반복 빌드하려면 Dockerfile이 더 적합하다.
- Spring Boot처럼 jar, 포트, 환경 변수, 실행 명령이 명확한 애플리케이션은 Dockerfile로 남기는 편이 좋다.

## 헷갈리기 쉬운 포인트

- `commit`은 컨테이너 내부에서 어떤 수동 작업을 했는지 파일로 설명해 주지 않는다.
- Dockerfile은 이미지 생성 과정 자체가 문서이자 코드가 된다.
- Docker Hub에 올릴 때는 `commit`으로 만들었든 Dockerfile로 만들었든 최종 이미지를 `docker tag` 후 `docker push`해야 한다.

## 관련 페이지

- [[summaries/2026-04-29-docker-network-volume-image|2026-04-29 Docker 네트워크, 볼륨, 사용자 정의 이미지]]
- [[summaries/2026-04-30-dockerfile-spring-load-balancing|2026-04-30 Dockerfile, Spring Boot 컨테이너, 로드 밸런싱]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[concepts/dockerfile-vs-compose|Dockerfile vs Docker Compose]]

## 출처

- `raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md`
- `raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md`
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf` — commit/Dockerfile 실습
- `raw/Study/5. Linux/교육 자료/docker image를 docker hub에 업로드 하기.md`
