def solution(s):
    answer = 0
    number = s
    num_dict = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, 
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
               }
    
    while number:
        if number[0].isdigit():
                answer = answer * 10 + int(number[0])
                number = number[1:]
                continue
                
        for i in range(len(number)):
            if number[:i+1] in num_dict:
                answer = answer * 10 + num_dict[number[:i+1]]
                number = number[i+1:]
                break    
        
    return answer