import numpy as np

def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        arr = np.array(arr)
        return np.delete(arr, np.argmin(arr)).tolist()