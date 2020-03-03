# 거의 다 풀었는데 마이너한 오류 있음
from collections import Counter
import math

def solution(n, words):
    for i in range(len(words) - 1):
        if not words[i][-1] == words[i + 1][0]:
            return [(i+2)%n, math.ceil((i+2)/n)]
    
    count = Counter(words)
    s = count.most_common(1)[0]
    if s[1] > 1:
        i = [index for index, value in enumerate(words) if value == s[0]][1]
        return [n-(i+1)%n, (i+1)/n]
    
    return [0, 0]