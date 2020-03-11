# 2개를 최소성이라고 가정하고 실시하였는데, 문제를 제대로 이해하지 못한 듯 함 

import pandas as pd

def solution(relation):
    answer = 0
    relation = pd.DataFrame(relation)

    for i in range(len(relation) - 2):
        if len(relation[i].unique()) == len(relation[i]):
            answer += 1
        else:
            for j in range(i + 1, len(relation) - 2):
                temp = [ii + jj for ii, jj in zip(map(str, relation[i].values.tolist()), relation[j].values.tolist())]
                
                if len(pd.Series(temp).unique()) == len(relation):
                    answer += 1
        
    return answer