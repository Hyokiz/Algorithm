# 4613. 러시아 국기 같은 깃발

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    new_arr = []
    ans = []
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            a = arr[:i+1][:]
            b = arr[i+1:j+1][:]
            c = arr[j+1:][:]

            cnt_a = (x.count('W') for x in a)
            cnt_b = (y.count('B') for y in b)
            cnt_c = (z.count('R') for z in c)

            result_a = len(a) * m - sum(cnt_a)
            result_b = len(b) * m - sum(cnt_b)
            result_c = len(c) * m - sum(cnt_c)

            ans.append(result_a + result_b + result_c)

    print(f'#{t}', min(ans))



