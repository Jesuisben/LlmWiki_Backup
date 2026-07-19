---
title: GitHub Actions Secrets 기반 배포
created: 2026-07-03
updated: 2026-07-19
type: concept
tags: [github, ci-cd, aws, auth]
sources:
  - raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md
  - raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md
  - raw/KoreaICT/7. Ci&CD/교육 자료/CI&CD(SpringBoot_실습).pdf
  - raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md
  - raw/KoreaICT/9. 중간 프로젝트 공부/CICD/Github_Secrets 예시.md
status: growing
confidence: medium
---

# GitHub Actions Secrets 기반 배포

## 정의

GitHub Actions Secrets 기반 배포는 workflow 실행 중 필요한 민감값을 GitHub Repository Secrets에 저장하고, YAML에서는 이름으로만 참조하는 배포 방식이다.

## 왜 중요한가

배포에는 SSH key, 서버 주소, DB 비밀번호, JWT 키처럼 노출되면 안 되는 값이 필요하다. 이 값을 코드나 위키에 적으면 저장소 히스토리에 남아 위험해진다.

## 핵심 설명

- Secret은 GitHub 저장소 설정에서 등록한다.
- workflow에서는 `${{ secrets.SECRET_NAME }}` 형태로 참조한다.
- Secret 이름은 역할 중심으로 짓고, 실제 값은 로그에 출력하지 않는다.
- 실습 원본에 예시 값이 있더라도 위키에는 `<SSH_PRIVATE_KEY>`, `<DB_PASSWORD>`처럼 역할만 드러내는 일반화 표기를 사용한다.
- 2026-05-11 Spring Boot CI/CD 실습에서는 Docker Hub 계정/token, EC2 host/key, Docker image/container 이름을 repository secrets로 분리했다. `ci.yml`/`cd.yml`에는 실제 값을 적지 않고 Secret 이름 참조만 둔다는 원칙으로 읽어야 한다.

단계 9의 중간 프로젝트 가이드는 이 기준을 backend/frontend image, DB 연결, JWT 비대칭키, object storage 설정까지 넓힌다. 별도 `Github_Secrets 예시.md`는 필요한 항목을 역할별로 모은 **입력 목록**이며, 실제 Secret 값·등록 화면·workflow run 결과는 아니다.

## 수업에서 분리한 값

| Secret 역할 | workflow에서 필요한 이유 |
|---|---|
| Docker registry 계정·token | image push 인증 |
| EC2 host·SSH key | 원격 배포 대상 접속 |
| Docker image·container 이름 | build 대상과 실행 단위 식별 |
| DB 연결 설정 | 배포 container가 database에 연결할 runtime input |
| JWT private/public key | 발급자의 서명과 application 검증에 필요한 key material |
| object storage 설정 | file upload 대상과 접근 권한 주입 |

05-11 날짜 원본은 이 역할의 Secret 이름을 기록하지만 실제 값은 공개 위키에 옮기지 않는다. 또한 GitHub Secrets에 값을 등록했다는 사실만으로 registry login이나 EC2 SSH 배포 성공이 증명되지는 않는다.

## configuration 주입과 완료 조건

1. **정의:** application·workflow가 어떤 설정 이름을 읽을지 정한다.
2. **저장:** GitHub Secrets 같은 보호 저장소에 실제 값을 넣는다.
3. **주입:** workflow가 build argument·environment·SSH command 등 필요한 지점에 전달한다.
4. **소비:** Spring Boot·Docker·Nginx·cloud SDK가 예상한 이름과 형식으로 읽는다.
5. **검증:** Secret 값을 출력하지 않고 build, container, API, DB/object storage 결과로 확인한다.

단계 9 raw에는 1~3단계의 template과 연결 예시가 있지만, 실제 repository 설정과 4~5단계의 runtime 결과는 보존되지 않았다. 더구나 DB URL은 workflow에서 주입하면서 application 설정의 소비 표현이 맞지 않고, Passwordless 설정도 등록 목록과 container 전달 항목이 완전히 일치하지 않는다. Secret의 존재·등록·전달을 application 소비나 배포·인증 성공으로 전파하지 않는다.

## 자주 헷갈리는 점

- Secret은 “숨겨진 변수”이지, 코드 품질이나 인증 설계를 대신해 주는 기능은 아니다.
- Actions 로그에 `echo $SECRET`처럼 출력하면 감춰지더라도 위험한 습관이다.
- `.env`와 GitHub Secrets는 목적이 비슷하지만 저장 위치와 실행 시점이 다르다.
- Secret 이름이 서로 맞아도 값의 format·line break·권한·실행 profile이 틀리면 consumer가 실패할 수 있다.
- RS256 key, SSH key, registry token, DB password는 모두 비밀이지만 생성 주체·소비 주체·회전 방법이 다르다.
- 교육용 가이드의 장기 access key·private key·DB credential·keystore password를 container 환경변수로 직접 전달하는 방식은 운영 기본값이 아니다. 최소 권한, 단기 credential 또는 workload role, 회전·폐기, process/container inspection과 log 노출 위험을 함께 검토한다.
- third-party workflow action은 version을 고정하고 공급망 위험을 검토한다.

## 관련 개념

- [[concepts/middle-project-cicd-deploy-flow|중간 프로젝트 CI/CD 배포 흐름]]
- [[concepts/github-actions-workflow|GitHub Actions workflow]]
- [[concepts/spring-boot-cicd-docker-ec2-flow|Spring Boot CI/CD Docker-EC2 배포 흐름]]
- [[concepts/jwt-rs256-key-flow|JWT RS256 키 흐름]]
- [[entities/github|GitHub]]

## 출처

- `raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md`
- `raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md`
- `raw/KoreaICT/7. Ci&CD/교육 자료/CI&CD(SpringBoot_실습).pdf`
- `raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md`
- `raw/KoreaICT/9. 중간 프로젝트 공부/CICD/Github_Secrets 예시.md`
