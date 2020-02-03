import numpy as np

def solution(N, stages):
    rate = {}
    
    for stage in range(1, N + 1):
        passer = np.sum(np.array(stages) > stage)
        challenger = np.sum(np.array(stages) == stage)
        rate[stage] = challenger / passer
    
    return sorted(rate, key=lambda x: rate[x], reverse=True)