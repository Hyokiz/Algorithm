def solution(picture, k):
    answer = []
    for s in picture:
        for _ in range(k):
            answer.append(s.replace(".", "." * k).replace("x", "x" * k))
    return answer