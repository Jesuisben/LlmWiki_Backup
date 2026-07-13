---
title: 2026-05-20 FilingBox GIGA/MEGA와 WORM 스토리지
created: 2026-07-03
updated: 2026-07-13
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

랜섬웨어 대응 관점에서 NAS, WORM, 읽기전용/추가전용/읽기쓰기 폴더 모드를 배우고, FilingBox GIGA/MEGA를 VM으로 구성해 네트워크 드라이브와 저장소 보호 흐름을 실습한 날이다.

## 배운 내용

- NAS는 네트워크를 통해 접근하는 저장 공간이며, 일반 클라우드 웹하드와는 운영·보호 관점이 다르다.
- WORM(Write Once Read Many)은 한 번 기록한 뒤 임의 수정/삭제를 제한해 원본성과 보존성을 높이는 방식이다.
- 랜섬웨어는 파일을 암호화해 사용할 수 없게 만들고 금전을 요구하므로, 저장소 모드와 접근 권한 설계가 중요하다.
- FilingBox GIGA 실습에서는 관리자 계정, 사용자, 그룹, 공유 폴더, 폴더 모드(RO/RW/AO/WORM)를 설정했다.
- MEGA 실습에서는 장치 관리자, MAC/IP 등록, Windows Client 설치처럼 endpoint/장치 관리에 가까운 흐름을 다뤘다.

## 핵심 개념

- [[concepts/nas-worm-storage-protection|NAS·WORM 저장소 보호]]
- [[summaries/2026-05-19-aam-ape-authentication-filingbox|2026-05-19 인증 기본과 AAM/APE 통합 설치]]
- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]

## 실습 / 예제

```text
FilingBox GIGA OVA import
→ 서버 IP 확인 및 관리자 페이지 접속
→ 라이선스 적용
→ 관리자 계정/사용자/그룹 생성
→ 공유 폴더와 모드 설정
→ Windows 네트워크 드라이브 연결
→ 용량 확장 시 LVM/파일시스템 확장 확인
```

GIGA 실습은 사용자·그룹·공유 폴더와 RO/RW/AO/WORM 모드를 설정한 뒤 Windows 네트워크 드라이브로 접근하는 흐름이었다. MEGA는 장치 관리자, MAC/IP 등록, Windows Client 연결을 중심으로 다뤘다. 두 제품을 X1280 인증 서버의 구성 요소로 쓰지 않고, 인증 이후의 데이터 보존·접근 제어 계층으로 구분한다.

## 헷갈린 점 / 질문

- WORM은 단순 “읽기전용”과 다르다. 이미 기록된 데이터의 변경 가능성을 줄이는 보존 정책에 가깝다.
- RO/RW/AO/WORM 같은 모드는 인증 자체보다 인증 이후의 권한·저장소 보호 정책에 가깝다.
- 이 날짜의 내용은 Passwordless 로그인 구현보다는 보안 제품군과 랜섬웨어 대응 저장소 보호 관점으로 연결된다.

## 관련 페이지

- [[summaries/2026-05-14-passwordless-x1280-intro|2026-05-14 Passwordless X1280 소개와 보안 배경]]
- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]
- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.20(수)/2026.05.20(수).md`
- `raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/NAS_WORM_교육.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/랜섬웨어_교육_박규휘_202605.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/FBG/ITUD_FilingBox GIGA_Hans_On_EN.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/FBM/ITUD_FilingBox MEGA_Hands_On_EN.pdf`
