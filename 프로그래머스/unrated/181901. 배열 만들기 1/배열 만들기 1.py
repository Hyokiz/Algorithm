def solution(n, k):
    return list(i * k for i in range(1, (n // k) + 1))