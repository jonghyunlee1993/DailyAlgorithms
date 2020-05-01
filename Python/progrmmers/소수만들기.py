from itertools import combinations

def is_prime(n): 
    if n < 2: 
        return False 
    if n in (2, 3): 
        return True 
    if n % 2 is 0 or n % 3 is 0: 
        return False 
    if n < 9: 
        return True
    
    k, l = 5, n**0.5 
    
    while k <= l: 
        if n % k is 0 or n % (k+2) is 0: 
            return False 
        k += 6 
    return True

def solution(nums):
    answer = 0
    comb = combinations(nums, 3)
    
    for data in comb:
        if is_prime(sum(data)):
            answer += 1
            
    return answer