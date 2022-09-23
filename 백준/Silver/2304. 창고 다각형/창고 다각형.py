n = int(input())
counter = [0 for _ in range(1001)]
max_idx = 0
max_height = 0
for _ in range(n):
    width, height = map(int, input().split())
    counter[width] = height
    if max_height < height:
        max_idx = width
        max_height = height

temp = 0
result = 0
for i in range(max_idx+1):
    temp = max(temp, counter[i])
    result += temp

temp = 0
for i in range(1000, max_idx, -1):
    temp = max(temp, counter[i])
    result += temp

print(result)