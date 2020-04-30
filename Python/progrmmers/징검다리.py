# 이분탐색법

def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance

    answer = 0
    
    while left <= right:
        prev = 0
        mins = distance
        removed_rocks = 0
        
        mid = (left + right) // 2

        for i in range(len(rocks)):
            if rocks[i] - prev < mid:
                removed_rocks += 1
            else:
                mins = min(mins, rocks[i] - prev)
                prev = rocks[i]
        
        if removed_rocks > n:
            right = mid - 1
        else:
            answer = mins
            left = mid + 1
            
    return answer

# 시간이 많이 걸리는 방법

import numpy as np
from itertools import combinations

def solution(distance, rocks, n):
    remain_rocks = combinations(rocks, len(rocks) - n)
    answer = 0
    
    for trial in remain_rocks:
        trial = list(trial)
        trial.insert(0, 0)
        trial.append(distance)
        
        array = np.array(sorted(trial))
        comp = np.min(np.diff(array))
        
        if comp > answer:
            answer = comp
            
    return answer