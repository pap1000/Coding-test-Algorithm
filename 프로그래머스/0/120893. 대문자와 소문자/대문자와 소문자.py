def solution(my_string):
    answer = ''
    for c in my_string:
        if 65 <= ord(c) <= 90:
            answer += chr(ord(c)+32)
        elif 97 <= ord(c) <= 122:
            answer += chr(ord(c)-32)
    return answer