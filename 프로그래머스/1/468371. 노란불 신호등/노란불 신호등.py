import math

def solution(signals):
    answer = 0
    L1 = signals[0][0]+signals[0][1]+signals[0][2]
    lengths = [signal[0]+signal[1]+signal[2] for signal in signals]
    
    answer += signals[0][0]

    while(answer<math.lcm(*lengths)):
        for t in range(signals[0][1]): # 첫번째 신호등의 노란색 주기 동안
            for i, signal in enumerate(signals): # 모든 신호등에 대해
                if signal[0]<=(answer+t)%lengths[i]<signal[0]+signal[1]: # 해당 신호등이 노란색
                    if i == len(signals)-1:
                        return answer+t+1

                    continue
                else:
                    break
        answer += L1
                    
    return -1
    