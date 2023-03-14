# 2606. 바이러스
from collections import deque

n = int(input())
m = int(input())
computers = list(range(n + 1))
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# print(graph)

def bfs(start):
    visited = [False] * (n + 1)
    visited[start] = True
    queue = deque([])
    queue.append(start)
    cnt = 0

    while queue:
        v = queue.popleft()
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                cnt += 1
                queue.append(next_v)

    return cnt

print(bfs(1))