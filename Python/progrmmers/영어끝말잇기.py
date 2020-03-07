# 스택으로 변경

def solution(n, words):
    prev_word = words[0]
    word_list = [prev_word]
    
    for i, word in enumerate(words[1:]):
        if word in word_list or not prev_word[-1] == word[0]:
            return [((i+1)%n)+1, ((i+1)//n)+1]
    
        word_list.append(word)
        prev_word = word

    return [0, 0]

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

