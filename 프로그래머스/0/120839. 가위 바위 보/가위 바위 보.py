def solution(rsp):
    against_rsp = [5, -1, 0, -1, -1, 2]
    return "".join([str(against_rsp[int(i)]) for i in rsp])