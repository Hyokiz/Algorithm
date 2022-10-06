# 14555. 공과 잡초

for t in range(1, int(input()) + 1):
    s = list(input())
    result = 0
    breaker = True
    for i in s:
        if i == '(':
            result += 1
            breaker = False

        elif i == ')':
            result += 1
            if breaker:
                continue
            else:
                result -= 1
                breaker = True
        else:
            breaker = True

    print(f'#{t}', result)