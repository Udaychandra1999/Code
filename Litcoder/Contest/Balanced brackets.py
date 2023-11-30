def is_balanced(s):
    stack = []
    for c in s:
        if c in ['(', '[', '{']:
            stack.append(c)
        elif c == ')':
            if not stack or stack[-1] != '(':
                return "NO"
            stack.pop()
        elif c == ']':
            if not stack or stack[-1] != '[':
                return "NO"
            stack.pop()
        elif c == '}':
            if not stack or stack[-1] != '{':
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

input_str = input().strip()
expressions = input_str.split(',')
for expr in expressions:
    print(is_balanced(expr))