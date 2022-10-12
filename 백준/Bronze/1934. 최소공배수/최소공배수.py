# 1934. 최소공배수

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    ans = 0
    if a > b:
        for i in range(1, b + 1):
            if (a * i) % b == 0:
                ans = a * i
                break

    elif a < b:
        for i in range(1, a + 1):
            if (b * i) % a == 0:
                ans = b * i
                break

    else:
        ans = a

    print(ans)