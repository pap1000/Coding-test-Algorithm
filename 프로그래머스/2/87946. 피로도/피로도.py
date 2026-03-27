import itertools

def solution(k, dungeons):
    answer = -1
    dungeons_index = [i for i in range(len(dungeons))]
    for p in itertools.permutations(dungeons_index, len(dungeons)):  # 길이에 따른 던전 순열
        curr_stamina = k  # 현재 피로도
        count_clear = 0  # 클리어한 횟수
        #print(p)
        for dungeon_index in p:  # 순서에 따라 던전 탐색
            if curr_stamina>=dungeons[dungeon_index][0]:  # 최소 피로도 충족 시
                curr_stamina -= dungeons[dungeon_index][1]
                count_clear += 1
                if answer < count_clear:  # 현재까지 클리어 횟수가 기존 클리어 횟수보다 크면 갱신
                    answer = count_clear
            else:  # 최소 피로도 불충족 시
                if answer < count_clear:  # 현재까지 클리어 횟수가 기존 클리어 횟수보다 크면 갱신
                    answer = count_clear
                break
    return answer