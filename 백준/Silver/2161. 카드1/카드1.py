n = int(input())
q = [i for i in range(1, n+1)]
result = []
while q:
    result.append(q.pop(0))
    if q:
        q.append(q.pop(0))

print(*result)