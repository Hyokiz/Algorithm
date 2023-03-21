# from itertools import permutations
# def solution(babbling):
#     answer = 0
#     speek = ["aya","ye","woo","ma"]
#     word = set()
#     for i in range(1, len(speek)+1):
#         for j in permutations(speek, i):
#             word.add(''.join(j))

#     for i in babbling:
#         if i in word:
#             answer += 1

#     return answer

def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in words:
            if not i * 2 in babbling:
                i = i.replace(j, " ")
                print(i)
        if len(i.strip()) == 0:
            answer += 1
    
    return answer