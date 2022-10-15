from collections import deque

a, b = map(int, input().split())

def bfs(a, b):
    q = deque([])
    q.append((a, 1))

    while q:
        a, cnt = q.popleft()

        if a == b:
            print(cnt)
            return

        if a * 2 <= b:
            q.append((a * 2, cnt + 1))

        if a * 10 + 1 <= b:
            q.append((a * 10 + 1, cnt + 1))

    print(-1)

bfs(a, b)
