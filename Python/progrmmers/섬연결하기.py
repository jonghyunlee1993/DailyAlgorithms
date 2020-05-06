'''
kruskal 알고리즘을 이용한다
탐욕적인 방법으로 그래프의 모든 정점을 최소 비용으로 연결하는 방법
처음 시작하는 노드에서 하나의 간선을 선택
connecte list에서 시작하는 하나의 다른 간선을 선택하는데, 이때의 비용 역시 최소
모든 노드가 연결되면 정지
'''

import numpy as np

def solution(n, costs):
    costs = sorted(costs)
    connected = set([costs[0][0]])
    answer = 0
    
    while len(connected) != n:
        min_cost = np.inf
        min_idx  = 0
        
        for i in range(len(costs)):
            if costs[i][0] in connected or costs[i][1] in connected:
                if costs[i][0] in connected and costs[i][1] in connected:
                    continue
                
                if min_cost > costs[i][2]:
                    min_cost = costs[i][2]
                    min_idx  = i
            
        answer += min_cost
        connected.add(costs[min_idx][0])
        connected.add(costs[min_idx][1])
        costs.pop(min_idx)
    
    return answer


# 처음 생각한 방법
# 단순히 최저 비용을 계속 고르면 될 것이라고 생각했다

def solution(n, costs):
    costs = sorted(costs, key = lambda x: x[2])
    answer = 0
    connected = set()
    
    for i, j, k in costs:        
        print(f"{[i, j]} connected: {connected} costs: {answer}")
        
        connected.add(i)
        connected.add(j)
        answer += k
        
        if len(connected) == n:
            print(connected)
            return answer
    