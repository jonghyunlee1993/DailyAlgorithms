def solution(d, budget):
    res = 0
    answer = []
    
    for i in sorted(d, reverse=False):
        if res + i <= budget:
            res += i
            answer.extend([i])
            
    return len(answer)