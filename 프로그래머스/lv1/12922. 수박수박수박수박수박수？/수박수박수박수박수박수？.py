def solution(n):
    s = "수박" * (n // 2)
    if n % 2 == 0:
        return s
    else:
        return s + "수"