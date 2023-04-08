while True:
    x, y, z = map(int, input().split())
    li = [x, y, z]
    li.sort()
    # 종료 조건
    if x == y == z == 0:
        break

    # 1-1. 삼각형의 조건을 만족하지 못할 경우
    if li[2] >= li[0] + li[1]:
        print("Invalid")
    # 1-2. 만족할 경우
    else:
        # 세 변의 길이가 같은 경우
        if x == y == z:
            print("Equilateral")
        # 두 변의 길이만 같은 경우
        elif x == y or y == z or z == x:
            print("Isosceles")
        # 세 변의 길이가 모두 다른 경우
        else:
            print("Scalene")