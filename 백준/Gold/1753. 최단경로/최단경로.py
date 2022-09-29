import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]     # 힙 선언 [(비용, 정점)]

    while heap:
        # 1. 최단 거리가 짧은 정점을 선택
        min_dist, min_node = heappop(heap)
        
        # 2. 이미 최단 거리로 기록되어 있는 값보다 높은 경우 무시
        if min_dist < distance[min_node]:
            continue
        
        # 3. 해당 정점에 인접한 정점에 대해 최단 거리 갱신
        for dist, next_node in graph[min_node]:
            new_dist = min_dist + dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))


v, e = map(int, input().split())        # 정점, 간선 개수
k = int(input())
graph = [[] for _ in range(v + 1)]
INF = 99999999      # 나올 수 없는 임의의 큰 수
distance = [INF] * (v + 1)      # 출발 정점에서 다른 정점들까지의 최단 거리(무한으로 초기화)
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

dijkstra(k)     # k 부터 시작

for i in distance[1:]:
    if i == INF:
        print('INF')
    else:
        print(i)