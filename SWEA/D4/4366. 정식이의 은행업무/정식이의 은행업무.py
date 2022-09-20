for t in range(1, int(input()) + 1):
    num1 = input()
    num2 = input()
    number1, number2 = [], []

    for i1 in range(1, len(num1)):
        for j1 in range(2):
            bit1 = num1[:i1] + str(j1) + num1[i1+1:]
            if bit1 != num1:
                number1.append(bit1)

    for i2 in range(len(num2)):
        for j2 in range(3):
            bit2 = num2[:i2] + str(j2) + num2[i2+1:]
            if bit2 != num2:
                number2.append(bit2)

    for i in range(len(number1)):
        for j in range(len(number2)):
            ans1 = int(number1[i], 2)
            ans2 = int(number2[j], 3)
            if ans1 == ans2:
                print(f'#{t} {ans1}')
