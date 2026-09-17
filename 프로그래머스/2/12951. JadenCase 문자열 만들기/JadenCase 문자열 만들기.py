def solution(s):
    words = s.split(" ")
    return " ".join(w.capitalize() for w in words)