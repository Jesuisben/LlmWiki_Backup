# Wiki Log

> 이 파일은 위키 작업의 시간순 기록이다.  
> append-only로 운영한다. 과거 기록을 임의로 삭제하지 않는다.  
> 형식: `## [YYYY-MM-DD] action | subject`  
> action 예시: `create`, `ingest`, `update`, `query`, `lint`, `archive`, `delete`


## 로그 아카이브

- [[_meta/wiki-log-archive-2026-06|Wiki Log Archive 2026-06]] — 2026년 6월 작업 기록
- [[_meta/wiki-log-archive-2026-07|Wiki Log Archive 2026-07]] — 2026년 7월 작업 기록 중 이번 분할 전까지의 기록

## 현재 로그

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
