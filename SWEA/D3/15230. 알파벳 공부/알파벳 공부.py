# 15230. 알파벳 공부
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for t in range(1, int(input()) + 1):
    s = list(input())
    alpha = list(alphabet)
    breaker = True
    cnt = 0
    for k, l in enumerate(s):
        for i, j in enumerate(alpha):
            if j == l:
                if i == k:
                    cnt += 1
                else:
                    breaker = False
                    break

        if not breaker:
            break

    print(f'#{t}', cnt)
