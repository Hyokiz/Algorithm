# BOJ 1260. DFS와 BFS
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in graph:
    i.sort()


def dfs(v):
    visited1[v] = True
    print(v, end=' ')

    for next_v in graph[v]:
        if not visited1[next_v]:
            dfs(next_v)


def bfs(v):
    visited2[v] = True
    queue = deque([v])
    print(v, end=' ')

    while queue:
        v = queue.popleft()

        for next_v in graph[v]:
            if not visited2[next_v]:
                visited2[next_v] = True
                queue.append(next_v)
                print(next_v, end=' ')


dfs(v)
print()
bfs(v)

