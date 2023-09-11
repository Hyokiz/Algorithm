def solution(arr, delete_list):
    answer = []
    delete_list = set(delete_list)
    for i in arr:
        if i in delete_list:
            continue
        else:
            answer.append(i)
    return answer