def solution(n):
    return sum(list(range(1, n+1, 2))) if n % 2 == 1 else sum(list(i**2 for i in range(2, n+1, 2)))