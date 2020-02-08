def solution(a, b):
    
    if a > b:
        a,b = b,a
    
    item = [item for item in range(int(a), int(b) + 1)]

    return np.array(item).sum()