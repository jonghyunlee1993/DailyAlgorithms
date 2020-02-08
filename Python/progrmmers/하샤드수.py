import numpy as np

def solution(x):
    if x % np.sum([int(item) for item in str(x)]) == 0:
        return True
    else:
        return False