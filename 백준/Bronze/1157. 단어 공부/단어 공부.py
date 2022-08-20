word = input().upper()
set_word = list(set(word))      # 같은 글자 줄이기

li  = []
# 빈도수를 li에 배치
for i in set_word:
    cnt = word.count(i)
    li.append(cnt)
# max인 값이 2개 이상인 경우 ? 출력
if li.count(max(li)) > 1:
    print('?')
# 아니면 문자 출력
else:
    print(set_word[li.index(max(li))])