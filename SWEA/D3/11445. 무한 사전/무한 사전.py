for t in range(1, int(input()) + 1):
    p = input().strip()
    q = input().strip()

    p_len = len(p)
    if p == q[:p_len] and q[p_len:] == 'a':
        print(f'#{t} N')
    else:
        print(f'#{t} Y')
