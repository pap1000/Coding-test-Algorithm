def solution(genres, plays):
    answer = []
    count_genres = {}
    # 장르별 총 재생 횟수 집계 후 정렬
    for i, genre in enumerate(genres):
        count_genres[genre] = count_genres.get(genre, 0) + plays[i]
    count_genres = sorted(count_genres, key=lambda x:count_genres[x], reverse=True)
    
    # 장르별 노래 리스트 생성 후 정렬
    genre_songs = {}
    for i in range(len(genres)):
        if genres[i] not in genre_songs:
            genre_songs[genres[i]] = []
        genre_songs[genres[i]].append((i, plays[i]))
        
    for genre in count_genres:
        genre_songs[genre].sort(key=lambda x: (-x[1], x[0]))
    
    # 각 장르별 노래 2곡 선정
    for genre in count_genres:
        count = 0
        for i, _ in genre_songs[genre]:
            if count==2:
                break
            answer.append(i)
            count+=1
    return answer