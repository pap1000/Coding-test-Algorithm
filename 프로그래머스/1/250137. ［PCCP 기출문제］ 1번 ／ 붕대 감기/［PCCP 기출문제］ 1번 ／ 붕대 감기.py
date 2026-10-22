def solution(bandage, health, attacks):
    t, x, y = bandage
    
    last_attack = 0
    curr_health = health
    for attack in attacks:
        print(attack)
        time, damage = attack
        duration = time - last_attack
        last_attack = time
        heal = (duration - 1) * x + ((duration - 1) // t) * y
        curr_health = min(curr_health + heal, health)
        curr_health -= damage
        if curr_health <= 0:
            return -1
        
    return curr_health