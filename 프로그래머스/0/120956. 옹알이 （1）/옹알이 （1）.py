def solution(babbling):
    answer = 0
    baby_word = ['aya', 'ye', 'woo', 'ma']
    while(babbling):
        word = babbling[0]  # babbling 내 단어
        while(word):
            if word[0:2] in baby_word:
                word = word[2:]
            elif word[0:3] in baby_word:
                word = word[3:]
            else:
                break
        if len(word)==0:
            answer += 1
        del babbling[0]
                
    return answer