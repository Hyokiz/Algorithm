for t in range(1, int(input()) + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    result = -1
    # 1. 먼저 모든 수의 곱을 구한다.
    for i in range(n-1):
        for j in range(i+1, n):
            # 숫자간 비교를 위해 number 변수에 문자열로 할당한다.
            number = str(numbers[i] * numbers[j])
            for k in range(len(number) - 1):
                if number[k] > number[k+1]:
                    break
            # 반복문이 무사히 종료될 경우 max 값을 넣어준다.
            else:
                if result < int(number):
                    result = int(number)

    print(f'#{t} {result}')