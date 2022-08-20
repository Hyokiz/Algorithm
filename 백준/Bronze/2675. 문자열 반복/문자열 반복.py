for t in range(int(input())):
    r, s = input().split()
    
    result = ''
    for i in s:
        result += i * int(r)
    
    print(result)