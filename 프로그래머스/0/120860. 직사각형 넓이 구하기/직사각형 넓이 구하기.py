def solution(dots):
    answer = 0
    x_dots = [dot[0] for dot in dots]
    y_dots = [dot[1] for dot in dots]
    
    return (max(x_dots) - min(x_dots)) * (max(y_dots) - min(y_dots))