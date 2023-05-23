# 9506. 약수들의 합
while True:
    n = int(input())
    divisor = []
    # -1이 입력되면 종료
    if n == -1:
        break

    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)

    if sum(divisor) == n:
        s = " + ".join(map(str, divisor))
        s.rstrip()
        print(f"{n} = {s}")
    else:
        print(f"{n} is NOT perfect.")