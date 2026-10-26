def solution(park, routes):
    answer = []
    n = len(park)
    m = len(park[0])
    print(n , m)
    
    for r, p in enumerate(park):
        for c, s in enumerate(p):
            if s == "S":
                curr = [r, c]
                break
    
    for route in routes:
        print(curr)
        way, dist = route.split()
        print(way, dist)
        dist = int(dist)
        if way == "E" and curr[1] + dist < m:
            if "X" not in park[curr[0]][curr[1]:curr[1]+dist+1]:
                curr[1] += dist
            
        elif way == "W" and curr[1] - dist >= 0:
            if "X" not in park[curr[0]][curr[1]-dist:curr[1]+1]:        
                curr[1] -= dist
            
        elif way == "S" and curr[0] + dist < n:
            if "X" not in [park[i][curr[1]] for i in range(curr[0], curr[0]+dist+1)]:
                curr[0] += dist
            
        elif way == "N" and curr[0] - dist >= 0:
            if "X" not in [park[i][curr[1]] for i in range(curr[0]-dist, curr[0])]:
                curr[0] -= dist
            
        else:
            continue
            
    return curr