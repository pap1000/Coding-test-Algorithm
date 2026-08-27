def solution(angle):
    return 2 * (angle//90) + 1 * (angle%90>0)