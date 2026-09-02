from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_queue = deque(truck_weights)
    on_bridge = deque()
    curr_w = 0

    while truck_queue or on_bridge:
        answer += 1
        if on_bridge:
            if answer - on_bridge[0][1] == bridge_length:
                curr_w -= on_bridge.popleft()[0]
        if truck_queue:
            if truck_queue[0] + curr_w <= weight:
                fore_truck = truck_queue.popleft()
                on_bridge.append((fore_truck, answer))
                curr_w += fore_truck
        
    return answer