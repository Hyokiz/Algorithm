# 1251. 하나로

from heapq import heappop, heappush
import math

def prim(start):
    visited = [False] * (n + 1)
    heap = [(0, start)]
    cost = 0

    while heap:
        min_dist, min_node = heappop(heap)

        if visited[min_node]:
            continue

        visited[min_node] = True
        cost += e * (min_dist ** 2)

        for next_dist, next_node in graph[min_node]:
            if not visited[next_node]:
                heappush(heap, (next_dist, next_node))

    return round(cost)


for t in range(1, int(input()) + 1):
    n = int(input())
    rows = list(map(int, input().split()))
    cols = list(map(int, input().split()))
    e = float(input())
    graph = [[] for _ in range(n)]
    nodes = []
    for i in range(n):
        nodes.append((i, rows[i], cols[i]))

    for i in range(n):
        for j in range(i+1, n):
            w = abs((nodes[i][1] - nodes[j][1]) ** 2+ (nodes[i][2] - nodes[j][2]) ** 2)
            w = math.sqrt(w)
            graph[i].append((w, j))
            graph[j].append((w, i))

    print(f'#{t}', prim(0))