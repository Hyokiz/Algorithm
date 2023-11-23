# 1021. 회전하는 큐

from collections import deque

n, m = map(int, input().split())
pos = list(map(int, input().split()))
dq = deque(list(range(1, n + 1)))

cnt = 0
for i in pos:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq) / 2:
                while dq[0] != i:
                    dq.append(dq.popleft())
                    cnt += 1
            else:
                while dq[0] != i:
                    dq.appendleft(dq.pop())
                    cnt += 1

print(cnt)