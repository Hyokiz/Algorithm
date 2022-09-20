code = {
    (2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4,
    (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7, (2, 1, 3): 8, (1, 1, 2): 9
}

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = sorted(list(set([input() for _ in range(n)])))
    arr.pop(0)
    password = []
    result = 0
    n1, n2, n3 = 0, 0, 0
    for row in arr:
        binary = ''
        for r in row:
            binary += r
        binary = binary.lstrip('0')
        odd, even = 0, 0
        temp = ''
        for idx in range(len(binary)):
            if binary[idx] == '1' and n2 == 0:
                n1 += 1
            elif binary[idx] == '0' and n1 != 0 and n3 == 0:
                n2 += 1
            elif binary[idx] == '1' and n2 != 0:
                n3 += 1
            elif binary[idx] == '0' and n3 != 0:
                temp += str(code[n1, n2, n3])
                n1, n2, n3 = 0, 0, 0

                if len(temp) == 8:

                    for i in range(len(temp)):
                        if i%2 == 0:
                            odd += int(temp[i])
                        else:
                            even += int(temp[i])

                    if (odd * 3 + even) % 10 == 0 and temp not in password:
                        password.append(temp)
                        result += odd + even
                    odd, even = 0, 0
                    temp = ''

    print(f'#{t} {result}')

