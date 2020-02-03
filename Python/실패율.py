import numpy as np

def solution(N, stages):
    rate = {}
    
    for stage in range(1, N + 1):
        passer = np.sum(np.array(stages) > stage)
        challenger = np.sum(np.array(stages) == stage)
        rate[stage] = challenger / passer
    
    return [item[0] for item in sorted(rate.items(), key=lambda x: x[1], reverse=True)]