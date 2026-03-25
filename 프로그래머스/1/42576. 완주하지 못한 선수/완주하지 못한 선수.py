def solution(participant, completion):
    participant_dict = {}
    for name in participant:
        participant_dict[name] = participant_dict.get(name, 0) + 1
    for name in completion:
        participant_dict[name] -= 1
    
    for name, count in participant_dict.items():
        if count > 0:
            return name
