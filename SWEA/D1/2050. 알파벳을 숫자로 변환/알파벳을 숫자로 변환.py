t = list(map(str, input()))

result = []

for i in t:

    result.append(ord(i) % 64)

print(*result)