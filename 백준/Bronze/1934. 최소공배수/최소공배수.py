import math

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    ans = math.lcm(a, b)
    
    print(ans)