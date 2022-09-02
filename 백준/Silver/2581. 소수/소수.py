m = int(input())
n = int(input())

result = set()

for i in range(m, n+1):
    if i != 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            result.add(i)

if not result:
    print(-1)
else:
    print(sum(result))
    print(min(result))
