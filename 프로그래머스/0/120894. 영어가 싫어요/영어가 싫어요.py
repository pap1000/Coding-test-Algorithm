def solution(numbers):
    answer = ""
    str_to_int = {'zero': '0','one': '1','two': '2','three': '3','four': '4','five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    number = ""
    for s in numbers:
        number+=s
        if number in str_to_int:
            answer += str_to_int[number]
            number = ""
    return int(answer)