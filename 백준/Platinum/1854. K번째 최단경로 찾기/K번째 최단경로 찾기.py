# 1854. k번째 최단 경로 찾기

from heapq import heappop, heappush

def dijkstra(start):
    distance[start][0] = 0
    heap = [(0, start)]

    while heap:
        min_dist, min_node = heappop(heap)

        for next_dist, next_node in graph[min_node]:
            new_dist = min_dist + next_dist

            if new_dist < distance[next_node][k-1]:
                distance[next_node][k-1] = new_dist
                distance[next_node].sort()
                heappush(heap, (new_dist, next_node))


n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = 99999999
distance = [[INF] * k for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))

dijkstra(1)

for i in range(1, n + 1):
    result = distance[i][k-1]
    if result == INF:
        print(-1)
    else:
        print(result)