# 1697. 숨바꼭질
from collections import deque

n, k = map(int, input().split())

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            return dist[x]

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < 100001 and not dist[nx]:
                dist[nx] = dist[x] + 1
                queue.append(nx)

dist = [0] * 100001
print(bfs())
