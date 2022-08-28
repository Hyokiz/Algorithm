n = int(input())
switch = list(map(int, input().split()))
student = int(input())
for _ in range(student):
    gender, number = map(int, input().split())
    # 1. 남자일때
    if gender == 1:
        for i in range(number-1, n, number):
            if switch[i] == 0:
                switch[i] = 1
            else:
                switch[i] = 0
    # 2. 여자일때
    else:
        if switch[number-1] == 0:
            switch[number-1] = 1
        else:
            switch[number-1] = 0

        s = number - 2
        e = number
        while s >= 0 and e < n and switch[s] == switch[e]:
            if switch[s] == 0:
                switch[s] , switch[e] = 1, 1
            elif switch[s] == 1:
                switch[s], switch[e] = 0, 0
            s -= 1
            e += 1
            if s < 0 and e >= n:
                break

if n > 20:
    cnt = 0
    for i in range(n):
        print(switch[i], end=' ')
        cnt += 1
        if cnt == 20:
            print()
            cnt = 0
else:
    print(*switch)