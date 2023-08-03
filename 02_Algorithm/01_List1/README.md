# List1
- SWEA IM / A
# 알고리즘
유한한 단계를 통해 문제를 해결하기 위한 절나차 방법  
컴퓨터 용어로 쓰이며, 컴퓨터가 어떤 일을 수행하기 위한 단계적 방법  
**어떠한 문제를 해결하기 위한 절차**

컴퓨터 분야에서 알고리즘을 표현하는 방법
- 의사코드(슈도코드)

![img](https://github.com/YUNA-AHN/TIL/assets/130244216/b3d04efa-6dac-4794-99bf-d6e0d32ca33e)

  
- 순서도  

![img_1](https://github.com/YUNA-AHN/TIL/assets/130244216/357af3d8-5e10-4981-88ef-bdd19461746b)


## 알고리즘의 성능
목표 : 보다 좋은 알고리즘을 이해하고 활용하는 것

좋은 알고리즘이란?
1. 정확성 : 얼마나 정확하게 동작하는가
2. 작업량 : 얼마나 적은 연산으로 원하는 결과를 얻어내는가
3. 메모리 사용량 : 얼마나 적은 메모리를 사용하는가
4. 단순성 : 얼마나 단순하가
5. 최적성: 더 이상 개선할 여지없이 최적화되었는가

주어진 문제를 해결하기 위헤 여러 개의 다양한 알고리즘이 가능
-> 어떤 알고리즘을 사용애야 하는가?

알고리즘의 성능 분석 필요
- 많은 문제에서 성능 분석의 기준으로 알고릐즘의 작업량을 비교한다.

ex ) 1부터 100까지 합을 구하는 문제
1.  1 + 2 + ... + 100 : 100변의 연산
2. (100 * (1 + 100) )/ 2 : 3번의 연산 ~ n의 크기와 상관없이!

알고리즘의 작업량을 표현할 때 시간복잡도로 표현

시간 복잡도(time Complexity)
- 실제 걸리는 시간을 측정
- 실행되는 명령문의 개수를 계산

![img_2](https://github.com/YUNA-AHN/TIL/assets/130244216/4c461cf2-7333-4db3-a5d0-34733e965ebe)

  

시간 복잡도 = 빅-오(O) 표기법 ⭐⭐⭐⭐⭐
- 빅-오 표기법(Big-Oh Notation)
- 시간 복잡도 함수 중에서 가장 큰 영향력을 주는 n에 대한 항만을 표시
- 시간 복잡도 최악, 상한선, 점근적인 상한선을 표기학 위해 사용 !!! < 중요
- 계수 (Coefficient)는 생략하여 표사
O(3n+2) =  o(3n) =  O(n)
  n 개의 데이터를 입력 받아 저장한 후 각 데이터에 1식 증가시킨 후 각 데이터 화면에 출력하는 알고르짐의 시간 복잡도는?
  O(n)
  
- 요소 수가 증가함에 따라 각기 다른 시간복잡도의 알고리즘은 아래와 같은 연산 수를 보인다.

![img_3](https://github.com/YUNA-AHN/TIL/assets/130244216/8cdeb8bd-119d-4dcd-8ca0-7954802a39e8)

  
# 배열
일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조
ex )  num0 = 0 , num1 = 1 , ...  -> num = [0, 1, ..., 5]

필요성
- 프로그램 내에서는 여러 개의 변수가 필요할 때, 일일이 다른 변수명을 이용하여 자료에 접근하는 것은 매우 비효율적일 수 있다.
- 배열을 사용하면 하나의 선언을 통해서 둘 이상의 변수를 선언한다.
- 단순히 다수의 변수 선언을 의미하는 것이 아니라, 다수의 변수로는 하기 힘든 작업을 배열을 활용해 쉽게 ㅎ할 수 있다.

## 1차원 배열
1차원 배열의 선언
- 별도의 선언 방법이 없으면 변수에 처음 값을 할당할 때 생성
- 이름 : 프로그램에서 사용할 배열의 이름
ex ) Arr = ;ist()
  
1차원 배열의 접근
- Arr[0] = 10 

## 연습문제
### 배열 활용 예제 : Gravity
- 상자들이 쌓여있는 방이 있다. 방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향울 받아 낙하한다고 할 때, 
  낙차가 가장 큰 상자를 구하여 그 낙차를 리턴하는 프로그램을 작성하시오
- 중력은 회적이 완료된 후 적응된다.
- 상자들은 모두 한쪽 벽면에 붙여진 상태로 쌓여 2차원의 형태를 이루며 벽에서 떨어져서 쌓인 상자는 없다.
- 방의 가로길이는 항상 100이며, 세로 길이도 항상 100이다.
- 즉, 상자는 최소 0, 최대 100 높이로 쌓을 수 있다.

sol) 나보다 작은 값은 어디까지?! 그중 가장 큰 값은??

# 정렬
2개 이상의 자료를 특정 기준에 의해 작은 값부터 큰 값(오름차순 : ascending), 혹르은
그 반대의 순서대로(내림차순 : descending) 재배열 하는 것
- 키 : 자료를 정렬하는 기준이 되는 특정 값

## 대표적인 정렬 방식의 종류
- 버블 정렬 (Bubble Sort) : 인접한 요소끼리 비교 교환 정렬
- 카운팅 정렬 (Counting Sort) : 요소 값에 대한 출현 횟수
- 선택 정렬 (Selection Sort) : 큰 값을 뽑아서 정렬
- 퀵 정렬 (Quick Sort) : 피봇 중간값으로 정렬
- 삽입 정렬 (Insertion Sort) : 새로운 값에 대해서 정렬이 된 부분에 삽입하는 방식처런 진행
- 병합 정렬 (Merge Sort) : 배열을 반씩 분할해서 정렬하고 병합하는 정렬

다양한 형태의 정렬울 학습하게 된다 !

### 버블 정렬(Bubble Sort)
인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식

- 정렬과정
    - 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동한다.
    - 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다.
    - 교환하며 자리를 이동하는 모습이 물 위에 올라오는 거품 모양과 같다고 하여 버블 정렬 !
    
- 시간 복잡도  : O(n^2)

### 카운팅 정렬(Counting Sort)
항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘

- 제한 사항
    - 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능 
      : 각 항목의 발생 회수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문이다.
- 시간 복잡도 : O(n+k) :  n은 리스트 길이, k는 정수의 최대값

정렬에 대한 안정성....?
- 안정성 X : 각 항목들의 발생 회수를 세고 직접 인덱스되는 배열
- 안정성 O :  누적합..?