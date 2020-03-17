# 이분탐색 알고리즘 도입해서 효율성 테스트 성공

def solution(budgets, M):
    answer = 0
    min_val, max_val = 0, max(budgets)
    
    while min_val <= max_val:
        mid_val = (min_val + max_val) // 2
        temp = [i if i < mid_val else mid_val for i in budgets]
        
        if sum(temp) > M:
            max_val = mid_val - 1
        else:
            answer = mid_val
            min_val = mid_val + 1
        
    return answer

# 효율성 테스트 2개 실패

import numpy as np

def solution(budgets, M):
    budgets = np.array(budgets)
    
    if np.sum(budgets) <= M:
        return np.max(budgets)
    else:
        minimum = np.ceil(M / len(budgets))
        while True:
            temp = budgets.copy()
            temp[temp > minimum] = minimum
            
            if np.sum(temp) < M:
                minimum += 1
            else:
                return minimum - 1