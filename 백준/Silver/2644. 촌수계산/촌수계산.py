import sys
sys.setrecursionlimit(10*7)

n = int(input())
s, e = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [0] * (n + 1)

def dfs(v):
    for next_v in graph[v]:
        if not visited[next_v]:
            visited[next_v] = visited[v] + 1
            dfs(next_v)

dfs(s)
if visited[e]:
    print(visited[e])
else:
    print(-1)