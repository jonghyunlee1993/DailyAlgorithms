"""

1. 1번 노드에서 가장 먼 거리를 리턴하는 것이 목표
2. 따라서 1번에서 연결된 노드를 모두 방문할 수 있게 한다.
3. 처음 방문한 노드는 거리를 1로 준다. 
4. 처음 방문한 노드와 연결된 노드들을 모두 q 에 집어 넣는다.
5. 만약 현재 노드와 연결된 노드 중, 방문한 적이 없는 노드는 1을 추가한다.
6. 끝까지 갔으면 다음으로 넘어간다 ...

"""

from collections import defaultdict, deque

def solution(n, vertex):
    dists = {i:0 for i in range(1, n+1)}
    edges = defaultdict(list)

    for u, v in vertex: 
        edges[u].append(v) 
        edges[v].append(u)
    
    q = deque(edges[1])
    dist = 1
    
    while q:
        print(q)
        for i in range(len(q)): 
            v = q.popleft()

            if dists[v] == 0: 
                dists[v] = dist 
                
                for w in edges[v]: 
                    q.append(w) 
                    
        dist += 1
        
    del dists[1] 
    
    answer = 0 
    max_dist = max(dists.values()) 
    for i in dists.values(): 
        if i == max_dist: 
            answer += 1 
    
    return answer

if __name__ == '__main__':
	n = 6
	vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

	answer = solution(n, vertex)
	print(answer)
