n = int(input())
numbers = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if numbers[i] > 1:
        for j in range(2, numbers[i]//2+1):
            if numbers[i] % j == 0:
                break
        else:
            cnt += 1

print(cnt)