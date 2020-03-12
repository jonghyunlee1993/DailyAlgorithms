# 비트 연산자 &를 이용해서 최소성 체크가 핵심

import pandas as pd
from itertools import combinations

def solution(relation):
    answer = []
    df = pd.DataFrame(relation)
    
    for i in range(1, len(df.columns) + 1):
        candidates = list(combinations(set(df.columns), i))

        for columns in candidates:
            temp = df[list(columns)].apply("".join, axis=1).unique()
            
            if len(temp) == len(df):
                is_exist = False
                
                for check in answer:
                    if check & set(list(columns)) == check:
                        is_exist = True
                        break

                if is_exist == False:
                    answer.append(set(list(columns)))
                    
    return len(answer)

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