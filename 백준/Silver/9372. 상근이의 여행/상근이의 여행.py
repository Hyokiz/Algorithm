# 9372. 상근이의 여행
from heapq import heappop, heappush

# 정점이 많다 > 크루스칼, 간선이 많다 > 프림

def prim(start):
    visited = [False] * (n + 1)
    heap = [start]
    cost = 0

    while heap:
        min_node = heappop(heap)

        if visited[min_node]:
            continue

        visited[min_node] = True
        cost += 1

        for next_node in graph[min_node]:
            if not visited[next_node]:
                heappush(heap, next_node)

    return cost - 1


for t in range(int(input())):
    n, m = map(int, input().split())
    graph =[[] for _ in range(n + 1)]
    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    print(prim(1))
