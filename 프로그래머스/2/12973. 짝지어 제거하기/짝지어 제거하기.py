def solution(s):
    stack = []
    
    for c in s:
        if not stack:
            stack.append(c)
        else:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
                
    return 1 if not stack else 0