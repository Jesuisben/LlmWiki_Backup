# Wiki Log

> 이 파일은 위키 작업의 시간순 기록이다.  
> append-only로 운영한다. 과거 기록을 임의로 삭제하지 않는다.  
> 형식: `## [YYYY-MM-DD] action | subject`  
> action 예시: `create`, `ingest`, `update`, `query`, `lint`, `archive`, `delete`


## 로그 아카이브

- [[_meta/wiki-log-archive-2026-06|Wiki Log Archive 2026-06]] — 2026년 6월 작업 기록
- [[_meta/wiki-log-archive-2026-07|Wiki Log Archive 2026-07]] — 2026년 7월 작업 기록 중 이번 분할 전까지의 기록

## 현재 로그

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
