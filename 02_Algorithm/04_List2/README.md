# 04_List2
# 검색
저장되어 있는 자료 중에서 원하는 항목을 찾는 작업
- 목적하는 탐색 키를 가진 항목을 찾는 것
    - 탐색 키(search key): 자료를 구별하여 인식할 수 있는 키

검색의 종류
- 순차 검색(sequential search)
- 이진 검색(binary search)
- 해쉬(hash) : 내용 이용해서 찾아가는 것

## 순차 검색 (Sequential Search)
- 가장 간단하고 직관적인 검색 방법
- 배열이나 연결 리스트 등 **순차구조**로 구현된 자료 구조에서 원하는 항목 찾을 때 유용
- 알고리즘이 단순하여 구현이 쉽지만, 검색 대상 많은 경우 비효율적
    - 정렬되어 있지 않은 경우
    - 정렬되어 있는 경우
    
### 검색 과정 - 정렬되어 있지 않은 경우
1. 첫 번째 원소부터 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾는다.
2. 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환
3. 자료구조의 마지막에 이를 때가지 검색 대상을 찾지 못하면 검색 실패

**찾고자 하는 원소의 순서**에 따라 **비교 회수**가 결정
- 첫 번째 원소를 찾을 땐 한 번 ~ 두 번재 원소를 찾을 때는 두 번 ~
- 정렬되지 않은 자료에서의 순차 검색의 평균 비교 횟수
    - (1/n) * (1+2+3+...+n) = (n+1)/2
- 시간 복잡도: O(n)
```python
def sequentialSearch(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i = i + 1
    if i < n : return i
    else: return - 1
```

### 검색 과정 - 정렬되어 있는 경우
- 자료가 오름차순으로 정렬된 상태에서 검색 실시 가정
- 자료를 순차적으로 검색하면서 키 값을 비교하여, 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것이므로 검색 종료

**찾고자 하는 원소의 순서**에 따라 **비교 회수**가 결정
- 정렬이 되어 있으므로, 검색 실패를 반환하는 경우 평균 비교히수가 반으로 감소
- 시간 복잡도: O(n)
```python
def sequentialSearch2(a, n, key):
    i = 0
    while i < n and a[i] < key :
        i = i + 1
    if i < n and a[i] == key:
        return i
    else: return -1
```
## 이진 검색(Binary Search) ⭐⭐⭐⭐⭐
(코드 2개 나오는데 서술 0.5 / 0.5)  
자료 **가운데**에 있는 항목의 키 값과 비교하여 
다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
- 목적 키를 찾을 때가지 이진 검색을 순환적으로 반복 수행 -> 검색 범위를 반으로 줄인다!

**이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.**

### 이진 검색 과정
1. 자료의 중앙에 있는 원소를 고른다.
2. 중안 원소의 값과 찾고자 하는 목표 값을 비교한다.
3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행, 크다면 자료의 오른쪽 방에 대해서 새로 검색
4. 찾고자 하는 값 찾을 때까지 1~3 과정 반복

### 구현
- 검색 범위의 시작점과 종료점을 이용항 검색을 반복 수행
- 이진 검색의 경우, 자료에 삽입이나 삭제 발생했을 때 배열의 상태를 **항상 정렬** 상태로 유지하는 추가 작업 필요


- 스스로 구현할 수 있도록!
```python
⭐⭐⭐⭐⭐
def binarySearch(a, N, key):
    start = 0
    end = N - 1
    while start <= end:
    middle = (start + end) // 2
    if a[middle] == key: # 검색 성공
        return True
    elif a[middle] > key :
        end = middle -1 # 무한루프에 걸릴 수 있음
    else:
        start = middle + 1 # 마찬가지로 무한루프!
    return False # 검색 실패
```

재귀함수 이용 - 하나의 방법 정도로 ~
```python
def binarySearch2(a, low, high, key):
    if low > high : # 검색 실패
        return False
    else:
    middle = (low + high) // 2
    if key == a[middle] : #검색 성공
        return True
    elif key < a[middle]:
        return binarySearch2(a, low, middle -1, key)
    elif a[middle] < key:
        return binarySearch2(a, middle + 1, high, key)
```

# 인덱스
Database에서 유래된 용어로, 테이블에 대한 동작 속도를 높여주는 자료 구조  
Look up table 등의 용러를 사용하기도

인덱스를 저장하는데 필요한 디스크 공간은 보통 테이블을 저장하는 데 필요한 디스크 공간보다 작음

- 배열을 사용한 인덱스 : 탐색(검색), 삽입, 삭제
    - 대량의 데이터를 매번 정렬하면 프로그램 느려짐
    - 대량 데이터 성능 저하 문제를 해결하기 위한 배열 인덱스  
원본 데이터와 별개로 **배열 인덱스를 추가**
      
## 선택 정렬(Selection Sort)⭐⭐⭐ : 버블정렬과 비교할 줄 알아야
주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치 교환하는 방식

- 정렬 과정
    - 주어진 리스트 중에서 **최소값**을 찾는다.
    - 그 값을 리스트의 맨 앞에 위치한 값과 교환
    - 맨 처음 위치를 제외한 나머지 리스트 대상으로 과정 반복
    
- 시간 복잡도 : O(n^2)

```python
def selectionSort(a, N):
    for i in range(N -1):
    minIdx = i
    for j in range(i + 1, N): # 최솟값 찾음
        if a[minIdx] > a[j]:
            minIdx = j
    a[i], a[minIdx] = a[minIdx], a[i] # 인덱스 교환
```

## 설렉션 알고리즘(Selection Algorithm)
저장되어 있는 자료로부터 k번재로 큰 혹은 작은 원소를 찾는 방법
- 최소값, 최대값 혹은 중간값을 찾는 알고리즘을 의미하기도 한다

### 선택 과정
1. 정렬 알고리즘을 이용하여 자료 정렬하기
2. 원하는 순서에 있는 원소 가져오기

k 번째로 작은 원소를 찾는 알고리즘
- 1번부터 k번째까지 작은 원소들을 찾아 배열의 앞쪽으로 이동시키고, 배열의 k번째를 반환한다.
- k가 비교적 작을 때 유용 / 시간복잡도 : O(kn)

```python
def select(arr, k):
    for i in range(0, k):
    minIdex = i
        for j in range(i+1, len(arr)):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return arr[k-1]
```

로직 흐름 이해할 수 있도록 ~ 손으로 한 번씩 써보자!
