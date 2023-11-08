# 04 Single-File components

# Single-File components

## Component

재사용 가능한 코드 블록

### Component 특징

- UI를 독립적이고 재사용 가능한 일부분으로 분할하고 각 부분을 개별적으로 다룰 수 잇음
- 그러면 자연스럽게 앱은 중첩된 Component의 트리로 구성됨

![Alt text](images/image.png)

### Component 예시

웹 서비스는 여러 개의 Component로 이루어져 잇음

![Alt text](images/image-1.png)

## SFC

### Single-File Components (SFC)

컴포넌트의 템플릿, 로직 및 스타일을 하나의 파일로 묶어낸 특수한 파일 형식(.vue 파일)

- 하나의 파일에 하나의 앱 !

### SFC 파일 예시

- Vue SFC는 HTML, CSS 및 JavaScript 3개를 하나로 합친 것
- template, script 및 style 블록은 하나의 파일에서 컴포넌트의 뷰 로직 및 스타일을 캡슐화하고 배치

![Alt text](images/image-2.png)

- 이제 자동완성도 쓸 수 있음
- vbase 이후 3-setup 선택 후 lang="scss" 삭제해주기

### SFC 문법

- 각 .vue 파일을 세 가지 유형의 최상위 언어 블록 template, script, style으로 구성됨
- 언어 블록의 작성 순서는 상과없으나 일반적으로 template -> script -> style 순서로 작성

### 언어 블록 - template

- 각 vue 파일은 최상위 template 블록을 하나만 포함할 수 잇음

![Alt text](images/image-3.png)

### 언어 블록 - script setup

- 각 vue 파일은 하나의 script setup 블록만 포함할 수 있음 (일반 script 제외)
- 컴포넌트의 setup() 함수로 사요되면 컴포넌트의 각 인스턴스에 대해 실행

![Alt text](images/image-4.png)

### 언어 블록 - style scope

- vue 파일에는 여러 style 태그가 포함될 수 있음
- scoped가 지정되면 CSS는 현재 컴포넌트에만 적용

![Alt text](images/image-5.png)

### 컴포넌트 사용하기

[https://play.vuejs.org/](https://play.vuejs.org/) 에서 Vue 컴포넌트 코드 작성 및 미리보기

- VueSFC는 컴파일러르 통해 컴파일 된 후 빌드 되어야 함
- 실제 프로젝트에서는 일반적으로 SFC 컴파일러를 Vite와 같은 공식 빌드 도구를 사용해 사용

# SFC build tool (Vite)

## Vite

프론트엔드 개발 도구

- 빠른 개발 환경을 위한 빌드 도구와 개발 서버를 제공

### Vite 튜토리얼

- vite 프로젝트 생성
- 수업에서는 위에 코드로 작성함

```bash
npm init vue@latest
npm create vue@latest
```

- 프로젝트 설정 관련 절차 진행
- 전부 No로 밀기

![Alt text](images/image-6.png)  
![Alt text](images/image-10.png)

- 프로젝트 폴더 이동 및 패기지 설치

![Alt text](images/image-7.png)

- Vue 프로젝트 서버 실행

![Alt text](images/image-8.png)

- Vue 프로젝트 실행 결과

![Alt text](images/image-9.png)

## NPM : Node Package Manager

Node.js의 기본 패키기 관리자

![Alt text](images/image-11.png)

- Chrom의 V8 JavaScripy 엔진을 기반으로 하는 Server-Side 실행 환경

### Node.js의 영향

- 기존의 브라우저 안에서만 동작할 수 있었던 JavaScript를 브라우저가 아닌 서버 측에서도 실행할 수 있게 함
  - 프로튼엔드와 백엔드에서 동일한 언어로 개발할 수 있게됨
- NPM을 활용해 수많은 오픈 소스 패키지와 라이브러리를 제공하여 개발자들이 손쉽게 코드를 공유하고 재사용할 수 있게 함

## Vite 프로젝트 구조

### Node_modules

- Node.js 프로젝트에서 사용되는 외부 패키지들이 저장되는 디렉퇼
- 프로젝트의 의존성 모듈을 저장하고 관리하는 공간
- 프로젝트가 실행될 때 필요한 라이브러리와 패키지들을 포함
- .gitignore에 작성됨

![Alt text](images/image-12.png)

### package-lock.json

- 패키지들의 실제 설치 버전, 의존성 관계, 하위 패키지 등을 포함하여 패키지 설치에 필요한 모든 정보를 포함
- 패키지들의 정확한 버전을 보장하여, 여러 개발자가 협업하거나 서버 환경에서 일관성 있는 의존성을 유지하는 데 도움을 줌
- npm install 명령을 통해 채키지를 설치할 때, 명시된 버전과 의존성을 기반으로 설치

![Alt text](images/image-13.png)

### package.json

- 프로젝트의 메타 정보와 의존성 패키지 목록을 포함
- 프로젝트의 이름, 버전, 작성자, 라이선스 등과 같은 메타 정보를 정의
- package-lock.json과 함게 프로젝트의 의존성을 관리하고, 버전 충돌 및 일관성을 유지하는 역할

![Alt text](images/image-14.png)

### Public 디렉토리

- 주로 다음 정적 파일을 위치 시킴
  - 소스코드에서 참조되지 않는
  - 항상 같은 이름을 갖는
  - import 할 필요 없는
- 항상 root 절대 경로를 사용하여 참조
- puclic/icon.png는 소스 코드에서 /icon.png로 참조할 수 있음

### src 디렉토리

- 프로젝트의 주요 소스 코드를 퐘하는 곳
- 컴포넌트, 스타일, 라우팅 등 프로젝트의 핵심 코드를 관리

### src/assets

- 프로젝트 내에서 사용되는 자원 (이미지, 폰트, 스타일 시트 등)을 관리
- 컴포넌트 자체에서 참조하는 내부 파일을 저장하는데 사용
- 컴포넌트가 아닌 곳에서는 public 디렉토리에 위치한 파일을 사용

![Alt text](images/image-15.png)

### src/somponents

- vue 컴포넌트들을 작성하는 곳

![Alt text](images/image-16.png)

### src/App.vue

- Vue 앱의 최상위 Root 컴포넌트
- 다른 하위 컴포넌트들을 포함
- 에플리케이션 전체의 레이아웃과 공통적인 요소를 정의

![Alt text](images/image-17.png)  
![Alt text](images/image-18.png)

### src/main.js

- Vue 인스턴스를 생성하고, 애플리케이션을 초기화하는 역할
- 필요한 라이브러리를 import 하고 전역 설저을 수행

![Alt text](images/image-19.png)

### index.html

- vue 앱의 기본 HTML 파일
- 앱의 진입점 (entry point)
- Root 컴포넌트인 App.vue가 해당 페이지에 마운트(mount)됨
  - vue 앱이 SPA인 이유
- 필요한 스타일 시트, 스크립트 등의 외부 리소스를 로드할 수 있음 ex.booststrap CDN

## 모듈과 번들러

### Module

프로그램을 구성하는 독립적인 코드 블록 (.js 파일)

- 개발하는 애플리케이션의 크기가 커지고 복잡해지면서 파일 하나에 모든 기능을 담기가 어려워짐
- 따라서 자연스럽게 파일을 여러 개로 분리하여 관리를 하게 되었고, 이때 분리된 파일 각각이 모듈(module) 즉, js 파일 하나가 하나의 모듈
- 모듈의 수가 많아지고 라이브러리 혹은 모듈 간의 의존성(연결성)이 깊어지면서 특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악하기 어려워짐
- 복잡하고 깊은 모듈의 의존성 문제를 해결하기 위한 도구가 필요 : Bundler

### node_modules의 의존성 깊이

![Alt text](images/image-20.png)

### Bundler

여러 모듈과 파일을 하나(혹은 여러 개)의 번들로 묶어 최적화하여 애플리케이션에서 사용할 수 있게 만들어주는 도구

### Bundelr의 역할

- 의존성 관리, 코드 최적화 관리, 리소스 관리 등
- Bundler가 하는 작업을 Bunding이라 함
- Vite는 Rollup이라는 Bundler를 사용하며 개발자가 별도로 기타 환결설정에 신경 쓰지 않도록 모두 설정해두고 있음

# Vue Component

## Component

### 컴포넌트 사용 2단계

1. 컴포넌트 파일 생성
2. 컴포넌트 등록(import)

### 사전 준비

1. 초기에 생성된 모든 컴포넌트 삭제(App.vue 제외)
2. App.vue 코드 초기화

![Alt text](images/image-22.png)

![Alt text](images/image-21.png)

1. 컴포넌트 파일 생성

- MyComponent.vue 생성

![Alt text](images/image-23.png)

2. 컴포넌트 등록

- App 컴포넌트에 MyComponent를 등록

![Alt text](images/image-24.png)

- App(부모) - MyComponent(자식) 관계 형성
- @-'src/' 경로를 뜻하는 약어

![Alt text](images/image-25.png)

3. 결과 확인

- Vue dev tools를 사용해 컴포넌트 관계 형성 확인

![Alt text](images/image-26.png)

### MyComponentItem 컴포넌트 등록 후 활용

- MyComponentItem는 MyComponent의 자식 컴포넌트

![Alt text](images/image-27.png)

- 컴포넌트의 재사용성 확인

![Alt text](images/image-28.png)

# 추가 주제

## Virtual DOM

- 가상의 DOM을 메모리에 저장하고 실제 DOM과 동기화하는 프로그래밍 개념
- 실제 DOM과 변경 사항 비교를 통해 변경된 부분만 실제 DOM에 적용하는 방식
- 웹 애플리케이션의 성능을 향상시키기 위한 Vue의 내부 렌더링 기술

![Alt text](images/image-29.png)

### 내부 렌더링 과정

![Alt text](images/image-30.png)

### Virtual DOM 패턴의 장점

효율성

- 실제 DOM 조작을 최소화하고, 변경된 부분만 업데이트하여 성능을 향상

반응성

- 데이터의 변경을 감지하고, Virtual DOM을 효율적으로 갱신하여 UI를 자동으로 업데이트

추상화

- 개발자는 실제 DOM 조작을 Vue에세 맡기고 컴포넌트와 템플릿을 활용하는 추상화된 프로그래밍 방식으로 원하는 UI 구조를 구성하고 관리할 수 잇음

### Virtual DOM 주의사항

- 실제 DOM에 직접 접근하지 말 것
  - JavaScript에서 사용하는 DOM 접근 관련 메서드 사용 금지
  - querySelector, createElemen, addEvenetListener 등
- Vue와 ref와 Lifecycle Hooks 함수를 사용해 간접적으로 접근하여 조작할 것

### 직접 DOM 엘리먼트에 접근해야 하는 경우

- ref 속성을 사용하여 특정 DOM 엘리먼트에 직접적인 참조를 얻을 수 있음

![Alt text](images/image-31.png)

## Composition API & Option API : 2가지 API 스타일

### Composition API

- import해서 가져온 API 함수들을 사용하여 컴포넌트의 로직을 정의
- Vue3에서의 권장 방식

![Alt text](images/image-32.png)

### Option API

- data, methods 및 mointed 같은 객체를 사용하여 컴포넌트의 로직을 정의
- Vue2 에서의 작성 방식

![Alt text](images/image-33.png)

### API 별 권장 사항

- Composition API + SFC
  - 규모가 있는 앱의 전체를 구축하려는 경우
- Option API
  - 빌드 도구를 사용하지 않거나 복잡성이 낮은 프로젝트에서 사용하려는 경우

# 참고

### Scaffoding(스캐폴딩)

- 새로운 프로젝트나 모듈을 시작하기 위해 초기 구조와 기본 코드를 자동으로 생성하는 과정
- 개발자들이 프로젝트를 시작하는 데 도움을 주는 틀이나 기반을 제공하는 작업
- 초기 설정, 폴더 구조, 파일 템플릿, 기본 코드 등을 자동으로 생성하여 개발자가 시작할 때 시간과 노력을 절약하고 일관된 구조를 유지할 수 있도록 도와줌

### SFC의 CSS 기능 - scoped

![Alt text](images/image-34.png)

- scoped를 사용하면 부모 컴포넌트의 스타일이 자식 컴포넌트로 유출되지 않음
- 단, 자식 컴포넌트의 최상위 요소(root element)는 부모와 자식의 CSS 모두의 영향을 받음
- 부모가 레이아웃 목적으로 자식 컴포넌트 최상위 요소의 스타일을 지정할 수 있도록 의도적으로 설계 된 것

### SFC의 CSS 기능 - scoped 예시

- 다음과 같이 App(부모) 컴포넌트에 적용한 스타일을 scoped가 작성되어 있지만, MyComponent(자식)의 최상위 요소는 부모와 본인의 CSS 모두의 영향을 받기 때문에 부모의 스타일이 적용됨 -> 태그로 지정시에

![Alt text](images/image-35.png)

### 모든 컴포넌트에는 최상단 HTML 요소가 작성되는 것이 권장

- 가독성, 스타일링, 명확환 컴포넌트 구조를 위해 각 컴포넌트에는 최상단 HTML 요소를 작성해야 함(Single Root Element)

![Alt text](images/image-36.png)

![Alt text](images/image-37.png)

웹팩(Webpack)이란 모듈 번들러의 일종으로 프론트엔드 개발을 할 때 여러 파일들을 모듈로서 관리를 하고 이를 하나의 번들(bundle)로 묶어서 사용하는 도구 입니다. 웹팩은 파일

의존성 파악을 해주고 자동으로 로드도 진행하며 코드 최적화도 진행하고, 이미지 파이을 압축을 해주거나 바이너리 형태의 문자열 데이터로 바꾸는 등의 기능을 추가 제공해준다.

## Vite란?

vue의 창시자 Evan이 만든 차세대 프론트엔드 빌드 툴입니다. 기존에 사용했던 WEBpack의 번들링 툴로 기능을 담당  
기본적으로 Webpack 작성된 프로젝트의 경우에 프로젝트 크기가 커지면서 빌드 속도가 같이 느려지는 문제..! 개발을 진행할 때, 개발 서버를 키는 속도가 같이 점점 느려지는 문제가 발생

- vite는 필요한 모듈을 그때그때 불러오도록 개발 서버를 최적화하는 로직을 추가 (프로젝트 크기와 상관없이 빠른 빌드 속도를 항상 유지)

요약 : vite 프로젝트로 진행하게 되는 경우 개발 서버 실행 속도를 빠르게 유지할 수 있다.

제품(production)을 만드는 상황일 때, WEbpack과 큰 성능 X
