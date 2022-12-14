from heapq import heappop, heappush

def prim(start):
    visited = [False] * (n + 1)
    heap = [(0, start)]
    cost = 0
    max_value = 0

    while heap:
        min_dist, min_node = heappop(heap)

        if visited[min_node]:
            continue

        visited[min_node] = True
        cost += min_dist
        if min_dist >= max_value:
            max_value = min_dist

        for next_dist, next_node in graph[min_node]:
            if not visited[next_node]:
                heappush(heap, (next_dist, next_node))

    return cost - max_value


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))
    graph[e].append((w, s))

print(prim(1))