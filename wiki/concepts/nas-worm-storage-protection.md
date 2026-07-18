---
title: NAS·WORM 저장소 보호
created: 2026-07-13
updated: 2026-07-18
type: concept
tags: [auth, linux, project]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.20(수)/2026.05.20(수).md
  - raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/NAS_WORM_교육.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/랜섬웨어_교육_박규휘_202605.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/FBG/ITUD_FilingBox GIGA_Hans_On_EN.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/FBM/ITUD_FilingBox MEGA_Hands_On_EN.pdf
status: growing
confidence: high
---

# NAS·WORM 저장소 보호

## 정의

NAS(Network Attached Storage)는 network를 통해 여러 client가 접근하는 저장소다. WORM(Write Once Read Many)은 기록한 data의 이후 변경·삭제를 제한해 보존성과 원본성을 높이는 정책이다.

## 왜 중요한가

Passwordless는 계정 인증 공격면을 줄이지만, 인증된 PC나 account가 침해된 뒤 file이 암호화·삭제되는 문제까지 자동 해결하지 않는다. 05-20 수업은 “누구인가”를 확인하는 인증과 “기록을 어떻게 보존하는가”를 담당하는 storage protection을 분리했다.

## mode별 판단 기준

| mode | 허용 의도 | 적합한 상황 | 주의할 오해 |
|---|---|---|---|
| RO | 읽기 | 배포된 기준 문서 열람 | 새 기록 추가도 제한될 수 있음 |
| RW | 읽기·쓰기 | 일반 협업 | ransomware가 가진 write 권한도 위험 |
| AO | 기존 기록 유지 + 추가 | append 중심 log·기록 | WORM과 보존 규칙이 동일하다고 단정하지 않음 |
| WORM | 기록 후 변경 제한 | 규정·원본 보존 | 단순 folder read-only와 같은 뜻이 아님 |

## 수업 예시

FilingBox GIGA에서는 OVA server를 준비하고 관리자·user·group·공유 folder·mode를 설정한 뒤 Windows network drive와 용량 확장 절차를 살폈다. MEGA에서는 장치 정보 등록과 Windows Client 설치를 다뤘다. 날짜 원본에는 설정·명령 순서가 있지만 mode별 실제 write/delete 거부, network drive 화면, 용량 전후 출력, client 최종 연결 결과는 독립 증거로 보존돼 있지 않다.

교육 PDF는 개념과 hands-on 화면을 제공하는 보조 입력이다. 교육 화면을 사용자 환경의 실행 결과로 바꾸지 않는다.

## 구성요소 책임

- **인증:** 사용자가 누구인지 확인한다.
- **인가·group:** 어떤 공유 folder에 접근할 수 있는지 판단한다.
- **storage mode:** 접근 후 read/write/append/변경 제한을 결정한다.
- **volume/filesystem:** 실제 용량과 file 저장을 담당한다.
- **backup·복구:** WORM과 별도 운영 책임이며 05-20 설정만으로 완료됐다고 보지 않는다.

## 자주 헷갈리는 점

- WORM과 RO는 목적과 기록 가능 시점이 다르다.
- NAS는 network 위치이고 WORM은 변경 통제 정책이므로 같은 분류의 대체재가 아니다.
- passwordless 인증이 성공해도 RW 권한을 가진 client의 ransomware 위험은 남는다.
- partition·LVM·filesystem 명령을 모두 실행해야 실제 용량 확장이 끝나며, 마지막 용량 확인이 완료 조건이다.

## 선행·후속 연결

- 선행: [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]과 [[summaries/2026-05-19-aam-ape-authentication-filingbox|AAM/APE 조직 인증 관리]].
- 직접 수업: [[summaries/2026-05-20-filingbox-giga-mega|FilingBox GIGA/MEGA와 WORM]].
- 연결: [[comparisons/authentication-vs-authorization|인증 vs 인가]]와 함께 보면 사용자 확인·접근 허용·storage operation 세 층을 구분할 수 있다.

## 관련 개념

- [[entities/passwordless-x1280|Passwordless X1280]]
- [[entities/aam-ape|AAM과 APE]]
- [[summaries/2026-05-21-passwordless-subject-review|Passwordless 총정리]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.20(수)/2026.05.20(수).md`
- `raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/NAS_WORM_교육.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/랜섬웨어_교육_박규휘_202605.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/FBG/ITUD_FilingBox GIGA_Hans_On_EN.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/FBM/ITUD_FilingBox MEGA_Hands_On_EN.pdf`