# 4153. 직각삼각형

while True:
    x, y, z = sorted(list(map(int, input().split())))

    if not x and not y and not z:
        break

    if x ** 2 + y ** 2 == z ** 2:
        print('right')
    else:
        print('wrong')

