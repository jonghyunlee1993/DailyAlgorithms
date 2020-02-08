import numpy as np

def solution(n):
    center = int(np.sqrt(n))
    
    answer = []
    
    for i in range(1, center + 1):
        if i ** 2 == n:
            answer.extend([i])
        elif n % i == 0:
            answer.extend([i, n/i])

    return np.sum(answer)