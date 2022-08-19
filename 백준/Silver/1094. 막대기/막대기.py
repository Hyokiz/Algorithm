stick = [64, 32, 16, 8, 4, 2, 1]

x = int(input())
cnt = 0

for i in stick:
    if x >= i:
        x = x - i
        cnt += 1

print(cnt)