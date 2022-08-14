l = [1, 1, 2, 2, 2, 8]

t = list(map(int, input().split()))

for i in range(6):
    print(l[i] - t[i], end=" ")