def solution(n, w, num):
    answer = 0
    idx = num - 1
    story = idx // w
    
    if story % 2 == 0:
        num_x = idx % w
    else:
        num_x = w - 1 - (idx % w)
        
    top = (n - 1) // w
    
    for i in range(story, top + 1):
        if i % 2 == 0:
            box_idx = i * w + num_x
        else:
            box_idx = i * w + (w - 1 - num_x)
        
        if box_idx < n:
            answer += 1
    
    return answer