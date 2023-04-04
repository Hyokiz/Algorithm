# def solution(s):
#     answer = ""
#     words = s.split(" ")
#     print(ord("0")) # 48
#     print(ord("9")) # 57
#     for i in range(len(words)):
#         if 48 <= ord(words[i][0]) <= 57:
#             continue
#         else:
#             words[i] = words[i].capitalize()
#     answer = " ".join(words)
    
#     return answer
def solution(s):
    return " ".join([word.capitalize() for word in s.split(" ")])

