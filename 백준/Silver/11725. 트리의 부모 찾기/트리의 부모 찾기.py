# 11725. 트리의 부모 찾기
from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        node = queue.popleft()
        for i in tree[node]:
            if not visited[i]:
                result[i] = node
                queue.append(i)
                visited[i] = True



n = int(input())
visited = [False] * (n + 1)
tree = [[] for _ in range(n+1)]
result = [0] * (n + 1)
for _ in range(n-1):
    v1, v2 = map(int, input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)

bfs(1)

for case in result[2:]:
    print(case)