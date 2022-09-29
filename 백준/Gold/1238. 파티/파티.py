from heapq import heappush, heappop

def dijkstra(distance, graph, start):
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


n, m, x = map(int, input().split())
graph1 = [[] for _ in range(n + 1)]
graph2 = [[] for _ in range(n + 1)]
INF = 99999999
distance1 = [INF] * (n + 1)
distance2 = [INF] * (n + 1)

for _ in range(m):
    s, e, w = map(int, input().split())
    graph1[s].append((w, e))
    graph2[e].append((w, s))

dijkstra(distance1, graph1, x)
dijkstra(distance2, graph2, x)

answer = []
for i in range(1, n + 1):
    answer.append(distance1[i] + distance2[i])

print(max(answer))