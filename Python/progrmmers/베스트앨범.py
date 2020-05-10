import pandas as pd

def solution(genres, plays):
    data = pd.DataFrame({"genres": genres, "plays":plays})
    data = data.sort_values(by=["genres", "plays"], axis=0, ascending=False)
    popular_genres = data.groupby(['genres']).apply(lambda x: x.plays.sum()).sort_values(ascending=False).index.to_list()
    
    answer = []
    
    for genre in popular_genres:
        genre_data = data[data['genres'] == genre].iloc[:2]
        music_index = genre_data.index.to_list()
        
        if len(genre_data) >= 2:
            if genre_data['plays'].iloc[0] == genre_data['plays'].iloc[1]:
                music_index = sorted(music_index)
        
        answer.extend(music_index)
        
    return answer