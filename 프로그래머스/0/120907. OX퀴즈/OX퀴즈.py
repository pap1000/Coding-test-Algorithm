def solution(quiz):
    answer = []
    ops = {
        "+" : lambda a, b : a + b,
        "-" : lambda a, b : a - b
    }
    
    for q in quiz:
        x, op, y, _, z = q.split()
        answer.append("O" if ops[op](int(x), int(y)) == int(z) else "X")
            
    return answer