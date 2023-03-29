def solution(sides):
    answer = 0
    first_case = max(sides)
    second_case = sum(sides)
    
    # 첫번째 경우
    for i in range(first_case - min(sides) + 1, first_case + 1):
        answer += 1
    
    # 두번째 경우
    for j in range(first_case + 1, second_case):
        answer += 1
    return answer