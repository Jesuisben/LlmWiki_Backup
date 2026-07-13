---
title: NAS·WORM 저장소 보호
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [auth, linux, project]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.20(수)/2026.05.20(수).md
status: growing
confidence: high
---

# NAS·WORM 저장소 보호

## 정의

NAS(Network Attached Storage)는 네트워크를 통해 여러 장치가 접근하는 저장소다. WORM(Write Once Read Many)은 기록한 데이터를 이후 읽기 중심으로 보존해 임의 변경을 어렵게 만드는 저장 방식이다.

## 왜 중요한가

Passwordless 인증은 계정 탈취 가능성을 낮추는 인증 계층이다. 하지만 인증만으로 랜섬웨어 이후의 데이터 변조·암호화를 막을 수는 없다. 2026-05-20 수업은 NAS·WORM·FilingBox를 통해 데이터 보존과 접근 제어를 별도의 저장소 보호 계층으로 다뤘다.

## 핵심 설명

FilingBox GIGA 실습에서는 VM으로 서버를 준비한 뒤 관리자, 사용자, 그룹, 공유 폴더를 만들고 폴더 모드를 설정했다. Windows 네트워크 드라이브로 개인·공유 폴더에 접속하고, 필요하면 LVM과 파일시스템 확장으로 용량 변경도 확인했다.

| 모드 | 의미 | 수업 맥락 |
|---|---|---|
| RO | Read Only | 원본·규정 자료 열람 |
| RW | Read Write | 일반 협업 폴더 |
| AO | Append Only | 기존 기록을 바꾸지 않고 새 기록 추가 |
| WORM | Write Once Read Many | 변경 방지가 필요한 보존 데이터 |

FilingBox MEGA 실습은 장치 관리자, MAC/IP 등록, Windows Client 연결처럼 장치 관리 관점이 더 강했다.

## 자주 헷갈리는 점

- WORM은 단순히 읽기만 가능한 RO와 완전히 같은 개념이 아니다. 기록 뒤 변경을 제한해 원본 보존을 지원하는 정책이다.
- NAS/WORM은 X1280 Auth Server의 구성 요소가 아니다. 같은 과목 안에서 인증 이후 데이터 보호를 연결해 본 별도 보안 계층이다.
- 권한 설정과 저장 모드는 인증 성공 여부가 아니라 인증 이후 데이터에 어떤 변경을 허용할지 결정하는 문제다.

## 관련 개념

- [[summaries/2026-05-20-filingbox-giga-mega|2026-05-20 FilingBox GIGA/MEGA와 WORM 스토리지]]
- [[summaries/2026-05-19-aam-ape-authentication-filingbox|2026-05-19 인증 기본과 AAM/APE 통합 설치]]
- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[comparisons/authentication-vs-authorization|인증(Authentication) vs 인가(Authorization)]]
- [[entities/passwordless-x1280|Passwordless X1280]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.20(수)/2026.05.20(수).md`
