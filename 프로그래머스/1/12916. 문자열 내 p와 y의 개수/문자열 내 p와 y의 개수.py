def solution(s):
    answer = True
    pn = 0
    yn = 0
    
    for c in s.lower():
        if c == "p":
            pn += 1
        elif c == "y":
            yn += 1

    return True if pn == yn else False