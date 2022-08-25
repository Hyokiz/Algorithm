n = int(input())

cnt = 1
bee = 6
result = 1
while n > cnt:
    result += 1
    cnt += bee
    bee += 6

print(result)