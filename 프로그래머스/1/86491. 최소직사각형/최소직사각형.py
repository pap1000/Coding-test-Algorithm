def solution(sizes):
    answer = 0
    widths = []
    heigths = []
    for w, h in sizes:
        if w < h:
            w, h = h, w
        widths.append(w)
        heigths.append(h)

    return max(widths)*max(heigths)