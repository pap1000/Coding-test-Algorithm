def solution(my_string):
    answer = 0
    buffer = ""
    for c in my_string:
        if c.isdigit():
            buffer += c
        elif buffer != "":
            answer += int(buffer)
            buffer = ""
    if buffer != "":
        answer += int(buffer)
        
    return answer