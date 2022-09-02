m = int(input())
n = int(input())

result = 0
sig = True
for i in range(m, n+1):
    if i != 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            result += i
            if sig:
                result_min = i
                sig = False
if not result:
    print(-1)
else:
    print(result)
    print(result_min)

