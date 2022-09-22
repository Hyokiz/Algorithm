n = int(input())
result = 0
for i in range(n//2, n+1):
    s = map(int, str(i))
    number = i + sum(s)
    
    if number == n:
        result = i
        break

print(result)