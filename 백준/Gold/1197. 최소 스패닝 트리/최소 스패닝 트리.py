# 1197. 최소 스패닝 트리
from heapq import heappop, heappush

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))
    graph[e].append((w, s))

def prim(start):
    visited = [False] * (v + 1)
    heap = [(0, start)]
    cost = 0

    while heap:
        min_dist, min_node = heappop(heap)

        if visited[min_node]:
            continue

        visited[min_node] = True
        cost += min_dist

        for dist, next_node in graph[min_node]:
            if not visited[next_node]:
                heappush(heap, (dist, next_node))

    return cost

print(prim(1))