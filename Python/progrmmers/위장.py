from collections import Counter

def solution(clothes):
    count = Counter(dict(clothes).values())
    
    for i, j in enumerate(count.keys()):
        if i == 0:
            ct = count[j] + 1
        else:
            ct *= count[j] + 1
            
    return ct - 1