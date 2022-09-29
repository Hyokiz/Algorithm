from heapq import heappush, heappop

# 가는길, 오는길 따로 일방통행인 다익스트라 문제
# 인자로 거리, 그래프, 시작점을 넣는다.
def dijkstra(distance, graph, start):
    # 시작점 거리 초기화
    distance[start] = 0
    # 거리, 시작점을 heap 에 추가
    heap = [(0, start)]

    while heap:
        # 1. 최단 거리가 가장 짧은 정점 선택
        min_dist, min_node = heappop(heap)

        # 2. 이미 최단 거리로 기록되어 있는 값보다 높은 경우 무시
        if min_dist > distance[min_node]:
            continue

        # 3. 해당 정점에 인접한 정점들에 대해 최단 거리 갱신
        for next_dist, next_node in graph[min_node]:
            new_dist = min_dist + next_dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))


n, m, x = map(int, input().split())
graph1 = [[] for _ in range(n + 1)]     # 가는길 인접정점
graph2 = [[] for _ in range(n + 1)]     # 오는길 인접정점
INF = 99999999
distance1 = [INF] * (n + 1)     # 가는길 거리
distance2 = [INF] * (n + 1)     # 오는길 거리

for _ in range(m):
    s, e, w = map(int, input().split())
    graph1[s].append((w, e))
    graph2[e].append((w, s))

# 가는길, 오는길 distance에 추가
dijkstra(distance1, graph1, x)
dijkstra(distance2, graph2, x)

answer = []
for i in range(1, n + 1):
    answer.append(distance1[i] + distance2[i])

print(max(answer))