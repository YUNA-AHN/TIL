# 01. HTML/CSS
# 웹 소개

## World Wide Web
인터넷으로 연결된 컴퓨터들이 정보를 공유하는 거대한 정보 공간

Web
- web site, web application 등을 통해 사용자들이 정보를 검색하고 상호 작용하는 기술

Web site
- 인터넷에서 여러개의 **Web page**가 모인 것으로, 사용자들에게 정보나 서비스를 제공하는 공간

Web page
- HTML, CSS 등의 웹 기술을 이용하여 만들어진, **"Web site"를 구성하는 하나의 요소**

Web page 구성 요소
![Alt text](image.png)
![Alt text](image-1.png)

# 웹 구조화
## HTML : HyperText Markup Language
웹 페이지의 의미와 **구조**를 정의하는 언어

Hypertext
- 웹 페이지를 다른 페이지로 연결하는 링크
- 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

Markup Language
- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
- ex) HTML, Markdown

Markup Language 예시
![Alt text](image-2.png)
![Alt text](image-3.png)
![Alt text](image-4.png)
![Alt text](image-5.png)

## Structure of HTML
```html
<!-- 저장 후 alt + b : 웹페이지로 확인 가능-->
<!DOCTYPE html>
 <html lang='en'> <!--어떤 언어로 읽혀야 하는지 -->
 <head>
    <meta charset="UTF-8"> <!-- 닫힌 태그가 없는 것 -->
    <title>My page</title>
</head>
<body>
    <p>This is my page</p>
</body>
</html>
```

태그들 사이에 상하관계가 존재한다.
- <!DOCTYPE html>
- <html></html>
    - 열린 태그와 닫힌 태그
    - 전체 페이지의 콘텐츠를 포함
- <title></title>
    - 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용
- <head></head>
    - HTML 문서에 관련된 설명, 설정 등
    - 사용자에게 보이지 않음
- <body></body>
    - 페이지에 표시되는 모든 콘텐츠


### HTML Element(요소)
![Alt text](image-6.png)
하나의 요소는 여는 태그와 닫는 태그 그리고 그 안의 내용으로 구성됨  
닫는태그는 태그 이름 앞에 슬래시가 포함되며 닫는 태그가 없는 태그도 존재

### HTML Attributes(속성)
![Alt text](image-7.png)
규칙
- 속성은 요소 이름과 속성 사이에 공백이 있어햐함
- 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분 함
- 속성 값은 열고 다는 따옴포료 감사야 함

목적
- 나타내고 싶지 않지만 **추가적인 기능, 내용**을 담고 싶을 때 사용
- CSS에서 해당 **요소를 선택**하기 위한 값으로 활용됨

```html
<!-- 저장 후 alt + b : 웹페이지로 확인 가능-->
<!DOCTYPE html>
 <html lang='en'> <!--어떤 언어로 읽혀야 하는지 -->
 <head>
    <meta charset="UTF-8"> <!-- 닫힌 태그가 없는 것 -->
    <title>My page</title>
</head>
<body>
    <p>This is my page</p> <!-- 기본 속성이 없는 태크 -->
    <a href="https://www.google.co.kr">Google</a> <!-- a 태그에 href을 입력 -->
    <img src = 'images/sample.png' alt="sample-img"> <!-- 이미지 주소 입력 : 로컬, 인터넷 모두 가능 -->
    <img src = 'https://random.imagecdn.app/600/150' alt="sample-img"> <!-- 스크린 읽기에서 alt 값을 읽음 -->
</body>
</html>
```
![Alt text](image-8.png)

## TEXT Strucutre
HTML TEXT Structure
- HTML의 주요 목적 중 하나는 **텍스트 구조와 의미**를 제공하는 것

HTML : HyperText Markup Language
- 웹 페이지의 **의미**와 구조를 정의하는 언어

<h1>Heading</h1>
- 예를 들어 h1 요소는 단순히 텍스트를 크게만 만드는 것이 아닌 현재 **문서의 최상위 제목**이라는 의미를 부여하는 것

### 대표적인 HTML Text structure
![Alt text](image-9.png)

HTML Text structure 예시
```html
<!DOCTYPE html>
<html lang = 'en'>
    <meta charset='UTF-8'> 
    <meta name="viewport" content="width=devixe-width, initia">
    <title>Document</title>
</html>
<body>
    <h1>main heading</h1>
    <h2>sub heading</h2>
    <p>this is my page</p>
    <!-- em : 기울임체 / strong : 볼드체 -->
    <p>this is <em>empahsis</em></p>
    <p>Hi my <strong>name is</strong> air</p>
    <ol> 
        <!-- ol(orderd list) : 정렬된 리스트여서 숫자가 붙어나옴
        <-> ul(unorderd list) : 정렬되지 않은 리스트 -->
        <li>파이썬</li>
        <li>알고리즘</li>
        <li>웹</li>
    </ol>
</body>
```
웹 특성상 디버깅이 어렵다 ! 출력되지 않음을 보고 수정해야한다.

# 웹스타일링
# CSS : Cascading Style Sheet
웹 페이지의 **디자인**과 **레이아웃**을 구성하는 언어

css를 적용하지 않은 웹 사이트 모습
![Alt text](image-12.png)

CSS 구문
![Alt text](image-11.png)
선언 마침을 나타내는 세미콜론(;)이 필요

CSS 적용 방법
1. 인라인(inline) 스타일
    - HTML 요소 안에 style 속성 값으로 작성
    ![Alt text](image-10.png)
2. 내부(Internal) 스타일 시트
    - head 태그 안에 style 태그에 작성
    ![Alt text](image-13.png)
3. 외부(External) 스타일 시트
    - 별도의 CSS 파일 생성 후 HTML link 태그를 사용해 불러오기
    - 가장 권장! 재사용성이 높음
    ![Alt text](image-14.png)

## CSS Selectors(CSS 선택자)
HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자

### CSS Selectors 종류
- 기본 선택자
    - 전체(*) 선택자
    - 요소(tag) 선택자
    - 클래스(class) 선택자
    - 아이디(id) 선택자
    - 속성(attr) 선택장 등
- 결합자 (Combinators)
    - 자손 결합자(" " (space))
    - 자식 결합자(>)

### CSS Selectors 특징
- 전체(*) 선택자
    - HTML 모든 요소를 선택
- 요소(tag) 선택자
    - 지정한 모든 태그를 선택
- 클래스(class) 선택자('.' (dot))
    - 주어진 클래스 속성을 가진 모든 요소를 선택
- 아이디 선택자('#')
    - 주어진 아이디 속성을 가진 모든 요소를 선택
    - 문서에는 주어진 아이디를 가진 요소가 하나만 있어야함
- 자손 결합자(" " (space))
    - 첫번째 요소의 자손 요소를 선턀
    - 예) p span은 <p>안에 있는 모든 <span>를 선택 (하위 레벨 상관 없이)
- 자식 결합자(>)
    - 턱 번째 요소의 직계 자식만 선택
    - 예> ul > li은 <ul> 안에 있는 모든 <li>를 선택 (한 단계 아래 자식드만)

## 우선순위 : Specificity
동일한 요소에 적용 가능한 같은 스타일 두 가지 이상 작성했을 때 어떤 규칙이 적용되는지 결정하는 것

Cascade: 계단식
- 동일한 우선순위를 갖는 규칙이 적용될 때 css에서 마지막에 나오는 규칙이 사용됨

### cascade 예시
h1 태그 내용의 색은 purple이 적용됨
```html
h1 {
    color: red;
}

h1 {
    color: purple;
}
```

### Specificity 예시
동일한 h1 태그에 다음과 같이 스타일이 작성됨다면 h1 내용의 색은 purple이 적용됨
```html
.make-red {
    color: red;
}

h1 {
    color: purple;
}
```

### 우선순위가 높은 순
1. Importance
    - !important
2. inline 스타일
3. 선택자
    - id 선택자 > class 선택자 > 요소 선택자
4. 소스 코드 순서

### !important
다른 우선순위 규치보다 우선하여 적용하는 키워드
**Cascade의 구조를 무시하고 강제로 스타일을 적용하는 방식이므로 사용을 권장하지 않음**

# 상속

# 참고
## HTML 관련 사항
- 요소(태그) 이름은 대소문자를 구분하지 않지만 "소문자" 사용을 권장
- 속성의 따옴표는 작은 따옴표와 큰 따옴표를 구분하지 않지만 "큰 따옴표" 권장
- HTML은 프로그래밍 언어와 달리 에러를 반환하지 않기 대문에 작성 시 주의

##  CSS 인라니(inline) 사티을은 사용하지 말것
CSS와 HTML 구조 정보가 혼합되어 작성되기 때문에 코드를 이해하기 어렵게 만듦