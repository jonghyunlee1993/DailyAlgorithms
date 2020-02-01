def solution(num):
    ct = 0
    while True:
        if num == 1:
            return ct
        elif num % 2 ==0:
            num = num / 2
            ct += 1
        else:
            num = (num * 3) + 1
            ct += 1 
    
        if num == 1:
            return ct
        elif ct >= 500:
            return -1
            
    