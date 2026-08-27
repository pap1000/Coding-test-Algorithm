def solution(array, commands):
    answer = []
    for command in commands:
        cutting = sorted(array[command[0]-1:command[1]])
        answer.append(cutting[command[2]-1])
        
    return answer