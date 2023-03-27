def solution(my_string):
    my_string = "".join([word if word.isnumeric() else ' ' for word in list(my_string)])
    
    number_list = list(map(int, my_string.split()))
    
    return sum(number_list)