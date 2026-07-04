# Wiki Log

> 이 파일은 위키 작업의 시간순 기록이다.  
> append-only로 운영한다. 과거 기록을 임의로 삭제하지 않는다.  
> 형식: `## [YYYY-MM-DD] action | subject`  
> action 예시: `create`, `ingest`, `update`, `query`, `lint`, `archive`, `delete`


## 로그 아카이브

- [[_meta/wiki-log-archive-2026-06|Wiki Log Archive 2026-06]] — 2026년 6월 작업 기록
- [[_meta/wiki-log-archive-2026-07|Wiki Log Archive 2026-07]] — 2026년 7월 작업 기록 중 이번 분할 전까지의 기록

## 현재 로그

## [2026-07-04] update | Java/Oracle subject-review hub 고도화

- 목적: 사용자가 요청한 1과목 Java와 2과목 Oracle wiki 업데이트를 기존 course-material-aware backfill의 연장선으로 수행하되, 신규 얕은 페이지를 만들지 않고 이미 존재하는 과목 복습 허브와 entity를 깊게 보강함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. Oracle 원본에 포함된 로컬 실습용 접속값/비밀번호류는 wiki 본문에 재노출하지 않고 역할·절차 중심으로 일반화함.
- 보강한 subject-review summary:
  - `wiki/summaries/2026-03-13-java-subject-review.md` — Java 파일 문법, 변수 읽기/쓰기, 형변환, 제어문, 배열, 클래스/객체, 생성자/오버로딩, 상속/다형성, 추상 클래스/인터페이스, static/final을 총정리 원본과 날짜별 노트 기준으로 재구성함.
  - `wiki/summaries/2026-03-20-oracle-subject-review.md` — DBMS/SQL, DBeaver 접속 흐름, DDL/DML/TCL, 테이블/제약조건/시퀀스, 참조 무결성, 함수/GROUP BY, JOIN, 서브쿼리, ERD/정규화를 총정리 원본과 날짜별 노트 기준으로 재구성함.
- 보강한 entity:
  - `wiki/entities/java.md` — 날짜별 학습 이력, 복습 경로, Spring/Oracle 연결을 보강함.
  - `wiki/entities/oracle-database.md` — 날짜별 학습 이력, SQL/무결성/조회/설계 복습 경로, Spring/React 프로젝트 연결과 보안 메모를 보강함.
- 신규 페이지는 만들지 않았고, `wiki/index.md`는 설명과 Last updated만 갱신해 Total pages 235를 유지함.

## [2026-07-03] ingest | Python 2026-07-03 Pandas groupby와 시각화

- 목적: `raw/Study/10. Python/2026.07.03(금)/2026.07.03(금).md`를 읽고, Pandas `groupby` 집계, 다중 색인 정리, 사용자 정의 집계, `transform`, `pd.cut`, matplotlib 시각화 흐름을 기존 Python/Pandas/Jupyter 페이지와 연결함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함.
- 새로 추가한 summary: `wiki/summaries/2026-07-03-python-pandas-groupby-visualization.md`.
- 새로 추가한 concept/entity: `wiki/concepts/pandas-groupby-aggregation.md`, `wiki/entities/matplotlib.md`.
- 보강한 기존 페이지: `wiki/concepts/pandas-dataframe-basics.md`, `wiki/entities/python.md`, `wiki/entities/pandas.md`, `wiki/entities/jupyter-notebook.md`, `wiki/_meta/wiki-quality-audit-2026-07-02.md`.
- `wiki/index.md`에 신규 페이지 3개를 등록하고 Total pages를 235로 갱신함.

## [2026-07-03] ingest | Python 날짜별 원본 2026-06-19~2026-06-30

- 목적: `raw/Study/10. Python`의 2026-06-19~2026-06-30 날짜별 원본을 읽고, Pandas 이전 Python 기초 문법·컬렉션·함수·모듈·표준 라이브러리·객체지향·예외 처리·파일/정규표현식·XML/JSON·Jupyter/Pandas 입문 흐름을 기존 Python/Pandas 페이지와 연결함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함.
- 새로 추가한 summary: 2026-06-19~2026-06-30 Python 날짜별 summary 8개.
- 새로 추가한 concept: `python-basic-syntax`, `python-collections-comprehension`, `python-functions-modules-packages`, `python-file-regex-data-processing`, `python-oop-basics`.
- 보강한 기존 페이지: `wiki/entities/python.md`, `wiki/entities/pandas.md`, `wiki/entities/jupyter-notebook.md`, `wiki/concepts/pandas-dataframe-basics.md`, `wiki/_meta/wiki-quality-audit-2026-07-02.md`.
- `wiki/index.md`에 신규 페이지 13개를 등록하고 Total pages를 232로 갱신함.


## [2026-07-03] ingest | Passwordless 날짜별 원본 2026-05-14~2026-05-21

- 목적: `raw/Study/8. Passwordless`의 2026-05-14~2026-05-21 날짜별 원본을 읽고, Passwordless/X1280 인증 흐름, QR/앱 승인, Spring Boot 인증 연동, REST API/Postman 실습을 기존 중간 프로젝트 Passwordless 페이지와 연결함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. 원본에 포함된 실습용 IP, 서버키, 라이선스 키, 관리자 비밀번호, DB 비밀번호 같은 민감값은 wiki에 재노출하지 않고 역할/placeholder 설명으로 일반화함.
- 참고한 대표 원본:
  - `raw/Study/8. Passwordless/2026.05.14(목)/2026.05.14(목).md`
  - `raw/Study/8. Passwordless/2026.05.15(금)/2026.05.15(금).md`
  - `raw/Study/8. Passwordless/2026.05.18(월)/2026.05.18(월).md`
  - `raw/Study/8. Passwordless/2026.05.19(화)/2026.05.19(화).md`
  - `raw/Study/8. Passwordless/2026.05.20(수)/2026.05.20(수).md`
  - `raw/Study/8. Passwordless/2026.05.21(목)/2026.05.21(목).md`
  - `raw/Study/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md`
- 새로 추가한 summary:
  - `wiki/summaries/2026-05-14-passwordless-x1280-intro.md`
  - `wiki/summaries/2026-05-15-passwordless-x1280-docker-service.md`
  - `wiki/summaries/2026-05-18-passwordless-x1280-server-spring-sample.md`
  - `wiki/summaries/2026-05-19-aam-ape-authentication-filingbox.md`
  - `wiki/summaries/2026-05-20-filingbox-giga-mega.md`
  - `wiki/summaries/2026-05-21-passwordless-x1280-rest-api.md`
- 새로 추가/보강한 concept/entity/comparison:
  - `wiki/concepts/passwordless-x1280-auth-flow.md`
  - `wiki/concepts/passwordless-qr-app-approval.md`
  - `wiki/concepts/spring-boot-passwordless-integration.md`
  - `wiki/entities/passwordless-x1280.md`
  - `wiki/comparisons/passwordless-vs-password-login.md`
- 연결 보강한 기존 페이지:
  - `wiki/summaries/2026-05-middle-project-cicd-passwordless-guide.md`
  - `wiki/concepts/spring-boot-rest-api.md`, `wiki/concepts/jwt-session-cookie-auth.md`, `wiki/concepts/spring-security-jwt-filter.md`, `wiki/concepts/frontend-backend-architecture.md`
  - `wiki/entities/spring-boot.md`, `wiki/entities/aws.md`
  - `wiki/_meta/wiki-quality-audit-2026-07-02.md`
- `wiki/index.md`에 신규 페이지 9개를 등록하고 Total pages를 219로 갱신함.

## [2026-07-03] ingest | Ci&CD 날짜별 원본 2026-05-11~2026-05-13

- 목적: `raw/Study/7. Ci&CD`의 2026-05-11~2026-05-13 날짜별 원본을 읽고, CI/CD 자동화, GitHub Actions, Docker Hub/EC2 배포, Route 53/ALB/HTTPS 복습, Terraform, S3 파일 업로드를 기존 AWS·중간 프로젝트 CI/CD 흐름과 연결함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. 원본에 포함된 Docker token, AWS access key, RDS password, IP/endpoint 같은 실습용 민감값은 wiki에 재노출하지 않고 placeholder/역할 설명으로 일반화함.
- 참고한 대표 원본:
  - `raw/Study/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md`
  - `raw/Study/7. Ci&CD/2026.05.12(화)/2026.05.12(화).md`
  - `raw/Study/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md`
  - `raw/Study/7. Ci&CD/교육 자료/CI&CD(SpringBoot_이론).pdf`
  - `raw/Study/7. Ci&CD/교육 자료/CI&CD(SpringBoot_실습).pdf`
  - `raw/Study/7. Ci&CD/교육 자료/cloud.02.AWS 교안(실습).pdf`
  - `raw/Study/7. Ci&CD/교육 자료/cloud.03.AWS 교안(이론).pdf`
- 새로 추가한 summary:
  - `wiki/summaries/2026-05-11-cicd-github-actions-spring-boot.md`
  - `wiki/summaries/2026-05-12-route53-alb-https-review.md`
  - `wiki/summaries/2026-05-13-terraform-s3-file-upload.md`
- 새로 추가한 concept/entity:
  - `wiki/concepts/ci-cd-automation.md`
  - `wiki/concepts/github-actions-workflow.md`
  - `wiki/concepts/spring-boot-cicd-docker-ec2-flow.md`
  - `wiki/concepts/terraform-infrastructure-as-code.md`
  - `wiki/concepts/aws-s3-file-upload.md`
  - `wiki/entities/amazon-s3.md`
- 보강한 기존 페이지:
  - `wiki/concepts/middle-project-cicd-deploy-flow.md`
  - `wiki/concepts/github-actions-secrets-deploy.md`
  - `wiki/entities/github.md`, `wiki/entities/aws.md`, `wiki/entities/spring-boot.md`
  - `wiki/_meta/wiki-quality-audit-2026-07-02.md`
- `wiki/index.md`에 신규 페이지 9개를 등록하고 Total pages를 210으로 갱신함.

## [2026-07-03] update | AWS course-material-aware wiki ingest

- 목적: 감사 리포트의 잔여 후보 중 `raw/Study/6. AWS/2026.05.06(수) - 시작/` ~ `raw/Study/6. AWS/2026.05.08(금)/` 범위를 다음 과목으로 선정하고, 사용자 날짜 MD가 시간표 템플릿뿐인 점을 확인한 뒤 AWS 교육자료 PDF와 실습 관리 대장을 주 provenance로 삼아 고품질 ingest를 수행함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. 날짜 MD는 비어 있는 시간표 템플릿으로 표시하고, 실제 내용 출처는 확인한 AWS 교육자료에 명시함.
- 참고한 대표 교육자료:
  - `raw/Study/6. AWS/교육 자료/AWS 기초 용어.pdf`
  - `raw/Study/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf`
  - `raw/Study/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf`
  - `raw/Study/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf`
  - `raw/Study/6. AWS/교육 자료/실습 관리 대장(텍스트).md`
- 새로 추가한 summary:
  - `wiki/summaries/2026-05-06-aws-cloud-vpc-ec2.md`
  - `wiki/summaries/2026-05-07-aws-ec2-nginx-rds.md`
  - `wiki/summaries/2026-05-08-aws-route53-load-balancer-https.md`
- 새로 추가한 concept/entity/comparison:
  - `wiki/concepts/aws-cloud-vpc-networking.md`
  - `wiki/concepts/aws-ec2-nginx-spring-deploy.md`
  - `wiki/concepts/aws-rds-spring-boot.md`
  - `wiki/concepts/aws-route53-load-balancer-https.md`
  - `wiki/entities/aws.md`, `wiki/entities/amazon-ec2.md`, `wiki/entities/amazon-rds.md`, `wiki/entities/amazon-route-53.md`
  - `wiki/comparisons/ec2-vs-rds.md`, `wiki/comparisons/clb-vs-alb.md`
- `wiki/index.md`에 신규 페이지 12개를 등록하고 Total pages를 189로 갱신함.

## [2026-07-03] update | Java course-material-aware wiki backfill

- 목적: `raw/Study/1. Java` 사용자 정리 MD 14개를 주 자료로 삼고, Java/IntelliJ/GitHub 교안 PDF와 2026-02-27·2026-03-03 문제 이미지를 실제 확인해 기존 Java wiki 1차 정리본을 교안-aware 방식으로 고도화함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. `sources`에는 사용자 정리 MD와 실제 참고한 교안 PDF/문제 이미지 경로를 함께 남김.
- 참고한 대표 교육자료:
  - `raw/Study/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
  - `raw/Study/1. Java/교육 자료/IntelliJ 교안.pdf`
  - `raw/Study/1. Java/교육 자료/Github 교안(실습).pdf`
  - `raw/Study/1. Java/2026.02.27(금)/1번 문제.png` ~ `3번 문제.png`
  - `raw/Study/1. Java/2026.03.03(화)/연산자 마무리 문제.png` 및 관련 문제 이미지
- 보강한 summary: `wiki/summaries/2026-02-26-orientation.md` ~ `wiki/summaries/2026-03-13-java-project-oracle-start.md` 총 12개
- 보강한 concept:
  - `wiki/concepts/java-basic-types.md`
  - `wiki/concepts/java-operators.md`
  - `wiki/concepts/java-conditional-logic.md`
  - `wiki/concepts/java-loop.md`
  - `wiki/concepts/java-array.md`
  - `wiki/concepts/java-class-object.md`
  - `wiki/concepts/java-method-constructor-overloading.md`
  - `wiki/concepts/java-object-array-memory.md`
  - `wiki/concepts/java-inheritance.md`
  - `wiki/concepts/java-polymorphism-casting.md`
  - `wiki/concepts/java-abstract-interface.md`
  - `wiki/concepts/java-interface-capability-design.md`
  - `wiki/concepts/java-memory-static-final.md`
- 보강한 entity/comparison:
  - `wiki/entities/java.md`, `wiki/entities/git.md`, `wiki/entities/github.md`, `wiki/entities/intellij-idea.md`
  - `wiki/comparisons/primitive-vs-reference-types.md`, `wiki/comparisons/array-vs-collection.md`, `wiki/comparisons/overloading-vs-overriding.md`, `wiki/comparisons/interface-vs-abstract-class.md`
- 새 페이지는 만들지 않았고, `wiki/index.md`는 설명과 Last updated만 갱신해 Total pages 176을 유지함.

## [2026-07-02] update | Oracle course-material-aware wiki backfill

- 목적: `raw/Study/2. Oracle` 사용자 정리 MD 6개를 주 자료로 삼고, Oracle/DBeaver 교안 PDF와 SQL 스크립트를 실제 확인해 기존 Oracle/DB 1차 wiki 정리본을 재검증·보강함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. `sources`에는 사용자 정리 MD와 실제 참고한 교육자료/SQL 스크립트 경로를 함께 남김.
- 참고한 대표 교육자료:
  - `raw/Study/2. Oracle/교육 자료/오라클 교안.pdf`
  - `raw/Study/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf`
  - `raw/Study/2. Oracle/교육 자료/디비버(Dbeaver) 사용법(version 2.0).pdf`
  - `raw/Study/2. Oracle/교육 자료/스크립트들/A01.관리자 사용자 생성하기.sql` ~ `A07 조인 실습.sql`
- 보강한 summary: `wiki/summaries/2026-03-13-java-project-oracle-start.md` ~ `wiki/summaries/2026-03-20-database-modeling-normalization-view-index.md` 총 6개
- 보강한 entity:
  - `wiki/entities/oracle-database.md`
  - `wiki/entities/dbeaver.md`
- 보강한 concept:
  - `wiki/concepts/oracle-sql-basics.md`
  - `wiki/concepts/oracle-ddl-dml-transaction.md`
  - `wiki/concepts/oracle-constraints-sequence.md`
  - `wiki/concepts/oracle-referential-integrity.md`
  - `wiki/concepts/oracle-sql-functions.md`
  - `wiki/concepts/oracle-join.md`
  - `wiki/concepts/oracle-subquery.md`
  - `wiki/concepts/database-modeling-normalization.md`
  - `wiki/concepts/database-normalization-functional-dependency.md`
  - `wiki/concepts/database-view-index.md`
- 새로 추가한 comparison:
  - `wiki/comparisons/on-delete-set-null-vs-cascade.md`
  - `wiki/comparisons/ddl-vs-dml-vs-dql.md`
  - `wiki/comparisons/primary-key-vs-foreign-key.md`
  - `wiki/comparisons/oracle-inner-vs-outer-join.md`
- `wiki/index.md`에 신규 페이지 4개를 등록하고 Total pages를 176으로 갱신함.

## [2026-07-02] update | Linux course-material-aware wiki backfill

- 목적: `raw/Study/5. Linux` 사용자 정리 MD를 주 자료로 삼고, MD에서 언급된 Linux/Docker/GitHub 교육자료 PDF·PNG·보조 MD를 실제 확인해 기존 Linux 관련 wiki 1차 정리본을 재검증·보강함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. `sources`에는 사용자 정리 MD와 실제 참고한 교육자료 경로를 함께 남김.
- 참고한 대표 교육자료:
  - `raw/Study/5. Linux/교육 자료/Linux/Linux 이론.pdf`
  - `raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf`
  - `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf`
  - `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf`
  - `raw/Study/5. Linux/교육 자료/Github 교안(실습).pdf`
  - `raw/Study/5. Linux/교육 자료/AccessRights.png`
  - `raw/Study/5. Linux/교육 자료/OwnerShip.png`
  - `raw/Study/5. Linux/교육 자료/로드 밸런싱.png`
  - `raw/Study/5. Linux/교육 자료/docker image를 docker hub에 업로드 하기.md`
  - `raw/Study/5. Linux/교육 자료/도커 컴포즈 종합 실습.md`
- 보강한 summary:
  - `wiki/summaries/2026-04-22-linux-install-ssh-cli.md`
  - `wiki/summaries/2026-04-23-linux-files-vi.md`
  - `wiki/summaries/2026-04-24-linux-users-permissions.md`
  - `wiki/summaries/2026-04-27-linux-archive-java-alias.md`
  - `wiki/summaries/2026-04-28-maven-spring-boot-docker-intro.md`
  - `wiki/summaries/2026-04-29-docker-network-volume-image.md`
  - `wiki/summaries/2026-04-30-dockerfile-spring-load-balancing.md`
  - `wiki/summaries/2026-05-01-docker-compose.md`
  - `wiki/summaries/2026-05-04-git-github-sourcetree.md`
  - `wiki/summaries/2026-05-06-github-branch-pr-conflict.md`
- 보강한 concept/entity/comparison:
  - `wiki/concepts/linux-cli-files.md`
  - `wiki/concepts/linux-users-permissions.md`
  - `wiki/concepts/linux-package-archive.md`
  - `wiki/concepts/linux-spring-boot-server-deploy.md`
  - `wiki/concepts/docker-image-container.md`
  - `wiki/concepts/docker-network-volume.md`
  - `wiki/concepts/dockerfile-vs-compose.md`
  - `wiki/concepts/git-github-collaboration.md`
  - `wiki/entities/linux.md`
  - `wiki/entities/docker.md`
  - `wiki/entities/git.md`
  - `wiki/entities/source-tree.md`
  - `wiki/entities/maven.md`
- 새로 추가한 페이지:
  - `wiki/concepts/linux-web-server-apache-nginx.md`
  - `wiki/concepts/docker-install-permission-setup.md`
  - `wiki/concepts/docker-cp-exec-container-files.md`
  - `wiki/concepts/docker-reverse-proxy-load-balancing.md`
  - `wiki/concepts/docker-compose-manifest.md`
  - `wiki/comparisons/docker-commit-vs-dockerfile.md`
  - `wiki/comparisons/docker-cp-vs-bind-mount-vs-volume.md`
  - `wiki/comparisons/git-fetch-vs-pull-vs-clone.md`
- `wiki/index.md`에 신규 페이지 8개를 등록하고 Total pages를 161로 갱신함.

## [2026-07-02] update | 긴 페이지 10개 분할/정리

- 목적: 200줄을 넘는 긴 페이지 10개를 허브+하위 페이지 구조로 나눠 읽기성과 유지보수성을 높임.
- 생성한 대표 파일:
  - `wiki/_meta/wiki-log-archive-2026-06.md`
  - `wiki/_meta/wiki-log-archive-2026-07.md`
  - `wiki/concepts/java-method-constructor-overloading.md`
  - `wiki/concepts/java-object-array-memory.md`
  - `wiki/concepts/java-polymorphism-casting.md`
  - `wiki/concepts/java-interface-capability-design.md`
  - `wiki/concepts/oracle-ddl-dml-transaction.md`
  - `wiki/concepts/oracle-sequence.md`
  - `wiki/concepts/oracle-referential-integrity.md`
  - `wiki/concepts/oracle-sql-functions.md`
  - `wiki/concepts/oracle-join.md`
  - `wiki/concepts/oracle-subquery.md`
  - `wiki/concepts/database-normalization-functional-dependency.md`
  - `wiki/concepts/database-view-index.md`
  - `wiki/concepts/spring-data-jpa-specification-pageable.md`
  - `wiki/concepts/spring-product-search-flow.md`
  - `wiki/_meta/hermes-home-laptop-git-obsidian-setup.md`
  - `wiki/_meta/hermes-home-laptop-hermes-config-migration.md`
  - `wiki/_meta/hermes-home-laptop-troubleshooting.md`
  - `wiki/_meta/wiki-log-archive-2026-07-01.md`
  - `wiki/_meta/wiki-log-archive-2026-07-02.md`
  - `wiki/_meta/hermes-home-laptop-hermes-backup-security.md`
  - `wiki/_meta/hermes-home-laptop-hermes-copy-verify.md`
  - `wiki/_meta/wiki-log-archive-2026-07-02-part-1.md`
  - `wiki/_meta/wiki-log-archive-2026-07-02-part-2.md`
- 수정한 파일:
  - 긴 페이지 10개를 허브 문서로 축소하고 하위 페이지 링크를 추가함.
  - `wiki/index.md` — 새 concept/meta 페이지를 등록하고 페이지 수를 갱신함.
  - `wiki/log.md` — 월별 아카이브 링크와 이번 작업 기록 중심으로 정리함.

## [2026-07-02] update | FrontEnd_BackEnd course-material-aware wiki backfill

- 목적: `raw/Study/4. FrontEnd_BackEnd` 사용자 정리 MD 18개를 주 자료로 삼고, MD에서 언급된 교육자료 PDF/PNG를 실제 확인해 기존 FrontEnd_BackEnd 1차 wiki 정리본을 재검증·보강함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. `sources`에는 사용자 정리 MD와 실제 참고한 교육자료 경로를 함께 남김.
- 참고한 대표 교육자료:
  - `raw/Study/4. FrontEnd_BackEnd/교육 자료/FrontEnd&BackEnd.pdf`
  - `raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf`
  - `raw/Study/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf`
  - `raw/Study/4. FrontEnd_BackEnd/교육 자료/JWT(이론).pdf`
  - `raw/Study/4. FrontEnd_BackEnd/교육 자료/IT 관련 용어.pdf`
  - `raw/Study/4. FrontEnd_BackEnd/교육 자료/필드 검색 기능.pdf`
  - `raw/Study/4. FrontEnd_BackEnd/교육 자료/프로그램 흐름 그림.png`
  - `raw/Study/4. FrontEnd_BackEnd/교육 자료/라우터 설명 그림.png`
  - `raw/Study/4. FrontEnd_BackEnd/교육 자료/쇼핑 카트 데이터 구조 다이어그램.png`
  - `raw/Study/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 01.png`
  - `raw/Study/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 02.png`
- 보강한 summary: `wiki/summaries/2026-03-30-fullstack-environment-setup.md` ~ `wiki/summaries/2026-04-22-product-repository-pageable-search.md` 총 18개
- 보강한 기존 concept/comparison: `fullstack-project-flow`, `spring-boot-rest-api`, `react-typescript-basics`, `jwt-session-cookie-auth`, `dto-entity-service-controller`, `shopping-cart-flow`, `pagination-search`, `spring-data-jpa-specification-pageable`, `session-vs-cookie-vs-jwt`, `react-router-vs-spring-api-url`
- 새로 추가한 페이지:
  - `wiki/entities/intellij-idea.md`
  - `wiki/concepts/frontend-backend-architecture.md`
  - `wiki/concepts/react-form-state-event.md`
  - `wiki/concepts/react-useeffect-data-fetching.md`
  - `wiki/concepts/spring-security-jwt-filter.md`
  - `wiki/concepts/product-domain-flow.md`
  - `wiki/comparisons/mpa-vs-spa.md`
  - `wiki/comparisons/props-vs-state.md`
- `wiki/index.md`에 신규 페이지 8개를 등록하고 Total pages를 169로 갱신함.

## [2026-07-02] update | UI&UX course-material-aware wiki backfill

- 목적: `raw/Study/3. UI&UX` 사용자 정리 MD 5개를 주 자료로 삼고, MD에서 언급된 UI&UX/HTML/CSS/JS/jQuery 교육자료 PDF·PNG·소스코드를 실제 확인해 기존 UI&UX 1차 wiki 정리본을 재검증·보강함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. `sources`에는 사용자 정리 MD와 실제 참고한 교육자료/소스코드 경로를 함께 남김.
- 참고한 대표 교육자료:
  - `raw/Study/3. UI&UX/교육 자료/웹 서비스 Ui&UX.pdf`
  - `raw/Study/3. UI&UX/교육 자료/HTML&JS&CSS 이론(new).pdf`
  - `raw/Study/3. UI&UX/교육 자료/IT 관련 용어.pdf`
  - `raw/Study/3. UI&UX/교육 자료/library&framework.png`
  - `raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/tableExam.html`
  - `raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/boxModelTest.html`
  - `raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/CartList.html`
  - `raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/CartList.html`
  - `raw/Study/3. UI&UX/교육 자료/jQueryImageTest/jQueryImageTest.html`
- 보강한 summary:
  - `wiki/summaries/2026-03-23-html-css-intro.md`
  - `wiki/summaries/2026-03-24-css-layout-javascript-intro.md`
  - `wiki/summaries/2026-03-25-bootstrap-form.md`
  - `wiki/summaries/2026-03-26-javascript-dom-product-pages.md`
  - `wiki/summaries/2026-03-27-jquery-ui-interaction.md`
- 보강한 concept/entity:
  - `wiki/concepts/html-css-basics.md`
  - `wiki/concepts/javascript-dom.md`
  - `wiki/concepts/bootstrap-basics.md`
  - `wiki/concepts/jquery-basics.md`
  - `wiki/entities/html.md`
  - `wiki/entities/css.md`
  - `wiki/entities/javascript.md`
  - `wiki/entities/bootstrap.md`
  - `wiki/entities/jquery.md`
- 새로 추가한 comparison:
  - `wiki/comparisons/library-vs-framework.md`
  - `wiki/comparisons/inline-style-vs-internal-css-vs-external-css.md`
  - `wiki/comparisons/get-vs-post.md`
- `wiki/index.md`에 신규 페이지 3개를 등록하고 Total pages를 172로 갱신함.

## [2026-07-03] update | AWS date-note-aware wiki correction

- 목적: 사용자가 지정한 AWS 날짜별 MD 3개가 더 이상 시간표 템플릿이 아니라 실제 수업 메모를 포함하고 있음을 확인하고, 기존 AWS wiki summary/concept/entity/comparison을 날짜별 MD와 교육자료 PDF/실습 관리 대장 기준으로 재검토·보강함.
- 원칙: `raw/Study/6. AWS`는 읽기 전용으로 유지했고, 사용자가 제외 지시한 AWS 총정리류는 건드리지 않음. 원본에 있는 실습용 공개 IP, RDS endpoint, DB 비밀번호 예시는 wiki에 그대로 재노출하지 않고 placeholder/보안 메모로 일반화함.
- 보강한 summary:
  - `wiki/summaries/2026-05-06-aws-cloud-vpc-ec2.md`
  - `wiki/summaries/2026-05-07-aws-ec2-nginx-rds.md`
  - `wiki/summaries/2026-05-08-aws-route53-load-balancer-https.md`
- 보강한 concept/entity/comparison:
  - `wiki/concepts/aws-cloud-vpc-networking.md`
  - `wiki/concepts/aws-ec2-nginx-spring-deploy.md`
  - `wiki/concepts/aws-rds-spring-boot.md`
  - `wiki/concepts/aws-route53-load-balancer-https.md`
  - `wiki/entities/aws.md`, `wiki/entities/amazon-ec2.md`, `wiki/entities/amazon-rds.md`, `wiki/entities/amazon-route-53.md`
  - `wiki/comparisons/ec2-vs-rds.md`, `wiki/comparisons/clb-vs-alb.md`
- `wiki/index.md`의 AWS 항목 설명을 최신화했고, 신규 페이지는 만들지 않아 Total pages는 189를 유지함.

## [2026-07-03] ingest | 1~4 과목 총정리 MD 균등 재점검/보강

- 목적: `raw/Study/1. Java` ~ `raw/Study/4. FrontEnd_BackEnd`의 과목별 총정리 MD 4개를 기준으로, 날짜별 summary를 대체하지 않는 복습 허브를 만들고 기존 과목 entity와 연결함.
- 참고한 원본:
  - `raw/Study/1. Java/Java 총정리/Java 총정리.md`
  - `raw/Study/2. Oracle/Oracle 총정리/Oracle 총정리.md`
  - `raw/Study/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
  - `raw/Study/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md`
- 새로 추가한 summary:
  - `wiki/summaries/2026-03-13-java-subject-review.md`
  - `wiki/summaries/2026-03-20-oracle-subject-review.md`
  - `wiki/summaries/2026-03-27-uiux-subject-review.md`
  - `wiki/summaries/2026-04-03-frontend-backend-subject-review.md`
- 보강한 허브 entity:
  - `wiki/entities/java.md`
  - `wiki/entities/oracle-database.md`
  - `wiki/entities/html.md`
  - `wiki/entities/spring-boot.md`
- `wiki/index.md`에 신규 summary 4개를 등록하고 Total pages를 193으로 갱신함.

## [2026-07-03] ingest | 5~10 선행 작업 묶음

- 목적: 사용자가 지정한 선행 순서에 따라 5~6 과목 총정리 생성, 7~8 날짜별 raw 변환, 9 중간 프로젝트 가이드 ingest, 10 Python 날짜별 raw 변환을 한 묶음으로 진행함.
- raw 변환/생성:
  - `raw/Study/5. Linux/Linux 총정리/Linux 총정리.md`
  - `raw/Study/6. AWS/AWS 총정리/AWS 총정리.md`
  - `raw/Study/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md` ~ `raw/Study/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md`
  - `raw/Study/8. Passwordless/2026.05.14(목)/2026.05.14(목).md` ~ `raw/Study/8. Passwordless/2026.05.21(목)/2026.05.21(목).md`
  - `raw/Study/10. Python/2026.06.19(금)/2026.06.19(금).md` ~ `raw/Study/10. Python/2026.06.30(화)/2026.06.30(화).md`
- 9번 프로젝트 가이드 신규 wiki 페이지:
  - `wiki/summaries/2026-05-middle-project-cicd-passwordless-guide.md`
  - `wiki/concepts/middle-project-cicd-deploy-flow.md`
  - `wiki/concepts/github-actions-secrets-deploy.md`
  - `wiki/concepts/jwt-rs256-key-flow.md`
  - `wiki/concepts/passwordless-x1280-auth-flow.md`
  - `wiki/comparisons/passwordless-vs-password-login.md`
- 보안 원칙: 원본 가이드에 포함될 수 있는 IP, endpoint, password, secret 값은 wiki 본문에서 placeholder와 역할 설명으로 일반화함.

## [2026-07-03] ingest | 5~6 과목 총정리

- 목적: `raw/Study/5. Linux/Linux 총정리/Linux 총정리.md`와 `raw/Study/6. AWS/AWS 총정리/AWS 총정리.md`를 날짜별 summary를 대체하지 않는 복습 허브로 wiki에 반영함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. 기존 Linux/AWS 날짜별 wiki와 entity 페이지를 우선 보강하고, 총정리 원본은 subject-review summary로 연결함.
- 새로 추가한 summary:
  - `wiki/summaries/2026-05-06-linux-subject-review.md`
  - `wiki/summaries/2026-05-08-aws-subject-review.md`
- 보강한 허브 entity:
  - `wiki/entities/linux.md`
  - `wiki/entities/docker.md`
  - `wiki/entities/aws.md`
- `wiki/index.md`에 신규 summary 2개를 등록하고 Total pages를 201로 갱신함.
