---
title: Python 내용 재고도화 전수 재고와 실행 분할 계획
created: 2026-07-19
updated: 2026-07-19
type: meta
tags: [python, curriculum, study-log]
sources:
  - AGENTS.md
  - wiki/index.md
  - wiki/log.md
  - wiki/_meta/wiki-content-rehighquality-work-plan.md
  - wiki/_meta/middle-project-rehighquality-inventory-plan.md
  - raw/KoreaICT/10. Python
status: growing
confidence: high
---

# Python 내용 재고도화 전수 재고와 실행 분할 계획

## 문서 상태와 범위

이 문서는 내용 재고도화 단계 10 Python의 실제 raw 재고, 직접 source 지식 페이지, 선행·후속 경계와 실행 분할 기준선이다.

- 현재 상태: **계획 세션 미완료 — 조사 중 raw manifest 변경 감지**
- 허용된 변경: 이 Meta, `wiki/index.md`, `wiki/log.md`
- 수정하지 않은 범위: `raw/KoreaICT/10. Python`, 기존 Summary·Concept·Entity·Comparison·Query 본문, 상위 단계 완료 표
- 단계 10 전체: **미완료**
- Git commit·push: 수행하지 않음

## 시작 Git·raw 기준선과 변경 감지

- branch: `master...origin/master`
- 시작 Python raw scoped status: `2026.07.01(수).md` 1개가 이미 modified
- 시작 scoped diff: 62 insertions, 3 deletions; raw 전체를 복구·수정·덮어쓰지 않음
- 시작 파일 수/bytes: 69개 / 19,260,879 bytes
- 시작 정렬 SHA-256 manifest digest: `d99db9e86ca0b1cb631dfc83eb7bffa67836c7c5f182947f78515f3a7992166a`
- 관찰 B 파일 수/bytes: 69개 / 19,261,681 bytes
- 관찰 B 정렬 SHA-256 manifest digest: `0744925070ef6becd163c08526e55ed3c90798fcb69e6315a13d7ee4f4124905`
- 관찰 C 파일 수/bytes: 69개 / 19,263,453 bytes
- 관찰 C 정렬 SHA-256 manifest digest: `56a6354b80eee66fb1c399203b79cee93b827ad9f6b430ab338c7d48c05f3dbe`
- 변경 감지: `2026.07.01(수).md`가 시작 33,988 bytes·1,253줄에서 관찰 C 36,562 bytes·1,307줄까지 계속 변경됨
- 종료 관찰 D: 69개 / 19,263,453 bytes / 정렬 SHA-256 manifest digest `56a6354b80eee66fb1c399203b79cee93b827ad9f6b430ab338c7d48c05f3dbe`; 관찰 C와는 같지만 시작과는 다름
- 판정: Agent 도구는 raw 쓰기를 수행하지 않았다. 그러나 시작→종료 manifest가 다르므로 이번 세션에서는 계획 완료를 선언하지 않는다.

## raw 전수 재고 요약

- 실제 파일: **69개**. 아래 파일별 표는 관찰 B(총 **19,261,681 bytes**) 스냅샷이며, 변동 중인 R09는 최종 재고가 아니다.
- Markdown: 관찰 B 기준 **16개·12,287줄** — 날짜 노트 14, 총정리 1, 라이브러리 설치 참고 1
- PDF: **3개** — catalog `/Pages/Count` 기준 62·322·514쪽
- CSV: **31개·10,575줄·header 등을 제외한 data row 10,534개** — 교육 dataset·중간/파생 파일 후보
- Python source: **9개·146줄** — 0바이트 3개 포함
- Python bytecode: **6개** — 생성 artifact
- PNG: **4개** — 실제 그래프 결과 2, 교육용 라이브러리 표 2
- notebook: **0개**, notebook cell/output 재고도 0
- JSON·XML·HTML 독립 파일: 각각 **0개**
- config: **0개**, archive: **0개**, 그 밖의 독립 script: **0개**
- 0바이트: **3개** — S01·S08·S09
- byte-identical 중복: **2그룹** — D27=D29, S01=S08=S09(모두 빈 파일)
- raw Markdown fence: **398개** (`python` 330, `text` 58, `txt` 1, `xml` 1, `json` 1, 무언어 6, `shell` 1)
- raw의 `txt` 1개와 무언어 fence 6개는 실행 세션에서 원문 문맥으로 output/prose/code를 다시 판정한다. raw 자체는 수정하지 않는다.

## raw 식별자와 파일별 역할

| ID | 실제 경로 | 확장자 | bytes | 줄/cell | 역할 |
|---|---|---|---:|---:|---|
| R01 | `raw/KoreaICT/10. Python/2026.06.19(금) - 시작/2026.06.19(금) - 시작.md` | `.md` | 25,029 | 852 | 날짜 노트 |
| R02 | `raw/KoreaICT/10. Python/2026.06.22(월)/2026.06.22(월).md` | `.md` | 26,952 | 964 | 날짜 노트 |
| R03 | `raw/KoreaICT/10. Python/2026.06.23(화)/2026.06.23(화).md` | `.md` | 28,728 | 927 | 날짜 노트 |
| R04 | `raw/KoreaICT/10. Python/2026.06.24(수)/2026.06.24(수).md` | `.md` | 20,664 | 726 | 날짜 노트 |
| R05 | `raw/KoreaICT/10. Python/2026.06.25(목)/2026.06.25(목).md` | `.md` | 27,691 | 873 | 날짜 노트 |
| R06 | `raw/KoreaICT/10. Python/2026.06.26(금)/2026.06.26(금).md` | `.md` | 29,217 | 924 | 날짜 노트 |
| R07 | `raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md` | `.md` | 33,334 | 1,005 | 날짜 노트 |
| R08 | `raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md` | `.md` | 31,536 | 1,143 | 날짜 노트 |
| I01 | `raw/KoreaICT/10. Python/2026.06.30(화)/첨부파일/Pasted image 20260715203348.png` | `.png` | 29,198 | — | 실제 저장 그래프 이미지 |
| I02 | `raw/KoreaICT/10. Python/2026.06.30(화)/첨부파일/Pasted image 20260715203436.png` | `.png` | 15,848 | — | 실제 저장 그래프 이미지 |
| R09 | `raw/KoreaICT/10. Python/2026.07.01(수)/2026.07.01(수).md` | `.md` | 34,790 | 1,268 | 날짜 노트 |
| R10 | `raw/KoreaICT/10. Python/2026.07.02(목)/2026.07.02(목).md` | `.md` | 18,276 | 612 | 날짜 노트 |
| R11 | `raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md` | `.md` | 10,914 | 375 | 날짜 노트 |
| R12 | `raw/KoreaICT/10. Python/2026.07.06(월)/2026.07.06(월).md` | `.md` | 28,911 | 751 | 날짜 노트 |
| R13 | `raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md` | `.md` | 40,080 | 1,169 | 날짜 노트 |
| R14 | `raw/KoreaICT/10. Python/2026.07.08(수)/2026.07.08(수).md` | `.md` | 7,513 | 242 | 날짜 노트 |
| R15 | `raw/KoreaICT/10. Python/Python 총정리/Python 총정리.md` | `.md` | 19,318 | 434 | 과목 총정리 |
| I03 | `raw/KoreaICT/10. Python/교육 자료/Pandas01.png` | `.png` | 42,196 | — | 교육용 라이브러리 표 이미지 |
| I04 | `raw/KoreaICT/10. Python/교육 자료/Pandas02.png` | `.png` | 55,775 | — | 교육용 라이브러리 표 이미지 |
| P01 | `raw/KoreaICT/10. Python/교육 자료/Python&PyCharm 설치&설정.pdf` | `.pdf` | 2,294,665 | — | 설치·이론·실습 교안 |
| P02 | `raw/KoreaICT/10. Python/교육 자료/Python(실습).pdf` | `.pdf` | 6,381,840 | — | 설치·이론·실습 교안 |
| P03 | `raw/KoreaICT/10. Python/교육 자료/Python(이론).pdf` | `.pdf` | 8,983,557 | — | 설치·이론·실습 교안 |
| D01 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/likelyhood.csv` | `.csv` | 392 | 15 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D02 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/likelyhood03.csv` | `.csv` | 151 | 6 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D03 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/likelyhood04.csv` | `.csv` | 136 | 6 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D04 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/meltsheet.csv` | `.csv` | 233 | 5 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D05 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/movie_show.csv` | `.csv` | 176 | 7 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D06 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/payment01.csv` | `.csv` | 296 | 6 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D07 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/payment02.csv` | `.csv` | 427 | 7 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D08 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/payment06.csv` | `.csv` | 126 | 5 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D09 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/payment07.csv` | `.csv` | 444 | 9 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D10 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/payment08.csv` | `.csv` | 408 | 9 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D11 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/pivotFile.csv` | `.csv` | 134 | 7 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D12 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/welfareCleanNew.csv` | `.csv` | 761,134 | 7,530 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D13 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/가전제품.csv` | `.csv` | 759 | 25 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D14 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/가전제품01.csv` | `.csv` | 139 | 7 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D15 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/가전제품02.csv` | `.csv` | 137 | 7 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D16 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/가전제품판매량01.csv` | `.csv` | 89 | 4 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D17 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/가전제품판매량02.csv` | `.csv` | 88 | 4 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D18 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/시험성적향상표.csv` | `.csv` | 689 | 33 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D19 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/시험점수01.csv` | `.csv` | 98 | 7 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D20 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/시험점수02.csv` | `.csv` | 103 | 7 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D21 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/시험점수03.csv` | `.csv` | 116 | 7 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D22 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/시험점수04.csv` | `.csv` | 100 | 6 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D23 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/시험점수05.csv` | `.csv` | 112 | 7 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D24 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/시험점수06.csv` | `.csv` | 96 | 6 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D25 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/시험점수07.csv` | `.csv` | 124 | 9 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D26 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/시험점수08.csv` | `.csv` | 102 | 8 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D27 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/학생정보01.csv` | `.csv` | 68 | 4 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D28 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/학생정보02.csv` | `.csv` | 72 | 4 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D29 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/학생정보07.csv` | `.csv` | 68 | 4 | Pandas 실습 dataset·중간/파생 파일 후보 |
| D30 | `raw/KoreaICT/10. Python/교육 자료/csv 파일들/학생정보08.csv` | `.csv` | 72 | 4 | Pandas 실습 dataset·중간/파생 파일 후보 |
| S01 | `raw/KoreaICT/10. Python/교육 자료/somefolder/__init__.py` | `.py` | 0 | 0 | 0바이트 package/source marker |
| A01 | `raw/KoreaICT/10. Python/교육 자료/somefolder/__pycache__/__init__.cpython-310.pyc` | `.pyc` | 127 | — | 실행/import 과정의 bytecode 생성 artifact |
| A02 | `raw/KoreaICT/10. Python/교육 자료/somefolder/__pycache__/__init__.cpython-311.pyc` | `.pyc` | 163 | — | 실행/import 과정의 bytecode 생성 artifact |
| S02 | `raw/KoreaICT/10. Python/교육 자료/somefolder/character/CharacterModule.py` | `.py` | 238 | 10 | module/package 실습 source |
| A03 | `raw/KoreaICT/10. Python/교육 자료/somefolder/character/__pycache__/CharacterModule.cpython-310.pyc` | `.pyc` | 503 | — | 실행/import 과정의 bytecode 생성 artifact |
| S03 | `raw/KoreaICT/10. Python/교육 자료/somefolder/mymath/MathModule.py` | `.py` | 196 | 10 | module/package 실습 source |
| A04 | `raw/KoreaICT/10. Python/교육 자료/somefolder/mymath/__pycache__/MathModule.cpython-310.pyc` | `.pyc` | 394 | — | 실행/import 과정의 bytecode 생성 artifact |
| A05 | `raw/KoreaICT/10. Python/교육 자료/somefolder/mymath/__pycache__/MathModule.cpython-311.pyc` | `.pyc` | 528 | — | 실행/import 과정의 bytecode 생성 artifact |
| S04 | `raw/KoreaICT/10. Python/교육 자료/somefolder/sansu/SansuModule.py` | `.py` | 113 | 8 | module/package 실습 source |
| A06 | `raw/KoreaICT/10. Python/교육 자료/somefolder/sansu/__pycache__/SansuModule.cpython-310.pyc` | `.pyc` | 338 | — | 실행/import 과정의 bytecode 생성 artifact |
| S05 | `raw/KoreaICT/10. Python/교육 자료/somefolder/test/MainTest01.py` | `.py` | 1,526 | 53 | module/package 실습 source |
| S06 | `raw/KoreaICT/10. Python/교육 자료/somefolder/test/MainTest02.py` | `.py` | 989 | 34 | module/package 실습 source |
| S07 | `raw/KoreaICT/10. Python/교육 자료/somefolder/test/MainTest03.py` | `.py` | 904 | 31 | module/package 실습 source |
| S08 | `raw/KoreaICT/10. Python/교육 자료/somefolder/test/__init__.py` | `.py` | 0 | 0 | 0바이트 package/source marker |
| S09 | `raw/KoreaICT/10. Python/교육 자료/somefolder/test/aaa.py` | `.py` | 0 | 0 | 0바이트 package/source marker |
| D31 | `raw/KoreaICT/10. Python/교육 자료/공공 데이터 이용/공공자전거 대여소 정보(25.12월 기준).csv` | `.csv` | 302,144 | 2,810 | Pandas 실습 dataset·중간/파생 파일 후보 |
| R16 | `raw/KoreaICT/10. Python/교육 자료/라이브러리 설치 파일.md` | `.md` | 397 | 29 | 라이브러리 설치 참고 |

### PDF·이미지 세부

- P01은 Python/PyCharm 설치·설정 교안, P02는 실습 교안, P03은 이론 교안이다. 날짜 노트가 실제 날짜 흐름의 최우선 근거이며 PDF는 보조 근거다.
- I01·I02는 06-30 수업에 물리적으로 저장된 선·막대 그래프 결과다. 그래프 파일 존재는 plotting 결과 보존 근거지만 전체 notebook 실행 성공을 뜻하지 않는다.
- I03은 package 설치/삭제/list·redirection 안내, I04는 과정 사용 라이브러리와 version 표다. 이름과 달리 Pandas DataFrame 결과가 아니라 교육용 환경 자료다.

## 날짜·학습 흐름

| raw | 날짜·단원 | 실제 학습 흐름 |
|---|---|---|
| R01 | 06-19 시작 | 설치·실행 환경 → 출력·문자열·형변환·입력·연산자 |
| R02 | 06-22 | 조건문·반복문·`range` → list·tuple |
| R03 | 06-23 | dict·set·중첩 collection·comprehension → `zip`·`sorted` 등 내장 함수 |
| R04 | 06-24 | 함수·가변 인수·lambda·`map/filter` → module·package |
| R05 | 06-25 | 표준 라이브러리 → class·상속·Has-A |
| R06 | 06-26 | 예외 처리 → 파일 입출력 → 정규표현식 입문 |
| R07 | 06-29 | 정규표현식 심화 → XML·JSON → pip·Jupyter 준비 |
| R08 | 06-30 | Pandas Series/DataFrame 입문 → matplotlib 그래프 |
| R09 | 07-01 | `loc/iloc`·조건 수정 → CSV 입출력·통계·기초 시각화 |
| R10 | 07-02 | `concat`·`merge`·`pivot`으로 결합·재구조화, SQL JOIN 연결 |
| R11 | 07-03 | `groupby`·`agg`·`transform`·범주화 → 집계 시각화 |
| R12 | 07-06 | 공공데이터 API·JSON/XML → DataFrame·CSV → 자전거 지도 분석 |
| R13 | 07-07 | Selenium·BeautifulSoup → 지오코딩·DataFrame → Folium 지도 |
| R14 | 07-08 | 한국어 형태소 분석·불용어·빈도 → WordCloud |
| R15 | 총정리 | 기본 문법부터 Pandas·외부 데이터·지도·텍스트 마이닝까지 연결 |
| R16 | 설치 참고 | 과정 사용 package와 설치 기준을 보조 |

## source·dataset·output·artifact·실행 증거 경계

| 증거 수준 | 현재 raw에서의 판정 |
|---|---|
| 설명·절차 | 날짜 MD·교안에 설치, 문법, 분석 절차가 보존됨 |
| 작성 code | 날짜 MD의 Python/XML/JSON/shell fence와 독립 Python source 9개가 존재 |
| 실제 output·Traceback | text 계열 fence와 06-19 Traceback 1개가 존재; error 단어만으로 실행 실패/성공을 확정하지 않음 |
| 수정 후 재실행 | 오류→수정→재실행 순서가 명시된 단위만 실행 세션에서 인정; 현재 계획에서는 일괄 성공으로 세지 않음 |
| dataset 입력 | CSV 31개가 물리적으로 존재; `read_csv` 입력·중간·파생 방향은 날짜 문맥으로 확정해야 함 |
| DataFrame·통계·그래프 | 날짜 MD에 code·일부 출력이 있고 I01·I02 그래프 2개가 실제 artifact로 존재 |
| 저장 CSV | `to_csv` code와 CSV 파일군은 존재하지만, 동일 실행에서 생성됐다는 provenance가 없는 파일은 결과로 과확정하지 않음 |
| 저장 HTML·notebook | 독립 HTML 0, notebook 0. 지도 `save` code가 있어도 현재 raw에 저장 HTML은 없음 |
| image artifact | 실제 수업 그래프 2개와 교육 이미지 2개를 분리 |
| Python bytecode | pyc 6개는 import/compile 흔적이지만 module 전체와 최종 프로그램 성공 증거는 아님 |
| 외부 API·웹·지도 | 요청·파싱·크롤링·지오코딩·지도 code와 일부 note output은 있으나 현재 raw에 독립 response dump·saved map HTML·browser screenshot이 없음 |
| 한국어 텍스트 마이닝 | 처리 code는 있으나 저장 WordCloud image/notebook artifact는 없음 |
| 현재 raw에 없는 성공 | package 설치 전체, API 응답 전체, 크롤링 최종 재현, 지도 HTML 표시, notebook 전체 실행을 일괄 성공으로 쓰지 않음 |

### 전수 감사에서 확인한 실행·데이터 품질 경계

- 독립 Python source 9개는 모두 AST 구문 검사를 통과했다. 다만 pyc 존재와 구문 통과는 전체 테스트·출력 정확성을 보장하지 않는다.
- R01에는 실제 Traceback → 형변환 수정 code → 정상 결과가 연속으로 있어, 현재 raw에서 가장 강한 오류→수정→재확인 증거다.
- `시험점수08.csv`는 행별 열 개수가 일정하지 않은 ragged CSV이고, 공공 자전거 CSV에는 이름 없는 빈 열이 있다.
- R04의 일부 함수 예제는 기본 인수와 오류 설명 또는 성공/실패 판정 문자열이 서로 맞지 않는 후보가 있다.
- R06의 출석 함수는 선언 매개변수 대신 외부 반복 변수에 의존하는 후보가 있다.
- R09에는 요구한 대상과 실제 DataFrame 선택 행이 다른 후보가 있다.
- R13에는 미정의/오타 변수, 결측 좌표 제거 전 DataFrame 사용, 동일 PNG 파일명 덮어쓰기 가능성이 있다.
- 위 후보는 출력 예시 존재만으로 성공을 확정하지 않고, 해당 실행 세션에서 원문 code·요구사항·결과를 함께 대조한다.

## 직접 source 지식 페이지 재계산

frontmatter `sources`가 Python raw를 직접 가리키는 **지식 페이지**는 Meta를 제외하고 총 **32개**다.

- Summary **15**
- Concept **9**
- Entity **7**
- Comparison **1**
- Query **0**
- 별도 운영 Meta direct source: `wiki/_meta/wiki-quality-audit-2026-07-02.md` 1개 — 지식 페이지 수에서 제외
- 디렉터리 기준과 frontmatter type 기준 불일치: 0
- index 미등록: 0
- source 실경로 누락: 0

### 직접 페이지 전수 분류

| 유형 | wiki 페이지 | Python raw ID | 계획 분류 | 확인 사항 |
|---|---|---|---|---|
| comparison | `wiki/comparisons/beautifulsoup-vs-selenium.md` | R13 | 유지 | 비교 축과 Selenium→page source→BeautifulSoup 조합이 구체적임 |
| concept | `wiki/concepts/korean-text-mining-pipeline.md` | R14 | 부분 보강 | 입력 artifact·단계별 결과·실패/환경 경계 보강 필요 |
| concept | `wiki/concepts/pandas-dataframe-basics.md` | R08, R09, R10, R11, R12, R13 | 부분 보강 | 본문 출처 동기화 후보 2; fence 3개/연속 일치 1개 |
| concept | `wiki/concepts/pandas-groupby-aggregation.md` | R11, R12, R13 | 부분 보강 | 본문 출처 동기화 후보 2; fence 4개/연속 일치 0개 |
| concept | `wiki/concepts/python-basic-syntax.md` | R01, R02 | 전면 재작성 | 구조 오류 없음; 내용 게이트 실행 필요 |
| concept | `wiki/concepts/python-collections-comprehension.md` | R02, R03 | 전면 재작성 | 구조 오류 없음; 내용 게이트 실행 필요 |
| concept | `wiki/concepts/python-external-data-collection-pipeline.md` | R12, R13 | 부분 보강 | 요청→응답→DataFrame→저장·시각화의 실제 완료 상태 보강 필요 |
| concept | `wiki/concepts/python-file-regex-data-processing.md` | R06, R07 | 전면 재작성 | 구조 오류 없음; 내용 게이트 실행 필요 |
| concept | `wiki/concepts/python-functions-modules-packages.md` | R04, R07 | 전면 재작성 | 구조 오류 없음; 내용 게이트 실행 필요 |
| concept | `wiki/concepts/python-oop-basics.md` | R05 | 전면 재작성 | 구조 오류 없음; 내용 게이트 실행 필요 |
| entity | `wiki/entities/folium.md` | R12, R13 | 부분 보강 | 날짜별 사용 이력·HTML 결과 부재·Marker/GeoJSON/HeatMap 책임 보강 필요 |
| entity | `wiki/entities/jupyter-notebook.md` | R07, R08, R09, R10, R11 | 부분 보강 | 구조 오류 없음; 내용 게이트 실행 필요 |
| entity | `wiki/entities/konlpy.md` | R14 | 부분 보강 | 형태소 분석·사용자 사전·JVM 의존성과 실제 처리 이력 보강 필요 |
| entity | `wiki/entities/matplotlib.md` | R11, R12, R13, R14 | 부분 보강 | 본문 출처 동기화 후보 3 |
| entity | `wiki/entities/pandas.md` | R07, R08, R09, R10, R11, R12, R13 | 부분 보강 | 본문 출처 동기화 후보 2 |
| entity | `wiki/entities/python.md` | R01, R02, R03, R04, R05, R06, R07, R08, R09, R10, R11, R12, R13, R14 | 부분 보강 | 본문 출처 동기화 후보 3 |
| entity | `wiki/entities/selenium.md` | R13 | 부분 보강 | WebDriver·wait·동적 상태·BeautifulSoup 전달과 날짜 이력 보강 필요 |
| summary | `wiki/summaries/2026-06-19-python-setup-basic-syntax.md` | R01 | 전면 재작성 | 구조 오류 없음; 내용 게이트 실행 필요 |
| summary | `wiki/summaries/2026-06-22-python-control-flow-collections.md` | R02 | 전면 재작성 | 구조 오류 없음; 내용 게이트 실행 필요 |
| summary | `wiki/summaries/2026-06-23-python-dict-comprehension-builtins.md` | R03 | 전면 재작성 | 구조 오류 없음; 내용 게이트 실행 필요 |
| summary | `wiki/summaries/2026-06-24-python-functions-modules.md` | R04 | 전면 재작성 | 구조 오류 없음; 내용 게이트 실행 필요 |
| summary | `wiki/summaries/2026-06-25-python-standard-library-oop.md` | R05 | 전면 재작성 | 구조 오류 없음; 내용 게이트 실행 필요 |
| summary | `wiki/summaries/2026-06-26-python-exception-file-regex.md` | R06 | 전면 재작성 | 구조 오류 없음; 내용 게이트 실행 필요 |
| summary | `wiki/summaries/2026-06-29-python-regex-xml-json-jupyter.md` | R07 | 전면 재작성 | 구조 오류 없음; 내용 게이트 실행 필요 |
| summary | `wiki/summaries/2026-06-30-python-pandas-series-dataframe-intro.md` | R08 | 전면 재작성 | 구조 오류 없음; 내용 게이트 실행 필요 |
| summary | `wiki/summaries/2026-07-01-python-pandas-dataframe.md` | R09 | 유지 | 커리큘럼 위치·DataFrame 조작·혼동 지점·다음 날짜 연결과 출처가 구체적임 |
| summary | `wiki/summaries/2026-07-02-python-pandas-reshape-merge.md` | R10 | 부분 보강 | fence 3개/연속 일치 1개 |
| summary | `wiki/summaries/2026-07-03-python-pandas-groupby-visualization.md` | R11 | 부분 보강 | fence 6개/연속 일치 1개 |
| summary | `wiki/summaries/2026-07-06-python-public-data-bicycle-analysis.md` | R12 | 전면 재작성 | 구조 오류 없음; 내용 게이트 실행 필요 |
| summary | `wiki/summaries/2026-07-07-python-web-crawling-geocoding-visualization.md` | R13 | 전면 재작성 | 구조 오류 없음; 내용 게이트 실행 필요 |
| summary | `wiki/summaries/2026-07-08-python-korean-text-mining.md` | R14 | 전면 재작성 | 구조 오류 없음; 내용 게이트 실행 필요 |
| summary | `wiki/summaries/2026-07-08-python-subject-review.md` | R15, R01, R14 | 전면 재작성 | 본문 출처 동기화 후보 2 |

### 분류 합계

- 전면 재작성 **17개**
- 부분 보강 **13개**
- 유지 **2개**, 통합 후보 0, 근거 부족 0, 미분류 0
- 유형별: Summary `유지 1 / 부분 2 / 전면 12`, Concept `부분 4 / 전면 5`, Entity `부분 7`, Comparison `유지 1`, Query 0
- 위 수치는 신규 후보와 섞지 않는다.

## raw source union과 frontmatter 비채택 raw

- 직접 지식 페이지의 Python raw source union: **15/69**
- union: R01~R15, 즉 날짜 노트 14개와 총정리 1개
- frontmatter 비채택 raw: **54개** — I01~I04, P01~P03, D01~D31, S01~S09, A01~A06, R16
- 역할 미분류 raw: **0개**. 54개는 누락으로 버리지 않고 교육자료·dataset·source·generated artifact로 모두 재고화했다.
- 실행 세션에서는 주장에 실제로 사용한 supplemental raw만 해당 페이지 frontmatter/body 출처에 채택하고, 단순 파일 존재만으로 sources를 강제하지 않는다.

### frontmatter sources와 본문 출처 동기화 후보

다음 6페이지는 frontmatter에 선언된 최신 날짜 source 중 본문 출처 절에서 경로/파일명이 직접 확인되지 않는 후보가 있다. 실행 세션에서 실제 claim 사용 여부를 확인해 본문 출처를 보강하거나 불필요 source를 제거한다.

- `wiki/concepts/pandas-dataframe-basics.md` — 2개
- `wiki/concepts/pandas-groupby-aggregation.md` — 2개
- `wiki/entities/matplotlib.md` — 3개
- `wiki/entities/pandas.md` — 2개
- `wiki/entities/python.md` — 3개
- `wiki/summaries/2026-07-08-python-subject-review.md` — 2개

`wiki/entities/jupyter-notebook.md`는 선언 source 벡터 자체는 본문과 맞지만, 07-06 실행환경 확장 claim에 해당 날짜 source가 없어 claim-level 보강 후보로 별도 관리한다.

## raw↔wiki 책임 대응

| raw 묶음 | 주 직접 페이지 책임 | supplemental 대응 |
|---|---|---|
| R01~R07 | 날짜 Summary 7, Python core Concept 5, Python/Jupyter Entity | P01~P03, S01~S09, A01~A06, R16 |
| R08~R11 | 날짜 Summary 4, DataFrame/groupby Concept, Pandas/Jupyter/matplotlib Entity | I01~I04, D01~D30 |
| R12 | 공공데이터 Summary, 외부 데이터 pipeline, Pandas/Folium/Python Entity | D31 |
| R13 | 크롤링 Summary, 외부 데이터 pipeline, Selenium/Folium Entity, BeautifulSoup vs Selenium | 저장 HTML artifact는 없음 |
| R14 | 텍스트 마이닝 Summary·Concept, KoNLPy/matplotlib/Python Entity | 저장 WordCloud image는 없음 |
| R15 | 과목 총정리 Summary와 Python/Pandas/Jupyter Entity의 전체 이력 | 보조 raw를 날짜 결과로 소급하지 않음 |

## 선행·후속·교차 과목 경계

직접 32페이지와 다음 경계 페이지를 분리해 센다.

| 구분 | 별도 경계 페이지 | 현재 연결 판정 |
|---|---|---|
| 선행 | `concepts/oracle-sql-functions` | Oracle 집계·GROUP BY/HAVING → Pandas `groupby`·`agg` |
| 선행 | `concepts/oracle-join` | Oracle JOIN의 결합·inner/outer 보존 범위 → Pandas `merge` |
| 선행 | `entities/html` | HTML element·attribute 구조 → BeautifulSoup 파싱 |
| 선행 | `concepts/javascript-dom` | DOM·이벤트·동적 화면 → Selenium 자동화 |
| 선행 | `concepts/spring-boot-rest-api` | REST method·URL·JSON 응답 모양 → JSON 수집·DataFrame 변환 |
| 교차 | `comparisons/where-vs-having` | SQL 집계 전후 필터 ↔ Pandas 행/그룹 필터 |
| 교차 | `comparisons/mpa-vs-spa` | 완성 HTML과 JavaScript 렌더링·REST JSON ↔ BeautifulSoup/Selenium 선택 |
| 교차 | `comparisons/entity-vs-dto` | DB row·Entity·DTO·runtime JSON ↔ DataFrame 입력 데이터 모양 |

비직접 경계는 **8개**(`선행 5 / 교차 3 / 후속 0`)이며 직접 32개에 포함하지 않는다. 지도·텍스트 마이닝의 별도 비직접 경계는 0개이고 해당 책임은 Python 직접 페이지가 소유한다. 탐색 허브·과목 전체 허브·키워드 언급 페이지와 Java 일반 페이지는 중복 또는 책임 불명확으로 제외한다.

## code fence 계획 감사

직접 32페이지 중 fence가 있는 페이지는 4개, fence는 모두 `python` 16개다.

| 페이지 | fence | 선언 text raw의 공백 정규화 연속 일치 | 계획 판정 |
|---|---:|---:|---|
| `concepts/pandas-dataframe-basics.md` | 3 | 1 | 2개 합성·축약 후보 |
| `concepts/pandas-groupby-aggregation.md` | 4 | 0 | 4개 합성·축약 후보 |
| `summaries/2026-07-02-python-pandas-reshape-merge.md` | 3 | 1 | 2개 합성·축약 후보 |
| `summaries/2026-07-03-python-pandas-groupby-visualization.md` | 6 | 1 | 5개 합성·축약 후보 |

- 연속 일치: **3/16**
- 실행 세션 재판정 후보: **13/16**
- `bash` fence: 0
- `shell`이 필요한 Linux/Unix 명령 fence를 새로 만들 때는 `shell`만 사용한다.
- Python code, shell 명령, text output·Traceback, JSON, XML, CSV, HTML을 원문 연속 단위로 구분한다.
- notebook output이나 설명문을 Python source로 과확정하지 않는다.

## 신규 후보 벡터

신규 수는 기존 32개 분류 합계와 분리한다. 실행 세션에서 반복성·독립 탐색 가치·중복 책임을 다시 판정한다.

### Concept 후보

- Python 예외 처리
- Python 정규표현식
- Python XML/JSON 구조화 데이터 처리
- 위 3개는 현재 `python-file-regex-data-processing`의 과도한 책임을 분리할 때만 신설한다.

### Entity 후보

- BeautifulSoup — 현재 Comparison과 Selenium Entity로 검색 책임이 충분한지 먼저 판단

### Comparison 후보

- `loc` vs `iloc`
- `concat` vs `merge` vs `pivot`
- `agg` vs `transform`

### Query 후보

- 현재 실제 사용자 질문·오류→원인→수정→재실행 기록에 근거한 독립 Query는 **0개 유지 후보**다.
- 단순 Traceback 존재만으로 가상의 troubleshooting Query를 만들지 않는다.

## 실제 규모에 맞춘 실행 분할안

현재 32페이지·raw 69개·직접 fence 16개 규모는 한 실행 세션에 고정점까지 끝내기보다 다음 **8개 세션(이번 계획 포함)**으로 나누는 것이 안전하다.

| 세션 | 범위 | 대상 규모 | 핵심 검증 |
|---:|---|---:|---|
| 1 | 이번 재고·계획 | raw 69·직접 32·경계 8 | raw 안정 manifest 재검증과 비동기 감사 정정 뒤 미완료 |
| 2 | Summary 전반 | R01~R07 날짜 Summary 7개 | 기본 문법→XML/JSON/Jupyter 흐름, output/Traceback 경계 |
| 3 | Summary 후반·총정리 | R08~R15 Summary 8개 | Pandas→API/크롤링/지도/텍스트, artifact·결과 경계, fence 9개 |
| 4 | Python core Concept | 기본 문법·collection·함수/module·OOP·file/regex 5개 | S01~S09·A01~A06와 code/output 분리, 신규 Concept 분리 판단 |
| 5 | Pandas·외부 데이터 Concept | DataFrame·groupby·외부 수집·텍스트 마이닝 4개 | D01~D31, SQL/API/UI 경계, fence 7개 |
| 6 | Entity | Python·Pandas·Jupyter·matplotlib·Selenium·Folium·KoNLPy 7개 | 첫 등장·날짜 이력·artifact와 package 설치/사용 구분 |
| 7 | Comparison·Query 최종 판단 | 기존 Comparison 1개+후보 | 신규 비교 억제, 실제 질문 0개 판단, 경계 역링크 |
| 8 | 단계 10 전체 고정점 | 직접 최종 페이지·raw 69·경계 8 | 전체 구조·내용·fence·민감정보·manifest·상위 완료 행 |

한 세션에서 끝내는 안은 raw 69개와 32페이지, 13개 fence 후보, 54개 supplemental raw의 claim-level provenance를 동시에 검증해야 해 실용적이지 않다.

## 이번 계획 세션 검증 결과

- raw 파일 69/69 재고·역할 분류: 완료
- 확장자·bytes·줄·0바이트·중복·manifest: 계산 완료
- 날짜·학습 흐름: R01~R15 실제 파일 기준 대응
- 직접 지식 페이지: 32/32 전수 분류, 유형 합계 일치
- 비동기 전수 감사 정정: `유지 2 / 부분 보강 13 / 전면 재작성 17`, 비직접 경계 8개로 감사 집합 확정
- 직접 source union: 15/69; frontmatter 비채택 54개 모두 역할 분류
- source 실경로·type/directory·index 등록·허용 tag·wikilink·고립·actionable placeholder·빈 sources: 오류 0
- frontmatter/body 출처 동기화: 6페이지 후보를 실행 범위로 명시
- 직접 200줄 초과: 0개 (`pandas-dataframe-basics`는 정확히 200줄)
- 직접 `needs-review`·`confidence: low`: 0개
- direct fence: 16개 중 3개 연속 일치, 13개 재판정 후보; `bash` 0
- 실제 민감 식별값: 이 inventory와 채팅에 재출력하지 않음; 직접 페이지 비출력 패턴 검사에서 후보 0
- actual page count: Meta 생성 전 279; 새 Meta 등록 뒤 **280으로 갱신·실측 일치 확인**
- 시작 raw scoped `git diff --check`: exit 0
- **실패 게이트:** 시작→조사 중 raw manifest가 변경됐고, 최초 Meta의 페이지 분류·경계 수도 비동기 전수 감사와 불일치해 정정함
- 단계 10 전체: 미완료, 상위 `wiki-content-rehighquality-work-plan.md` 완료 행 미추가

## 완료 전 남은 고정점

1. raw가 더 이상 변하지 않는 새 기준선에서 69개 파일·bytes·줄·manifest를 다시 계산한다.
2. 최신 R09를 포함해 직접 32페이지 분류·source union·fence 후보를 다시 계산한다.
3. 시작/종료 scoped status·diff·정렬 SHA-256 manifest가 동일한지 확인한다.
4. 동일하면 이 문서의 상태를 `계획 세션 완료`로 갱신하고 세션 2 Summary 전반 프롬프트를 확정한다.
5. 단계 10 전체 완료 행은 세션 8 전체 고정점 전까지 추가하지 않는다.

## 관련 페이지

- [[_meta/wiki-content-rehighquality-work-plan|LLM Wiki 내용 재고도화 작업 계획]]
- [[_meta/middle-project-rehighquality-inventory-plan|중간 프로젝트 공부 내용 재고도화 전수 재고와 실용형 실행 계획]]
- [[summaries/2026-07-08-python-subject-review|Python 총정리]]
- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
