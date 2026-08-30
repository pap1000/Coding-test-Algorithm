from collections import Counter

def solution(spell, dic):
    s_length = len(spell)
    
    for word in dic:
        word_counter = Counter(word)
        w_length = len(word)
        
        if w_length != s_length:
            continue
        
        for i, c in enumerate(spell):
            if word_counter[c] == 1:
                if i == s_length-1:
                    return 1
                continue
            elif word_counter[c] != 1:
                break
            
    return 2