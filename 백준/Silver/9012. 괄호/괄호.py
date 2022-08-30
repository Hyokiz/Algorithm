t = int(input())
for _ in range(t):
    arr = list(input())
    result = []
    for i in arr:
        if not result:
            result.append(i)

        elif i == '(':
            result.append(i)

        elif i == ')':

            if not result:
                print("NO")
                break

            elif result[-1] != '(':
                print("NO")
                break

            else:
                result.pop()

    else:
        if result:
            print("NO")

        else:
            print("YES")