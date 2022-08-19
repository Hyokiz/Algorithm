for _ in range(int(input())):
    number = list(map(int, input().split()))
    avg = sum(number[1:]) / number[0]

    cnt = 0
    for i in number[1:]:
        if i > avg:
            cnt += 1

    result = (cnt/number[0])*100
    print('%.3f' %result + '%')