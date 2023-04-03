def solution(x):
    y = sum(list(map(int, str(x))))
    if x % y:
        return False
    else:
        return True