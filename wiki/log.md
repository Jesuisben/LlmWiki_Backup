# Wiki Log

> 이 파일은 위키 작업의 시간순 기록이다.  
> append-only로 운영한다. 과거 기록을 임의로 삭제하지 않는다.  
> 형식: `## [YYYY-MM-DD] action | subject`  
> action 예시: `create`, `ingest`, `update`, `query`, `lint`, `archive`, `delete`


## 로그 아카이브

- [[_meta/wiki-log-archive-2026-06|Wiki Log Archive 2026-06]] — 2026년 6월 작업 기록
- [[_meta/wiki-log-archive-2026-07|Wiki Log Archive 2026-07]] — 2026년 7월 작업 기록 중 이번 분할 전까지의 기록

## 현재 로그

## [2026-07-19] update | Python 계획 Meta 비동기 전수 감사 정정

- 정정 사유: 계획 세션 종료 뒤 도착한 raw·직접 페이지·경계 페이지 병렬 전수 감사 결과를 기존 Meta 분류와 대조해, 휴리스틱 초안의 직접 페이지 분류와 경계 후보가 과도했음을 확인했다.
- 직접 페이지: 총 32개와 `summary 15 / concept 9 / entity 7 / comparison 1 / query 0`은 유지한다. 페이지별 내용을 전수 판독한 단일 분류는 `유지 2 / 부분 보강 13 / 전면 재작성 17 / 통합 0 / 근거 부족 0`으로 정정했다.
- 비직접 경계: 탐색 허브·과목 전체 허브·키워드 언급·책임 불명확 페이지를 제외해 `선행 5 / 교차 3 / 후속 0`, 총 8개로 정정했다. 직접 페이지 32개와 합산하지 않는다.
- 후보 벡터: Concept 3개(예외 처리·정규표현식·XML/JSON), Entity 1개(BeautifulSoup), Comparison 3개(`loc/iloc`, `concat/merge/pivot`, `agg/transform`), Query 0개로 보수화했다.
- 증거 보강: Python source 9개 AST 통과, R01의 오류→수정→정상 결과, CSV 구조 이상과 R04·R06·R09·R13 code 불일치 후보, Jupyter claim-level source 후보를 Meta에 기록했다. 실제 식별값은 재출력하지 않았다.
- 상태: raw 시작·종료 manifest 불일치와 최초 분류 정정 이력 때문에 계획 세션과 단계 10 전체는 계속 미완료다. 기존 지식 본문·raw·상위 완료 표는 수정하지 않았고 Git commit·push도 수행하지 않았다.

## [2026-07-19] update | Python 내용 재고도화 재고·분할 계획 미완료

- 범위: 단계 10 계획 세션으로 `raw/KoreaICT/10. Python` 실제 파일 69개와 frontmatter source 기준 직접 지식 페이지 32개를 전수 재계산했다. 기존 지식 본문과 상위 단계 완료 표는 수정하지 않았다.
- raw 재고: Markdown 16·PDF 3·CSV 31·Python source 9·bytecode 6·PNG 4, 총 69개다. notebook·독립 JSON/XML/HTML·config·archive는 0개이며, 0바이트 3개와 byte-identical 중복 2그룹을 확인했다.
- 직접 페이지: `summary 15 / concept 9 / entity 7 / comparison 1 / query 0`, 총 32개다. raw source union은 날짜 노트 14개와 총정리 1개인 15/69이고, 나머지 54개는 교육자료·dataset·source·generated artifact로 역할을 분류했다.
- 증거 경계: code·text output·Traceback·dataset·DataFrame/통계/그래프·CSV·이미지·bytecode와 현재 raw에 없는 notebook·saved map HTML·독립 API/browser 결과를 분리했다. 직접 page fence 16개 중 원문 연속 일치 3개, 재판정 후보 13개를 기록했다.
- 실행 분할: 계획을 포함해 Summary 전반, Summary 후반·총정리, Python core Concept, Pandas·외부 데이터 Concept, Entity, Comparison·Query, 전체 고정점의 8개 세션을 제안했다.
- 보류 사유: 조사 중 기존 modified 상태였던 `2026.07.01(수).md`의 bytes·줄·SHA-256이 바뀌어 시작 manifest와 최신 manifest가 달라졌다. Agent는 raw 쓰기를 수행하지 않았지만 raw 안정성 게이트를 충족하지 못했으므로 계획 세션과 단계 10 전체를 완료로 선언하지 않았다.
- 기록: [[_meta/python-rehighquality-inventory-plan|Python 내용 재고도화 전수 재고와 실행 분할 계획]]을 생성하고 index `Total pages`를 280으로 갱신했다. Git commit·push는 수행하지 않았다.

## [2026-07-19] lint | 중간 프로젝트 공부 실용형 세션 2 전체 고정점·단계 9 완료

- 범위: 단계 9 두 번째이자 최종 실행 단위로 기존 `passwordless-vs-password-login`을 고도화하고 HS256/RS256, workflow 정의/실행 결과, polling/callback, local file/object storage, 실제 장애 Query 후보를 전수 판정한 뒤 직접 15페이지와 raw 4개 전체 고정점을 처리했다. 단계 10 Python은 시작하지 않았다.
- Comparison·Query: 기존 로그인 Comparison은 비밀번호/JWT 기준선과 Passwordless 외부 승인 뒤 application session/JWT·인가 책임, 단계 9 polling·callback 부재·challenge/session 결속을 비교하는 독립 책임이 있어 유지·고도화했다. HS256/RS256·workflow 정의/실행·local/object storage는 기존 Concept·Entity·Summary에 흡수했고, polling/callback은 raw가 polling만 제공하므로 신규 기각했다. 실패 관찰은 있으나 원인→수정→재검증 이력이 없어 장애 Query도 만들지 않았다.
- 증거 경계: embedded snippet·부분 출력·관찰 서술·실패 관찰·조건/지시·독립 end-to-end 결과를 분리했다. 관리형 DB 계획/VM DB container, DB URL 주입/application 소비, test 생략/test 성공, object 삭제 설명 충돌, Secret 등록/전달 불일치, polling/timeout/error, 승인 결과/JWT·인가 경계를 유지했다.
- 구조·보안: 직접 페이지는 `summary 1 / concept 6 / entity 7 / comparison 1 / query 0`, 총 15개이며 raw source union 4/4다. frontmatter·source·본문 출처·tag·type·link·index·고립·placeholder·빈 sources·장문·needs-review/low-confidence·fence 오류 0개이고, 변경 추가행의 실제 민감 식별값 노출 지표도 0개다.
- 고정점: actual page 수와 index `Total pages`는 279/279다. raw는 4개·170,194 bytes·Markdown 4,481줄이며 시작·종료 scoped status/diff 0건, 정렬 SHA-256 manifest digest `1d77c60dbfa22cf5f9173b897b1e0ddb0906b98ff9b543a1ba476d7b13d2a50f`가 세션 1 최종값과 동일하다. scoped `git diff --check`를 통과했고 commit·push는 하지 않았다.
- 단계 상태: 단계 9 중간 프로젝트 공부를 최종 완료로 확정했다. 다음 작업 단위는 단계 10 Python의 실제 재고·직접 페이지 범위를 먼저 확정하는 계획 세션이다.

## [2026-07-19] update | 중간 프로젝트 공부 실용형 세션 1 재고·Summary·Concept·Entity 고도화

- 범위: 단계 9 첫 실행 단위로 `raw/KoreaICT/9. 중간 프로젝트 공부` 실제 파일 4개를 다시 계산하고, frontmatter source 기준 직접 지식 페이지를 세션 시작 9개에서 Summary 1·Concept 6·Entity 7·Comparison 1·Query 0, 총 15개로 확정했다. Comparison·Query 최종 판단과 단계 9 전체 완료는 다음 세션으로 남겼다.
- raw 재고: Markdown 4개·4,481줄·170,194 bytes, PDF/JSON/image/archive/독립 source/config/script 0개, 0바이트·byte-identical 중복 0개다. R01~R04는 Secret 역할 목록, RS256 key 생성 절차, CI/CD·배포 가이드, Passwordless 적용 가이드로 분류했다.
- Summary: `2026-05-middle-project-cicd-passwordless-guide`를 backend→Docker/AWS→Actions→React/Nginx→file/S3→DNS/ALB와 Passwordless server→Spring REST→React polling 흐름으로 전면 고도화하고, embedded snippet과 독립 project artifact·실행 결과를 분리했다.
- Concept: 배포 완료 사다리, Secret 저장→주입→소비→비노출 검증, RS256 key 생성→서명→검증→Authentication→인가, Passwordless Member/REST/Service/Controller/SecurityConfig/React polling의 written-vs-wired-vs-runtime 경계를 보강했다. raw와 불일치한 합성 text fence 1개를 제거해 직접 페이지 fence를 0개로 만들었다.
- 후속 병렬 감사 교정: 단계 9 raw에 포함된 일부 shell·인증서·container 파일·거부 HTTP 응답과 성공/실패 관찰을 복원했다. DB 관리형 계획과 VM container 상세 절차, DB URL 주입과 설정 소비, object 삭제 설명, Passwordless Secret 전달의 불일치를 `미확정`으로 기록했다. backend test 생략, polling과 외부 callback 미구현, timeout·오류 혼합, challenge/session 결속·공개 endpoint·local 상태 drift도 Concept에 반영했다.
- Entity: GitHub·Docker·AWS·Spring Boot·React·JWT·Passwordless 제품에 단계 9 학습 이력과 실제 프로젝트 역할을 누적했다. workflow template, Dockerfile, cloud 절차, Java/TypeScript snippet을 run·image·resource·API/browser/DB 성공으로 과확정하지 않았다.
- 경계: Linux·AWS·CI/CD·Passwordless 직접 수업 결과와 단계 9 적용 가이드를 분리했다. 단계 8 결과를 단계 9에 소급하거나 단계 9 설계를 05월 Passwordless 실행 결과로 되돌리지 않았다.
- 기록: `_meta/middle-project-rehighquality-inventory-plan`을 생성하고 index `Total pages`를 279로 갱신했다. 상위 작업 계획의 단계 9 완료 행은 추가하지 않았다.
- Git: `raw/KoreaICT/9. 중간 프로젝트 공부`는 시작·종료 scoped status/diff 0건과 정렬 SHA-256 manifest 동일 여부를 확인했다. commit·push는 수행하지 않았다.

## [2026-07-18] lint | Passwordless 실용형 세션 2 전체 고정점·단계 8 완료

- 범위: 단계 8 Passwordless 두 번째이자 최종 실행 단위로 기존 Comparison 2개 유지·고도화, 신규 Comparison 4개·Query 1개 후보 판단, frontmatter source 기준 직접 15페이지와 raw 20개 전체 고정점을 처리했다. 단계 9 중간 프로젝트 본문은 시작하지 않았다.
- Comparison: `passwordless-vs-password-login`은 비밀번호/JWT 기준선과 05-15 서비스·Docker·사용자/인증기 등록, 05-18 샘플 관찰, 05-21 등록 상태 조회 응답 1건, 외부 인증 뒤 session/JWT·endpoint 인가 경계를 분리했다. `authentication-vs-authorization`은 신원 확인, role·ownership·endpoint 판단, AAM/APE 조직 관리, FilingBox RO/RW/AO/WORM operation을 서로 다른 완료 상태로 고정했다.
- 신규 판단: 등록 vs 로그인 vs 해제, AAM vs APE, 인증 보안 vs WORM, REST 등록 확인 vs 실제 사용자 인증은 기존 Concept·Entity가 검색 책임을 충분히 소유해 모두 신규 기각했다. 실제 장애→원인→수정→재검증 이력이 없어 Spring 로그인 장애 Query도 만들지 않고 연동 Concept의 진단 checklist로 흡수했다.
- 직접 결과 경계: 05-14 실행 결과 0, 05-15 일부 상태·plugin 관찰, 05-18 DB·샘플 관찰과 단계별 응답 미보존, 05-19 일부 상태·전달 확인 서술, 05-20 절차·명령만 보존, 05-21 등록 상태 조회 JSON 1건으로 확정했다. 교육 PDF와 Postman saved response는 교육 입력자료다.
- 구조·fence·보안: 직접 페이지는 `summary 7 / concept 4 / entity 2 / comparison 2 / query 0`, 총 15개이며 raw source union 20/20이다. frontmatter·source·tag·link·index·고립·placeholder·빈 sources·장문·needs-review/low-confidence 오류 0개, JSON fence 1/1 원문 연속 일치, `bash` 0개, 실제 민감 식별값 노출 지표 0개다.
- 고정점: 실제 page 수와 index `Total pages`는 278/278이다. Passwordless raw는 시작·종료 scoped status/diff 0건이고 정렬된 20개 SHA-256 manifest digest `88645aa40d8e3a533ee916009e999a6c32de4eb49dbb0f103812f93f9ec0fd90`가 동일하다. scoped `git diff --check`를 통과했고 commit·push는 하지 않았다.
- 단계 상태: 단계 8 Passwordless를 최종 완료로 확정했다. 다음 작업 단위는 단계 9 중간 프로젝트 공부 실용형 첫 세션이며 이 세션에서는 시작하지 않았다.

## [2026-07-18] update | Passwordless 실용형 세션 1 전수 재고·핵심 지식 고도화

- 범위: 단계 8 Passwordless 첫 실행 단위로 `raw/KoreaICT/8. Passwordless` 20개를 R01~R07·P01~P11·J01~J02에 전수 대응하고, frontmatter source 기준 직접 지식 페이지를 최종 `summary 7 / concept 4 / entity 2 / comparison 2 / query 0`, 총 15개로 재계산했다. 단계 9 중간 프로젝트 본문은 시작하지 않았다.
- raw 재고: 날짜 MD 6·총정리 MD 1·PDF 11·Postman JSON 2, 총 39,906,657 bytes·Markdown 2,190줄·0바이트 0개·과목 내부 중복 0개다. image·archive·독립 실행 artifact와 독립 Java/properties/YAML/XML/shell/SQL source는 0개이며 PDF 11개는 모두 text 추출 가능했다.
- 내용 고도화: 기존 Summary 6·Concept 4·Entity 2를 전면 고도화하고 `Passwordless 총정리` Summary를 신설했다. Summary는 날짜 순서와 직접 결과/미보존 결과, Concept는 구성요소·상태·완료 조건, Entity는 첫 등장·학습 이력과 제품 경계를 소유하도록 분리했다.
- 결과 경계: 05-14 실행 결과 0, 05-15 일부 상태·plugin 성공 관찰, 05-18 DB 결과·등록/로그인/해제 관찰과 미보존 단계별 API/화면, 05-19 일부 service 상태·사용자 전달 확인 서술, 05-20 설정·명령만 보존, 05-21 등록 여부 JSON 한 건 직접으로 고정했다. 교육 PDF와 완성형 Postman saved response는 사용자 실행 결과로 세지 않았다.
- fence·보안: 시작 직접 14페이지 fence 11개 중 합성·비연속 text diagram 10개를 prose/table로 바꾸고, 05-21 raw와 연속 일치하는 JSON 1개만 유지했다. `bash`는 0개다. 실제 account·contact·domain·IP·endpoint·organization·service/license/key/token/password/DB/X1280·AAM·APE 식별값은 wiki와 기록에 옮기지 않았다.
- 기록·단계 상태: [[_meta/passwordless-rehighquality-inventory-plan|Passwordless 내용 재고도화 전수 재고와 실용형 실행 계획]]을 생성하고 index에 총정리 Summary·Meta를 등록해 실제 page 수와 `Total pages`를 278로 맞췄다. 신규 Comparison·Query는 만들지 않았고 후보만 inventory에 남겼다. 단계 8 전체 완료 행은 상위 계획에 추가하지 않았다.
- 검증·raw/Git: 직접 15페이지 전수 분류·raw source union 20/20, frontmatter/source/body/tag/link/index/orphan/placeholder/empty/low-confidence·fence·민감정보·날짜/과목 경계·actual page count 검사를 통과했고 scoped `git diff --check`도 통과했다. Passwordless raw scoped status/diff는 시작·종료 모두 0건이며 정렬된 20개 SHA-256 manifest digest는 시작·종료 모두 `88645aa40d8e3a533ee916009e999a6c32de4eb49dbb0f103812f93f9ec0fd90`이다.

## [2026-07-18] fix | CI/CD 세션 2 비동기 감사 후속 교정

- 독립 Comparison·날짜/Query 감사 결과를 완료본과 다시 대조했다. 구조 감사는 직접 19페이지·fence 3개·source/link/index에서 오류 0건을 재확인했다.
- 05-13 S3 첫 실패→policy 수정→재시도 성공·bucket object 확인은 원본 메모에 보존된 실행 관찰 서술이지만 listing·API 응답·screenshot은 없다. 이를 1차 결과처럼 읽히게 하던 Summary·Concept·Entity·inventory 표현을 교정했다.
- 05-11 workflow의 `-DskipTests`가 테스트 성공이 아니라 테스트를 생략한 Maven package 절차임을 Summary와 GitHub Actions Concept에 명시했다.
- Comparison 감사의 S3/RDS·CI/CD/Terraform 신설 권고는 기존 페이지가 역할·검증 경계를 이미 소유하고 반복 혼동 근거가 부족해 채택하지 않았다. `clb-vs-alb` 흡수 권고도 P04 일반 이론 출처·직접 근거 축소·`confidence: medium`으로 독립 비교 책임을 제한해 유지했다. Query 0개 판단은 감사와 일치했다.
- 후속 교정 뒤 직접 페이지 구조·출처·fence·민감정보·page count·scoped diff와 raw manifest를 다시 검증했다. 단계 7 완료 상태는 유지하며 단계 8은 시작하지 않았다.

## [2026-07-18] lint | CI/CD 실용형 세션 2 전체 고정점·단계 7 완료

- 범위: 단계 7 CI/CD 두 번째이자 최종 실행 단위로 `clb-vs-alb` 최종 고도화, Comparison·Query 후보 판단, frontmatter source 기준 직접 19페이지와 R01~R04·P01~P04 전체 고정점을 처리했다. 단계 8 Passwordless 본문은 시작하지 않았다.
- Comparison·Query: `clb-vs-alb`는 CLB 예정 항목/ALB 구성 절차/일반 기능/미보존 결과를 분리해 유지했다. Route 53/ALB, S3/RDS, CI/CD/Terraform 및 세부 후보는 기존 페이지가 검색 책임을 흡수해 신규 생성하지 않았다. 실제 장애 질문·해결 이력이 완전히 보존되지 않아 Query도 0개를 유지했다.
- 내용·경계: 05-11 Docker group/version·container `Up`·80→9000 mapping, 05-12 절차만 보존, 05-13 Terraform version·apply 오류·S3 재시도 성공을 직접 결과로 고정했다. Actions/JAR/image/SSH/browser, DNS/ACM/target/ALB/삭제, 최종 Terraform apply/destroy·독립 artifact·RDS query 결과는 미보존이다.
- 구조·fence·보안: 직접 페이지는 `summary 3 / concept 9 / entity 6 / comparison 1 / query 0`, 총 19개이며 R01~R04·P01~P04 source union 8/8이다. frontmatter·source 실경로·본문 출처 동기화·tag·link·index·고립·placeholder·빈 sources·장문·needs-review/low-confidence 오류 0개, YAML 1·XML 2 fence 3/3 원문 연속 일치, `bash` 0개, 민감정보 노출 지표 0개다.
- 고정점: 실제 page 수와 index `Total pages`는 276/276이다. CI/CD raw는 시작/종료 scoped status·diff 0건이고 정렬된 8개 SHA-256 manifest digest `c1facebda686016a17322d4d65c09c40ab880b968d032189a5fac2c92ceceff1`가 동일하다. scoped `git diff --check`를 통과했고 commit·push는 하지 않았다.
- 단계 상태: 단계 7 CI/CD를 최종 완료로 확정했다. 다음 작업 단위는 단계 8 Passwordless 실용형 첫 세션이며 이 세션에서는 시작하지 않았다.

## [2026-07-18] update | CI/CD 실용형 세션 1 전수 재고·핵심 지식 고도화

- 범위: 단계 7 CI/CD 첫 실행 단위로 `raw/KoreaICT/7. Ci&CD` 8개를 R01~R04·P01~P04에 전수 대응하고, frontmatter source 기준 직접 지식 페이지 19개를 `summary 3 / concept 9 / entity 6 / comparison 1 / query 0`으로 재계산했다. 단계 8 Passwordless 본문은 시작하지 않았다.
- raw 재고: 날짜 MD 3·총정리 MD 1·PDF 4, 총 23,226,472 bytes·Markdown 1,466줄·0바이트 0개·과목 내부 중복 0개다. P04는 AWS 과목의 동일 교안과 byte-identical이다. 독립 source/config/script와 image/artifact는 0개다.
- 내용 고도화: Summary 3·Concept 9·Entity 6에서 05-11 workflow/명령과 보존된 Docker/container 결과, 05-12 DNS·ACM·ALB 절차와 미보존 결과, 05-13 Terraform version·apply 오류·S3 재시도 성공·RDS query 미보존을 분리했다. Linux 선행, AWS 05-06~08 직접, CI/CD 직접, Passwordless·중간 프로젝트 후속 책임을 분리했다.
- fence·보안: 직접 페이지의 시작 fence 18개 중 비연속 축약·합성 diagram/config/workflow 15개를 prose/table로 바꾸고, 원본 연속 YAML 1·XML 2만 유지했다. 최종 3/3 원문 일치·`bash` 0개다. 기존 `clb-vs-alb`는 최종 판단을 다음 세션에 남기되 실제 resource 이름과 접속 성공 과확정만 최소 교정했다. 실제 account·email·repository URL·IP·domain·endpoint·Key Pair/resource 이름·password·token·credential·AWS identifier 노출 지표는 0개다.
- 구조 검증: 직접 19페이지의 frontmatter·source 실경로·허용 tag·링크·index·고립·placeholder·빈 sources·200줄 초과·needs-review/low-confidence 오류 0개다. 새 Meta를 index에 등록했고 실제 page 수와 `Total pages`는 276으로 일치한다.
- raw/Git: 시작과 검증 시점의 CI/CD raw scoped status/diff는 0건이며, 8개 정렬 SHA-256 manifest digest는 `c1facebda686016a17322d4d65c09c40ab880b968d032189a5fac2c92ceceff1`로 동일하다. 변경 scope의 `git diff --check`를 통과했고 commit·push는 수행하지 않았다.
- 기록: [[_meta/cicd-rehighquality-inventory-plan|CI/CD 내용 재고도화 전수 재고와 실용형 실행 계획]]을 생성했다. 신규 Comparison·Query는 만들지 않았으며 후보와 판단 근거만 inventory에 남겼다. 단계 7 전체 완료 행은 상위 계획에 추가하지 않았다.
- 비동기 독립 감사 반영: 동시 수정 전 지적을 최신 본문과 재대조해 이미 해결된 Route 53·S3·RDS·05-12 항목을 확인하고, 남아 있던 AWS→Passwordless 무출처 확장과 CLB/ALB의 일반 기능·직접 근거 혼합을 교정했다. frontmatter에 선언한 `Ci&CD 총정리.md`가 본문 출처에서 빠진 13페이지도 동기화했다.

## [2026-07-18] lint | AWS 실용형 세션 2 전체 고정점·단계 6 완료

- 범위: 단계 6 AWS 두 번째이자 최종 실행 단위로 `ec2-vs-rds` 고도화, Query 최종 판단, 직접 source 지식 페이지 12개와 R01~R04·P01~P05, Linux 선행·CI/CD 05-11~13 후속 경계를 한 번에 검증했다. 단계 7 CI/CD 본문은 수정하지 않았다.
- Comparison·Query: `ec2-vs-rds`를 EC2 process 실행/RDS data 계층, endpoint·3306·Security Group, 비용·삭제, 명령과 미보존 결과 중심으로 재구성했다. Multi-AZ·Read Replica는 05-08 직접 실습 결과가 아닌 일반 기능으로 분리했다. 독립 질문 기록이 없고 기존 Concept·Comparison이 혼동을 흡수하므로 AWS Query는 신규 **0개 유지**로 확정했다.
- 내용·경계: 05-06 메뉴·이론, 05-07 VPC·EC2·EIP·SSH, 05-08 ICMP 성공과 Nginx·Spring·RDS/JDBC 절차를 재대조했다. 실제 출력이 없는 browser·build·DB query·application·삭제 결과를 성공으로 확대하지 않았고 Linux process/port와 CI/CD Actions·Route 53·ACM·ALB·Terraform·S3 책임을 분리했다.
- 구조·보안: 직접 12페이지는 `summary 4 / concept 4 / entity 3 / comparison 1 / query 0`이며 frontmatter·source 실경로·허용 tag·링크·index·고립·placeholder·빈 sources·장문·needs-review/low-confidence 오류 0개다. fence·`bash`는 0개이며 실제 account·email·IP·endpoint·Key Pair/resource·DB 이름·password·token·credential·AWS identifier 노출 지표도 0개다.
- 고정점: 실제 page 수와 index `Total pages`는 275/275다. AWS raw는 9개·23,952,751 bytes·MD 1,454줄이며 시작/종료 scoped status·diff 0건, 정렬된 SHA-256 manifest digest `b185d92d5866e27d1593681db97bbe8709059debdc3eef56527b5b220d51e2af` 무변경을 확인했다. AWS scoped `git diff --check`를 통과했고 commit·push는 하지 않았다.
- 단계 상태: 단계 6 AWS를 최종 완료로 확정했다. 다음 작업 단위는 단계 7 CI/CD 실용형 첫 세션이며 이 세션에서는 시작하지 않았다.

## [2026-07-18] update | AWS 실용형 세션 1 재고·핵심 지식 고도화

- 범위: 단계 6 AWS 첫 실행 단위로 `raw/KoreaICT/6. AWS` 9개를 R01~R04·P01~P05로 전수 재고화하고, 직접 source 지식 페이지를 `summary 4 / concept 4 / entity 3 / comparison 1 / query 0`, 총 12개로 재계산했다. 단계 7 CI/CD 본문은 시작하지 않았다.
- raw·대응: 날짜 MD 3개·AWS 총정리 1개·교육자료 MD 1개·PDF 4개를 실제 경로·쪽수·중복·역할과 대응했다. 과목 내부 byte-identical 중복은 0개이고 P04 PDF 1개만 CI/CD 교육자료와 동일하다. 교육자료는 이론·화면 절차 보조이며 날짜 MD에 없는 수업일·성공 결과를 만들지 않았다.
- 핵심 고도화: 지정 Summary 4·Concept 4·Entity 3의 실제 내용 공백과 과확정만 교정했다. 05-06 메뉴·Subnet·IP/CIDR 사전 학습, 05-07 VPC·IGW·Route·SG·EC2·EIP·SSH, 05-08 ICMP·Nginx·Spring·RDS를 분리하고, 출력으로 확인된 ping 성공과 명령·설정만 남은 Nginx/browser·JAR·RDS SQL/JDBC·삭제 상태를 구분했다.
- 경계·fence·보안: Linux의 VirtualBox·SSH·UFW·Nginx·JAR·iptables, AWS의 VPC·Subnet·IGW·Route·SG·EC2·EIP·RDS, CI/CD 05-11~13의 Actions·Route 53·ACM·Target Group·ALB·HTTPS·Terraform·S3 책임을 분리했다. 직접 페이지의 합성 fence 12개를 표·prose로 바꿔 최종 0개로 만들었고 실제 account·email·IP·endpoint·Key Pair/resource 이름·password·token·credential을 변경분에 옮기지 않았다.
- 기록: `wiki/_meta/aws-rehighquality-inventory-plan.md`를 생성해 raw↔wiki 대응표·2개 세션 계획·다음 완료 게이트를 고정했다. 새 Meta 1개를 index에 등록하고 설명을 갱신했으며 실제 page count와 `Total pages`를 275/275로 맞췄다. 새 지식 페이지·Comparison·Query는 만들지 않았다.
- 단계 상태: 세션 1의 재고와 핵심 Summary·Concept·Entity는 완료했다. 단계 6 AWS 전체와 상위 작업 계획 완료 행은 미완료이며, 다음 세션에서 `ec2-vs-rds`·Query 0개 유지 판단·직접 12페이지 전체 고정점을 한 번에 처리한다. Git commit·push는 하지 않았다.

## [2026-07-18] fix | Linux 세션 10 비동기 감사 후속 교정

- 비동기 Summary·Concept/Entity·Comparison/후속 경계 감사 3계통의 지적을 raw R06~R10·AWS 05-07~08·CI/CD 05-12와 직접 재대조했다. 1차 완료 보고를 최종 근거로 삼지 않고 실제 오류를 모두 교정한 뒤 고정점을 다시 실행했다.
- 완료 상태: R06은 login→tag→push digest까지만 완료하고 remote pull/run은 올바른 명령만 존재함을 고정했다. R07은 container `Up`·DB row와 결과 미보존 Spring log/browser를, R08은 첫 Compose의 `Up`·DB 결과와 미보존 browser/down, WordPress 명령·volume 이름 불일치를 분리했다. R10의 닫히지 않은 `user.email` 명령은 정상 설정 완료로 확정하지 않았다.
- 후속 경계·탐색: 05-07 VPC·EC2와 05-08 Nginx·Spring·RDS를 분리하고 ALB·Target Group·Route 53·ACM을 05-12 CI/CD 후속으로 귀속했다. CLB 예정 이름과 실제 ALB 생성 결과를 분리하고 Linux 직접 페이지↔05-07·05-08·05-12 Summary 링크를 보강했다. `dockerfile-vs-compose` index 등록은 파일 경로를 유지한 채 frontmatter type에 맞춰 Comparisons로 옮겼다.
- 상태: 전체 구조·source·링크·page count·fence·민감정보·scoped diff·raw Linux 무변경 검증을 다시 통과한 뒤 단계 5 Linux 최종 완료를 확정했다. AWS 단계 6과 Git commit·push는 시작하지 않았다.

## [2026-07-18] lint | Linux 과목 전체 고정점 완료

- 범위: 단계 5 Linux 세션 10으로 직접 source 지식 페이지 39개, 후속 경계 15개, raw R01~R11·P01~P10·I01~I03, 신규 페이지·중요 허브·code fence를 전수 검증했다. AWS 단계 6은 시작하지 않았다.
- 세션 9 재확인: patch 경고 대상 기존 6개는 실제 본문·Git diff·신규 2개·index·log·inventory를 상호 대조해 보강 내용이 모두 반영됐음을 확인했다. 경고 문구를 미수정 근거로 사용하지 않았다.
- 직접 페이지·raw 대응: 디렉터리 기준 `summary 11 / concept 15 / entity 6 / comparison 6 / query 1`, frontmatter type 기준 `summary 11 / concept 14 / entity 6 / comparison 7 / query 1`로 총 39개다. R01~R11은 실제 경로·직접 source union·대표 artifact 대응 11/11, P01~P10·I01~I03 inventory 대응은 10/10·3/3이다.
- 최소 교정: 신규 sudo/root Comparison과 permission Query가 상호 링크에만 의존하지 않도록 04-24·04-27 Summary, Linux 권한 Concept, Linux Entity에 관련 링크 8개를 보강했다. 그 밖의 세션 2~9 본문과 후속 경계 15개는 다시 쓰지 않았다.
- 구조·내용: 필수 frontmatter·type·status·confidence·허용 tag·source 실경로·깨진 링크·고립·index 누락·등록 중복·actionable placeholder·needs-review/low-confidence 오류 0건이다. 실제 page 수와 index 등록은 274/274로 일치해 `wiki/index.md`는 수정하지 않았다. 200줄 초과 지식 페이지는 0개이며 장문 inventory는 대응표·실행 이력 보존 때문에 유지했다.
- fence·보안: 직접 39개 전체 fence는 R07 exact 원문과 일치하는 `nginx` 1개뿐이며 미처리 0·`bash` 0이다. Linux wiki 변경분의 실제 account·email·repository URL·password·PAT·token·credential·one-time code 노출 지표는 0건이다.
- Git·상태: scoped `git diff --check`를 통과했고 `raw/KoreaICT/5. Linux` status/diff는 0건이다. Linux 범위 밖 기존 Python raw 변경은 보존했으며 Git commit·push는 하지 않았다. 단계 5 Linux를 최종 완료로 기록하고 다음 실행 단위를 단계 6 AWS 실용형 첫 세션으로만 남겼다.

## [2026-07-18] update | Linux 최종 Comparison/Query 고도화

- 범위: 단계 5 Linux 세션 9로 기존 Comparison `dockerfile-vs-compose`, `docker-commit-vs-dockerfile`, `docker-cp-vs-bind-mount-vs-volume`, `git-fetch-vs-pull-vs-clone`, `host-port-forwarding-vs-docker-port-mapping`, `virtual-machine-vs-docker-container` 6개를 고도화했다. `dockerfile-vs-compose`의 위치/type 불일치는 이동하지 않고 내용만 보강했다.
- Docker·실행 계층: R06~R08 날짜 MD를 최우선 근거로 commit snapshot/Dockerfile recipe/Compose runtime, cp/bind/volume, VM guest/Docker host/container, VirtualBox NAT·guest iptables/UFW/Docker publish의 선택 상황·함께 쓰는 관계·artifact·오류·완료 조건을 분리했다. P02~P03·P08은 전사된 이론·화면 절차와 registry naming 보조로만 사용했다.
- Git: R09의 새 local clone·remote 변경 pull과 R10의 fetch→remote-tracking→local branch를 분리했다. 기존 placeholder repository URL과 서로 떨어진 세 명령을 합친 `bash` fence 1개를 제거해 수업 원문 한 실행 묶음처럼 보이지 않게 했다.
- 신규 후보: `sudo vs sudo su - vs root session`은 R01·R03~R05·R08의 반복 관리자 작업과 R03의 명시적 “꼭 root?” 혼동 때문에 Comparison으로 생성했다. `sudo로 만든 디렉터리는 왜 일반 사용자로 수정·복사할 수 없는가`는 R03 `touch`와 R04 drag-and-drop의 반복 오류를 종합하는 독립 troubleshooting 가치가 있어 Query로 생성했다.
- provenance·보안: R01·R03~R11 주 근거와 P02~P04·P08 역할을 8개 page claim에 필요한 범위로 대응했다. 세션 9 대상 fence는 최종 `0 / 원문 검증 0 / 수동 예외 0 / 실패 0`, `bash` 0개이며 Linux 직접 페이지의 미처리 fence도 0개다. 실제 account·email·repository URL·password·PAT·token·credential 재노출은 0건이다.
- 기록·상태: 신규 2개와 실제 설명 변경을 index에 반영하고 Total pages를 274로 재계산했다. Linux 직접 source 지식 페이지는 세션 5 신규 Concept의 과거 집계 누락을 바로잡아 39개로 확정했고, inventory의 세션 9 결과·후보 판정·fence 잔여를 갱신했다. `raw/KoreaICT/5. Linux`는 수정하지 않았다.
- 단계 상태: 단계 5 Linux는 미완료다. 세션 10 전체 고정점, 상위 계획의 단계 5 완료 기록, 단계 6 AWS, Git commit·push를 시작하지 않았다.

## [2026-07-16] update | Linux Git·GitHub Entity/Concept 고도화

- 범위: 단계 5 Linux 세션 8로 기존 `git-github-collaboration`, `git`, `github`, `source-tree` 4개를 고도화했다. 신규 지식 페이지는 만들지 않았고 Summary·Comparison·Query·Docker 관련 페이지·sudo/root·permission 후보는 수정하지 않았다.
- 협업 artifact: R09의 WorkTree→stage→commit→remote, commit 없는 push, clone·pull, SourceTree 두 local repository의 push 거부·수동 통합과 `animal` branch 시작을 복원했다. R10의 팀원 clone·`sport` push, `animal`·`sport` PR review/merge, remote `master`→각 local pull, fetch→remote-tracking/local branch, `Main.java`·`Cat.java` conflict와 merge/rebase 범위를 실제 순서로 연결했다.
- 상태·완료 조건: working tree·staging area·commit·local branch·remote-tracking branch·remote branch·PR·merge 결과를 분리했다. add·commit·push·fetch·pull·merge·rebase의 입력→처리→결과와 push·PR 생성·PR merge·remote master·local master pull·fetch·conflict 해결을 별도 완료 상태로 기록했다.
- 책임·경계: Git의 local 상태·이력, GitHub의 remote hosting·PR, SourceTree·IntelliJ의 서로 다른 client 실행, GitHub Actions의 후속 workflow 책임을 분리했다. Java 개인 Git 선행, Linux 05-04~05-06 팀 협업 직접 수업, CI/CD 후속 활용을 같은 학습일이나 성공 결과로 합치지 않았다.
- provenance·검증: R09·R10·R11 3/3·미분류 0건이다. P04는 Git Bash P.11~31, SourceTree P.35~60, branch·PR·conflict P.62~131의 화면 절차만 보조했다. 시작 fence 2개(`bash` 2)의 placeholder URL·합성 feature 예시를 prose·표로 해소해 최종 대상 `0 / 원문 검증 0 / 수동 예외 0 / 실패 0`, `bash` 0개이며 실제 식별자·credential 재노출도 0건이다.
- 기록·상태: 고도화 결과와 어긋난 index 설명 4개와 Linux inventory의 세션 8 상태·대응표·fence 재고를 갱신했다. 신규 페이지가 없어 Total pages는 272를 유지했고 `raw/KoreaICT/5. Linux`는 수정하지 않았다.
- 단계 상태: 단계 5 Linux는 미완료다. 세션 9, 상위 계획의 단계 5 완료 기록, 단계 6 AWS, Git commit·push를 시작하지 않았다.

## [2026-07-16] update | Linux Dockerfile·reverse proxy·Compose Concept/Entity 고도화

- 범위: 단계 5 Linux 세션 7로 기존 `docker-reverse-proxy-load-balancing`, `docker-compose-manifest`, `docker` 3개를 고도화하고 `docker-registry-tag-push-pull` Concept 1개를 신규 생성했다. Summary·Comparison·Query, 세션 6 Docker core Concept, Git/GitHub 페이지는 수정하지 않았다.
- Dockerfile·proxy: R07의 Apache/Nginx Dockerfile과 Spring JAR image artifact를 Docker Entity 이력에 연결했다. `proxy-net`의 backend 여섯 개, host-mounted `nginx.conf`, `reverse-proxy`의 host 80 진입, upstream·proxy_pass→browser 응답을 복원하고 backend 실행·network·config·proxy process·backend 응답·browser 분배를 별도 완료 조건으로 분리했다. I03은 상담자 업무 분배 비유로만 사용했다.
- Compose: R08의 MySQL+Spring과 MySQL+WordPress manifest를 service/container 이름, image·network·volume·environment·ports·depends_on에 대응했다. 제공 WordPress manifest의 YAML 들여쓰기와 요구사항 값 수정 범위, service name/container_name, depends_on/readiness, up/application 성공, down/image·volume 삭제를 구분하고 삭제 명령의 volume 이름 불일치도 미확정으로 보존했다.
- Docker Entity·registry 판정: R05 설치/image/container→R06 network/storage/commit/registry→R07 Dockerfile/Spring+DB/proxy→R08 Compose의 날짜별 이력을 복원했다. registry는 local image 생성·실행과 다른 naming·인증·push·다른 환경 retrieval 질문, namespace 오류, credential 경고, 수동/CI 경계가 독립 탐색 가치가 있어 신규 Concept로 만들고 Entity에서 역링크했다. push digest는 확인됐지만 다른 환경의 최종 browser/file 결과는 미보존으로 남겼다.
- 책임·완료 경계: Linux host·Docker Engine·image/container/network/volume·Dockerfile·Compose·registry·CI/CD와 04-27 host Nginx·04-28 web container·04-30 reverse proxy·후속 AWS ALB를 분리했다. 설치·image build·container Up·network·DB readiness·proxy/browser·Compose up/down·registry push/pull을 같은 성공 상태로 합치지 않았다.
- provenance·검증: R06·R07·R08·R11 핵심 대응 4/4·미분류 0건이다. 세션 시작 대상 fence 4개(`text/nginx/yaml/bash` 각 1) 중 합성 3개를 prose·표로 해소하고 `nginx` 1개를 R07 lines 803~844의 연속 원문으로 교체해 최종 1/원문 검증 1/수동 예외 0/실패 0, 대상 `bash` 0개다. P02·P03·P08·P09와 I03은 날짜 귀속·성공 결과를 만들지 않는 보조자료로만 판정했고 실제 account·email·repository URL·password·PAT·token·credential 재노출은 0건이다.
- 기록·상태: 신규 Concept와 실제 설명 변경을 index에 반영하고 Total pages를 272로 재계산했다. Linux inventory의 세션 7 상태·대응표·registry·fence 판정을 갱신했으며 `raw/KoreaICT/5. Linux`는 수정하지 않았다.
- 단계 상태: 단계 5 Linux는 미완료다. 세션 8, 상위 계획의 단계 5 완료 기록, 단계 6 AWS, Git commit·push를 시작하지 않았다.

## [2026-07-16] update | Linux Docker core Concept 고도화

- 범위: 단계 5 Linux 세션 6으로 기존 `docker-install-permission-setup`, `docker-image-container`, `docker-cp-exec-container-files`, `docker-network-volume` 4개만 고도화했다. Summary·Entity·Comparison·Query와 Dockerfile·reverse proxy·Compose Concept는 수정하지 않았고 신규 페이지를 만들지 않았다.
- 설치·권한: R05 setup script·CRLF·execute bit·root 위치, Docker service, socket/docker group과 재login을 복원하고 설치·service active·계정 group 등록·현재 session 반영·일반 사용자 daemon 접근을 별도 완료 조건으로 분리했다. R08/P09 setup은 반복 checklist로만 사용했다.
- image/container·exec/cp: R05 기성 `httpd`·Nginx·MySQL·WordPress lifecycle·port·browser/DB 상태를 R06 commit image·R07 Dockerfile·registry/CI image와 분리했다. 실제 Apache/Nginx/MySQL container와 document root를 대조해 내부 명령, host↔container 양방향 일회 copy, browser 반영, commit image 결과를 서로 다른 완료 조건으로 복원했다.
- network/storage: R05 `network01` WordPress–MySQL과 R06 `network02` MariaDB–Redmine의 이름 기반 통신을 host port 공개와 분리했다. Apache 빈 bind의 `Index of /`, Nginx 403, `mount-vol` inspect·삭제를 실제 날짜에 연결하고 R06에는 재생성 뒤 persistence 실측이 없음을 명시했다. Compose·VirtualBox NAT·iptables·AWS VPC는 별도 계층으로 유지했다.
- provenance·검증: R05·R06·R08·R11 source union 4/4·미분류 0건이다. 기존 합성 `bash` fence 4개를 prose·표로 해소해 최종 대상 fence 0/원문 검증 0/수동 예외 0/실패 0, `bash` 0개이며 실제 IP·account·email·repository URL·Docker Hub account·credential 재노출도 0건이다.
- 기록·상태: Linux inventory의 세션 6 상태·대응표·fence 잔여를 갱신했다. 신규 페이지와 설명 불일치가 없어 index는 수정하지 않았고 Total pages는 271이다. Docker registry 후보는 세션 7 판단으로 유지했다.
- 단계 상태: 단계 5 Linux는 미완료다. 세션 7, 상위 계획의 단계 5 완료 기록, 단계 6 AWS, Git commit·push를 시작하지 않았다.

## [2026-07-16] update | Linux VM·SSH·process·service·network·server Concept/Entity 고도화

- 범위: 단계 5 Linux 세션 5로 기존 `linux-spring-boot-server-deploy`, `linux-web-server-apache-nginx`, `linux`, `maven` 4개를 고도화하고 `linux-process-service-port-firewall` Concept 1개를 신규 생성했다. Summary·Comparison·Query·Docker core·세션 4 Concept는 수정하지 않았다.
- Spring Boot·Maven: R05의 project/9000→VirtualBox NAT→guest iptables/UFW→Maven 설치/version→project root package→`target` JAR→host process→browser를 복원하고 설치·build·artifact·process·port·응답 완료 조건을 분리했다. R07 Dockerfile/JAR와 CI Maven build는 후속 책임으로 구분했다.
- web server·Linux: 누락됐던 핵심 R04 source를 바로잡고 Apache/Nginx package·enable/start/status, UFW 22/80/443, SSH 보호, document root backup·homepage 교체·browser 결과를 복원했다. VirtualBox Ubuntu·OpenSSH·MobaXterm에서 permission·process/service·network·host server로 확장된 Linux 이력과 Docker·EC2·CI/CD 경계를 분리했다.
- 신규 판단: SSH·Apache/Nginx·Spring에 반복되는 process→service→listening port→firewall→NAT/redirect→client 응답은 독립 탐색 가치가 있어 신규 Concept 1개로 보존하고 기존 대상 4개에서 역링크했다. 별도 VM·SSH·service·firewall·port Comparison은 만들지 않았다.
- provenance·검증: R01·R03~R05·R07·R11 핵심 대응 6/6·미분류 0건이다. 대상 기존 합성 fence 4개를 prose·표로 해소해 최종 대상 5개 fence 0/원문 검증 0/수동 예외 0/실패 0, `bash` 0개이며 실제 IP·account·email·repository URL·credential 재노출도 0건이다.
- 기록·상태: 신규 Concept와 고도화 결과 설명을 index에 반영하고 Total pages를 실제 정의에 따라 271로 재계산했다. Linux inventory의 세션 5 상태·대응표·후보 판정·fence 잔여를 갱신했고 `raw/KoreaICT/5. Linux`는 수정하지 않았다.
- 단계 상태: 단계 5 Linux는 미완료다. 세션 6, 상위 계획의 단계 5 완료 기록, 단계 6 AWS, Git commit·push를 시작하지 않았다.

## [2026-07-16] update | Linux CLI·파일·vi·권한 Concept 고도화

- 범위: 단계 5 Linux 세션 4로 지정 Concept `linux-cli-files`, `linux-package-archive`, `linux-users-permissions` 3개만 부분 보강했다. Summary·Entity·Comparison·Query와 다른 Concept는 수정하지 않았고 신규 지식 페이지를 만들지 않았다.
- CLI·파일·vi: prompt 사용자/host/path, `/`·`/root`·home, 절대/상대 path, 방송사 tree의 file 상태 변화, `find`/`grep`, `cat`/`more`, redirection·`diff`, vi 명령/입력/마지막 행 모드와 저장·종료·검색·치환을 복원했다. Librarian 교시의 세부 결과 부재도 보존했다.
- package·archive: `apt update/install`, `wget`·`curl`, tar+gzip, zip/unzip의 책임과 Vim archive·해제 directory·zip artifact 확인을 분리했다. root 소유 download directory의 file 반입 실패→ownership 확인·변경→성공 흐름과 package/download/archive/move의 단계 차이를 복원했다.
- user·permission: account file·UID/GID·home/login shell·기본/보조 group, file/directory `r/w/x`, 숫자/기호 chmod 선택, directory `x`, sudo/root, chmod/chown/chgrp, root 소유 directory와 script 실행 권한 오류를 정리했다. I01~I02는 실제 표시 요소만 사용했으며 vi·경로·권한 비교 후보는 지정 Concept에 흡수하고 Comparison을 수정·신설하지 않았다.
- provenance·검증: Concept source union R01~R04·R11 5/5, 미분류 0건이다. 대상 기존 `bash` fence 3개를 제거해 최종 fence 전체 0개/원문 검증 0개/수동 예외 0개/실패 0개, `bash` 0개이며 실제 account·email·repository URL·password·token·one-time code 재노출도 0건이다.
- 기록·상태: Linux inventory의 세션 4 상태·결과를 갱신했다. 새 페이지가 없고 index 설명이 현재 내용과 어긋나지 않아 `wiki/index.md`는 수정하지 않았으며 Total pages는 실제 정의에 따라 270이다. `raw/KoreaICT/5. Linux`는 수정하지 않았다.
- 단계 상태: 단계 5 Linux는 미완료다. 세션 5, 상위 계획의 단계 5 완료 기록, 단계 6 AWS, Git commit·push를 시작하지 않았다.

## [2026-07-16] update | Linux Summary 후반부·총정리 R06~R11 고도화

- 범위: 단계 5 Linux 세션 3으로 04-29·04-30·05-01·05-04·05-06 날짜 Summary 5개를 전면 재작성하고 Linux 총정리 허브 1개를 부분 보강했다. Concept·Entity·Comparison·Query와 R01~R05 Summary는 수정하지 않았다.
- Docker 흐름: MariaDB–Redmine network→exec/cp→bind/volume→commit→Docker Hub registry, Dockerfile build context·Spring JAR/MySQL→Nginx reverse proxy, Compose YAML→up/status/DB/browser/down의 artifact·상태·입력→처리→결과를 복원했다.
- Git 흐름: WorkTree→stage→local repository→GitHub remote, commit 없는 push, clone·pull·SourceTree·두 작업자 conflict, team branch→PR review/merge→master pull·fetch→merge/rebase의 실제 수업 범위를 복원했다.
- 오류·경계: Apache/Nginx 빈 bind 결과, build/Up/log/browser, `depends_on`/readiness, `down`/volume 삭제, 빈 교시·05-01 backend 시험, 04-29 AWS 가입 예고·05-06 AWS 본수업, Linux 직접 수업과 AWS/CI/CD 후속 활용을 분리했다.
- 보조자료·provenance: P01~P04·P08~P09는 날짜 MD에 필요한 내용이 충분히 전사되어 page source로 강제하지 않았다. I03은 상담자 요청 분배 비유에만 채택했다. code fence는 전체 0개/원문 검증 0개/수동 예외 0개/실패 0개, `bash` fence 0개이며 실제 식별자·credential 재노출도 0건이다.
- 기록: 실제 고도화와 어긋난 index 설명 6개와 Linux 재고 계획의 세션 3 상태·결과를 갱신했다. 새 페이지가 없어 Total pages는 실제 정의에 따라 270을 유지한다.
- 상태: 단계 5 Linux는 미완료다. 세션 4, 단계 6 AWS, Git commit·push를 시작하지 않았고 `raw/KoreaICT/5. Linux`는 수정하지 않았다.

## [2026-07-16] update | Linux Summary 전반부 R01~R05 고도화

- 범위: 단계 5 Linux 세션 2로 04-22·04-23·04-24·04-27·04-28 Summary 5개만 R01~R05 날짜 MD 전체 교시 흐름에 맞춰 전면 재작성했다. Concept·Entity·Comparison·Query와 R06~R11 Summary는 수정하지 않았다.
- 흐름 복원: VM/bridge/OpenSSH/MobaXterm/path → 방송사·Librarian file/vi/redirection/diff → account file·UID/GID·chmod/chown/chgrp → download/archive/alias/Java/Git/Apache·Nginx → Maven JAR/port 계층/Docker lifecycle/WordPress–MySQL network의 날짜별 책임을 복원했다.
- 오류·혼동: 설치/service 실행, `>`/`>>`, owner/group/others와 숫자·기호 권한, root 소유 directory, alias session/.bashrc, JDK/JDBC/DB 연결, VirtualBox NAT·guest iptables·Docker port, image/container, Docker network/AWS VPC를 분리했다. 04-24 “하지는 않음” 구간은 실행 결과에서 제외했다.
- 보조자료·provenance: P05~P07·P10은 날짜 MD에 필요한 내용이 충분히 전사되어 page source로 강제하지 않았다. I01~I02는 실제 판독해 04-24 source로 채택했다. 새 code fence는 0개/원문 검증 0개/수동 예외 0개이며 Linux `bash` fence도 0개다.
- 기록: 대상과 명백히 어긋난 index 설명 5개와 Linux 재고 계획의 세션 2 상태·결과를 갱신했다. 새 페이지가 없어 Total pages는 실제 정의에 따라 270을 유지한다.
- 상태: 단계 5 Linux는 미완료다. 세션 3, 단계 6 AWS, Git commit·push를 시작하지 않았고 `raw/KoreaICT/5. Linux`는 수정하지 않았다.

## [2026-07-16] update | Linux 내용 재고도화 세션 1 전수 재고·실행 계획

- 범위: 단계 5 Linux의 세션 1로 `raw/KoreaICT/5. Linux`와 기존 Linux 직접 source 지식 페이지, FrontEnd_BackEnd/AWS/CI/CD 후속 경계 페이지를 전수 조사했다. 지식 페이지 본문 고도화는 시작하지 않았다.
- raw 재고: 실제 파일 24개를 R01~R11 날짜별·총정리 MD, P01~P10 PDF·문서형 교육자료, I01~I03 이미지로 전체 경로와 함께 대응했다. Markdown 14·PDF 7·PNG 3, 0바이트 0, 과목 내·과목 간 byte-identical 중복 0건이다.
- wiki 대응: Linux raw를 직접 source로 가진 35개(디렉터리 기준 `summaries 11 / concepts 13 / entities 6 / comparisons 5 / queries 0`, frontmatter type 기준 `summary 11 / concept 12 / entity 6 / comparison 6 / query 0`)와 후속 경계 15개를 유지 19·부분 보강 17·전면 재작성 13·통합 후보 0·근거 부족 1로 분류했다. 신규 후보는 process/service/firewall/port와 Docker registry Concept, sudo/root Comparison, permission Query 4개이며 실행 세션에서 최종 판단한다.
- fence 재고: 직접 페이지 13개에 code fence 18개(`bash 14 / yaml 1 / text 1 / nginx 1 / dockerfile 1`)가 있다. 18개 모두 선언 텍스트 raw의 공백 정규화 연속 부분문자열과 일치하지 않아 합성·일반화·PDF 수동 근거 후보로 표시했고, CLI `bash`는 향후 `shell` 교정 대상으로 고정했다.
- 실행 분할: Summary 전반/후반, Linux CLI·파일·vi·권한, VM·SSH·process·service·network·server, Docker core, Dockerfile·Compose, Git/GitHub, 최종 Comparison/Query, 전체 고정점까지 총 10개 세션으로 나눴다.
- 기록: `wiki/_meta/linux-rehighquality-inventory-plan.md`를 만들고 index에 등록해 Total pages를 270으로 재계산했다. `raw/`와 기존 지식 본문은 수정하지 않았고 상위 계획에 단계 5 완료 행을 쓰지 않았으며 세션 2를 자동 실행하지 않았다.

## [2026-07-16] lint | FrontEnd_BackEnd 과목 전체 고정점 완료

- 범위: 실행 분할 세션 16에서 FrontEnd_BackEnd 직접 source를 가진 최종 지식 페이지 59개(`summary 19 / concept 20 / entity 9 / comparison 9 / query 2`)와 index·log·상위 계획을 전수 QA했다. 새 페이지는 만들지 않았고 Total pages는 269를 유지했다.
- raw·artifact: R01~R19 MD 19개·총 22,838행, P01~P10 PDF 10개, I01~I05 이미지 5개를 실제 파일 기준으로 재계산·대응했다. R19의 실제 끝은 04-15 Cart 삭제이며 04-16 이후 Order·검색 근거로 소급하지 않았다.
- 내용 경계: 04-06 JWT 준비/04-07 credential·Bearer 인증, React role UI/JWT Claim/GrantedAuthority/SecurityContext/endpoint 인가, CartProduct/OrderProduct·checked/quantity/stock, 04-16 주문 생성/04-17 목록/04-20 상태·취소, 04-21 frontend/04-22 검색 backend 코드·runtime 미확정을 다시 분리했다. Passwordless와 단계 5 이후 과목은 후속 경계로 유지했다.
- 최소 교정: `jpql-vs-sql`의 SQL·JPQL fence 2개를 실제 raw와 연속 일치하도록 수정했다. 신규 Query 2개와 세션 15 Comparison 2개가 Summary·Concept·Entity에서 역링크를 갖도록 관련 링크 10개만 보강했으며 다른 본문은 재작성하지 않았다.
- 구조 검증: 59개 전체의 필수 frontmatter·source 실경로·허용 태그·위키링크·고립·index 등록·placeholder 오류는 0건, code fence는 2/2 원문 일치다. 신규 Query와 세션 15 Comparison은 각각 Summary·Concept·Entity 역링크를 최소 1개 이상 확보했다.
- 상태: 단계 4 FrontEnd_BackEnd는 최종 완료했다. 상위 계획과 index에 완료 근거를 반영했고 단계 5 Linux는 시작하지 않았다.

## [2026-07-16] update | FrontEnd_BackEnd Comparison/Query B 고도화

- 범위: 실행 분할 세션 15의 지정 Comparison `authentication-vs-authorization`, `passwordless-vs-password-login` 2개를 고도화하고 Query `why-shopping-cart-order-flow-is-complex`, `jwt-role-ui-vs-server-authorization` 2개를 신규 생성했다. 세션 2~14 지식 페이지와 `raw/`는 수정하지 않았다.
- raw·교안 대응: R06·R07·R12~R16 실제 경로를 7/7 대응했다. P04·I01·I02·I04는 날짜 MD와 고도화 Summary/Concept에 필요한 내용이 충분히 전사되어 직접 열거나 새 페이지 source에 추가하지 않았다.
- 인증 경계: 04-06 구성 준비와 04-07 credential login·Bearer filter·SecurityContext 실제 연결을 분리했다. React role UI, localStorage user, JWT role Claim, GrantedAuthority, SecurityContext Authentication, endpoint authorization을 같은 완료 상태로 합치지 않았다.
- 구현 경계: 확인된 `permitAll`·`authenticated`와 미확정 endpoint role·ownership 정책을 나눴다. Passwordless는 후속 X1280 QR·앱 승인·외부 인증 서버 및 중간 프로젝트 적용 설계로만 비교하고 FrontEnd_BackEnd 직접 구현으로 소급하지 않았다.
- Cart/Order 경계: 관계·DTO·checked/quantity/stock·CartProduct/OrderProduct 생명주기, Cart 삭제·Order 저장, transaction, 완료·취소·재고 복원을 04-14~04-20 실제 흐름으로 추적했다.
- provenance·검증: 대상 code fence는 전체 0개/선언 텍스트 raw 원문 검증 0개/수동 예외 0개다. 4개 페이지의 필수 구조와 frontmatter·실재 source·허용 태그·위키링크·placeholder를 통과했고, Query 2개를 index에 등록해 Total pages를 269로 갱신했다.
- 상태: 단계 4 FrontEnd_BackEnd는 미완료다. 세션 15만 처리했고 세션 16·단계 5 Linux를 시작하지 않았으며 상위 계획 완료 행을 기록하지 않았다.

## [2026-07-16] update | FrontEnd_BackEnd Comparison A 고도화

- 범위: 실행 분할 세션 14의 지정 Comparison `controller-service-repository`, `entity-vs-dto`, `props-vs-state`, `react-router-vs-spring-api-url`, `mpa-vs-spa`, `session-vs-cookie-vs-jwt` 6개만 고도화했다. 세션 2~13 Summary·Concept·Entity와 세션 15 Comparison/Query, `raw/`는 수정하지 않았다.
- raw·교안 대응: R03·R06·R07·R10·R12~R18 source union 11/11과 P01·P03·P04·P07·P08 실제 매핑 5/5를 확인했다. 첫 비교 시점에는 R01·R02·R05를 필요한 페이지에서만 보조했다. PDF 내용은 날짜 MD/Summary에 충분히 전사돼 직접 열거나 source에 추가하지 않았고, I03은 실제 Router 비유 범위만 확인해 사용했다.
- 계층·데이터 경계: Controller의 HTTP 입력·응답, Service의 업무·transaction, Repository의 DB 접근과 실제 Member·Product·Cart·Order·검색 호출 범위를 구분했다. Entity·요청/응답 DTO·Map 응답·TypeScript type·runtime JSON·DB row와 Product 직접 Entity 수신, Cart/Order 변환 지점을 분리했다.
- React·URL 경계: props/state를 callback·setter·API·DB 저장과 분리했다. Router path/API URL의 runtime·port·요청 주체·결과를 Fruit·Cart·Paging으로 비교하고 CORS를 다른 origin 간 browser 정책으로 유지했다.
- rendering·인증 경계: MPA/SPA rendering과 Session/JWT 인증 상태를 다른 축으로 유지했다. Cookie=저장·전달 수단, Session=server 상태, JWT=서명 token으로 나누고 04-06 이론·구성 준비와 04-07 login·localStorage·Bearer filter·SecurityContext 연결을 분리했다.
- 독립 감사 교정: props의 04-06 `onLogin` callback, Router의 03-31 자리표시→04-01 실제 API 왕복·04-07 Security CORS 이동, 04-14 인증 email 소비와 04-17 client role/memberId 미확정을 추가했다. 03-31 Thymeleaf는 MPA 전체 완성 대신 server-rendered HTML 응답 패턴으로, JWT는 claim 구성 코드와 runtime token 관찰을 분리했다.
- provenance·검증: 대상 code fence는 전체 0개/선언 텍스트 raw 원문 검증 0개/수동 예외 0개다. 6개 Comparison의 필수 내용 구조와 frontmatter·실재 source·허용 태그·위키링크·placeholder를 확인하고 명백히 낡은 index 설명 6개만 갱신했다.
- 상태: 단계 4 FrontEnd_BackEnd는 미완료다. 세션 14만 처리했고 세션 15·단계 5 Linux를 시작하지 않았으며 상위 계획 완료 행을 기록하지 않았다.

## [2026-07-16] create | LLM Wiki 사용자 학습 가이드

- 목적: 페이지 수가 많아 사용자가 직접 공부할 때 시작점을 찾기 어려운 문제를 해결하기 위해 사용자용 학습 안내서를 만들었다.
- 생성: `wiki/_meta/wiki-user-study-guide.md`에 과목 총정리→Concept·Comparison→날짜 Summary→필요한 raw 원본으로 이어지는 기본 학습 순서를 정리했다.
- 활용: 페이지 유형별 역할, 오늘 복습·과목 전체 복습·프로젝트·시험/면접 상황별 공부법, 적정 학습량, 읽지 않아도 되는 관리 문서, AI 요청 예시를 포함했다.
- 접근성: `wiki/index.md`의 사용 방법 상단과 Meta 목록에 시작 링크를 등록하고 전체 페이지 수를 267로 갱신했다. `raw/`는 수정하지 않았다.

## [2026-07-16] update | FrontEnd_BackEnd Entity B 고도화

- 범위: 실행 분할 세션 13의 지정 Entity `node-js`, `visual-studio-code`, `intellij-idea`, `oracle-database` 4개만 고도화했다. 세션 2~12 Summary·Concept·Entity A와 다른 Comparison·Query 본문, `raw/`는 수정하지 않았다.
- raw·교안 대응: R01~R05, P02·P06·P09의 실제 매핑 8/8과 Java IntelliJ·Oracle 직접 수업 경계를 확인했다. P06·P09 내용은 날짜 MD와 고도화 Summary에 충분히 전사되어 직접 열거나 source에 추가하지 않았다.
- runtime·editor 경계: Node.js runtime, npm package manager, Vite project/development/build tool, React browser rendering을 분리했다. VS Code는 React/TypeScript editor 이력만 맡기고 npm·Vite·React의 실행을 editor 기능으로 설명하지 않았다.
- IDE·DB 경계: IntelliJ는 Java→Spring Boot backend 작업환경으로 정리하되 Java/JVM·Maven·Spring Boot 기능과 분리했다. Oracle 직접 SQL·schema·sequence·constraint·JOIN 이력과 03-30 이후 MySQL/JPA runtime을 구분하고 Oracle `NEXTVAL`/JPA `GeneratedValue(AUTO)`, Oracle SQL/MySQL SQL을 같은 구현으로 합치지 않았다.
- P02 중복: FrontEnd_BackEnd와 Java의 `IntelliJ 교안.pdf`가 동일 SHA-256이며 byte-identical임을 재확인했다. Java 단계의 동일 교안 source만 유지하고 P02로 사실·source를 중복 생성하지 않았다.
- provenance·검증: 대상 code fence는 전체 0개/선언 텍스트 raw 원문 검증 0개/수동 예외 0개다. 4개 Entity의 필수 내용 구조와 frontmatter·실재 source·허용 태그·위키링크·placeholder를 확인하고 명백히 낡은 index 설명 4개만 갱신했다.
- 상태: 단계 4 FrontEnd_BackEnd는 미완료다. 세션 13만 처리했고 세션 14·단계 5 Linux를 시작하지 않았으며 상위 계획 완료 행을 기록하지 않았다.

## [2026-07-16] update | FrontEnd_BackEnd Entity A 고도화

- 범위: 실행 분할 세션 12의 지정 Entity `spring-boot`, `react`, `typescript`, `jwt`, `mysql` 5개만 전면 고도화했다. 세션 7~11 Summary/Concept와 다른 Entity·Comparison·Query 본문, `raw/`는 수정하지 않았다.
- raw·교안 대응: R01~R18과 P04·P05·P07·P08 실제 경로를 22/22 확인했다. 직접 구현 순서는 날짜 MD와 고도화 Summary를 우선했으며 PDF 내용은 충분히 전사돼 직접 열거나 Entity source에 추가하지 않았다.
- 기술 이력: Spring Boot는 dependency 선택과 실제 계층·Security·도메인 기능 사용 날짜를 분리했다. React는 component/state/rendering과 Router·axios·Bootstrap·TypeScript를 구분하고 Fruit→Product·Cart·Order·Paging/Search 화면 이력을 복원했다. TypeScript는 compile-time type/interface·props/state·event·배열·optional chaining을 runtime JSON·Java DTO/Entity·DB 행과 분리했다.
- 인증·DB 경계: JWT의 04-06 준비와 04-07 생성·저장·Bearer 전달·filter 검증·SecurityContext·logout을 단계별로 나누고 client role/token authority/server authorization을 구분했다. MySQL은 Oracle 직접 SQL에서 MySQL/JPA runtime으로의 전환과 Member·Product·Cart·Order·page/search SQL 이력을 정리하며 Oracle sequence/SQL과 GeneratedValue/MySQL SQL을 합치지 않았다.
- 완료 경계: dependency·UI control·type 선언·token 저장·Repository 호출·SQL 시나리오가 있다는 사실만으로 실제 기능/runtime 성공을 과장하지 않았다. 04-10·04-17 불일치와 04-22 executor/날짜 type/API 결과 미확정, Order table/result 미확정을 보존했다.
- provenance·검증: Entity source union R01~R18 18/18, P 매핑 4/4다. 대상 code fence는 전체 0개/선언 텍스트 raw 원문 검증 0개/수동 예외 0개다. 필수 frontmatter·실재 source·허용 태그·위키링크·placeholder·Entity 내용 게이트를 확인하고, 명백히 낡은 MySQL index 설명 1개만 갱신했다.
- 상태: 단계 4 FrontEnd_BackEnd는 미완료다. 세션 12만 처리했고 세션 13·단계 5 Linux를 시작하지 않았으며 상위 계획 완료 행을 기록하지 않았다.

## [2026-07-16] update | FrontEnd_BackEnd Concept Backend/Spring/데이터 C 고도화

- 범위: 실행 분할 세션 11의 지정 concept `spring-data-jpa-specification-pageable`, `spring-product-search-flow`, `database-normalization-functional-dependency`, `oracle-sequence` 4개만 고도화했다. 세션 8의 Product·Cart·Order·Paging, 세션 10의 JPA 관계 mapping과 다른 지식 페이지 본문, `raw/`는 수정하지 않았다.
- raw·교안 대응: R01·R14·R17·R18·P08·P10 실제 경로를 6/6 확인하고 Oracle 03-16~03-18 sequence·03-20 정규화 근거와 04-02 GeneratedValue를 필요한 경계만 대조했다. P08·P10 내용은 날짜 MD와 고도화 Summary에 충분히 전사되어 PDF를 직접 열거나 source에 추가하지 않았다.
- 검색 고도화: 04-20 Paging UI, 04-21 단순 Pageable Page 왕복과 검색 control/state/request·SearchDto·개별 Specification 준비, 04-22 Controller 수신→Service 조건 조립·Sort·PageRequest→Repository 호출→Page 응답→MySQL 조건 대조를 날짜·계층별로 분리했다. Querydsl 언급과 실제 Specification 구현도 구분했다.
- 완료 경계: ProductRepository의 `JpaSpecificationExecutor<Product>` 상속 미확인과 `LocalDate` inputdate/`LocalDateTime` 비교값 정합성 미확정을 보존했다. Repository 호출 코드·MySQL SQL 시나리오는 확인되지만 실제 Specification API 응답·확정 건수는 없어 runtime 검색 성공을 단정하지 않았다.
- 데이터 경계: 함수 종속성, 정규화·분해, PK/FK, JOIN, JPA Entity 관계를 다른 계층으로 나누고 Order/OrderProduct는 후속 적용 사례로만 연결했다. Oracle 독립 sequence와 MySQL/JPA GeneratedValue(AUTO)도 같은 구현으로 합치지 않았으며 AUTO_INCREMENT·GenerationType별 DB 동작을 원본 없이 만들지 않았다.
- provenance·검증: 대상 code fence는 전체 0개/선언 텍스트 raw 원문 검증 0개/수동 예외 0개다. 4개 모두 필수 내용 구조와 frontmatter·실재 source·허용 태그·실재 위키링크·placeholder를 통과했고, 내용과 명백히 어긋난 index 설명 4개만 갱신했다.
- 상태: 단계 4 FrontEnd_BackEnd는 미완료다. 세션 11만 처리했고 세션 12·단계 5 Linux를 시작하지 않았으며 상위 계획 완료 행을 기록하지 않았다.

## [2026-07-16] update | FrontEnd_BackEnd Concept Backend/Spring/데이터 B 고도화

- 범위: 실행 분할 세션 10의 지정 concept `jpa-relationship-mapping` 1개만 전면 고도화했다. 세션 8의 Product·Cart·Order·Paging concept와 다른 summary·concept·entity·comparison·query 본문, `raw/`는 수정하지 않았다.
- raw·artifact 대응: R11·R12·R14·R19·P08·I01~I04 실제 경로를 9/9 확인했다. 03-30 Fruit·04-02 Member·04-08 Product는 R01·R04·R08로 선행 배경만 보강했다. I01·I02·I04는 실제로 확인해 source에 선언했고, Router 그림인 I03은 JPA 근거에서 제외했다. P08 내용은 날짜 MD에 충분히 전사돼 PDF source를 추가하지 않았다.
- 관계·FK: Cart=`carts.member_id`, CartProduct=`cart_products.cart_id/product_id`, Order=`orders.member_id`, OrderProduct=`order_products.order_id/product_id`의 owning side를 실제 Entity 코드로 확정했다. `mappedBy = "cart"/"order"`는 반대편 Java 필드명이며 Member/Product 쪽 미확인 반대편은 임의로 만들지 않았다.
- 수업 흐름: 04-13 관계 Entity·quantity·Repository·상세 Cart 요청 준비, 04-14 email→Member→Cart 조회/생성→Product·동일 품목 탐색→quantity 누적/신규 저장→CartItemDto 변환, 04-16 별도 Order/OrderProduct·DTO→새 주문 품목 조립→CartProduct 후속 삭제→Order 저장을 날짜별로 분리했다.
- 생명주기 경계: CartProduct와 OrderProduct를 같은 Entity로 보지 않고 주문 전/후 관계와 수명을 비교했다. OrderProduct 가격 snapshot 필드는 원본에 없다고 명시했다. Cart·Order의 JPA cascade, Order orphan removal, Oracle DB `ON DELETE`를 동작 주체·계층별로 분리하고 신규 comparison 후보 2개는 기존 페이지에 흡수했다.
- R19·provenance: R19는 실제 04-15 Cart 삭제까지만 사용하고 Order를 소급하지 않았다. code fence는 전체 0개/선언 raw 원문 검증 0개/수동 예외 0개다. frontmatter·source 10/10·허용 태그·위키링크·placeholder·index 설명·scoped diff를 검사했으며 index 설명은 유지했다.
- 상태: 단계 4 FrontEnd_BackEnd는 미완료다. 세션 10만 처리했고 세션 11·단계 5 Linux를 시작하지 않았으며 상위 계획 완료 행을 기록하지 않았다.

## [2026-07-16] update | FrontEnd_BackEnd Concept Backend/Spring A 고도화

- 범위: 실행 분할 세션 9의 지정 concept `spring-boot-rest-api`, `dto-entity-service-controller`, `jwt-session-cookie-auth`, `spring-security-jwt-filter`, `spring-data-jpa-repository` 5개만 전면 고도화했다. 다른 summary·concept·entity·comparison·query 본문과 `raw/`는 수정하지 않았다.
- raw 대응: 주 범위 R02~R08·R12·R18·P03·P04·P08의 실제 매핑을 12/12 확인하고, Product CRUD·Cart·Order·Page·Repository 날짜 근거에는 R01·R09~R11·R13~R17을 보조 사용했다. 날짜 MD와 고도화 Summary에 필요한 내용이 전사돼 PDF를 source에 추가하지 않았다.
- 책임 분리: REST는 method·URL·입력 위치·status/body, DTO/Entity는 계층 사이 데이터 모양과 변환, JWT는 Session/Cookie 비교와 token 생성·저장·전달·삭제, Security filter는 login 인증과 후속 Bearer 검증·SecurityContext, Repository는 기본 CRUD·derived query·JPQL·Pageable·Specification 호출을 맡도록 고정했다.
- 정확성 경계: Signup field map과 Product `{message, errors}`, 04-06 구성 작성과 04-07 실제 연결, interceptor/filter/Controller/Service/Repository, role UI/client role/token authority/server authorization을 분리했다. 04-17 Repository 선언·Service 호출 이름 불일치와 04-22 executor 상속·날짜 type·실행 성공 미확정을 보존했다.
- R19·provenance: R19가 실제로 04-15 Cart 삭제에서 끝나는 것을 확인하고 이후 Order·대표 상품·검색을 소급하지 않았다. 대상 code fence는 전체 0개/원문 검증 0개/수동 예외 0개로 합성 코드를 만들지 않았다.
- 최종 검증: 5개 모두 필수 frontmatter·실재 source·허용 태그·실재 위키링크·placeholder·날짜·artifact·입력→처리→결과·혼동·선행/후속·직접/교안/후속 경계를 확인했다. 현재 내용과 명백히 어긋난 index 한 줄 설명 5개를 갱신했고, 기록 파일 반영 뒤 scoped `git diff --check`와 FrontEnd_BackEnd raw status/diff를 통과했다.
- 상태: 단계 4 FrontEnd_BackEnd는 미완료다. 세션 9만 처리했으며 세션 10·단계 5 Linux를 시작하지 않았고 상위 계획에 완료 행을 기록하지 않았다.

## [2026-07-16] update | FrontEnd_BackEnd Concept Frontend/React/TypeScript B 고도화

- 범위: 실행 분할 세션 8의 지정 concept `axios-interceptor-error-handling`, `product-domain-flow`, `shopping-cart-flow`, `order-flow`, `pagination-search` 5개만 전면 고도화했다. 다른 summary·concept·entity·comparison·query 본문과 `raw/`는 수정하지 않았고, index 설명은 기존 내용과 명백히 어긋나지 않아 유지했다.
- raw 대응: R06~R18·R19, P03·P07·P08·P10, I01~I04의 실제 매핑을 22/22 확인했다. axios의 Order 목록·상태 근거에 R15·R16을 포함했다. 날짜별 직접 구현은 raw 날짜 MD와 고도화 Summary를 우선했으며 PDF·이미지 내용은 충분히 전사되어 별도 source로 추가하지 않았다.
- 역할 분리: axios는 공통 HTTP 요청·Bearer·로그인 외 401과 form Validation 오류, Product는 seed→CRUD→상세→대표 상품→검색, Cart는 관계·선택·수량·삭제, Order는 생성·PENDING 목록·완료/취소·재고, Paging은 04-20 UI→04-21 page/search 요청→04-22 backend 조건 연결 코드와 실행 검증 경계를 맡도록 책임을 고정했다.
- 핵심 경계: React axios 요청 함수/interceptor/Spring filter·Service, `CartProductDto`/`CartItemDto`, checked/quantity/stock, Cart 삭제/Order 생성, 04-16 Order Entity·생성/04-17 목록/04-20 상태 UI, Product 배열/Page content·metadata, Querydsl 언급/Specification 구현을 구분했다.
- 비동기 감사 교정: raw 줄 범위 교차대조로 일반 `axios` Product 삭제는 interceptor 대상이 아님, 04-10 Product 저장 후 `null` 반환/Controller 500 불일치, Cart 누적 quantity 재고 검사의 한계, 04-16 주문 함수/API와 04-17 버튼 연결, Cart `some`의 quantity 0 검사, client `memberId`·`role`과 서버 인가 미확인을 최종 페이지에 반영했다.
- 최종 독립 감사 교정: Signup의 field map body와 Product의 `{message, errors}` body를 분리하고 axios source에 04-17·04-20을 추가했다. 04-22 검색은 Specification+Pageable 호출 코드 작성과 실행 검증 완료를 분리하고 `JpaSpecificationExecutor` 상속·날짜 타입 정합성 미확정 경계를 명시했다.
- R19·provenance: R19가 04-15 Cart 삭제에서 끝나는 범위를 유지하고 04-16 이후 Order·대표 상품·검색을 소급하지 않았다. 대상 code fence는 전체 0개/선언 텍스트 raw 원문 검증 0개/수동 예외 0개이며 합성 코드를 만들지 않았다.
- 검증: 대상 5개 모두 실제 날짜·대표 artifact·입력→처리→결과·혼동 원인·선행/후속·직접 수업/교안/후속 경계를 갖췄다. frontmatter·source 실경로·허용 태그·위키링크·placeholder·주 raw 22/22, scoped diff와 `git diff --check`, FrontEnd_BackEnd raw status/diff를 기록 파일 반영 후 다시 확인했다.
- 상태: 단계 4 FrontEnd_BackEnd는 미완료다. 세션 8만 처리했으며 세션 9와 단계 5 Linux는 시작하지 않았다.

## [2026-07-16] update | FrontEnd_BackEnd Concept Frontend/React/TypeScript A 고도화

- 범위: 실행 분할 세션 7의 지정 concept `frontend-backend-architecture`, `fullstack-project-flow`, `react-typescript-basics`, `react-form-state-event`, `react-useeffect-data-fetching` 5개만 전면 고도화했다. 다른 summary·concept·entity·comparison·query 본문과 `raw/`는 수정하지 않았다.
- 역할 분리: architecture는 React Router/axios와 Spring Controller→Service→Repository→MySQL의 요청·응답·JSON/CORS/DTO 경계, project-flow는 환경→Fruit→Member/JWT→Product→Cart→Order→대표 상품→검색의 반복 구현 절차, React/TypeScript는 component·props/state·type/interface·배열/optional chaining, form은 Signup/Product/Cart 입력·FileReader·Validation, useEffect는 Fruit/Product/Cart/Order/Page 검색의 실행 시점·dependency·재요청 조건을 맡도록 중복 책임을 정리했다.
- raw 대응: R01~R05·R10~R13·R17·R19와 P01·P07·I03·I05의 실제 경로 매핑을 15/15로 확인했다. 날짜별 직접 구현은 raw 날짜 MD와 고도화된 날짜 Summary를 우선하고, R19가 04-15 Cart 삭제에서 끝나는 범위와 04-16 이후 날짜 Summary 보완을 구분했다.
- 핵심 경계: React Router path/API URL, frontend state/DB 데이터, TypeScript type/Java class·Entity·DTO/runtime JSON, text/file input, 등록/수정 form, React 오류 표시/Spring Validation, dependency 존재/실제 API 호출, UI control/request/backend 소비를 각각 분리했다.
- provenance: 대상 5개에는 code fence가 전체 0개이므로 선언 텍스트 raw 원문 검증 0개, 수동 fence 예외 0개다. 원본에 없는 수업 코드·클래스·메서드·출력·상태 코드·사용자 질문이나 여러 원본 조각을 합친 코드를 추가하지 않았다.
- 검증: 5개 모두 실제 날짜·대표 artifact·입력→처리→결과·혼동 원인·선행/후속·직접 수업/교안/후속 경계를 갖췄다. frontmatter 필수 키·source 실경로·허용 태그·위키링크·placeholder·주 raw 15/15와 scoped `git diff --check`, FrontEnd_BackEnd raw status/diff를 확인했다. index는 확장된 내용과 명백히 어긋난 3개 설명만 갱신했다.
- 상태: 단계 4 FrontEnd_BackEnd는 미완료다. 세션 7만 처리했으며 세션 8과 단계 5 Linux는 시작하지 않았다.

## [2026-07-16] update | FrontEnd_BackEnd Summary 후반부 B·허브 고도화

- 범위: 실행 분할 세션 6의 지정 대상인 2026-04-21·04-22 날짜 summary와 FrontEnd_BackEnd 총정리 허브 3개만 전면 재작성했다. 다른 summary·concept·entity·comparison 본문과 `raw/`는 수정하지 않았다.
- 흐름 복원: 04-21은 04-20의 Paging UI 준비→React page parameter·Spring Page 응답→단순 Pageable backend→검색 state/request·SearchDto·개별 Specification 준비, 04-22는 Repository→Service 조건 조립·sort/PageRequest→Controller parameter·Page 응답→MySQL 기간·카테고리·다중 조건 시나리오 순서로 정리했다.
- 허브 복원: R01~R18 날짜 Summary를 대조해 환경→Fruit→Member/회원가입→JWT→Product CRUD→Cart→Order→대표 상품→페이징/검색의 실제 날짜 귀속, 기능별 대표 artifact와 요청·응답 왕복을 연결했다. R19 총정리 원본이 실제로는 04-15 Cart 삭제에서 끝난다는 범위도 명시했다.
- 핵심 경계: Paging/search control의 표시와 실제 request/response 연결, 04-21 frontend·조건 준비와 04-22 backend 검색 완성, 직접 수업·교안 보충·Linux/AWS/CI/CD/Passwordless/중간 프로젝트 후속 확장을 분리했다.
- provenance: P03·P08·P10·I01~I05의 필요한 설명이 텍스트 raw와 날짜 Summary에 충분히 전사되어 있어 별도 source를 추가하지 않았다. code fence는 전체 0개/선언 텍스트 raw 원문 검증 0개/수동 fence 예외 0개다.
- 검증: summary↔주 raw 3/3, 04-21·04-22 교시 흐름·이전/다음·artifact·입력→처리→결과·혼동·직접/후속 경계와 허브의 R01~R19 흐름·날짜 링크·왕복·근거 경계를 확인했다. frontmatter·source·태그·위키링크·index 설명·placeholder·scoped diff·`git diff --check`와 FrontEnd_BackEnd raw status/diff를 기록 파일 반영 후 재검사했다.
- 상태: 단계 4 FrontEnd_BackEnd는 미완료다. 세션 6만 처리했으며 세션 7과 단계 5 Linux는 시작하지 않았다.

## [2026-07-16] update | FrontEnd_BackEnd Summary 후반부 A 고도화

- 범위: 실행 분할 세션 5의 지정 대상인 2026-04-15·04-16·04-17·04-20 summary 4개만 날짜 MD 전체 교시 흐름과 4/4 대응해 전면 재작성했다. 다른 summary·concept·entity·comparison 본문과 `raw/`는 수정하지 않았다.
- 흐름 복원: 04-15는 로그인 user props→전체/개별 선택·합계→수량 PATCH와 재고 검증 초안→삭제 백엔드 기반, 04-16은 CartProduct 관계를 이용한 수량 보정·React 삭제→OrderStatus/Entity/DTO→선택 Cart 품목 POST→주문상품·재고·Cart 처리→저장, 04-17은 stock 전달·`some`·오류 Alert→상품 상세 즉시 주문→역할별 PENDING 목록 DTO/API/초기 화면, 04-20은 주문 카드·역할별 버튼→완료/취소·재고 복원→대표 상품 carousel→페이징 시작 순서로 정리했다.
- 핵심 경계: 04-15의 control 표시/handler 연결, 04-16의 Cart 삭제/Order 직접 구현, 04-17의 일반 배열 메서드/실제 Cart 사용, 04-20의 이전 날짜 Order 생성·목록 시작/당일 상태 처리와 후반 Product 전환을 분리했다. 각 페이지에 이전·다음 날짜, 대표 artifact, 입력→처리→결과, 실제 혼동 원인과 직접 수업/후속 검색·페이징·Linux·AWS·CI/CD·Passwordless 경계를 명시했다.
- 보조자료·provenance: P03·P08·I01~I04의 필요한 용어·관계·실습 흐름이 날짜 MD에 충분히 전사되어 있어 별도 PDF/이미지 주장이나 source를 추가하지 않았다. summary code fence는 전체 0개/선언 텍스트 raw 원문 검증 0개/수동 fence 예외 0개다.
- 검증: summary↔raw 4/4, 날짜·전체 교시 흐름·이전/다음·artifact·입력→처리→결과·혼동·직접/후속 경계와 필수 섹션 4/4를 확인했다. frontmatter·source 실경로·허용 태그·위키링크·index 설명·placeholder·scoped diff와 `git diff --check`, FrontEnd_BackEnd raw status/diff를 검사했다.
- 상태: 단계 4 FrontEnd_BackEnd는 미완료다. 세션 5만 처리했으며 세션 6과 단계 5 Linux는 시작하지 않았다.

## [2026-07-16] update | FrontEnd_BackEnd Summary 중반부 고도화

- 범위: 실행 분할 세션 4의 지정 대상인 2026-04-09·04-10·04-13·04-14 summary 4개만 날짜 MD 전체 교시 흐름과 4/4 대응해 전면 재작성했다. 다른 summary·concept·entity·comparison 본문과 `raw/`는 수정하지 않았다.
- 흐름 복원: 04-09는 관리자 삭제 클릭→버블링 방지→ProductService/Controller의 이미지·DB 처리→목록 state 갱신→등록 route/form 시작, 04-10은 event/spread→form state→FileReader→POST body→이미지 저장·Validation 오류→수정 form 시작, 04-13은 상품 수정 GET/PUT→상세 GET/useEffect→Cart/CartProduct 관계·장바구니 요청 준비, 04-14는 인증 사용자→Cart 추가·동일 품목 수량 누적→CartItemDto 목록→React CartList 표시 순서로 정리했다.
- 내용 경계: 일반 table/JSX와 Product 기능, 등록/수정의 공통점·차이, Product 마무리/Cart 시작, 추가 DTO/목록 DTO를 구분했다. 각 페이지에 이전·다음 날짜, 대표 artifact, 입력→처리→결과, 실제 혼동 원인과 직접 수업/후속 Cart 수량·삭제·Order·검색/페이징·Linux·AWS·CI/CD·Passwordless 경계를 명시했다.
- 보조 근거·provenance: Router 그림은 화면 안내 비유만, 장바구니 그림은 Member–Cart–CartProduct–Product 관계와 quantity만 사용했다. summary code fence는 0개이므로 전체 0개/선언 텍스트 raw 원문 검증 0개/수동 fence 예외 0개다.
- 검증: summary↔raw 4/4, 날짜·전체 교시 흐름·이전/다음·artifact·입력→처리→결과·혼동·직접/후속 경계 4/4를 확인했다. frontmatter·source 실경로·허용 태그·위키링크·index 설명·placeholder·필수 섹션·scoped diff와 `git diff --check`, FrontEnd_BackEnd raw status/diff를 검사했다.
- 상태: 단계 4 FrontEnd_BackEnd는 미완료다. 세션 4만 처리했으며 세션 5와 단계 5 Linux는 시작하지 않았다.

## [2026-07-15] update | FrontEnd_BackEnd Summary 전반부 B 고도화

- 범위: 실행 분할 세션 3의 지정 대상인 2026-04-03·04-06·04-07·04-08 summary 4개만 날짜 MD 전체 교시 흐름과 4/4 대응해 전면 재작성했다. 다른 summary·concept·entity·comparison 본문과 `raw/`는 수정하지 않았다.
- 흐름 복원: 04-03은 Member seed와 SignupPage event→Repository→Service→Controller→Validation/BindingResult→저장·응답, 04-06은 Cookie/Session/JWT·MPA/SPA→axiosInstance/LoginPage→LoginDto/JwtTokenProvider, 04-07은 String/Bearer→JWT Filter·SecurityContext와 별도 사용자 조회 경로→CORS/SecurityConfig→login/logout 테스트, 04-08은 Category/Product→이미지 seed·단위 테스트→목록 REST API→React Product type·card 화면 순서로 정리했다.
- 내용 경계: 각 페이지에 이전·다음 날짜, 대표 artifact, 입력→처리→결과, 실제 혼동 원인과 직접 수업/후속 Product·Cart·Order·Linux·AWS·CI/CD·Passwordless 경계를 명시했다. 04-08의 OCI는 raw의 짧은 소개·가입 자료 안내 범위만 보존하고 상품 기능을 중심에 두었다.
- provenance: summary에는 code fence를 사용하지 않았다. 따라서 fence 전체 0개/선언 텍스트 raw 원문 검증 0개/수동 예외 0개이며, PDF 전용 주장이나 합성 코드를 추가하지 않았다.
- 검증: summary↔raw 4/4, 날짜·전체 교시 흐름·이전/다음·artifact·입력→처리→결과·혼동·직접/후속 경계 4/4를 확인했다. frontmatter·source 실경로·허용 태그·위키링크·index 설명·placeholder·scoped diff와 `git diff --check`, FrontEnd_BackEnd raw status/diff를 검사했다.
- 상태: 단계 4 FrontEnd_BackEnd는 미완료다. 세션 3만 처리했으며 세션 4와 단계 5 Linux는 시작하지 않았다.

## [2026-07-15] update | FrontEnd_BackEnd Summary 전반부 A 고도화

- 범위: 실행 분할 세션 2의 지정 대상인 2026-03-30~04-02 날짜 summary 4개만 각 날짜 MD 전체 교시 흐름과 4/4 대응해 전면 재작성했다. 다른 summary·concept·entity·comparison 본문과 `raw/`는 수정하지 않았다.
- 흐름 복원: 03-30은 환경 준비→Spring 정적 응답→Vite React→MySQL/Spring 설정→`Fruit`, 03-31은 `FruitHtmlController`/Thymeleaf→REST JSON→React 컴포넌트/Router, 04-01은 `Fruit` type→axios/state/effect→CORS/`WebConfig`→목록/props, 04-02는 React Bootstrap HomePage→Member JPA/Validation→Security→Repository/DI 순서로 정리했다.
- 내용 경계: 각 페이지에 이전·다음 날짜, 대표 artifact, 입력→처리→결과, 실제 혼동 원인과 직접 수업/후속 Member·JWT·Product·Linux·AWS 확장 경계를 명시했다. 원본에 없는 코드·출력·사용자 질문을 만들지 않았고 새 지식 페이지도 만들지 않았다.
- 보조 근거: 세션 범위 이미지 I03의 Router 안내 비유와 I05의 template→Controller→Service→Repository→DB 계층 도식을 확인했다. 날짜별 직접 구현 순서는 해당 날짜 MD를 우선했으며 summary에는 code fence를 사용하지 않았다.
- 검증: summary↔raw 4/4, 필수 내용 구조 4/4, code fence 0개/원문 검증 0개/수동 예외 0개다. frontmatter·source 실경로·허용 태그·위키링크·index 설명·placeholder 오류 0건, scoped whitespace와 `git diff --check` 통과, FrontEnd_BackEnd raw status 0건·diff exit 0을 확인했다.
- 상태: 단계 4 FrontEnd_BackEnd는 미완료다. 세션 2만 처리했으며 세션 3과 단계 5 Linux는 시작하지 않았다.

## [2026-07-15] update | FrontEnd_BackEnd 읽기 감사·실행 분할 계획

- 범위: `raw/KoreaICT/4. FrontEnd_BackEnd` 실제 파일 34개(Markdown 19, PDF 10, PNG 5)를 전체 경로로 재고화했다. Markdown은 날짜별 18개와 총정리 1개이며, 독립 코드·설정 파일은 없고 코드 근거는 MD 내부 fence에 있다.
- 중복·보조자료: 과목 내부 byte-identical 중복과 0바이트 파일은 0개다. `IntelliJ 교안.pdf`는 Java 과목의 동일 교안과 byte-identical인 보존형 중복이며, PDF/PNG는 날짜 MD의 수업일·실습 순서를 대체하지 않는 보조 근거로 분류했다.
- wiki 대응: FrontEnd_BackEnd raw를 직접 source로 가진 기존 지식 페이지 56개(summary 19, concept 20, entity 9, comparison 8, query 0)를 전수 대응했다. 분류 초안은 유지 5, 부분 보강 19, 전면 재작성 30, 통합 후보 2, 근거 부족·미분류 0이며 신규 후보 4개는 실행 세션에서 생성/흡수 여부를 재판정한다.
- 실행 분할: 이번 세션을 포함해 총 16개 세션으로 나눴다. summary 5개 묶음(각 4개 이하), Frontend/React/TypeScript 및 Backend/Spring/인증/데이터 concept 5개 묶음(각 5개 이하), entity 2개 묶음, comparison/query 2개 묶음(각 6개 이하), 최종 고정점 1개 세션이다.
- 기록: `wiki/_meta/frontend-backend-rehighquality-inventory-plan.md`를 만들고 index에 등록했다. 이번 기록은 과목 완료가 아닌 읽기 감사·실행 분할 계획이며, 기존 지식 페이지 본문과 `raw/`는 수정하지 않았고 단계 5 Linux도 시작하지 않았다.

## [2026-07-15] update | UI&UX 비동기 3계통 감사 반영 및 최종 재검증

- 배경: 단계 3의 첫 완료 기록 뒤 병렬 summary, concept, entity/comparison 감사 3계통이 도착했다. 감사 시점이 본 수정과 겹쳐 이미 해결된 지적과 실제 잔여 공백을 현재 wiki와 raw에 다시 대조했다.
- 분류 정정: 기존 21개는 유지 1, 부분 보강 16, 전면 재작성 4로 확정했다. 03-24·03-26·03-27 날짜 summary와 UI&UX 총정리 허브는 실제 날짜 흐름·artifact 차이·혼동을 중심으로 전면 재작성급 보강했고, jQuery concept는 기존 구조를 유지하며 경미 보강했다.
- 추가 보정: UI/UX 첫 정의와 IntelliJ/DevTools 흐름, list/span/box/non-Bootstrap CartList, 날짜 노트와 현재 ProductInsertForm의 id/grid/error class 차이, ProductList alert와 ProductDetailNew URL 이동의 분리, jQuery selector/class/file명 차이를 복원했다. raw에서 확인되지 않은 `.addClass(...).attr(...).show()` 합성 method-chaining 예시는 제거했다.
- 신규 판단: `wiki/concepts/html-form-controls-submission.md`, `wiki/comparisons/ui-vs-ux.md`, `wiki/comparisons/custom-css-vs-bootstrap.md`를 신설했다. CSS layout·JavaScript 언어 기초는 기존 concept 보강으로 유지했고 loading/error/success 상태도 JavaScript DOM·03-26 summary에 흡수했다. 반복된 독립 사용자 질문 근거가 없어 query는 0개다.
- 최종 검증: UI&UX 대상은 기존 21개+신규 3개=24개다. raw 96/96, code fence 39개(HTML 11, CSS 3, JavaScript 25)를 39/39 원문 연속 코드로 대조했다. 전체 지식 페이지 265개, source 974건, 위키링크 1,801건이며 frontmatter·source·허용 태그·깨진/모호 링크·index 등록/페이지 수·유형별 내용 게이트 오류는 0건이다.
- raw/범위 경계: `raw/KoreaICT/3. UI&UX`는 수정하지 않았고 status/diff 0건을 유지했다. `FrontEnd&BackEnd.pdf`는 UI&UX 교육자료 경계로만 확인했으며 단계 4 FrontEnd_BackEnd 감사·수정은 시작하지 않았다.

## [2026-07-15] update | 내용 재고도화 단계 3 UI&UX 완료

- 범위: `raw/KoreaICT/3. UI&UX` 실제 파일 96개(Markdown 8, PDF 5, HTML 59, CSS 1, JavaScript 1, PNG 11, JPG 9, GIF 2)와 직접 관련 기존 wiki 21개(summary 6, concept 4, entity 5, comparison 6)를 전수 대응했다. 감사 분류는 21개 모두 부분 보강이며 유지·전면 재작성·통합 후보·근거 부족·미분류는 0개다.
- 실제 수정: 기존 21개에 날짜별 학습 순서, 실제 table/form/상품 목록-상세/jQuery image 코드, 실행 데이터 흐름, 혼동 원인, 직접 구현과 후속 React·Spring 확장 경계를 보강했다. 독립 학습 단위는 기존 페이지로 충분하고 실제 보존 질문도 없어 신규 페이지와 query는 만들지 않았다.
- 내용 정정: 총정리 원본의 `<alt>` 표기를 실제 `img` 속성으로 교정하고, non-Bootstrap form→Bootstrap class 적용, relative 부모→absolute 자식, 더미 배열→DOM card→query string→`Number`→`find`, jQuery 선택→이벤트→class/attribute/display/노드 이동 흐름을 복원했다. POST는 주소창에 보이지 않는 것만으로 안전하지 않으며 HTTPS·서버 검증이 필요함을 명시했다.
- 코드 근거: 의미만 같던 축약·합성 fence를 날짜별 MD와 교육 HTML/CSS/JavaScript의 연속된 실제 코드로 교체했다. 최종 code fence 37개(HTML 10, CSS 3, JavaScript 24)를 37/37 원문 대조했다. PDF에서 추출되지 않은 코드나 실행 결과는 만들지 않았다.
- 검증: 전체 지식 페이지 262개, source 908건, 위키링크 2,031건이며 frontmatter·source 존재·허용 태그·깨진 링크·index 등록/페이지 수·유형별 내용 게이트·raw 재고 96/96·대응표 21행·scoped diff 오류는 0건이다. `wiki/index.md`의 UI&UX 21개 설명을 현재 내용에 맞게 갱신했고 `Total pages: 262`를 유지했다.
- raw/범위 경계: `raw/KoreaICT/3. UI&UX`의 Git status와 diff는 0건이며 수정하지 않았다. 해당 폴더의 `FrontEnd&BackEnd.pdf`는 UI&UX 재고의 교육자료 경계만 확인했고 단계 4 날짜별 raw·관련 wiki 감사/수정은 시작하지 않았다.

## [2026-07-15] update | Oracle 비동기 3계통 감사 반영 및 최종 재검증

- 배경: 단계 2 완료 직후 병렬로 실행한 summary, concept, entity/comparison 감사 3계통이 도착했다. 감사 시점이 본 수정과 겹쳐 이미 해결된 지적과 실제 잔여 공백을 현재 파일·raw에 다시 대조했다.
- 추가 보정: 03-16의 INSERT 방식·DBeaver 단축키·COMMIT/ROLLBACK·BOARDS/PRODUCTS/sequence 후반, 03-17의 삭제 테스트·제약조건 5종·DDL 재생성, 03-18의 `SAVEPOINT`·`ORA-12899` 우선순위·A04/A05 source 불일치, 03-19의 `RTRIM` 문자 집합·GROUP BY 오해, 03-20의 1NF→2NF→3NF·No Action·관리자/ORAMAN/GOMDORI View 세션을 복원했다.
- 정확성 경계: Oracle DDL implicit commit과 DBeaver Auto Commit, sequence gap과 `NOCACHE`, 서브쿼리의 논리적 읽기와 옵티마이저의 물리 실행, FK의 PK/UNIQUE 참조와 nullable 조건을 구분했다. 03-30부터 MySQL·MySQL Driver·Spring Data JPA 환경으로 전환했음을 명시해 Oracle→JPA가 같은 DB 실행환경의 연속으로 보이지 않게 했다.
- 신규 concept: `wiki/concepts/oracle-data-dictionary-schema-objects.md`를 만들었다. 03-17·03-20·총정리에 반복된 `USER_TABLES`, `USER_SEQUENCES`, `USER_VIEWS`를 DDL 결과와 사용자 소유 schema 객체 검증이라는 독립 학습축으로 정리하고 index·시퀀스·View·Oracle entity에 연결했다. 실제 질문은 기존 concept/comparison에 흡수돼 별도 query는 만들지 않았다.
- 최종 검증: 기존 28개+신규 1개=Oracle 지식 페이지 29개, raw 24개, SQL fence 61/61을 통과했다. 전체 지식 페이지 262개, source 904건, 위키링크 2,028건이며 frontmatter·source 존재·허용 태그·깨진 링크·index 누락·페이지 수·placeholder·scoped diff 오류는 모두 0건이다.
- raw/범위 경계: `raw/KoreaICT/2. Oracle` Git 상태는 0건이며 수정하지 않았다. UI&UX는 시작하지 않았다.

## [2026-07-15] update | 내용 재고도화 단계 2 Oracle 완료

- 범위: Oracle raw 24개(날짜별 MD 6개, 총정리 1개, PDF 3개, 수업 SQL 14개)와 관련 기존 wiki 28개(summary 7, concept 12, entity 2, comparison 7)를 전수 대응했다. 감사 분류는 부분 보강 19개, 전면 재작성 7개, 통합 후보 2개이며 미분류·근거 부족은 0개다.
- 실제 수정: 기존 28개를 모두 수업 순서·대표 SQL·혼동 원인·선행/후속 연결 중심으로 고도화했다. 통합 후보 `oracle-constraints-sequence`와 `oracle-functions-join-subquery`는 각각 공동 overview와 03-19 탐색 지도로 역할을 명확히 해 유지했다. 기존 페이지로 학습 단위가 충분해 신규 페이지와 query는 만들지 않았다.
- 내용 정정: DBMS/클라이언트와 관리자/일반 사용자를 구분하고, 시퀀스→데이터 사전→PK/FK, 제약조건 위반→트랜잭션→DDL/DQL, 함수→집계→JOIN→서브쿼리, 이상 현상→함수 종속성→분해→FK/JOIN 흐름을 복원했다. 원본의 “X는 기본키, Y는 외래키” 메모를 함수 종속성의 일반 정의로 사용하지 않도록 교정하고, JOIN/FK·`MAX(id)`/`NEXTVAL`·`COUNT(*)`/`COUNT(expr)`·`WHERE`/`HAVING`·DB `ON DELETE`/JPA cascade 경계를 명시했다.
- 원문 경계: 원본에 없던 합성 SQL을 만들지 않도록 모든 SQL fence를 MD/SQL source와 재대조했다. schema 접두사·축약 함수·임의 WHERE 조건·결합 HAVING처럼 원문과 달랐던 표기는 실제 03-18~03-19 SQL로 교체했다. View의 `password` 컬럼은 수업 문법 예제임을 밝히고 실제 서비스의 비밀값 비노출 경계를 추가했다.
- 검증: 대상 28개·raw 24개·대응표 28행, SQL fence 56/56, 시작(03-16)·중간(03-19)·끝(03-20)·총정리 고위험 대조 4/4를 통과했다. 전체 위키는 지식 페이지 261개, source 883건, 위키링크 1,750건, frontmatter/source/허용 태그/링크/index 누락·초과 오류 0건이며 `Total pages: 261`과 일치했다. 대상 범위 `git diff --check`도 통과했다.
- raw 경계: Oracle raw에 쓰기 도구를 사용하지 않았다. 최종 Git 상태는 시작과 같은 tracked modified 64개·untracked 3개였고, raw status의 유일한 항목은 작업 전부터 있던 `raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md`였다. 다음 단계 UI&UX는 시작하지 않았다.

## [2026-07-15] update | 내용 재고도화 단계 1 Java 완료

- 범위: 기존 Java summary 13개, concept 13개, Java·Git·GitHub·IntelliJ entity 4개, comparison 4개를 전수 감사했다. 감사 분류는 유지 1개, 부분 보강 22개, 전면 재작성 10개, 통합 후보 1개이며, 통합 후보는 고유 역할을 강화해 유지했다.
- 실제 수정: 기존 34개를 모두 고도화하고 `java-access-modifier-encapsulation` concept과 `java-homework-research-review` summary를 신설해 최종 대상은 36개가 됐다. 별도 query는 만들지 않았다.
- 내용 정정: 02-26 변수 읽기/쓰기, 02-27 증감 추적과 Git 전체 흐름, 03-03 형변환·char, 03-04 `printf`, 03-06 입력 배열·요구/구현 불일치, 03-10 `Animal` 날짜 귀속과 원천 코드 불일치, 03-12 `beverageCount`·기능 인터페이스를 복원했다. 비근거 `Cookable`·`Iceable` 예시는 실제 `Beverage05`, `WaterAdjustable`, `ShotAddable`, `MilkAddable`, `SpecialCoffee05` 흐름으로 교정했다.
- 근거 경계: Java 직접 수업과 숙제 사전조사, 이후 Spring/프로젝트 확장을 분리했다. 03-13 프로젝트 세부는 raw 근거가 없어 팀 프로젝트·코드 리뷰 사실만 남겼고, 숙제의 메모리·컬렉션·제네릭 및 현대 Java 인터페이스 예외는 직접 실행 여부와 정확성 경계를 명시했다.
- 검증: Java 대상 36개·frontmatter source 155건에서 유형별 내용 게이트, 존재 source, 허용 태그, 링크, placeholder, 고립, 비근거 인터페이스명을 검사해 오류 0건이었다. 전체 위키는 지식 페이지 261개, source 881건, 위키링크 1,731건, index 누락·초과·오류 0건이며 `Total pages: 261`과 일치했다. 추적/미추적 대상 모두 `git diff --check`를 통과했다.
- raw 경계: `raw/KoreaICT/1. Java`의 status/diff는 0건으로 Agent가 수정하지 않았다. 작업 중 대상 밖 `raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md` 변경이 별도로 나타났으나 이 세션에서는 읽기 확인만 하고 수정·되돌리기하지 않았다. Oracle은 시작하지 않았다.

## [2026-07-15] create | LLM Wiki 내용 재고도화 작업 계획

- 목적: 구조 lint 중심의 기존 완료 판정에서 벗어나, 사용자가 직접 다시 공부할 수 있고 Agent도 수업 맥락을 복원할 수 있도록 기존 wiki를 과목별로 내용 재고도화하는 실행 계획을 만들었다.
- 세션 단위: 과목 하나의 감사 → 수정 → 검증을 새 세션 하나에서 완결한다. 정상 완료 보고 마지막에는 다음 과목 하나의 복붙 프롬프트를 제공하고, 미완료 시에는 같은 과목의 재개 프롬프트를 제공한다.
- 순서: Java → Oracle → UI&UX → FrontEnd_BackEnd → Linux → AWS → Ci&CD → Passwordless → 중간 프로젝트 공부 → Python → 전체 통합 품질 검증.
- 완료 기준: 구조 정합성뿐 아니라 실제 raw 대조, 구체 실습·혼동·이전/다음 연결, 페이지 유형별 내용 게이트, 미분류 후보 0건, scoped diff 검증을 요구한다. `raw/`는 수정하지 않았다.

## [2026-07-15] update | 날짜 기반 학습 회상 규칙

- 목적: 공유된 Vault를 Codex 등 다른 Agent가 작업 폴더로 열어도 “어제 뭐 했지?” 같은 학습 회상 질문을 날짜별 원본 수업 메모 기준으로 답하도록 공통 규칙을 추가했다.
- 반영: `AGENTS.md` Query 작업 순서 아래에 현재 날짜 계산, `raw/KoreaICT/` 날짜 메모 최우선 조회, wiki summary 보조 활용, 수업 메모 부재 시 명시적 안내 규칙을 추가했다. `wiki/log.md`·Git 수정 시각으로 학습 내용을 추측하지 않도록 명시했다.
- 경계: `raw/`는 수정하지 않았으며, 이 규칙은 Hermes 전용 memory/skill이 아닌 Vault 공유 규칙으로 유지한다.

## [2026-07-14] update | 9. 중간 프로젝트 공부 provenance 보강

- 범위: 중간 프로젝트 CI/CD·Passwordless 관련 wiki 4개 페이지의 `sources`에서 절대 경로 10개를 현재 Vault 상대 경로 `raw/KoreaICT/9. 중간 프로젝트 공부/...`로 정정했다. 새 페이지를 만들지 않아 Total pages는 258로 유지했다.
- P1 보강: CI/CD·Passwordless 가이드 summary에 GitHub Secrets 역할, CI Docker Hub push → CD EC2 container 갱신, 외부 인증 서버·QR·앱 승인, RS256 개인키 서명·공개키 검증 근거 marker 4개를 추가했다. CI/CD 배포 흐름 concept에는 백엔드 환경 변수·Dockerfile 준비, Secret 항목 역할, CI/CD 책임 분리, React `/api`·Nginx proxy·S3·도메인 확장 근거 marker 4개를 추가했다.
- 안전 경계: 실제 IP, endpoint, password, token, private key, Secret 값은 추가하지 않았고 `raw/`는 수정하지 않았다.

## [2026-07-14] lint | 전체 Vault 통합 정합성 점검

- 범위: `wiki/` Markdown 전체를 재집계하고, 과거 감사 리포트의 전체 수치 표현, frontmatter·source 경로·태그·위키링크·index 등록·본문 링크 기준 고립 후보와 `raw/KoreaICT` 과목별 frontmatter 출처 누적을 함께 점검했다. `raw/`는 수정하지 않았다.
- 현재 수치: Markdown 260개(`index.md`, `log.md` 포함), 지식 페이지 258개이며 `wiki/index.md`의 `Total pages: 258`과 일치한다. 감사 리포트의 현재값으로 남아 있던 247/245만 260/258로 갱신했고, 235·243/241 등 과거 작업 기록 수치는 역사 문맥으로 보존했다.
- 결과: frontmatter 누락·빈 `sources`·존재하지 않는 source 경로·허용 밖 태그·깨진/모호 링크·index 누락은 모두 0개다. 과목별 frontmatter 출처는 Java·Oracle·UI&UX·FrontEnd_BackEnd·Linux·AWS·Ci&CD·Passwordless·중간 프로젝트·Python 10개 범위에서 실제 경로로 확인했다.
- 보정: `txt-to-md-conversion-work-plan`의 운영 source를 명시하고, Linux Apache/Nginx concept·Linux 총정리·변환 작업 인계의 본문 링크를 보강해 고립 후보 3개를 해소했다.

## [2026-07-13] ingest | 10. Python 최신 MD 기준 고도화

- 범위: `raw/KoreaICT/10. Python` 날짜별 MD 14개와 `Python 총정리.md`를 실제 내용으로 대조해 Python/Pandas/Jupyter 관련 wiki를 고도화했다. `raw/`는 수정하지 않았다.
- 정정: 기존 wiki의 학습 경계가 2026-07-03 Pandas 집계·시각화에 멈춰 있던 상태를 07-06 공공데이터 API·자전거 분석, 07-07 Selenium/지오코딩/지도, 07-08 한국어 텍스트 마이닝까지 확장했다.
- 신규: 날짜별 summary 3개와 Python 총정리 허브, 외부 데이터 수집·한국어 텍스트 마이닝 concept, Selenium/Folium/KoNLPy entity, BeautifulSoup vs Selenium comparison을 추가했다.
- 범위 lint: frontmatter·sources·링크·index 등록·민감값 재노출·페이지 수·scoped diff를 확인한다.

## [2026-07-13] ingest | 8. Passwordless 최신 MD 기준 고도화

- 범위: `raw/KoreaICT/8. Passwordless` 날짜별 MD 6개와 `Passwordless 총정리.md`를 실제 내용으로 대조해 Passwordless 관련 summary, concept, entity, comparison을 고도화했다. `raw/`는 수정하지 않았다.
- 정정: X1280 핵심 인증 흐름(소개 → Members/`setting.ap` → Docker Auth/User Connection/Push Request → Spring·MariaDB·Tomcat 샘플 → Postman REST API)과 05-19 AAM/APE 기업형 인증 관리, 05-20 FilingBox/NAS/WORM 저장소 보호를 분리했다.
- 출처 경계: React polling·callback, JWT/세션, Member 상태, DTO/Service/Controller/SecurityConfig의 전체 프로젝트 설계는 8과목 날짜 수업 직접 구현이 아니라 9과목 중간 프로젝트 Passwordless 적용 가이드의 확장 범위로 표기했다.
- 신규: `concepts/nas-worm-storage-protection`, `entities/aam-ape`, `comparisons/authentication-vs-authorization`를 추가하고 index Total pages를 248로 갱신했다. 범위 lint는 frontmatter·sources·링크·민감값 재노출·페이지 수·scoped diff를 확인한다.

## [2026-07-13] ingest | 7. Ci&CD 최신 MD 기준 고도화

- 범위: 2026-05-11~13 날짜별 MD와 `Ci&CD 총정리.md`를 실제 내용으로 대조해 CI/CD 관련 summary, concept, entity, comparison을 고도화했다. `raw/`는 수정하지 않았다.
- 정정: 기본 `ci.yml`의 Maven CI, Docker Hub image build/push 확장, 별도 `cd.yml`을 통한 EC2 배포 연결을 구분했다. 날짜 원본에 없는 `cd.yml` 구현 전문과 HTTP 80 listener 구성은 추정하지 않고, EC2 container 갱신·ALB HTTPS Listener 역할로만 보존했다.
- 반영: Route 53 Hosted Zone/NS → ACM CNAME 검증·발급 → ALB Target Group/HTTPS Listener → Alias A record, Terraform IaC, S3 객체 저장 → RDS `coffee.product`의 `image_url` 저장 흐름을 최신 원본에 맞췄다.
- 신규 페이지는 만들지 않아 index Total pages 245를 유지했다. 범위 lint는 frontmatter·sources·링크·민감값 재노출·source 귀속·scoped diff를 확인한다.

## [2026-07-13] ingest | 6. AWS 최신 MD 기준 고도화

- 범위: 2026-05-06~08 날짜별 MD와 `AWS 총정리.md`를 실제 내용으로 대조해 AWS wiki를 고도화했다. `raw/`는 수정하지 않았다.
- 정정: 05-07은 VPC·EC2·EIP·SSH·자원 해제, 05-08은 ping/ICMP·Nginx·Spring Boot jar·RDS MySQL·자원 정리로 날짜 경계를 바로잡았다. AWS 05-08에 잘못 귀속된 Route 53/ACM/ALB 실습은 실제 원본 `7. Ci&CD/2026.05.12(화)`로 재귀속했다.
- 신규: `concepts/aws-resource-lifecycle-cost-management`를 생성해 On-Demand 비용, EIP release, EC2/RDS·네트워크 자원의 의존성 기반 정리 흐름을 보존했다.
- index: 05-08 summary rename을 반영하고 신규 concept 1개를 등록해 Total pages를 245로 갱신했다. 범위 lint는 sources·frontmatter·링크·rename 잔존 경로·민감값 재노출·scoped diff를 확인한다.

## [2026-07-13] ingest | 5. Linux 최신 MD 기준 고도화

- 범위: `raw/KoreaICT/5. Linux`의 날짜별 MD 10개와 `Linux 총정리.md`를 주 출처로 삼아 Linux/Docker/GitHub 관련 summary, concept, entity, comparison을 최신 원본의 실습 흐름에 맞게 고도화했다. `raw/`는 수정하지 않았다.
- 반영: VM/SSH·CLI → 파일/vi·사용자/권한 → 다운로드/압축·JDK → Maven/Spring Boot jar·host 포트 → Docker image/container/network/mount/Dockerfile/Compose → Git/GitHub branch/PR/conflict 흐름을 subject-review 및 기존 관련 페이지의 구체 실습 근거에 연결했다.
- 신규 비교: `virtual-machine-vs-docker-container`, `host-port-forwarding-vs-docker-port-mapping`을 생성해 VM/SSH/Linux/container 층위와 Linux host 포트 전환/Docker `-p`의 반복 혼동을 분리했다.
- index: 신규 비교 2개를 등록하고 Total pages를 244로 갱신했다. 고정점 검증은 Linux 범위 frontmatter·출처·링크·원본 경로·diff 점검으로 수행한다.

## [2026-07-13] update | TXT→MD 작업 단계 완료 상태 정정

- 정정: 9. 중간 프로젝트 공부의 민감정보 후보 탐지·처리는 이미 완료되었으며, 변환·재작성 대상이 아니다.
- 현재 상태: 5~8과목 날짜별 TXT→MD와 과목 총정리, 10. Python 지정 범위 날짜별 TXT→MD와 Python 총정리가 완료되었다. 이에 따라 TXT→MD 정리 단계는 종료되었다.
- 다음 단계: 현재 `raw/KoreaICT/` MD를 기준으로 과목별 wiki 고도화 ingest를 수행하고, 과목별 lint 후 전체 통합 lint를 진행한다.
- 반영: `wiki/_meta/txt-to-md-conversion-work-plan.md`의 9과목 상태와 새 세션 체크리스트를 현재 완료 상태에 맞게 갱신했다. `raw/`는 수정하지 않았다.

## [2026-07-13] update | 10. Python Python 총정리 MD 작성

- 범위: 사용자의 명시 지시에 따라 Python 날짜별 MD 14개(`2026.06.19(금) - 시작`~`2026.07.08(수)`)를 내용 근거로 사용해 `raw/KoreaICT/10. Python/Python 총정리/Python 총정리.md`를 새로 작성함. 기존 총정리의 표현·형식만 참고했으며, wiki ingest와 lint는 시작하지 않음.
- 내용: 기본 문법·컬렉션·함수·객체지향에서 예외 처리·파일 입출력·정규 표현식·XML/JSON으로 이어지고, Pandas Series/DataFrame·CSV·시각화·결합·그룹화·범주화, 공공데이터 API·Selenium 크롤링·Folium 지도·한국어 텍스트 마이닝까지 날짜별 수업 흐름으로 재구성함.
- 검증: 흐름 화살표 4개를 모두 prose `-\>`로 확인하고, fence 18개(`python` 18)의 균형·첫/끝 빈줄·언어·본문을 전수 감사함. prose-in-fence·code-outside-fence·분리 code unit 0건이며, scoped `git diff --check` exit 0과 새 untracked MD의 `git diff --no-index --check` 무출력을 기록 반영 전에 확인함.
- 계획 정정: `wiki/_meta/txt-to-md-conversion-work-plan.md`의 기존 Python 총정리 사용자 작성 제외 규칙을 이번 사용자 명시 지시에 따른 완료 사실로 갱신함.

## [2026-07-13] update | 8. Passwordless Passwordless 총정리 MD 작성

- 범위: 완료된 Passwordless 날짜별 원본/결과 MD 6개(`2026.05.14(목) - 시작`~`2026.05.21(목)`)만 내용 근거로 사용해 `raw/KoreaICT/8. Passwordless/Passwordless 총정리/Passwordless 총정리.md`를 새로 작성함. 기존 Linux·AWS·Ci&CD·FrontEnd_BackEnd 총정리는 제목·`#### \#` 라벨·공백·fence 표현 형식만 참고했으며, wiki ingest와 lint는 시작하지 않음.
- 내용: 위협 모델(피싱·랜섬웨어·RCE·DDoS)과 제로트러스트에서 출발해 X1280 Passwordless·인증/인가·IDP·SSO·상호인증, Members 서비스 등록, Docker 기반 Auth/User Connection/Push Request 서버, Spring·MariaDB·Tomcat 연동, AAM/APE, FilingBox WORM, Postman REST API까지 날짜별 수업 순서로 재구성함.
- 검증: 흐름 화살표 5개를 모두 prose `-\>`로 확인하고, fence 8개(`shell` 5·`properties` 1·`sql` 1·`json` 1)의 균형·첫/끝 빈줄·언어·본문을 전수 감사함. prose-in-fence·code-outside-fence·분리 code unit 0건이며, scoped `git diff --check` exit 0과 새 untracked MD의 `git diff --no-index --check` 무출력을 기록 반영 전에 확인함.
- 기록: `wiki/_meta/txt-to-md-conversion-work-plan.md` 완료 표에 같은 작업 단위 행을 추가함.

## [2026-07-13] update | 7. Ci&CD Ci&CD 총정리 MD 작성

- 범위: 완료된 Ci&CD 날짜별 MD 3개(`2026.05.11(월) - 시작`~`2026.05.13(수)`)만 내용 근거로 사용해 `raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md`를 새로 작성함. 기존 Linux·AWS·FrontEnd_BackEnd 총정리는 제목·`#### \#` 라벨·공백·fence 표현 형식만 참고했으며, wiki ingest와 lint는 시작하지 않음.
- 내용: GitHub Actions의 Maven CI, GitHub Secrets와 Docker Hub 인증, EC2 Docker Container 배포, Route 53·ACM·ALB HTTPS/분산 처리, Terraform IaC, S3 이미지 업로드와 RDS MySQL 연결을 날짜별 수업 순서로 재구성함.
- 검증: Markdown escape, fence 20개(`java` 1·`properties` 2·`xml` 2·`yaml` 2·`shell` 7·`text` 3·`hcl` 1·`json` 1·`sql` 1) semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0을 기록 반영 전에 확인함.
- 기록: `wiki/_meta/txt-to-md-conversion-work-plan.md`의 완료 표에 같은 작업 단위 행을 추가함.

## [2026-07-13] update | 6. AWS AWS 총정리 MD 작성

- 범위: 완료된 AWS 날짜별 원본/대응 MD 3개(`2026.05.06(수) - 시작`~`2026.05.08(금)`)만 내용 근거로 사용해 `raw/KoreaICT/6. AWS/AWS 총정리/AWS 총정리.md`를 재작성함. 기존 총정리는 제목·`#### \#` 라벨·공백·fence 표현 형식만 참고했으며, wiki ingest와 lint는 시작하지 않음.
- 내용: AWS 서비스/용어, CIDR·VPC·Subnet·IGW·Route Table·Security Group, EC2 2대·탄력적 IP·SSH, ping·nginx·Spring Boot 배포, RDS MySQL·`application.properties`·SQL, 비용을 고려한 자원 정리 흐름을 날짜별 수업 순서로 재구성함.
- source 흐름 정정: 날짜별 AWS 자료에서 근거를 확인하지 못한 Route 53·ACM·Load Balancer 구간은 기존 총정리에서 복사하지 않고 제거함.
- 검증: Markdown escape, fence 14개(`shell` 10·`text` 2·`properties` 1·`sql` 1) semantic inventory, prose-in-fence·code-outside-fence·분리 code unit·실제 credential 값 0건, scoped `git diff --check` exit 0을 기록 파일 반영 전 확인함.
- 기록: `wiki/_meta/txt-to-md-conversion-work-plan.md`의 완료 표에 같은 작업 단위 행을 추가함.

## [2026-07-13] update | 10. Python 2026.06.25(목) TXT→MD 변환

- 범위: 외부 `10. Python/2026.06.25(목)/2026.06.25(목).txt` 1개만 대응 `raw/KoreaICT/10. Python/2026.06.25(목)/2026.06.25(목).md`로 변환·덮어씀. 9. 중간 프로젝트 공부와 다음 Python 파일은 진행하지 않음.
- 민감정보 게이트: 실제 외부 원본 TXT 837행을 credential 문맥·짧은 PW 값·로그인 역방향 표기·직접 secret 대입까지 검사해 실제 값 후보 0건을 확인한 뒤 변환함.
- 검증: 원본 순서·공백 역대조 0건 불일치(날짜 줄·직후 선행 공백 제거와 줄끝 공백 11건 정규화 예외), Markdown escape, fence 24개(`python` 20·`text` 4) semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check`은 기록 파일까지 포함해 최종 확인함.
- 기록: `wiki/_meta/txt-to-md-conversion-work-plan.md`의 파일별 완료 표에 같은 완료 행을 추가함.

## [2026-07-13] update | 10. Python 2026.06.24(수) TXT→MD 변환

- 범위: 외부 `10. Python/2026.06.24(수)/2026.06.24(수).txt` 1개만 대응 `raw/KoreaICT/10. Python/2026.06.24(수)/2026.06.24(수).md`로 변환·덮어씀. 9. 중간 프로젝트 공부와 다음 Python 파일은 진행하지 않음.
- 민감정보 게이트: 실제 외부 원본 TXT 663행을 credential 문맥·직접 secret/token 대입까지 검사해 실제 값 후보 0건을 확인한 뒤 변환함.
- 검증: 원본 순서·공백 역대조 0건 불일치(날짜 줄·직후 선행 공백 제거와 빈 줄의 trailing whitespace 2건 정규화 예외), Markdown escape, fence 33개(`python` 26·`text` 7) semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0.
- 기록: `wiki/_meta/txt-to-md-conversion-work-plan.md`의 파일별 완료 표에 같은 완료 행을 추가함.

## [2026-07-13] update | 10. Python 2026.06.23(화) TXT→MD 변환

- 범위: 외부 `10. Python/2026.06.23(화)/2026.06.23(화).txt` 1개만 대응 `raw/KoreaICT/10. Python/2026.06.23(화)/2026.06.23(화).md`로 변환·덮어씀. 9. 중간 프로젝트 공부와 다음 Python 파일은 진행하지 않음.
- 민감정보 게이트: 실제 외부 원본 TXT 868행을 credential 문맥·로그인 역방향 표기까지 검사해 실제 값 후보 0건을 확인한 뒤 변환함.
- 검증: 원본 순서·공백 역대조 0건 불일치(날짜 줄·직후 선행 공백 제거와 terminal EOF 빈 줄 정규화 예외), Markdown escape, fence 36개(`python` 27·`text` 9) semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0.
- 기록: `wiki/_meta/txt-to-md-conversion-work-plan.md`의 파일별 완료 표에 같은 완료 행을 추가함.

## [2026-07-13] update | 10. Python 2026.06.22(월) TXT→MD 변환

- 범위: 외부 `10. Python/2026.06.22(월)/2026.06.22(월).txt` 1개만 대응 `raw/KoreaICT/10. Python/2026.06.22(월)/2026.06.22(월).md`로 변환·덮어씀. 9. 중간 프로젝트 공부와 다음 Python 파일은 진행하지 않음.
- 민감정보 게이트: 실제 외부 원본 TXT 906행을 credential 문맥·로그인 역방향 표기까지 검사해 실제 값 후보 0건을 확인한 뒤 변환함.
- 검증: 원본 순서·공백 역대조 0건 불일치(날짜 줄·직후 선행 공백 및 후행 공백 정규화 예외), Markdown escape, fence 30개(`python` 22·`text` 8) semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0.
- 기록: `wiki/_meta/txt-to-md-conversion-work-plan.md`의 파일별 완료 표에 같은 완료 행을 추가함.

## [2026-07-13] update | Python 빈 N) 단계 라벨 Markdown 렌더링 정정

- 정정: `10. Python/2026.06.19(금) - 시작`의 빈 단계 라벨 `1)`, `2)` 끝에 ASCII 공백 1개를 추가함. Obsidian Markdown에서 ordered list로 렌더링하기 위한 의도적 공백임.
- 검증: 대상 68·74행이 각각 정확히 `1) `·`2) `임을 확인함. scoped `git diff --check`의 trailing-whitespace 2건은 이 두 렌더링 예외와 정확히 일치하며, 다른 후보는 없음.
- 재발 방지: 빈 `N)` 단계 라벨은 이후 TXT→MD 변환에서도 끝 공백 1개를 반드시 유지함.

## [2026-07-13] update | Python 출력 화살표와 text fence 경계 정정

- 정정: `10. Python/2026.06.19(금) - 시작` 결과 MD에서 코드 실행 뒤의 `->`는 출력 자체가 아니라 설명 연결 표기이므로 fence 밖 prose로 유지하도록 확인·보정함.
- 적용: 오류 예제의 `->`는 기존에도 fence 밖에 있었음을 확인했고, 형변환 예제의 `-> 나이 : 30`을 `text` fence 밖 prose로 이동함. Traceback·실제 출력 묶음만 `text` fence에 남김.
- 재발 방지: 이후 TXT→MD에서 코드/출력 관계 화살표 `->`는 fence 밖 prose로 두고, 실제 출력만 `text` fence로 분리함.

## [2026-07-13] update | 10. Python 2026.06.19(금) - 시작 TXT→MD 변환

- 범위: 외부 `10. Python/2026.06.19(금) - 시작/2026.06.19(금) - 시작.txt` 1개만 대응 `raw/KoreaICT/10. Python/2026.06.19(금) - 시작/2026.06.19(금) - 시작.md`로 변환·덮어씀. 다음 파일은 진행하지 않음.
- 민감정보 게이트: 실제 외부 원본 TXT 806행을 검사해 credential 문맥 뒤 실제 값 후보 0건을 확인한 뒤 변환함.
- 검증: 원본 순서·공백 역대조 0건 불일치(날짜 줄·직후 선행 공백 및 EOF 빈 줄 정규화 예외), Markdown escape, fence 29개(`python` 26·`text` 3) semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0.
- 기록: `wiki/_meta/txt-to-md-conversion-work-plan.md`의 파일별 완료 표에 같은 완료 행을 추가함.

## [2026-07-13] update | TXT→MD 다음 작업 단위 정정

- 정정: Passwordless 2026.05.21(목) 변환 완료 뒤 다음 작업을 `8. Passwordless 총정리 작성`으로 잘못 안내한 것을 바로잡음.
- 현재 순서: 9. 중간 프로젝트 공부는 변환 대상이 아니므로 건너뛰고, 10. Python의 제한 범위(`2026.06.19(금) - 시작`~`2026.06.25(목)`) 날짜별 TXT→MD 변환을 먼저 진행함.
- 다음 단위: 외부 `10. Python/2026.06.19(금) - 시작/2026.06.19(금) - 시작.txt` 1개만 민감정보 검사 후 대응 `raw/KoreaICT/10. Python/2026.06.19(금) - 시작/2026.06.19(금) - 시작.md` 변환.

## [2026-07-13] update | 8. Passwordless 2026.05.21(목) TXT→MD 변환

- 범위: 외부 `8. Passwordless/2026.05.21(목)/2026.05.21(목).txt` 1개만 대응 `raw/KoreaICT/8. Passwordless/2026.05.21(목)/2026.05.21(목).md`로 변환·덮어씀. 다음 파일은 진행하지 않음.
- 민감정보 게이트: 사용자가 `수정했어`로 명시 재개한 뒤 실제 원본 TXT를 재검사해 `{MASKED}` 외 credential·서버 인증값 후보 0건을 확인함. 외부 TXT는 수정하지 않음.
- 검증: 원본 순서·공백 역대조 0건 불일치(날짜 줄·직후 선행 공백, EOF 빈 줄 및 후행 탭 정규화 예외), Markdown escape, fence 12개(`shell` 11·`json` 1) semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0.
- 기록: `wiki/_meta/txt-to-md-conversion-work-plan.md`의 파일별 완료 표에 같은 완료 행을 추가함.

## [2026-07-13] update | 8. Passwordless 2026.05.20(수) TXT→MD 변환

- 범위: 외부 `8. Passwordless/2026.05.20(수)/2026.05.20(수).txt` 1개만 대응 `raw/KoreaICT/8. Passwordless/2026.05.20(수)/2026.05.20(수).md`로 변환·덮어씀. 다음 파일은 진행하지 않음.
- 민감정보 게이트: 사용자가 `수정했어`로 명시 재개한 뒤 실제 원본 TXT를 재검사해 credential·키·토큰·라이선스 값 후보 0건을 확인함. 외부 TXT는 수정하지 않음.
- 검증: 원본 순서·공백 역대조 0건 불일치(날짜 줄·직후 선행 공백 및 EOF 빈 줄 정규화 예외), Markdown escape, shell fence 1개 semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0.
- 기록: `wiki/_meta/txt-to-md-conversion-work-plan.md`의 파일별 완료 표에 같은 완료 행을 추가함.

## [2026-07-13] update | 8. Passwordless 2026.05.15(금) 정정 및 2026.05.18(월) 재검증

- 정정: `raw/KoreaICT/8. Passwordless/2026.05.15(금)/2026.05.15(금).md`에서 fence 밖 설명용 leading `N.` 12개를 `N\.`로 escape하고, 원본 교시 heading의 누락된 `N.` 8개를 복원함.
- 재검증: 5월 15일은 원본·결과 비공백 308행, leading `N.` 33개, 교시 heading 8개를 각각 전수 매핑해 0건 불일치를 확인함. 5월 18일은 비공백 311행, leading `N.` 40개, 교시 heading 8개 전수 매핑이 모두 일치했으며 본문 수정은 없음.
- fence 감사: 5월 15일 16개, 5월 18일 39개 fence가 모두 균형·비어 있지 않음을 확인함. 감사기의 7개 후보는 원본 보존 빈줄 5개와 placeholder 설정값을 포함한 올바른 `properties` fence 2개로 원본 문맥에서 정상 예외로 종결함.
- 검증: 두 파일의 Markdown escape·원본 비공백 순서 역대조 및 scoped `git diff --check` exit 0.

## [2026-07-13] update | 최초 수업 자료 ` - 시작` 경로 동기화

- 사용자가 원본 TXT·변환 MD의 본문은 변경하지 않고, 9. 중간 프로젝트 공부를 제외한 과목별 최초 자료 폴더·파일명에 ` - 시작`을 추가한 구조 변경을 반영함.
- 갱신: Java 첫 수업을 참조하는 wiki 페이지 6개, Passwordless 변환 작업 계획 1개, Passwordless·Python 최초 수업 폴더를 적은 품질 감사 리포트 1개.
- 제외: `raw/`는 수정하지 않았고, append-only 원칙에 따라 기존 `wiki/log.md` 및 로그 아카이브의 과거 경로는 변경하지 않음.
- 검증: 현재 참조 대상의 이전 raw 경로를 전체 재검색하고, 갱신한 새 raw 경로의 실제 존재 여부를 확인함.

## [2026-07-13] update | 8. Passwordless 2026.05.19(화) TXT→MD 변환

- 범위: 외부 `8. Passwordless/2026.05.19(화)/2026.05.19(화).txt` 1개만 대응 `raw/KoreaICT/8. Passwordless/2026.05.19(화)/2026.05.19(화).md`로 변환·덮어씀. 다음 파일은 진행하지 않음.
- 민감정보 게이트: 실제 원본 TXT의 credential·license 후보를 줄 번호 순으로 보고했고, 사용자가 수업용 예시값을 원문 그대로 두도록 `유지하고 이어서`를 명시함. 외부 TXT는 수정하지 않음.
- 검증: 원본 순서·공백 역대조 0건 불일치(날짜 줄·직후 선행 공백 제거와 EOF 빈 줄 정규화 예외), Markdown escape, shell fence 14개 semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0.
- 기록: `wiki/_meta/txt-to-md-conversion-work-plan.md`의 파일별 완료 표에 같은 완료 행을 추가함.

## [2026-07-13] update | 8. Passwordless 2026.05.18(월) TXT→MD 변환

- 범위: 외부 `8. Passwordless/2026.05.18(월)/2026.05.18(월).txt` 1개만 대응 `raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md`로 변환·덮어씀. 다음 파일은 진행하지 않음.
- 민감정보 게이트: 실제 원본 TXT의 후보를 줄 번호 순서대로 보고했고, 사용자가 `수정했어` 후에도 남은 수업용 credential 예시를 `유지하고 이어서`로 명시해 원본 값을 그대로 보존함.
- 검증: 원본 순서·공백 역대조 0건 불일치(날짜 줄·직후 선행 공백 및 EOF 공백 정규화 예외), Markdown escape, fence 39개(`shell` 35·`sql` 2·`properties` 2) semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0.
- 기록: `wiki/_meta/txt-to-md-conversion-work-plan.md`의 파일별 완료 표에 같은 완료 행을 추가함.

## [2026-07-13] update | 8. Passwordless 2026.05.15(금) TXT→MD 변환

- 범위: 외부 `8. Passwordless/2026.05.15(금)/2026.05.15(금).txt` 1개만 대응 `raw/KoreaICT/8. Passwordless/2026.05.15(금)/2026.05.15(금).md`로 변환·덮어씀. 다음 파일은 진행하지 않음.
- 민감정보 게이트: 실제 외부 원본 TXT를 재검사해 후보를 줄 번호 순서대로 보고했고, 사용자가 `유지하고 이어서`를 명시해 실제 계정·비밀번호 값은 원본 그대로 보존함.
- 검증: 원본 순서·공백 역대조 0건 불일치(날짜 줄·직후 선행 공백과 EOF 공백 정규화 예외), Markdown escape, shell fence 16개 semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0.
- 기록: `wiki/_meta/txt-to-md-conversion-work-plan.md`의 파일별 완료 표에 같은 완료 행을 추가함.

## [2026-07-13] update | 8. Passwordless 2026.05.14(목) TXT→MD 변환

- 범위: 외부 `8. Passwordless/2026.05.14(목)/2026.05.14(목).txt` 1개만 대응 `raw/KoreaICT/8. Passwordless/2026.05.14(목)/2026.05.14(목).md`로 변환·덮어씀. 다음 파일은 진행하지 않음.
- 민감정보 게이트: 실제 외부 원본 TXT만 검사했고 credential 문맥 뒤 실제 값 후보는 0건이어서 변환을 진행함.
- 검증: 원본 순서·공백 역대조 0건 불일치(날짜 줄·직후 선행 공백과 EOF 공백 정규화 예외), Markdown escape, fence 0개 semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0.
- 기록: `wiki/_meta/txt-to-md-conversion-work-plan.md`의 파일별 완료 표에 같은 완료 행을 추가함.

## [2026-07-13] update | TXT→MD 다음 세션 인계에 smart 모드 명시

- 사용자가 이후 날짜별 TXT→MD 작업을 smart 모드로 진행하겠다고 지정함.
- 변경: 다음 세션 복붙 프롬프트의 첫 줄을 `smart 모드로 진행한다.`로 고정하고, 해당 모드 명시 누락도 완료 보고 게이트 미충족으로 처리함.

## [2026-07-13] update | 날짜별 TXT→MD 완료 보고의 다음 세션 인계 게이트 강화

- 원인 정정: `다음 파일 자동 실행 금지`를 다음 세션용 복붙 프롬프트 생략으로 잘못 처리한 사례를 재발 방지 대상으로 기록함.
- 변경: `wiki/_meta/txt-to-md-conversion-work-plan.md`에 날짜별 파일 완료 보고의 필수 항목으로 다음 작업 단위 1개의 복붙 프롬프트를 추가함. 해당 프롬프트가 없으면 변환·검증이 통과해도 사용자 보고는 미완료로 본다.
- 적용: 직전 7. Ci&CD 2026.05.13(수) 완료 뒤의 다음 실제 단위는 `8. Passwordless 2026.05.14(목)`으로 확인했으며, 이번 보고 마지막에 해당 프롬프트를 제공함.

## [2026-07-13] update | 7. Ci&CD 2026.05.13(수) TXT→MD 변환

- 범위: 외부 `7. Ci&CD/2026.05.13(수)/2026.05.13(수).txt` 1개를 대응 `raw/KoreaICT/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md`로 변환·덮어씀. 다음 파일은 진행하지 않음.
- 민감정보 게이트: AWS 액세스 키·비밀 키, RDS 비밀번호·endpoint 등 기존 후보가 사용자의 수정 후 모두 `{MASKED}`임을 같은 원본 TXT 재검사로 확인한 뒤 진행함.
- 검증: 원본 순서·공백 역대조 0건 불일치(날짜 첫 줄 제거·끝 공백 정규화만 예외), Markdown escape, fence 12개(`text`, `hcl`, `shell`, `properties`, `xml`, `json`, `sql`) semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0.
- 기록: `wiki/_meta/txt-to-md-conversion-work-plan.md`의 파일별 완료 표에 같은 완료 행을 추가함.

## [2026-07-13] update | TXT→MD·고도화 ingest·lint 단계 계획 재정렬

- 확정 순서: 남은 날짜별 MD를 세션당 파일 1개씩 변환·고정점 검증 → 모든 날짜별 MD 완료 후 과목별 총정리 MD 작성 → 모든 raw MD 완성 후 과목별 고도화 ingest → 과목별 lint → 전체 통합 lint.
- 보류 규칙: 날짜별 변환 또는 총정리 작성이 남아 있는 동안 ingest/lint를 시작하지 않으며, 일부 과목만 선행 ingest하지 않음.
- 세션 인계: 사용자가 `변환작업 시작`이라고 하면 현재 완료 기록 기준의 바로 다음 날짜별 파일만 안내·처리하고, 완료 뒤 다음 세션용 복붙 프롬프트를 제공함. 다음 파일로 자동 연속 진행하지 않음.
- 반영 문서: `wiki/_meta/txt-to-md-conversion-work-plan.md`.

## [2026-07-12] update | Linux 날짜별 MD 기반 총정리 재작성

- 범위: `raw/KoreaICT/5. Linux`의 날짜별 MD 10개를 내용 근거로 삼아 `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md`를 기존 간략 초안에서 전면 재작성함.
- 형식: 사용자 작성 1~4과목 총정리의 일반 텍스트 제목, `#### \\#` 중분류, 원본 흐름·공백·Markdown escape·실제 코드/설정만 fence 처리 규칙을 적용함. 날짜별 노트의 시간대 대분류는 넣지 않음.
- 내용: Ubuntu VM/SSH, 파일 시스템·vi, 사용자·그룹·권한, 다운로드·압축·JDK, Apache/Nginx·Maven·Spring Boot, Docker image/container/network/mount/Dockerfile/Compose, Git/GitHub branch·PR·conflict까지 학습 흐름으로 종합함.
- 검증: 656줄, fence 46개(`shell`, `dockerfile`, `nginx`, `yaml`, `text`)의 균형·빈 본문·semantic inventory 오류 0건, 시간대 heading 0개, scoped `git diff --check` exit 0을 확인함.
- 기록: `wiki/_meta/txt-to-md-conversion-work-plan.md`에 과목 총정리 완료 행을 추가함. 날짜별 Linux MD는 이번 작업에서 수정하지 않음.

## [2026-07-12] update | Linux 날짜별 TXT→MD 재생성

- 범위: 외부 `5. Linux` 원본의 `2026.04.24(금)`, `2026.04.27(월)`~`2026.05.01(금)`, `2026.05.04(월)`, `2026.05.06(수)` 날짜별 TXT 8개를 대응 `raw/KoreaICT/5. Linux/` MD로 재생성·덮어씀.
- 제외: 같은 날짜의 6. AWS 시작 자료, `교육 자료/`, `wiki` ingest. 이전에 사용자 확인한 5과목 민감정보 검사는 재실행하지 않음.
- 검증: 원본 순서·빈 줄 구조 역대조, Markdown escape, fence 균형/빈 본문/경계, prose-in-fence·code-outside-fence, 언어 교차, literal `*` 검사를 고정점으로 반복해 후보 0건을 확인함. 대상 MD는 최종 후보와 SHA-256 일치, scoped `git diff --check` exit 0.
- 기록: 파일별 원본·결과 경로와 검증 결과는 `wiki/_meta/txt-to-md-conversion-work-plan.md`에 8행으로 남김.

## [2026-07-12] create | TXT→MD 남은 과목 변환 작업 인계

- 생성: `wiki/_meta/txt-to-md-conversion-work-plan.md`에 5~8과목 날짜별 TXT→MD 변환과 날짜별 원본 기반 총정리 MD 작성, 9. 중간 프로젝트 공부의 민감정보 탐지 전용 범위, 10. Python의 2026.06.19~06.25 제한 범위를 기록함.
- 총정리 기준: 기존 사용자 작성 총정리 MD는 표현·형식의 기준으로만 사용하고, 새 총정리의 내용은 각 과목 날짜별 원본 TXT 전체에서 종합한다.
- 제외: Python 2026.06.25 이후 파일과 10·11과목 총정리는 사용자 작성 범위로 명시함.
- 원칙: 과목별 실제 외부 원본 TXT 민감정보 검사 → 후보 보고·사용자 명시 재개 → 변환 → semantic fence 포함 고정점 검증 순서를 유지하며, raw/와 외부 TXT는 수정하지 않음.

## [2026-07-11] update | FrontEnd_BackEnd 총정리 fence 언어 라벨 정정

- 원인: FrontEnd_BackEnd 과목의 React/TypeScript 문맥을 fence별 실제 문법보다 우선해, Java/Spring·HTML 블록까지 `typescript`로 일반화했고 일부 React import 예제는 반대로 `java`로 라벨링함.
- 수정: 원본 문맥과 주석을 제외한 실행 코드 문법으로 확정한 fence 라벨만 교정함. SQL 주석·SQL 문 묶음은 `sql`, Spring annotation/`package`/`public String`은 `java`, `<!DOCTYPE html>`은 `html`, React import/JSX는 `typescript`로 유지·정정함.
- 재발 방지: 전역 `llm-wiki-vault` canonical 규칙에 과목 단위 기본값 금지, 실제 문법 우선, 주석 단서 제외, fence별 기대 언어·근거 inventory 및 언어 불일치 0건 검증을 추가함.

## [2026-07-11] update | FrontEnd_BackEnd 총정리 fence 경계 빈줄 정정

- 원인: 원본 TXT의 단계 구분용 빈줄을 보존하는 과정에서 closing fence를 빈줄 뒤에 두고, 일부는 opening fence를 빈줄 앞에 둬 빈줄이 코드블록의 첫/끝 본문이 됨.
- 수정: `raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md`의 선두·끝 빈줄이 있는 fence 163개에서 경계만 이동해, 빈줄은 fence 밖에 두고 실제 코드/명령/출력만 fence 본문으로 유지함.
- 재발 방지: 전역 `llm-wiki-vault` 스킬에 fence 본문의 첫·끝 빈줄 금지, 원본 빈줄의 fence 외부 귀속, 별도 경계 검증 규칙을 추가함.

## [2026-07-11] update | Linux 첫째·둘째 날짜 TXT→MD 재변환과 dotted-number literal 규칙 실험

- 범위: 외부 `5. Linux/2026.04.22(수) - 시작/2026.04.22(수).txt`, `5. Linux/2026.04.23(목)/2026.04.23(목).txt`만 입력으로 사용해 대응 `raw/KoreaICT/` MD 2개를 재생성함. 기존 MD는 변환 입력·스타일 근거로 사용하지 않음.
- 민감정보 게이트: 첫째 원본의 실제 값 후보 5건은 사용자 검토 후 `유지하고 이어서`를 받았고, 외부 TXT는 수정하지 않음. 둘째 원본은 후보 0건.
- 신규 canonical: prose 줄 시작의 `숫자.`는 `숫자\.`로 escape해 자동 ordered list를 막고, `숫자)`는 그대로 유지함. 교시 heading과 code fence는 이 규칙의 예외임. 전역 `llm-wiki-vault` completion gate에 반영함.
- 검증: 2026-04-22는 원본 비공백 토큰·빈 줄 배치 262줄, 3 bash fence, raw dotted number 0·escaped dotted number 17·`숫자)` 9, Markdown 기호 후보 0. 2026-04-23은 609줄, 44 bash + 1 text fence, raw dotted number 0·escaped dotted number 5·`숫자)` 17, Markdown 기호 후보 0. 두 파일 모두 fence 미분류/빈 fence 0, scoped `git diff --check` exit 0.

## [2026-07-10] update | Linux 2026-04-23 TXT→MD fence 경계 재감사와 완료 판정 정정

- 정정 사유: 앞선 대상 MD 검증은 fence 짝·빈 fence·기호 escape 중심의 구조 검사 결과를 code/prose 경계까지 검증한 것처럼 잘못 보고했음. `tree / -L 1 명령어 이용`, `tree 입력하면 … 보여줌`이라는 한국어 설명문 2개가 `bash` fence 안에 남아 있었음.
- 수정: 대상 MD에서 위 설명문을 감싼 `bash` fence 2개를 제거하고 원본 흐름의 prose로 복원함. 외부 원본 TXT는 수정하지 않음.
- 전역 재발 방지: Hermes 전역 `llm-wiki-vault` completion gate에 모든 fence의 시작/끝·언어·본문·원본 대응 줄·keep/unfence/needs-review 판정을 전수 목록화하고, fence 안 prose 또는 fence 밖 command-like 줄이 미분류면 실패 처리하도록 보강함. `ex)` 예시는 원본 문맥이 실행 블록임을 증명하지 않는 한 prose로 유지함.
- 재검사: 원본 비공백 토큰·빈 줄 배치 609줄 대조, fence 49개(48 bash·1 text) 균형/빈 fence 0, fence decision needs-review 0, fence 밖 command-like 18개(설명 13·`ex)` 예시 5) 전수 분류, raw `>`·잘못된 `\->`·raw `*`·raw `[]`·standalone `---`·HTML tag·hash 후보 모두 0, scoped `git diff --check` exit 0을 확인함.

## [2026-07-10] update | AGENTS 단일 구조 복구와 Vault 내부 분리 절차 비정본화 정정

- 정정 대상: 아래의 `AGENTS 규칙 의미 보존 분리와 TXT→MD 보조 스킬` 기록은 당시의 분리 시도를 보존하는 과거 사실이며, 현재 정본 구조를 설명하지 않는다.
- 현재 상태 확인: `AGENTS.md`는 페이지 작성·ingest·query·lint 규칙을 다시 포함한 단일 414줄 구조이고, Vault 내부 `agent-rules/`, `agent-skills/`는 존재하지 않는다.
- 정본화 정정: TXT→MD 변환의 canonical 규칙·완료 게이트·재발 방지는 Vault 내부 절차 파일이 아니라 Hermes 전역 `llm-wiki-vault` 스킬이 담당한다. 이 정정으로 `AGENTS.md`를 다시 세분화하거나 Vault 내부 절차 폴더를 재생성하지 않는다.
- 경계: 외부 원본 TXT와 `raw/`는 이 로그 정정에서 수정하지 않음.

## [2026-07-10] update | TXT→MD 짧은 비밀번호 후보 검사 정정

- 원인: 기존 검사 구현이 길이가 긴 credential 중심으로만 후보를 잡아, `암호 : ubuntu`처럼 짧은 수업용 기본 비밀번호를 누락했음.
- 수정: `AGENTS.md`와 활성 `llm-wiki-vault` 스킬에 credential 문맥 뒤 실제 값은 길이와 무관하게 후보로 보고하고, 값 없는 절차 안내문은 후보에서 제외하는 2단계 판정 규칙을 추가함.
- 회귀 검증: `5. Linux/2026.04.22(수) - 시작` 원본에서 실제 값 후보 37·50·55·143·165행 5건을 모두 탐지했고, 값 없는 79·106·114행은 오탐 없이 제외함. 후보가 있으므로 사용자 명시 재개 전 TXT→MD 변환은 시작하지 않음.
- 원칙: 외부 원본 TXT와 `raw/` 결과 MD는 수정하지 않음.

## [2026-07-10] update | TXT→MD 원본 공백 보존 기본값과 검증 정정

- 정정: 특정 코드 fence 뒤 빈 줄만의 사례 규칙이 아니라, 원본 빈 줄의 개수·위치를 보존하는 것을 기본값으로 명시함. fence를 열고 닫아도 원본 공백을 삭제·병합·추가하지 않음.
- 명시 예외: 단독 날짜 줄 제거 뒤 파일 시작 선행 공백 제거, 교시·형제 중분류의 확정된 3줄/0줄 공백 계약만 적용함.
- 검증: 공백 패턴을 원본과 대조하고, 명시 예외 외 공백의 손실·추가·병합을 오류로 분류해 고정점 검증에서 반복 확인하도록 보강함.
- 원칙: raw와 외부 원본 TXT는 수정하지 않음.

## [2026-07-10] update | TXT→MD 민감정보 사용자 게이트와 고정점 검증 순서 명시

- 보강: 민감정보 후보 보고에 원본 TXT 전체 경로, 실제 줄 번호, 감지 종류·근거·신뢰도, 비밀값 전체를 숨긴 마스킹 줄을 필수로 명시함.
- 실행 순서: 실제 원본 TXT의 후보 탐지·보고 → 사용자 직접 판단·필요 시 수정 또는 유지 → `수정했어`/`이어서 해줘` 같은 명시 재개 → 원본 재독 → TXT→MD 변환 → 실제 오류·고위험 후보가 없어질 때까지 반복 검증으로 고정함.
- 경계: 후보가 있으면 AI는 외부 원본 TXT를 자동 수정·마스킹·삭제하지 않고 변환도 시작하지 않음. raw와 외부 원본 TXT는 수정하지 않음.

## [2026-07-10] update | TXT→MD 소스 매핑의 잘못된 일반화 정정

- 정정 사유: 직전 보강이 날짜 MD 본문의 참고 TXT 파일명을 변환 원본 후보처럼 취급하고, 이미 확정된 동일 날짜명 TXT 매핑을 금지하는 잘못된 일반화를 포함했음.
- 확정 기본 루트: 원본은 `C:\Users\ICT02-006\Desktop\한국ICT인재개발원\교육`, 결과는 `D:\Study_LLM_Wiki\raw\KoreaICT`임.
- 정정 규칙: 원본의 과목 아래 상대경로를 결과에 그대로 미러링하고 `.txt`만 `.md`로 바꾼다. 날짜 노트는 동일 날짜 폴더·동일 날짜명 TXT, 과목 총정리는 동일 이름의 총정리 폴더·총정리 TXT를 사용한다. `- 시작` 접미사도 폴더·파일명에 그대로 보존한다.
- 제외: MD 본문의 `(...txt)`, `파일 참조` 표기는 수업 중 참고 자료명일 수 있으므로 변환 원본 선정 근거로 사용하지 않는다. `교육 자료/`는 기본 변환 대상이 아니다.
- 원칙: 외부 원본 TXT와 `raw/`는 수정하지 않음.

## [2026-07-10] update | TXT→MD 외부 원본 소스 매핑 절차 보강

- 문제: 보조 스킬이 외부 원본 TXT를 전제로 했지만, 대상 날짜 MD에서 외부 원본의 하위폴더·복수 TXT 구성을 복원하는 우선순위가 명시되지 않아 Vault 안에서 원본을 찾지 못한 에이전트가 작업을 중단할 수 있었음.
- 근거: `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md`에 `06.장바구니.txt`, `CartList04.txt`처럼 한 날짜 MD가 복수 TXT를 참조하는 표기가 있음을 확인함.
- 보강: `academy-txt-to-md-conversion/SKILL.md`에 사용자 제공 경로 → 과목별 소스 매핑 → MD 본문의 TXT 후보 표기 순서, 날짜명 TXT 단순 추정 금지, 미확정 시 무차별 검색·재변환 금지 규칙을 추가함.
- 생성: `agent-skills/academy-txt-to-md-conversion/references/academy-source-map.template.md`에 `대상 MD → 외부 하위폴더 → 원본 TXT 목록`을 기록하는 과목별 매핑 템플릿을 추가함.
- 원칙: 외부 원본 TXT와 `raw/`는 수정하지 않음.

## [2026-07-10] update | TXT→MD 보조 스킬의 2026-04-14 재현 규칙 보강

- 근거: `2026.04.14(화)` 외부 원본 TXT 기반 재변환 세션과 결과 MD, 사용자 확인 Java·Oracle·UI&UX canonical 샘플 규칙, FrontEnd_BackEnd 후속 검증 레퍼런스를 대조함.
- 보강: 날짜 노트의 교시/형제 중분류 전 정확한 3줄 공백, 교시 직후 첫 중분류와 원본 연속 라벨의 무공백, 코드 밖 `<`/`>` 전부 escape, React/JSX의 `typescript` fence 고정, 원본 비공백 순서·연속 라벨·공백·fence·특수기호 검증을 명시함.
- 정정: canonical 스타일 근거를 Java·Oracle만이 아니라 사용자 확인 Java·Oracle·UI&UX 수동 변환본 전체로 명시함.

## [2026-07-10] update | AGENTS 규칙 의미 보존 분리와 TXT→MD 보조 스킬

- 목적: 407줄 규모의 `AGENTS.md`가 매 세션에 전부 읽히는 비용을 줄이되, 기존 운영 규칙을 삭제하지 않고 작업별 상세 문서로 분리함.
- 수정: `AGENTS.md`는 Vault 목적·폴더 경계·raw 읽기 전용·세션 시작 규칙·index/log 원칙·작업별 필수 문서 경로를 가진 짧은 진입점/라우터로 정리함.
- 생성: `agent-rules/wiki-authoring.md`에 페이지 형식·링크·출처·태그·유형별 작성·품질·문체 규칙을, `agent-rules/wiki-workflows.md`에 ingest/query/lint·고정점 검증 절차를 이관함.
- 생성: `agent-skills/academy-txt-to-md-conversion/SKILL.md`에 사용자 확인 수동 변환본 기준, 원본·교육 자료 보호, secret 사전 점검, 코드/설명 경계, 고정점 검증을 담은 이식 가능한 TXT→MD 보조 절차를 작성함.
- 생성: `agent-rules/rule-mapping.md`에 기존 AGENTS 절과 새 정본 문서의 매핑을 기록해 규칙 누락을 점검할 수 있게 함.
- 원칙: `wiki/index.md`는 학습 지식 카탈로그이므로 운영 문서를 등록하지 않았고, `raw/`는 수정하지 않음.

## [2026-07-09] update | raw 출처 구조 마이그레이션

- 목적: `raw/Study/`가 개인 공부 전체처럼 보이는 문제를 줄이고, 출처별 raw 구조를 장기 운영에 맞게 정리함.
- 변경: `raw/Study/`를 `raw/KoreaICT/`로 이름 변경하고, `raw/PersonalStudy/`, `raw/PersonalProjects/`, `raw/References/`를 새 출처 구획으로 추가함.
- 이동: `raw/ai-instructions/`와 `raw/markdown-grammar/`는 `raw/References/` 아래로 옮김. `raw/assets/`는 공통 첨부 폴더로 유지함.
- 참조 갱신: `AGENTS.md`, `wiki/`, 관련 raw 참고문서 안의 `raw/Study`, `raw/ai-instructions`, `raw/markdown-grammar` 경로 문자열을 새 경로로 갱신함.
- 원칙: `wiki/`는 출처별로 분할하지 않고 기존 `summaries/concepts/entities/comparisons/queries` 구조를 유지하며, 출처 맥락은 각 페이지의 제목·frontmatter·본문·sources에서 구분한다.

## [2026-07-09] update | 4·5과목 재ingest 표현 정정 및 raw 기준 보강

- 목적: 직전 감사 리포트와 로그의 “전면 재ingest/모두 통과” 표현이 구조 검증 결과를 내용 품질 완료처럼 보이게 한 문제를 정정함.
- 감사 리포트: `wiki/_meta/wiki-quality-audit-2026-07-02.md`의 결론과 4·5과목 섹션을 재검증 필요/정정 완료 기준으로 바꿈.
- 4과목: `raw/KoreaICT/4. FrontEnd_BackEnd` 현재 MD 기준으로 날짜별 summary 18개와 `FrontEnd_BackEnd 총정리` 허브를 기능 흐름 중심으로 재작성/보강함.
- 5과목: `raw/KoreaICT/5. Linux` 현재 MD 기준으로 날짜별 summary 10개와 `Linux 총정리` 허브를 운영·Docker·GitHub 흐름 중심으로 재작성/보강함.
- 관련 concept/entity/comparison: 4과목 16개, 5과목 18개 페이지에 현재 raw MD 기준 재검증 메모를 추가해 단순 일반론이 아니라 수업 기능 흐름으로 읽히도록 보정함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. 후속 검증은 placeholder/source/link/index/log/audit 후보가 새로 나오지 않을 때까지 반복함.


## [2026-07-09] ingest | 4·5과목 현재 MD 기준 전면 재ingest

- 목적: 사용자의 요청에 따라 `raw/KoreaICT/4. FrontEnd_BackEnd` 19개 MD와 방금 재변환된 `raw/KoreaICT/5. Linux` 11개 MD를 기준으로 관련 wiki를 전면 재검증·보정함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. 이번 작업은 wiki ingest이며, 새 페이지를 만들지 않고 기존 4·5과목 summary/concept/entity/comparison의 current-source 기준성을 맞추는 방식으로 수행함.
- 4과목 처리: 날짜별 summary 18개, `FrontEnd_BackEnd 총정리`, 풀스택/상품/장바구니/주문/페이징/JPA/axios/JPQL 관련 기존 페이지의 frontmatter 갱신과 subject-review 허브 재작성.
- 5과목 처리: 날짜별 summary 10개, `Linux 총정리`, Linux/Docker/GitHub 관련 기존 페이지의 frontmatter 갱신과 subject-review 허브 재작성. `Linux 총정리`는 현재 `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md`와 날짜별 MD 10개를 주 출처로 정리함.
- 검증 예정/결과는 같은 날짜 감사 리포트 섹션에 기록함.


## [2026-07-06] ingest | Linux 변경 MD 기준 전면 재ingest

- 목적: 정밀 검증이 끝난 `raw/KoreaICT/5. Linux` 현재 MD를 기준으로 기존 Linux/Docker/GitHub wiki를 증분 보강이 아니라 재작성/재검증함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. 날짜별 MD와 `Linux 총정리`를 주 provenance로 삼고, 교육자료 MD/PDF/이미지는 기존 보강 출처로 유지함.
- 재작성한 summary:
  - `wiki/summaries/2026-04-22-linux-install-ssh-cli.md` ~ `wiki/summaries/2026-05-06-github-branch-pr-conflict.md` 날짜별 10개
  - `wiki/summaries/2026-05-06-linux-subject-review.md`
- 재작성한 concept/entity/comparison:
  - Linux: `linux-cli-files`, `linux-users-permissions`, `linux-package-archive`, `linux-web-server-apache-nginx`, `linux-spring-boot-server-deploy`
  - Docker: `docker-install-permission-setup`, `docker-image-container`, `docker-cp-exec-container-files`, `docker-network-volume`, `docker-reverse-proxy-load-balancing`, `docker-compose-manifest`, `dockerfile-vs-compose`
  - Git/GitHub: `git-github-collaboration`, `git-fetch-vs-pull-vs-clone`, `git`, `github`, `source-tree`
  - entities/comparisons: `linux`, `docker`, `maven`, `docker-commit-vs-dockerfile`, `docker-cp-vs-bind-mount-vs-volume`
- 신규 페이지는 만들지 않아 `wiki/index.md` Total pages는 241을 유지하고, Linux 관련 설명 줄만 현재 원본 기준으로 보정함.


## [2026-07-06] update | FrontEnd_BackEnd 재ingest 후속 품질 점검

- 목적: 방금 재ingest한 FrontEnd_BackEnd wiki를 `AGENTS.md`와 `llm-wiki-vault` 품질 기준에 맞춰 감사 리포트와 연결해 후속 점검함.
- 점검 결과: FrontEnd_BackEnd 대상 27개 파일에서 frontmatter 누락, 빈 sources, `raw/KoreaICT/4. FrontEnd_BackEnd` 출처 누락, placeholder/TODO, index 미등록, scoped 깨진 wikilink, `needs-review`/`confidence: low`가 모두 0개임을 확인함.
- 수정한 파일:
  - `wiki/_meta/wiki-quality-audit-2026-07-02.md` — `updated: 2026-07-06`, 현재 전체 수치 243/241, FrontEnd_BackEnd 후속 점검 섹션 추가.
  - `wiki/index.md` — `jwt-session-cookie-auth`, `axios-interceptor-error-handling`, `product-domain-flow`, `jpa-relationship-mapping`, `entity-vs-dto`, `jpql-vs-sql` 항목 설명 줄 정리.
  - `wiki/concepts/shopping-cart-flow.md`, `wiki/concepts/order-flow.md`, `wiki/concepts/passwordless-x1280-auth-flow.md` — 본문 링크 기준 고립 후보 summary 3개를 자연스럽게 연결.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함.

## [2026-07-06] ingest | FrontEnd_BackEnd 변경 MD 19개 기준 전면 재ingest

- 목적: 방금 변환된 `raw/KoreaICT/4. FrontEnd_BackEnd` MD 19개를 기준으로 기존 FrontEnd_BackEnd wiki를 증분 보강이 아니라 현재 원본 기준으로 재작성/재검증함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. 교육 자료는 이번 패스에서 필요할 때의 보강 출처로만 두고, 기본 provenance는 현재 MD 19개로 삼음.
- 재작성한 summary:
  - `wiki/summaries/2026-03-30-fullstack-environment-setup.md` ~ `wiki/summaries/2026-04-22-product-repository-pageable-search.md` 날짜별 18개
  - `wiki/summaries/2026-04-03-frontend-backend-subject-review.md`
- 보강한 기존 concept:
  - `wiki/concepts/fullstack-project-flow.md`
  - `wiki/concepts/product-domain-flow.md`
  - `wiki/concepts/shopping-cart-flow.md`
  - `wiki/concepts/order-flow.md`
  - `wiki/concepts/pagination-search.md`
- 새로 추가한 durable page:
  - `wiki/concepts/jpa-relationship-mapping.md`
  - `wiki/concepts/axios-interceptor-error-handling.md`
  - `wiki/comparisons/jpql-vs-sql.md`
- `wiki/index.md`에 신규 페이지 3개를 등록하고 Total pages를 241로 갱신함.


## [2026-07-06] lint | UI&UX 태그 허용 목록 후속 정리

- 목적: UI&UX 재ingest 후속 lint에서 `jquery` 태그가 실제 UI&UX 학습 페이지에 사용되었으나 `AGENTS.md` 허용 태그 목록에는 없던 상태를 정리함.
- 결정: jQuery는 2026-03-27 수업과 UI&UX 총정리에서 중심적으로 다룬 프론트엔드 라이브러리이므로 `AGENTS.md` 태그 규칙의 허용 태그에 `jquery`를 추가함. 이어서 전체 태그 lint에 남아 있던 `docker`, `github`도 각각 Linux/Docker·CI/CD/GitHub Actions 학습에서 반복되는 핵심 주제라 허용 태그로 함께 반영함.
- 확인한 `jquery` 태그 사용 페이지:
  - `wiki/summaries/2026-03-27-jquery-ui-interaction.md`
  - `wiki/summaries/2026-03-27-uiux-subject-review.md`
  - `wiki/concepts/jquery-basics.md`
  - `wiki/entities/jquery.md`
  - `wiki/comparisons/javascript-dom-vs-jquery.md`
  - `wiki/comparisons/library-vs-framework.md`
- 추가 반영한 비-UI&UX 태그 사용 페이지:
  - `wiki/concepts/github-actions-secrets-deploy.md` — `github`
  - `wiki/summaries/2026-05-06-linux-subject-review.md` — `docker`
  - `wiki/summaries/2026-05-15-passwordless-x1280-docker-service.md` — `docker`
  - `wiki/summaries/2026-05-18-passwordless-x1280-server-spring-sample.md` — `docker`
- 범위: 이번 정리는 태그 허용 목록 후속 정리이므로 `raw/`는 수정하지 않았고, 새 페이지 생성 없이 `AGENTS.md`와 `wiki/log.md`만 갱신함.

## [2026-07-06] ingest | UI&UX 변경 MD 기준 전면 재ingest

- 목적: `raw/KoreaICT/3. UI&UX`의 날짜별 MD와 `UI&UX 총정리`, `속성들`, `태그들` MD가 갱신된 상태를 기준으로 기존 UI&UX wiki를 증분 보강이 아니라 전면 재작성/재검증함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. 기존 Obsidian 링크 안정성을 위해 파일 삭제 후 재생성이 아니라 기존 UI&UX wiki 파일을 현재 원본 기준으로 갈아엎는 방식으로 수행함.
- 재작성한 summary:
  - `wiki/summaries/2026-03-23-html-css-intro.md`
  - `wiki/summaries/2026-03-24-css-layout-javascript-intro.md`
  - `wiki/summaries/2026-03-25-bootstrap-form.md`
  - `wiki/summaries/2026-03-26-javascript-dom-product-pages.md`
  - `wiki/summaries/2026-03-27-jquery-ui-interaction.md`
  - `wiki/summaries/2026-03-27-uiux-subject-review.md`
- 재작성한 concept/entity/comparison:
  - `wiki/concepts/html-css-basics.md`, `wiki/concepts/javascript-dom.md`, `wiki/concepts/bootstrap-basics.md`, `wiki/concepts/jquery-basics.md`
  - `wiki/entities/html.md`, `wiki/entities/css.md`, `wiki/entities/javascript.md`, `wiki/entities/bootstrap.md`, `wiki/entities/jquery.md`
  - `wiki/comparisons/library-vs-framework.md`, `wiki/comparisons/inline-style-vs-internal-css-vs-external-css.md`, `wiki/comparisons/get-vs-post.md`
- 새로 추가한 comparison:
  - `wiki/comparisons/html-tag-vs-attribute.md`
  - `wiki/comparisons/id-vs-class.md`
  - `wiki/comparisons/javascript-dom-vs-jquery.md`
- `wiki/index.md`에 신규 비교 페이지 3개를 등록하고 Total pages를 238로 갱신함.

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

- 목적: `raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md`를 읽고, Pandas `groupby` 집계, 다중 색인 정리, 사용자 정의 집계, `transform`, `pd.cut`, matplotlib 시각화 흐름을 기존 Python/Pandas/Jupyter 페이지와 연결함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함.
- 새로 추가한 summary: `wiki/summaries/2026-07-03-python-pandas-groupby-visualization.md`.
- 새로 추가한 concept/entity: `wiki/concepts/pandas-groupby-aggregation.md`, `wiki/entities/matplotlib.md`.
- 보강한 기존 페이지: `wiki/concepts/pandas-dataframe-basics.md`, `wiki/entities/python.md`, `wiki/entities/pandas.md`, `wiki/entities/jupyter-notebook.md`, `wiki/_meta/wiki-quality-audit-2026-07-02.md`.
- `wiki/index.md`에 신규 페이지 3개를 등록하고 Total pages를 235로 갱신함.

## [2026-07-03] ingest | Python 날짜별 원본 2026-06-19~2026-06-30

- 목적: `raw/KoreaICT/10. Python`의 2026-06-19~2026-06-30 날짜별 원본을 읽고, Pandas 이전 Python 기초 문법·컬렉션·함수·모듈·표준 라이브러리·객체지향·예외 처리·파일/정규표현식·XML/JSON·Jupyter/Pandas 입문 흐름을 기존 Python/Pandas 페이지와 연결함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함.
- 새로 추가한 summary: 2026-06-19~2026-06-30 Python 날짜별 summary 8개.
- 새로 추가한 concept: `python-basic-syntax`, `python-collections-comprehension`, `python-functions-modules-packages`, `python-file-regex-data-processing`, `python-oop-basics`.
- 보강한 기존 페이지: `wiki/entities/python.md`, `wiki/entities/pandas.md`, `wiki/entities/jupyter-notebook.md`, `wiki/concepts/pandas-dataframe-basics.md`, `wiki/_meta/wiki-quality-audit-2026-07-02.md`.
- `wiki/index.md`에 신규 페이지 13개를 등록하고 Total pages를 232로 갱신함.


## [2026-07-03] ingest | Passwordless 날짜별 원본 2026-05-14~2026-05-21

- 목적: `raw/KoreaICT/8. Passwordless`의 2026-05-14~2026-05-21 날짜별 원본을 읽고, Passwordless/X1280 인증 흐름, QR/앱 승인, Spring Boot 인증 연동, REST API/Postman 실습을 기존 중간 프로젝트 Passwordless 페이지와 연결함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. 원본에 포함된 실습용 IP, 서버키, 라이선스 키, 관리자 비밀번호, DB 비밀번호 같은 민감값은 wiki에 재노출하지 않고 역할/placeholder 설명으로 일반화함.
- 참고한 대표 원본:
  - `raw/KoreaICT/8. Passwordless/2026.05.14(목) - 시작/2026.05.14(목) - 시작.md`
  - `raw/KoreaICT/8. Passwordless/2026.05.15(금)/2026.05.15(금).md`
  - `raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md`
  - `raw/KoreaICT/8. Passwordless/2026.05.19(화)/2026.05.19(화).md`
  - `raw/KoreaICT/8. Passwordless/2026.05.20(수)/2026.05.20(수).md`
  - `raw/KoreaICT/8. Passwordless/2026.05.21(목)/2026.05.21(목).md`
  - `raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md`
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

- 목적: `raw/KoreaICT/7. Ci&CD`의 2026-05-11~2026-05-13 날짜별 원본을 읽고, CI/CD 자동화, GitHub Actions, Docker Hub/EC2 배포, Route 53/ALB/HTTPS 복습, Terraform, S3 파일 업로드를 기존 AWS·중간 프로젝트 CI/CD 흐름과 연결함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. 원본에 포함된 Docker token, AWS access key, RDS password, IP/endpoint 같은 실습용 민감값은 wiki에 재노출하지 않고 placeholder/역할 설명으로 일반화함.
- 참고한 대표 원본:
  - `raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md`
  - `raw/KoreaICT/7. Ci&CD/2026.05.12(화)/2026.05.12(화).md`
  - `raw/KoreaICT/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md`
  - `raw/KoreaICT/7. Ci&CD/교육 자료/CI&CD(SpringBoot_이론).pdf`
  - `raw/KoreaICT/7. Ci&CD/교육 자료/CI&CD(SpringBoot_실습).pdf`
  - `raw/KoreaICT/7. Ci&CD/교육 자료/cloud.02.AWS 교안(실습).pdf`
  - `raw/KoreaICT/7. Ci&CD/교육 자료/cloud.03.AWS 교안(이론).pdf`
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

- 목적: 감사 리포트의 잔여 후보 중 `raw/KoreaICT/6. AWS/2026.05.06(수) - 시작/` ~ `raw/KoreaICT/6. AWS/2026.05.08(금)/` 범위를 다음 과목으로 선정하고, 사용자 날짜 MD가 시간표 템플릿뿐인 점을 확인한 뒤 AWS 교육자료 PDF와 실습 관리 대장을 주 provenance로 삼아 고품질 ingest를 수행함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. 날짜 MD는 비어 있는 시간표 템플릿으로 표시하고, 실제 내용 출처는 확인한 AWS 교육자료에 명시함.
- 참고한 대표 교육자료:
  - `raw/KoreaICT/6. AWS/교육 자료/AWS 기초 용어.pdf`
  - `raw/KoreaICT/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf`
  - `raw/KoreaICT/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf`
  - `raw/KoreaICT/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf`
  - `raw/KoreaICT/6. AWS/교육 자료/실습 관리 대장(텍스트).md`
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

- 목적: `raw/KoreaICT/1. Java` 사용자 정리 MD 14개를 주 자료로 삼고, Java/IntelliJ/GitHub 교안 PDF와 2026-02-27·2026-03-03 문제 이미지를 실제 확인해 기존 Java wiki 1차 정리본을 교안-aware 방식으로 고도화함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. `sources`에는 사용자 정리 MD와 실제 참고한 교안 PDF/문제 이미지 경로를 함께 남김.
- 참고한 대표 교육자료:
  - `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
  - `raw/KoreaICT/1. Java/교육 자료/IntelliJ 교안.pdf`
  - `raw/KoreaICT/1. Java/교육 자료/Github 교안(실습).pdf`
  - `raw/KoreaICT/1. Java/2026.02.27(금)/1번 문제.png` ~ `3번 문제.png`
  - `raw/KoreaICT/1. Java/2026.03.03(화)/연산자 마무리 문제.png` 및 관련 문제 이미지
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

- 목적: `raw/KoreaICT/2. Oracle` 사용자 정리 MD 6개를 주 자료로 삼고, Oracle/DBeaver 교안 PDF와 SQL 스크립트를 실제 확인해 기존 Oracle/DB 1차 wiki 정리본을 재검증·보강함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. `sources`에는 사용자 정리 MD와 실제 참고한 교육자료/SQL 스크립트 경로를 함께 남김.
- 참고한 대표 교육자료:
  - `raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf`
  - `raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf`
  - `raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법(version 2.0).pdf`
  - `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A01.관리자 사용자 생성하기.sql` ~ `A07 조인 실습.sql`
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

- 목적: `raw/KoreaICT/5. Linux` 사용자 정리 MD를 주 자료로 삼고, MD에서 언급된 Linux/Docker/GitHub 교육자료 PDF·PNG·보조 MD를 실제 확인해 기존 Linux 관련 wiki 1차 정리본을 재검증·보강함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. `sources`에는 사용자 정리 MD와 실제 참고한 교육자료 경로를 함께 남김.
- 참고한 대표 교육자료:
  - `raw/KoreaICT/5. Linux/교육 자료/Linux/Linux 이론.pdf`
  - `raw/KoreaICT/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf`
  - `raw/KoreaICT/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf`
  - `raw/KoreaICT/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf`
  - `raw/KoreaICT/5. Linux/교육 자료/Github 교안(실습).pdf`
  - `raw/KoreaICT/5. Linux/교육 자료/AccessRights.png`
  - `raw/KoreaICT/5. Linux/교육 자료/OwnerShip.png`
  - `raw/KoreaICT/5. Linux/교육 자료/로드 밸런싱.png`
  - `raw/KoreaICT/5. Linux/교육 자료/docker image를 docker hub에 업로드 하기.md`
  - `raw/KoreaICT/5. Linux/교육 자료/도커 컴포즈 종합 실습.md`
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

- 목적: `raw/KoreaICT/4. FrontEnd_BackEnd` 사용자 정리 MD 18개를 주 자료로 삼고, MD에서 언급된 교육자료 PDF/PNG를 실제 확인해 기존 FrontEnd_BackEnd 1차 wiki 정리본을 재검증·보강함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. `sources`에는 사용자 정리 MD와 실제 참고한 교육자료 경로를 함께 남김.
- 참고한 대표 교육자료:
  - `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/FrontEnd&BackEnd.pdf`
  - `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf`
  - `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf`
  - `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/JWT(이론).pdf`
  - `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/IT 관련 용어.pdf`
  - `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/필드 검색 기능.pdf`
  - `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/프로그램 흐름 그림.png`
  - `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/라우터 설명 그림.png`
  - `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/쇼핑 카트 데이터 구조 다이어그램.png`
  - `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 01.png`
  - `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 02.png`
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

- 목적: `raw/KoreaICT/3. UI&UX` 사용자 정리 MD 5개를 주 자료로 삼고, MD에서 언급된 UI&UX/HTML/CSS/JS/jQuery 교육자료 PDF·PNG·소스코드를 실제 확인해 기존 UI&UX 1차 wiki 정리본을 재검증·보강함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. `sources`에는 사용자 정리 MD와 실제 참고한 교육자료/소스코드 경로를 함께 남김.
- 참고한 대표 교육자료:
  - `raw/KoreaICT/3. UI&UX/교육 자료/웹 서비스 Ui&UX.pdf`
  - `raw/KoreaICT/3. UI&UX/교육 자료/HTML&JS&CSS 이론(new).pdf`
  - `raw/KoreaICT/3. UI&UX/교육 자료/IT 관련 용어.pdf`
  - `raw/KoreaICT/3. UI&UX/교육 자료/library&framework.png`
  - `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/tableExam.html`
  - `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/boxModelTest.html`
  - `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/CartList.html`
  - `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/CartList.html`
  - `raw/KoreaICT/3. UI&UX/교육 자료/jQueryImageTest/jQueryImageTest.html`
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
- 원칙: `raw/KoreaICT/6. AWS`는 읽기 전용으로 유지했고, 사용자가 제외 지시한 AWS 총정리류는 건드리지 않음. 원본에 있는 실습용 공개 IP, RDS endpoint, DB 비밀번호 예시는 wiki에 그대로 재노출하지 않고 placeholder/보안 메모로 일반화함.
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

- 목적: `raw/KoreaICT/1. Java` ~ `raw/KoreaICT/4. FrontEnd_BackEnd`의 과목별 총정리 MD 4개를 기준으로, 날짜별 summary를 대체하지 않는 복습 허브를 만들고 기존 과목 entity와 연결함.
- 참고한 원본:
  - `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
  - `raw/KoreaICT/2. Oracle/Oracle 총정리/Oracle 총정리.md`
  - `raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
  - `raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md`
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
  - `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md`
  - `raw/KoreaICT/6. AWS/AWS 총정리/AWS 총정리.md`
  - `raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md` ~ `raw/KoreaICT/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md`
  - `raw/KoreaICT/8. Passwordless/2026.05.14(목) - 시작/2026.05.14(목) - 시작.md` ~ `raw/KoreaICT/8. Passwordless/2026.05.21(목)/2026.05.21(목).md`
  - `raw/KoreaICT/10. Python/2026.06.19(금) - 시작/2026.06.19(금) - 시작.md` ~ `raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md`
- 9번 프로젝트 가이드 신규 wiki 페이지:
  - `wiki/summaries/2026-05-middle-project-cicd-passwordless-guide.md`
  - `wiki/concepts/middle-project-cicd-deploy-flow.md`
  - `wiki/concepts/github-actions-secrets-deploy.md`
  - `wiki/concepts/jwt-rs256-key-flow.md`
  - `wiki/concepts/passwordless-x1280-auth-flow.md`
  - `wiki/comparisons/passwordless-vs-password-login.md`
- 보안 원칙: 원본 가이드에 포함될 수 있는 IP, endpoint, password, secret 값은 wiki 본문에서 placeholder와 역할 설명으로 일반화함.

## [2026-07-03] ingest | 5~6 과목 총정리

- 목적: `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md`와 `raw/KoreaICT/6. AWS/AWS 총정리/AWS 총정리.md`를 날짜별 summary를 대체하지 않는 복습 허브로 wiki에 반영함.
- 원칙: `raw/`는 수정하지 않고 `wiki/`만 수정함. 기존 Linux/AWS 날짜별 wiki와 entity 페이지를 우선 보강하고, 총정리 원본은 subject-review summary로 연결함.
- 새로 추가한 summary:
  - `wiki/summaries/2026-05-06-linux-subject-review.md`
  - `wiki/summaries/2026-05-08-aws-subject-review.md`
- 보강한 허브 entity:
  - `wiki/entities/linux.md`
  - `wiki/entities/docker.md`
  - `wiki/entities/aws.md`
- `wiki/index.md`에 신규 summary 2개를 등록하고 Total pages를 201로 갱신함.
