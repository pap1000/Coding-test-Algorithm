def solution(price):
    return int(price if price < 100000 else(price*0.95 if 100000 <= price < 300000 else(price*0.9 if 300000 <= price < 500000 else price*0.8)))