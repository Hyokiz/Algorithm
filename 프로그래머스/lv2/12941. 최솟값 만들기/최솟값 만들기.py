def solution(A,B):
    answer = 0
    n = len(A)
    A.sort()
    B.sort(reverse=True)
    for i in range(n-1, -1, -1):
        answer += A.pop() * B.pop()

    return answer