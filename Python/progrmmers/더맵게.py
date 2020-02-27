
# 모범 답안
# heapq를 이용하면 우선순위 정렬을 할 수 있음. 이를 이용해 sort에 시간을 절약함
import heapq

def solution(scoville, K):
    heap = []
    
    for num in scoville:
        heapq.heappush(heap, num)
    
    count = 0
    
    while heap[0] < K:
        if len(heap) < 2:
            return -1
        
        heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        count += 1
        
    return count

# 효율성 실패, 개념 자체는 맞음
def solution(scoville, K):
    count = 0
    while min(scoville) < K:
        if len(scoville) < 2:
            return -1
        
        scoville = sorted(scoville)
        
        s1 = scoville.pop(0)
        s2 = scoville.pop(0)
        
        scoville.append(s1 + s2*2)
        count += 1
        
    return count
    