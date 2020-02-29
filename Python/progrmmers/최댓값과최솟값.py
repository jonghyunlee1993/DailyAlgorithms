import numpy as np

def solution(s):
    s = np.array(list(map(int, s.split(" "))))
    return " ".join([str(np.min(s)), str(np.max(s))])