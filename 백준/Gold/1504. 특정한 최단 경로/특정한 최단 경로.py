import sys
from heapq import heappop, heappush
INF = 99999999

def dijkstra(start, end):
    distance = [INF] * (n + 1)
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        min_dist, min_node = heappop(heap)

        if min_dist > distance[min_node]:
            continue

        for next_dist, next_node in graph[min_node]:
            new_dist = min_dist + next_dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))

    return distance[end]

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))
    graph[e].append((w, s))

u, v = map(int, input().split())

result1 = dijkstra(1, u) + dijkstra(u, v) + dijkstra(v, n)
result2 = dijkstra(1, v) + dijkstra(v, u) + dijkstra(u, n)

if result1 + result2 > INF:
    print(-1)
else:
    print(min(result1, result2))
