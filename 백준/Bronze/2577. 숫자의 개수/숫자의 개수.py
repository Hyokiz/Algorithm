A = int(input())
B = int(input())
C = int(input())

num = list(str(A * B * C))
cnt = [0] * 10
for i in range(len(num)):
    cnt[int(num[i])] += 1

for i in cnt:
    print(i)