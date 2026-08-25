def solution(message, spoiler_ranges):
    # 모든 단어의 (start, end, word) 분리
    words = []
    i = 0
    n = len(message)
    while i < n:
        if message[i] != ' ':
            start = i
            while i < n and message[i] != ' ':
                i += 1
            words.append((start, i - 1, message[start:i]))
        else:
            i += 1

    # 스포일러가 전혀 안 걸친 단어(plain_words)와 스포일러 단어 분류
    plain_words = set()
    spoiler_words = []

    for w_start, w_end, word in words:
        is_spoiled = False
        for s_start, s_end in spoiler_ranges: # 모든 스포일러 구간에 대해 단어의 포함여부 확인
            if not (w_end < s_start or w_start > s_end): # 포함되는 경우
                is_spoiled = True
                break
        
        if is_spoiled: # 스포일러 단어 등록
            spoiler_words.append(word)
        else:   # 스포일러 단어가 아닌 단어 등록
            plain_words.add(word)

    # 왼쪽부터 등장하는 스포일러 단어 중 조건에 맞는 단어 카운트
    answer = 0
    important_word = set()

    for word in spoiler_words:  # 스포일러 단어 중
        if word in plain_words: # 스포일러 구간이 아닌 구간에서 등장하지 않고
            continue
        if word not in important_word:  # 처음 등장하는 단어라면
            important_word.add(word)
            answer += 1

    return answer