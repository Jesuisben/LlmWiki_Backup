---
title: 2026-05-20 FilingBox GIGA/MEGA와 WORM 스토리지
created: 2026-07-03
updated: 2026-07-18
type: summary
tags: [auth, linux, project, curriculum]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.20(수)/2026.05.20(수).md
  - raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/NAS_WORM_교육.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/랜섬웨어_교육_박규휘_202605.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/FBG/ITUD_FilingBox GIGA_Hans_On_EN.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/FBM/ITUD_FilingBox MEGA_Hands_On_EN.pdf
status: growing
confidence: high
---

# 2026-05-20 FilingBox GIGA/MEGA와 WORM 스토리지

## 한 줄 요약

강한 로그인 인증만으로는 랜섬웨어 이후의 파일 변조를 막을 수 없다는 경계에서, NAS·WORM과 FilingBox GIGA/MEGA의 사용자·장치·공유 저장소 보호 절차를 배운 날이다.

## 왜 이 순서로 배웠는가

05-19까지는 “누가 접속하는가”와 조직 인증을 다뤘다. 이날은 인증된 계정이나 PC가 침해된 뒤에도 “어떤 데이터를 어떻게 쓰고 바꿀 수 있는가”가 남는다는 문제로 이동했다. 그래서 NAS·WORM·랜섬웨어 개념을 먼저 배우고 저장소와 client를 구성했다.

## 배운 내용

- NAS는 network를 통해 여러 client가 접근하는 저장소이며, browser 기반 cloud drive와 같은 사용 방식으로만 이해하면 안 된다.
- WORM은 기록 후 임의 수정·삭제를 제한해 보존성과 원본성을 높이는 정책이다.
- GIGA에서는 OVA 기반 server, 관리자 계정, group·user, 공유 folder와 RO/RW/AO/WORM mode를 설정했다.
- Windows network drive를 연결하고 개인·공유 folder 접근 절차를 살폈다.
- GIGA 저장 공간 확장 절차에서 disk·partition·LVM·filesystem 계층을 순서대로 다뤘다.
- MEGA에서는 장치 관리자, client 장치 정보, Windows Client 설치처럼 endpoint 관리에 가까운 절차를 배웠다.

## 저장 mode 구분

| mode | 핵심 의미 | 판단 기준 |
|---|---|---|
| RO | 읽기 전용 | 기존 자료를 열람만 시킬 때 |
| RW | 읽기·쓰기 | 일반 협업처럼 수정이 필요할 때 |
| AO | 추가 전용 | 기존 기록을 바꾸지 않고 새 기록만 쌓을 때 |
| WORM | 기록 후 변경 제한 | 보존 기간과 원본성 요구가 있을 때 |

## 직접 보존된 결과와 미보존 결과

원본에는 OVA import, server IP 확인, 관리자 화면 접근, 계정·group·공유 folder·mode 입력, network drive 연결, 용량 확장 명령, MEGA client 설치 순서가 보존돼 있다. 그러나 각 folder mode의 실제 쓰기·수정·삭제 거부 결과, network drive 화면, LVM 확장 전후 용량 출력, MEGA client 연결 성공을 독립 결과로 보여주는 response나 screenshot은 없다.

교육 PDF는 제품별 hands-on 절차와 개념을 보조한다. 교육자료의 화면을 사용자의 실제 환경 성공 증거로 계산하지 않는다.

## 헷갈린 점 / 질문

- WORM은 처음부터 아무것도 쓸 수 없는 RO와 다르다. 핵심은 기록 이후 변경을 제한하는 보존 정책이다.
- storage mode는 사용자 인증이 성공했는지가 아니라 인증 이후 허용할 data operation을 결정한다.
- GIGA/MEGA는 X1280 Auth Server의 하위 server가 아니다. 같은 보안 과목에서 data 보호를 다룬 별도 제품군이다.
- LVM 명령을 실행했다는 사실과 실제 filesystem 용량 증가 확인은 다른 완료 조건이다.

## 이전·다음 연결

- 이전: [[summaries/2026-05-19-aam-ape-authentication-filingbox|05-19 AAM/APE]]의 조직 사용자·인증기 관리.
- 다음: [[summaries/2026-05-21-passwordless-x1280-rest-api|05-21 X1280 REST API]]에서 다시 인증 서버의 요청·응답 검증으로 돌아간다.
- 선행 기반: [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]과 [[concepts/linux-cli-files|Linux CLI와 파일 시스템]].

## 관련 페이지

- [[concepts/nas-worm-storage-protection|NAS·WORM 저장소 보호]]
- [[comparisons/authentication-vs-authorization|인증(Authentication) vs 인가(Authorization)]]
- [[summaries/2026-05-21-passwordless-subject-review|Passwordless 총정리]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.20(수)/2026.05.20(수).md`
- `raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/NAS_WORM_교육.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/랜섬웨어_교육_박규휘_202605.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/FBG/ITUD_FilingBox GIGA_Hans_On_EN.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/FBM/ITUD_FilingBox MEGA_Hands_On_EN.pdf`