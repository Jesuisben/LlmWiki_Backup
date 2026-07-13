---
title: docker commit vs Dockerfile
created: 2026-07-02
updated: 2026-07-13
type: comparison
tags: [linux, docker, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/KoreaICT/5. Linux/교육 자료/docker image를 docker hub에 업로드 하기.md
  - raw/KoreaICT/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
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
| 장점 | 빠르게 현재 상태를 이미지로 저장 | 재현 가능하고 Git으로 이력 관리 가능 |
| 단점 | 어떤 명령으로 만들었는지 남기기 어렵다 | 처음에는 문법을 익혀야 한다 |
| 수업 예시 | HTML을 바꾼 컨테이너를 `jeju-img`로 저장 | Spring Boot jar를 담은 `myspring-img` 생성 |
| 실무 감각 | 임시 실험/스냅샷 | 표준적인 이미지 빌드 방식 |

## 언제 무엇을 쓰는가

- 지금 컨테이너 상태를 빠르게 저장해 실험을 이어가려면 `docker commit`이 편하다.
- 같은 이미지를 다시 만들거나 팀원/서버/CI에서 재현해야 하면 Dockerfile을 쓴다.
- 학습 초반에는 `commit`이 직관적이지만, 프로젝트 배포에서는 Dockerfile 중심으로 넘어가야 한다.

## 헷갈리기 쉬운 포인트

- `docker commit`으로 만든 이미지는 “어떻게 만들었는지”가 문서화되지 않는다.
- Dockerfile은 명령 이력을 파일로 남기므로 GitHub 협업과 CI/CD에 더 적합하다.
- Docker Hub에 올릴 이미지는 되도록 Dockerfile로 재현 가능하게 만드는 편이 좋다.

## 관련 페이지

- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[concepts/dockerfile-vs-compose|Dockerfile vs Docker Compose]]
- [[entities/docker|Docker]]

## 최신 원본 대조

2026-04-29의 수정 컨테이너를 `docker commit`한 실습과 04-30의 FROM/COPY/Dockerfile build 실습을 기준으로 보강했다. 빠른 상태 스냅샷과 재현 가능한 절차 파일을 구분한다.

## 출처

- `raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md`
- `raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md`
