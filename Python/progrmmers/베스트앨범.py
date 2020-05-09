# pandas를 이용해서 풀고 싶으나
# 런타임 오류가 발생하는 문제가 있음

import pandas as pd

def solution(genres, plays):
    data = pd.DataFrame({"genres": genres, "plays":plays})
    data = data.sort_values(by=["plays", "genres"], axis=0, ascending=False)
    
    answer = []
    
    for genre in pd.unique(data['genres'].to_list()):
        genre_data = data[data['genres'] == genre].iloc[:2]
        music_index = genre_data.index.to_list()
        
        if genre_data['plays'].iloc[0] == genre_data['plays'].iloc[1]:
            music_index = sorted(music_index)
        
        answer.extend(music_index)
        
    return answer