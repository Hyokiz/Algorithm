t = int(input())

for tc in range(1, t+1):
    day = input()
    year = int(day[0:4])
    month = int(day[4:6])
    date = int(day[6:8])

    if month < 1 or month > 12:
        print(f'#{tc} -1')
        continue

    if month in [1, 3, 5, 7, 8, 10, 12]:
        if date < 1 or date > 31:
            print(f'#{tc} -1')
            continue

    if month in [4, 6, 9, 11]:
        if date < 1 or date > 30:
            print(f'#{tc} -1')
            continue

    if month == 2:
        if date < 1 or date > 28:
            print(f'#{tc} -1')
            continue

    print(f"#{tc} %04d/%02d/%02d" %(year, month, date))