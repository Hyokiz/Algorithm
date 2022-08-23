def infix_to_postfix(word):
    expression = ''
    stack = []

    for token in word:
        if token in '*/+-()':
            if not stack or token == '(':
                stack.append(token)
            elif token in '*/':
                while stack and stack[-1] in '*/':
                    expression += stack.pop()
                stack.append(token)
            elif token in '+-':
                while stack and stack[-1] != '(':
                    expression += stack.pop()
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    expression += stack.pop()
                stack.pop()
        else:
            expression += token

    while stack:
        expression += stack.pop()

    return expression


# 후위표기법 계산기
def calculate(expression):
    stack = []

    for token in expression:
        if token not in '*/+-':
            stack.append(int(token))
        else:
            x = stack.pop()
            y = stack.pop()
            if token == '+':
                stack.append(y + x)
            elif token == '-':
                stack.append(y - x)
            elif token == '*':
                stack.append(y * x)
            elif token == '/':
                stack.append(y / x)

    return stack[-1]


for t in range(1, 11):
    n = input()
    postfix_expression = infix_to_postfix(input())  # 후위표기법으로 변환
    print(f'#{t} {calculate(postfix_expression)}')  # 계산