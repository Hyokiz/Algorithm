# 13229. 일요일

days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
for t in range(1, int(input()) + 1):
    s = input()
    ans = 7 - days.index(s)
    print(f'#{t}', ans)