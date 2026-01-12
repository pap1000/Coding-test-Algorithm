def solution(video_len, pos, op_start, op_end, commands):
    def calc_sec(time): # 시계열 데이터를 int로 변환 후 분리
        m, s = map(int, time.split(':'))
        return m*60 + s
    
    # 각 시점을 모두 초 단위로 변환
    total_sec = calc_sec(video_len)
    current_sec = calc_sec(pos)
    op_start_sec = calc_sec(op_start)
    op_end_sec = calc_sec(op_end)
    
    if op_start_sec <= current_sec <= op_end_sec:
        current_sec = op_end_sec
        
    for command in commands:
        if command == "prev":
            current_sec -= 10
            if current_sec < 0:
                current_sec = 0
        elif command == "next":
            current_sec += 10
            if current_sec > total_sec:
                current_sec = total_sec
        
        if op_start_sec <= current_sec <= op_end_sec:
            current_sec = op_end_sec
    
    mm = current_sec // 60
    ss = current_sec % 60
    
    return f"{mm:02d}:{ss:02d}"