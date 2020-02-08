def is_prime(n):
    if n < 2: 
        return False 
    if n is 2: 
        return True 
    if n % 2 is 0: 
        return False 
    
    l = round(n ** 0.5) + 1 
    
    for i in range(3, l, 2): 
        if n % i is 0: 
            return False 
            
    return True

def solution(n):
    ct = 0
    
    for i in range(n + 1):
        if is_prime(i):
            ct += 1
    
    return ctㅑㅐ