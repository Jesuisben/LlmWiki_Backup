---
title: 집 노트북에 LLM Wiki와 Hermes Agent 환경 복제하기
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
# 집 노트북에 LLM Wiki와 Hermes Agent 환경 복제하기

## 목적

현재 학원 PC의 Obsidian LLM Wiki와 Hermes Agent 환경을 집 노트북에서도 최대한 비슷하게 사용할 수 있도록 복제 절차를 정리한 허브 문서다.

## 전체 구조 이해

이전 작업은 크게 세 덩어리로 나뉜다.

1. Git/GitHub/Obsidian으로 Vault를 옮긴다.
2. Hermes 로컬 설정 중 인증 파일을 제외한 핵심 설정을 옮긴다.
3. 집 노트북에서 경로, 인증, memory/skills, Git push를 확인한다.

## 분리된 세부 가이드

- [[_meta/hermes-home-laptop-git-obsidian-setup|집 노트북 Git/Obsidian 설정]] — 현재 PC push, 집 노트북 clone, Obsidian Vault 열기, Git 사용자 정보 확인
- [[_meta/hermes-home-laptop-hermes-config-migration|집 노트북 Hermes 설정 마이그레이션]] — Hermes AppData 백업/복사, 인증 파일 제외, `config.yaml` 경로 수정, memory/skills 확인
- [[_meta/hermes-home-laptop-troubleshooting|집 노트북 Hermes 이전 문제 해결]] — D드라이브 경로 오류, Git push 오류, memory/테마 문제, 최종 체크리스트

## 핵심 보안 원칙

`.env`, `auth.json`, provider/API key/OAuth token 같은 인증 파일은 그대로 복사하지 않는다. 집 노트북에서는 Hermes를 설치한 뒤 OpenAI OAuth나 필요한 provider 인증을 새로 연결하는 방식이 안전하다.

## 한 줄 요약

Vault는 GitHub로 옮기고, Hermes 설정은 인증 파일을 제외해 복사한 뒤, 집 노트북 경로와 인증을 새로 맞춘다.

## 관련 페이지

- [[_meta/llm-wiki-operating-model|LLM Wiki 운영 모델]]
- [[_meta/hermes-default-profile-mode-system|Hermes default 프로필 모드 시스템]]
- [[_meta/hermes-home-laptop-git-obsidian-setup|집 노트북 Git/Obsidian 설정]]
- [[_meta/hermes-home-laptop-hermes-config-migration|집 노트북 Hermes 설정 마이그레이션]]
- [[_meta/hermes-home-laptop-troubleshooting|집 노트북 Hermes 이전 문제 해결]]

## 출처

- `AGENTS.md`
- `wiki/index.md`
- `wiki/log.md`
- `wiki/_meta/hermes-default-profile-mode-system.md`
