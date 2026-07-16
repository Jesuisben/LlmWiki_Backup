---
title: Docker registry tag·push·pull
created: 2026-07-16
updated: 2026-07-16
type: concept
tags: [linux, docker, ci-cd]
sources:
  - raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
  - raw/KoreaICT/5. Linux/교육 자료/docker image를 docker hub에 업로드 하기.md
status: growing
confidence: high
---

# Docker registry tag·push·pull

## 이 페이지의 책임과 신규 판단

이 페이지는 **한 host의 local image를 registry 이름으로 식별해 업로드하고, 다른 환경에서 다시 찾는 수동 전달 생명주기**를 맡는다. [[concepts/docker-image-container|Docker 이미지와 컨테이너]]의 생성·실행 기본기나 [[entities/docker|Docker]]의 전체 기술 이력과 달리, 핵심 질문은 “내 local image를 다른 환경이 어떤 이름과 저장소에서 찾는가?”다.

2026-04-29 수업에서 local image → tag → login → push → 다른 환경의 pull/run이 독립된 7교시 실습으로 이어졌고, 잘못된 local 이름으로 실행했을 때의 접근 오류도 함께 관찰했다. 독립 검색 역할과 troubleshooting 가치가 충분하므로 기존 Entity의 한 문단에만 흡수하지 않고 Concept로 보존한다.

## registry와 tag가 필요한 이유

- **Registry**는 container image를 저장하고 환경 사이에 전달하는 service다. 수업에서는 Docker Hub를 사용했다.
- **Tag**는 image에 registry namespace·repository·version을 포함한 이름을 붙인다.
- **Push**는 local image layer를 registry에 올린다.
- **Pull**은 registry image를 현재 host로 가져온다. local에 없으면 namespace가 정확해야 올바른 repository를 찾을 수 있다.

local에서 짧은 image 이름으로 실행되던 사실만으로 다른 host가 같은 image를 찾을 수 있는 것은 아니다. 다른 환경에는 local image와 local 이름표가 없으므로 registry namespace를 포함한 참조가 필요했다.

## 실제 수업 흐름

### 1. 전달할 local image 준비

먼저 Apache container의 homepage와 확인용 text를 바꾼 뒤 `docker commit`으로 사용자 정의 image를 만들었다. 새 image에서 file과 browser 결과를 확인한 과정은 registry가 아니라 **전달할 artifact 준비** 단계다.

### 2. registry 인증

Docker Hub account로 login하고 성공 메시지를 확인했다. 원본에는 password 대신 PAT를 사용할 수 있다는 안내와 credential이 암호화되지 않은 config file에 저장될 수 있다는 경고가 있다.

login 성공은 push 권한을 얻었다는 뜻이지 image가 업로드됐다는 뜻은 아니다. 실제 account·email·password·PAT·token 값은 이 페이지에 재노출하지 않는다.

### 3. registry 형식으로 tag

local image에 `namespace/repository:version` 구조의 새 tag를 붙였다. tag는 image layer를 다시 build하거나 복사하는 단계가 아니라, registry가 어느 account의 어느 repository·version으로 취급할지 식별자를 추가하는 단계다.

### 4. push와 원격 확인

registry 형식의 tag를 push했다. 출력에서 layer가 `Pushed` 또는 기존 layer에서 `Mounted`된 상태와 최종 digest가 기록됐다. 이후 Docker Hub repository 화면에서 image가 보이는지 확인했다.

### 5. 다른 환경에서 pull/run

다른 환경에서 namespace 없이 local 이름만으로 container를 실행하려 했을 때 local image를 찾지 못했고 repository 접근 오류가 발생했다. registry namespace를 포함해 pull하거나 run해야 올바른 원격 image를 찾을 수 있었다.

원본에는 다른 환경의 pull/run 명령까지 있지만, 그 container의 최종 browser 화면이나 내부 file을 다시 확인한 결과는 독립적으로 보존돼 있지 않다. 따라서 “원격 image 참조와 container 실행 단계가 기록됐다”까지만 확정하고 application 내용 동일성까지 과장하지 않는다.

## 입력 → 처리 → 결과

| 단계 | 입력 | 처리 | 확인 결과 |
|---|---|---|---|
| local artifact | 변경 container | `commit`으로 image 생성 | 새 local image와 새 container의 file·homepage 확인 |
| tag | local image·registry 식별 구조 | registry용 이름 추가 | namespace·repository·version을 가진 local tag |
| login | account 인증 | registry push 권한 확인 | login 성공과 credential 저장 경고 |
| push | registry tag | image layer 업로드·재사용 | layer 상태·digest와 repository 화면 |
| pull/run | 다른 환경의 registry 참조 | remote image 탐색·download·container 생성 | namespace 없는 접근 오류와 올바른 참조 명령; 최종 browser 결과는 미보존 |

## 완료 조건을 분리하기

1. **local image 존재**: 전달할 artifact가 준비됐다.
2. **registry tag 존재**: 올릴 repository·version 이름이 붙었다.
3. **login 성공**: 인증이 됐지만 아직 업로드 완료는 아니다.
4. **push 완료**: layer 상태와 digest가 나왔다.
5. **remote repository 확인**: registry UI에서 image를 찾을 수 있다.
6. **다른 환경 pull 성공**: 올바른 namespace로 image를 내려받았다.
7. **다른 환경 run 성공**: container process를 만들었다.
8. **application 동일성 확인**: browser·내부 file을 다시 확인해야 하지만 이 마지막 결과는 원본에 독립 보존되지 않았다.

push digest 하나만으로 다른 환경의 container·application 성공까지 확정하지 않는다.

## 자주 헷갈리는 지점과 오류

- **tag 없이 push:** registry가 요구하는 namespace/repository 이름이 없어 실패할 수 있다.
- **짧은 local 이름으로 다른 host에서 실행:** 다른 host에는 그 local image가 없으므로 잘못된 repository를 찾거나 접근 오류가 난다.
- **namespace 오타·권한 없음:** 다른 account repository이거나 private repository 권한이 없으면 push/pull이 실패할 수 있다.
- **tag와 build:** tag는 image 내용을 만들지 않는다. image 내용은 commit 또는 Dockerfile build 단계에서 정해진다.
- **Docker Hub와 GitHub:** Docker Hub는 image registry이고 GitHub는 source와 Git commit의 remote collaboration service다.
- **login 성공과 credential 안전:** login 성공 메시지가 credential helper 구성이나 안전한 저장을 의미하지 않는다.
- **수동 push와 CI/CD:** 이날은 사람이 login·tag·push·pull한 실습이다. [[concepts/ci-cd-automation|CI/CD 자동화]]의 workflow build·push·deploy 성공으로 소급하지 않는다.

## 선행·후속 연결

- 선행: [[comparisons/docker-commit-vs-dockerfile|docker commit vs Dockerfile]]에서 현재 상태 snapshot과 재현 recipe를 구분한다.
- 기본 단위: [[concepts/docker-image-container|Docker 이미지와 컨테이너]]가 local image와 running container의 차이를 맡는다.
- 날짜 흐름: [[summaries/2026-04-29-docker-network-volume-image|04-29 Summary]]의 network·storage·commit 다음 단계로 registry가 등장했다.
- 후속: CI/CD에서는 source 변경을 trigger로 image build·registry push·server 갱신을 자동화하지만, registry 자체의 저장·전달 책임은 그대로 남는다.

## 출처

- `raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md`
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md`
- `raw/KoreaICT/5. Linux/교육 자료/docker image를 docker hub에 업로드 하기.md`

원본의 실제 account·email·repository URL·password·PAT·token·credential 값은 사용하지 않고 단계·오류·경고의 역할만 보존했다.
