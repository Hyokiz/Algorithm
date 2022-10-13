# 1966. 프린터 큐
from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    queue = deque(priority)
    cnt = 0
    while queue:
        max_v = max(queue)
        p = queue.popleft()
        m -= 1

        if max_v == p:
            cnt += 1
            if m < 0:
                print(cnt)
                break

        else:
            queue.append(p)

            if m < 0:
                m = len(queue) - 1