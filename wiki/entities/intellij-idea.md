---
title: IntelliJ IDEA
created: 2026-07-02
updated: 2026-07-16
type: entity
tags: [java, spring]
sources:
  - raw/KoreaICT/1. Java/2026.02.26(목) - 시작/2026.02.26(목) - 시작.md
  - raw/KoreaICT/1. Java/2026.02.27(금)/깃허브 초기 설정.md
  - raw/KoreaICT/1. Java/교육 자료/IntelliJ 교안.pdf
  - raw/KoreaICT/1. Java/교육 자료/Github 교안(실습).pdf
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md
status: stable
confidence: high
---

# IntelliJ IDEA

## 무엇인가

IntelliJ IDEA는 Java source와 project 구조를 편집하고 실행 구성을 다루는 IDE다. 이 위키에서는 Java 첫 project부터 Spring Boot backend의 Java·properties·Controller·Entity·Repository·Service를 작성하고 실행한 작업 환경이다.

## 왜 중요한가

사용자는 Java 문법을 처음 배울 때 project→package→class→`main` 구조를 IntelliJ에서 직접 만들었다. FrontEnd_BackEnd에서는 Spring Initializr가 생성한 Maven project를 같은 IDE로 열어 backend source·설정·application 실행을 관리했다. 따라서 언어 학습과 framework project가 이어지는 작업 환경이지만, Java·JVM·Maven·Spring Boot 기능 자체와는 구분해야 한다.

## 이 위키에서의 맥락

2026-02-26 첫 Java 수업에서 설치·설정하고 `MyJava` project를 만든 뒤 package, class, `main`, Run으로 첫 출력을 확인했다. 03-30에는 IntelliJ 동작을 먼저 확인하고 Spring Initializr의 `spring_cafe` folder를 열어 JDK 21과 project 구조를 맞춘 다음 `CoffeeApplication`을 실행했다. 03-31 이후 Controller와 template, 04-02~03에는 Member Entity·Repository·Service·Controller를 작성했다.

## 대표 artifact와 입력 → 처리 → 결과

| 시기 | 대표 artifact | 입력 | IDE에서 한 작업 | 확인된 결과 |
|---|---|---|---|---|
| 02-26 | `MyJava`, package, `MyPrint`·`YourPrint` | project·package·class 생성 | Java source 편집 후 Run | `hello`, `world`, 이름 출력 확인 |
| 02-27 | `MyJava` Git repository | local source와 remote 설정 | VCS/Git 메뉴에서 연동 준비 | commit·push·pull 학습으로 연결 |
| 03-30 | `spring_cafe`, `CoffeeApplication`, properties | Spring Initializr zip을 푼 folder | Open, JDK 21 설정, Java/properties/static file 편집·application 실행 | 9000번 정적 home 확인 |
| 03-31 | `FruitHtmlController`, `FruitController`, template | GET 요청 처리 코드 | Controller·template 작성과 backend 실행 | Thymeleaf HTML과 JSON 확인 |
| 04-02~03 | `Member`, Repository·Service·Controller | 회원 field·Validation·요청 처리 | Java class/enum/interface 작성과 test/application 실행 | MySQL row·회원가입 응답 흐름 확인 |

## 확인된 범위와 미확정 범위

- 확인됨: project/folder open, package·class·enum/interface 작성, Java·properties·HTML 편집, JDK 21 설정, Run, 자동 import, Git 연동, 자동 build·annotation processing·Lombok plugin 설정.
- 확인됨: Spring Boot 정적 page·Fruit HTML/JSON·Member 저장 결과는 IntelliJ에서 작성·실행한 project의 결과다.
- 미확정: 03-30에 Spring Initializr dependency를 선택했다는 사실만으로 H2·Spring Web Services가 실제 기능에 사용됐다고 보지 않는다.
- 구분: IntelliJ가 Java를 실행하는 것이 아니라 JDK/JVM이 Java program을 실행하고, Maven이 dependency/build를 관리하며, Spring Boot가 application runtime과 framework 기능을 제공한다.

## 학습 이력

- [[summaries/2026-02-26-orientation|2026-02-26]]: IntelliJ 설치, 테마/글꼴 설정, 첫 출력 실습
- [[summaries/2026-02-27-github-initial-setup|2026-02-27]]: Git과 IntelliJ 연동
- [[summaries/2026-03-30-fullstack-environment-setup|2026-03-30]]: Spring Boot project open·JDK 21·properties·application 실행
- [[summaries/2026-03-31-spring-boot-controller-html|2026-03-31]]: Fruit Controller와 template·REST JSON 작성
- [[summaries/2026-04-02-react-bootstrap-homepage|2026-04-02]]~[[summaries/2026-04-03-spring-member-seed-react-comments|04-03]]: Member Entity·Validation·Security·Repository·Service·Controller 작성과 test

## 자주 헷갈리는 원인

- **IDE와 Java/JVM:** IntelliJ는 source 작성과 실행 요청을 돕는 환경이다. Java 문법과 JVM 실행 원리를 IDE 기능으로 설명하지 않는다.
- **IDE와 Maven:** `pom.xml`을 editor에서 수정해도 dependency 해석·build 책임은 Maven에 있다.
- **IDE와 Spring Boot:** Controller, JPA, Security, dependency injection은 Spring/Spring Boot 기능이다. IntelliJ는 해당 code를 작성하고 application을 실행한 환경이다.
- **설치와 실행:** project를 Open한 시점, JDK를 맞춘 시점, `CoffeeApplication`을 실행해 browser 결과를 확인한 시점을 한 단계로 합치지 않는다.

## 교안·후속 과목 경계

- P02 `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/IntelliJ 교안.pdf`는 `raw/KoreaICT/1. Java/교육 자료/IntelliJ 교안.pdf`와 byte-identical하다. Java 단계에서 이미 직접 사용한 동일 교안이므로 FrontEnd_BackEnd source로 중복 선언하거나 새 사실을 만들지 않았다.
- SpringBoot 교안의 필요한 project 절차는 03-30 날짜 MD에 전사되어 있어 PDF-only 주장 없이 날짜 raw를 우선했다.
- Linux에서는 IDE 밖 shell에서 Maven·jar를 실행하고, AWS/CI/CD에서는 cloud·workflow가 build/deploy를 담당한다. 이는 IntelliJ 기능의 확장이 아니라 실행 환경의 전환이다.
- Passwordless·중간 프로젝트에서도 Java/Spring source를 IntelliJ로 편집할 수 있지만 인증 제품·pipeline·server runtime을 IDE 기능으로 설명하지 않는다.

## 관련 개념

- [[entities/java|Java]]
- [[entities/git|Git]]
- [[entities/github|GitHub]]
- [[entities/spring-boot|Spring Boot]]
- [[entities/maven|Maven]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]

## 출처

- `raw/KoreaICT/1. Java/2026.02.26(목) - 시작/2026.02.26(목) - 시작.md`
- `raw/KoreaICT/1. Java/2026.02.27(금)/깃허브 초기 설정.md`
- `raw/KoreaICT/1. Java/교육 자료/IntelliJ 교안.pdf`
- `raw/KoreaICT/1. Java/교육 자료/Github 교안(실습).pdf`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md`
