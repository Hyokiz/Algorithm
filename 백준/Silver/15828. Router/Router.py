from collections import deque

n = int(input())
q = deque()
while True:
    r = int(input())
    if r == -1:
        break

    if r != 0 and len(q) < n:
        q.append(r)

    elif r == 0:
        q.popleft()

if q:
    print(*q)
else:
    print("empty")


    