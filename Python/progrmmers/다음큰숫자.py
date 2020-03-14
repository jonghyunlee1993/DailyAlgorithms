def solution(n):
    b = format(n, 'b')
    comp = n + 1
    
    while True:
        cb = format(comp, 'b')
        
        if cb.count("1") == b.count("1"):
            return comp
        
        comp += 1
        