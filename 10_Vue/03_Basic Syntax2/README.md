# 03. Basic Synytax

# Vue의 Directive

HTML 요소에 추가적인 동작을 부여하는 특별한 값을 속성

1. v-if : 조건부 렌더링을 수행하는 directive.

- 해당 요소가 렌더링에서 제외된다.

2. v-show : 조건부 렌더링을 수행하는 directive.

- 해당 속성이 부여되어 있는 조건이 거짓이 되는 경우 해당 HTML 요소를 CSS display 속성으로 숨긴다.

3. v-for : 리스트 렌더링 수행하는 directive.

- 지정된 배열에 대해서 템플릿을 여러번 반복하여 렌더링할 때 사용.
- v-for 배열을 순회하거나 객체 속성을 반복하여 사용할 때 쓰임
- **각 반복되는 요소에 대한 고유한 ,key 속성이 있어야 한다.**

v-for에 key 사용해야 하는 이유

- 해당 HTML 요소에 대해서 고유하게 식별하기 위한 정보로서 keu를 사용하기 때문
  - 가상 DOM에서 요소에 대한 재활용을 위해 아이템이 재정렬(순서)되거나, 데이터에 대한 변경점이 생긴 경우! key에 의존하여 다시 렌더링을 수행하게 된다.
    - in place-patch 전략 : in-place(현 시점에서) patch(땜방)을 DOM에서 바뀌어야할 부분만 처리하거나 재사용한다.

v-if와 v-for를 같이 사용하지 말라! (하나의 HTML 요소에 v-if, v-for 속성을 같이 사용하지 말라)

- v-if/v-for를 같이 활용할 수 잇도록 해결 방안 두가지

1. 조건부 (v-if)에 대한 렌더링과 반복(v-for에 대한 렌더링 분리해서 작성하기)

- v-if를 상위의 부모 노드에 속성으로 부여(조건부 렌더링), v-for를 자식 노드의 속성으로 부여

# 속성

## Methods

해당 컴포넌트 내에서 메소드를 정의를 하여 원하는 동작을 구현할 수 있다.
(Vue3 인스턴스 내에서 정의하는 메소드를 의미합니다.)

## Computed

Vue에 있는 인스턴스 데이터를 기반으로 계산된 값을 자동으로 업데이트하고 캐싱하는 속성입니다.

- 템플릿에서 표현식이나 메소드를 활용할 때보다 더 효율적

# Watch

Vue 인스턴스 데이터 변화를 감시하다가 변화가 발생하면 특정 로직을 수행하는 역할

- 요약 : 둘 다 데이터 변화를 감지하고 처리하느 (공통)
  - computed : 일기 형태러 데이터를 변환하거나 계산된 값을 반환하는 역할
  - watch : 데이터의 변화를 감지해서 특정 로직을 실행하는 역할
  - 둘 다 원본 데이터에 대한 변경처리를 되도록 지양하라

# 라이프 사이클 훅

- 컴포넌트의 생명주기에 대해서 내가 원하는 동작(코드를) 실행할 수 있도록 조작, 제어하는 역할 부여
  - setup(BeforeCreate), created : Vue객체가 생성되는 때에 데이터 초기 상태를 만들 때 사용
  - onBeforeMount : 컴포넌트가 DOM에 마운트(연결) 되기 전
  - onMounted : 해당 컴포넌트가 DOM에 마운트(연결) 됨
    - DOM에 대한 기초 조작이 필요할 때 활용
  - onBeforeUpdate : 해당 컴포넌트가 업데이트(렌더링) 되기 전
    - 가상 DOM -> 실제 DOM 진행되기 전
    - 해당 변경될 데이터에 대한 검증 또는 추가적인 로직 시행
  - onUpdated : 해당 컴포넌트가 업데이트(렌더링) 된 후
    - 가상 DOM -> 실제 DOM 동기화 완료된 시점
    - 해당 변경된 데이터들을 서버와 동기화할 때에 활용
    - **절대! onUpdated에서 DOM에 대한 변경이 일어나는 코드 작성 X**
  - onBeforeUnmount : 해당 컴포넌트가 DOM에 대한 연결이 끊기기 전
  - onUnmount : 해당 컴포넌트가 DOM에 대한 연결이 끊김
    - 데이터에 대한 소별 관리를 진행할 때에 사용 (서버를 삭제)

# Computed Property

## computed

계산된 속성을 정의하는 함수

- 미리 계산된 속성을 사용하여 템플릿에서 표현식을 단순하게 하고 불필요한 반복 연산을 줄임

### 기본 예시

- 할일이 남았는지 여부에 따라 다른 메시지를 출력하기

![Alt text](images/image.png)

- 템플릿이 복잡해지면 todos에 따라 계산을 수행하게 됨
- 만약 이 계산을 템플릿에 여러 번 사용하는 경우 반복이 발생

---

computed 적용

- 반응성 데이터를 포함하는 복잡한 로직의 경우 computed를 활용하여 미리 값을 계산

![Alt text](images/image-1.png)

### computed 특징

- 이미 계산된 결과를 가져오는 것임! 함수를 가져오는게 아니다 ~~
- 반환되는 값은 computed ref이며 일반 refs와 유사하게 계산된 결과를 .value로 참조할 수 있음(템플릿에서는 .value 생략 가능)
- computed 속성은 의존된 반응형 데이터를 **자동으로 추적**
- 의존하는 데이터가 변경될 때만 재평가
  - restOfTodos의 계산은 todos에 의존하고 있음
  - 따라서 **todos가 변경될 때만 resOfTodos가 업데이트**더;ㅁ

![Alt text](images/image-2.png)

## Computed vs .Methods

### computed와 동일한 로직을 처리할 수 있는 method

- computed 속성 대신 method로도 동일한 기능을 정의할 수 있음
- 두 가지 접근 방식은 실제로 완전히 동일

![Alt text](images/image-3.png)

### computed와 method 차이

- computed 속성은 **의존된 반응형 데이터를 기반으로 캐시(cached)된다**
- 의존하는 데이터가 변경된 경우에만 재평가됨
- 즉, 의존된 반응형 데이터가 변경되지 않는 한 이미 계산괸 결과에 대한 여러 참조는 다시 평가할 필요 없이 이전에 계산된 결과를 즉시 반환
- 반면, method 호출은 다시 렌더링이 발상핼 때마다 항상 함수를 실행

### Cache (캐시)

- 데이터나 결과를 일시적으로 저장해두는 임시 저장소
- 이후에 같은 데이터나 결과를 다시 계산하지 않고 빠르게 접근할 수 있도록 함

예시

- 웹 페이지의 캐시 데이터
  - 페이지 일부 데이터를 브라우저 캐시에 저장 후 같은 페이지에 다시 요청 시 모든 데이터를 다시 응답 받는 것이 아니 캐시된 데이터를 사용하여 더 빠르게 웹 페이지를 렌더링

![Alt text](images/image-4.png)

### computed와 method의 적절한 사용처

computed

- 의존하는 데이터에 따라 결과가 바뀌는 계산된 속성을 만들 때 유용
- 동일한 의존성을 가진 여러 곳에서 사용할 때 계산 결과를 캐싱하여 중복 계산 방지

method

- 단순히 특정 동작을 숳애하는 함수를 정의할 때 사용
- 데이터에 의존하는지 여부와 관계없이 항상 동일한 결과를 반환하는 함수

### method와 computed 정리

- computed : 의존된 데이터가 변경되면 자동으로 업데이트
- mtehod : 호출해야만 실행됨
- 무조건 computed만 사용하는 것이 아니라 사용 목적과 상황에 맞게 computed와 method를 적절히 조합하여 사용

# conditional rendering

## v-if

표현식 값의 T/F를 기반으로 요소를 조건부로 렌더링

### v-if 예시

- 'v-else' directive를 사용하여 v-if에 대한 else 블록을 나타낼 수 잇음

![Alt text](images/image-5.png)  
![Alt text](images/image-6.png)

- 'v-else-if' directive를 사용하여 v-if에 대한 else if 블록을 나타낼 수 잇음

![Alt text](images/image-7.png)

### 여러 요소에 대한 v-if 적용

- v-if는d directive이기 때문에 단일 요소에만 연결 가능
- 이 경우 **template**요소에 v-if를 사용하여 하나 이상의 요소에 대해 적용할 수 있음 (v-else, v-else-if 모두 적용 가능)

![Alt text](images/image-8.png)

### HTML template element

- 페이지가 로드될 때 렌더링 되지 않지만 JavaScript를 사용하여 나중에 문서에 사용할 수 있도록 하는 HTML을 보유하기 위한 메커니즘
- 보이지 않는 wrapper 역할

## v-if vs v-show

### v-show

표현식 값의 T/F를 기반으로 요소의 가시성(visibility)을 전환

### v-show 예시

- v-show 요소는 항상 렌더링 되어 DOM에 남아 있음!!
- CSS display 속성만 전환하기 때문
- 일단 렌더링 해두고 display:none으로 진행

![Alt text](images/image-9.png)

### v-if vs v-show

- v-if (Cheap initial load, expensive toggle)

  - 초기 조건이 false인 경우 아무 작업도 수행하지 안흥ㅁ
  - 토글 비용이 높음
  - 거짓이라면 이거 지우고 다시 쓰고 해야하니까 토글이 비싸다!

- v-show (Expensive initial load, cheap toggle)

  - 초기 조건에 관계 없이 항상 렌더링
  - 초기 렌더링 비용이 더 높음
  - 일단 렌더링 해두니까 초기 비용이 비싸다!

- 무언가를 매우 자주 전환해야 하는 경우에는 v-show를, 실행 중에 조건이 자주 변경되지 않는 경우에는 v-if를 권장

# List Rendering

## v-for

소스 데이터 (Array, Object, number, string, iterable)를 기반으로 요소 또는 템플릿 블록을 여러 번 렌더링

### v-for 구조

- v-for는 **alias in expression**형식의 특수 구문을 사용하여 반복되는 현재 요소에 대한 별칭(allias)을 제공

![Alt text](images/image-11.png)

- 인덱스(객체에서는 키)에 대한 별칭을 지정할 수 잇음

![Alt text](images/image-10.png)

### v-for 예시

- 배열 반복

![Alt text](images/image-13.png)

- 객체 반복

![Alt text](images/image-12.png)

### 여러 요소에 대한 v-for 적용

- template 요소에 대한 v-for를 사용하여 하나 이상의 요소에 대해 반복 렌더링 할 수 있음

![Alt text](images/image-14.png)

### 중첩된 v-for

각 v-for 범위는 상위 범위에 접근할 수 잇음

![Alt text](images/image-15.png)

## v-for with key

반드시 v-for와 key를 함께 사용한다.

- 내부 컴포넌트의 상태를 일관되게 유지
- 데이터의 예측 강능하 행동을 유지 (Vue 내부 동작 관련)

### v-for와 key

- key는 반드시 각 요소에 대한 고유한 값을 나타낼 수 잇는 식별자여야 함

![Alt text](images/image-16.png)

## v-for with v-if

동일 요소에 v-for와 v-if를 함께 사용하지 않는다.

- 동일한 요소에서 v-if가 v-for보다 우선순위가 더 높기 대문
- v-if 조건은 v-for 범위의 변수에 접근할 수 없음

### v-for와 v-if 문제 상황

- todo 데이터를 이미 처리 한 (isComplete === true) todo만 출력하기
- v-if는 todo에 대하여 값을 처리해야 하는데 동시에 진행되니 문제

![Alt text](images/image-17.png)

### v-for와 v-if 해결법 - 1

- **computed를 활용해 필터링 된 목록을 반환하여 반복하도록 설정**

![Alt text](images/image-19.png)

### v-for와 v-if 해결법 - 1

- v-if가 더 높은 우선순위를 가지므로 v-for의 todo 요소를 v-if에서 사용할 수 없음

![Alt text](images/image-18.png)

- v-for와 template 요소를 사용하여 **v-if를 이동**

![Alt text](images/image-20.png)

# Watchers

### watch()

반응형 데이터를 감시하고, 감시하는 데이터가 변경되면 콜백 함수를 호출

### watch 구조

![Alt text](images/image-21.png)

- variablee : 감시하는 변수
- newValue : 감시하는 변수가 변환된 값, 콜백 함수의 첫번째 인자
- oldValue : 콜백 함수의 두번째 인자

### watch 예시

1. 감시하는 변수에 변화가 생겼을 때 기본 동작 확인하기

![Alt text](images/image-22.png)
![Alt text](images/image-23.png)

2. 감시하는 변수에 변화가 생겼을 때 연관 데이터 업데이트하기

![Alt text](images/image-24.png)  
![Alt text](images/image-25.png)

### Computed와 Watchers

![Alt text](images/image-26.png)

# Lifecycle Hooks

Vuw 인스턴스의 생애주기 동안 특정 시점에 실행되는 함수

- 개발자가 특정 단계에서 의도하는 로직이 실행될 수 잇도록 함

### Lifecycle Hooks 예시

1. Vue 컴포넌트 인스턴스가 초기 렌더링 및 DOM 요소 생성이 완료된 후 특정 로직을 수행하기

![Alt text](images/image-27.png)

2. 반응형 데이터의 변경으로 인해 컴포넌트의 DOM이 업데이트된 후 특정 로직을 수행하기

![Alt text](images/image-28.png)  
![Alt text](images/image-29.png)

### Lifecycle Hooks 특징

- Vue는 Lifecycle Hooks에 등록된 콜백 함수들을 인스턴스와 자동으로 연결함
- 이렇게 동작하려면 hooks 함수들은 반드시 동기적으로 작성되어야 함
- 인스턴스 생애 주기의 여러 단계에서 호출되는 다른 hooks도 있으며, 가장 일반적으로 사용되는 것은 onMounted, onUpdated, onUnmounted

### Lifecycle Hooks Diagram

![Alt text](images/image-30.png)

# Vue Style Guide

- vue의 스타일 가이드 규칙은 우선순위에 따라 4가지 범주로 나눔
- 규칙 범주
  - ![Alt text](images/image-31.png)

### 우선순위 별 특징

A : 필수(Essential)

- 오류를 방지하는데 도움이 되므로 어떤 경우에도 규칙을 학습하고 준수
  - v-for에 key 작성하기
  - 동일 요소에 v-if와 v-for 함께 사용하지 않기

B : 적극 권장(Strongly Recommended)

- 가독성 및/떠ㅗ는 개발자 경험을 향상시킴
- 규칙을 어겨도 코드는 여전히 실행되겠지만, 정당한 사유가 있어야 규칙을 위반할 수 있음

C : 권장 (Recommended)

- 일관성을 보장하도록 임의의 선택을 할 수 잇음

D : 주의 필요 (User with Caution)

- 잠재적 위험 특성을 고려함

# 참고

### [주의] computed의 반환 값은 변경하지 말 것

- computed의 반환 값은 의존하는 데이터의 파생된 값
- 일종의 snapshot이며 의존하는 데이터가 변경될 때 마다 새 snapshot이 생성됨
- snapshot 을 변경하는 것은 의미가 없으므로 계산된 반환 값은 읽기 전용으로 취급되어야 하며 변경되어서는 안됨
- 대신 새 값을 얻기 위해서는 의존하는 데이터를 업데이트 해야함

### [주의] computed 사용 시 원본 배열 변경하지 말 것

- computed에서 reverse() 및 sort() 사용시 원본 배열을 변경하기 때문에 벅사본을 만들어서 진행해야함

![Alt text](images/image-32.png)

### [주의] 배열의 인덱스를 v-for의 key로 사용하지 말것

![Alt text](images/image-33.png)

- 인덱스는 식별자가 아닌 배열의 항목 위치만 나타내기 때문에 Vue가 Dom을 변경할 때(끝이 아닌 위치에 새 항목이 배열에 삽입되면) 여러 컴포넌트간 데이터 공유 시 문제가 발생
- 직접 고유한 값을 만들어내는 메서드를 만들거나 외부 라이브러리 등을 활용하는 등 식별자 역할을 할 수 있는 값을 만들어 사용

### v-for와 배열 - 배열 변경 감지

수정 메서드 (원본 배열 수정)

- Vue는 반응형 배열의 변경 메소드가 호출 되는 것을 감지하여, 필요한 업데이트를 발생 시팀
- push(), pop(), shift(), unshift(), splice(), sort(), reverse()

배열 교체

- 원본 배열을 수정하지 않고 새 배열을 반환
- filter(), concat(), slice()

### v-for와 배열 - 필터링/정렬 결과 표사

원본 데이터를 수정하거나 교체하지 않고 필터링 되거나 정렬된 결과를 표시

1. computed 활용

![Alt text](images/image-34.png)

2. method 활용(computed가 불가능한 중첩된 v-for에 경우)

![Alt text](images/image-35.png)
