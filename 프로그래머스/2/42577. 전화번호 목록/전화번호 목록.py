def solution(phone_book):
    phone_numbers = set(phone_book)
    for number in phone_numbers:
        for i in range(len(number)):
            if number[:i] in phone_numbers:
                return False
    return True