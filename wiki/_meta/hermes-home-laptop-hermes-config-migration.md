---
title: 집 노트북 Hermes 설정 마이그레이션
created: 2026-07-02
updated: 2026-07-02
type: meta
tags: [study-log]
sources:
  - AGENTS.md
  - wiki/index.md
  - wiki/log.md
  - wiki/_meta/hermes-default-profile-mode-system.md
status: growing
confidence: high
---
# 집 노트북 Hermes 설정 마이그레이션

## 목적

집 노트북에서 현재 Hermes Agent 설정을 최대한 이어 쓰기 위한 마이그레이션 허브다. 보안상 인증 파일은 그대로 복사하지 않고, 설정·기억·스킬·프로젝트 정보 중심으로 옮긴다.

## 분리된 세부 가이드

- [[_meta/hermes-home-laptop-hermes-backup-security|집 노트북 Hermes 백업과 보안 원칙]] — 백업 대상, 제외할 인증 파일, Desktop UI 설정 선택 백업
- [[_meta/hermes-home-laptop-hermes-copy-verify|집 노트북 Hermes 설정 복사와 검증]] — AppData 복사, `config.yaml` 경로 수정, 실행 후 memory/skills 확인
- [[_meta/hermes-home-laptop-troubleshooting|집 노트북 Hermes 이전 문제 해결]] — 경로, Git, memory, theme 문제 해결

## 핵심 원칙

- `.env`, `auth.json`, OAuth token, provider key는 그대로 복사하지 않는다.
- `config.yaml` 안의 `cwd` 같은 작업 폴더 경로는 집 노트북 실제 경로에 맞게 수정한다.
- Hermes를 완전히 종료한 뒤 설정 파일을 복사한다.
- 복사 후에는 Hermes 실행, 현재 작업 폴더, memory/skills 반영 여부를 확인한다.

## 관련 페이지

- [[_meta/hermes-home-laptop-setup|집 노트북에 LLM Wiki와 Hermes Agent 환경 복제하기]]
- [[_meta/hermes-home-laptop-hermes-backup-security|집 노트북 Hermes 백업과 보안 원칙]]
- [[_meta/hermes-home-laptop-hermes-copy-verify|집 노트북 Hermes 설정 복사와 검증]]
- [[_meta/hermes-default-profile-mode-system|Hermes default 프로필 모드 시스템]]

## 출처

- `AGENTS.md`
- `wiki/index.md`
- `wiki/log.md`
- `wiki/_meta/hermes-default-profile-mode-system.md`
