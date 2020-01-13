def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    answer = list(answer.keys())[0]
    return answer

from collections import Counter
import sys

part = sys.stdin.readline()
comp = sys.stdin.readline()

print(part, comp)