while True:
    n = int(input())
    if n == 0:
        break

    temp = str(n)
    mid = len(temp) // 2
    if len(temp) % 2 == 0:
        l = temp[0:mid]
        r = temp[mid:]

    else:
        l = temp[0:mid]
        r = temp[mid+1:]

    if l[::-1] == r:
        print('yes')
    else:
        print('no')