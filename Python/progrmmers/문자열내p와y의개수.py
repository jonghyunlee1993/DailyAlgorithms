def solution(s):
    ct_p = s.count("p") + s.count("P")
    ct_y = s.count("y") + s.count("Y")
    
    if ct_p == ct_y:
        return True
    else:
        return False