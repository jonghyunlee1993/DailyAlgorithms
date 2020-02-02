def solution(s):
    s = s.split(" ")
    res = str()
    
    for space, word in enumerate(s):
        if space != 0:
            res += " "
        
        for idx, alpha in enumerate(word):
            if idx == 0:
                res += alpha.upper()
            elif idx % 2 == 0:
                res += alpha.upper()
            else:
                res += alpha.lower()     
    
    return res