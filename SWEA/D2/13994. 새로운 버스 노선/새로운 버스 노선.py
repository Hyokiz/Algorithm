for tc in range(1, int(input())+1):
    no_sun = int(input())
    arr = [0] * 1001
    for _ in range(no_sun):

        x, a, b = map(int, input().split())

        if x == 1:
            for i in range(a, b + 1):
                arr[i] += 1

        elif x == 2:
            for i in range(a, b + 1, 2):
                arr[i] += 1

        else:
            for i in range(a, b + 1):
                if a % 2 == 1 and (i % 3 == 0 and i % 10 != 0):
                    arr[i] += 1

                elif a % 2 == 0 and i % 4 == 0:
                    arr[i] += 1




    print('#{} {}'.format(tc, max(arr)))