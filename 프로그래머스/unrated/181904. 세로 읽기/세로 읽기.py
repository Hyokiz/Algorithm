def solution(my_string, m, c):
    strings = [my_string[i:i+m] for i in range(0, len(my_string), m)]
    temp = [i[c-1] for i in strings]
    return "".join(temp)
