# 04. graph 
# 최소 신장 트리(MST)
그래프에서 최소 비용 문제
1. 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리 -> MST
2. 두 정점 사이의 최소 비용의 경로 찾기 -> 다익스트라

신장 트리
- n개의 정점으로 이루어진 무방향 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리

최소 신장 트리(Minimum spanning Tree)
- 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리

![images/img.png](images/img.png)
1) 갈 수 있는 곳 중 제일 짧은 곳으로 간다! 
    - BFS와 유사 + 가중치 활용 => 우선순위 큐 활용
    
2) 전체 간선들 중에서 제일 가중치가 적은 곳부터 선택하자

![images/img_1.png](images/img_1.png)

## Prim 알고리즘
하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식
1. 임의의 정점을 하나 선택해서 시작
2. 선택한 정점과 인접하는 정점들중 최소 비용의 간선이 존재하는 정점을 선택
3. 모든 정점이 선택될 때까지 1, 2 반복

서로소인 2개의 집합(2 disjoint-sets) 정보를 유지
- 트리 정점들(tree vertices) - MST를 만들기 위해 선택된 정점즐
- 비트리 정점들(nontree vertices) - 선택되지 않은 정점들

![images/img_2.png](images/img_2.png)
![images/img_3.png](images/img_3.png)

![images/img_4.png](images/img_4.png)
![images/img_5.png](images/img_5.png)

## Kruskal 알고리즘
간선을 하나씩 선택해서 MST를 찾는 알고리즘
1. 최초, 모든 간선을 가중치에 따라 **오름차순**으로 정렬
2. 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가시킴
   - 사이클이 존재하면 다음으로 가중치가 낮은 간선 선택
3. n-1개의 간선이 선택될때까지 2를 반복

![images/img_9.png](images/img_9.png)  
![images/img_8.png](images/img_8.png)  
![images/img_7.png](images/img_7.png)  
![images/img_6.png](images/img_6.png)  

# 최단 경로
간선의 가중치가 있는 그래프에서 두 정점 사이의 경로들 중에 간선의 가중치의 합이 최소인 경로

하나의 시작 점정에서 끝 정점까지의 최단 경로
- 다익스트라(dijkstra) 알고리즘
   - 음의 가중치를 허용하지 않음
- 벨만-포드(Bellman-Ford) 알고리즘
   - 음의 가중치 허용
   
모든 정점들에 대한 최단 경로
- 플로이드-워샬 알고리즘

## dijkstra 알고리즘
시작 정점에서 거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하는 방식

- 시작정점(s)에서 끝정점(t)가지의 최단 경로에 점점 x가 존재한다.
- 이때, 최단경로는 s에서 x까지의 최단 경로와 x에서 t까지의 최단 경로 구성된다
- 탐욕 기법을 사용한 알고리즘으로 MST의 프림 알고리즘과 유사하다.

![images/img_10.png](images/img_10.png)


![images/img_19.png](images/img_19.png)
a 정점에 대해서 현재 정점까지의 최소 비용 계산

![images/img_18.png](images/img_18.png)
D에는 해당 노드가지 최소 거리를 입력

![images/img_17.png](images/img_17.png)
방문하지 않고, 우선 순위 큐에 따라 b가 u에 입력

![images/img_16.png](images/img_16.png)
b에서 방문할 수 있는 c의 최단 거리 계산

![images/img_15.png](images/img_15.png)
![images/img_14.png](images/img_14.png)
![images/img_13.png](images/img_13.png)
![images/img_12.png](images/img_12.png)
![images/img_11.png](images/img_11.png)

### 총정리
그래프 탐색
- 완전 탐색 : DFS, BFS

서로소 집합
- 대표 데이터 비교
- 그래프에서는 싸이클 판별

최소 비용
1. 최소신장트리(MST)
- 전체 그래프에서 총합이 최소인 신장 트리

2. 최단 거리(다익 스트라)
- 정점 사이의 거리가 최단인 경로 찾기