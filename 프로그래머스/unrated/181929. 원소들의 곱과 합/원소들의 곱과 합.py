def solution(num_list):
    sum_value = sum(num_list)
    mul_value = 1
    for i in num_list:
        mul_value *= i
    
    return 1 if sum_value ** 2 > mul_value else 0