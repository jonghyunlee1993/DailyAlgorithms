def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices)-1):
        for ct, j in enumerate(range(i + 1, len(prices))):
            if prices[i] > prices[j]:
                break
        answer[i] = ct + 1

    return answer