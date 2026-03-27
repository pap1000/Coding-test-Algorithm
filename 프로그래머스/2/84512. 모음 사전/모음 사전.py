from itertools import product

def solution(word):
    answer = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    
    for i in range(1, 6):
        for w in product(vowels, repeat=i):
            dictionary.append(''.join(w))
    dictionary.sort()
    
    
    return dictionary.index(word)+1