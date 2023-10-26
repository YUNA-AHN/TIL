# 이벤트

웹페이지:

- 사용자의 입력 (input 폼 입력, 클릭) - 키보드 입력 & akdntm dlqfur
- 브라우저 상태 변화 (페이지 로드, 페이지 새로고침)
- 폼을 제툴

## 이벤트 핸들러(Event Handler)

자바스크립트에서 이벤트를 처리하는 방식  
이벤트 발생 -> 해당 이벤트를 처리하는 함수

### 이벤트 핸들러 정의

- DOM 요소 속성 이벤 핸들러를 정의

```js
<button onclick="alert('클릭했어요!')">Click</button>
```

- addEventListener() 메서드를 사용해서 정의

```js
<button id="myButton">Click</button>
<script>
    const buttonTag = document.querySelector("#myButton");
    buttonTag.addEventListener("click", function () {
    alert("클릭했어요!");
    });
```

## 이벤트 버블링(Event Bubbling)

이벤트가 발생한 요소로부터 상위 요소까지 이벤트가 쭈욱 전파되는 방식을 의미합니다.  
(발생한 위치에서 최상위 요소까지 이벤트가 전달)

```js
    <form>
      <div>
        <button>버튼</button>
      </div>
    </form>
    <script>
      const buttonTag = document.querySelector("button");
      buttonTag.addEventListener("click", function () {
        alert("button 태그가 클릭되었어요!");
      });
      const divTag = document.querySelector("div");
      divTag.addEventListener("click", function () {
        alert("div 태그가 클릭되었어요!");
      });
      const formTag = document.querySelector("form");
      formTag.addEventListener("click", function () {
        alert("form 태그가 클릭되었어요!");
      });
    </script>
```

## 이벤트 캡쳐링(Event Capturing)

```js
// 한바퀴 쭉 내려갔다가 쭉 올라옴
<form>
    <div>
    <button>버튼</button>
    </div>
</form>
<script>
    const tags = document.querySelectorAll("*");
    for (const tag of tags) {
    tag.addEventListener(
        "click",
        function () {
        alert(this.tagName + "클릭");
        },
        false // 세번째 인자를 false로 버블링 방식
    );
    tag.addEventListener(
        "click",
        function () {
        alert(this.tagName + "클릭");
        },
        true // 세번째 인자를 true로 캡쳐링 방식
    );
    }
</script>
```

## 이벤트(evnet) 객체

자바스크립트에서 이벤트가 발생했을 때 이벤트와 관련된 정보를 담고 잇는 객체를 event 객체라고 한다.

이벤트 객체의 속성중에서 target 속성과 currentTarget 속성 이 두가지를 알아보자

target 속성 : 이벤트가 실제로 발생한 요소를 참조
currentTarget 속성 : 이벤트 핸들러가 추가된 요소를 참조(=this)

버블링 막기(Prevent Event Bobbling )
이벤트 버블링은 이벤트가 발생한 요소에서 가장 최상위 요소가지 이벤트가 전파되는 현상
-> 자바스크립트에서는 'preventdefault() / defaultPrevented' 이 두가지를 통해서 버블링 현상을 확인하고 조건 처리를 할 수 있다.

- event.stopPropagation 이 메소드를 사용해서 아예 버블링을 중단시킬 수 잇음

event.stopPropagation()을 사용하게 되면 이벤트가 상위요소로 전파되는것을 막ㄱ을 수 잇다. 이벤트 버블링 현상을 완전히 막아버린다.
상위요소에서 해당 이벤트를 처리해야하는 상황인 경우에는 적절치 않다.

preventDefault() 메소드는 이벤트가 발생된 요소에 대한 기본 동작을 취소할 수 있는 메소드 입니다.
예) a 태그: 클릭하였을 때 -> href 속성으로 들어있는 사이트 페이지로 이동! (기본)
input[type="submit"] 태그 : 클릭 -> form에 잇는 데이터가 서버로 전송 ( 기본)
-> 이러한 기본 동작을 취소할 수 있게 해준다.

이 preventDefault() 메소드가 한 번 호출이 되면, defaultPrevented라는 속성값이 true로 벼경이 됩니다.
-> 해당 속성값을 사용해서
