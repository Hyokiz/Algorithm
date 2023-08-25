def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        res = ""
        a = bin(arr1[i])[2:]
        b = bin(arr2[i])[2:]
        a = "0" * (n - len(a)) + a
        b = "0" * (n - len(b)) + b
        
        for j in range(len(a)):
            if a[j] == "1" or b[j] == "1":
                res += "#"
            else:
                res += " "
        answer.append(res)
            
    return answer
        