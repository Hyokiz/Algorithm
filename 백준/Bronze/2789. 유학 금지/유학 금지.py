text = "CAMBRIDGE"
t = input()
# text 와 input 비교
for i in text:
    for j in t:
        if i == j:
            t = t.replace(j, '') # 같다면 빈칸으로 대체

print(t)