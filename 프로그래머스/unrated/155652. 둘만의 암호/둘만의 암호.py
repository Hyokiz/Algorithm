def solution(s, skip, index):
    answer = ''
    skips = set()
    for char in skip:
        skips.add(ord(char))
    
    alphabet = []
    for i in range(97, 123):
        if i not in skips:
            alphabet.append(i)

    for char in s:
        askii = ord(char)
        idx = alphabet.index(askii)
        answer += chr(alphabet[(idx + index) % len(alphabet)])
        
    return answer