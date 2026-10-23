def solution(n, words):
    answer = []
    word_set = set()
    for i, word in enumerate(words):
        if word not in word_set:
            word_set.add(word)
            
        else:
            return [i % n + 1, i // n + 1] 
        
        if i == 0:
            continue
            
        if words[i-1][-1] != word[0]:
            return [i % n + 1, i // n + 1]
        
    return [0, 0]