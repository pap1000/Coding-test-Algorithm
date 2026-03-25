def solution(genres, plays):
    answer = []
    count_genres = {}
    # 장르별 재생 횟수 집계 후 정렬
    for i, genre in enumerate(genres):
        count_genres[genre] = count_genres.get(genre, 0) + plays[i]
    count_genres = sorted(count_genres, key=lambda x:count_genres[x], reverse=True)
    
    # 노래를 재생 횟수 순으로 정렬
    songs = {}
    for id, play in enumerate(plays):
        songs[id] = play
    songs = sorted(songs, key=lambda x:songs[x], reverse=True)
    
    # 각 장르별 노래 2곡 선정
    for genre in count_genres:
        count = 0
        for id in songs:
            if count==2:
                break
            if genres[id]==genre:
                answer.append(id)
                count+=1
    return answer