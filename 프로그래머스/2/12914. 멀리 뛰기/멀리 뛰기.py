def solution(n):
    fib = [1, 1]
    for i in range(1, n):
        fib.append(fib[i] + fib[i - 1])
    
    return fib[n] % 1234567